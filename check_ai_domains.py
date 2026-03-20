#!/usr/bin/env python3
"""
Single-Word .ai Domain Availability Checker (Multi-Provider)

Checks every single-word .ai domain for availability across multiple providers
and writes results to CSV files (available.csv, taken.csv, all_results.csv).

Supported providers:
  - RDAP        (FREE, no account needed, most reliable)
  - Porkbun     (FREE with account, includes pricing)
  - Namecheap   (FREE with account, sandbox available)
  - GoDaddy     (requires 50+ domains on account)
  - WHOIS       (FREE, no account, needs whois command)
  - DNS         (FREE, fast, least accurate)

Usage:
    # RDAP — best option, free, no auth, accurate:
    python3 check_ai_domains.py --rdap

    # Porkbun API (free account at porkbun.com):
    python3 check_ai_domains.py --porkbun-key YOUR_KEY --porkbun-secret YOUR_SECRET

    # Namecheap sandbox (free account at sandbox.namecheap.com):
    python3 check_ai_domains.py --namecheap-key KEY --namecheap-user USER --namecheap-ip YOUR_IP

    # GoDaddy API (requires 50+ domains):
    python3 check_ai_domains.py --godaddy-key KEY --godaddy-secret SECRET

    # Filter by word length:
    python3 check_ai_domains.py --rdap --max-length 6

    # Resume from where you left off:
    python3 check_ai_domains.py --rdap --resume
"""

import argparse
import csv
import json
import os
import random
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Install with: pip3 install requests")
    sys.exit(1)


# ── Paths ───────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
WORDLIST_FILE = SCRIPT_DIR / "wordlist.txt"
RESULTS_DIR = SCRIPT_DIR / "results"
AVAILABLE_CSV = RESULTS_DIR / "available.csv"
TAKEN_CSV = RESULTS_DIR / "taken.csv"
ALL_RESULTS_CSV = RESULTS_DIR / "all_results.csv"
PROGRESS_FILE = RESULTS_DIR / "progress.json"

# ── Provider URLs ───────────────────────────────────────────────────────────────

RDAP_AI_URL = "https://rdap.identitydigital.services/rdap/domain"

PORKBUN_API_URL = "https://api.porkbun.com/api/json/v3/domain/checkDomain"

NAMECHEAP_PROD_URL = "https://api.namecheap.com/xml.response"
NAMECHEAP_SANDBOX_URL = "https://api.sandbox.namecheap.com/xml.response"

GODADDY_PROD_URL = "https://api.godaddy.com/v1/domains/available"
GODADDY_OTE_URL = "https://api.ote-godaddy.com/v1/domains/available"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
]


# ── Helpers ─────────────────────────────────────────────────────────────────────

def load_wordlist(filepath, min_length=1, max_length=None):
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
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"checked": [], "last_word": None, "timestamp": None}


def save_progress(checked_words, last_word):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump({
            "checked": checked_words,
            "last_word": last_word,
            "timestamp": datetime.now().isoformat(),
            "total_checked": len(checked_words),
        }, f)


def write_result(filepath, domain, word, available, price=None, currency=None, provider=None):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    file_exists = filepath.exists()
    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["domain", "word", "available", "price", "currency", "provider", "checked_at"])
        writer.writerow([
            domain, word, available, price or "", currency or "",
            provider or "", datetime.now().isoformat()
        ])


def retry_request(fn, max_retries=4, label=""):
    """Retry a request function with exponential backoff."""
    for attempt in range(max_retries):
        try:
            return fn()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            wait = (2 ** attempt) + random.uniform(0, 1)
            print(f"  Network error{' for ' + label if label else ''}: {e}, retry in {wait:.1f}s...")
            time.sleep(wait)


# ── RDAP Provider (FREE, no auth) ──────────────────────────────────────────────

def check_domain_rdap(word, session=None):
    """
    Check domain via RDAP (Registration Data Access Protocol).
    FREE, no authentication needed. The .ai registry uses Identity Digital's RDAP.
    """
    domain = f"{word}.ai"
    if session is None:
        session = requests.Session()

    for attempt in range(4):
        try:
            resp = session.get(
                f"{RDAP_AI_URL}/{domain}",
                headers={"Accept": "application/rdap+json", "User-Agent": random.choice(USER_AGENTS)},
                timeout=15,
            )

            if resp.status_code == 200:
                # Domain exists in registry = TAKEN
                data = resp.json()
                registrar = ""
                for entity in data.get("entities", []):
                    if "registrar" in entity.get("roles", []):
                        vcard = entity.get("vcardArray", [None, []])[1] if entity.get("vcardArray") else []
                        for field in vcard:
                            if field[0] == "fn":
                                registrar = field[3]
                                break

                # Extract dates
                events = {e["eventAction"]: e["eventDate"] for e in data.get("events", [])}

                return {
                    "word": word,
                    "domain": domain,
                    "available": False,
                    "registrar": registrar,
                    "created": events.get("registration", ""),
                    "expires": events.get("expiration", ""),
                    "provider": "rdap",
                }

            elif resp.status_code == 404:
                # Domain NOT found in registry = AVAILABLE
                return {
                    "word": word,
                    "domain": domain,
                    "available": True,
                    "provider": "rdap",
                }

            elif resp.status_code == 429:
                wait = (2 ** attempt) + random.uniform(1, 3)
                print(f"  RDAP rate limited on {domain}, waiting {wait:.1f}s...")
                time.sleep(wait)
                continue

            else:
                # Other status codes
                if attempt < 3:
                    time.sleep((2 ** attempt) + random.uniform(0, 1))
                    continue
                return {"word": word, "domain": domain, "available": None, "error": f"http_{resp.status_code}", "provider": "rdap"}

        except requests.exceptions.RequestException as e:
            if attempt < 3:
                time.sleep((2 ** attempt) + random.uniform(0, 1))
                continue
            return {"word": word, "domain": domain, "available": None, "error": str(e), "provider": "rdap"}

    return {"word": word, "domain": domain, "available": None, "error": "max_retries", "provider": "rdap"}


# ── Porkbun Provider ───────────────────────────────────────────────────────────

def check_domain_porkbun(word, api_key, secret_key, session=None):
    """
    Check domain via Porkbun API.
    Free with account. Get keys at: https://porkbun.com/account/api
    Rate limit: ~1 check per 10 seconds.
    """
    domain = f"{word}.ai"
    if session is None:
        session = requests.Session()

    payload = {
        "secretapikey": secret_key,
        "apikey": api_key,
    }

    for attempt in range(4):
        try:
            resp = session.post(
                f"{PORKBUN_API_URL}/{domain}",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=15,
            )

            if resp.status_code == 200:
                data = resp.json()
                if data.get("status") == "SUCCESS":
                    avail = data.get("avail", "no") == "yes"
                    pricing = data.get("pricing", {})
                    reg_price = pricing.get("registration") if pricing else None
                    return {
                        "word": word,
                        "domain": domain,
                        "available": avail,
                        "price": reg_price,
                        "currency": "USD",
                        "premium": data.get("premium", False),
                        "provider": "porkbun",
                    }
                elif "rate limit" in data.get("message", "").lower():
                    wait = 10 + random.uniform(0, 3)
                    print(f"  Porkbun rate limited on {domain}, waiting {wait:.1f}s...")
                    time.sleep(wait)
                    continue
                else:
                    return {
                        "word": word, "domain": domain, "available": None,
                        "error": data.get("message", "unknown"), "provider": "porkbun",
                    }

            elif resp.status_code == 429:
                wait = 10 + random.uniform(0, 5)
                print(f"  Porkbun rate limited on {domain}, waiting {wait:.1f}s...")
                time.sleep(wait)
                continue

            elif resp.status_code in (401, 403):
                return {"word": word, "domain": domain, "available": None, "error": "auth_failed", "provider": "porkbun"}

            else:
                if attempt < 3:
                    time.sleep((2 ** attempt) + random.uniform(0, 1))
                    continue
                return {"word": word, "domain": domain, "available": None, "error": f"http_{resp.status_code}", "provider": "porkbun"}

        except requests.exceptions.RequestException as e:
            if attempt < 3:
                time.sleep((2 ** attempt) + random.uniform(0, 1))
                continue
            return {"word": word, "domain": domain, "available": None, "error": str(e), "provider": "porkbun"}

    return {"word": word, "domain": domain, "available": None, "error": "max_retries", "provider": "porkbun"}


# ── Namecheap Provider ─────────────────────────────────────────────────────────

def check_domain_namecheap(word, api_key, api_user, client_ip, sandbox=False, session=None):
    """
    Check domain via Namecheap API.
    Free sandbox: sign up at https://www.sandbox.namecheap.com/
    Enable API at: Profile > Tools > API Access
    """
    domain = f"{word}.ai"
    if session is None:
        session = requests.Session()

    base_url = NAMECHEAP_SANDBOX_URL if sandbox else NAMECHEAP_PROD_URL
    params = {
        "ApiUser": api_user,
        "ApiKey": api_key,
        "UserName": api_user,
        "Command": "namecheap.domains.check",
        "ClientIp": client_ip,
        "DomainList": domain,
    }

    for attempt in range(4):
        try:
            resp = session.get(base_url, params=params, timeout=15)

            if resp.status_code == 200:
                try:
                    root = ET.fromstring(resp.text)
                    # Namecheap XML namespace
                    ns = {"nc": "http://api.namecheap.com/xml.response"}

                    # Check for errors
                    errors = root.findall(".//nc:Errors/nc:Error", ns)
                    if not errors:
                        # Try without namespace
                        errors = root.findall(".//Errors/Error")

                    if errors:
                        err_msg = errors[0].text or errors[0].get("Number", "unknown")
                        return {"word": word, "domain": domain, "available": None, "error": err_msg, "provider": "namecheap"}

                    # Find domain check result
                    results = root.findall(".//nc:DomainCheckResult", ns)
                    if not results:
                        results = root.findall(".//DomainCheckResult")

                    for r in results:
                        if r.get("Domain", "").lower() == domain.lower():
                            avail = r.get("Available", "false").lower() == "true"
                            is_premium = r.get("IsPremiumName", "false").lower() == "true"
                            price = r.get("PremiumRegistrationPrice") if is_premium else None
                            return {
                                "word": word,
                                "domain": domain,
                                "available": avail,
                                "price": price,
                                "currency": "USD" if price else None,
                                "premium": is_premium,
                                "provider": "namecheap",
                            }

                    return {"word": word, "domain": domain, "available": None, "error": "no_result_in_xml", "provider": "namecheap"}

                except ET.ParseError:
                    return {"word": word, "domain": domain, "available": None, "error": "xml_parse_error", "provider": "namecheap"}

            elif resp.status_code == 429:
                wait = (2 ** attempt) + random.uniform(1, 3)
                time.sleep(wait)
                continue

            else:
                if attempt < 3:
                    time.sleep((2 ** attempt) + random.uniform(0, 1))
                    continue
                return {"word": word, "domain": domain, "available": None, "error": f"http_{resp.status_code}", "provider": "namecheap"}

        except requests.exceptions.RequestException as e:
            if attempt < 3:
                time.sleep((2 ** attempt) + random.uniform(0, 1))
                continue
            return {"word": word, "domain": domain, "available": None, "error": str(e), "provider": "namecheap"}

    return {"word": word, "domain": domain, "available": None, "error": "max_retries", "provider": "namecheap"}


# ── GoDaddy Provider ───────────────────────────────────────────────────────────

def check_domain_godaddy(word, api_key, api_secret, ote=False):
    """Check domain availability via GoDaddy API (requires 50+ domains on account)."""
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
                    "word": word, "domain": domain,
                    "available": data.get("available", False),
                    "price": data.get("price"), "currency": data.get("currency"),
                    "provider": "godaddy",
                }
            elif resp.status_code == 429:
                wait = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait)
                continue
            elif resp.status_code in (401, 403):
                msg = "auth_failed" if resp.status_code == 401 else "access_denied"
                return {"word": word, "domain": domain, "available": None, "error": msg, "provider": "godaddy"}
            else:
                if attempt < 3:
                    time.sleep((2 ** attempt) + random.uniform(0, 1))
                    continue
        except requests.exceptions.RequestException:
            if attempt < 3:
                time.sleep((2 ** attempt) + random.uniform(0, 1))
                continue

    return {"word": word, "domain": domain, "available": None, "error": "max_retries", "provider": "godaddy"}


# ── WHOIS Provider ──────────────────────────────────────────────────────────────

def check_domain_whois(word):
    """Check domain via WHOIS lookup (needs whois command installed)."""
    import subprocess
    domain = f"{word}.ai"
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=15)
        output = result.stdout.lower()
        if "no match" in output or "not found" in output or "no data found" in output:
            return {"word": word, "domain": domain, "available": True, "provider": "whois"}
        elif "domain name:" in output or "registrant" in output or "creation date" in output:
            return {"word": word, "domain": domain, "available": False, "provider": "whois"}
        else:
            return {"word": word, "domain": domain, "available": "unknown", "provider": "whois"}
    except FileNotFoundError:
        return {"word": word, "domain": domain, "available": None, "error": "whois_not_installed", "provider": "whois"}
    except subprocess.TimeoutExpired:
        return {"word": word, "domain": domain, "available": None, "error": "whois_timeout", "provider": "whois"}
    except Exception as e:
        return {"word": word, "domain": domain, "available": None, "error": str(e), "provider": "whois"}


# ── DNS Provider ────────────────────────────────────────────────────────────────

def check_domain_dns(word):
    """Fallback: check if domain resolves (taken domains usually resolve)."""
    import socket
    domain = f"{word}.ai"
    try:
        socket.setdefaulttimeout(5)
        socket.getaddrinfo(domain, None)
        return {"word": word, "domain": domain, "available": False, "provider": "dns"}
    except socket.gaierror:
        return {"word": word, "domain": domain, "available": "unknown_dns", "provider": "dns"}
    except Exception:
        return {"word": word, "domain": domain, "available": None, "error": "dns_error", "provider": "dns"}


# ── Runner ──────────────────────────────────────────────────────────────────────

def run_checks(words, check_fn, delay=1.0, resume=False, needs_session=False):
    """Run domain checks across all words."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

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
    print(f"Results saved to: {RESULTS_DIR}/")
    print(f"  available.csv | taken.csv | all_results.csv | progress.json\n")

    session = requests.Session() if needs_session else None
    start_time = time.time()

    for i, word in enumerate(words):
        try:
            if needs_session:
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
        provider = result.get("provider", "")

        write_result(ALL_RESULTS_CSV, domain, word, avail, price, currency, provider)

        if avail is True:
            write_result(AVAILABLE_CSV, domain, word, True, price, currency, provider)
            available_count += 1
            status = "AVAILABLE"
            if price:
                try:
                    p = float(price)
                    status += f" (${p/1e6:.2f})" if p > 10000 else f" (${p:.2f})"
                except (ValueError, TypeError):
                    status += f" ({price})"
        elif avail is False:
            write_result(TAKEN_CSV, domain, word, False, price, currency, provider)
            taken_count += 1
            registrar = result.get("registrar", "")
            status = f"TAKEN" + (f" [{registrar}]" if registrar else "")
        elif error:
            error_count += 1
            status = f"ERROR: {error}"
            if error in ("auth_failed", "access_denied"):
                print(f"\nStopping: {error}. Check your credentials/account.")
                break
        else:
            status = "UNKNOWN"

        checked_set.add(word)
        elapsed = time.time() - start_time
        rate = (i + 1) / elapsed if elapsed > 0 else 0
        eta = (total - i - 1) / rate if rate > 0 else 0

        if (i + 1) % 10 == 0 or avail is True:
            print(f"  [{i+1}/{total}] {domain:30s} {status:30s} | "
                  f"A={available_count} T={taken_count} E={error_count} | "
                  f"{rate:.1f}/s ETA:{eta/60:.0f}m")

        if (i + 1) % 100 == 0:
            save_progress(list(checked_set), word)

        if delay > 0:
            time.sleep(delay + random.uniform(0, delay * 0.3))

    save_progress(list(checked_set), words[-1] if words else None)

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"DONE! Checked {len(checked_set)} domains in {elapsed/60:.1f} minutes")
    print(f"  Available: {available_count}")
    print(f"  Taken:     {taken_count}")
    print(f"  Errors:    {error_count}")
    print(f"\n  {AVAILABLE_CSV}")
    print(f"  {TAKEN_CSV}")
    print(f"  {ALL_RESULTS_CSV}")
    print(f"{'='*60}")


# ── Main ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Check single-word .ai domain availability (multi-provider)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Providers (pick one):

  RDAP (RECOMMENDED — free, no account needed, accurate):
    python3 check_ai_domains.py --rdap

  Porkbun (free account, includes pricing):
    python3 check_ai_domains.py --porkbun-key KEY --porkbun-secret SECRET
    Get keys: https://porkbun.com/account/api

  Namecheap (free sandbox account):
    python3 check_ai_domains.py --namecheap-key KEY --namecheap-user USER --namecheap-ip IP --namecheap-sandbox
    Sandbox signup: https://www.sandbox.namecheap.com/

  GoDaddy (requires 50+ domains):
    python3 check_ai_domains.py --godaddy-key KEY --godaddy-secret SECRET
    Get keys: https://developer.godaddy.com/keys

  WHOIS (free, needs whois command):
    python3 check_ai_domains.py --whois

  DNS (free, fast, least accurate):
    python3 check_ai_domains.py --dns

Examples:
  python3 check_ai_domains.py --rdap --max-length 5
  python3 check_ai_domains.py --rdap --start-letter a --end-letter c --resume
  python3 check_ai_domains.py --porkbun-key pk1_xxx --porkbun-secret sk1_xxx --max-length 4
  python3 check_ai_domains.py --namecheap-key KEY --namecheap-user USER --namecheap-ip 1.2.3.4 --namecheap-sandbox
        """,
    )

    # Provider flags
    rdap = parser.add_argument_group("RDAP (recommended)")
    rdap.add_argument("--rdap", action="store_true", help="Use RDAP protocol (free, no auth)")

    pb = parser.add_argument_group("Porkbun")
    pb.add_argument("--porkbun-key", help="Porkbun API key")
    pb.add_argument("--porkbun-secret", help="Porkbun secret API key")

    nc = parser.add_argument_group("Namecheap")
    nc.add_argument("--namecheap-key", help="Namecheap API key")
    nc.add_argument("--namecheap-user", help="Namecheap API username")
    nc.add_argument("--namecheap-ip", help="Your whitelisted IP for Namecheap API")
    nc.add_argument("--namecheap-sandbox", action="store_true", help="Use Namecheap sandbox")

    gd = parser.add_argument_group("GoDaddy")
    gd.add_argument("--godaddy-key", help="GoDaddy API key")
    gd.add_argument("--godaddy-secret", help="GoDaddy API secret")
    gd.add_argument("--godaddy-ote", action="store_true", help="Use GoDaddy OTE sandbox")

    other = parser.add_argument_group("Other methods")
    other.add_argument("--whois", action="store_true", help="Use WHOIS lookups")
    other.add_argument("--dns", action="store_true", help="Use DNS resolution (fast, less accurate)")

    # Filtering
    filt = parser.add_argument_group("Filtering")
    filt.add_argument("--wordlist", default=str(WORDLIST_FILE), help="Path to word list file")
    filt.add_argument("--min-length", type=int, default=1, help="Minimum word length (default: 1)")
    filt.add_argument("--max-length", type=int, default=None, help="Maximum word length")
    filt.add_argument("--start-letter", help="Start from words beginning with this letter")
    filt.add_argument("--end-letter", help="Stop at words beginning with this letter")
    filt.add_argument("--delay", type=float, default=None, help="Delay between requests (seconds)")
    filt.add_argument("--resume", action="store_true", help="Resume from previous progress")

    args = parser.parse_args()

    # Determine provider
    check_fn = None
    provider_name = None
    default_delay = 1.0
    needs_session = False

    if args.rdap:
        check_fn = check_domain_rdap
        provider_name = "RDAP (rdap.identitydigital.services)"
        default_delay = 0.5
        needs_session = True

    elif args.porkbun_key:
        if not args.porkbun_secret:
            parser.error("--porkbun-secret required with --porkbun-key")
        key, secret = args.porkbun_key, args.porkbun_secret
        check_fn = lambda w, session=None: check_domain_porkbun(w, key, secret, session)
        provider_name = "Porkbun API"
        default_delay = 10.0  # Porkbun rate limits to ~1/10s
        needs_session = True

    elif args.namecheap_key:
        if not args.namecheap_user or not args.namecheap_ip:
            parser.error("--namecheap-user and --namecheap-ip required with --namecheap-key")
        key, user, ip, sandbox = args.namecheap_key, args.namecheap_user, args.namecheap_ip, args.namecheap_sandbox
        check_fn = lambda w, session=None: check_domain_namecheap(w, key, user, ip, sandbox, session)
        provider_name = f"Namecheap {'Sandbox' if sandbox else 'Production'} API"
        default_delay = 1.0
        needs_session = True

    elif args.godaddy_key:
        if not args.godaddy_secret:
            parser.error("--godaddy-secret required with --godaddy-key")
        key, secret, ote = args.godaddy_key, args.godaddy_secret, args.godaddy_ote
        check_fn = lambda w: check_domain_godaddy(w, key, secret, ote)
        provider_name = f"GoDaddy {'OTE' if ote else 'Production'} API"
        default_delay = 1.0

    elif args.whois:
        check_fn = check_domain_whois
        provider_name = "WHOIS"
        default_delay = 1.0

    elif args.dns:
        check_fn = check_domain_dns
        provider_name = "DNS Resolution"
        default_delay = 0.1

    else:
        print("ERROR: Pick a provider. Recommended: --rdap (free, no account needed)\n")
        parser.print_help()
        sys.exit(1)

    delay = args.delay if args.delay is not None else default_delay

    # Load words
    if not os.path.exists(args.wordlist):
        print(f"ERROR: Word list not found: {args.wordlist}")
        sys.exit(1)

    words = load_wordlist(args.wordlist, args.min_length, args.max_length)
    if args.start_letter:
        words = [w for w in words if w[0] >= args.start_letter.lower()]
    if args.end_letter:
        words = [w for w in words if w[0] <= args.end_letter.lower()]

    print(f"Provider: {provider_name}")
    print(f"Words: {len(words)} (length {args.min_length}-{args.max_length or 'any'})")
    print(f"Delay: {delay}s between checks")

    run_checks(words, check_fn, delay=delay, resume=args.resume, needs_session=needs_session)


if __name__ == "__main__":
    main()
