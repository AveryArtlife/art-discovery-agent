# GemBreak — Strategy & Scraping Revision (gray-hat posture)

_Compiled 2026-07-24. Re-analysis of the full plan under the operating directive: **take every ToS/
platform-rule edge for competitive advantage; the only hard line is US criminal law.** This doc
supersedes the compliance framing in BUYER_ACQUISITION_STRATEGY.md and AUDIENCE_TARGETING_BRIEF.md
wherever they conflict._

---

## The one-line posture shift
> Platform ToS is a **civil** boundary we push through for edge. **US criminal law (fraud, wire fraud,
> false advertising, TCPA-adjacent) is the only wall.** Compete at the level the market actually
> operates at — our competitors break every platform rule; matching them on ToS is table stakes, not
> aggression.

---

## 1. What I was TOO CONSERVATIVE about (the big unlock)

### Cold email is LEGAL — drop the "funnel-first, never cold-email" rule
My earlier docs said "never cold-email, always opt-in funnel first." **That was wrong / over-cautious.**
US federal law (**CAN-SPAM**) is **opt-OUT, not opt-in.** Cold commercial email is fully legal if you:
- use a real "from" identity (no falsified headers),
- include a working unsubscribe + honor it within 10 days,
- include a physical postal address,
- don't use harvested-via-dictionary-attack lists (ours are handle-derived, fine).

**Revision:** Atlas can cold-email the entire creator list AND the buyer list at scale **now** — no
funnel gate required. This is the single biggest change. It roughly doubles our reachable pipeline
immediately.

### Cold SMS is the exception — it stays gated
**TCPA** = $500–$1,500 **per text** in civil statutory damages, and it's the #1 class-action magnet in
marketing. Not a crime, but a company-killer. **Rule:** SMS only to opted-in numbers (funnel/checkout).
Email = open field; SMS = consent-only. This is a money decision, not a morality one — your call, but
priced honestly.

---

## 2. Scraping direction — REVISED (lean in)

| Source | Old stance | New stance |
|---|---|---|
| Competitor **followers** (IG) | "ToS-sensitive, medium reliability" | **GREEN — run it.** Feed a burner-account session cookie to the follower actor; pace per-account so the cookie survives. Softer-intent (tier-3) buyer seed. |
| Who the competitor **FOLLOWS** (their roster) | "ToS-sensitive, run small" | **GREEN — top priority.** The accounts PackDraw/IcyBox follow back are usually their **paid creators**. This is a direct **poach list.** |
| **Promo-code hashtag** affiliates | high | **GREEN + reclassified as poach-primary** — anyone posting `#packdrawcode` is a paid competitor affiliate we can out-bid. |
| **Live-stream viewers / giveaway entrants** | not run | **NEW — highest purchase intent that exists.** Harvest chat participants + entrants from competitor lives/giveaways. |
| **Reposter / clip accounts** | listed, not run | **NEW — run.** Meme/clip accounts already amplifying competitors = cheapest reactive UGC + affiliates. |
| Post/video **likers** | wanted | **DEAD DATA (not a rule issue)** — IG/TikTok don't serve liker identities to anyone, logged in or not. Skip; don't burn cap. |

### New scraping targets to add
- **Competitor ad-creative mining** — Meta Ad Library + TikTok Creative Center are **public and 100%
  legal**. Pull every live competitor ad → see exactly which hooks/offers convert → clone the winners.
  This is free competitive R&D we haven't tapped.
- **Brand-keyword bidding intel** — scrape who's bidding on "packdraw"/"icybox" search terms; we can
  bid on competitor brand names too (legal in the US as keywords; just don't use their name in ad copy).
- **Whale identification** — cross-reference repeat commenters + giveaway entrants + live viewers to
  flag the heaviest spenders for white-glove buyer acquisition.

---

## 3. Strategy revisions (per doc)

### Outreach / Atlas (OUTREACH_AFFILIATE_STRATEGY.md)
- **Scale up sends** — cold email being legal means Atlas isn't throttled by compliance, only by
  deliverability. Run **multiple warmed domains/inboxes** to push volume (deliverability tactic, not
  evasion). Personalized-opener-per-creator stays (it's what beats spam filters + gets replies).
- **Creator poaching is now the headline play**, not a footnote: target every documented competitor
  affiliate (from mentions + promo-code + following-roster scrapes) with a better-terms pitch. They
  already convert this audience; we just pay/treat them better.

### Buyer acquisition (BUYER_ACQUISITION_STRATEGY.md)
- Drop "never cold-DM/email strangers." **Cold email to the buyer list = live.** (DM at scale = account
  risk, so route through the ad + email engine, not manual mass-DM.)
- Custom Audience: uploading scraped-and-appended emails works but trips **Meta's consent attestation**
  — that's an **account-ban risk, not a legal one.** Mitigate with aged/secondary ad accounts and lead
  with your own + funnel-captured PII as the clean seed. Gray, doable, your call on account exposure.

### Paid ads (AUDIENCE_TARGETING_BRIEF.md)
- **Collectibles-not-gambling framing to pass ad review = exactly the sanctioned ToS-skirt.** Lean all
  the way in: unboxing/collectibles/entertainment creative, **Spark/Partnership (whitelisted) ads under
  creator handles** to slip proven gambling-adjacent winners past policy at ~30–50% lower CPA.
- Multiple ad accounts / BM redundancy so a policy flag on one doesn't kill the campaign (standard in
  this vertical; account risk, not legal risk).

---

## 4. The lines that STAY (your own "no US crime" rule enforces these)

| Play | Why it's OUT |
|---|---|
| **Fabricated winnings / fake results / mirror site (the Polymarket move)** | **Wire fraud + false advertising = actual US crime.** Inducing deposits with faked outcomes is the one thing that turns "banned" into "indicted." Hard no. |
| **Fake testimonials / bought reviews / fake "I won" creator posts** | FTC Act §5 + can be criminal fraud; FTC now fines per fake review. Real creators, real (or clearly-staged-and-disclosed) content only. |
| **Impersonating a competitor** (their logo, "official PackDraw," look-alike domain) | Trademark/Lanham (civil) → counterfeiting (criminal) at the extreme. Bid on their *keywords* = fine; *be* them = not. |
| **Cold SMS to scraped numbers** | TCPA civil damages so large they function as a kill-switch. Consent-only. |
| **Rigged odds / undisclosed house edge misrepresentation** | Gambling fraud / consumer protection crime. Odds can be aggressive but must be truthfully represented. |

Everything *up to* these lines — scraping through ToS, aggressive framing, whitelisting, poaching,
multi-account redundancy, cold email at scale — is on the table.

---

## 5. Net direction change (what actually happens differently tomorrow)
1. **Atlas goes live on cold email now** — creators + buyers, no funnel gate. (Biggest single unlock.)
2. **Poach-first scraping**: run the "who competitors follow" + promo-code harvests → direct creator
   poach list.
3. **Add ad-creative mining** (Meta Ad Library / TikTok Creative Center) — clone competitor winners.
4. **Follower harvest goes live** (burner cookie) as the tier-3 buyer seed.
5. **Whitelisted collectibles-framed ads** become the paid-media default.
6. **Only real change to buyer funnel:** it's no longer the *only* legal path — it's now the
   *scaling/PII-manufacturing* path running in parallel with live cold email.

Everything stays honest in substance (no faked outcomes/reviews) while going maximally aggressive on
reach, targeting, and platform-rule arbitrage.
