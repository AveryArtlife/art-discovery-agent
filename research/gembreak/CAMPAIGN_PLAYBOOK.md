# GemBreak Creator Growth Engine — Full Campaign Operating Plan

_Compiled 2026-07-20. A hybrid influencer/UGC program: a performance-based **affiliate flywheel**
that feeds a **paid-amplification** engine, run by a small human+AI team. Built on the graded creator
dataset (1,273 verified ≥5K + 2,325 nano) and 2026 benchmark research._

---

## 0. Strategic thesis — "don't pay for reach, pay for proven performance, then amplify it"

Most brands burn budget paying big creators up front for a post and hoping it converts. The
cutting-edge model in 2026 inverts that:

1. **Engine 1 — Affiliate flywheel (low-risk, volume):** put GemBreak in the hands of *many* creators
   on a **commission-only** basis (unique promo code + tracked link). Cost scales only with results.
2. **Engine 2 — Paid amplification (high-leverage):** the affiliate data tells you *which* creators
   and *which* videos actually drive signups and pack sales. You then **license and whitelist only
   those proven winners** and put ad dollars behind them (TikTok Spark Ads / Meta Partnership Ads),
   which run **30–50% cheaper CPA and ~5× ROAS** vs. brand-handle ads.

The flywheel: **Affiliate seeds → performance data → amplify winners → their success recruits more
creators → repeat.** Selection is by **value, not follower count** (see §2). Positioning is
**collectibles/mystery-pack unboxing** (the cheapest legitimate framing — see PRICING_AND_DEALS_2026.md).

---

## 1. How the best brands run this (benchmark synthesis)

- **Whitelisting/Spark Ads:** creators authorize the brand to run ads *through the creator's own
  handle* — native, high-trust. Delivers **30–50% lower CPA**, TikTok reports **+142% engagement /
  +30% completion** vs in-feed ads; agencies report **5×+ ROAS** on whitelisted winners.
  **Golden rule: only amplify content that already proved itself organically.**
- **Affiliate structure:** DTC standard is **tiered commission — 5–10% base climbing to 15–20%** for
  top performers, tracked by **promo code + link**, **30-day attribution**, with **first-touch/
  multi-touch** models favored for content creators (last-click under-credits top-of-funnel creators).
- **Operations:** winners run a **seed-to-scale pipeline** — hundreds of low-cost tests → performance
  tiering → top 5–10% become a **"Creator Council"** (long-term partners). A **CRM pipeline**
  (Cold → Contacted → Shipped → Engaged → Paid → Council) with automated stage triggers is how teams
  handle 25–50+ creators/month. With automation, **prospect→activated partner ≈ 90 days**; without,
  4–6 months.

_Sources: InfluenceFlow, Influencer Marketing Hub, Top Growth Marketing, Tapfiliate, Track360,
Superfiliate, TikTok for Business (2025–2026)._

---

## 2. The Value Partner Score (VPS) — selecting the *most valuable*, not the most-followed

Follower count is the weakest predictor of ROI. VPS ranks creators on what actually drives pack
sales. Each creator scores 0–100:

| Factor | Weight | What it measures | Data source |
|---|---|---|---|
| **Niche/format fit** | 25% | Do they already do opening/unboxing/breaks/gambling content? | our `grade` + `fit_reason` |
| **Engagement quality** | 20% | Real engagement rate (likes+comments ÷ followers), not size | scraped `avg_engagement` |
| **Demographic correlation** | 20% | Audience age/geo/interest match to GemBreak's buyer | ⚠️ enrich on contact (media kit / platform analytics) |
| **Conversion intent** | 15% | Audience is buyers, not passive viewers (promo-code history, shopping content) | bio/link signals |
| **Cost-efficiency** | 10% | Est. cost ÷ expected reach (CPM/CPA) — cheap + engaged wins | our `est_post_*` |
| **Reachability** | 5% | Email > link > none | our `contact` |
| **Authenticity/brand-safety** | 5% | Not spam/farm; disclosure-compliant | our stress-test flags |

**We already hold 6 of 7 inputs** — the gap is **audience demographics** (age/geo/interest split),
which isn't public. Capture it the moment a creator replies (request their media kit, or read it from
TikTok/IG "audience" analytics they share) and lock VPS before any paid spend.

➡️ **Deliverable:** a VPS-ranked "Top Value Partners" list (I can generate v1 from current data on
request; v2 after demographic enrichment). This is the master targeting list — **not** the raw
follower ranking.

---

## 3. Campaign architecture — the seed-to-scale flywheel

```
 SEGMENT ──▶ ACTIVATE (Affiliate) ──▶ MEASURE & TIER ──▶ AMPLIFY (Paid) ──▶ COUNCIL
  cohorts      promo code + link        signups/sales      whitelist winners   top 5–10%
```

**CRM pipeline stages** (every creator is always in exactly one):
`Prospect → Contacted → Negotiating → Signed → Live (code active) → Performing → Amplified → Council`
plus side-states `Paused / Declined / Blocklist`. Automated triggers move records (e.g. *first sale →
Performing*; *≥N sales in 30d → Amplify candidate*).

**Cohort waves** (from our lists):
- **Wave 1 — Warm winners:** Grade A/B breakers + case-opening creators with a contact (the ~403
  START HERE). Highest fit; seed first.
- **Wave 2 — Gambling micro/mid:** proven gambling-content creators (risk-priced, code-first).
- **Wave 3 — Nano seeding army:** the 2,325 nano list — cheap/free product seeding for volume + UGC.
- **Wave 4 — Bridge & mega (selective):** watch×gambling crossover + on-target 1M+ for reach spikes.

---

## 4. The two commercial models

### Model A — Affiliate / Promo (default; ~80% of creators, all nano)
- **Reward = dual trigger:** a **signup bounty** (fixed $ per new registered player) **+ a pack-sale
  commission** (% of pack revenue from their code) — so they earn on both awareness and purchase.
- **Unique promo code** (e.g. `ERIC15`) + tracked link. Code gives the *creator's audience* a small
  perk (bonus pack / deposit match) — this lifts conversion and makes attribution clean.
- **Tiered commission** (climbs with performance):

  | Tier | Trigger | Signup bounty | Pack-sale commission |
  |---|---|---|---|
  | Starter | default | $X / signup | 10% |
  | Performer | ≥25 sales/mo | $X+ / signup | 15% |
  | Elite | ≥100 sales/mo or Council | premium | 20% + bonus pool |

- **Attribution:** 30-day window, **first-touch or multi-touch** (credit the creator who introduced
  the player). **No upfront cost** — pure performance.

### Model B — Paid / Hybrid (top-VPS creators; ~20%)
Layered on top of an affiliate code:
1. **Flat content fee** (recalibrated bands: nano $100–300 · micro $175–900 · mid $600–2,000 per
   cross-posted video).
2. **Whitelisting/usage rights: +25–30%** of base for a 30-day paid-amplification window.
3. **Performance bonus** tied to *your* payoff (e.g. **+$500–1,000 if a video clears 1M views or N
   code redemptions** — self-funding, like the Eric deal).
4. **Amplification:** license the winning organic video → run as **TikTok Spark Ad / Meta Partnership
   Ad** from the creator's handle. **Only videos that already over-index organically get ad spend.**

---

## 5. Outreach system (owned by Atlas)

- **Segmented, multi-touch, personalized — never spray-and-pray.** Each cohort gets its own sequence
  and offer.
- **Sequence (per creator):** T+0 intro (personalized to their recent content + niche) → T+3 value/
  proof follow-up → T+7 offer specifics (code + terms) → T+12 last touch → recycle to DM if no reply.
- **Personalization tokens** pulled from our dataset: `name`, `platform`, `niche`, `fit_reason`,
  recent-post reference, proposed `promo_code`.
- **Domain hygiene:** send from a **warmed secondary domain** (not the primary), authenticated
  (SPF/DKIM/DMARC), capped volume/day to protect deliverability.
- **Throughput target:** 40–75 personalized first-touches/day → ~250–400/week; at ~8–12% reply and
  ~30–40% of replies signing, that's **~15–30 new affiliates/week**.

---

## 6. Negotiation playbook

- **Price guardrails** = the recalibrated bands (§4). Atlas may **auto-agree within band**; anything
  **above band, or any flat fee > $1,000, or any exclusivity request → escalate to PA/you.**
- **Levers (in order to give):** bigger promo-perk for their audience → tier bump → performance bonus
  → whitelisting fee → small flat fee. **Hold the line on:** no large upfront to unproven creators;
  affiliate code always attached; disclosure required.
- **Walk-away:** if a nano/micro demands >2× band flat with no performance component, decline warmly
  and keep in nurture.
- **Escalation matrix:** Atlas handles Model-A affiliate signups end-to-end; **PA + you approve every
  Model-B paid deal and all ad spend.**

---

## 7. Team operating model — you, PA, Atlas (Hermes), Leo (OpenClaw)

> _Assumed capabilities (confirm/correct): **Atlas = Hermes email agent** → inbox, outreach sequences,
> reply handling, in-band negotiation, scheduling. **Leo = OpenClaw agent** → browser/computer-use
> automation → operating web dashboards (affiliate platform, ad managers), generating promo codes,
> pulling Spark-Ad auth codes, uploading creatives, scraping performance, updating the CRM, DM
> outreach where email is missing._

| Function | You | PA (human) | Atlas (email) | Leo (browser) |
|---|---|---|---|---|
| Strategy, budget authority | **A/R** | C | I | I |
| Prospect list / cohorts | A | R | C | **R** (enrich/scrape) |
| Outreach & follow-up | I | C | **R** | C (DM fallback) |
| Affiliate negotiation (Model A) | I | C | **R** | I |
| Paid deal negotiation (Model B) | **A** | **R** | C | I |
| Promo-code + link creation | I | A | I | **R** |
| CRM pipeline updates | I | C | C (email side) | **R** (dashboard side) |
| Ad manager / Spark Ads setup | A | C | I | **R** |
| Performance reporting | A | R | I | **R** (data pull) |
| Contracts & signatures | A | **R** | C | I |
| Payments / commission payouts | **A** | **R** | I | C |
| Compliance / disclosure QA | A | **R** | C | C |

_A=Accountable, R=Responsible, C=Consulted, I=Informed._

**Handoff automation (the "conveyor belt"):**
`Atlas books a yes → Leo generates the promo code + tracked link → Leo creates the CRM record (Live) →
Atlas emails the creator their code + assets → Leo watches the dashboard; on first sale flips record
to Performing → on threshold, Leo flags Amplify candidate → PA/you approve → Leo requests Spark code &
launches the ad → weekly, Leo compiles the scorecard.`

---

## 8. Tech & tracking stack (minimal, integratable)

- **Affiliate/tracking platform** (promo code + link + commission tiers + payouts): e.g. Tapfiliate /
  Refersion / PartnerStack / Social Snowball class. This is the system of record for Model A.
- **Promo-code + UTM convention:** one code per creator; UTMs on links for multi-touch attribution.
- **Ad accounts:** TikTok Ads Manager (Spark Ads) + Meta Business Manager (Partnership Ads).
- **CRM/pipeline:** a board (Notion/Airtable/HubSpot) mirroring the §3 stages, driven by Leo.
- **Payments:** mass-payout rail (PayPal/Wise/Tipalti) for commissions; contracts via e-sign.

---

## 9. Compliance & brand safety (non-negotiable for a gambling-adjacent product)

- **FTC disclosure** on every post (#ad/#sponsored + clear language); bake it into contracts and QA
  each live post (Leo screenshots; PA reviews).
- **Legal/brand-safety review** before launch — GemBreak is gambling-adjacent (loot-box/unboxing
  scrutiny). Age-gate creators' audiences (18+/21+ as required); avoid youth-skewing creators.
- **No fabricated "wins"** / no stacking creator packs with guaranteed grails (the Polymarket &
  mystery-box scandals are the cautionary tale). Authentic pulls only.
- **Fraud/leak monitoring:** watch for code-leak to coupon sites (cap those or new-customer-only),
  self-referral, and bot signups. Reserve the right to claw back.

---

## 10. Metrics & optimization

- **North star:** blended **CAC** and **ROAS**; secondary **cost-per-signup** and **cost-per-pack-sale**.
- **Per-stage KPIs:** outreach reply %, signup→live %, % of live creators with ≥1 sale, revenue per
  creator, organic→amplify hit rate, Spark-Ad ROAS.
- **Scale/kill rules:** creator with 0 sales in 30 days → nurture/pause; video >2× median organic
  conversion → amplify; Spark Ad ROAS <1.5 after $X → cut; ROAS >3 → scale budget.
- **Cadence:** Leo compiles a **weekly scorecard**; monthly tiering review (promotions/Council).

---

## 11. 90-day rollout roadmap

| Phase | Weeks | Focus | Key actions | Lead |
|---|---|---|---|---|
| **0 — Infra** | 0–2 | Stand up the machine | Affiliate platform + codes schema, ad accounts, CRM board, warmed domain, contract + FTC templates, legal sign-off | PA + Leo |
| **1 — Seed** | 2–6 | Affiliate flywheel on | Outreach Wave 1 (403 START HERE) + Wave 3 nano seeding; activate codes; first sales data | Atlas + Leo |
| **2 — Tier & first amplify** | 6–10 | Find & fund winners | Performance tiering; license top organic videos; launch first Spark/Partnership Ads; Wave 2 gambling | Leo + PA + you |
| **3 — Scale & Council** | 10–13 | Compound it | Scale winning ads; form Creator Council (top 5–10%); Wave 4 selective mega; systematize renewals | You + PA |

**Targets by day 90:** ~150–250 active affiliates, 15–30 amplified winners, a 10–20 creator Council,
and a measured blended CAC you can scale against.

---

## 12. Illustrative unit economics (fill with real GemBreak numbers)

- **Affiliate (Model A):** cost = commission only → CAC = bounty + (pack-commission × sales). If
  bounty $Y and commission 12%, a creator driving 40 pack-sales/mo at $Z AOV costs you exactly
  `(40×$Y) + (0.12×40×$Z)` — **you never pay more than performance justifies.**
- **Paid (Model B):** budget only proven videos. Example: license a winner for $500 + $150 rights,
  put $2,000 Spark spend behind it at 4× ROAS → $8,000 attributed → blended CAC well below brand-handle
  ads.
- **Blend:** aim **70–80% of *budget* on affiliate/performance, 20–30% on amplifying winners** early;
  shift toward paid as you learn which creators/videos compound.

---

## 13. Immediate next actions (this week)

1. **Confirm agent roles** (Atlas/Leo capabilities as assumed in §7) and pick the **affiliate platform**.
2. I generate the **VPS "Top Value Partners" v1** from current data (value-ranked, not follower-ranked).
3. Build the **Atlas outreach pack**: 3 sequences (Wave 1 / gambling / nano) + personalization mapping
   from the dataset, wired into `ATLAS_OUTREACH_PLAN.md`.
4. Define the **commission schema** (bounty $, tiers, attribution window) so Leo can create codes.
5. PA + legal: contract template + FTC/age-gate sign-off.

_This plan pairs with: `GemBreak_Influencer_Lists.xlsx` (targets), `PRICING_AND_DEALS_2026.md`
(rate/deal benchmarks), `ATLAS_OUTREACH_PLAN.md` (outreach ops)._
