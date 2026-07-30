#!/usr/bin/env python3
"""Convert an Apify instagram-scraper dataset export into posts.csv.

Run the actor with apify/instagram-scraper-input.json, then export the
dataset as JSON and convert it:

    python scripts/apify_to_posts_csv.py dataset.json data/posts.csv

Optionally also convert an apify/instagram-profile-scraper export to
refresh follower counts in the accounts CSV:

    python scripts/apify_to_posts_csv.py dataset.json data/posts.csv \
        --profiles profiles.json --accounts data/accounts.csv

Then rank:

    python scripts/rank_engagement.py data/posts.csv --accounts data/accounts.csv
"""

import argparse
import csv
import json


# Accounts that renamed themselves; map back to the handle in accounts.csv.
ALIASES = {"cursedmemerz": "crimeworld81"}


def post_rows(items):
    for item in items:
        handle = (item.get("ownerUsername") or "").lower()
        if not handle:  # error rows: not_found / restricted profiles
            continue
        likes = item.get("likesCount")
        yield {
            "handle": ALIASES.get(handle, handle),
            # Image posts have no view count; leave blank rather than 0 so
            # they don't drag the view average down.
            "views": item.get("videoPlayCount") or item.get("videoViewCount") or "",
            # likesCount is -1 when the account hides like counts.
            "likes": likes if likes is not None and likes >= 0 else "",
            "comments": item.get("commentsCount") or 0,
            "shares": "",  # not exposed by Instagram publicly
            "saves": "",
        }


def update_accounts(profiles_path, accounts_path):
    with open(profiles_path, encoding="utf-8") as f:
        followers = {
            ALIASES.get((p.get("username") or "").lower(), (p.get("username") or "").lower()):
                p.get("followersCount")
            for p in json.load(f)
        }
    with open(accounts_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        live = followers.get(row["handle"].lower())
        if live:
            row["followers"] = live
    with open(accounts_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["handle", "followers", "niche"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"updated follower counts in {accounts_path}")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("dataset_json", help="Apify instagram-scraper dataset export (JSON)")
    p.add_argument("out_csv", help="output posts CSV path")
    p.add_argument("--profiles", help="Apify instagram-profile-scraper dataset export (JSON)")
    p.add_argument("--accounts", help="accounts CSV to refresh follower counts in")
    args = p.parse_args()

    with open(args.dataset_json, encoding="utf-8") as f:
        items = json.load(f)
    rows = list(post_rows(items))
    with open(args.out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["handle", "views", "likes", "comments", "shares", "saves"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} posts to {args.out_csv}")

    if args.profiles and args.accounts:
        update_accounts(args.profiles, args.accounts)


if __name__ == "__main__":
    main()
