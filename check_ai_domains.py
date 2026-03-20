#!/usr/bin/env python3
"""
GoDaddy .ai Domain Availability Checker

Checks every single-word .ai domain against GoDaddy's API and writes results
to CSV files (available.csv, taken.csv, all_results.csv).

Usage:
    # Using GoDaddy API (production - requires 50+ domains on account):
    python3 check_ai_domains.py --api-key YOUR_KEY --api-secret YOUR_SECRET

    # Using GoDaddy OTE (sandbox/test - free, may have stale data):
    python3 check_ai_domains.py --api-key YOUR_OTE_KEY --api-secret YOUR_OTE_SECRET --ote

    # Using GoDaddy website scraping (no API key needed, slower):
    python3 check_ai_domains.py --scrape

    # Filter by word length:
    python3 check_ai_domains.py --scrape --max-length 6

    # Resume from where you left off:
    python3 check_ai_domains.py --scrape --resume

Get API keys at: https://developer.godaddy.com/keys
"""

import argparse
import csv
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Install with: pip3 install requests")
    sys.exit(1)


SCRIPT_DIR = Path(__file__).parent
WORDLIST_FILE = SCRIPT_DIR / "wordlist.txt"
RESULTS_DIR = SCRIPT_DIR / "results"
AVAILABLE_CSV = RESULTS_DIR / "available.csv"
TAKEN_CSV = RESULTS_DIR / "taken.csv"
ALL_RESULTS_CSV = RESULTS_DIR / "all_results.csv"
PROGRESS_FILE = RESULTS_DIR / "progress.json"

GODADDY_PROD_URL = "https://api.godaddy.com/v1/domains/available"
GODADDY_OTE_URL = "https://api.ote-godaddy.com/v1/domains/available"
GODADDY_SEARCH_URL = "https://find.godaddy.com/domainsapi/v1/search/exact"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
]


def load_wordlist(filepath, min_length=1, max_length=None):
    """Load words from the wordlist file."""
    words = []
    with open(filepath, "r") as f:
        for line in f:
            word = line.strip().lower()
            if not word or not word.isalpha():
                continue
            if len(word) < min_length:
                continue
            if max_length and len(word) > max_length:
                continue
            words.append(word)
    return sorted(set(words))


def load_progress():
    """Load progress from previous run."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"checked": [], "last_word": None, "timestamp": None}


def save_progress(checked_words, last_word):
    """Save progress for resume capability."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    progress = {
        "checked": checked_words,
        "last_word": last_word,
        "timestamp": datetime.now().isoformat(),
        "total_checked": len(checked_words),
    }
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)


def write_result(filepath, domain, word, available, price=None, currency=None):
    """Append a single result to a CSV file."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    file_exists = filepath.exists()
    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["domain", "word", "available", "price", "currency", "checked_at"])
        writer.writerow([domain, word, available, price or "", currency or "", datetime.now().isoformat()])


def check_domain_api(word, api_key, api_secret, ote=False):
    """Check domain availability via GoDaddy API."""
    domain = f"{word}.ai"
    url = GODADDY_OTE_URL if ote else GODADDY_PROD_URL
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Accept": "application/json",
    }
    params = {"domain": domain, "checkType": "FAST", "forTransfer": "false"}

    for attempt in range(4):
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "word": word,
                    "domain": domain,
                    "available": data.get("available", False),
                    "price": data.get("price", None),
                    "currency": data.get("currency", None),
                }
            elif resp.status_code == 429:
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"  Rate limited on {domain}, waiting {wait:.1f}s...")
                time.sleep(wait)
                continue
            elif resp.status_code == 401:
                print(f"  AUTH ERROR: Invalid API key/secret. Check your credentials.")
                return {"word": word, "domain": domain, "available": None, "error": "auth_failed"}
            elif resp.status_code == 403:
                print(f"  ACCESS DENIED: Your account may not meet GoDaddy's API requirements (50+ domains).")
                return {"word": word, "domain": domain, "available": None, "error": "access_denied"}
            else:
                print(f"  HTTP {resp.status_code} for {domain}: {resp.text[:200]}")
                wait = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait)
        except requests.exceptions.RequestException as e:
            wait = (2 ** attempt) + random.uniform(0, 1)
            print(f"  Network error for {domain}: {e}, retrying in {wait:.1f}s...")
            time.sleep(wait)

    return {"word": word, "domain": domain, "available": None, "error": "max_retries"}


def check_domain_scrape(word, session=None):
    """Check domain availability by scraping GoDaddy's search page."""
    domain = f"{word}.ai"
    if session is None:
        session = requests.Session()

    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.godaddy.com/domainsearch/find",
        "Origin": "https://www.godaddy.com",
    }

    # Try the domain search API endpoint
    urls_to_try = [
        f"https://find.godaddy.com/domainsapi/v1/search/exact?key=dpp_search&q={domain}",
        f"https://www.godaddy.com/domainfind/v1/search/exact?key=dpp_search&q={domain}",
    ]

    for url in urls_to_try:
        for attempt in range(3):
            try:
                resp = session.get(url, headers=headers, timeout=20)
                if resp.status_code == 200:
                    data = resp.json()
                    # Parse the response - structure varies
                    if isinstance(data, dict):
                        products = data.get("Products", data.get("products", []))
                        exact = data.get("ExactMatchDomain", data.get("exactMatchDomain", {}))
                        if exact:
                            avail = exact.get("IsAvailable", exact.get("isAvailable", False))
                            price_info = exact.get("PriceInfo", exact.get("priceInfo", {}))
                            price = price_info.get("CurrentPrice", price_info.get("currentPrice")) if price_info else None
                            return {
                                "word": word,
                                "domain": domain,
                                "available": avail,
                                "price": price,
                                "currency": "USD",
                            }
                        # Fallback: look in products list
                        for p in products:
                            if p.get("Fqdn", p.get("fqdn", "")).lower() == domain.lower():
                                return {
                                    "word": word,
                                    "domain": domain,
                                    "available": p.get("IsAvailable", p.get("isAvailable", False)),
                                    "price": p.get("PriceInfo", {}).get("CurrentPrice"),
                                    "currency": "USD",
                                }
                    return {"word": word, "domain": domain, "available": None, "error": "parse_error"}
                elif resp.status_code == 429:
                    wait = (3 ** attempt) + random.uniform(1, 3)
                    print(f"  Rate limited on {domain}, waiting {wait:.1f}s...")
                    time.sleep(wait)
                    continue
                else:
                    break  # Try next URL
            except requests.exceptions.RequestException as e:
                wait = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait)

    # Fallback: use whois-style check
    return check_domain_dns(word)


def check_domain_dns(word):
    """Fallback: check if domain resolves via DNS (taken domains usually resolve)."""
    import socket
    domain = f"{word}.ai"
    try:
        socket.setdefaulttimeout(5)
        socket.getaddrinfo(domain, None)
        # Domain resolves - likely taken
        return {"word": word, "domain": domain, "available": False, "price": None, "currency": None, "method": "dns"}
    except socket.gaierror:
        # Domain doesn't resolve - might be available (or just not configured)
        return {"word": word, "domain": domain, "available": "unknown_dns", "price": None, "currency": None, "method": "dns"}
    except Exception:
        return {"word": word, "domain": domain, "available": None, "error": "dns_error"}


def check_domain_whois(word):
    """Check domain via WHOIS lookup."""
    domain = f"{word}.ai"
    try:
        import subprocess
        result = subprocess.run(
            ["whois", domain],
            capture_output=True, text=True, timeout=15
        )
        output = result.stdout.lower()
        if "no match" in output or "not found" in output or "no data found" in output:
            return {"word": word, "domain": domain, "available": True, "method": "whois"}
        elif "domain name:" in output or "registrant" in output or "creation date" in output:
            return {"word": word, "domain": domain, "available": False, "method": "whois"}
        else:
            return {"word": word, "domain": domain, "available": "unknown", "method": "whois"}
    except FileNotFoundError:
        return {"word": word, "domain": domain, "available": None, "error": "whois_not_installed"}
    except subprocess.TimeoutExpired:
        return {"word": word, "domain": domain, "available": None, "error": "whois_timeout"}
    except Exception as e:
        return {"word": word, "domain": domain, "available": None, "error": str(e)}


def run_checks(words, check_fn, workers=1, delay=1.0, resume=False):
    """Run domain checks across all words."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Handle resume
    checked_set = set()
    if resume:
        progress = load_progress()
        checked_set = set(progress.get("checked", []))
        if checked_set:
            print(f"Resuming: {len(checked_set)} words already checked, skipping them.")
        words = [w for w in words if w not in checked_set]

    total = len(words)
    available_count = 0
    taken_count = 0
    error_count = 0

    print(f"\nChecking {total} domains...")
    print(f"Results will be saved to: {RESULTS_DIR}/")
    print(f"  - available.csv: Available domains")
    print(f"  - taken.csv: Taken domains")
    print(f"  - all_results.csv: All results")
    print(f"  - progress.json: Resume checkpoint")
    print()

    session = requests.Session()
    start_time = time.time()

    for i, word in enumerate(words):
        try:
            if hasattr(check_fn, '__name__') and 'scrape' in check_fn.__name__:
                result = check_fn(word, session=session)
            else:
                result = check_fn(word)
        except Exception as e:
            result = {"word": word, "domain": f"{word}.ai", "available": None, "error": str(e)}

        domain = result["domain"]
        avail = result.get("available")
        price = result.get("price")
        currency = result.get("currency")
        error = result.get("error")

        # Write to appropriate files
        write_result(ALL_RESULTS_CSV, domain, word, avail, price, currency)

        if avail is True:
            write_result(AVAILABLE_CSV, domain, word, True, price, currency)
            available_count += 1
            status = f"AVAILABLE"
            if price:
                status += f" (${price/1e6:.2f})" if price > 1000 else f" (${price:.2f})"
        elif avail is False:
            write_result(TAKEN_CSV, domain, word, False, price, currency)
            taken_count += 1
            status = "TAKEN"
        elif error:
            error_count += 1
            status = f"ERROR: {error}"
            # Stop on auth/access errors
            if error in ("auth_failed", "access_denied"):
                print(f"\nStopping due to {error}. Please check your credentials/account.")
                break
        else:
            status = "UNKNOWN"

        # Progress update
        checked_set.add(word)
        elapsed = time.time() - start_time
        rate = (i + 1) / elapsed if elapsed > 0 else 0
        eta = (total - i - 1) / rate if rate > 0 else 0

        if (i + 1) % 10 == 0 or avail is True:
            print(f"  [{i+1}/{total}] {domain:30s} {status:20s} | "
                  f"avail={available_count} taken={taken_count} err={error_count} | "
                  f"{rate:.1f}/s ETA: {eta/60:.0f}m")

        # Save progress every 100 words
        if (i + 1) % 100 == 0:
            save_progress(list(checked_set), word)

        # Rate limiting delay
        if delay > 0:
            time.sleep(delay + random.uniform(0, delay * 0.5))

    # Final save
    save_progress(list(checked_set), words[-1] if words else None)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"DONE! Checked {len(checked_set)} domains in {elapsed/60:.1f} minutes")
    print(f"  Available: {available_count}")
    print(f"  Taken:     {taken_count}")
    print(f"  Errors:    {error_count}")
    print(f"\nResults saved to:")
    print(f"  {AVAILABLE_CSV}")
    print(f"  {TAKEN_CSV}")
    print(f"  {ALL_RESULTS_CSV}")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(
        description="Check single-word .ai domain availability on GoDaddy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check all words using GoDaddy API:
  python3 check_ai_domains.py --api-key KEY --api-secret SECRET

  # Check short words (<=5 chars) using web scraping:
  python3 check_ai_domains.py --scrape --max-length 5

  # Check using WHOIS lookups (no GoDaddy account needed):
  python3 check_ai_domains.py --whois --max-length 8

  # Check using DNS resolution (fastest, least accurate):
  python3 check_ai_domains.py --dns

  # Resume a previous interrupted run:
  python3 check_ai_domains.py --scrape --resume

  # Use a custom word list:
  python3 check_ai_domains.py --scrape --wordlist my_words.txt
        """,
    )
    parser.add_argument("--api-key", help="GoDaddy API key")
    parser.add_argument("--api-secret", help="GoDaddy API secret")
    parser.add_argument("--ote", action="store_true", help="Use GoDaddy OTE (sandbox) environment")
    parser.add_argument("--scrape", action="store_true", help="Use web scraping instead of API")
    parser.add_argument("--whois", action="store_true", help="Use WHOIS lookups (slower but no API key needed)")
    parser.add_argument("--dns", action="store_true", help="Use DNS resolution check (fast, less accurate)")
    parser.add_argument("--wordlist", default=str(WORDLIST_FILE), help="Path to word list file")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum word length (default: 1)")
    parser.add_argument("--max-length", type=int, default=None, help="Maximum word length (default: no limit)")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests in seconds (default: 1.0)")
    parser.add_argument("--resume", action="store_true", help="Resume from previous progress")
    parser.add_argument("--workers", type=int, default=1, help="Number of parallel workers (use carefully)")
    parser.add_argument("--start-letter", help="Start from words beginning with this letter")
    parser.add_argument("--end-letter", help="Stop at words beginning with this letter")

    args = parser.parse_args()

    # Validate mode
    if not args.api_key and not args.scrape and not args.whois and not args.dns:
        print("ERROR: Specify a check method:")
        print("  --api-key KEY --api-secret SECRET   (GoDaddy API)")
        print("  --scrape                            (Web scraping)")
        print("  --whois                             (WHOIS lookups)")
        print("  --dns                               (DNS resolution)")
        parser.print_help()
        sys.exit(1)

    # Load words
    if not os.path.exists(args.wordlist):
        print(f"ERROR: Word list not found: {args.wordlist}")
        print("Run this script from the same directory as wordlist.txt")
        sys.exit(1)

    words = load_wordlist(args.wordlist, args.min_length, args.max_length)

    # Filter by letter range
    if args.start_letter:
        words = [w for w in words if w[0] >= args.start_letter.lower()]
    if args.end_letter:
        words = [w for w in words if w[0] <= args.end_letter.lower()]

    print(f"Loaded {len(words)} words (length {args.min_length}-{args.max_length or 'any'})")

    # Select check function
    if args.api_key:
        if not args.api_secret:
            print("ERROR: --api-secret required with --api-key")
            sys.exit(1)
        check_fn = lambda w: check_domain_api(w, args.api_key, args.api_secret, args.ote)
        print(f"Using GoDaddy {'OTE' if args.ote else 'Production'} API")
    elif args.scrape:
        check_fn = check_domain_scrape
        print("Using GoDaddy web scraping")
    elif args.whois:
        check_fn = check_domain_whois
        print("Using WHOIS lookups")
    elif args.dns:
        check_fn = check_domain_dns
        args.delay = 0.1  # DNS is fast, less delay needed
        print("Using DNS resolution (note: unregistered domains may still not resolve)")

    run_checks(words, check_fn, workers=args.workers, delay=args.delay, resume=args.resume)


if __name__ == "__main__":
    main()
