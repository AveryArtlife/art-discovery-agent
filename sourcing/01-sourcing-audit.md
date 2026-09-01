# Global Sourcing Audit — Individual MRE-Style Meals for a Mexican Institutional Customer

Date: 1 September 2026
Scope: individual sealed meal packets (NOT 24-hour ration packs). Pilot 3,500 meals;
follow-on potentially 25K / 100K / 250K / 500K / 1MM+.

> **Verification ceiling:** all research in this document was performed through
> search-engine retrieval only. Direct website access was blocked by this
> environment's egress policy (HTTP 403 on every host tested, including
> `dla.mil`, `ameriqualgroup.com`, `sopakco.com`). No primary document was
> opened. See `00-README.md`. Confidence tags: `FACT (search)`, `ESTIMATE`,
> `ASSUMPTION`, `UNKNOWN`.

---

## 1. Executive summary

**Nine things that change how you should run this deal.**

1. **The customer's reference sample is a genuine U.S. Government Property MRE
   that cannot legally be resold — and the spec it sets is your Spec B, not your
   Spec A.** They photographed a DoD MRE (Menu 21, AmeriQual, marked *"Commercial
   Resale is Unlawful"*). See §1.5 and §1.6 for what that means and what to buy
   instead. Independently, their national standard points the same way: Mexico's SEDENA issues a *"Ración Diaria Individual de
   Combate"* — a daily box **containing three individual meal packs**, totalling
   **3,640–4,030 kcal/day**. That is **~1,213–1,343 kcal per individual meal**, and
   each meal pack carries **two retort pouches** (a meat item and a staple).
   `FACT (search)` — Wikipedia "Field ration" / MREInfo, retrieved 1 Sep 2026.
   Your "three packets per day" requirement is not a coincidence: it is the
   incumbent Mexican architecture. **Quoting only the 900–1,100 kcal value config
   risks failing qualification on calorie count alone.** Lead with Config B.

2. **The $4.17/meal APack number is not a factory price and is not repeatable.**
   It is clearance pricing on a **dormant retail line**. See §3. Do not build a
   model on it.

3. **The real benchmark for a US MRE is roughly 3x that.** DLA's FY24/FY25
   standard price for a case of 12 MREs is **$150.32 → $12.53 per meal**.
   `FACT (search)`. That is DLA's internal sales price, not contractor cost, but
   contractor cost is nowhere near $4.17.

4. **The one genuinely hard government unit price I found is the Humanitarian
   Daily Ration: $42.00–$43.00 per case of 10 individual bags → $4.20–$4.30 per
   ration.** `FACT (search)`, from a DLA solicitation document (c. 2011). That is
   the closest thing to a floor — and it is for a **vegetarian, no-meat, no-FRH,
   single-bag** ration bought at enormous scale over a decade ago. It is a floor,
   not a comparable.

5. **Your price targets are half right.** `$4.00–$7.00 factory for a premium
   US-MRE-equivalent` is **not achievable from a US manufacturer** — expect
   roughly $8.50–$12.00. It **is** plausibly achievable from Turkey, Malaysia,
   Singapore, Poland or South Africa at 100K+. `$2.50–$4.50 for the value config`
   is achievable only at the **top** of that band, only at 250K+, and realistically
   only **without** an FRH. See §6.

6. **Spain is structurally the best product match and nobody has priced it that
   way.** Jomipsa already manufactures the **UAE Type C ration: a bagged,
   MRE-style, three-meal 24-hour pack at 3,400 kcal** `FACT (search)` — the same
   architecture Mexico uses. Spanish-language packaging is native, not a
   customisation charge. Jomipsa also already sells into **Chilean, Ecuadorian and
   Uruguayan** armed forces through its Chilean JV partner Servivac `FACT (search)`.

7. **Trade preference is a real line item you have not costed.** US-origin goods
   enter Mexico under USMCA; EU-origin goods under the EU–Mexico agreement.
   Turkey, Malaysia, Singapore, India and South Africa have **no** preferential
   arrangement with Mexico and pay MFN duty. `ASSUMPTION` — must be confirmed
   against the actual HS codes. A 10–20% duty differential can erase Turkey's
   factory-price advantage. **Get the HS classification ruled before you rank on
   landed cost.**

8. **Mexican import compliance is the most likely thing to kill your pilot
   timeline, not price.** Shelf-stable meat products need SENASICA animal-product
   clearance (an HRZ requirements sheet, plus establishment eligibility), a
   COFEPRIS import permit, and a **Certificate of Analysis per lot** with
   physical, chemical and microbiological testing from an accredited lab.
   `FACT (search)`. Plus NOM-051 Spanish labelling. Start this in week 1, in
   parallel with RFQs — not after you pick a supplier.

9. **Never touch US Government Property stock.** DoD requires *"U.S. Government
   Property, Commercial Resale is Unlawful"* printed on MRE cases `FACT (search)`;
   GAO investigated the eBay trade (GAO-06-410R). Commercial production carries no
   such restriction. Selling government-marked rations onward to a foreign
   government customer is an unacceptable risk to this programme. See §10.

**My recommendation in one line:** run Jomipsa (Spain), UNIFO (Turkey) and SOPAKCO
(USA) as the three live tracks, buy the 3,500-unit pilot from whoever can ship
fresh product fastest — probably SOPAKCO — and position UNIFO or Jomipsa for the
100K+ economics.

---

## 1.5 The customer's reference sample — what they actually sent

The customer supplied a photograph of the product they want matched. It is
**not** an APack. Read off the pouch:

| Field on the pouch | Value |
|---|---|
| Product | `MRE — MEAL, READY-TO-EAT, INDIVIDUAL` |
| Menu | `MENU 21 — TUNA, CHUNK, LIGHT, WATER PACKED, LEMON PEPPER` (bilingual EN/FR) |
| Assembler | `AMERIQUAL PACKAGING, EVANSVILLE, IN 47710` |
| Markings | DoD seal; `Warfighter Recommended, Warfighter Tested, Warfighter Approved` |
| **Restriction** | **`U.S. GOVERNMENT PROPERTY — COMMERCIAL RESALE IS UNLAWFUL`** |

### Three conclusions, and they matter more than anything else in this pack

**1. The reference item cannot be legally supplied to you through any commercial
channel.** It is a DoD-owned ration produced under a DLA contract. Its own
packaging says so. Any broker who offers to sell you this exact item in quantity
is offering diverted government property. This is not a technicality to work
around — for a defence-adjacent Mexican government customer it is a
programme-ending risk. See §10.

*(Note: the ZIP on the pouch, 47710, corresponds to AmeriQual's West Morgan Avenue
plant in Evansville — one of the two AmeriQual addresses found independently in
§5. That is corroboration that the pouch is genuine, not that it is buyable.)*

**2. The target spec is now unambiguous: a full U.S. military MRE, not a value
meal.** A current US MRE averages **~1,250 kcal** (13% protein / 36% fat / 51%
carbohydrate) and delivers **1/3 of the Military RDA** of vitamins and minerals,
with entrée + side + crackers + spread + dessert/snack + beverage powders +
accessory pack (spoon, matches, creamer, sugar, salt, gum, tissue) `FACT (search)`.
**That is your Config B.** Config A (900–1,100 kcal) is a cost-down alternative to
quote alongside — it is *not* what they showed you.

**3. Your job is now precisely defined: find the cheapest *legal, commercially
produced* clone of this object.** That is a much more tractable question than
"find an MRE supplier," and it has a clear answer — §1.6.

---

## 1.6 The cheapest legal replacement for the customer's sample

Ranked by how closely each matches the photographed item, against price.

### Tier 1 — near-identical, same components, same industry

**SOPAKCO Sure-Pak 12 (with heaters)** — *the answer for the pilot.*

- **All food components are exactly the same as those in military MREs**
  `FACT (search)`. SOPAKCO is one of the three DLA MRE primes, so Sure-Pak is
  literally the same factory and the same component supply chain as the pouch in
  the photo — just commercially packaged and legal to resell.
- Heaters optional; **when included they are the same military FRH activated with
  plain water** `FACT (search)`.
- Differences vs the photographed item: **900–1,250 kcal vs ~1,300**; **no gum,
  candy, toilet paper or hot sauce** `FACT (search)`.
- Retail today **$65–$85/case of 12 → $5.42–$7.08/meal** `FACT (search)`.
  Wholesale is below that but unpublished; a **published wholesale programme**
  exists with applications to `sphillips@sopakco.com` `FACT (search)`.
- `ESTIMATE` wholesale/factory-direct: **$4.75–$6.25/meal** at 25K+, **$4.25–$5.60**
  at 250K+.
- **Gap to close:** the calorie shortfall and the missing accessory items. Both are
  specifiable — ask SOPAKCO to build to ~1,250 kcal with a full accessory pack.

**AmeriQual commercial production** — same assembler as the photographed pouch,
which is rhetorically powerful with the customer ("same plant, commercial line").
But the APack retail line is dormant (§3) and commercial/export MOQ is `UNKNOWN`.
Ask; expect a high minimum and a high price. `ESTIMATE` **$8.50–$12.00/meal**.

**Baxters North America (Wornick)** — the third prime; same logic, use as the
competitive lever.

### Tier 2 — purpose-built for exactly this use case

**MRE STAR** — the most interesting find for your specific deal. It
**specialises in export sales, and its rations can be customised in your language
and with your country's flag or insignia** `FACT (search)`. That directly answers
the Spanish-packaging and private-label requirement in a way the DLA primes will
not want to. FSSC 22000, USDA/FSIS/FDA, HACCP. **Caveat: the actual factory behind
the brand is unverified — see red flags.** `ESTIMATE` **$5.00–$7.50/meal** at volume.

**XMRE / NEX-XOS** — US-made, explicitly supplies militaries, governments and
international organisations. Same factory-verification caveat.
`ESTIMATE` **$5.50–$8.00/meal**.

### Tier 3 — cheapest at scale, but a functional equivalent rather than a clone

**UNIFO (Turkey)**, **Golden Season (Singapore)**, **Brahim's Dewina (Malaysia)**,
**Jomipsa (Spain)**. These build MRE-style packs to customer specification rather
than cloning the US item. `ESTIMATE` **$4.50–$7.00/meal** for a 1,250 kcal
config at 100K+. Jomipsa additionally gives you native Spanish and EU–Mexico duty
preference.

### The trap to avoid

Search results surface commercial "MRE" offers **from about $0.47 per unit** on
open B2B marketplaces `FACT (search)`. **That is not this product.** At $0.47 you
are being offered a snack pack, a single retort pouch, or nothing at all. Any
quote below roughly **$3.00/meal** for a full MRE-equivalent has had the entrée,
the FRH, or the truth removed. Meanwhile genuine fresh military-spec cases retail
at **$90–$130/case → $7.50–$10.83/meal** `FACT (search)` — which is the honest
market reality for the object in the photograph.

### Bottom line

> **Buy the pilot from SOPAKCO as Sure-Pak 12 with heaters, specified up to
> ~1,250 kcal with a full accessory pack. It is the same components and the same
> prime as the pouch the customer photographed, it is legal to resell and export,
> and it is the fastest route to a qualification sample. In parallel, run MRE STAR
> for Spanish-language private label and UNIFO or Jomipsa for the 100K+ price.**

---

## 2. The Mexican spec — read this before writing any RFQ

> **Reconciliation note.** The customer's own reference sample (§1.5) is a
> **U.S. military MRE — a single-entrée pouch**. The SEDENA incumbent described
> below is a **two-retort-pouch** meal. These do not match. The customer showed you
> the US MRE, so **the US MRE architecture is the spec you quote**. Treat the
> two-entrée point below as a **question to put to the customer**, not a hard
> requirement — but be aware of it, because if the incumbent really is a two-pouch
> meal, a US-MRE clone may read as a downgrade on entrée volume even at equal
> calories. Ask before you quote. `ASSUMPTION` either way.

`FACT (search)`, retrieved 1 Sep 2026:

> SEDENA issues the *"Ración Diaria Individual de Combate"*: an olive-green and
> black plastic box containing **three individual meal packs**, **3,640–4,030
> kcal** total per day. Each individual meal package contains **two main retort
> pouches** meant to be eaten together — the first a meat product (beef, pork,
> sausage, fish, ham, seafood, chicken, tuna, bacon, usually with a sauce and
> vegetables), the second a staple (rice, hominy, noodles, beans, pasta, eggs or
> vegetables).

Implications you should act on:

| Implication | Action |
|---|---|
| Per-meal target is **~1,215–1,345 kcal**, not 900–1,100 | Make Config B the primary quote; Config A is the cost-down alternative |
| **Two retort entrées per meal**, not one | Explicitly specify this in the RFQ — most Western MREs have one entrée + a side. This is a real cost driver and suppliers will under-quote if you don't say it |
| Menu profile is Mexican/Latin | Ask for tortillas over crackers, and for salsa/chile condiments. Jomipsa, Spanish producers and US Hispanic-market co-packers have an edge |
| The incumbent is a **box**, not a pouch | Confirm whether the customer wants your outer packaging to match the incumbent box format or a flexible pouch |
| A daily unit = 3 meals | 3,500 meals ≈ **1,167 soldier-days**. 1,000,000 meals ≈ 333,333 soldier-days. Sanity-check the customer's stated force size against this — it is the fastest way to detect a fantasy follow-on |

`UNKNOWN`: who currently manufactures SEDENA's ration, and at what unit price.
Mexican federal procurement is published on **CompraNet**; I could not reach it.
This is the single highest-value open item in the whole audit — if you can pull
the incumbent award price off CompraNet you will know the ceiling before you quote.

---

## 3. The AmeriQual APack $50/12 investigation

**Verdict: the $50/12 (~$4.17/meal) number is real as a retail listing, but it is
liquidation pricing on a discontinued consumer line. It has no bearing on factory
economics and cannot be repeated at any volume.**

### The evidence

| Finding | Detail | Confidence |
|---|---|---|
| Advertised price is real | $49.00 (Ozark Outdoorz) to $51.50 (Ammo Can Man) per case of 12 | `FACT (search)` |
| The retail line is dormant | *"Ameriqual APacks are no longer widely available as a direct-to-consumer brand in 2025… the classic 'APack' retail line is effectively dormant"*; availability *"spotty at best, mostly old stock"*; status *"Legacy / Hard to Find"* | `FACT (search)` |
| Listings are keyed to **inspection dates**, not pack dates | Retail SKUs are literally titled by inspection date — 2023, 2024, and one at 10/2029 | `FACT (search)` |
| Inspection date ≠ expiry | An inspection date is a re-inspection checkpoint, *"typically three to five years after the meal was packed"* | `FACT (search)` |
| Therefore the cheap stock is old | A case sold in 2026 with a **2023 or 2024** inspection date was packed roughly **2018–2021** | `ESTIMATE`, applying the 3–5 year rule |
| Fresh product costs much more | The comparable current commercial product, SOPAKCO Sure-Pak 12, retails **$65–$85/case → $5.42–$7.08/meal** | `FACT (search)` |
| Genuine current-inspection military cases cost more still | Retail commentary notes prices *"significantly higher than the 'classic' $60 price point for any case with a valid future inspection date"* | `FACT (search)` |

**The tell:** an $49–51 case with a 2023/2024 inspection date sits next to a
$65–85 case of fresh commercial product. That gap *is* the age discount. You are
looking at inventory being cleared before it becomes unsellable.

### Answers to your ten questions

1. **Is ~$50/12 current, repeatable retail pricing?** It is currently *listed*, but
   it is not repeatable — it is clearance on a legacy line, and it is retail, not
   wholesale. `FACT (search)` + `ESTIMATE`.
2. **Fresh production or older inventory?** Older inventory. The line is dormant
   and SKUs are sorted by inspection date. `ESTIMATE` (high confidence).
3. **Production / inspection dates and remaining shelf life?** Listings show
   inspection dates of 2023, 2024 and 10/2029. Implied pack dates ~2018–2021 for
   the cheap stock. Actual production dates: `UNKNOWN` — only a case-code read
   will tell you, and you must demand it in writing.
4. **Can current-production APacks be bought direct from AmeriQual?** `UNKNOWN`.
   AmeriQual unambiguously still manufactures (largest MRE provider to the US
   military, and it holds a **$221,062,100** UGR-A award announced 8 Aug 2025
   `FACT (search)`). Whether it will sell *APack-branded commercial* product
   direct, and in what form, must be asked. Note it operates several web
   properties — ameriqual.com, ameriqualgroup.com, ameriqualpackaging.com — and a
   consumer site readymeal.com that reportedly now offers only a notify-me form.
5. **AmeriQual's MOQ?** `UNKNOWN`. Not published. Given it is a DLA prime running
   retort lines, expect a full-production-run minimum well above 3,500.
   `ASSUMPTION`.
6. **Distributors with true wholesale pricing?** `UNKNOWN` for AmeriQual. **For
   SOPAKCO, yes** — a published wholesale programme with a stated minimum,
   applications to `sphillips@sopakco.com` `FACT (search)`. That is the single most
   actionable wholesale channel found in this audit.
7. **Can fresh APacks be exported to Mexico?** No legal barrier identified for
   *commercial* production. Practical barriers are Mexican-side: SENASICA
   animal-product clearance, COFEPRIS permit, per-lot COA, NOM-051 labelling
   `FACT (search)`. Government-marked MREs are a different matter — see §10.
8. **Meaningful difference between APack and military MRE?** Small but real.
   APack is **1,140–1,310 kcal** vs a military MRE at **~1,200 kcal**; APack has
   **half the dairy shake**, **no coffee, no matches, no tissue**, and substitutes
   lemonade for coffee. `FACT (search)`. Functionally equivalent; not identical.
   Note that APack at 1,140–1,310 kcal is **already your Spec B**, not your Spec A —
   there is no "value APack."
9. **Realistic factory/direct wholesale price at each tier?** See §6. Short
   version for fresh US commercial MRE-equivalent: `ESTIMATE` $8.50–$12.00/meal at
   your volumes. Not $4.17.
10. **Legal restriction on "U.S. Government Property" MREs?** Yes, and it does not
    apply to commercial production. See §10.

---

## 4. Government and institutional price evidence

Everything here is normalised to **USD per individual meal**. The unit-of-issue
trap you flagged is real and I have kept case/ration/day units explicit.

| Programme | Unit of issue | Price | Per individual meal | Year | Confidence |
|---|---|---|---|---|---|
| **US MRE — DLA standard price** | case of 12 meals | $150.32 | **$12.53** | FY24/FY25 | `FACT (search)` — DLA price list. This is DLA's *sales* price to the services, not contractor cost |
| **US MRE — contract, historical** | reported "per unit" $64.14 | $64.14 | **$5.35** if per case of 12 | 2006 | `FACT (search)` for the figure; `ASSUMPTION` that the unit is a case |
| **Humanitarian Daily Ration** | case of **10** individual bags | $42.00–$43.00 | **$4.20–$4.30** | c. 2011 solicitation | `FACT (search)` — ceiling prices, DLA solicitation |
| **Humanitarian Daily Ration** | box of 10 | $39.50 | **$3.95** | 2006 | `FACT (search)` |
| **HDR, reported** | per ration | ~$4.70 | **$4.70** | 2012 | `FACT (search)` |
| **US MRE/HDR IDIQ awards** | 5-year IDIQ ceilings | SOPAKCO $101,574,000 / AmeriQual $100,507,000 / Wornick $75,630,500 | not derivable | Nov 2021 | `FACT (search)`. **Do not divide these by a meal count** — ceilings, not quantities |
| **UGR-A modules** | 5-year IDIQ | AmeriQual $221,062,100 / Wornick $25,308,625 | n/a — group ration, not individual | Aug 2025 | `FACT (search)` |
| **Spanish Army field rations** | framework, 2 years, mixed lots | €4,134,092 incl. tax (vs €8,268,300 base budget) | not derivable | c. 2019 | `FACT (search)`. Mixed basket: individual combat rations modules A/B, breakfast module, bread-biscuit module, 10-person collective rations, emergency rations, supplements, AVE drinks. **Cannot be reduced to a per-meal price** |
| **Spanish MoD framework** | framework ceiling | €21.8M | not derivable | recent | `FACT (search)` |
| **Spanish Army tender** | tender value, 2 fiscal years | €9.9M | not derivable | Oct 2023 | `FACT (search)` |

### What this evidence actually supports

- **A complete, individual, shelf-stable ration bag can be produced for ~$4.20–$4.30
  at massive government scale** — *if* it is vegetarian, has no FRH, and is packed
  in a single bag. That is the HDR. Inflated to 2026 at ~3%/yr that is roughly
  **$5.80–$6.10**. `ESTIMATE`.
- **A US MRE is a fundamentally more expensive object** — meat entrées, an FRH, a
  multi-component accessory pack, a rugged outer pouch, and MIL-SPEC QA. The
  $12.53 DLA number and the $5.42–$7.08 fresh commercial retail number bracket it.
- **The Spanish contracts cannot give you a unit price** and anyone who tells you
  they can is dividing a mixed-basket framework by a made-up meal count. I am not
  going to do that. The per-unit prices live in the *pliegos de prescripciones
  técnicas*, which I could not retrieve.

### Sources I could not reach and you should

`UNKNOWN` on all of these — each is a genuine, high-value lead:

- **CompraNet (Mexico)** — the incumbent SEDENA ration award. Highest value.
- **TED / EU procurement** — Spanish and Polish MoD award notices with unit prices.
- **SAM.gov / FPDS / USAspending** — actual DLA MRE contractor unit prices, not
  the DLA standard price.
- **DLA price list PDFs** (`dla.mil/Portals/104/…/pricesFY24.pdf`) — the primary for the $150.32.
- **Turkish SSB / Polish MoD / SANDF** tender portals.

---

## 5. Longlist — 26 manufacturers and channels

Legend: **OEM** = manufactures food; **ASM** = assembles ration packs;
**DIST** = distributor/reseller.

### United States

| # | Legal name | Location | Type | Notes | Confidence |
|---|---|---|---|---|---|
| 1 | **AmeriQual Group, LLC** / AmeriQual Packaging | 18200 Highway 41 N, Evansville, IN 47725; also 225 W Morgan Ave, Evansville, IN 47710 | OEM+ASM | Founded 1987. *"Largest provider of MREs to the U.S. Military."* Retort + aseptic, flexible pouches, trays, multi-component kits, private label. UGR-A award $221.06M Aug 2025 | `FACT (search)` |
| 2 | **SOPAKCO, Inc.** (So-Pak-Co) | 118 S Cypress St, Mullins, SC 29574 | OEM+ASM | Feeding military since 1943. MRE prime. **Sure-Pak 12 commercial line with a published wholesale programme** | `FACT (search)` |
| 3 | **Baxters North America, Inc. dba The Wornick Co.** | Cincinnati, OH | OEM+ASM | Predecessor from 1971; first contractor to deliver MREs to DoD in 1981. Acquired by Baxters 2014. McAllen TX plant closed (consolidated to Cincinnati) | `FACT (search)` |
| 4 | **XMRE** (brand) — *"manufactured and assembled by NEX-XOS"* | Pembroke Park, FL | ASM (factory `UNKNOWN`) | Supplies militaries, international organisations, governments. US-made, USDA/FSIS + FDA | `FACT (search)` for the claim; NEX-XOS's actual factory `UNKNOWN` — **see red flags** |
| 5 | **MRE STAR, L.L.C.** | USA | ASM (factory `UNKNOWN`) | FSSC 22000, USDA/FSIS/FDA, HACCP. Standard + Halal. Has a stated wholesale programme. Reported manufacturer *"International Meals Supply"* | `FACT (search)` for claims; factory identity **unverified** |
| 6 | **Luxfer Magtech** | USA | OEM (component) | **Sole supplier of the FRH to the US military**; TRUETECH FRH since 1990; *"over two billion FRHs"* supplied, including to international militaries and humanitarian organisations | `FACT (search)` |

### Europe

| # | Legal name | Location | Type | Notes | Confidence |
|---|---|---|---|---|---|
| 7 | **Jomipsa** | Mutxamel (Muchamiel), Alicante, Spain | OEM+ASM | 35–40 yrs in combat rations. **Makes the UAE Type C: bagged MRE-style 3-meal 24-hr pack, 3,400 kcal.** Spanish Army prime via UTE Raciones. ISO 9001 / 14001 / 22000. Halal range. LatAm JV with Servivac (Chile) | `FACT (search)` |
| 8 | **Alonso Hipercas** | Alcorcón, Spain | OEM/ASM | Co-member of UTE Raciones (Spanish Army field rations) | `FACT (search)` |
| 9 | **Teógenes Ruiz (TR)** | Tarancón, Spain | OEM/ASM | Co-member of UTE Raciones | `FACT (search)` |
| 10 | **ARPOL** | Zielona Góra, Poland | OEM+ASM | Food rations + special military canned food for Polish Armed Forces. **NATO AQAP 2110:2016**, ISO 9001:2015, ISO 22000, **NCAGE 1126H since 2006**. Makes a self-heating "Hot can". Deployed Haiti, Moscow, Montenegro | `FACT (search)` |
| 11 | **LYOFOOD** | Kielce, Poland | OEM (component) | Freeze-dried meal items for military ration packs | `FACT (search)` |
| 12 | **Rationtech Europe / Rationtech Global** | Netherlands | ASM (+claimed OEM) | *"350 customers in 36 countries"*; 800+ products since 2006; **48-month shelf life** capability; sterilised bread/pastries/desserts | `FACT (search)` — **manufacturing model needs verification, see red flags** |
| 13 | **Vestey Foods UK** (part of Purple Foodservice Solutions Ltd) | UK | ASM+procurement | UK MoD Special Contracts Division. Only officially licensed vendor of the British Army ration-pack brand. Supplies Norway, Sweden, Denmark, Malta, Ireland. *"Only ambient feeding suppliers in the current NAMSA catalogue"* | `FACT (search)` |
| 14 | **Podravka** | Croatia | OEM | Makes the Croatian *Individualni Borbeni Obrok Tip 3*, produced to **NATO STANAG 2937** | `FACT (search)` |

### Turkey

| # | Legal name | Location | Type | Notes | Confidence |
|---|---|---|---|---|---|
| 15 | **UNIFO Gıda ve Savunma Sanayi Ticaret A.Ş.** | Gebze Organize Sanayi Bölgesi, 400. Sokak No:412, Gebze 41480, Kocaeli, Turkey (+ Yerköy branch) | OEM+ASM | Founded 1997, UYAR Group. Combat ration packs for military, police, NGOs, peacekeeping, humanitarian aid; MREs; sterilised/pasteurised shelf-stable meals. 10,870.68 m² plant, **320 employees (2025)**. Consumer brand *ta!da!*. Claims **"the world's largest filling plant for packaging ration products"** | `FACT (search)`; the capacity claim is the **company's own** and is `UNKNOWN` independently |

### Asia

| # | Legal name | Location | Type | Notes | Confidence |
|---|---|---|---|---|---|
| 16 | **Golden Season Pte Ltd** (UEN 198403734E) | 31 Playfair Road #02-01, Singapore | OEM+ASM | Est. 1982. Combat ration packs, halal ready meals, durable energy products, military rescue equipment, inflatable boats. **HALAL, HACCP, ISO 9001, ISO 22000.** States it manufactures MRE packs **to specification** with a wide menu range | `FACT (search)` |
| 17 | **Dewina Food Industries Sdn Bhd** (Brahim's Dewina Group) | Malaysia | OEM+ASM | Military rations *"for at least the past three decades"*; supplier to regional armies and **UN Peacekeeping Forces**; *"first Halal retort processing facility in the world"*; JAKIM halal + Veterinary Health Mark. Two-year shelf life stated on halal foods | `FACT (search)` — note the **2-year** shelf-life claim vs your 24–36 month floor |
| 18 | **Unique Presence Sdn Bhd (UPSB)** | Malaysia | ASM/OEM `UNKNOWN` | Combat ration packs, halal ready meals, military rescue equipment; MRE page for humanitarian relief | `FACT (search)` |
| 19 | **D'Era Pouch Industries Sdn. Bhd.** | Malaysia | OEM | Makes MRE products for the Malaysian Armed Forces | `FACT (search)` |
| 20 | **D'Heritage** | Malaysia | `UNKNOWN` | Positions as an MRE industry leader | `FACT (search)`, thin |
| 21 | **Charoen Pokphand Foods (CPF)** | Thailand | OEM | *"The current version of Thai Army rations is made by CPF"* — Thailand's largest food company, major retort/export capability | `FACT (search)` |

### Africa & Latin America

| # | Legal name | Location | Type | Notes | Confidence |
|---|---|---|---|---|---|
| 22 | **Africor Holdings** | South Africa | ASM (+uniforms/apparel) | Ration packs and MREs; states factory holds **ISO 22000, ISO 9001, HALAL**; positions as SA's leading ration pack supplier; 12-hr and 24-hr packs | `FACT (search)` — **also a uniform/apparel manufacturer; verify the food factory is theirs** |
| 23 | **MRE International** (a division of Snippets) | South Africa | DIST/ASM `UNKNOWN` | Relief and ration packs, local + international; SA 24-hour ration packs | `FACT (search)` |
| 24 | **Outdoor Cuisine** (supplies military via Serac) | South Africa | OEM | *"Leading manufacturer of ready to eat meals"* | `FACT (search)` |
| 25 | **Servivac** | Santiago, Chile (+ subsidiaries) | DIST | Est. 2001. Jomipsa's LatAm JV partner. Clients include **Chilean, Ecuadorian and Uruguayan armed forces**; serves Brazil and Paraguay | `FACT (search)` — **channel-conflict risk, see §9** |
| 26 | **India — DFRL Mysore licensee network** | India | OEM | Defence Food Research Laboratory (Mysore) provides the retort MRE technology; trilaminate retort pouches sealed in a heavy-duty outer bag; menus incl. chicken biryani, dal makhani, rajma, veg pulao | `FACT (search)` — **no specific exporting company identified.** See red flags |

### Names that did NOT check out

- **"Musli Klex" (Poland)** — `UNKNOWN`. Searched directly; no Polish military
  ration manufacturer by that name surfaced. The name may be garbled, may be a
  brand rather than a company, or may not exist. **Do not put it on an RFQ list
  until someone produces a company registration number.** The verified Polish
  names are **ARPOL** and **LYOFOOD**.
- **Czech Republic** — `UNKNOWN`. No Czech combat-ration manufacturer identified.
- **Germany / Italy** — no manufacturer names established. Notable finding: the
  **plastic-bag version of the German EPa has been outsourced to Spain**
  `FACT (search)`, which reinforces Spain as the European ration-production centre.
  Italian rations use **cans, not retort pouches** `FACT (search)` — wrong
  technology for your spec.
- **South Korea / Taiwan / Vietnam / UAE** — no manufacturer names established.
  The **UAE Type C ration is supplied by Jomipsa (Spain)** `FACT (search)`, so the
  UAE is a customer, not a source.
- **China** — PLA individual MRE packs exist and are traded, but no exporting OEM
  was identified, and Chinese-origin rations carry political and audit risk for a
  Mexican defence-adjacent customer. Deprioritised on those grounds, not on capability.

---

## 6. Pricing model — and a straight answer on whether your targets are real

### 6.1 Bottom-up build cost, per individual meal

This is a **cost model**, not a quotation. Ranges span low-cost-country (Turkey,
Malaysia, Poland, South Africa, India) at the low end to US production at the high
end. All figures `ESTIMATE`.

| Component | Low | High | Note |
|---|---|---|---|
| Main retort entrée, 250–300 g, with meat | $0.90 | $1.60 | Protein cost dominates and is volatile |
| Second retort pouch (starch/staple) — **required by the Mexican spec** | $0.35 | $0.70 | Most Western MREs omit this; it is why "MRE-equivalent" quotes will come in low |
| Bread / crackers / tortilla, shelf-stable | $0.25 | $0.55 | |
| Spread sachet (peanut butter, cheese, jam) | $0.10 | $0.20 | |
| Snack / energy component | $0.25 | $0.50 | |
| Dessert / fruit / sweet | $0.20 | $0.45 | |
| Beverage powders, electrolyte, coffee, sugar, creamer | $0.15 | $0.35 | |
| Accessory pack (spoon, napkin, wipe, salt, pepper) | $0.12 | $0.25 | |
| Outer pouch + inner films + print | $0.20 | $0.45 | Rugged waterproof outer costs more than a simple bag |
| Assembly labour, QA, retort energy, overhead | $0.35 | $0.80 | The main US-vs-LCC divergence |
| **Subtotal, no FRH** | **$2.87** | **$5.85** | |
| Flameless ration heater | $0.55 | $1.20 | Luxfer-branded at the top; Asian FRH at the bottom |
| **Subtotal with FRH** | **$3.42** | **$7.05** | |
| Manufacturer margin @ 10–20% | | | |
| **EXW price, Config A (900–1,100 kcal, single entrée)** | **~$3.20** | **~$6.00** | Drop the second retort pouch and trim components |
| **EXW price, Config B (1,215–1,345 kcal, two entrées + FRH)** | **~$4.60** | **~$8.40** | LCC low end → US-adjacent high end |
| **EXW price, Config B from a US prime** | **~$8.50** | **~$12.00** | US labour, US protein, MIL-SPEC QA overhead |

**Cross-check against the HDR anchor.** The HDR — a complete 2,200 kcal individual
ration bag — was bought by DLA at **$4.20–$4.30** at enormous scale c. 2011,
inflating to roughly **$5.80–$6.10** in 2026 `ESTIMATE`. But the HDR is
**vegetarian, has no FRH, no meat retort, and minimal accessories**. That it lands
just below my Config B low end is exactly what you would expect, and it makes the
model credible rather than undermining it.

**Cross-check against retail.** Fresh Sure-Pak 12 retails at **$5.42–$7.08/meal**
`FACT (search)`. Retail carries distributor and retailer margin on top of factory
cost. A US factory price meaningfully below ~$4.50 is therefore not consistent
with observed retail. This is the cleanest disproof of the $4.17 factory theory.

### 6.2 Indicative price by volume tier

All `ESTIMATE`. **Ranges, not quotations.** Use these to judge whether an incoming
quote is serious, never to tell a supplier what you will pay.

**Config A — value, ~900–1,100 kcal, single entrée**

| Tier | LCC EXW, no FRH | LCC EXW, with FRH | US EXW, with FRH |
|---|---|---|---|
| 3,500 | $4.60–$6.20 | $5.30–$7.00 | $8.00–$11.00 |
| 25,000 | $4.00–$5.30 | $4.70–$6.10 | $7.00–$9.50 |
| 100,000 | $3.55–$4.70 | $4.20–$5.40 | $6.30–$8.50 |
| 250,000 | $3.35–$4.40 | $3.95–$5.05 | $5.90–$7.90 |
| 500,000 | $3.20–$4.20 | $3.80–$4.85 | $5.60–$7.50 |
| 1,000,000 | $3.05–$4.00 | $3.65–$4.65 | $5.40–$7.20 |

**Config B — premium, ~1,215–1,345 kcal, two retort entrées + FRH**

| Tier | LCC EXW | Spain/Poland EXW | US EXW |
|---|---|---|---|
| 3,500 | $6.80–$9.20 | $7.80–$10.50 | $11.00–$15.00 |
| 25,000 | $5.90–$7.90 | $6.80–$9.00 | $9.80–$13.00 |
| 100,000 | $5.20–$7.00 | $6.00–$8.00 | $8.80–$11.50 |
| 250,000 | $4.90–$6.55 | $5.60–$7.45 | $8.30–$10.80 |
| 500,000 | $4.70–$6.25 | $5.35–$7.10 | $8.00–$10.30 |
| 1,000,000 | $4.50–$6.00 | $5.15–$6.80 | $7.70–$9.90 |

### 6.3 Freight and landed cost

Container maths `ESTIMATE`, built on one search-derived datapoint (**48 cases per
pallet** for APack) and standard equipment dimensions:

- 48 cases/pallet × ~21 pallets in a 40 ft HC (single-stacked; the stack is too
  tall to double) ≈ **1,000 cases ≈ 12,000 meals per 40 ft container**, ~10 t.
- 53 ft trailer ≈ 26 pallets ≈ 1,250 cases ≈ **15,000 meals**.

| Lane | Cost | Per meal | Transit | Confidence |
|---|---|---|---|---|
| Spain (Valencia/Barcelona) → Veracruz/Altamira, 40 ft | $3,500–$3,800 | **$0.29–$0.32** | 21–31 days | `FACT (search)` for the rate; `ESTIMATE` for per-meal |
| Turkey/Asia → Manzanillo/Veracruz, 40 ft | `UNKNOWN`, assume $3,000–$5,500 | **$0.25–$0.46** | 30–45 days | `ASSUMPTION` |
| US → Mexico, cross-border FTL 53 ft | $1,800–$2,800 | **$0.12–$0.19** | 3–7 days | `FACT (search)` for the rate |
| US → Mexico, LTL for the 3,500 pilot (~6 pallets) | `UNKNOWN`, assume $1,200–$2,500 | **$0.34–$0.71** | 5–10 days | `ASSUMPTION` |

**Freight is not the deciding variable — it is $0.12–$0.46/meal on a $4–$12 product.**
The deciding variables are factory price, duty treatment, and whether the product
passes qualification. Do not let a supplier win on freight.

**Duty is the variable people miss.** US-origin under USMCA and EU-origin under the
EU–Mexico agreement should enter at preferential rates; Turkey, Malaysia, Singapore,
India and South Africa should not. `ASSUMPTION` — **get a Mexican customs broker to
rule the HS classification** (likely heading 1602 for prepared meat, 2004/2005 for
prepared vegetables, 1905 for bakery — a multi-component kit may classify by
essential character or as a set). If MFN duty is 15–20%, Turkey's $1.50/meal factory
advantage over the US shrinks to well under $1.00 landed.

### 6.4 Verdict on your stated targets

| Your target | Verdict | Why |
|---|---|---|
| **Value MRE $2.50–$4.50 factory** | **Partly realistic — top half only** | $3.20–$4.50 EXW is attainable from Turkey/Malaysia/South Africa at 250K+, realistically **without an FRH**. **$2.50 is below build cost** for anything with a meat retort entrée; any supplier quoting it is either omitting the entrée, omitting the FRH, quoting a snack pack, or is not going to deliver |
| **Premium MRE $4.00–$7.00 factory** | **Realistic from LCC at scale. Not realistic from the USA.** | LCC Config B lands $4.50–$7.00 EXW at 250K+. A US prime will be $8–$12. If you need US origin, reset the budget or accept Config A |
| **Implied $4.17 from the APack listing** | **Not a valid target at all** | Clearance retail on a dormant line. See §3 |

**The defensible ranges to plan against** `ESTIMATE`:

- **Pilot 3,500:** $6.50–$11.00/meal landed Mexico (premium), $5.00–$8.00 (value).
  Pilots are expensive. Do not let the pilot price anchor the programme.
- **100,000:** $5.20–$8.00/meal landed (premium), $4.00–$5.75 (value).
- **500,000–1,000,000:** $4.75–$7.00/meal landed (premium), $3.50–$5.00 (value).

---

## 7. Top 10 ranking

**Scoring is my judgement**, built on search-derived evidence and constrained by the
verification ceiling. Weights reflect your stated priorities (price first, then
reliability, product match, scale, speed):

`PRICE 28% · QUALITY 18% · PRODUCT MATCH 14% · SCALABILITY 14% · LOGISTICS TO MEXICO 10% · MILITARY CREDENTIALS 6% · CUSTOMISATION 5% · CONFIDENCE 5%`

| # | Supplier | Price | Product match | Quality | Mil. creds | Scale | Custom | Logistics MX | Confidence | **Overall** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AmeriQual** (US) | 3 | 10 | 10 | 10 | 9 | 7 | 10 | 7 | **7.60** |
| 2 | **UNIFO** (TR) | 9 | 8 | 7 | 7 | 8 | 7 | 5 | 6 | **7.59** |
| 3 | **SOPAKCO** (US) | 4 | 10 | 9 | 10 | 8 | 6 | 10 | 8 | **7.56** |
| 4 | **Baxters/Wornick** (US) | 4 | 10 | 9 | 10 | 8 | 6 | 10 | 6 | **7.46** |
| 5 | **Jomipsa** (ES) | 6 | 9 | 8 | 9 | 6 | 10 | 7 | 8 | **7.36** |
| 6 | **Golden Season** (SG) | 8 | 7 | 7 | 6 | 7 | 8 | 5 | 6 | **7.02** |
| 7 | **XMRE / NEX-XOS** (US) | 6 | 9 | 7 | 6 | 6 | 7 | 10 | 5 | **7.00** |
| 8 | **Brahim's Dewina** (MY) | 8 | 6 | 7 | 7 | 7 | 7 | 5 | 6 | **6.89** |
| 9 | **MRE STAR** (US) | 6 | 8 | 7 | 5 | 6 | 7 | 10 | 5 | **6.80** |
| 10 | **ARPOL** (PL) | 7 | 6 | 8 | 9 | 6 | 6 | 5 | 7 | **6.77** |
| — | *Rationtech (NL)* | 7 | 8 | 7 | 6 | 6 | 7 | 5 | 5 | *6.64* |
| — | *Africor (ZA)* | 8 | 7 | 6 | 6 | 5 | 6 | 4 | 5 | *6.31* |

### The awards

- **BEST OVERALL — Jomipsa (Spain).** *This is a deliberate override of the composite
  table and I want to be explicit about it.* AmeriQual wins the arithmetic, but the
  score cannot express "the price is 2–3x the budget," which is fatal given price is
  your #1 criterion. Jomipsa is the only supplier that already builds **the exact
  architecture the Mexican customer uses** — a bagged, MRE-style, three-meal 24-hour
  pack (UAE Type C, 3,400 kcal) — in **Spanish**, with an existing **Latin American
  military channel**, at a mid price, under EU–Mexico trade preference.
- **CHEAPEST CREDIBLE — UNIFO (Turkey).** Genuine dedicated ration-filling capacity
  and a real defence identity (*Gıda ve **Savunma*** — food *and defence*), at Turkish
  cost. Its "world's largest ration filling plant" claim is unverified; test it.
- **BEST U.S. OPTION — SOPAKCO.** Not AmeriQual. SOPAKCO is the only US prime with a
  **published, working commercial wholesale channel** and a current individual-meal
  retail product (Sure-Pak 12). AmeriQual's commercial line is dormant.
- **BEST EUROPEAN OPTION — Jomipsa**, with **ARPOL** as the NATO-credentialled backup.
- **BEST ASIAN OPTION — Golden Season (Singapore).** Singapore HQ means cleaner
  contracting and English documentation; states it builds MRE packs to specification.
  **Brahim's Dewina** is the alternate, with the caveat that its stated 2-year shelf
  life is below your 24–36 month floor.
- **BEST FOR THE 3,500 PILOT — SOPAKCO.** 3,500 meals ≈ **292 cases ≈ 6 pallets**.
  That is an LTL truck from South Carolina, days not months, with USMCA treatment,
  from an existing wholesale programme. Fastest credible route to qualification samples
  at scale. **XMRE/NEX-XOS** is the fallback if SOPAKCO's MOQ blocks you.
- **BEST FOR 500K–1MM+ — UNIFO** on price, **AmeriQual** as the risk-managed hedge.
  Which one wins depends entirely on whether the customer's budget is ~$5 or ~$9.
- **BEST BACKUP SUPPLIER — Baxters North America (Wornick).** A second US prime with
  materially the same capability as AmeriQual. Its value is as a **competitive lever**
  and a genuine second source; never run this programme single-sourced.

---

## 8. Recommended sourcing strategy

**Run three tracks in parallel. Do not sequence them.**

| Track | Suppliers | Purpose |
|---|---|---|
| **A — Speed** | SOPAKCO, XMRE/NEX-XOS, MRE STAR | Win the 3,500-unit pilot on lead time. US origin, truck freight, USMCA |
| **B — Product match** | Jomipsa, ARPOL, Rationtech | Nail the Mexican 3-meal/two-entrée architecture and Spanish packaging |
| **C — Price at scale** | UNIFO, Golden Season, Brahim's Dewina, Africor | Establish the true floor for the 100K–1MM tiers |

**Sequence, weeks 1–8:**

1. **Week 1** — Send Email #1 to the US list and Email #2 to the international list
   the same morning. Simultaneously brief a Mexican customs broker to rule the HS
   codes and confirm SENASICA/COFEPRIS pathway. **Do this in week 1** — it has the
   longest lead time and it is not supplier-dependent.
2. **Week 1** — Ask the customer, in writing, for the incumbent ration's technical
   sheet. If they will share it, your spec becomes exact and your quotes become
   comparable. Meanwhile try to pull the incumbent award off CompraNet.
3. **Weeks 2–3** — Triage quotes. Anything that cannot state a **manufacturing date
   policy** and a **factory address** drops out immediately.
4. **Weeks 3–4** — Samples from the top 5 (2–5 menus each). Run the scorecard in
   `05-sample-evaluation-scorecard.md`.
5. **Week 4** — Email #3 (negotiation) to the survivors, with the 100K–1MM tiers as
   the explicit lever.
6. **Weeks 5–6** — Place the 3,500 pilot. Dual-source it if the budget allows:
   ~1,750 from the US track and ~1,750 from the best international quote. **Two
   pilot lots for barely more money is the best diligence spend in this programme** —
   it tests two supply chains, two customs pathways and two products at once.
7. **Weeks 6–8** — Customer qualification. Lock the 100K+ supplier against a real
   qualification result, not a sample.

**Commercial protections to build in now:**

- **Manufacturing date policy in writing**: no product with a pack date older than
  90 days at shipment; minimum 90% of stated shelf life remaining on arrival.
- **Price validity + escalation formula.** Protein is volatile. Get a stated basis
  and an indexation mechanism rather than a price that silently expires.
- **Capacity option, not an obligation.** Buy the right to 1MM units at a fixed
  formula; do not commit volume you do not have a contract for.
- **Never disclose the end customer.** Every supplier in Track B and C has a
  motive to reach a Mexican defence buyer directly — Jomipsa in particular already
  has a Latin American channel through Servivac (see §9 channel conflict).
- **Payment terms.** Resist 100% advance. Target 30% deposit / 70% against
  documents, or an LC at sight for the large tiers.

### Channel-conflict warning — Jomipsa / Servivac

Jomipsa's Latin American route to market is a **joint venture with Servivac
(Santiago, Chile)**, whose existing customers include the Chilean, Ecuadorian and
Uruguayan armed forces `FACT (search)`. If you approach Jomipsa cold, you may be
routed to Servivac as the regional channel — which inserts a margin layer and puts
a LatAm defence distributor next to your customer. **Approach Jomipsa's export/
defence sales directly, state that you require a direct factory relationship for
the Mexican market, and settle territory before you share any customer detail.**

---

## 9. Red flags — general checklist and the specific ones already raised

### Disqualify or escalate immediately if a supplier:

1. Cannot name the **legal entity and physical address** of the factory that
   performs the retort processing.
2. Is a **distributor presenting as a manufacturer** — test: ask who owns the
   retort autoclaves and ask for the establishment/approval number.
3. Offers **military surplus** or stock with a near or past inspection date.
4. Offers anything marked **"U.S. Government Property, Commercial Resale is
   Unlawful."** Walk away — see §10.
5. Cannot produce **certificates** (HACCP, ISO 22000 / FSSC 22000 / BRCGS / IFS)
   with certificate numbers and expiry dates.
6. Quotes **suspiciously low** — below ~$3.00/meal for anything with a meat retort
   entrée. Ask what has been removed. Usually it is the entrée, the FRH, or the truth.
7. **Confuses a 24-hour ration with an individual meal.** This is the single most
   common quoting error in this category and it produces a fake 3x price advantage.
   Force every quote onto the line *"price per ONE individually sealed meal packet."*
8. Cannot show **monthly capacity** in units, or gives capacity in "tons."
9. Cannot supply **recent production** — insists on shipping existing stock.
10. Demands **unreasonable advance payment** (100% T/T up front).
11. Names **military customers that cannot be substantiated** — ask for a contract
    number, a tender reference, or a contactable referee.
12. Cannot commit to a **manufacturing date policy** in writing.

### Specific flags raised by this audit

| Supplier / item | Flag | Action |
|---|---|---|
| **"Musli Klex" (Poland)** | Could not be verified to exist as a ration manufacturer | Do not RFQ until someone produces a registration number. Use ARPOL |
| **XMRE** | Brand; *"manufactured and assembled by NEX-XOS"* — NEX-XOS's factory is `UNKNOWN` | Ask directly: who owns the plant, where is it, what is the FSIS establishment number |
| **MRE STAR** | Manufacturer reported as *"International Meals Supply"*, unconfirmed. Multiple third-party "factory authorised agents" in the channel | Establish the factory before quoting; you may be talking to a reseller |
| **Rationtech (NL)** | *"manufacture… in-house wherever they are required in Europe"* reads like a distributed assembly/procurement network, not one factory | Ask which specific plant would make your order and get its certificates |
| **Africor (ZA)** | Primarily a uniform/apparel manufacturer that also sells rations; its site metadata references "rationtech" | Confirm whether the food factory is owned or contracted |
| **Brahim's Dewina** | States a **2-year** shelf life on its halal foods — below your 24–36 month floor | Confirm shelf life on the specific MRE product before evaluating |
| **India** | Technology (DFRL Mysore) is real; **no specific exporting company identified** | Treat India as an unexplored option, not a shortlist entry, until you have a named factory |
| **All retail listings** (Ammo Can Man, Ozark Outdoorz, Tactical Shit, Brownells, Wholesale Hunter) | Retailers. Not sources of factory pricing | Use only as market-price evidence, never as a supply route for 3,500+ |
| **FRH transport classification** | `UNKNOWN` — FRHs contain magnesium/iron powder and may carry dangerous-goods restrictions, particularly by air | Ask every supplier for the FRH's UN classification and any IATA/IMDG restriction. This can affect sample shipping |

---

## 10. The "U.S. Government Property" question

`FACT (search)`:

- DoD requires **"U.S. Government Property, Commercial Resale is Unlawful"** printed
  on each case of MREs, introduced in response to unauthorised sales to civilians.
- DLA/DSCP customer eligibility policy limits MRE sales to a defined set of
  organisations (US military and federally funded activities).
- Military MREs are procured by DLA with appropriated funds and are **owned by the
  government until consumed or properly disposed of**; they are **never** treated as
  surplus.
- GAO investigated the eBay trade in **GAO-06-410R**.
- The legal position on civilian *resale* is genuinely contested — some sources note
  no statute squarely prohibits private resale — but **theft-of-government-property
  exposure is not contested** where the stock originated with servicemembers or
  contractors.

**Commercially produced product — APack, Sure-Pak, XMRE, MRE STAR and every
non-US manufacturer in this pack — carries none of these restrictions.** It is
ordinary commercial food, subject only to normal food-safety and export rules.

**Recommendation, unambiguously: buy commercial production only.** For a
defence-adjacent Mexican government customer, delivering cases stencilled
"U.S. Government Property" would be an unrecoverable reputational and legal
problem, whatever the resale technicalities. Put an explicit warranty in your
purchase order: *"Goods shall be commercially produced and shall not bear any
United States Government property marking."*

---

## 11. What I could not verify (open items, ranked by value)

| # | Open item | Why it matters | Where to get it |
|---|---|---|---|
| 1 | **Incumbent SEDENA ration award price and manufacturer** | Tells you the ceiling before you quote | CompraNet |
| 2 | **Actual DLA contractor unit prices for MRE** (not the $150.32 standard price) | The true US factory benchmark | SAM.gov, FPDS, USAspending |
| 3 | **Named export/defence sales contacts at all 26 companies** | You cannot send the RFQ without them | Company sites, LinkedIn, trade-show directories — see `04-supplier-contact-sheet.md` |
| 4 | **HS classification and Mexican duty rates** | Can move landed cost 15–20% | Mexican customs broker |
| 5 | **Spanish/Polish MoD per-unit prices** | European benchmark | TED, Plataforma de Contratación del Sector Público |
| 6 | **UNIFO's actual capacity** | Underpins the 500K–1MM recommendation | Direct question in the RFQ |
| 7 | **AmeriQual commercial/export MOQ and whether APack is still produced** | Decides whether the best US supplier is even available | Direct question |
| 8 | **Current APack production dates on offered stock** | Decides whether any of it is buyable | Case-code read, demanded in writing |

---

## 12. Before money moves — mandatory primary-source confirmations

Nothing in this pack substitutes for these:

1. Certificate copies with **numbers and expiry dates** (HACCP, ISO 22000 / FSSC
   22000 / BRCGS / IFS), verified on the certification body's register.
2. **Factory address and legal entity**, cross-checked against a company registry.
3. **Nutritional analysis per menu** from an accredited lab, not a marketing sheet.
4. **Shelf-life validation study** supporting the claimed 24–36 months.
5. **Manufacturing date policy** in writing on the PO.
6. **Sample product physically evaluated** against `05-sample-evaluation-scorecard.md`.
7. **Mexican regulatory pathway confirmed** by a customs broker and a Mexican
   regulatory consultant, in writing, before the pilot ships.
8. **Bank details verified by voice callback** to a number obtained independently of
   any email. Procurement fraud in this category is routine.

---

## 13. WHO I WOULD CONTACT FIRST TOMORROW MORNING

Ranked. One sentence each. Contact details and the verification protocol are in
`04-supplier-contact-sheet.md` — **run Step 1–3 of that protocol on each name
before you send**, because none of these contacts could be confirmed from inside
this research session.

| # | Contact | Why them, first |
|---|---|---|
| 1 | **SOPAKCO — wholesale desk (`sphillips@sopakco.com`), then phone Mullins SC** | The only supplier in this entire audit with a published, working commercial wholesale channel selling an individual meal whose **food components are identical to the military MRE in your customer's photograph** — this is the fastest legal route to the 3,500 pilot and you should open it before anything else. |
| 2 | **Jomipsa — export / defence sales, Alicante** | They already manufacture the exact architecture your customer uses (three MRE-style meals per 24-hour pack, built for the UAE), in native Spanish, with an existing Latin American military channel — and no one has priced them for Mexico. |
| 3 | **UNIFO — export sales, Gebze** | Your most likely source of a genuinely low number at 100K+ from a real dedicated ration line, and the sooner you have their price the sooner every other quote becomes negotiable. |
| 4 | **AmeriQual — commercial / private-label enquiry, Evansville** | They assembled the pouch your customer photographed, which makes their commercial quote both the definitive benchmark and the single most persuasive thing you can put in front of the end customer — ask specifically whether APack or an equivalent commercial line is still produced, and what the export MOQ is. |
| 5 | **MRE STAR — wholesale / export desk** | The only supplier found that explicitly advertises customising rations **in the customer's language with the customer's national insignia**, which is precisely the Spanish private-label capability this deal turns on. |
| 6 | **XMRE / NEX-XOS — Pembroke Park FL** | US-made, explicitly export- and government-oriented, and likely to accept a 3,500-unit order that the DLA primes may refuse — a useful pilot fallback. |
| 7 | **Baxters North America (Wornick) — Cincinnati** | The third US prime; you need their number to have any real leverage over AmeriQual and SOPAKCO, and a genuine second source before you commit to volume. |
| 8 | **Golden Season — Singapore** | Your Asian price benchmark from a Singapore-domiciled company that states it builds MRE packs to customer specification, with cleaner contracting and English documentation than most regional alternatives. |
| 9 | **ARPOL — Zielona Góra** | The strongest independently verifiable defence credentials of any European candidate (NATO AQAP 2110, NCAGE 1126H) and a genuine self-heating capability, worth a quote even though their product line skews to 24-hour rations. |
| 10 | **A Mexican customs broker — not a supplier** | This is the contact most people leave until week six and it is the one most likely to determine whether your pilot lands on time: get the HS classification ruled and the SENASICA/COFEPRIS pathway confirmed while the RFQs are still out. |

**Also on day one, in parallel:** ask the customer in writing for the incumbent
ration's technical data sheet, and confirm whether they require a single-entrée
(US MRE) or two-entrée (SEDENA-style) meal. That one answer removes the largest
remaining ambiguity in the whole specification.

---

## 14. Final answers to your closing questions

### What I would buy for the first 3,500 meals

**SOPAKCO Sure-Pak 12 with heaters, specified up to ~1,250 kcal with a full
accessory pack**, bought through SOPAKCO's wholesale programme, shipped LTL from
Mullins SC into Mexico under USMCA.

Reasoning: same food components and same prime as the pouch your customer
photographed; legal to resell and export; ~292 cases is about six pallets, which is
days of freight rather than weeks; and it is the only route where a fresh,
correctly dated, fully documented qualification lot can realistically be on the
customer's table inside six weeks.

**If SOPAKCO's MOQ blocks it:** XMRE/NEX-XOS, then MRE STAR.

**Better still, if the budget stretches:** split the pilot — ~1,750 units from
SOPAKCO and ~1,750 from the best international quote. Two supply chains, two
customs pathways and two products tested for barely more money. This is the highest
return on any dollar in this programme.

### Maximum price per meal for the pilot

| Configuration | Maximum I would accept, landed Mexico |
|---|---|
| **Config B (premium, ~1,250 kcal, with FRH)** | **$9.50/meal** |
| **Config A (value, 900–1,100 kcal)** | **$7.00/meal** |

`ESTIMATE`. Above $9.50 you are being sold either surplus or a distributor's
margin. Below about $5.50 at this quantity, be suspicious and check the
manufacturing date before you check anything else.

**Say this out loud once and then act on it: do not let the pilot price anchor the
programme.** A 3,500-unit run is a short production run with full setup cost
amortised over almost nothing. Paying $9/meal for the pilot and $5.50 at 250,000
is a normal and healthy outcome. Tell the customer that now, before they see the
pilot invoice and form the wrong expectation.

### Supplier to position for 100K+

**UNIFO (Turkey)** as primary, **Jomipsa (Spain)** as the qualified alternative.

UNIFO should produce the lowest credible factory number from a real ration line.
Jomipsa is the hedge that wins if duty treatment, Spanish-language packaging or
Latin American familiarity turn out to matter more than the last $0.40 — and under
the EU–Mexico agreement its landed-cost gap to Turkey may be smaller than the
factory-price gap suggests.

### Supplier to position for 500K–1MM+

**UNIFO** if the customer's budget lands near $5/meal; **AmeriQual** if it lands
near $9 and origin, certainty and audit-proof provenance outrank price.

At 500K–1MM you are buying **capacity and continuity**, not a unit price. Whoever
you pick, structure it as a **capacity option** — the right to volume at a fixed
formula, not a volume commitment — and keep **Baxters North America (Wornick)**
qualified as the second source. Never run a programme this size single-sourced.

### Realistic price per meal, by stage

`ESTIMATE`. **Landed Mexico**, both configurations.

| Stage | Config A — value | Config B — premium (your actual spec) |
|---|---|---|
| **3,500 pilot** | $5.00–$7.00 | **$6.50–$9.50** |
| **25,000** | $4.50–$6.00 | $5.90–$8.20 |
| **100,000** | $4.00–$5.50 | **$5.20–$7.20** |
| **250,000** | $3.75–$5.10 | $4.95–$6.75 |
| **500,000** | $3.60–$4.90 | $4.80–$6.50 |
| **1,000,000** | $3.45–$4.70 | **$4.65–$6.20** |

**The one-line summary of this entire audit:** the $4.17/meal figure that started
this exercise came from clearance stock of a discontinued retail line, the item
your customer actually photographed cannot legally be sold to you at any price, and
the honest number for a fresh, legal, MRE-equivalent meal delivered into Mexico is
roughly **$5–$7 at scale and $6.50–$9.50 for the pilot**. Everything above is the
evidence for that, and the plan to go and test it against real quotes.
