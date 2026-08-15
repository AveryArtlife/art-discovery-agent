# Methodology & Data-Quality Notes

_Competitive-intelligence research on creators promoting PackDraw and comparable
mystery-box / case-opening brands. Compiled 2026-06-24._

## Scope & sources
- **Public pages only.** All data was gathered via web search and fetching of
  publicly accessible pages (creator profiles, public videos/posts, brand
  affiliate/code directories, third-party stats pages). No login walls,
  captchas, rate limits, or anti-bot measures were bypassed.
- **Brands tracked:** PackDraw, HypeDrop, RillaBox, Stake Drops, CSGORoll,
  Cases.GG, Clash.gg, plus adjacent CS2 skin sites (Rain.gg, Key-Drop, etc.).

## Discovery process
1. Searched each brand + intent terms ("code", "referral", "sponsored", "ad",
   "promo") across YouTube, TikTok, Instagram, Twitch, X/Twitter, Kick, Reddit.
2. Pulled referral/affiliate codes from videos and bios, then searched the
   **codes themselves** — each code typically unspools more of a brand's
   affiliate roster.
3. Followed "similar creators" / suggested-channel trails to expand the set.
4. Included commenters / quote-tweeters only when they are themselves creators
   promoting the brand.

## Contact-data guardrails
Only **publicly-listed business/booking contacts** were captured — the email or
form a creator deliberately posts for partnerships (YouTube "About" tab business
email, link-in-bio, Linktree, press kit, management agency). Creators with no
public business contact are marked `none found`. No private/personal addresses
were sought or recorded.

## Confidence & estimates
- Follower/subscriber counts are tagged with the date observed. Where a count
  could not be directly observed on a public page, it is marked `N/A` or
  `ESTIMATE`. **An honest N/A is preferred over a fabricated number.**
- Audience tiers: nano `<10k` / micro `10k–100k` / mid `100k–500k` /
  macro `500k+`.
- Follower counts on these platforms move quickly; treat every figure as a
  snapshot, not a live value.

## Scoring model (1–5 unless noted)
- **engagement_rate** — avg (likes+comments)/followers on recent public posts;
  platform measured is noted. `N/A` when too few public posts to estimate.
  Normalised to 1–5 for the composite (`engagement_rate_normalized`).
- **brand_fit** — closeness to the case-opening / mystery-box niche.
  `5` = already promotes this exact category; `1` = adjacent at best.
- **audience_quality** — comment authenticity, view-to-follower ratio, signs of
  inflated/bot following. Anything that looks purchased is flagged.
- **est_partnership_cost** — tier/rate-card estimate, ALWAYS marked `ESTIMATE`
  (micro `$100–500`, mid `$500–3k`, macro `$3k+`). Kept as its own column, not
  folded into the composite.
- **reachability** — `5` = public business email or agency listed; `1` = none.
- **priority_score** = `(brand_fit × 0.35) + (engagement_rate_normalized × 0.25)
  + (audience_quality × 0.20) + (reachability × 0.20)`.

## How to read this dataset
- This is an **outreach-planning shortlist**, not an audited dataset. Re-verify
  follower counts, contacts, and codes at the moment of outreach.
- Promoting real-money or skin-gambling-adjacent products carries legal,
  platform-policy, and brand-safety constraints that vary by jurisdiction and by
  creator. Vet each candidate against the relevant advertising rules before
  engaging.

## Regulatory / brand-safety caveat
Several brands in this set operate in the loot-box / skin-gambling grey area and
have drawn regulatory and platform-policy scrutiny. Creators in this niche range
from straightforward unboxing/entertainment to gambling-style content. Factor
brand-safety and disclosure-compliance review into any partnership decision.
