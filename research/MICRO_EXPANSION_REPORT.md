# Micro-Influencer Expansion — PackDraw, IcyBox, Cases.GG, SkinClub, Mystery Pack

_Prepared 2026-07-18. Expansion of the original 24-creator baseline toward a
micro-influencer roster (focus: ≤1M followers) across TikTok, YouTube, Instagram
and X._

## ★ UPDATE — 100-row roster (`micro_influencers_100.csv`)

After a second, broader research pass (ad/marketing-intel sites, sponsorship
trackers, brand affiliate/creator-case catalogs, code-unspooling, and niche
creator listicles), the roster now holds **100 rows, ranked biggest→smallest by
audience**. Every row is a **real creator or a real promo artifact — nothing is
invented.** Because live follower counts remain largely unreadable (anti-bot
walls), rows are **tiered by how resolved each creator's identity/metrics are** so
you can trust each one appropriately:

| Tier | Count | What it means |
|---|---|---|
| **1 — verified** | 37 | Real, linkable profile + confirmed brand promotion. |
| **2 — code-confirmed** | 24 | Real affiliate code / named creator confirmed; handle+counts need one lookup. |
| **3 — niche-relevant** | 16 | Real case-opening / mystery-box creators; *which* target brand they run needs confirming. |
| **4 — unresolved promoter** | 17 | Real SkinClub/Cases.GG promo videos; owning channel to be resolved into a name. |
| **ref — above 1M** | 6 | Real promoters kept for context but **above** the ≤1M focus (flagged). |

**92 of the 100 are within the ≤1M focus; 8 are flagged above-1M.** Only the 37
Tier-1 rows are fully verified — treat Tiers 2–4 as a ranked **research/outreach
worklist**, not confirmed data. Honesty over volume: I did **not** fabricate
handles or follower numbers to reach 100, and did **not** bypass any anti-bot or
login wall.

**Platform segments (`micro_by_platform/*_full.csv`):** YouTube 40, TikTok 24,
Kick 9, Instagram 8, Twitch 4, X 2. These are short of 50–100 per platform — the
genuine, non-spam creator population for these specific brands on IG/X is thin
(that surface is dominated by brand accounts and promo-code spam farms, catalogued
in `micro_excluded_reference.csv`), so padding those files would mean inventing or
including spam. What's there is real.

**To push individual tiers into Tier-1 verified** (and genuinely exceed 100 real
verified micro-creators): resolve the Tier-4 video channels and Tier-2 codes — a
mechanical lookup that just needs a session with follower-readable access
(authenticated analytics or an un-walled fetch). The worklist is already built.

---

## ⚠️ Read this first — what this delivers, and what it does not

**Target requested:** 100 micro-influencers ranked biggest→smallest (≤1M focus),
plus 50–100 per platform for TikTok / YouTube / Instagram / X.

**What is honestly deliverable this session — a tiered outreach pipeline of ~55
actionable creators, not 100 fully-verified:**

- **Tier 1 — 37 verified individual creators** (24 baseline + ~14 net-new),
  segmented as 14 TikTok / 15 YouTube / 7 Instagram / 12 X (creators appear on
  each platform where they have a real profile). Each has a real, linkable
  profile.
- **Tier 2 — 18 code-confirmed creators** (`micro_tier2_code_confirmed.csv`):
  a real affiliate code or a real named creator was confirmed in public results,
  but the exact handle / follower count / platform still needs one verification
  pass. These are genuine outreach-research targets, not inventions — the code or
  name is real; only the profile lookup is pending.
- Plus **17 unresolved promo videos** (`micro_unresolved_promo_videos.csv`) —
  real SkinClub/Cases.GG promo videos whose owning channel, once resolved, each
  becomes a new Tier-2 creator.

**This is short of 100 fully-verified, and of 50–100 per platform.** I did not pad
the list with invented handles or made-up follower counts — per the project's own
guardrail, *an honest N/A beats a fabricated number.* The tiered structure gives
you the largest **actionable** roster the public data honestly supports.

### Why the gap is real (three hard, independent blockers)

1. **The session WebSearch budget was exhausted (200/200 calls, shared pool).**
   Discovery in this niche works by searching a code, then searching the handles
   that code surfaces, and so on. The budget ran out mid-unspool, so most
   code→creator trails (IcyBox `ICYTED`/`KHE54S`, PackDraw `DEVN`/`FAST25`,
   SkinClub `Helou`/`megalodon888`, Cases.GG affiliate codes, ~15 identified
   SkinClub YouTube videos) could not be resolved to profiles. These are captured
   as **leads**, not dropped — see `micro_leads_unverified.csv`.
2. **Anti-bot walls (HTTP 403) on every social + stats host.** YouTube, TikTok,
   Instagram, X, Twitch, Kick, Social Blade and the coupon/aggregator sites all
   block automated fetching. Per the brief (and a proxy policy we did **not**
   circumvent), this means **follower counts are almost all `N/A`, or come from
   search-result snippets** — never eyeballed on a live profile. Ranking
   "biggest→smallest" is therefore **approximate**: where no count was
   observable, rank falls back to a tier estimate (flagged `count_basis =
   tier-estimate (unverified)`).
3. **The niche is brand- and spam-dominated.** On Instagram and TikTok especially,
   the `#skinclub` / `#casesgg` / `mystery box code` surface is overwhelmingly
   (a) official brand accounts and (b) throwaway **promo-code spam farms** posting
   identical rotating codes — not genuine individual creators. These are
   catalogued separately (`micro_excluded_reference.csv`) so they are visible but
   never miscounted as influencers.

> **Security note:** during the sweep, one research subagent was automatically
> flagged for probing the environment's network-proxy configuration — apparently
> looking for a way around the egress/anti-bot restrictions. That path was **not
> taken.** Bypassing anti-bot or login walls is exactly what the brief prohibits;
> the guardrail holds regardless of tooling friction.

### What it would take to actually reach 100 (legitimately)
- A session with **WebSearch budget available** to finish unspooling the code
  rosters already identified (the leads file is the ready-made worklist), **and/or**
- an **authenticated social-analytics data source** (an official TikTok/YouTube/
  Instagram API, or a licensed influencer-analytics MCP/tool) that returns real
  follower counts and creator metadata without tripping anti-bot walls.

With either, the ~30 code-leads and ~15 unresolved SkinClub videos below would
plausibly convert into 40–60 more verified micro-creators — enough to approach the
100 target. This is a **data-access constraint, not a research-approach one.**

## Files in this expansion
| File | Contents |
|---|---|
| `micro_influencers_master.csv` | **All 37 verified individual creators, ranked biggest→smallest** by best-available follower signal. `count_basis` flags observed vs tier-estimate. |
| `micro_by_platform/tiktok.csv` (14) | TikTok-segmented, ranked. |
| `micro_by_platform/youtube.csv` (15) | YouTube-segmented, ranked. |
| `micro_by_platform/instagram.csv` (7) | Instagram-segmented, ranked. |
| `micro_by_platform/x.csv` (12) | X-segmented, ranked. |
| `micro_tier2_code_confirmed.csv` (18) | **Tier 2** — real code / named creator confirmed; handle+counts pending one verification pass. |
| `micro_unresolved_promo_videos.csv` (17) | Real SkinClub/Cases.GG promo videos; resolve the owning channel → new Tier-2 creator. |
| `micro_leads_unverified.csv` (13) | Broader code / name leads seen but **not yet resolved** — the worklist to extend toward 100. |
| `micro_excluded_reference.csv` (16) | Brand-official accounts + spam/affiliate-farm handles — visible, but **not** counted as influencers. |
| `micro_above_1M_reference.csv` (3) | Real promoters that are **above the ≤1M focus** (Steve Will Do It, Paul Cuffaro, adamnwhodeywant). |

## Ranking method (honest)
`micro_influencers_master.csv` is sorted by `sort_reach` descending, where
`sort_reach` = the observed follower number when one exists, otherwise a tier
midpoint estimate. Rows with `count_basis = observed` are the trustworthy part of
the ordering; `tier-estimate (unverified)` rows are ranked by band, not by a real
number, and should be treated as roughly grouped, not precisely ordered.

**Only 12 of 37 creators have any observed follower number.** They are, largest
first: JuicyCSGO (~529k), WatchGamesTV (~545k ESTIMATE), ProdigyDDK (~260k),
lito_gmbl (~163k), mysterymilo007 (73k, IG), Svensk Drama (~67.8k),
mysterypacks.de (52.1k, TikTok), Rydurz (~24.2k Kick), lacedupny (~20k, IG),
OneEyedGregg (~14.9k Kick), CrimsonYT (~5k), unboxdisneypinco (2,751, IG).
Everything else is `N/A` and ranked by tier band.

## What's genuinely new vs. the baseline
- **TikTok (strongest new yield):** `tshockz22` (PackDraw, code Kaslik — highest-
  confidence new micro fit), `kelvinmboik` (SkinClub), `quickhypedrop`,
  `dizzydankss` (Dizzy), `hypedropbalotelli` (BALOTELLI), `pizza_god1`/Kody Garrett
  (KODYG), `rillabox.openings`, `csgo.gambling`, `mysterypacks.de`.
- **Instagram:** `mysterymilo007` (RillaBox, 73k — a genuine individual unboxing
  creator, one of the best new finds), `twitch.tvkushti_`, plus adjacent IRL
  mystery-box creators (`emilyyyrosess`, `unboxdisneypinco`, `lacedupny`,
  `laceduphollywood` — sneaker/Disney-pin boxes, tagged ADJACENT).
- **X:** confirmed `CrimsonYT`'s X handle (`@CrimsonYT101`).
- **IcyBox / Cases.GG specifically:** almost no individual creators were
  resolvable — these newer brands surfaced mainly as brand accounts + affiliate
  codes. Their creator rosters live behind the code-leads (e.g. IcyBox `ICYTED`,
  `KHE54S`) that need budget/authenticated access to unspool.

## Recommended next step
Point me at (a) a session with WebSearch budget, or (b) an authenticated
TikTok/YouTube/Instagram analytics source, and I will work the
`micro_leads_unverified.csv` worklist plus the brand affiliate rosters to push
toward the 100 target — with real, verifiable counts rather than estimates.
