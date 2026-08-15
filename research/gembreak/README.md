# GemBreak Partner Research — Prediction Markets, Watches & Collectibles

_Compiled 2026-07-19. Expansion of the influencer research into three new verticals
+ cross-references, culminating in a ranked GemBreak partner shortlist._

## What GemBreak is (working assumption)
GemBreak reads as a **gem/card "breaking"** product — live pack/box breaking of
collectibles, which is structurally a **gambling-adjacent unbox mechanic** (the
same psychology as case-opening and mystery boxes; note the 2026 Whatnot lawsuits
literally arguing card-breaks are an "unregulated online casino"). That places
GemBreak at the intersection of **collectibles × gambling/prediction × unboxing**,
which is exactly why all three requested verticals are relevant.
*If GemBreak's product is narrower/different, tell me and I'll re-weight the ranking.*

## Files
| File | Rows | What |
|---|---|---|
| `prediction_gambling_influencers.csv` | 12 | Polymarket / Kalshi / Stake / Roobet / Rainbet promoters |
| `watch_influencers.csv` | 14 | Watch dealers & reviewers (Neel/TPT, Nico Leonard, Teddy B., micro names) |
| `pokemon_collectible_influencers.csv` | 59 | Pokémon/TCG creators & breakers (incl. Feedspot "must-follow" set) |
| `crossref_watch_x_gambling.csv` | 8 | Watch people who also touch gambling/prediction |
| `crossref_collectible_x_gambling.csv` | 10 | Collectible creators whose format IS the gambling mechanic (breakers) + jeweler→Polymarket |
| `gembreak_top100.csv` | 100 | **The deliverable** — ranked best-fit GemBreak partners, with a `why` for each |

## The GemBreak Top 100 — how it's ranked
`gembreak_score = break_fit×0.40 + crossover×0.25 + tier_fit×0.15 + reachability×0.20`
- **break_fit** — closeness to live pack/box breaking. Collectible **breakers = 5**,
  case-opening/mystery-box = 4, watch dealer/unbox = 3–4, pure prediction = 2.
- **crossover** — comfort bridging collectibles ↔ gambling/prediction. Documented
  crossover = 5, breakers (format = the mechanic) = 4, gambling-native = 3.
- **tier_fit** — GemBreak wants **engaged micro**: micro/nano = 5 → macro = 3.
- **reachability** — public email/site = 5 → nothing = 2.

**Top-100 composition:** 88 case-opening/mystery-box (carried from the existing
roster — same unbox mechanic), 9 collectible breakers, 2 watch, 1 prediction;
98 within the ≤1M micro focus. Top names: **Neel Alwani (NeelTPT)** (watch dealer,
directly reachable + gambling-world clientele), micro Pokémon breakers **Gio the
Pokémon Puller** and **rogerrips**, and **ChrisG** (the one creator with a public
email).

### Honest note on the mix
The list skews to case-opening because that roster was already fully built and
scored, while the new Pokémon set is broad (59) but mostly **list-only** (no
verified counts/URLs yet → scored conservatively). If GemBreak's priority is
*collectible breakers specifically*, the right next step is to **enrich the Pokémon
breakers** (counts, handles, contacts) — they'd then rise to the top on break_fit.

## Cross-reference findings (the highest-value insight)
- **The card-breaking format is itself the crossover.** Breakers (rogerrips,
  RealBreakingNate, UnlistedLeaf, PokeRev, etc.) already run a live, randomized,
  gambling-style unbox — they are GemBreak's most natural partners and need no
  "conversion."
- **Documented collectible/watch → gambling/prediction bridges:**
  - **Moses the Jeweler** (@mosesjewelry) — a jeweler paid to promote **Polymarket**.
  - **Timepiece Trading / Neel Alwani** — sells watches to **SteveWillDoIt, Drake,
    6ix9ine** (the gambling-creator economy) — a direct commercial bridge.
  - **Celebrity gamblers who collect watches** — Drake, SteveWillDoIt, Adin Ross
    (Stake/Rainbet) overlap the luxury-watch world (macro, reference only).

## ⚠️ Brand-safety flags (read before outreach)
- **Prediction-market scandal:** a WSJ investigation found Polymarket paid **800+
  creators $2.5M** to post **staged/fake winning bets** on dummy sites, undisclosed
  (Kalshi similar). Named cohort members (e.g. George Makihara, and the "fake $100k
  win" videos) are flagged — associating GemBreak with that cohort is reputational
  risk. Prefer transparent, disclosure-compliant creators.
- The whole category is gambling-adjacent and under active regulatory/legal scrutiny
  (Whatnot lawsuits, FTC disclosure precedent). Run legal/brand-safety review before
  any deal.

## LunarCrush-verified counts (2026-07-19)
~35 creators now carry **live, verified follower counts** pulled from the LunarCrush
MCP connector (tagged `(LunarCrush 2026-07-19)` in the `followers` field), replacing
estimates. Coverage notes:
- **YouTube and X: excellent** — real current follower counts + 24h engagement.
- **Instagram: not available** — LunarCrush returns empty follower data for IG, so
  IG counts remain estimate/paste-sourced.
- **Kick / Twitch: not covered** — so for gamblers who are primarily Kick/Twitch
  streamers (e.g. Bouchonnoir, Aiden Gambles, GW1917), the LunarCrush *YouTube*
  number is only their small YT presence, **not** their true live-stream audience.
  Treat those as a floor, not their real reach.
- Several estimates were corrected by real data (e.g. Bouchonnoir 2,850; Aiden
  Gambles 5,930; PokiChloe 136k; Watchfinder 1.17M; Nico Leonard 2.06M).

## Honest data caveats (same walls as before)
- **Follower counts** are ESTIMATE/N-A where social & stats sites block automated
  reads; the Feedspot Pokémon set is real creators but URLs/counts still need
  verification (marked low-confidence).
- **Direct emails are almost entirely unavailable** — anti-bot walls block About-tab
  scraping, and per the project guardrails only *public business* contacts are
  captured (watch dealers list company sites; most creators have none public). This
  is the same enrichment gap flagged throughout — an authenticated analytics/contact
  source unlocks it.
- **"Quantzy" list:** no such file exists in the repo or prior outputs. I merged the
  existing 100-creator roster as the baseline instead. Share the Quantzy list and
  I'll fold it in.
- Nothing here was fabricated and no anti-bot/login wall was bypassed.

## Suggested next steps
1. Confirm GemBreak's exact product so I can re-weight (collectible-breaker-first vs.
   the current unbox-mechanic-first blend).
2. **Enrich the top ~30** (verify counts, pull public business contacts/sites) — the
   Pokémon breakers especially.
3. Feed the enriched shortlist into the Atlas outreach + testing protocol
   (`../outreach/ATLAS_OUTREACH_PLAN.md`).
