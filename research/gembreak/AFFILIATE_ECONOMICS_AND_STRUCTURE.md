# GemBreak — Affiliate / Influencer Fee Structure & Unit Economics

_Compiled 2026-07-24. How competitor mystery-pack sites structure promo-code deals (user-side incentive
+ influencer-side offer), and — given GemBreak pays a product cost AND cashes back most of the pack
price — how to structure affiliate fees so the program is ALWAYS profitable. Pairs with
THEBADDEST_OUTREACH_CAMPAIGN.md and GEMBREAK_MASTER_STRATEGY_2026.md._

---

## Part 1 — How competitors structure promo-code campaigns (audit synthesis)

Every site runs the **same dual-benefit code**: one code that rewards the audience AND pays the creator,
so the audience *wants* to enter it (not just the creator to share it).

| Site | What the USER (audience) gets via the code | What the INFLUENCER gets |
|---|---|---|
| **PackDraw** | Permanent **5–10% deposit bonus on every deposit** | Per-open commission on their **custom packs** + deposit-based % — **exclusivity required** (can't promote rivals or your % resets to 0) |
| **HypeDrop** | 5% deposit bonus + **3 free boxes** | **0.6% → 10%** of every referred deposit, tiered up by volume (withdrawable anytime) |
| **Jemlit** | Free box + deposit boost | **8% of every friend's deposit** (recruited programmatically via Indoleads network) |
| **Clash.gg** | 5% deposit bonus + **daily free case** + rakeback | Commission + **3% on custom-case opens**; **>$3M paid** to affiliates |
| **Cases.gg** | Daily free boxes + deposit bonus | **Up to 45% revshare** on active referred players; custom-box building unlocks at level 5; **>$3M paid** |
| **RillaBox** | **20% deposit bonus** + daily free box | **Two-sided: $7 to referrer / $4 to friend** when friend deposits ≥$25 |
| **CSGORoll** | 3 free cases + 5% deposit bonus | Tiered % of referred deposits + event invites; **$8.7M** earned by top influencers collectively |

**Sweepstakes-casino benchmark (the mainstream-scale version):** CPA **$25–120**/qualified player ·
RevShare **25–45% of NET** · Hybrid (**$25–50 CPA + 15–25% revshare**) · 30–90-day cookie. Stake.us goes
to 45% revshare + 10% of house edge.

### The three patterns to copy
1. **Dual-benefit code** — user perk + creator payout on one code (self-propagating).
2. **Commission on referred DEPOSITS / NET, tiered by volume** — never a flat fee per post.
3. **Custom-pack ownership** — the highest-value hook: creators earn per-open on packs they build (turns
   them from endorsers into storefront owners). *This is our biggest structural opportunity.*

---

## Part 2 — ⚠️ The margin trap (why this needs its own math)

A mystery-pack site is **not** a normal e-commerce store with 50% product margins. Two costs eat the
pack price:

1. **Product/inventory cost** — the items in the pack.
2. **Cashback / RTP** — you return most of the pack price as pull value (users can sell back / cash out).
   Mystery sites run **high RTP (≈85–95%)** to stay attractive (Stake Cases advertise 98% RTP).

**So your real margin per pack is small — the "house edge," not the pack price.**

> **Worked example.** Pack price **$100**, RTP **90%** → you pay out **$90** in pull value → **gross
> margin = $10/pack (10% house edge).** Now pay an affiliate the "industry-sounding" **20% of pack
> price = $20**. You just **lost $10 on every pack they sell.** The more they sell, the more you lose.

**This is the #1 mistake to avoid: never pay commission on gross pack sales or gross wager.** At a 10%
house edge, any gross-based commission above ~10% is unprofitable *before* payment fees and user bonuses.

---

## Part 3 — The rule that makes it always profitable

**Pay commission on NET REVENUE — the money you actually keep — not on gross pack sales.**

Define the waterfall (this is the sweepstakes/iGaming standard, adapted):

```
Gross pack sales (from the code's referred users)
  − Cashback / pull value paid out (RTP)          ─┐
  − Product / fulfillment cost                      ├─►  = GROSS MARGIN (house edge)
  − Payment processing (~2–3%)                      │
  − User promo bonus (the code's deposit match/free pack) ┘
  ─────────────────────────────────────────────
  = NET REVENUE (NGR)  ◄── commission is a % of THIS
```

Because commission is a **share of money you already netted**, the program is **self-financing by
construction** — you can never pay out more than the profit the creator generated. This is the single
most important design decision.

**Equivalent simpler proxy (easier to track):** **Net Deposits = deposits − withdrawals/cashouts** from
the code's users. Over a player's lifetime, net deposits ≈ what the house keeps (the RTP just determines
how long the money churns before the edge captures it). Revshare on net deposits ≈ revshare on NGR and
is just as safe. Use whichever your platform tracks cleanly.

### Two guardrails borrowed from iGaming (both protect you)
- **Negative carryover:** if a creator's referred cohort is net-negative in a month (big winners cashed
  out), that shortfall **carries forward** against their next month's commission — so one lucky whale
  doesn't cost you a commission on a loss.
- **Bonus & fee netting:** the user-side incentive (deposit bonus / free pack) and payment fees are
  subtracted **before** the commission %, so the creator shares net-of-promo profit, not gross.

---

## Part 4 — The tiered deal structure (what to actually offer)

All tiers pay backend commission **on NET REVENUE**. Tiers differ in the **upfront** and the **%**.

> **Micro creators get the SIMPLE version — see CREATOR_DEAL_CARD.md.** The table below is the internal
> accounting; a micro creator is only ever pitched: *"$25 per customer who deposits $50+ and opens a
> pack, + 5% of their spend for life, stepping up to 10%, free pack for your followers, no upfront."*
> The net-deposit basis + qualifier + carryover keep that simple pitch profitable.

### Illustrative economics (replace with GemBreak's real numbers)
- House edge (gross margin): **10%** of pack sales · Payment fees: **3%** · User bonus: **5%**
- ⇒ **NGR ≈ 2% of gross pack sales** in a naive single-pass… **BUT** with replay/churn, **NGR ≈ net
  deposits**. Assume avg **90-day net revenue per activated depositor = $80** (whales lift this).
- Avg first deposit ~$50; qualified depositor = deposits ≥ $20.

| Tier | Who | Upfront | Backend (revshare on NGR / net deposits) | Signup bounty (CPA) | Guardrail |
|---|---|---|---|---|---|
| **Micro / Nano** | <50K, most of the list | **$0** | **30–40%** | optional **$15–30** per qualified depositor | CPA capped ≪ $80 LTV; pure performance |
| **Mid** | 50K–500K | **Recoupable advance $250–1,000** | **25–30%** | — (rolled into advance) | Advance **recouped from their backend before further payout**; size to confidence |
| **Large / Hero** | 500K+ / proven | **Flat content fee $1,000–2,500** (non-recoupable) + whitelisting +25–30% | **20–25%** | — | Fee justified by **Spark-Ad amplification ROAS**, not affiliate alone (Engine 2 budget line) |
| **Custom-Pack Partner** | any tier, high-fit | $0–advance | **per-open commission on their branded pack** (e.g. 3–5% of pack price *from the house edge*) + referral revshare | — | Per-open % must sit **inside** the house edge |

### Why each upfront is safe
- **Micro = $0 upfront, higher %:** you pay only from realized net revenue. The higher 30–40% share is
  affordable *because* it's a share of profit, and it makes "no advance" attractive to volume creators.
- **Mid = recoupable advance:** you advance $250–1,000, but it's **recouped from their own backend
  commission** before they earn more — like a record-deal advance. Worst case (cohort underperforms) you
  eat the gap between advance and earned commission, so **size the advance to ~1 month of their expected
  25–30% revshare**, not to their follower count.
- **Large = flat fee + whitelisting:** this is really **Engine 2 (paid amplification)** — you're buying
  content + ad rights whose ROAS you measure directly (only amplify proven organic winners), plus a
  lower backend %. Different budget line from pure affiliate.

### Worked P&L per tier (illustrative)
- **Micro, 35% revshare:** referred cohort nets **$2,000** over 90 days → creator earns **$700**, you
  keep **$1,300**. Cost only when profit exists. ✅
- **Mid, $500 advance + 25%:** cohort nets **$4,000** → 25% = **$1,000**; minus $500 recouped advance →
  **$500 more paid**; total creator **$1,000**, you keep **$3,000**. ✅ (If cohort only nets $1,200 → 25%
  = $300 < $500 advance → you're **−$200** on the advance: the sized risk of the mid tier.)
- **Large, $1,500 fee + 20% + $2,000 Spark spend:** judged on blended ROAS; amplify only if the organic
  video already over-indexed. Affiliate backend is upside on top.

---

## Part 5 — The user-side incentive (fund it from margin, count it before commission)

What the code gives the audience (pick 1–2, keep it inside the margin math):
- **Free first pack / no-deposit bonus** — lowest friction (biggest signup lift). Cost = one pack's edge.
- **Permanent 5–10% deposit bonus** (the PackDraw/HypeDrop standard) — ongoing reason to keep the code.
- **Bonus packs / daily free pack** — habit loop.

Every one of these is subtracted in the NGR waterfall **before** the creator's commission — so the
creator shares the profit *after* the audience perk, and the perk never pushes you underwater.

---

## Part 6 — Anti-leak / fraud guardrails (protect the margin)
- **Min-deposit qualification** ($20) before any CPA/bounty triggers — kills bonus-only tourists.
- **New-customer-only codes** + coupon-site monitoring (cap leaked codes).
- **Self-referral & bot detection**; clawback rights in the contract.
- **Negative carryover** (Part 3) so cashed-out winners don't generate a commission.
- **KYC at cash-out** — the compliance + fraud chokepoint (also the legal-moat point from the master
  strategy).

---

### Bottom line
1. **Never pay on gross pack sales** — at a ~10% house edge, gross-% commission loses money.
2. **Pay a % of NET revenue / net deposits** — self-financing; you only ever share realized profit.
3. **Micro = $0 upfront + 30–40% backend + small capped CPA.** **Mid = recoupable advance + 25–30%.**
   **Large = flat fee + whitelisting + 20–25% (Engine 2).**
4. **Custom-pack ownership** (per-open % inside the house edge) is the highest-alignment, most scalable
   hook — build it.
5. **Netting + negative carryover + min-deposit + KYC** keep every tier structurally profitable.
