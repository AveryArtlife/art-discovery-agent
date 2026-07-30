#!/usr/bin/env python3
"""Rank Instagram pages by engagement strength.

Reads per-post metrics and produces a numeric ranking of accounts by a
weighted engagement score (views, comments, likes, shares/saves), plus
engagement rate per follower.

Input: a CSV with one row per post:

    handle,views,likes,comments,shares,saves

Collect the rows however you like — Instagram professional-account
insights exports, a Meta Graph API pull, or a locally-run scraper such
as instaloader (requires your own logged-in session; Instagram blocks
anonymous access). Only `handle` and at least one metric column are
required; missing columns are treated as 0.

Usage:
    python scripts/rank_engagement.py data/posts.csv --accounts data/accounts.csv

The accounts CSV (handle,followers,niche) supplies follower counts for
the engagement-rate column; without it only absolute scores are shown.
"""

import argparse
import csv
import sys
from collections import defaultdict

# Comments and shares signal far stronger intent than a like or a view,
# so they dominate the interaction score.
WEIGHTS = {
    "views": 0.01,
    "likes": 1.0,
    "comments": 8.0,
    "shares": 6.0,
    "saves": 4.0,
}

METRICS = list(WEIGHTS)


def _num(row, key):
    try:
        return float(row.get(key, 0) or 0)
    except ValueError:
        return 0.0


def load_posts(path):
    per_account = defaultdict(lambda: {m: 0.0 for m in METRICS} | {"posts": 0})
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            handle = (row.get("handle") or "").strip().lstrip("@").lower()
            if not handle:
                continue
            acc = per_account[handle]
            acc["posts"] += 1
            for m in METRICS:
                acc[m] += _num(row, m)
    if not per_account:
        sys.exit(f"error: no usable rows in {path}")
    return per_account


def load_accounts(path):
    info = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            handle = (row.get("handle") or "").strip().lstrip("@").lower()
            if handle:
                info[handle] = {
                    "followers": _num(row, "followers"),
                    "niche": (row.get("niche") or "").strip(),
                }
    return info


def rank(per_account, accounts):
    rows = []
    for handle, acc in per_account.items():
        posts = acc["posts"] or 1
        score = sum(WEIGHTS[m] * acc[m] for m in METRICS) / posts
        followers = accounts.get(handle, {}).get("followers", 0)
        rate = (acc["likes"] + acc["comments"]) / posts / followers * 100 if followers else None
        rows.append({
            "handle": handle,
            "niche": accounts.get(handle, {}).get("niche", ""),
            "followers": int(followers),
            "posts": acc["posts"],
            "avg_views": acc["views"] / posts,
            "avg_comments": acc["comments"] / posts,
            "score": score,
            "rate": rate,
        })
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("posts_csv", help="per-post metrics CSV (handle,views,likes,comments,shares,saves)")
    p.add_argument("--accounts", help="accounts CSV (handle,followers,niche)")
    args = p.parse_args()

    accounts = load_accounts(args.accounts) if args.accounts else {}
    rows = rank(load_posts(args.posts_csv), accounts)

    print(f"{'#':>2}  {'handle':<22}{'niche':<12}{'followers':>10}{'avg views':>12}"
          f"{'avg cmts':>10}{'score/post':>12}{'eng rate':>10}")
    for i, r in enumerate(rows, 1):
        rate = f"{r['rate']:.2f}%" if r["rate"] is not None else "-"
        print(f"{i:>2}  @{r['handle']:<21}{r['niche']:<12}{r['followers']:>10,}"
              f"{r['avg_views']:>12,.0f}{r['avg_comments']:>10,.1f}{r['score']:>12,.0f}{rate:>10}")


if __name__ == "__main__":
    main()
