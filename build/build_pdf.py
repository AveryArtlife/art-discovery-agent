import json, sys, os
sys.path.insert(0, "build")
from pdf_lib import *

mv = json.load(open("build/model_values.json"))
SM = mv["summary"]
def sv(label, sc): return SM[label][sc]
comp = json.load(open("research/05_compliance_matrix.json"))
celeb = json.load(open("research/03_celebrity_database.json"))
tele = [x for x in json.load(open("research/01_telehealth_companies.json")) if "company" in x]
prc = json.load(open("research/02_pharmacy_ruo_consumer.json"))

C = "build/charts/"
chart_scenarios(mv, C + "scen.png"); chart_funnel(mv, C + "funnel.png"); chart_market(C + "market.png"); chart_ltv(mv, C + "ltv.png"); chart_gantt(C + "gantt.png"); chart_pricebands(C + "prices.png")
import collections
cc = collections.Counter(x["relationship_class"].split(" - ")[1] for x in celeb)
order = ["Verified founder or cofounder", "Verified equity owner or investor", "Executive or board member", "Medical advisor", "Brand ambassador or spokesperson", "Recurring paid influencer", "Affiliate", "One-time campaign participant", "Unverified or rumored association"]
chart_bars([f"{i+1} {o}" for i, o in enumerate(order)], [cc.get(o, 0) for o in order], "Celebrity relationships found, by verified class (n = 59 records)", C + "celeb.png", figsize=(9.2, 3.2), horizontal=True)
rc = collections.Counter(i["risk_level"] for i in comp)
chart_bars(["High", "Med", "Low"], [rc["High"], rc["Med"], rc["Low"]], "Preliminary compliance matrix: 36 issues by risk level", C + "risk.png", color=CAT[1], figsize=(6, 2.6))
segcount = {"Telehealth / clinician-led": len(tele), "Compounding pharmacy": 14, "RUO vendor": 13, "Consumer supplement / cosmetic": 12, "Education / testing / practitioner": 9, "Celebrity-associated additions": 34}
chart_bars(list(segcount.keys()), list(segcount.values()), "Companies evaluated, by legal / business-model segment (n = 109)", C + "seg.png", color=CAT[0], figsize=(9.2, 2.8), horizontal=True)

Y = lambda s, y: money(sv(f"Year {y} net revenue", s))
CAP = lambda s: money(sv("Capital required (peak burn + 15% contingency)", s))
BE = lambda s: sv("Break-even month (first positive EBITDA)", s)
BE_s = lambda s: (str(int(BE(s))) if isinstance(BE(s), (int, float)) else str(BE(s)))

from reportlab.platypus import CondPageBreak
SB = lambda: CondPageBreak(4.2 * inch)
story = []
# ---------------------------------------------------------------- COVER
story += [Spacer(1, 2.1 * inch),
          Table([[Paragraph("AminoLord", S["cover_t"])]], colWidths=[CW], rowHeights=[None], style=[("LEFTPADDING", (0, 0), (-1, -1), LM)]),
          Table([[Paragraph("Peptide Market Audit, E-Commerce Strategy<br/>and Business Proposal", S["cover_s"])]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LM)]),
          Spacer(1, 1.3 * inch),
          Table([[Paragraph("Proposed concept · Working draft for founders, partners, investors, clinicians and counsel<br/>Prepared 2026-09-02 · United States market<br/><br/>Proposed principals: Scott Disick (brand partner, proposed) and Dr. Michael Azziz (medical cofounder, proposed). Both roles are unverified and subject to definitive agreements. No endorsement, ownership, or authorization is implied.", S["cover_m"])]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LM)]),
          NextPageTemplate("main"), SB()]

# ---------------------------------------------------------------- TOC
toc = TableOfContents(); toc.levelStyles = [S["toc0"], S["toc1"]]; toc.dotsMinLevel = 0
story += [Paragraph("Contents", S["h1"]), toc, SB()]

# ---------------------------------------------------------------- 1 Confidentiality
story += [H1("Confidentiality and important assumptions", "1"),
 P("This document is a working draft prepared for the AminoLord project owner. It combines a market audit, a strategic plan and a driver-based financial model for a **proposed concept**. It is not an offer of securities, and it is not legal, medical, regulatory, tax or investment advice. Every regulatory statement must be reviewed by qualified healthcare, FDA, pharmacy, corporate-practice-of-medicine, privacy, advertising and intellectual-property counsel before reliance."),
 H2("Labeling convention"),
 T([["Label", "Meaning"], ["Verified fact", "Corroborated against an authoritative or primary source surfaced in research on 2026-09-02"], ["Company-reported claim", "Stated by the company itself (site, release, filing); not independently verified"], ["Third-party estimate / report", "Trade press, law-firm alert, database or estimation tool; not independently verified"], ["Analyst inference", "Our synthesis from indirect evidence"], ["Strategic recommendation [SR]", "What we advise; a judgment, not a fact"], ["Financial assumption [FA]", "A modeling input; editable in the workbook; not a forecast"], ["Recalled / unverified", "Figures the research team could not access live and reproduced from prior knowledge; must be re-checked"]], widths=[1.7 * inch, CW - 1.7 * inch]),
 H2("Research limitations that materially affect this document"),
 CALLOUT("The research environment used for this project blocked direct page loads of company websites, regulators, review sites, advertising libraries and traffic tools, and capped web searches. Consequently: (1) company facts derive from dated search-result excerpts of the cited pages rather than full page reads; (2) website UI/UX scores are either 'not assessed' or low-confidence inferences, and no screenshots were captured; (3) traffic estimates, social audience counts and ad-library activity were not retrievable; (4) the market-size and benchmark workstream was produced without live access and is labeled recalled/unverified; (5) identity, licensure and trademark checks for the proposed principals could not be completed against USPTO, NPI Registry or state medical boards. Nothing was invented. Every deliverable carries a verification backlog (see 08_AminoLord_Evidence_Ledger.xlsx) that should be worked before any external use."),
 H2("Assumptions used throughout"),
 *BUL(["Initial geography: United States; prescription programs launch only in states where corporate-practice, telehealth-modality and pharmacy-licensure conditions are satisfied.", "Primary model evaluated: premium consumer health — education, clinical intake, telehealth through an affiliated medical practice, licensed-pharmacy fulfillment, membership, and compliant non-prescription commerce.", "Brand and domain: AminoLord / AminoLord.com. The domain resolves to parking infrastructure and no public entity, trademark filing, social presence or press mention was found (analyst inference; registrar and USPTO checks blocked).", "Scott Disick and Dr. Michael Azziz: proposed roles only. No public evidence connects either to AminoLord. Two scenarios are planned: A (named partners under signed agreements) and B (independent brand).", "Budget, ownership, launch date and capitalization are unconfirmed; the financial model provides conservative, base and upside cases with an assumptions register."]),
 SB()]

# ---------------------------------------------------------------- 2 Executive summary
story += [H1("Executive summary", "2"),
 P("Peptides moved from niche to mainstream between 2023 and 2026, pulled by GLP-1 normalization, podcast culture and a 2026 federal reversal that is reopening compounding access to several popular peptides. The category is now crowded with three very different kinds of business that are often confused: licensed telehealth programs, research-use-only (RUO) chemical vendors, and consumer 'peptide' supplements and cosmetics. Enforcement in 2025–2026 has been aimed squarely at the second group and at misleading compounded-GLP-1 marketing in the first. The white space is a brand that is premium in feel, clinician-led in substance, and radically transparent about what it will not sell."),
 STATS([("109", "companies mapped; 75 audited in depth"), ("59", "celebrity relationships classified"), ("36", "compliance issues; 23 rated High"), (Y("Base", 3), "Base-case year-3 net revenue [FA]"), (CAP("Base"), "Base-case capital required [FA]")]),
 H2("What we recommend"),
 *BUL(["**Business model:** a premium membership and clinician-led telehealth platform (management-services company plus affiliated medical practice and licensed 503A/503B pharmacies), with an education library and a separate non-prescription shop. Prescription products are reached only through eligibility screening and independent clinician consultation, never an open cart. Compounded GLP-1s are excluded; GLP-1 demand is routed to branded direct-to-consumer channels or clinician care.",
        "**Positioning:** 'Peptide health, done properly' — standards-first premium longevity for 30–55-year-olds who have heard about peptides and want a trustworthy way in. Reasons to believe: named licensed clinicians, licensed US pharmacies, an FDA-status badge on every ingredient, honest evidence grades, all-in pricing, and a public list of what AminoLord will not sell.",
        "**Principals:** proceed on two parallel tracks. Scenario A treats Scott Disick as a brand partner for creative direction and launch awareness under a name-and-likeness agreement with FTC disclosure, morality, exclusivity and termination terms, and Dr. Michael Azziz as medical director once identity, licensure and board status are verified. Scenario B launches without either. The brand must be able to stand on its clinical substance in either case.",
        f"**Launch path:** six phases over roughly nine months to public launch: foundation and compliance, internal pilot, private beta in 4–6 states, waitlist and early access, coordinated public launch, then state-by-state expansion. The base case reaches positive monthly EBITDA in month {BE_s('Base')} and needs about {CAP('Base')} of capital; the conservative case needs {CAP('Conservative')} and does not break even within 36 months, which is the honest downside if demand disappoints and spend continues.",
        "**Largest risks:** regulatory reversal on peptide compounding; FTC action on subscriptions, testimonials and endorsements; state corporate-practice and pharmacy-licensure constraints; ad-platform and payment-processor restrictions; and key-person and reputation risk concentrated in a celebrity partner with a prior FTC warning letter and a documented GLP-1 association."]),
 H2("Direct answers to the fifteen questions posed"),
 T([["Question", "Short answer"],
    ["Segment leaders", "Telehealth: Hims & Hers (scale), Function Health (capital, no Rx yet), Superpower, Hone, Joi/Blokes. Pharmacies: Belmar, Wells, Olympia (clean records; dual 503A/503B). RUO: none recommended; category is under enforcement. Consumer: Thorne, Vital Proteins, Medik8, The Ordinary. Platforms: Function, Superpower, SSRP (education)."],
    ["Strongest UI/UX and conversion systems", "Could not be scored from rendered pages this session. Third-party descriptions point to flat transparent pricing (Peter MD, Henry Meds), labs-first onboarding (Hone, Marek, Superpower), and Hims-style bundled convenience as the conversion patterns to study first."],
    ["Most attractive categories and models", "Clinician-led programs built on lawfully compoundable or approved peptides (sermorelin, NAD+, tesamorelin) plus diagnostics memberships; RUO and compounded GLP-1 are commercially attractive only until enforcement, which has already arrived."],
    ["Effective marketing tactics", "Founder or clinician long-form content, podcasts, educational SEO, labs-to-program funnels, disclosed creator programs; single-spectacle campaigns produce spikes not trust."],
    ["Riskiest practices", "RUO positioning, compounded-GLP-1 'same as Ozempic' claims, hidden subscriptions and fees, fake or atypical testimonials, before/after imagery, undisclosed celebrity compensation, health-data leakage to ad pixels."],
    ["Verified celebrity founders/partners", "29 verified founders/cofounders and 14 verified investors across 59 records (e.g., Kourtney Kardashian/Lemme, Hailey Bieber/Rhode, Mark Hyman/Function, Robbins & Diamandis/Fountain Life, Campbell & Williams/BioLongevity Labs; Serena Williams is a Ro ambassador, not an owner)."],
    ["Is celebrity-led positioning durable?", "Only when the celebrity owns equity, engages repeatedly in trusted formats, and the product has independent substance. Cosmetic involvement (Ladder, SKKN) did not convert; exits (Oprah/WW, Brecka/10X) were costly."],
    ["Copy / adapt / avoid", "Copy: transparent all-in pricing, named clinicians, labs-first safety. Adapt: diagnostics membership, education library. Avoid: RUO, ingredient 'stacks', step-up intro pricing, hidden memberships, B/A imagery."],
    ["Business model to pursue", "Option 3 hybrid: premium membership plus telehealth/MSO with compliant commerce; education-only as fallback if counsel restricts the formulary."],
    ["What must be true before principals are public", "Verified identity and credentials; signed agreements with NIL, disclosure, morality, exclusivity, termination and post-termination terms; resolution of any prior GLP-1 endorsement exclusivity; medical-independence protections; counsel sign-off."],
    ["Website architecture and technology", "Next.js site and member portal; Shopify for non-Rx commerce only; licensed telehealth/EHR/e-Rx vendor for the clinical core; Stripe Billing for programs and membership; HIPAA-eligible data warehouse; consent logging; no health data to ad platforms."],
    ["Most credible launch sequence", "Foundation → internal pilot → private beta (4–6 states) → waitlist and early access → coordinated public launch → tranche-based expansion."],
    ["Capital, team, partners, approvals", f"Base {CAP('Base')} (conservative {CAP('Conservative')}); 10–14 people by launch; telehealth/EHR vendor, 2 pharmacies, lab partner, ID verification, high-risk-capable processor; counsel opinions, LegitScript certification, insurance, medical director sign-off."],
    ["Biggest reasons for failure", "Regulatory reversal; FTC/state enforcement; ad-platform lockout; retention below 85% month-1; principal controversy; pharmacy quality event; running the conservative case without cutting spend."],
    ["Five next actions", "1) Verify principals and secure term sheets or activate Scenario B; 2) engage counsel for structure and formulary memo; 3) file trademark clearance and secure handles; 4) issue vendor RFPs (telehealth/EHR, pharmacies, labs, payments); 5) fund Phase 0 and start the prototype and library."]], widths=[1.9 * inch, CW - 1.9 * inch], font=7.4),
 SB()]

# ---------------------------------------------------------------- 3 Opportunity
story += [H1("The AminoLord opportunity", "3"),
 P("Three forces converge. First, demand: peptides are now a mainstream wellness conversation, carried by GLP-1 normalization (roughly one in eight US adults reports ever using a GLP-1 drug per KFF polling — recalled, unverified), by podcast hosts who have discussed BPC-157 dozens of times, and by a 2025–2026 press cycle on the 'peptide boom'. Second, supply: the Sept 2023 FDA decision that placed about nineteen popular peptides in 503A Category 2 was partially reversed in 2026 — HHS announced on Feb 27, 2026 that most would move out; FDA updated the 503A bulks document on Apr 15, 2026; and the Pharmacy Compounding Advisory Committee recommended BPC-157, KPV, TB-500, MOTS-c, semax and epitalon on Jul 23–24, 2026 over staff objections (third-party reports; final rulemaking pending). Third, trust: enforcement against RUO sellers and misleading compounded-GLP-1 marketing has removed the low-integrity end of the market and made compliance a visible differentiator."),
 H2("Why now, and why this concept"),
 *BUL(["The incumbents are either scaled generalists adding peptides late (Hims & Hers plans NAD+, sermorelin and glutathione before end-2026), diagnostics-first platforms converging on the same funnel (Function, Superpower, Hone, Lifeforce), or budget hormone clinics with thin trust infrastructure. Nobody owns 'the trustworthy premium front door' to peptide health.",
        "A brand that publishes FDA status and evidence grades for every ingredient, names its clinicians and pharmacies, prices all-in, and states what it will not sell can convert the largest untapped segment: curious, affluent adults who are put off by both the 'peptide bro' aesthetic and the hospital feel.",
        "Celebrity awareness can compress the time to a national audience, but the research is unambiguous that awareness without substance does not convert and that a health brand inherits its face's reputation. The concept is therefore designed so that the medical substance leads and any celebrity involvement amplifies it."]),
 H2("What AminoLord would sell"),
 T([["Layer", "Offer", "Legal frame", "Revenue"], ["Education", "Peptide library, evidence grades, clinician video, journal", "Editorial; medically reviewed", "Indirect (SEO, trust)"], ["Membership", "Navigation, clinician Q&A, lab coordination, member pricing on non-Rx, community", "Membership services; auto-renewal law", "Recurring fee"], ["Clinician-led programs", "Eligibility → intake → independent clinician → Rx if appropriate → licensed pharmacy → monitoring", "Affiliated medical practice; MSO services; pharmacy dispensing", "Program fees (structure per counsel)"], ["Labs", "Baseline and monitoring panels via lab partners", "Clinician-ordered", "Lab fees"], ["Non-Rx shop", "Supplements and cosmetics that meet standards; no RUO", "DSHEA / cosmetics", "Retail margin"]], widths=[1.1 * inch, 2.5 * inch, 1.8 * inch, CW - 5.4 * inch]),
 SB()]

# ---------------------------------------------------------------- 4 Market definition and size
story += [H1("Market definition and market size", "4"),
 CALLOUT("Caveat on every number in this section: the market-size workstream could not access syndicated reports or filings during this project; values are recalled ranges from analyst knowledge (cutoff mid-2026), labeled recalled/unverified in the evidence ledger with source URLs to re-check. They are presented for structure and order of magnitude, not as verified data."),
 IMG(C + "market.png"), SRC("research/06_market_size.json (recalled, unverified): Grand View Research, Precedence Research, Fortune Business Insights, McKinsey Future of Wellness 2024–25, company statements. Midpoints of ranges; log scale."),
 H2("Which markets apply, and which do not"),
 T([["Market", "Definition, geography, base, forecast, CAGR", "Reported or inferred", "Applicability"],
    ["Peptide therapeutics", "Approved peptide drugs; global; 2024 ~$45–50B → 2030 ~$75–80B; ~8–9%", "Third-party (recalled)", "Low — pharma GLP-1/insulin dominated; context only"],
    ["503A/503B compounding", "US; 2024 ~$5.5–6.5B → 2030 ~$8–9B; ~5–6%", "Third-party (recalled)", "High as supply market and cost base"],
    ["Telehealth / virtual care", "US; 2024 ~$40–45B → 2030 ~$90–120B; 15–20%; cash-pay DTC subset ~$4–6B (2025)", "Third-party; DTC subset inferred", "High — cash-pay DTC subset is the core SAM"],
    ["Longevity / healthy aging", "Global anti-aging ~$70–80B (2024); longevity therapies ~$25–30B; ~7–9%", "Third-party (recalled)", "Moderate — demand narrative"],
    ["Medical weight management / GLP-1", "US branded anti-obesity ~$20–25B (2025) → $60–80B (2030); compounded GLP-1 peak run-rate ~$1.5–3B early 2025, declining", "Inferred from Novo/Lilly, Hims, LifeMD", "High as demand engine; compounded segment is a wind-down, not a target"],
    ["Hormone optimization / TRT", "US TRT ~$1.2–1.5B (2024); cash-pay hormone/peptide clinics and telehealth ~$3–5B (2025), 12–15%", "Third-party; clinic set inferred", "High — direct competitive set"],
    ["Sports recovery / performance", "US recovery tech and services ~$3–5B; sports nutrition global ~$45–50B", "Inferred / third-party", "Moderate — adjacency"],
    ["Consumer wellness", "Global ~$2.0T (2025); US ~$480–500B; 4–10%", "Third-party (McKinsey, recalled)", "Context only"],
    ["Premium / personalized supplements", "US supplements ~$55–65B; personalized nutrition global ~$15–20B, 12–15%", "Third-party (recalled)", "Moderate — non-Rx shop"],
    ["Personalized / precision medicine", "Global ~$550–650B broad; ~$100–140B narrow", "Third-party (recalled)", "Low — excluded from sizing"],
    ["Men's health telehealth", "US ~$3–4B (2024) → $6–8B (2028)", "Inferred from Hims, Ro, Hone", "High — same persona"],
    ["DTC lab testing / diagnostics memberships", "Global ~$2.5–3.5B (2024) → $5–7B; Function Health ~$2.5B valuation, >200k members at $499/yr", "Third-party; company-reported", "High — on-ramp product"]], widths=[1.35 * inch, 2.7 * inch, 1.25 * inch, CW - 5.3 * inch], font=7.2),
 H2("TAM, SAM and initial SOM (three definitions)"),
 T([["", "Conservative", "Base", "Expansive"],
    ["TAM (US, annual spend addressable by the model)", "Cash-pay hormone/peptide optimization (~$3B) + cash-pay DTC telehealth share relevant to longevity/men's health (~$2B) + longevity diagnostics memberships (~$1B) ≈ **$6B**", "Add full cash-pay DTC telehealth (~$5B) and premium supplement slice (~$3B) ≈ **$11B**", "Add branded GLP-1 DTC context and broader premium wellness ≈ **$20B+**"],
    ["SAM (states served × premium segment)", "40% population coverage at launch × ~$4B direct set ≈ **$1.6B**", "85% coverage by month 24 × ~$5B ≈ **$4B**", "National coverage × ~$8B ≈ **$8B**"],
    ["SOM (year-3 net revenue from the model)", f"**{Y('Conservative', 3)}** (~0.3% of SAM)", f"**{Y('Base', 3)}** (~1% of SAM)", f"**{Y('Upside', 3)}** (~2.5% of SAM)"]], widths=[1.6 * inch] + [(CW - 1.6 * inch) / 3] * 3),
 SRC("Analyst inference built on recalled ranges above and the financial model (07_AminoLord_Financial_Model.xlsx). All three definitions must be rebuilt once syndicated reports and company filings are verified."),
 SB()]

# ---------------------------------------------------------------- 5 Segmentation
story += [H1("Market segmentation", "5"),
 P("The seven categories below operate under different laws and economics and should never be compared as if equivalent. The universe mapped in 01_Peptide_Market_Landscape.csv contains 109 companies; 75 received the detailed audit."),
 IMG(C + "seg.png", maxh=2.6 * inch), SRC("01_Peptide_Market_Landscape.csv; research/01, 02, 03. Counts are companies profiled, not market shares."),
 T([["Segment", "How revenue is made", "Rx / clinician?", "Who dispenses", "Product status", "Journey and pricing", "Principal risks"],
    ["1 Licensed telehealth / clinician-led", "Program or medication subscriptions, consults, memberships", "Yes", "Partner or owned 503A/503B pharmacies", "Approved and compounded drugs", "Quiz → intake → async/video → Rx → ship; $79–$400/mo + $39–$199 memberships", "CPOM, FTC subscriptions/claims, compounded-GLP-1 enforcement, formulary changes"],
    ["2 Compounding pharmacies", "Dispensing fees on prescriptions; 503B bulk sales to clinics", "Yes (prescriber)", "Themselves", "Compounded preparations", "B2B; not consumer facing", "FDA 483s/warning letters, sterility, bulks-list status, brand-owner litigation"],
    ["3 Longevity, hormone, metabolic, performance clinics", "Memberships $10K–$85K/yr (Fountain Life) to $99–$350/mo clinics; labs; Rx", "Yes", "Partner pharmacies", "Approved and compounded", "Labs-first; concierge", "Claims, off-label promotion, key-person"],
    ["4 Research-use-only vendors", "Online sale of peptide vials 'for research'", "No", "Themselves (often foreign manufacturing)", "Unapproved drugs when marketed for human use", "Cart checkout; alternative payment rails; affiliate codes", "FDA warning letters (Mar 2026 wave), DOJ prosecutions (Amino Asylum, Paradigm), card-network bans"],
    ["5 Consumer supplement, collagen, cosmetic peptide", "Retail and subscription product sales", "No", "3PL / retail", "Supplements and cosmetics", "Standard e-commerce; $16–$70 AOV", "DSHEA/cosmetic claims; 'GLP-1' naming (Lemme class actions)"],
    ["6 Education, membership, testing, practitioner platforms", "Diagnostics memberships $149–$499/yr; certifications $99–$1,000; communities", "Sometimes (labs ordered by clinicians)", "Labs / n/a", "Services", "Annual membership; upsell to care", "Health-data privacy; unlicensed protocol advice in communities"],
    ["7 Celebrity-founded adjacent wellness", "Product sales leveraging founder audience", "Rarely", "3PL / retail", "Supplements, cosmetics, fitness", "DTC and retail", "Endorsement disclosure, substantiation, key-person"]], widths=[1.1 * inch, 1.1 * inch, 0.8 * inch, 0.9 * inch, 0.85 * inch, 1.1 * inch, CW - 5.85 * inch], font=6.9),
 SB()]

# ---------------------------------------------------------------- 6 Competitive landscape
def rankrows(names, seg, keys):
    return [[str(i + 1)] + [S_(c, k) for k in keys] for i, c in enumerate(names)]
story += [H1("Competitive landscape", "6"),
 P("Ranking method: because private revenue and traffic tools were unavailable, companies were ranked within their own segment on a transparent proxy scorecard — disclosed funding or performance, formulary and program breadth, pricing evidence, review signals and vertical integration — with traffic, advertising and social metrics recorded as not retrieved. Ranks are provisional and documented in 02_Competitor_Website_Audit.xlsx (Segment Rankings)."),
 H2("Telehealth and clinician-led (top 12 of 27)"),
 T([["#", "Company", "Why it ranks here (evidence label)", "Peptide relevance"],
    ["1", "Hims & Hers", "Only public scaled player ($753M Q2-2026 revenue, company-reported via press); owns pharmacies; peptides (NAD+, sermorelin, glutathione) announced for launch before end-2026 with lab testing", "Entering; waits for FDA clearance on restricted peptides"],
    ["2", "Function Health", "$2.5B valuation (Nov 2025) and $450M growth financing (Jul 2026); >100k–200k members at $499/yr; celebrity investors; acquisitions (Ezra, Getlabs)", "No prescribing yet; obvious entrant"],
    ["3", "Superpower", "$199–$499/yr diagnostics; 13 Rx live since Jan 2026 incl. sermorelin and NAD+; ~$72M raised; celebrity investors", "Direct"],
    ["4", "Hone Health", "~$63M 2025 revenue (third-party estimate); $33M Series A; lab-gated sermorelin $130/mo + $149 membership; strong content", "Direct"],
    ["5", "Joi + Blokes", ">$50M bootstrapped revenue, 50k+ patients; sermorelin ~$199/mo", "Direct"],
    ["6", "Mochi Health", "500k+ patients, cash-flow positive (company-reported); sermorelin and NAD+", "Direct"],
    ["7", "Ivím Health", "Inc. 5000 #38 (2026); 50 states; sermorelin ODT $129, NAD+ $249, membership $74.99", "Direct"],
    ["8", "Noom Med", "Acquired Tailor Made Compounding (Apr 2026; 40+ peptide catalog); retail rollout not yet verified", "Vertical integration"],
    ["9", "Peter MD", "Low-price leader ($79–$99 TRT; peptides $150–$400); ~14k Trustpilot reviews at 4.8; sells BPC-157 in transitional status", "Direct; compliance watch"],
    ["10", "Maximus", "Brand-led; $15M Series A; sermorelin <$175/mo", "Direct"],
    ["11", "Lifeforce", "$129–$199/mo longevity membership with quarterly labs and peptides; closest single analog", "Direct"],
    ["12", "Marek Health", "Influencer-founded (MPMD); premium labs-first; broad peptide menu incl. BPC-157; per-vial pricing (~$350/15 mg)", "Direct; compliance watch"]], widths=[0.3 * inch, 1.1 * inch, 4.0 * inch, CW - 5.4 * inch], font=7.2),
 SRC("research/01_telehealth_companies.md and .json; labels per row in 08_AminoLord_Evidence_Ledger.xlsx. Ro (GLP-1 only), Eden, Henry Meds, TRT Nation, Defy, Gameday, AlphaMD, Calibrate, Limitless Male, BodyLogicMD, Fountain, Concierge MD, Mito, Found and Craft complete the 27."),
 H2("Other segments — leaders and cautionary cases"),
 T([["Segment", "Leaders (rationale)", "Cautionary cases"],
    ["Compounding pharmacies (14)", "Belmar (6×503A + 2×503B, hormone-anchored, no enforcement found); Wells (503A+503B, in-house sterility testing); Olympia (dual model, compliance-forward content); Red Rock (PCAB, LegitScript)", "Empower (warning letters 2017, 2021, two in Apr 2025; Lilly litigation); ReviveRx (WL Sept 2025 on HCG/TB-4); Boothwyn (WLs 2018, Jan 2026; recall); ProRx (WL Mar 2025; recall); Tailor Made (2020 WL, guilty plea, $1.79M forfeiture; now Noom-owned)"],
    ["RUO vendors (13; 3 defunct)", "None recommended. Particle Peptides and BioLongevity Labs publish the strongest quality claims; both still market to consumers, which FDA treats as intended human use", "Peptide Sciences (voluntary shutdown); Amino Asylum (raid Jun 2025; guilty pleas Dec 2025); Paradigm Peptides (owner sentenced ~6 years, Aug 2026); Swiss Chems (WL Dec 2024); PureRawz (WL Sept 2025)"],
    ["Consumer supplement / cosmetic (12)", "Thorne ($3.8B P&G acquisition pending, Aug 2026); Vital Proteins (#1 collagen, Circana); Medik8 (L'Oréal ~€1B; peptide skincare); The Ordinary (copper peptides ~$31); Momentous (NSF, Huberman)", "Oral 'BPC-157' capsule brands (not a lawful dietary ingredient; availability contracting); Lemme GLP-1 Daily (class actions; rebranded)"],
    ["Education / testing / practitioner (9)", "Function Health; Superpower; SSRP Institute (transparent clinician curriculum); InsideTracker; SiPhox", "Consumer communities selling protocol advice without licensure (affiliate-driven demand for RUO)"]], widths=[1.3 * inch, 3.0 * inch, CW - 4.3 * inch], font=7.2),
 SRC("research/02_pharmacy_ruo_consumer.md; FDA warning-letter references as cited in the evidence ledger (Verified fact where the FDA page surfaced; otherwise Third-party report)."),
 SB()]

# ---------------------------------------------------------------- 7 Website findings
story += [H1("Top-performing website findings", "7"),
 CALLOUT("Honest status: no competitor website could be rendered during this project, so the 23-criterion scores in 02_Competitor_Website_Audit.xlsx are marked 'not assessed' or low-confidence inference, and no screenshots exist. The findings below are patterns reported consistently by third-party reviews, press and search excerpts. They should be confirmed in a rendered-page audit (checklist provided in the workbook) before being treated as fact."),
 H2("Patterns reported across leaders"),
 T([["Pattern", "Where reported", "Effect on conversion or trust", "AminoLord stance [SR]"],
    ["Flat, published pricing", "Peter MD ($79–$99), TRT Nation ($99), Henry Meds ($149, no membership), Hone ($130 + $149)", "Reduces friction; but membership add-ons (Ivím ~$75, Eden $39→$99, Hone $149) often double effective cost and draw complaints", "All-in pricing before intake; one optional membership, never required for Rx pricing"],
    ["Labs-first onboarding", "Hone (owned phlebotomy), Marek, Superpower, Function, Lifeforce", "Improves safety narrative and retention; adds cost and delay", "Labs where clinically indicated; transparent lab pricing"],
    ["Bundled convenience", "Hims (consult + Rx + ongoing testing in one price)", "Highest scale in category", "Bundle consult, plan, monitoring; medication price shown separately when required by counsel"],
    ["Curated review widgets", "TRT Nation: Trustpilot 1.9 vs Birdeye 4.9", "Divergence is a due-diligence flag and an FTC fake-review exposure", "Verified reviews only; publish aggregate and link to source"],
    ["Step-up introductory pricing", "Eden, Noom", "Boosts starts; ROSCA disclosure hotspot", "Avoid"],
    ["Peptide 'menus' with per-vial prices", "Defy (34 peptides from $160/mo), Marek (BPC-157 ~$350/vial)", "Signals breadth; risks reading as a catalogue of unapproved drugs", "Programs by health goal; ingredient library with FDA status instead of a menu"],
    ["Compliance-forward waiting", "AlphaMD and Hims explicitly wait for FDA clearance before adding restricted peptides", "Builds trust with clinicians and regulators", "Adopt and publicize"],
    ["Founder-influencer channels", "Marek (MPMD), Ways2Well (Rogan appearances), BioLongevity Labs", "Powerful demand; scrutiny attaches to the founder", "Clinician-led content first; celebrity amplifies"]], widths=[1.3 * inch, 1.9 * inch, 2.0 * inch, CW - 5.2 * inch], font=7.2),
 H2("Customer-journey and medical-experience gaps noted"),
 *BUL(["Cancellation terms and refill criteria were rarely described in accessible third-party sources; FTC's NextMed order (Dec 2025) and the 2026 FTC/state action against Hims & Hers (third-party report) show these are enforcement targets.", "Clinician credentials are frequently presented generically ('our doctors'); named-clinician transparency (Defy, Hone) is the exception.", "Adverse-event instructions, contraindication screening and emergency disclaimers are not prominent on landing pages described in reviews; they are typically inside FAQs or consent documents.", "Several clinics sold BPC-157 during its transitional status (Apr–Sep 2026) — a visible signal of how each company weighs regulatory risk."]),
 SRC("research/01_telehealth_companies.json (customer_journey_notes, medical_experience_notes); research/05_regulatory_brief.md. Analyst inference where noted."),
 SB()]

# ---------------------------------------------------------------- 8 UI/UX white space
story += [H1("UI/UX patterns and white space", "8"),
 P("The category splits into two visual worlds: budget hormone clinics and RUO vendors with syringe imagery, dark gradients and price-led layouts; and diagnostics platforms with clean, data-heavy dashboards. Neither speaks to the premium, cautious adult who wants to understand before committing. The white space is an editorial-health experience that makes standards visible."),
 T([["White-space opportunity", "Evidence of gap", "How AminoLord fills it"],
    ["FDA-status and evidence badge on every ingredient", "No audited site is reported to label ingredients by 503A category or evidence grade", "Library component with 'Approved / Compounded / Restricted — not offered / Supplement' badge and A–D evidence grade with citations"],
    ["'What we won't sell' transparency", "Compliance postures are implicit (AlphaMD, Hims) rather than marketed", "Homepage block and Standards page listing exclusions (RUO, Category 2, compounded GLP-1s)"],
    ["Separation of Rx and retail", "Mixed menus at clinics; RUO carts", "Programs use 'Check eligibility'; only non-Rx items have 'Add to bag'"],
    ["Named clinicians with licensure", "Generic 'our doctors' common", "Clinician cards with license states and independence statement"],
    ["Two-click cancellation and renewal reminders", "Widespread opacity; ROSCA enforcement", "Subscription page designed to exceed California ARL and FTC expectations"],
    ["Health-data-aware analytics", "FTC actions on health-data sharing (GoodRx, BetterHelp precedents; Hims 2026 third-party report)", "Server-side pipeline; no health inputs to ad pixels; consumer-health-data consent"],
    ["Premium, discreet tone", "Biohacker jargon and physique imagery dominate", "Editorial typography, real people, no before/after"]], widths=[1.8 * inch, 2.3 * inch, CW - 4.1 * inch], font=7.4),
 SRC("Analyst inference from research/01 and research/02 messaging and audit notes; 05_AminoLord_Website_Strategy.md sections 1–2."),
 SB()]

# ---------------------------------------------------------------- 9 Product and pricing
story += [H1("Product and pricing landscape", "9"),
 P("136 offerings were inventoried across the 75 audited companies (03_Peptide_Product_and_Pricing_Audit.xlsx). Prices below are third-party or company-reported values captured on 2026-09-02; RUO vendor prices were deliberately not recorded because the sites could not be loaded."),
 IMG(C + "prices.png"), SRC("03_Peptide_Product_and_Pricing_Audit.xlsx (Price Bands); research/01, research/06 (benchmarks recalled/unverified for tesamorelin and CJC/ipamorelin). AminoLord band is a financial assumption."),
 H2("Regulatory classification of what is being sold"),
 T([["Classification", "Examples found in market", "Implication for AminoLord"],
    ["FDA-approved drugs", "Semaglutide, tirzepatide (branded DTC $149–$449); tesamorelin (Egrifta); bremelanotide (Vyleesi); testosterone", "Prescribable; brand must not promote off-label uses"],
    ["Compounded, permissible (Category 1 or approved-drug API)", "Sermorelin, ipamorelin, NAD+, glutathione", "Core of an initial formulary, subject to counsel and medical director"],
    ["Transitional (removed from Category 2 Apr 2026; PCAC-recommended Jul 2026; final rule pending)", "BPC-157, KPV, TB-500, MOTS-c, semax, epitalon; CJC-1295, GHK-Cu inj., AOD-9604, Ta1, selank pending review", "Exclude until final rulemaking; publish library entries; monitor monthly"],
    ["Remaining Category 2", "Melanotan II, GHRP-2, GHRP-6, LL-37, PEG-MGF", "Never"],
    ["Compounded GLP-1s", "Semaglutide $149–$399; tirzepatide $299–$599; 100+ FDA warning letters 2025–26; Apr 30, 2026 proposal to exclude from 503B bulks list", "Exclude; route to branded DTC or clinician care"],
    ["Supplements / cosmetics", "Collagen peptides, copper-peptide serums, urolithin A", "Non-Rx shop candidates with substantiated claims"],
    ["RUO", "Any vial 'for research' sold to consumers", "Never sold, linked or described as available"]], widths=[1.9 * inch, 2.6 * inch, CW - 4.5 * inch], font=7.2),
 H2("Monetization patterns and lifetime-value logic"),
 *BUL(["Memberships ($39–$199/mo) and care plans are the dominant recurring layer; they are also the most criticized when hidden. Diagnostics platforms anchor on annual fees ($149–$499).", "Consultation fees range from $0 (bundled) to $250 (Defy); lab fees are bundled (Hims planned) or $99–$600 separately.", "Lifetime value is retention-driven: benchmarks (recalled) suggest 5–10% monthly churn for DTC health subscriptions, 8–15% for GLP-1 and 2–4% for hormone programs.", "Pricing recommendation [SR]: do not copy competitor prices. Run the ten-step pricing plan (Van Westendorp, MaxDiff, interviews, landing-page tests, cost floor with ≥55% gross margin) in Phase 1; the model's $249–$299 all-in program band is a placeholder."]),
 SB()]

# ---------------------------------------------------------------- 10 Marketing and claims
story += [H1("Marketing and claims landscape", "10"),
 H2("Narratives that win, clichés that saturate, claims that endanger"),
 T([["Winning narratives (adopt)", "Overused clichés (avoid)", "Unsupported or risky claims (never)"],
    ["Clinician-led, data-driven care; transparent flat pricing; 'we wait for FDA clearance'; labs-first safety; plain-language education (Huberman/Attia-style)", "'Optimize', 'biohack', 'unlock', 'peptide stacks', 'anti-aging breakthrough', 'doctor-designed' without names, physique imagery, scarcity timers", "'Same as Ozempic'; implying FDA approval of compounded products; healing, longevity or fat-loss outcomes for BPC-157/TB-500; 'natural GLP-1'; results guarantees; typicality-free testimonials; RUO disclaimers as a shield"]], widths=[CW / 3] * 3),
 H2("Acquisition channels observed"),
 T([["Channel", "Observed use", "Assessment"],
    ["Organic search and educational content", "Hone, Marek, Ivím, Function, telehealth blogs; SSRP for clinicians", "Highest durable value; E-E-A-T requires named reviewers"],
    ["Podcasts and founder channels", "Marek (MPMD), Ways2Well (JRE), AG1/Onnit cap tables, Huberman/Momentous", "Repeated long-form recommendation converts; scrutiny attaches to host"],
    ["Paid search", "Certified telehealth advertisers (LegitScript required for Rx-related ads)", "Gate for AminoLord; apply in Phase 0"],
    ["Meta / TikTok / YouTube", "Hims 2025 Super Bowl (+650% traffic, third-party); TikTok banning retatrutide promotion; Meta health-data restrictions limit optimization", "Creative-led broad targeting; non-health optimization events"],
    ["Affiliates and creator codes", "RUO vendors (cited by FDA), consumer supplements (10–30% commissions)", "Non-Rx and education only; disclosed"],
    ["Referral programs", "Common in DTC supplements", "Membership/non-Rx only; never for prescriptions"],
    ["Practitioner referrals", "Belmar/Wells clinician education; A4M/SSRP", "Pursue education partnerships without per-Rx fees"],
    ["PR and press", "Function, Superpower, Neko funding stories; peptide-boom features", "Standards-first narrative and medical spokesperson"],
    ["Email / SMS", "Universal", "Benchmarks (recalled): email open 35–50%, click 1–2%; SMS CTR 6–10%"]], widths=[1.6 * inch, 3.0 * inch, CW - 4.6 * inch], font=7.2),
 SRC("research/01 and 02 (acquisition_channels_observed, messaging_claims); research/03 (Hims traffic spike, third-party); research/05 (platform policies, third-party reports); research/06 (channel benchmarks, recalled/unverified). Ad libraries were not accessible."),
 SB()]

# ---------------------------------------------------------------- 11 Celebrity findings
story += [H1("Celebrity-founder findings", "11"),
 IMG(C + "celeb.png", maxh=2.7 * inch), SRC("04_Celebrity_Founder_Database.xlsx; research/03_celebrity_database.json. Classification by evidence, not by advertising appearance; follower counts approximate and to be re-verified."),
 H2("Verified peptide-direct relationships"),
 T([["Company", "Person", "Class", "Evidence (label)"],
    ["BioLongevity Labs (RUO manufacturer)", "Jay Campbell, Hunter Williams, Josh Felber", "1 Founder/cofounder", "Forbes Jul 2026 coverage; company statements (third-party / company-reported)"],
    ["Fountain Life (longevity clinic; peptides, NAD+)", "Tony Robbins, Peter Diamandis", "1 Cofounder", "Company and press; $18M raise Aug 2025 (third-party)"],
    ["10X Health / The Ultimate Human", "Gary Brecka (former), Grant Cardone", "1 Cofounder / 2 Investor", "Litigation records 2024–25 (third-party); key-person case"],
    ["Ro (GLP-1 telehealth)", "Serena Williams", "5 Ambassador", "PR Newswire Aug 21, 2025 (verified); husband Alexis Ohanian is investor and board member"],
    ["Noom", "Rebel Wilson", "5 Ambassador ('Chief Wellness Ambassador')", "GlobeNewswire Sept 2025 (verified)"],
    ["Lemme ('GLP-1 Daily' supplement)", "Kourtney Kardashian Barker, Simon Huck", "1 Cofounder", "WWD; class actions CA/NY 2025 (third-party)"],
    ["Rhode (peptide lip treatment)", "Hailey Bieber", "1 Founder", "$1B e.l.f. acquisition May–Aug 2025 (verified)"],
    ["Function Health (diagnostics)", "Mark Hyman (cofounder/CMO); Damon, Efron, Hart, Pascal (investors)", "1 / 2", "Fierce, Modern Healthcare (third-party)"],
    ["Superpower", "Logan Paul, Steve Aoki, Vanessa Hudgens, Giannis Antetokounmpo", "2 Investor", "Series A announcement Apr 2025 (third-party)"],
    ["Ways2Well (peptide telehealth)", "Joe Rogan (listed as client; founder is repeat JRE guest)", "9 Unverified", "AP/CNN Nov 2025 (third-party)"],
    ["Vital Proteins", "Jennifer Aniston", "3 Executive title (CCO) attached to paid spokesperson role", "WWD; NBC (third-party)"],
    ["Blueprint", "Bryan Johnson", "1 Founder", "NYT 2025 reporting on losses (third-party)"]], widths=[1.7 * inch, 1.7 * inch, 1.2 * inch, CW - 4.6 * inch], font=7.2),
 H2("Lessons that shape the AminoLord design"),
 *BUL(["**Advantage is real when ownership, repetition and substance coincide.** Rhode (peptide lip SKU launch hero, $1B exit), AG1 and Onnit (podcast-host cap tables), Function Health (investor halo to $2.5B) and Prenuvo (unpaid Kim Kardashian post cited in a $120M raise) show measurable effects. Oprah's WeightWatchers arc priced one celebrity at roughly a quarter of market cap on exit (Feb 2024).",
        "**Involvement is cosmetic when the face is rented.** Ladder reached only ~$4M revenue with >180M combined followers; SKKN by Kim folded in 2025; investor cohorts announce and disappear.",
        "**Trust transfers fastest through medical credibility and breaks hardest there.** Prenuvo/Kardashian and 10X/Brecka both converted and both drew physician rebuttals; Goop's 2018 $145K settlement and Kim Kardashian's 2022 SEC $1.26M order set the disclosure and substantiation floor.",
        "**Key-person risk must be contracted for.** TB12's rebrand after the Brady–Guerrero split, 10X's $100M/$13M cross-suits, and Bulletproof's managed decoupling are the templates: earnouts, morals and PED-disclosure clauses, testimonial ownership, and equity in operating cofounders with domain credentials.",
        "**Peptide launches will be read as MAHA-adjacent in 2026.** Press ties the FDA reversal to influencer demand; any celebrity peptide brand inherits that political framing and the scrutiny that follows."]),
 SRC("research/03_celebrity_database.md sections 3.1–3.7 with sources by record."),
 SB()]

# ---------------------------------------------------------------- 12 Positioning
story += [H1("AminoLord positioning", "12"),
 P("Four territories were evaluated. Each is viable; one is recommended."),
 T([["Territory", "Target customer / problem", "Core promise and reasons to believe", "Personality, sample headline", "Advantages", "Risks"],
    ["A. Standards-first premium longevity (recommended)", "30–55, affluent, peptide-curious, distrustful of hype; problem: no trustworthy front door", "'Peptide health, done properly.' Named clinicians; licensed pharmacies; FDA-status badges; evidence grades; all-in pricing; public exclusions", "Calm, confident, editorial. 'We'll tell you what we won't sell.'", "Defensible against both budget clinics and generalists; aligns with enforcement direction; works in Scenario B", "Slower than hype-driven growth; requires clinical bench"],
    ["B. Modern men's health with peptides", "Men 30–50 already in TRT/ED telehealth", "'Beyond TRT': integrated hormone and peptide care", "Direct, masculine", "Large proven persona (Hims, Hone)", "Crowded; price-led; less differentiation; excludes women"],
    ["C. Luxury concierge health", "High-net-worth; problem: time and access", "White-glove clinician access, labs, priority", "Discreet, exclusive", "High ARPU; Fountain Life analog", "Small; celebrity may skew 'lifestyle over medicine'; low scalability"],
    ["D. Evidence-first education platform with commerce", "Broad curious audience", "'Understand peptides before you buy'", "Teacherly", "Lowest regulatory exposure; SEO moat", "Monetization limited; risk of becoming a referral site"]], widths=[1.15 * inch, 1.2 * inch, 1.5 * inch, 1.05 * inch, 1.1 * inch, CW - 6.0 * inch], font=6.9),
 H2("Why Territory A"),
 P("It is the only territory that converts the category's weakness — distrust — into the brand's asset, survives either direction of FDA rulemaking, and does not depend on a celebrity to be credible. Territory B is the fallback if research shows demand is overwhelmingly male and price-sensitive; Territory D is the fallback if counsel restricts the formulary so far that programs are not viable at launch. The brand should never be built on unsupported clinical outcomes or on the assumption that celebrity awareness creates trust; the celebrity research shows it does not."),
 H2("Brand architecture"),
 *BUL(["Masterbrand: AminoLord. Sub-labels: Programs (clinician-led), Library (education), Standards (governance), Shop (non-Rx).", "Design system: editorial serif wordmark, humanist sans UI, ink/bone/moss/brass palette, WCAG 2.2 AA; no syringes-as-hero, no before/after, no celebrity imagery without contract.", "Voice: plain language, honest about uncertainty, specific about what is included and excluded."]),
 SB()]

# ---------------------------------------------------------------- 13 Disick
story += [H1("Scott Disick — proposed role", "13"),
 CALLOUT("Verification status: identity verified (Scott Michael Disick, b. May 26, 1983; The Kardashians on Hulu; Talentless apparel). No public evidence of any relationship with AminoLord or with any peptide company was found. Everything below is a proposed structure contingent on his interest, his representatives, his Hulu and existing endorsement obligations, and counsel."),
 H2("What the research found"),
 T([["Finding", "Detail", "Label"],
    ["Audience", "~27M Instagram; ~5.7M X; small TikTok count reported (verify handle)", "Search snippet"],
    ["GLP-1 association", "Confirmed Mounjaro use on The Kardashians (Feb 2025: 'I'm not embarrassed I took it'; ~30 lb lost); a Yahoo headline reports him promoting a GLP-1 medication — brand, date and paid status unverified", "Verified / third-party (headline)"],
    ["FTC history", "On the FTC's Sept 6, 2017 list of 21 influencers sent warning letters on undisclosed material connections; 2016 Bootea caption incident; TINA.org database of his posts", "Verified"],
    ["Reputation", "Documented addiction and rehab history; frequent tabloid coverage; 2022 car crash", "Verified (public reporting)"],
    ["Commercial", "Talentless (2018); IN COMMON Beauty partner (2021); reported 'multiple vitamin companies' (unnamed); est. net worth ~$45M", "Third-party"],
    ["Rights holders", "Hulu cast agreement (two-season renewal 2024; S7 aired Oct 2025); agency not identified; trademarks not queryable", "Blocked / inference"]], widths=[1.2 * inch, 4.4 * inch, CW - 5.6 * inch], font=7.2),
 H2("Proposed responsibilities and terms (subject to definitive agreements)"),
 T([["Area", "Proposal [SR]"],
    ["Responsibilities", "Brand vision and creative direction input; media and launch awareness; community and content (founder-led series, disclosed); partnerships introductions; customer insight sessions. No involvement in clinical decisions, formulary, or medical content."],
    ["Deliverables and time", "Defined content days per quarter (e.g., 4–6), launch-week availability, quarterly creative review; approvals within agreed SLAs."],
    ["Media obligations", "Approved scripts only; all health statements medically reviewed; no personal outcome claims that are not typical; no discussion of prescription products beyond approved language."],
    ["Approval rights", "Consultation on brand creative; no veto over medical, compliance or pricing decisions."],
    ["Morality and reputation", "Mutual morality clause; suspension and termination triggers; crisis-communications cooperation; PED/medication disclosure obligations relevant to testimonials."],
    ["Exclusivity", "Category exclusivity in peptide/longevity/telehealth for the term; resolution of any existing GLP-1 endorsement conflict as a condition precedent."],
    ["Compensation scenarios (hypothetical)", "Cash retainer; equity with vesting tied to deliverables; capped royalty on net revenue; or mixed. Modeled in 07_AminoLord_Financial_Model.xlsx (Celebrity Economics). No terms have been offered or accepted."],
    ["FTC disclosure", "Ownership and compensation disclosed clearly and conspicuously in every endorsement (16 CFR Part 255, 2023); disclosure page on site; training and monitoring."],
    ["Name and likeness", "Licensed NIL with scope, territory, term, approved uses, and quality control; no use before signature."],
    ["Termination and post-termination", "Wind-down period for content removal; survival of disclosure obligations; buy-back or forfeiture of unvested equity; non-disparagement."]], widths=[1.6 * inch, CW - 1.6 * inch], font=7.3),
 SRC("research/04_principal_verification.md sections 1.1–1.8; FTC 2017 press releases (verified); E! Online and others Feb 27, 2025 (search snippets)."),
 SB()]

# ---------------------------------------------------------------- 14 Azziz
story += [H1("Dr. Michael Azziz — proposed role", "14"),
 CALLOUT("Verification status: no physician with the exact spelling 'Michael Azziz' was located. The most plausible candidate (~60% confidence, analyst inference) is Michael (H.) Aziz, MD, a New York internist (515 Madison Ave; Lenox Hill attending; author of The Perfect 10 Diet and The Ageless Revolution, 2025) whose practice markets peptide therapy, hormones and TRT. Dr. Ricardo Azziz (reproductive endocrinology) and Michael M. Aziz (Allegheny Health Network) are different people. NPI Registry, New York State Education Department, ABIM and PubMed checks were blocked; no disciplinary reports surfaced in the limited searches. The project owner must supply the intended physician's legal name, NPI and license state before any public reference."),
 H2("Credential requirements before appointment"),
 *BUL(["Active, unrestricted license in the affiliated practice's home state and in each launch state (or supervision structure per counsel); board certification claim verified (ABMS/ABIM); NPI and DEA (if applicable) verified; malpractice history and disciplinary lookups in all states; peer references; conflict-of-interest disclosure (ownership in pharmacies, RUO vendors, supplement brands, affiliate income)."]),
 H2("Proposed responsibilities and protections"),
 T([["Area", "Proposal [SR]"],
    ["Clinical governance", "Chairs the clinical governance committee; owns formulary policy keyed to FDA 503A status with change control; approves protocols; reviews adverse events; sets provider standards and credentialing."],
    ["Medical education and content", "Medical reviewer of record for library and program pages; review dates published; sign-off on all health claims in marketing."],
    ["Clinical independence", "Employed or contracted by the affiliated professional entity, not the brand/MSO; compensation fixed or time-based; expressly not tied to prescription volume, enrollment or revenue; documented authority to decline or restrict offerings."],
    ["Conflicts of interest", "Disclosure and recusal policy; no financial interest in dispensing pharmacies or suppliers; no affiliate income from peptide vendors."],
    ["State licensure limits", "Practices only where licensed; state medical directors added as expansion requires; telehealth modality rules per state."],
    ["Professional liability", "Individual and entity coverage; tail coverage; incident reporting."],
    ["Content approval", "Final say on medical accuracy; compliance lead has final say on legal claims; either can block publication."],
    ["Succession", "Named deputy medical director by Phase 2; documented handover; key-person insurance considered."],
    ["Public role", "May be presented publicly only after verification and agreement; title matches credentials; biography sourced."]], widths=[1.6 * inch, CW - 1.6 * inch], font=7.3),
 P("Medical decisions must remain independent of celebrity, sales, or marketing pressure. This is both a regulatory necessity (corporate practice of medicine; fee-splitting; anti-kickback principles) and the brand's core promise."),
 SRC("research/04_principal_verification.md section 2; research/05_regulatory_brief.md (CPOM, fee-splitting; analyst inference pending counsel)."),
 SB()]

# ---------------------------------------------------------------- 15 Business model
story += [H1("Recommended business model", "15"),
 T([["Criterion", "1. Education and wellness commerce only", "2. Telehealth/MSO with affiliated practice and licensed pharmacies", "3. Premium membership + telehealth/MSO + compliant commerce (recommended)"],
    ["Revenue streams", "Non-Rx products, affiliate (non-RUO), courses, sponsorship", "Program/consult fees (structure per counsel), labs, MSO management fees", "Membership + programs + labs + non-Rx + education"],
    ["Customer experience", "Learn and buy; no care", "Care pathway; episodic", "Continuous relationship: learn → screen → care → monitor"],
    ["Gross margin", "35–65% product", "50–65% blended (pharmacy, clinical, shipping)", "50–60% blended; membership lifts mix"],
    ["Operational complexity", "Low", "High (clinical, pharmacy, state law)", "High"],
    ["Required partners", "3PL, suppliers", "Telehealth/EHR vendor, professional entity, 503A/503B pharmacies, labs, ID verification, high-risk processor", "All of model 2 plus community/content"],
    ["Regulatory exposure", "FTC claims, DSHEA, privacy (CHD laws)", "CPOM, fee-splitting, telehealth, pharmacy, FDA status, HIPAA, ROSCA", "Model 2 plus auto-renewal on membership"],
    ["Time to launch", "3–4 months", "8–10 months", "8–10 months (membership can launch earlier)"],
    ["Capital to month 12 [FA]", "$1–2M", "$3.5–5M", f"{CAP('Base')} base ({CAP('Conservative')} conservative)"],
    ["Geographic scalability", "National", "State-by-state", "State-by-state for Rx; national for education, membership, shop"],
    ["Technology", "Shopify + CMS", "Portal + vendor clinical core", "Portal + vendor clinical core + Shopify"],
    ["Acquisition implications", "Content and creators; ad platforms permissive", "LegitScript certification; health-ad restrictions", "Education funnels de-risk paid dependence"],
    ["Principal risks", "Thin differentiation; RUO temptation", "Regulatory reversal; enforcement; clinical capacity", "Same, plus membership churn"]], widths=[1.15 * inch] + [(CW - 1.15 * inch) / 3] * 3, font=7.0),
 H2("Revenue architecture (legally supportable streams only)"),
 *BUL(["Membership fees (education, navigation, clinician Q&A, lab coordination, member pricing on non-Rx).", "Program and consultation fees collected in the structure counsel prescribes (the affiliated practice may need to be merchant of record for professional fees; the MSO charges fair-market-value management fees; pharmacies bill medication or the practice does, per state law).", "Compliant non-prescription commerce; educational products; clinician-led group programs; corporate wellness limited to education and testing.", "**Flagged for counsel:** referral fees, pharmacy rebates, prescription-volume incentives, percentage-of-collections management fees in strict CPOM states, and any revenue share with prescribers or celebrities tied to prescriptions."]),
 SRC("06_AminoLord_Launch_Plan.md; research/05_regulatory_brief.md; financial model. Structure is analyst recommendation pending counsel."),
 SB()]

# ---------------------------------------------------------------- 16 Customer experience
story += [H1("Customer experience", "16"),
 P("The experience is designed around four promises: understand before you commit, a real clinician decides, nothing is hidden, and help is always reachable."),
 T([["Stage", "What the member experiences", "What happens behind the scenes", "Safeguards"],
    ["First visit and education", "Homepage answers 'what is this and is it for me'; library with FDA status and evidence grades", "CMS with medical-review workflow; analytics without health data", "Educational disclaimers; reviewer names and dates"],
    ["Eligibility", "3-minute quiz; consented; clear outcome (proceed / not a fit with reasons)", "Red-flag rules; state gating; CHD consent logged", "No diagnosis; no guarantee of prescription"],
    ["Intake and consultation", "Account, ID check, state consent, history; async review within 48h or video where required", "Vendor EHR; licensed clinician in member's state", "Independence statement; informed consent; AE instructions"],
    ["Plan and payment", "Clinician plan with all-in price; auto-renewal terms; single confirmation", "Stripe Billing; consent versions stored", "ROSCA-grade disclosure; 2-click cancel"],
    ["Fulfillment", "Licensed pharmacy ships with tracking; onboarding sequence on use, storage, side effects", "e-Rx to 503A/503B; cold chain; status webhooks", "Recall procedure; pharmacy disclosure"],
    ["Monitoring and refills", "Day-7 and day-30 check-ins; labs cadence; refill request with short check-in", "Clinician review; hold if concerns", "Refill criteria; escalation"],
    ["Support and cancellation", "Support hours and SLAs; report-a-side-effect 24/7; pause or cancel in account", "Non-clinical vs clinical routing", "AE logging; clinician notified on discontinuation"]], widths=[1.15 * inch, 2.2 * inch, 1.9 * inch, CW - 5.25 * inch], font=7.2),
 SRC("05_AminoLord_Website_Strategy.md sections 4–5 [SR]."),
 SB()]

# ---------------------------------------------------------------- 17 Website concept
story += [H1("Website concept", "17"),
 P("AminoLord.com should feel premium, confident, modern, medically credible, educational, discreet, human, transparent, easy to navigate and mobile-first. The full specification (principles, design system, 16 page specifications, 12 user flows, 8 wireframes, draft copy, technology comparison) is in 05_AminoLord_Website_Strategy.md; the essentials follow."),
 H2("Design-system direction"),
 T([["Element", "Direction"], ["Typography", "High-contrast serif wordmark and headings (open-license faces such as Fraunces or Instrument Serif); humanist sans for UI (Inter or Geist)"], ["Palette", "Ink #14171C, Bone #F6F3EE, Deep Moss #1F3D33 (single accent), Brass #B08D57 (highlights), Signal Red for warnings only; all pairings WCAG 2.2 AA"], ["Photography", "Natural light; real clinicians and consenting members; no syringes-as-hero; no before/after; no celebrity imagery without contract"], ["Components", "FDA-status badge; evidence-grade badge; clinician card with license states; all-in pricing table; eligibility stepper; consent modal; adverse-event banner; auto-renewal disclosure block; state-availability selector; cookie/CHD consent manager"], ["Accessibility", "WCAG 2.2 AA; keyboard-operable quiz and checkout; captions; automated plus manual screen-reader testing pre-launch and quarterly"]], widths=[1.3 * inch, CW - 1.3 * inch]),
 H2("Draft homepage copy (requires legal and medical review)"),
 CALLOUT("**Peptide health, done properly.** Independent clinicians decide what's right for you. Licensed US pharmacies fill it. We explain the science in plain language and tell you what we won't sell. [Check eligibility] [Explore the library] — Licensed pharmacies · Independent clinician review · Third-party tested · Transparent, all-in pricing. What we won't do: we do not sell research-use-only peptides, we do not promise results, we do not hide fees or trap you in subscriptions. Prescription products are available only after a consultation with an independent licensed clinician and only where clinically appropriate. Compounded medications are not FDA-approved. Not available in all states."),
 SB()]

# ---------------------------------------------------------------- 18 Sitemap & flows
story += [H1("Sitemap and user flows", "18"),
 MONO("""/                     Homepage                         /learn, /learn/{slug}    Journal
/how-it-works         Rx path vs non-Rx path            /shop, /shop/{slug}      Non-Rx commerce (standard cart)
/programs             Health-goal hub                   /membership              Membership
  /programs/recovery | metabolic | vitality |           /faq  /support  /contact
  performance | sexual-health | skin                    /state-availability      Rx programs by state
/peptides, /peptides/{slug}  Library (FDA status +      /account                 Member dashboard
  evidence grade; 'offered by AminoLord?')                /account/program | subscriptions | labs |
/science              Science & Standards                 orders | privacy
/medical-team         Named clinicians, licensure       /legal/privacy | consumer-health-data | terms |
/pricing              All-in pricing, cancellation        telehealth-consent | shipping-returns |
/eligibility          Consented quiz → intake or educ.    accessibility | notice-of-privacy-practices |
/labs  /safety  /evidence                                  disclosures (material connections)
Rule: Rx programs never expose 'Add to Cart'. Legal pages are published by the correct entity (brand/MSO vs practice vs pharmacy)."""),
 H2("Primary flows"),
 T([["Flow", "Path", "Key controls"],
    ["Visitor → education", "Home → library teaser → ingredient page → related program → eligibility", "Reviewer credentials; educational disclaimer"],
    ["Visitor → eligibility", "Program → quiz intro → CHD consent → goal, state, age, red flags, meds → contact → outcome", "Decline path; disqualification with education; state waitlist"],
    ["Eligibility → intake", "Account (passkey/MFA) → ID verification → state telehealth consent + NPP → history → labs if required → consult-fee authorization", "Versioned consents; PHI in vendor EHR only"],
    ["Approval → payment → fulfillment", "Clinician decision → plan and all-in price → auto-renewal consent → payment → e-Rx → pharmacy → cold-chain ship → onboarding → day-7/30 check-ins", "ROSCA-grade disclosure; pharmacy verification; tracking"],
    ["Non-Rx purchase", "Shop → PDP → cart → Shopify checkout → 3PL", "DSHEA/cosmetic claims only"],
    ["Membership", "Plan → account → auto-renewal consent → payment → dashboard", "Renewal reminders; cancel in ≤2 clicks"],
    ["Labs", "Clinician order → site or kit → results to EHR → clinician review → dashboard notification", "Results never emailed; abnormal-result outreach"],
    ["Refill", "Dashboard → short check-in → clinician approve/adjust/hold → pharmacy", "Refill criteria documented"],
    ["Cancellation", "Subscriptions → pause/change/cancel → confirm → email", "One optional pause offer; clinician notified for Rx"],
    ["Adverse event / urgent", "Any page banner → triage → severe: 911 guidance + on-call; non-severe: clinician within 24h → logged; MedWatch where appropriate", "Pharmacovigilance SOP; pharmacy notified"],
    ["Support", "Chat/email/phone in hours → clinical questions routed to practice (HIPAA channel)", "First response <4h; AE-related <1h"]], widths=[1.3 * inch, 3.6 * inch, CW - 4.9 * inch], font=7.2),
 SB()]

# ---------------------------------------------------------------- 19 Wireframes
story += [H1("Sample wireframes", "19"),
 P("Low-fidelity wireframes for the eight key screens are in 05_AminoLord_Website_Strategy.md section 6. Two are reproduced here."),
 H3("Homepage — desktop (left) and mobile (right)"),
 WIRE([("Desktop 1280", 2.6, [
   (0, 0, 100, 6, ["AminoLord   Programs  Library  Science  Team  Pricing            [Check eligibility]   Account"], "band"),
   (0, 6, 100, 4, ["Serving CA, TX, FL, NY … · non-Rx ships nationwide"], "chip"),
   (0, 11, 58, 24, ["Peptide health, done properly.", "Clinician-led programs, tested products, plain-language science.", "", "Rx products require a clinician consultation; not everyone qualifies."], "box"),
   (2, 25, 20, 6, ["Check eligibility"], "cta"), (24, 25, 22, 6, ["Explore the library"], "cta2"),
   (60, 11, 40, 24, ["[ambient video, muted, captioned]"], "media"),
   (0, 36, 25, 6, ["✓ Licensed US pharmacies"], "chip"), (25, 36, 25, 6, ["✓ Independent clinicians"], "chip"), (50, 36, 25, 6, ["✓ Third-party tested"], "chip"), (75, 36, 25, 6, ["✓ All-in pricing"], "chip"),
   (0, 43, 100, 4, ["Choose your goal"], "box"),
   (0, 47, 16.6, 12, ["Recovery"], "box"), (16.6, 47, 16.6, 12, ["Metabolic"], "box"), (33.2, 47, 16.6, 12, ["Vitality"], "box"), (49.8, 47, 16.6, 12, ["Performance"], "box"), (66.4, 47, 16.6, 12, ["Sexual health"], "box"), (83, 47, 17, 12, ["Skin (non-Rx)"], "box"),
   (0, 60, 100, 6, ["How it works:  1 Learn  →  2 Check eligibility  →  3 Clinician plan"], "band"),
   (0, 67, 100, 8, ["Library:  BPC-157 [Restricted — not offered] · Sermorelin [Compounded]", "Tesamorelin [FDA-approved] · NAD+ [Compounded] · → all entries"], "box"),
   (0, 76, 50, 8, ["Medical team: Dr. X, MD (CA, TX) · Dr. Y, DO (FL)", "Independence statement"], "box"),
   (50, 76, 50, 8, ["What we won't do: RUO · unproven claims", "forced subscriptions · hidden fees"], "warn"),
   (0, 85, 100, 6, ["Learn: three latest articles (medically reviewed)"], "box"),
   (0, 92, 100, 8, ["Footer: Legal · Consumer Health Data · Accessibility · Disclosures · Rx disclaimer · 911 notice"], "band")]),
  ("Mobile 390", 1, [
   (0, 0, 100, 6, ["☰  AminoLord     Acct"], "band"), (0, 6, 100, 4, ["Serving 12 states"], "chip"),
   (0, 11, 100, 16, ["Peptide health,", "done properly."], "box"), (0, 27, 100, 10, ["[video]"], "media"),
   (5, 38, 90, 6, ["Check eligibility"], "cta"), (5, 45, 90, 6, ["Explore the library"], "cta2"),
   (0, 52, 50, 6, ["✓ Pharmacies"], "chip"), (50, 52, 50, 6, ["✓ Clinicians"], "chip"), (0, 58, 50, 6, ["✓ Tested"], "chip"), (50, 58, 50, 6, ["✓ Pricing"], "chip"),
   (0, 65, 100, 4, ["Choose your goal"], "box"), (0, 69, 45, 9, ["Recovery"], "box"), (47, 69, 45, 9, ["Metabolic ▶"], "box"),
   (0, 79, 100, 6, ["1 Learn → 2 Check → 3 Plan"], "band"), (0, 86, 100, 6, ["Library chips · Medical team"], "box"),
   (0, 93, 100, 7, ["Sticky: Check eligibility"], "cta")])], height=3.4 * inch),
 H3("Program page, eligibility flow, checkout and dashboard"),
 WIRE([("Program page", 1.3, [
   (0, 0, 100, 4, ["Programs › Recovery"], "band"),
   (0, 5, 70, 12, ["Recovery & tissue support", "Who it's for / who it's not for"], "box"), (72, 5, 28, 6, ["Evidence: B"], "chip"),
   (0, 18, 34, 6, ["Check eligibility"], "cta"), (36, 18, 34, 6, ["Read the science"], "cta2"),
   (0, 26, 100, 9, ["What's included: consult · clinician plan", "Rx if appropriate · monitoring · support · shipping"], "box"),
   (0, 36, 100, 4, ["Candidate ingredients"], "box"),
   (0, 40, 100, 7, ["Tesamorelin   [FDA-approved]   [Evidence B]"], "box"), (0, 47, 100, 7, ["Sermorelin    [Compounded]     [Evidence C]"], "box"), (0, 54, 100, 7, ["BPC-157   [FDA-restricted — not offered]"], "warn"),
   (0, 63, 100, 10, ["All-in pricing table  ($/mo · included · excluded)"], "band"),
   (0, 74, 100, 8, ["Safety & side effects · Labs required", "Clinician quote (named)"], "box"),
   (0, 83, 100, 6, ["FAQ"], "box"), (0, 90, 100, 5, ["Medical emergency? Call 911"], "warn"), (0, 95, 100, 5, ["Check eligibility"], "cta")]),
  ("Eligibility quiz (one question per screen)", 1.3, [
   (0, 0, 100, 4, ["Step 1 of 8   ■■□□□□□□"], "band"),
   (0, 6, 100, 8, ["Privacy: health questions route you safely.", "[Consumer-health-data notice]  ☐ I consent"], "chip"),
   (0, 16, 100, 8, ["What's your main goal?"], "box"),
   (0, 25, 48, 7, ["○ Recovery"], "box"), (52, 25, 48, 7, ["○ Metabolic health"], "box"), (0, 33, 48, 7, ["○ Vitality"], "box"), (52, 33, 48, 7, ["○ Performance"], "box"),
   (0, 43, 100, 6, ["Continue"], "cta"),
   (0, 52, 100, 12, ["Later steps: State → Age → Red flags →", "Conditions → Medications → Contact", "(SMS opt-in separate)"], "box"),
   (0, 66, 100, 12, ["Outcome A: proceed to clinician review", "[Continue to intake]"], "chip"),
   (0, 80, 100, 14, ["Outcome B: not a fit right now", "Reasons · education · non-Rx options", "Not a diagnosis; a clinician decides"], "warn")]),
  ("Checkout (Rx) and member dashboard", 1.3, [
   (0, 0, 100, 4, ["1 Plan  ›  2 Pricing & consent  ›  3 Payment"], "band"),
   (0, 5, 100, 10, ["Order: Recovery program  $X/mo all-in", "Next charge date · Cancel in account (2 clicks)"], "box"),
   (0, 16, 100, 7, ["☐ I agree to the auto-renewal terms above"], "chip"),
   (0, 24, 100, 6, ["Confirm & pay"], "cta"), (0, 31, 100, 4, ["Secure · PCI · no insurance billed"], "box"),
   (0, 40, 100, 4, ["Dashboard"], "band"),
   (0, 45, 48, 11, ["Program: Active", "Next check-in: day 30"], "box"), (52, 45, 48, 11, ["Next refill: Oct 3", "[Request now]"], "box"),
   (0, 57, 48, 11, ["Messages (care team)", "1 new"], "box"), (52, 57, 48, 11, ["Labs", "Results ready · [View]"], "box"),
   (0, 69, 48, 11, ["Subscriptions", "Manage · Pause · Cancel"], "box"), (52, 69, 48, 11, ["Report a side effect", "24/7"], "warn"),
   (0, 81, 48, 11, ["Learn", "Recommended for you"], "box"), (52, 81, 48, 11, ["Privacy & data", "Download · Delete"], "box")])], height=3.6 * inch),
 SB()]

# ---------------------------------------------------------------- 20 Technology and operations
story += [H1("Technology and operations", "20"),
 T([["Criterion", "A. Shopify + external clinical workflow", "B. Headless commerce + integrated telehealth", "C. Custom member portal over proven clinical infrastructure (recommended)"],
    ["Time to market", "8–12 weeks", "16–24 weeks", "12–18 weeks"],
    ["Build cost [FA]", "$60–120k", "$250–500k", "$150–300k"],
    ["Flexibility", "Low (vendor UX owns Rx journey)", "High", "High where it matters"],
    ["HIPAA / CHD", "PHI with vendor; Shopify not for health inputs", "Own HIPAA-eligible infra", "PHI in vendor EHR + HIPAA-eligible warehouse; minimal consented CHD on brand site"],
    ["Pharmacy / labs / identity", "Via vendor", "Direct APIs", "Vendor e-Rx network + pharmacy status API; lab vendor; ID vendor"],
    ["Subscriptions and payments", "Shopify (non-Rx)", "Custom", "Shopify (non-Rx) + Stripe Billing (programs, membership); high-risk backup processor"],
    ["Analytics and consent", "Vendor", "Own", "Server-side events with health-data filtering; versioned consent log"],
    ["Maintenance", "Low", "High", "Medium"],
    ["Risk", "Brand break at handoff; weak differentiation", "Highest cost; full regulatory surface owned", "Vendor dependence for clinical core (acceptable, auditable)"]], widths=[1.2 * inch] + [(CW - 1.2 * inch) / 3] * 3, font=7.2),
 H2("Recommended stack and build/license/integrate split"),
 *BUL(["**Build:** Next.js marketing site, library, program pages, quiz UI, member dashboard; consent-logging service; analytics pipeline with consumer-health-data filtering.", "**License:** CMS with medical-review workflow (Sanity/Contentful); Shopify for non-Rx; Stripe Billing; identity verification (Persona/Veriff/Stripe Identity); telehealth/EHR/e-Rx and provider network (candidates to diligence: OpenLoop, Wheel, SteadyMD, Healthie with DoseSpot/Surescripts); lab integration vendor; consent-management platform; Klaviyo, Twilio (TCPA consent), HIPAA-eligible messaging; Zendesk.", "**Integrate:** 503A/503B pharmacies with status webhooks and cold-chain carriers; Quest/Labcorp via lab vendor; LegitScript certification; SOC 2 vendors with BAAs.", "**Operations:** pharmacy quality agreements and recall SOP; adverse-event and pharmacovigilance SOP; cold-chain exceptions tracking; certificates of analysis for non-Rx products; cybersecurity program (pen test, incident response, cyber insurance)."]),
 SRC("05_AminoLord_Website_Strategy.md section 8 [SR]; vendor pricing benchmarks in research/06 (recalled/unverified)."),
 SB()]

# ---------------------------------------------------------------- 21 Clinical and pharmacy partner model
story += [H1("Clinical and pharmacy partner model", "21"),
 P("AminoLord (brand and management-services organization) does not practice medicine or dispense drugs. It contracts with an affiliated professional entity that employs or contracts licensed clinicians, and with licensed pharmacies that dispense on valid patient-specific prescriptions. Counsel must confirm the structure state by state; the diagram below is the working hypothesis."),
 MONO("""  Member ──► AminoLord.com (brand/MSO: marketing, technology, non-clinical support, billing services)
                │ management-services agreement (fair-market-value fee; no control of clinical judgment)
                ▼
      Affiliated professional entity (physician-owned where required) ── licensed clinicians in member's state
                │ patient-specific prescription (e-Rx)                         │ orders labs
                ▼                                                              ▼
      Licensed 503A pharmacies (patient-specific) / 503B outsourcing facility ── Lab partner (Quest/Labcorp via vendor)
                │ verified, compounded, cold-chain shipped, status webhooks
                ▼
      Member (onboarding, monitoring, refills, adverse-event reporting; MedWatch where appropriate)"""),
 H2("Partner due-diligence framework"),
 T([["Partner", "Diligence items", "Contract controls"],
    ["Medical entity and clinicians", "Ownership structure vs CPOM; licenses in each state; board status; malpractice; disciplinary history; telehealth-modality competence", "Independence; credentialing; no volume incentives; documentation standards"],
    ["Telehealth / EHR vendor", "HIPAA program, BAA, SOC 2; e-Rx network; state coverage; async/video support; ID verification; uptime", "SLAs; data ownership; exit and portability"],
    ["503A pharmacies", "State licensure incl. non-resident; FDA 483/warning-letter history (see Empower, ReviveRx, Boothwyn, ProRx cases); USP 795/797/800; PCAB; testing (sterility, potency, endotoxin); bulks-list compliance", "Quality agreement; COA access; recall procedure; adverse-event reporting; audit rights"],
    ["503B outsourcing facility", "FDA registration; cGMP inspection history; product list; capacity", "As above plus supply continuity"],
    ["Testing laboratories and lab partners", "CLIA/CAP; draw network; turnaround; result integration", "Result handling; abnormal-result escalation"],
    ["Fulfillment / cold chain", "Validated packaging; temperature monitoring; carrier performance", "Exception handling; replacement policy"],
    ["Customer support", "HIPAA training; escalation paths", "SLAs; QA sampling"],
    ["Insurance", "Professional (entity and clinicians), product, cyber, D&O, general", "Certificates; additional-insured status"]], widths=[1.4 * inch, 3.2 * inch, CW - 4.6 * inch], font=7.2),
 P("No specific supplier is recommended in this document; the pharmacies with clean enforcement records identified in the audit (Belmar, Wells, Olympia, Red Rock) are starting points for diligence, not selections."),
 SRC("research/02_pharmacy_ruo_consumer.md (enforcement records: FDA pages where surfaced, otherwise third-party); research/05 [analyst inference pending counsel]."),
 SB()]

# ---------------------------------------------------------------- 22 Compliance framework
hi = [i for i in comp if i["risk_level"] == "High"]
story += [H1("Compliance framework", "22"),
 P("The preliminary matrix covers 36 issues (23 High, 11 Medium, 2 Low). The full matrix with owners, professional review, pre-launch actions, ongoing controls and sources is in 08_AminoLord_Evidence_Ledger.xlsx (Compliance Matrix) and research/05_regulatory_brief.md. It is research, not legal advice; every item requires review by qualified counsel."),
 IMG(C + "risk.png", width=4.2 * inch, maxh=2.0 * inch), SRC("research/05_compliance_matrix.json; preliminary risk = enforcement likelihood × severity for a well-run brand (analyst inference)."),
 H2("High-risk issues and pre-launch actions"),
 T([["Issue", "Why it matters", "Pre-launch action"]] + [[i["issue"], i["why_it_matters"][:260] + ("…" if len(i["why_it_matters"]) > 260 else ""), i["pre_launch_action"][:230] + ("…" if len(i["pre_launch_action"]) > 230 else "")] for i in hi], widths=[1.6 * inch, 2.8 * inch, CW - 4.4 * inch], font=6.8),
 H2("Medium and low issues (summary)"),
 P("; ".join(i["issue"] for i in comp if i["risk_level"] != "High") + "."),
 SRC("research/05_regulatory_brief.md sources table (79 rows): FDA, FTC, court and statute references where surfaced (Verified fact); law-firm and trade-press alerts (Third-party report); background items flagged Analyst inference for counsel verification."),
 SB()]

# ---------------------------------------------------------------- 23 Launch strategy
story += [H1("Launch strategy", "23"),
 IMG(C + "gantt.png", maxh=2.5 * inch), SRC("06_AminoLord_Launch_Plan.md; timing per Base scenario [FA]."),
 T([["Phase", "Objectives", "Exit criteria", "Budget [FA]", "KPIs"],
    ["0 Foundation & compliance (M0–3)", "Structure, principals and rights, counsel memos, partners, standards, brand and prototype, analytics, pilot states, advisors", "Counsel sign-off; signed clinical and pharmacy agreements; insurance; pilot states", "$350–700k", "Checklist items 1–10; prototype SUS ≥80"],
    ["1 Internal pilot (M3–4)", "Test positioning, flows, pricing, support, clinical handoffs", "Pricing v1; P0/P1 issues closed; compliance spot-check", "$80–150k", "Task success ≥90%; intake→decision ≤48h"],
    ["2 Private beta (M4–6)", "150–300 invited members in 2–3 states; safety, retention, fulfillment", "≥200 served; unit economics within 20% of model; AE process validated", "$150–300k", "Month-2 retention ≥75%; fulfillment ≤5 days; refunds <5%"],
    ["3 Waitlist & early access (M5–7)", "Owned audience; authority content; podcasts; referral mechanics", "Waitlist ≥15k; library live; nurture performing", "$200–400k", "Email open ≥45%; organic library sessions ≥25k/mo"],
    ["4 Public launch (M7–8)", "Coordinated multi-channel launch; celebrity audience only if contracted; crisis coverage", "Stable operations 4 weeks; CAC and retention within bands; no open P0", "$400–900k (month)", "≥1,000 enrollments in 30 days (base); CAC ≤$350; AE response <1h"],
    ["5 Expansion (M9–24)", "States in tranches; programs by evidence; retention and referral; partnerships with guardrails", "Sustainable contribution margin; repeatable state playbook", "$150–400k/mo", "20+ states by M18; LTV:CAC ≥3; NPS ≥50; 0 compliance incidents"]], widths=[1.25 * inch, 1.9 * inch, 1.5 * inch, 0.8 * inch, CW - 5.45 * inch], font=6.9),
 H2("Roadmap"),
 T([["30 days", "60 days", "90 days", "6 months", "12 months"], ["Counsel engaged; structure memo; principal verification; trademark clearance; vendor RFPs; brand direction; Scenario A/B framework", "Term sheets or documented no-go; formulary v1; telehealth vendor selected; pharmacies in diligence; prototype + 20 library entries; analytics/consent live", "Entities formed; agreements signed; LegitScript application; pilot states; internal pilot; pricing research fielded", "Private beta complete; waitlist ≥15k; 40+ library entries; podcast placements; go/no-go for launch", "Public launch done; 10–15 states; 3–4 programs; membership live; ~1,700 active Rx members (base); first Standards Report"]], widths=[CW / 5] * 5, font=7.0),
 SB()]

# ---------------------------------------------------------------- 24 Channel plan
story += [H1("Channel plan", "24"),
 P("Channels are structured as owned (website, email, library, community), rented (social, search, media platforms) and borrowed (podcasts, clinicians, creators, partners, press). Every rented or borrowed impression is routed into an owned asset. Prescription volume is never a growth KPI."),
 T([["Channel", "Phase 0–1", "Phase 2–3", "Phase 4", "Phase 5"],
    ["Website / library (owned)", "Prototype; 20 entries", "40+ entries; articles", "GA", "State pages; continuous"],
    ["Email / SMS (owned)", "Consent flows", "Waitlist nurture", "Launch waves", "Lifecycle, retention"],
    ["Founder / clinician video (owned)", "Scripts; medical review", "Series 1", "Launch content", "Ongoing"],
    ["Podcasts (borrowed)", "Target list", "5+ placements", "Tour", "Recurring"],
    ["Creators (borrowed/rented)", "Contracts; disclosure kit", "Disclosed seeding", "Wave", "Ambassadors (disclosed)"],
    ["PR (borrowed)", "Backgrounder", "Standards narrative", "Exclusives", "Quarterly reports"],
    ["Paid social (rented)", "—", "Waitlist ads (non-health events)", "Scale with guardrails", "Efficiency"],
    ["Paid search (rented)", "LegitScript prep", "—", "Brand + category (certified)", "Scale"],
    ["Practitioner referrals (borrowed)", "Advisory clinicians", "Pilot referrals", "—", "Program (no per-Rx fees)"],
    ["Partnerships (borrowed)", "—", "—", "—", "Gyms, clinics, corporate education/testing"]], widths=[1.6 * inch] + [(CW - 1.6 * inch) / 4] * 4, font=7.2),
 H2("Measurement framework (base-case month-12 targets [FA])"),
 T([["Metric", "Target", "Metric", "Target"], ["Qualified traffic", "120k sessions/mo", "Gross margin", "55–65%"], ["Waitlist conversion (pre-launch)", "6–10%", "Refund rate", "<4%"], ["Quiz start / completion", "8% / 65%", "Monthly churn (blended Rx)", "8–12%"], ["Consultation completion (show rate)", "≥80%", "LTV : CAC", "≥3.0"], ["Medical eligibility rate", "50–70% (monitored, not targeted)", "CAC payback", "≤6 months"], ["Enrollment conversion (eligible → paid)", "≥45%", "Referral share of new members", "≥12%"], ["Blended CAC", "≤$300", "NPS", "≥50"], ["AOV / program value", "$250–350", "Support first response", "<4h (AE <1h)"], ["Fulfillment time (median)", "≤5 days", "Compliance incidents", "0"]], widths=[2.0 * inch, 1.5 * inch, 2.0 * inch, CW - 5.5 * inch], font=7.2),
 SRC("06_AminoLord_Launch_Plan.md sections 4–5 [SR/FA]."),
 SB()]

# ---------------------------------------------------------------- 25 Financial model
m12 = lambda s, k: mv["monthly"][s][k][11]
story += [H1("Financial model", "25"),
 P("The model (07_AminoLord_Financial_Model.xlsx) is driver-based and editable: 68 labeled assumptions in three scenario columns feed three 36-month model sheets, a scenario summary, sensitivity grids, hypothetical celebrity-economics structures and an assumptions register with rationale, source, confidence, sensitivity and validation method. Every output is a formula; no result is hard-coded. Nothing here is a forecast of results."),
 IMG(C + "scen.png"), SRC("07_AminoLord_Financial_Model.xlsx, Model_* sheets. Financial assumptions [FA]; benchmark-informed inputs are labeled recalled/unverified in the assumptions register."),
 T([["Output", "Conservative", "Base", "Upside"],
    ["Year 1 / 2 / 3 net revenue", f"{Y('Conservative',1)} / {Y('Conservative',2)} / {Y('Conservative',3)}", f"{Y('Base',1)} / {Y('Base',2)} / {Y('Base',3)}", f"{Y('Upside',1)} / {Y('Upside',2)} / {Y('Upside',3)}"],
    ["Year 3 gross margin", f"{sv('Year 3 gross margin %','Conservative')*100:.0f}%", f"{sv('Year 3 gross margin %','Base')*100:.0f}%", f"{sv('Year 3 gross margin %','Upside')*100:.0f}%"],
    ["Year 1 / 2 / 3 EBITDA", f"{money(sv('Year 1 EBITDA','Conservative'))} / {money(sv('Year 2 EBITDA','Conservative'))} / {money(sv('Year 3 EBITDA','Conservative'))}", f"{money(sv('Year 1 EBITDA','Base'))} / {money(sv('Year 2 EBITDA','Base'))} / {money(sv('Year 3 EBITDA','Base'))}", f"{money(sv('Year 1 EBITDA','Upside'))} / {money(sv('Year 2 EBITDA','Upside'))} / {money(sv('Year 3 EBITDA','Upside'))}"],
    ["Active Rx members, month 12 / 24 / 36", f"{num(sv('Active Rx members, month 12','Conservative'))} / {num(sv('Active Rx members, month 24','Conservative'))} / {num(sv('Active Rx members, month 36','Conservative'))}", f"{num(sv('Active Rx members, month 12','Base'))} / {num(sv('Active Rx members, month 24','Base'))} / {num(sv('Active Rx members, month 36','Base'))}", f"{num(sv('Active Rx members, month 12','Upside'))} / {num(sv('Active Rx members, month 24','Upside'))} / {num(sv('Active Rx members, month 36','Upside'))}"],
    ["CAC per Rx member, month 24", money(sv('CAC per Rx member, month 24','Conservative')), money(sv('CAC per Rx member, month 24','Base')), money(sv('CAC per Rx member, month 24','Upside'))],
    ["Contribution per Rx member-month / LTV", f"${sv('Contribution per Rx member-month','Conservative'):.0f} / {money(sv('LTV (contribution-based)','Conservative'))}", f"${sv('Contribution per Rx member-month','Base'):.0f} / {money(sv('LTV (contribution-based)','Base'))}", f"${sv('Contribution per Rx member-month','Upside'):.0f} / {money(sv('LTV (contribution-based)','Upside'))}"],
    ["LTV : CAC, month 24 / payback (months)", f"{sv('LTV : CAC, month 24','Conservative'):.1f}x / {sv('CAC payback, month 24 (months)','Conservative'):.1f}", f"{sv('LTV : CAC, month 24','Base'):.1f}x / {sv('CAC payback, month 24 (months)','Base'):.1f}", f"{sv('LTV : CAC, month 24','Upside'):.1f}x / {sv('CAC payback, month 24 (months)','Upside'):.1f}"],
    ["Break-even month (EBITDA)", BE_s("Conservative"), BE_s("Base"), BE_s("Upside")],
    ["Peak cumulative burn", money(sv('Peak cumulative cash burn','Conservative')), money(sv('Peak cumulative cash burn','Base')), money(sv('Peak cumulative cash burn','Upside'))],
    ["Capital required (+15% contingency)", CAP("Conservative"), CAP("Base"), CAP("Upside")],
    ["Brand-partner cash + royalty, 36 months (Scenario A)", money(sv('Brand partner cash + royalty paid, 36 months','Conservative')), money(sv('Brand partner cash + royalty paid, 36 months','Base')), money(sv('Brand partner cash + royalty paid, 36 months','Upside'))]], widths=[2.2 * inch] + [(CW - 2.2 * inch) / 3] * 3, align_right_cols=(1, 2, 3)),
 SRC("07_AminoLord_Financial_Model.xlsx (Scenario Summary), recalculated 2026-09-02. Prescribing rate is a clinical outcome monitored for safety, not a target."),
 H2("Revenue and cost architecture"),
 *BUL(["**Revenue drivers:** paid and organic sessions → quiz starts → completions → eligible outcomes (screen and state coverage) → intakes (consult fee) → consults → prescriptions (clinician decision) → paying program members; plus membership sign-ups, lab orders and non-Rx orders with repeat purchases; monthly churn on programs and membership; state coverage rising from 40% to a cap.", "**Costs:** pharmacy/medication per member-month, clinician cost per consult and per member-month monitoring, labs, cold-chain fulfillment, payment fees, refunds, variable support, non-Rx COGS; operating expenses by phase for team, medical leadership, technology, build, legal and compliance, insurance, creative; acquisition (paid, influencer, launch PR) and brand-partner cash and royalty (Scenario A toggle).", "**Working capital:** non-Rx inventory only; prescription products are dispensed by pharmacies."]),
 SB()]

# ---------------------------------------------------------------- 26 Scenario and sensitivity
story += [H1("Scenario and sensitivity analysis", "26"),
 IMG(C + "funnel.png", maxh=2.6 * inch), SRC("Model_Base, month 24. Each stage is a labeled assumption; the prescribing stage is a clinical decision."),
 IMG(C + "ltv.png", maxh=2.5 * inch), SRC("07_AminoLord_Financial_Model.xlsx (Sensitivity). Contribution = program price net of refunds and fees minus pharmacy, monitoring, shipping and support per member-month."),
 H2("What matters most"),
 T([["Driver", "Why it dominates", "Validation before launch"], ["Monthly churn on programs", "LTV is contribution ÷ churn; moving churn from 11% to 14% cuts LTV by about a fifth", "Beta cohort retention; onboarding and check-in cadence"], ["Cost per paid session and funnel rates", "CAC per Rx member scales inversely with the product of seven funnel rates", "Waitlist and beta analytics; landing-page tests"], ["State coverage", "Eligible outcomes scale linearly with covered population", "Counsel state map; pharmacy licensure"], ["Program price and pharmacy cost", "Together set contribution per member-month", "Pricing research; signed pharmacy contracts"], ["Celebrity uplift and cost", "Scenario A adds retainer and royalty; uplift on organic traffic is unproven", "Brand-lift study in Phase 3; toggle Scenario B in the model"]], widths=[1.6 * inch, 3.0 * inch, CW - 4.6 * inch], font=7.3),
 P("The conservative case is deliberately severe: it assumes weaker funnel rates, higher churn and cost, and that the team and marketing plan continue without cuts. It does not reach break-even within 36 months and requires the most capital; a real operator would re-plan at the Phase 2 exit gate if beta economics track the conservative case."),
 SB()]

# ---------------------------------------------------------------- 27 Funding
story += [H1("Funding and resource requirements", "27"),
 T([["Bucket (months 0–12) [FA]", "Conservative", "Base", "Upside"], ["Legal, regulatory, insurance", "$250k", "$350k", "$450k"], ["Product, engineering, design", "$350k", "$550k", "$800k"], ["Clinical leadership and governance", "$150k", "$250k", "$350k"], ["Content, brand, production", "$200k", "$350k", "$600k"], ["Paid acquisition and creators", "$400k", "$1.0M", "$2.0M"], ["Team and operations", "$700k", "$1.1M", "$1.6M"], ["Principal compensation (cash portion; Scenario A)", "$0 (Scenario B)", "$300k", "$750k"], ["Working capital and contingency", "$250k", "$400k", "$600k"], ["**Year-1 requirement (plan view)**", "**~$2.3M**", "**~$4.3M**", "**~$7.2M**"], ["**Capital required to peak burn + 15% (model view)**", f"**{CAP('Conservative')}**", f"**{CAP('Base')}**", f"**{CAP('Upside')}**"]], widths=[2.6 * inch] + [(CW - 2.6 * inch) / 3] * 3, align_right_cols=(1, 2, 3)),
 SRC("06_AminoLord_Launch_Plan.md section 7 (plan view) and 07_AminoLord_Financial_Model.xlsx (model view). The two views differ by design: the plan view is a year-1 budget; the model view is cumulative burn to break-even including years 2–3 where applicable."),
 H2("Team, partners and approvals"),
 T([["Team by launch", "Partners", "Approvals and certifications"], ["CEO/GM; Medical Director (proposed Dr. Azziz, subject to verification); Compliance & Regulatory Lead; Head of Product & Design; 2–3 engineers; Head of Growth; Content Lead + 2 medical writers; Head of Support; Pharmacy & Ops Lead; fractional CFO; brand partner (proposed Scott Disick, subject to agreement); PR and production agencies", "Telehealth/EHR/e-Rx vendor; affiliated professional entity; 2 licensed pharmacies (503A) and 1 503B relationship; lab partner; ID verification; payments (primary + high-risk backup); CMP; 3PL; insurance broker", "Counsel opinions (CPOM, fee-splitting, telehealth, pharmacy, privacy, advertising); LegitScript certification; state pharmacy and clinician licensure verification; insurance binding; medical director and compliance sign-off; trademark filing"]], widths=[CW / 3] * 3, font=7.3),
 H2("Hypothetical brand-partner structures (no terms offered)"),
 T([["Structure", "Shape", "Trade-off"], ["1 Cash retainer only", "Fixed annual fee", "Front-loads risk before demand is proven"], ["2 Equity only", "Fully diluted stake with vesting", "Aligned; dilutive; no cash cost"], ["3 Royalty only", "% of net revenue", "Scales with success; margin drag"], ["4 Mixed (recommended starting point)", "Modest retainer + capped royalty + vesting equity tied to deliverables", "Balances incentives and cash"], ["5 Performance royalty", "Royalty above a revenue hurdle", "Pays only for outperformance"]], widths=[1.8 * inch, 3.0 * inch, CW - 4.8 * inch], font=7.3),
 SRC("07_AminoLord_Financial_Model.xlsx (Celebrity Economics); licensing benchmarks recalled/unverified."),
 SB()]

# ---------------------------------------------------------------- 28 Milestones
story += [H1("Milestones", "28"),
 T([["Month", "Milestone", "Owner", "Gate"], ["1", "Counsel engaged; principal verification complete; trademark clearance filed; vendor RFPs", "GM; counsel", "—"], ["2", "Term sheets or Scenario B decision; formulary v1; telehealth vendor selected", "GM; Medical Director", "Founder decision"], ["3", "Entities formed; pharmacy agreements; prototype and 20 library entries; analytics/consent stack", "GM; Product; Compliance", "Phase 0 exit"], ["4", "Internal pilot; pricing research fielded; accessibility and security audits", "Product; Medical Director", "Phase 1 exit"], ["5–6", "Private beta in 2–3 states; ≥200 members; AE drill; LegitScript application", "GM; Support; Ops", "Phase 2 exit"], ["6–7", "Waitlist ≥15k; 40+ library entries; podcast placements; creator contracts", "Growth; Content; PR", "Phase 3 exit"], ["8", "Public launch (4–6 states)", "All", "Go/No-Go complete"], ["12", "10–15 states; membership live; first Standards Report; base ~1,700 active Rx members", "GM; Ops", "Board review"], ["18", "20+ states; LTV:CAC ≥3; repeatable state playbook; Series A readiness (if venture path)", "GM; Finance", "Board review"], ["24", "Positive monthly EBITDA sustained (base from month 18); 3–4 programs; corporate education pilots", "GM", "—"]], widths=[0.6 * inch, 3.6 * inch, 1.5 * inch, CW - 5.7 * inch], font=7.3),
 SB()]

# ---------------------------------------------------------------- 29 Risks
story += [H1("Principal risks and mitigations", "29"),
 T([["Risk", "Likelihood / impact", "Mitigation"],
    ["FDA reverses or narrows the 2026 peptide reclassification; final rule excludes key substances", "Medium / High", "Formulary keyed to current status with change control; launch on sermorelin, NAD+, approved drugs; library, membership and non-Rx do not depend on restricted peptides"],
    ["FTC or state action on subscriptions, testimonials, endorsements or health-data sharing", "Medium / High", "ROSCA-grade flows; verified reviews only; disclosure program; no health data to ad platforms; compliance lead sign-off on all creative"],
    ["State CPOM, fee-splitting, telehealth-modality or pharmacy-licensure barriers slow expansion", "High / Medium", "State readiness checklist; tranche expansion; counsel map; async-friendly states first"],
    ["Ad platforms or payment processors restrict the account", "Medium / High", "LegitScript certification; creative-led broad targeting; education funnels; backup high-risk processor; reserves budgeted"],
    ["Retention below plan (month-1 <85%; churn >12%)", "Medium / High", "Onboarding cadence; clinician check-ins; labs cadence; pause option; membership layer"],
    ["Principal controversy or exit (Scenario A)", "Medium / High", "Morality, exclusivity, termination and post-termination terms; Scenario B parallel; clinicians as durable face"],
    ["Pharmacy quality event or recall", "Low-Medium / High", "Diligence on enforcement history; quality agreements; two pharmacies; recall SOP; member communications plan"],
    ["Adverse event with public attention", "Low / High", "Pharmacovigilance SOP; 24/7 escalation; medical spokesperson; transparent reporting"],
    ["Clinical capacity shortfall at launch", "Medium / Medium", "50% capacity buffer; wave-based waitlist release"],
    ["Trademark conflict on AMINO-formative marks", "Medium / Medium", "Clearance search in Classes 5, 35, 44, 25 before spend; fallback naming"],
    ["Conservative case realized without re-planning", "Medium / High", "Phase 2 exit gate with unit-economics thresholds; spend discipline tied to payback"]], widths=[2.3 * inch, 1.0 * inch, CW - 3.3 * inch], font=7.3),
 SRC("research/05_regulatory_brief.md; research/03; financial model; analyst inference."),
 SB()]

# ---------------------------------------------------------------- 30 Go/no-go
story += [H1("Go/no-go requirements", "30"),
 P("No customer is accepted until every item is complete and signed off in writing by the Medical Director, the Compliance Lead and the GM."),
 T([["#", "Requirement"]] + [[str(i + 1), t] for i, t in enumerate([
  "Corporate structure executed; counsel opinion on CPOM and fee-splitting for each pilot state",
  "Affiliated professional entity formed; medical director appointed with verified licenses, board status and malpractice coverage",
  "Formulary approved: every ingredient classified (approved / compounded-permissible / excluded); restricted bulk substances excluded from compounded offerings",
  "Pharmacy partners licensed in each pilot state (verified with boards); 503A/503B roles defined; quality agreements and recall procedures signed",
  "Telehealth vendor, EHR, e-Rx and identity verification live; state-specific consents versioned and logged",
  "Privacy program: HIPAA policies and BAAs; consumer-health-data policy; consent manager configured; DSAR process tested",
  "Claims review of all site copy, ads and creator scripts against FTC Health Products Guidance and Endorsement Guides; disclosures live",
  "Auto-renewal compliance: pre-checkout disclosure, affirmative consent, easy cancellation, renewal reminders per state law",
  "Payments: processor approval in writing for the business model; backup processor; chargeback plan",
  "Insurance bound: professional (practice and clinicians), product, cyber, D&O, general",
  "Adverse-event and pharmacovigilance SOP tested; 24/7 clinical escalation staffed",
  "Accessibility audit passed (WCAG 2.2 AA); penetration test passed; incident-response plan approved",
  "Support staffed to SLA; refund and return policies published",
  "Trademark application filed with clearance memo; domain and social handles secured",
  "Principals: identity and credentials verified; agreements signed with NIL, morality, exclusivity, FTC disclosure, termination and post-termination terms — or Scenario B activated and all principal references removed",
  "LegitScript certification granted, or paid search deferred",
  "Written sign-offs: Medical Director, Compliance Lead, GM"])], widths=[0.4 * inch, CW - 0.4 * inch], font=7.6),
 SB()]

# ---------------------------------------------------------------- 31 Next steps
story += [H1("Recommended next steps", "31"),
 T([["Priority", "Action", "Owner", "Timing", "Why it is first"],
    ["1", "Verify the principals: obtain the intended physician's legal name, NPI and license state and run board, ABIM and NPI checks; identify Scott Disick's representatives, the reported GLP-1 promotional post and any category exclusivity; obtain term-sheet interest or activate Scenario B", "Founder; counsel", "Weeks 1–4", "Everything downstream (brand, comp, disclosures) depends on it"],
    ["2", "Engage healthcare regulatory counsel for the structure memo (MSO + affiliated practice), state map, formulary policy keyed to FDA 503A status, and advertising review process", "GM; counsel", "Weeks 1–6", "Determines what can be sold, where, and how revenue flows"],
    ["3", "Trademark clearance and filing for AMINOLORD (Classes 5, 35, 44, 25); confirm domain registrar account; secure social handles", "GM; IP counsel", "Weeks 1–3", "AMINO-formative marks are crowded; a conflict later is expensive"],
    ["4", "Issue RFPs: telehealth/EHR/e-Rx vendor; two 503A pharmacies and one 503B; lab partner; identity verification; payments (primary and high-risk backup); begin LegitScript preparation", "Product; Ops; Finance", "Weeks 2–8", "Longest lead times; gate Phase 2"],
    ["5", "Fund Phase 0 and start: brand identity, prototype with 20 library entries and eligibility quiz, analytics and consent stack, advisory group, and the pricing research plan", "GM; Product; Growth", "Weeks 2–12", "Builds the owned assets that every later phase compounds on"]], widths=[0.55 * inch, 3.0 * inch, 1.0 * inch, 0.8 * inch, CW - 5.35 * inch], font=7.3),
 H2("Decisions requiring founder approval"),
 *BUL(["Scenario A versus B, and the negotiating envelope for principal compensation (cash, equity, royalty, mixed).", "Positioning territory (A recommended) and the fallback if pricing research or counsel constrains the formulary.", "Pilot states and the state-expansion sequence.", "Capitalization target: base-case capital requirement versus conservative-case cover.", "Whether to pursue the membership layer at launch or after beta.", "Approval of the verification backlog and budget to re-run the blocked research items before any external use of this document."]),
 SB()]

# ---------------------------------------------------------------- 32 Sources & appendices
led = json.load(open("research/04_principal_verification.json"))["evidence"]
story += [H1("Sources and appendices", "32"),
 P("The complete evidence register (790 entries with URLs, access dates and labels) is in 08_AminoLord_Evidence_Ledger.xlsx. Selected primary and high-value sources are listed below; entries marked (snippet) were seen only as search-result excerpts of the cited page."),
 H2("Appendix A — Selected sources"),
 T([["Topic", "Source", "Label"],
    ["FDA 503A bulks-list update removing peptides from Category 2 (Apr 15, 2026); PCAC Jul 23–24, 2026 recommendations", "AJMC; STAT (2026-07-23); Pharmacy Times; Newtropin; DJ Holt Law", "Third-party reports"],
    ["FDA PCAC briefing citing online BPC-157 availability", "fda.gov/media/193343/download", "Verified fact (surfaced)"],
    ["FDA RUO warning letters (Mar 31, 2026; Gram Peptides; Wholesale Peptide Jun 17, 2026)", "fda.gov warning-letter pages; Health Law Alliance", "Verified / third-party"],
    ["Compounded GLP-1 enforcement (Sept 2025; Mar and Jun 2026); Apr 30, 2026 503B proposal", "Venable; Sheppard Mullin; Orrick; Pharmacy Times", "Third-party reports"],
    ["Pharmacy warning letters (Empower 2025; ReviveRx 2025-09-22; Boothwyn 2026-01-16; ProRx 2025-03-04; Tailor Made 2020)", "fda.gov warning-letter database entries as surfaced", "Verified fact (surfaced)"],
    ["FTC NextMed final order (Dec 3, 2025); Click-to-Cancel vacatur (Jul 8, 2025); ANPRM (Mar 11, 2026)", "ftc.gov; law-firm alerts", "Verified / third-party"],
    ["FTC Sept 6, 2017 influencer warning letters (incl. Scott Disick)", "ftc.gov press release; TheFashionLaw; Consumer Reports", "Verified"],
    ["Scott Disick Mounjaro disclosure (Feb 2025)", "E! Online; Just Jared; Hola (snippets)", "Verified across outlets (snippets)"],
    ["Michael Aziz, MD practice and books", "michaelazizmd.com; US News; Zocdoc; publisher pages (snippets)", "Company-reported / third-party"],
    ["Ro–Serena Williams (Aug 21, 2025); Noom–Rebel Wilson (Sept 2025)", "PR Newswire; GlobeNewswire", "Verified"],
    ["Rhode–e.l.f. ($1B, May–Aug 2025)", "WWD; Fortune", "Verified"],
    ["Function Health Series B ($2.5B, Nov 2025); $450M financing (Jul 2026)", "Modern Healthcare; Radiology Business; press", "Third-party"],
    ["Hims & Hers Q2-2026 revenue; peptide launch plan", "Bloomberg (2026-08-10); earnings coverage (snippets)", "Company-reported via press"],
    ["Lemme GLP-1 Daily class actions (2025)", "Bloomberg Law; OpenClassActions; SupplySide SJ", "Verified (snippets)"],
    ["Goop settlement (2018); Kardashian SEC order (2022)", "Sonoma County DA; sec.gov", "Verified"],
    ["Thorne–P&G ($3.8B, Aug 2026); Medik8–L'Oréal", "Press coverage (snippets)", "Third-party"],
    ["Market-size ranges (peptide therapeutics, compounding, telehealth, longevity, GLP-1, TRT, wellness, supplements, diagnostics)", "Grand View Research; Precedence; Fortune BI; McKinsey; KFF (URLs in ledger)", "Recalled / unverified"]], widths=[2.6 * inch, 2.6 * inch, CW - 5.2 * inch], font=7.0),
 H2("Appendix B — Deliverables"),
 T([["File", "Contents"], ["01_Peptide_Market_Landscape.csv", "109 companies by segment with legal model, business model, pricing examples, ranks, evidence confidence and source"], ["02_Competitor_Website_Audit.xlsx", "Framework, scores (with assessment status), score notes, profiles, journey and medical notes, messaging, channels, rankings, 374 sources"], ["03_Peptide_Product_and_Pricing_Audit.xlsx", "136-item product inventory, price bands, monetization patterns, claims classification, regulatory legend, pricing research plan"], ["04_Celebrity_Founder_Database.xlsx", "59 classified relationships, summary formulas, lessons, principal watchlist, sources"], ["05_AminoLord_Website_Strategy.md", "Principles, design system, sitemap, 16 page specs, 12 flows, 8 wireframes, draft copy, technology comparison and stack"], ["06_AminoLord_Launch_Plan.md", "Six phases with objectives, owners, dependencies, budgets, KPIs, risks, exit criteria; roadmaps; measurement; team; budget; pricing plan; go/no-go; crisis readiness"], ["07_AminoLord_Financial_Model.xlsx", "Driver-based 36-month model, three scenarios, sensitivity, celebrity economics, assumptions register"], ["08_AminoLord_Evidence_Ledger.xlsx", "790 evidence entries, principal verification, market size, benchmarks, compliance matrix, assumption traceability, verification backlog"]], widths=[2.3 * inch, CW - 2.3 * inch], font=7.3),
 H2("Appendix C — Verification backlog (priority 1)"),
 *BUL(["Re-run website audits from rendered pages with screenshots for the top 30 companies.", "Verify Hims & Hers, LifeMD and WW 2025–2026 filings; Function, Superpower and Lifeforce funding; syndicated market reports.", "Open FDA 503A bulks-list page and PCAC July 2026 materials; confirm any final rule.", "USPTO clearance for AMINOLORD; WHOIS for aminolord.com; social handles.", "NPI, state board and ABIM checks for the intended physician; identify the reported Disick GLP-1 promotional post and its terms."]),
]

doc = Doc("outputs/AminoLord_Business_Plan_and_Proposal.pdf")
doc.multiBuild(story)
print("PDF built")
