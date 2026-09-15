# Atlas prompt — Artnet auction unsold-lot tracker

**Target auction:** https://www.artnet.com/auctions/20th-century-art-0926/2
(The `/2` is page 2; also crawl `/1`, `/3`, … until no more pages.)

**Goal:** Right before each lot closes, record whether it sold. When the whole
sale is over, output a list of every unsold lot with its opening/reserve bid.

---

## Setup (one time, at start of run)

1. Open the auction landing page (page 1) in an authenticated browser session
   (my Artnet login cookies). Artnet lot pages are JS-rendered — use a real
   browser, not a raw HTTP fetch.
2. Paginate through every results page for this sale. For each lot, capture:
   - `lot_id` (URL slug or numeric id)
   - `lot_url`
   - `lot_number`
   - `artist`
   - `title`
   - `opening_bid` (the "Starting bid" / "Opening bid" / reserve shown before
     any bids are placed — this is the number the user cares about)
   - `current_bid` (may equal opening if no bids yet)
   - `bid_count`
   - `close_at` (absolute UTC timestamp — convert from Artnet's countdown /
     local time; store ISO-8601)
3. Persist the list to `./state/lots.json`. Keep it as the source of truth;
   later steps update rows in place.

## Per-lot watch loop

For each lot in `lots.json`, schedule a task to fire **60 seconds before
`close_at`**. Stagger fires so you never have more than ~3 tabs open at once
(Artnet rate-limits and lots in this sale close in 30-second stair-steps).

When a scheduled task fires for a lot:

1. Reload the lot page in the authenticated browser.
2. Wait until the countdown shows ≤ 5 seconds, then capture:
   - `final_bid`
   - `final_bid_count`
   - `status_text` (Artnet shows "Sold", "Passed", "Reserve not met",
     "No bids", or "Withdrawn")
3. Wait an additional 30 seconds past `close_at`, reload once more, and
   re-capture the same fields — Artnet sometimes flips the status after the
   hammer.
4. Classify:
   - `sold` if `status_text` contains "Sold" **or** `final_bid_count > 0` and
     `final_bid >= opening_bid` and status is not "Reserve not met" / "Passed"
     / "Withdrawn".
   - `unsold` otherwise. Sub-reason = the raw `status_text` (or
     `"no bids"` if empty and `final_bid_count == 0`).
5. Write the result back into the lot's row in `lots.json` and append a line
   to `./state/events.log` with the timestamp so the run is auditable.

## Robustness

- If a page fails to load, retry with exponential backoff (5s, 15s, 45s). If
  still failing, mark the lot `check_failed` and keep going — do not abort
  the whole run.
- If the login cookie has expired, pause the run and surface a prompt for me
  to re-auth; resume from `lots.json` after.
- Persist after every write so a crash never loses more than one lot's
  update.

## Final report

Once every lot has a terminal status (sold / unsold / check_failed), produce
`./out/unsold.csv` with columns:

```
lot_number, artist, title, opening_bid, final_bid, final_bid_count, status_text, lot_url
```

Include only rows where classification is `unsold`. Sort by `opening_bid`
descending.

Also print a short summary to the console:

- total lots in sale
- number sold
- number unsold (and % of sale)
- sum of opening bids for unsold lots (the "value that failed to clear")
- any `check_failed` rows I should re-check manually

## Non-goals

- Do **not** place any bids.
- Do **not** log in on my behalf if the session is already dead — surface it
  to me.
- Do **not** post anywhere public; this is a private report.
