# GemBreak — Paid Audience Targeting Brief (competitor-audience acquisition)

_Compiled 2026-07-24. How to reach mystery-pack buyers at scale on Meta & TikTok. Two paths:
(A) native competitor-audience targeting you can run NOW without any upload, and (B) the Custom
Audience upload you populate once you have real PII (email/phone)._

---

## ⚠️ Read this first: handles ≠ uploadable audiences
Meta & TikTok Custom Audiences match on **email, phone, or device ID (IDFA/GAID)** — **not** on
IG/TikTok/X @handles. So our 1,492 buyer-prospect *handles* cannot be uploaded to seed a lookalike
directly. They're valuable for **organic engagement** and as **research** (they tell us who the buyers
are), but the paid engine runs on the two paths below.

---

## Path A — Native competitor-audience targeting (run NOW, no upload)

Both platforms let you reach the competitors' audience *without* PII, using built-in targeting:

### TikTok Ads
- **Creator/Hashtag targeting & "Video interactions":** target users who engaged with mystery-box /
  case-opening content and creators.
- **Interest & behavior:** Collectibles, Trading Cards, Gaming, Luxury, Sweepstakes.
- **Custom Audience from your own pixel:** once GemBreak's pixel fires, build **web-engagement** and
  **video-view** audiences → then **Lookalikes** off *converters* (the gold seed).

### Meta (Facebook/Instagram) Ads
- **Detailed interest targeting:** seed with interests like *mystery box, unboxing, Pokémon TCG,
  Rolex/luxury watches, sports cards, online gaming, sweepstakes* + competitor-adjacent interests.
- **Engagement Custom Audiences:** people who engaged with **your** IG/FB (build this from day 1).
- **Lookalikes** off your pixel converters and your customer list (Path B).

### The competitor angle
You can't target "@packdraw's followers" by name, but you approximate it with the **interest +
behavior + creator** stack above, then let the **pixel + lookalikes** tighten it as data comes in.
Our scraped audience data validates *which* interests/creators to pick.

---

## Path B — Custom Audience upload (populate as PII arrives)

`custom_audience_upload_TEMPLATE.csv` is pre-formatted to Meta's hashed-match schema (works for TikTok
too): `email, phone, fn, ln, ct, st, zip, country, madid`. Fill it from — in priority order:

1. **GemBreak's OWN customer/signup list** — the single best lookalike seed (real buyers). Export and
   drop into this template → Custom Audience → 1–3% Lookalike. **Do this first.**
2. **Opt-in funnel captures** — every email/phone from the "free pack" landing page (age-gated,
   consented) appends here.
3. **The 541 seed emails** already in the template (from our research) — a *directional* "people
   interested in this space" seed. Weaker than real buyers, but usable as a cold interest seed and for
   suppression. Use only if allowed by your terms.

Upload → **Lookalike 1%** (tightest) for prospecting, 1–3% for scale, exclude existing customers.

---

## The full buyer funnel (where audiences plug in)
```
Interest/creator ads (Path A) + Lookalikes (Path B seed)
        → promo-offer creative (free pack / deposit match)
        → landing page (AGE-GATE 18+/21+ + opt-in capture)   ← this creates Path-B PII
        → email/SMS nurture (consented)  → first pack  → pixel converter
        → Lookalike off converters (the compounding loop)
```

## Creative & offer (to convert the competitor audience)
- Hooks pulled from the BrainRot scripts (fast, reactive, the pull = payoff).
- Offers: **free first pack** (top of funnel) → **deposit match** → **refer-a-friend**.
- **Creator-code tie-in** — run creator-whitelisted (Spark/Partnership) ads so the promo comes from a
  trusted creator's handle → highest-converting cold traffic.

## Compliance (gambling-adjacent — hard rules)
- **18+/21+ age-gate** on every ad set + landing page; exclude minors and restricted geos.
- Lead with **collectibles / entertainment / unboxing** framing to pass Meta/TikTok gambling-ad
  policy; have RG (responsible-gambling) messaging + a compliance/legal review before spend.
- Custom Audience data must be collected/consented lawfully (that's why Path B is funnel-first).

## KPIs
Cost per signup · signup→first-pack % · first-pack ROAS · lookalike CAC vs interest-targeting CAC ·
landing-page opt-in rate · converter-lookalike performance over time.

---

### Bottom line
Run **Path A now** (interest + creator + pixel, our research picks the parameters), stand up the
**age-gated opt-in funnel** to manufacture Path-B PII, seed **Custom Audiences from GemBreak's own
buyers**, and let **converter-lookalikes** compound. The handle list drives organic + tells us the
targeting; it is not the upload itself.
