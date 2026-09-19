# Peptide / GLP-1 Market Profiles: Compounding Pharmacies, RUO Vendors, Consumer Brands, and Education/Testing Platforms

Research date: 2026-09-02. Companion data file: `research/02_pharmacy_ruo_consumer.json` (48 company objects).

## Method and limitations (read first)

- All facts were gathered with live WebSearch on 2026-09-02 (approximately 65 queries). Every fact in the JSON carries a source URL and a label (Verified fact / Company-reported claim / Third-party estimate / Analyst inference).
- **Direct page fetches were egress-blocked for every external domain** (company sites, fda.gov, review aggregators). Consequently:
  - RUO vendor **prices** for BPC-157, TB-500, semaglutide, tirzepatide, retatrutide, CJC-1295, ipamorelin, GHK-Cu, PT-141 and NAD+ are recorded as *not retrieved*. No prices were invented.
  - **Website audit scores** (1-5) are low-confidence inferences from search snippets, page titles and third-party reviews; each score carries that caveat in the JSON (`audit_confidence: low`).
  - Traffic proxies (Similarweb/Semrush), social audience counts and ad-library visibility could not be pulled; they are marked "no public estimate found" / "not retrieved".
- The session's WebSearch budget (200) was exhausted before a final round of per-company detail queries (founders, state licensure lists, exact list prices). Items that would have been covered by that round are flagged "Not verified this session".
- Companies that could not be verified at all and are therefore omitted or minimally profiled: **Absolute Pharmacy**, **Base Pharmacy**, **Precision Compounding** (no attributable results surfaced); **PeptideWiki**, **ResearchChemical/BioLabs** (not searched before budget exhaustion); Seed, Elysium, Novos (not searched; none has meaningful peptide positioning).

## Regulatory backdrop (verified, drives every ranking below)

| Date | Event | Source |
|---|---|---|
| 2023-09-29 | FDA placed BPC-157 (and other peptides) in 503A Category 2 ("significant safety risks") | fda.gov Category-2 page |
| Feb 2025 | FDA declared semaglutide shortage resolved; phased wind-down for compounders | fda.gov statement |
| Sept 2025 | FDA issued 50+ warning letters to compounders, telehealth firms and "research use only" sellers (semaglutide, tirzepatide, retatrutide, BPC-157, SARMs) | Health Law Alliance |
| Dec 2025 | Warning letters to Pinnacle Peptides, Prime Sports Nutrition; API importer Darmerica cited for distributing retatrutide to 503As | fda.gov |
| 2026-03-31 / 2026-06-17 | Warning letters to Gram Peptides and Wholesale Peptide (RUO GLP-1s, disease claims) | fda.gov |
| 2026-04-15 | FDA removed 12 peptides incl. BPC-157 from Category 2 (not an approval) | Orrick; Holt Law |
| 2026-04-30 | FDA proposed excluding semaglutide, tirzepatide, liraglutide from 503B bulks list; comments closed 2026-06-29 | Orrick; Pharmacy Times |
| 2026-07-23/24 | PCAC voted to recommend BPC-157, KPV, TB-500, MOTS-c, Epitalon, Semax (not Emideltide) for the 503A bulks list; advisory only, rulemaking pending | Buchanan; TIME; CNN |
| Aug 2026 | Paradigm Peptides owner sentenced to ~6 years (adulterated products) | CBS News |

Implication: as of September 2026 no 503A pharmacy has legal authority to compound the PCAC-recommended peptides from bulk until FDA completes rulemaking; GLP-1 bulk compounding is contracting; "research use only" labeling is treated by FDA as irrelevant when marketing implies human use (FTC's Health Products Compliance Guidance applies to the same claims).

---

## Segment A -- Compounding pharmacies / pharmacy-affiliated platforms (14 profiled)

Ranking criteria: (1) enforcement record 2018-2026, (2) verified 503A/503B footprint and testing infrastructure, (3) breadth of peptide/GLP-1 menu relevant to prescribers, (4) strategic resilience under the 2026 rule changes.

| Rank | Company | Model | Enforcement record found | Rationale |
|---|---|---|---|---|
| 1 | **Belmar Pharma Solutions** (Golden/Lakewood CO) | 6x 503A + 2x 503B | None found | Dual model, hormone-anchored revenue (pellets, testosterone) so less GLP-1-dependent; sermorelin/NAD+/peptides on 503A menu; strong clinician education. |
| 2 | **Wells Pharmacy Network** (Ocala FL) | 503A + 503B | None found | 20.5k sq ft 503A + 20k sq ft 503B, in-house sterility/endotoxin testing, A4M-embedded distribution. |
| 3 | **Olympia Pharmaceuticals** (Orlando FL) | 503A + 503B | None found | Dual model, publishes compliance-forward peptide policy content; menu not verified. |
| 4 | **Red Rock Pharmacy** (Utah) | 503A | None found | PCAB + LegitScript + USP 795/797/800 (third-party); clean record, but GLP-1-heavy (incl. tirz/sema combo) so exposed to 2026 wind-down. |
| 5 | **Valor Compounding** (Berkeley CA) -- control case | 503A, 18 states | FDA 483 on file | Explicitly refuses peptides/GLP-1s; included as the compliance benchmark, not a peptide supplier. |
| 6 | **Innovation Compounding** (Kennesaw GA; Revelation Pharma since Jan 2022) | 503A | None found | PE-backed platform; peptide menu unverified. |
| 7 | **Foothills Professional Pharmacy** | 503A, 50 states (company) | 2x WL Sept 2020 | Telemedicine fulfillment scale; older enforcement history. |
| 8 | **Hallandale Pharmacy** (Hallandale Beach FL) | 503A | WL 2020-03-11, closed out May 2022 | Major telehealth GLP-1/peptide fulfiller; catalog peptides historically off the bulks list. |
| 9 | **Strive Pharmacy** | Not verified | None found | Insufficient verifiable data; ranked mid-low on evidence, not on findings. |
| 10 | **Empower Pharmacy / Empower Pharma** (Houston TX) | 503A + 503B | WLs 2017, 2021, 2x 2025-04-02; 483 Aug 2024; recall; Lilly litigation | Largest scale, but the most persistent enforcement record in the set. |
| 11 | **ReviveRx** (Houston TX) | 503A | WL 2025-09-22 (HCG/thymosin beta-4 as biologics) | Telehealth-oriented; fresh warning letter specifically on peptide/biologic eligibility. |
| 12 | **Boothwyn Pharmacy** (Kennett Square PA) | 503A | WL 2018-07-25; WL 2026-01-16; OOS recall 2025-07-09 | Repeat sterility findings on GLP-1 lines; production paused in 2025. |
| 13 | **ProRx, LLC** (Exton PA per FDA; brief said Brooksville) | 503B | WL 2025-03-04 (cGMP: insects in sterile areas); Class II recall 2025-10-15 | GLP-1-only exposure plus adulteration findings. |
| 14 | **Tailor Made Compounding** (Nicholasville KY) | 503A | WL 2020-04-01; federal guilty plea; $1.79M forfeiture; founder sentenced | Defined by the criminal case (BPC-157, CJC-1295, ipamorelin, SARMs etc. as unapproved drugs). |

Cross-segment observations:
- Direct-to-consumer: none of the pharmacies sells without a prescription; all route through prescribers/telehealth. Consumer-facing "pharmacy-affiliated platforms" appear only as telehealth partners (not separately profiled here).
- State licensure lists were not retrievable; Foothills (50 states) and Valor (18 states) are company-reported.
- Peptides named for prescribers across the set: sermorelin, NAD+, BPC-157, CJC-1295/ipamorelin, thymosin beta-4/TB-500, glutathione, GAC, plus semaglutide/tirzepatide (Empower, Hallandale, Red Rock, ReviveRx, ProRx, Boothwyn).

---

## Segment B -- Research-use-only (RUO) peptide vendors (13 profiled; 3 defunct)

Ranking criteria: (1) absence/presence of FDA action, (2) published quality/testing claims, (3) payment and buyer-protection posture, (4) marketing restraint (the FDA's intended-use test). Prices could not be retrieved; no price-based ranking is offered.

| Rank | Vendor | Status | FDA action found | Rationale |
|---|---|---|---|---|
| 1 | **Particle Peptides** (PARTICLE s.r.o., Slovakia; ships US) | Active | None | Strongest documented quality claims (manufacturer inspected by FDA/EMA/NMPA/TGA/MFDS; cGMP, ISO 9001/13485); cross-border import risk. |
| 2 | **BioLongevity Labs** | Active | None | US GMP manufacturing + "triple third-party testing" claims; but consumer-press positioning ("peptides for the masses") is intended-use evidence. |
| 3 | **Polaris Peptides** | Active | None | Independent sample-testing coverage (97 samples); thin public footprint. |
| 4 | **Core Peptides** | Active | None | Mainstream vendor; no enforcement surfaced; limited verifiable quality data. |
| 5 | **Biotech Peptides** | Active | None (but BPC-157 listings cited in FDA's July 2026 PCAC briefing) | Now on FDA's documentary radar. |
| 6 | **Sports Technology Labs** | Active | None | SARM-led catalog raises criminal-referral risk profile even absent a letter. |
| 7 | **Aminos.Science** | Active | None | "99% HPLC" and institutional-customer claims unverifiable. |
| 8 | **Limitless Life Nootropics** | Active | None | Zelle/CashApp/Revolut-only payments, BBB complaints, Trustpilot 3.4/5, r/Nootropics "unreliable". |
| 9 | **PureRawz** | Active | WL 715218 (2025-09-08, tianeptine) | FDA called RUO label a sham; peptide/SARM lines untouched by that letter. |
| 10 | **Swiss Chems** (NYC, est. 2018) | Active | WL 2024-12-10 (semaglutide, retatrutide; social posts cited) | Removed GLP-1s; still SARMs; influencer discount codes. |
| 11 | **Peptide Sciences** | Defunct (voluntary shutdown) | None | Former category leader; exit marks the enforcement wave. |
| 12 | **Amino Asylum** | Defunct (raid ~2025-06-18; founders pleaded guilty Dec 2025) | Multiple WLs ignored | Testosterone in SARM-labeled products. |
| 13 | **Paradigm Peptides** | Defunct (owner sentenced ~6 yrs, Aug 2026) | WL 2020-12-07 (COVID claims) | Adulterated with steroids. |

Compliance/positioning concerns (neutral summary): FDA warning letters to RUO sellers consistently cite (a) product pages for GLP-1 analogs (semaglutide, tirzepatide, retatrutide) and BPC-157, (b) dosing/benefit language, and (c) social-media posts as evidence of intended human use; the disclaimer does not cure this. FTC's Health Products Compliance Guidance (2022) requires competent and reliable scientific evidence for health-benefit claims and clear disclosure of paid endorsements (affiliate codes, TikTok creators). Alternative payment rails (Zelle/CashApp/crypto) indicate card-network exclusion and remove chargeback protection. Foreign-domiciled vendors add import-detention risk.

---

## Segment C -- Consumer supplement / collagen / cosmetic-peptide brands (12 profiled)

Regulatory classification: all are dietary supplements (DSHEA) or cosmetics; **none is an FDA-approved drug**. "Collagen peptides" (hydrolyzed collagen) and cosmetic signal/copper peptides are categorically different from injectable therapeutic peptides. Oral "BPC-157" capsule brands are the exception: unclear/unlawful status (BPC-157 is not a lawful dietary ingredient).

Ranking criteria: (1) verified scale/ownership and disclosed performance, (2) strength of peptide positioning, (3) substantiation/trust signals, (4) momentum in 2026.

| Rank | Brand | Class | Key verified facts | Rationale |
|---|---|---|---|---|
| 1 | **Thorne** (P&G, pending) | Supplement | $3.8B P&G deal (2026-08-04); >$500M 2025 revenue, ~$650M 2026 pace | Largest disclosed scale; practitioner + consumer; Collagen Plus. |
| 2 | **Vital Proteins** (Nestle Health Science) | Supplement | "#1 collagen brand" (Circana 52 wks to 2025-12-28); Jennifer Aniston paid spokesperson | Category-defining mass collagen; heavy price promotion ($16-$20 deals). |
| 3 | **Medik8** (L'Oreal, ~EUR1bn) | Cosmetic | Liquid Peptides $66; peptides = US growth engine; Advanced MP launched Jan 2026 | Strongest pure "peptide" skincare positioning validated by M&A. |
| 4 | **The Ordinary** (Estee Lauder) | Cosmetic | Multi-Peptide + Copper Peptides 1% at $30.90-$32 | Most accessible GHK-Cu product; transparent pricing. |
| 5 | **Momentous** | Supplement | $32M Humble Growth (2024); Huberman advisor; NSF Certified for Sport | Best trust stack among collagen brands. |
| 6 | **Timeline / Amazentis** | Supplement (adjacent) | CHF 56M Series D (L'Oreal BOLD, Nestle HS); GRAS, NSF; 25+ studies | Evidence-heavy longevity adjacency; not a peptide. |
| 7 | **ProLon / L-Nutra** | Food program (adjacent) | $48M funding; 40+ trials; bio-age -2.5 yrs claim | Competes for metabolic-health spend vs GLP-1/peptides. |
| 8 | **Ancient Nutrition** | Supplement | Founded 2016 (Axe/Rubin); 120+ investors; 47k+ Amazon reviews | Founder-content engine; limited disclosure. |
| 9 | **Drunk Elephant** (Shiseido) | Cosmetic | Protini ~$68; brand sales -14% in Q1 2026 | Hero peptide cream inside a turnaround. |
| 10 | **Olay Regenerist** (P&G) | Cosmetic | Collagen Peptide 24 at mass retail | Mass peptide claims; price not retrieved. |
| 11 | **BodyHealth PerfectAmino** | Supplement | Dr. David Minkoff; Gary Brecka page; "99% utilized" claims | Aggressive absorption claims; influencer-led. |
| 12 | **Oral BPC-157 brands** (ProHealth, Infiniwell, Everest, Amino Club) -- watchlist | Unclear | Sponsored listicles; availability contracting in 2026 | Regulatory status is the risk; not a lawful supplement ingredient. |

Consumer "oral peptide" traction note: search evidence shows Amazon-style availability of BPC-157 capsules has largely disappeared in 2026, with promotion shifting to PR-wire listicles, affiliate sites and TikTok; TikTok has begun banning retatrutide promotion.

---

## Segment D -- Education / membership / testing / practitioner platforms (9 profiled)

Ranking criteria: (1) verified funding/scale, (2) pricing transparency, (3) relevance to peptide users/prescribers, (4) regulatory posture.

| Rank | Platform | Type | Key verified facts | Rationale |
|---|---|---|---|---|
| 1 | **Function Health** | Testing membership | $298M Series B at $2.5B (Nov 2025); $450M General Catalyst financing (Jul 2026); ~$808M raised; 160+ tests | Category leader; monitoring layer for peptide/GLP-1 users. |
| 2 | **Superpower** | Testing membership | $199/yr; 100+ biomarkers; $30M Series A; $432M valuation; David Beckham | Price disruptor with care marketplace. |
| 3 | **SSRP Institute** | Clinician certification | Pro membership $999.50/yr or $99.95/mo; Foundations $99/$199/$299; 2026 certification cohort | Most transparent, structured peptide curriculum for prescribers. |
| 4 | **InsideTracker** (Segterra) | Testing membership | $149/yr membership; Ultimate $340 with membership | Incumbent; clear pricing. |
| 5 | **SiPhox Health** | At-home testing | $33M raised (Intel Capital, Khosla); from $99-$125; up to 60 biomarkers 4x/yr | Cheapest high-frequency re-testing. |
| 6 | **A4M Peptide Therapy Certification** | Clinician CME | 2 modules; GWU CME listing; partner price ~$500/module | Incumbent CME body; official price not retrieved. |
| 7 | **International Peptide Society** | Clinician membership | Founded 2018, Boca Raton; A4M/Informa discounts | Membership price not retrieved. |
| 8 | **Jay Campbell -- Fully Optimized Health** | Consumer community | $129 initial payment; Tuesday AMAs; women's calls | Influential demand driver for RUO vendors; affiliate-disclosure and unapproved-drug-claim exposure. |
| 9 | **Hunter Williams** | Consumer coaching | Podcast + guides + 1:1 coaching; prices undisclosed | Opaque pricing; unlicensed protocol advice. |

---

## What could not be verified (summary for the caller)

1. RUO vendor prices for the ten key peptides (all vendors) -- sites blocked; budget exhausted before aggregator queries.
2. Website audits -- no page rendered; scores are inferential and flagged low-confidence.
3. Traffic estimates, social follower counts, ad-library visibility -- none retrieved.
4. State licensure lists and founder/founding dates for most pharmacies (Empower, Olympia, Hallandale, Belmar, Strive, Wells).
5. Absolute Pharmacy, Base Pharmacy, Precision Compounding -- no attributable results; omitted.
6. Exact 2026 list prices for Vital Proteins, Olay, Ancient Nutrition, Momentous, Thorne Collagen Plus, Timeline, ProLon, Function Health ($499 widely reported but not re-verified).
7. Whether Superpower's marketplace routes to peptide/GLP-1 prescribers.
8. ProRx location discrepancy: FDA letter lists Exton, PA; the brief said Brooksville, FL -- FDA address used.
