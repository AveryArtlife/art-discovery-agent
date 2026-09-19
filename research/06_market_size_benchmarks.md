# 06 — Market Sizing & Financial-Model Benchmarks (AminoLord)

**Prepared:** 2026-09-02  
**Companion data files:** `06_market_size.json` (35 market-size records), `06_benchmarks.json` (60 benchmark records)

> ## READ FIRST — Verification status
> This session had **no working web access**: the WebSearch budget was exhausted (200/200) before the task began, and the egress proxy blocked every source domain attempted (Grand View, Precedence, Fortune BI, McKinsey, SEC EDGAR, KFF, Hims/LifeMD IR, FDA, CDC, Rock Health, TechCrunch, Fierce, STAT, Reuters, GlobeNewswire/BusinessWire/PRNewswire, Wikipedia, Huberman Lab, Function Health, Superpower, web.archive.org). Only raw.githubusercontent.com was reachable.
>
> Everything below is therefore **recalled from analyst training knowledge (cutoff ~mid-2026) and is UNVERIFIED**, except where marked **[xref]** — items cross-referenced against sibling research files written the same day (`05_regulatory_brief.md`, `03_celebrity_database.json`, `04_principal_verification.md`), whose sessions saw search-result snippets of the cited pages (third-party reports; pages not opened). Every JSON record carries `access_date: null`, an `access_note` explaining the block, a `label` of `*_unverified`, and a `confidence` grade (high / medium / low). Figures are shown as ranges where recall is imprecise. **Nothing in this file should enter the financial model or an investor document until re-checked against the listed source URL.** A prioritized verification checklist is at the end.

---

## 1. How to use these numbers for AminoLord

AminoLord — per sibling research, a **pre-launch / stealth** peptide-longevity brand associated with Scott Disick (~27M Instagram followers; publicly confirmed Mounjaro use Feb-2025) and a "Dr. Michael Azziz", scored across three models: **(A) education/commerce** (content + non-Rx supplements, affiliate), **(B) telehealth/MSO** (affiliated PC prescribing compounded peptides via 503A/503B partners), **(C) premium membership** (labs + concierge layered on A/B) — does not have a single syndicated "market." Each JSON market record now carries an `aminolord_model_relevance` field. The usable framing is:

| Layer | Best proxy | Recalled size (US unless noted) | Applicability |
|---|---|---|---|
| **Context (TAM narrative)** | Global wellness (McKinsey) | ~$2.0T global (2025), ~$480-500B US, +4-10%/yr | Headline only |
| **Adjacent demand engine** | Branded GLP-1 anti-obesity drugs | ~$20-25B US (2025) → $60-80B (2030) | Normalized injectable, telehealth-prescribed optimization |
| **Serviceable channel** | Cash-pay DTC telehealth (Hims, Ro, LifeMD, Noom, WW, long tail) | ~$4-6B (2025) → $6-8B (2026) | **Core SAM** |
| **Direct competitive set** | Cash-pay hormone optimization / TRT / peptide clinics & telehealth | ~$3-5B (2025), +12-15% | **Core SAM** (bottom-up needed) |
| **Supply chain** | US 503A/503B compounding | ~$5.5-6.5B (503A+B); 503B ~$3-4B | Cost/COGS side |
| **On-ramp product** | DTC lab testing / longevity diagnostics memberships | ~$2.5-3.5B global DTC labs; Function Health ~$2.5B valuation, >200k members at $499/yr | Lab-first funnel |
| **Cross-sell** | US supplements ~$55-65B; personalized nutrition ~$15-20B global | Premium/DTC subscription ~10-15% subsegment | Supplement SKUs |

The **peptide therapeutics market (~$45-50B global)** is the most tempting headline and the *least* applicable: it is >80% approved GLP-1/insulin/oncology peptides sold by big pharma. AminoLord's compounded wellness-peptide niche is unmeasured by any syndicated report; a plausible bottom-up order of magnitude is **$1-3B US in 2025** (clinic + telehealth + grey-market "research peptides"), growing fast but regulatorily constrained (FDA Category 2 list, Sept-2023).

---

## 2. TASK A — Market sizing by category (recalled, unverified)

Legend: **TP** = third-party estimate (recalled); **INF** = analyst inference; **CR** = company-reported (recalled). Conf = confidence in recall.

### 2.1 Peptide therapeutics
| Definition | Geo | Base | Forecast | CAGR | Source (URL in JSON) | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Approved peptide drugs | Global | 2024: ~$45-50B | 2030: ~$75-80B | ~8-9% | Grand View Research | TP / med | LOW-MOD — pharma-dominated |
| Approved peptide drugs, 10-yr | Global | 2024: ~$50B | 2034: ~$100-115B | ~8% | Precedence Research | TP / low | LOW-MOD |
| US share (~40-45% of global) | US | 2024: ~$18-22B | 2030: ~$32-36B | ~8-9% | Inferred from regional splits | INF / low | LOW-MOD; needs bottom-up wellness-peptide estimate |

### 2.2 Compounded medications (503A / 503B)
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| US compounding pharmacies (503A+503B) | US | 2024: ~$5.5-6.5B | 2030: ~$8-9B | ~5-6% | Grand View Research | TP / med | HIGH — supplier market |
| 503B outsourcing facilities | US | 2024: ~$3-4B | 2030: ~$5-6B | ~7-9% | Fortune BI / GVR / R&M | TP / low | HIGH — scaled injectable supply |
| Compounded GLP-1 spend (shortage era) | US | Early-2025 peak run-rate ~$1.5-3B | Declining post-enforcement (Apr/May-2025) | n/a | Inferred from Hims ($225M 2024; $725M 2025 guide), LifeMD, Ro, Noom, WW; Novo est. ~2M patients | INF / low | HIGH — proves model & regulatory-shock risk |

### 2.3 Telehealth / virtual care
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| US telehealth services | US | 2024: ~$40-45B | 2030: ~$90-120B | ~15-20% | Grand View Research | TP / low (definitions vary $30-100B+) | MOD — channel scale |
| Adults who have used telemedicine | US | 2024: ~76-80% ever | — | — | Rock Health consumer survey | TP / med | HIGH — funnel |
| Cash-pay DTC telehealth | US | 2025: ~$4-6B | 2026: ~$6-8B | ~30%+ | Inferred (Hims ~$2.3-2.4B, LifeMD ~$0.24B, Ro >$1B run-rate, Noom, WW, tail) | INF / low | **HIGH — core SAM** |

### 2.4 Longevity / healthy aging / anti-aging
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Anti-aging products & services | Global | 2024: ~$70-80B | 2030: ~$110-130B | ~7-8% | Grand View Research | TP / low | MOD — cosmetic-heavy |
| Longevity & anti-senescence therapies | Global | 2024: ~$25-30B | 2030: ~$40-50B | ~7-9% | Precedence / Allied | TP / low | MOD-HIGH |
| "Longevity economy" | Global | 2019: ~$110B (longevity tech) | 2025: ~$600B | n/a | BofA (2019) | TP / med | LOW — headline only |
| Consumers rating healthy aging a top priority | US | 2025: ~60% (wellness ~82%) | — | — | McKinsey Future of Wellness | TP / med | HIGH — demand narrative |

### 2.5 Medical weight management / GLP-1
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Branded GLP-1 anti-obesity drug sales | US | 2025: ~$20-25B | 2030: ~$60-80B | ~25-30% | Inferred from Novo/Lilly reports + GS/MS forecasts | INF / med | HIGH — demand engine |
| Weight management services & products | US | 2024: ~$75-90B | 2030: ~$110-130B | ~6-7% | Marketdata / GVR | TP / low | MOD |
| Telehealth GLP-1 revenue comps | US | Hims WL ~$225M (2024) | Hims ~$725M (2025 guide, later restated) | n/a | Hims releases; Ro press | CR / med | HIGH — direct comps |
| GLP-1 usage | US | 12% ever / 6% current (May-2024) | ~12-13% / ~6-8% (2025 polls) | — | KFF, Gallup, RAND | TP / high | HIGH — funnel & price sensitivity |

### 2.6 Hormone optimization / TRT / HRT
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Testosterone replacement therapy | US | 2024: ~$1.2-1.5B | 2030: ~$1.8-2.2B | ~5-7% | Grand View Research | TP / med | HIGH (excludes compounded/clinic memberships) |
| Menopause HRT drugs | US | 2024: ~$5-7B | 2030: ~$8-10B | ~6-7% | GVR / Fortune BI | TP / low | MOD-HIGH |
| Cash-pay hormone optimization clinics & telehealth | US | 2025: ~$3-5B | 2030: ~$6-9B | ~12-15% | Inferred (Hone, Marek, Lifeforce, Defy, Gameday franchises) | INF / low | **HIGH — direct competitive set** |

### 2.7 Sports recovery & performance
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Sports medicine devices & services | Global | 2024: ~$7-8B | 2030: ~$11-13B | ~7-8% | Grand View Research | TP / low | LOW |
| Sports nutrition | Global | 2024: ~$45-50B | 2030: ~$75-85B | ~8-9% | GVR / Euromonitor | TP / low | MOD — supplement adjacency |
| Recovery tech & services | US | 2024: ~$3-5B | 2030: ~$6-9B | ~10-12% | Inferred (Therabody, Hyperice, Restore Hyper Wellness) | INF / low | MOD |

### 2.8 Consumer wellness
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Global wellness market (McKinsey) | Global | 2024: ~$1.8T | 2025: ~$2.0T | ~4-5%/yr | McKinsey Future of Wellness (Jan-2024; May-2025) | TP / high | HIGH context — trend chapters map to AminoLord |
| US wellness market (McKinsey) | US | 2024: ~$480B | 2025: ~$500B+ | ~5-10%/yr | McKinsey | TP / med | HIGH context |
| Global wellness economy (GWI) | Global | 2023: ~$6.3T | 2028: ~$9T | ~7% | Global Wellness Institute | TP / med | LOW — too broad |

### 2.9 Premium / personalized supplements
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| US dietary supplements | US | 2024: ~$55-65B | 2030: ~$80-90B | ~5-6% | NBJ / Grand View | TP / med | MOD-HIGH |
| Personalized nutrition | Global | 2024: ~$15-20B | 2030: ~$30-40B | ~12-15% | GVR / Precedence | TP / low | HIGH (note Care/of shutdown 2024) |

### 2.10 Personalized / precision health
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Personalized medicine (broad) | Global | 2024: ~$550-650B | 2030: ~$0.9-1.1T | ~7-8% | Grand View Research | TP / low | LOW |
| Precision medicine (narrow) | Global | 2024: ~$100-140B | 2030: ~$200-250B | ~11-12% | Precedence / Fortune BI | TP / low | LOW |

### 2.11 Men's health telehealth
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| Men's health telehealth (ED, hair, low-T, PE, weight) | US | 2024: ~$3-4B | 2028: ~$6-8B | ~15-20% | Inferred (Hims $1.48B FY24, Ro, Keeps, Hone, BlueChew) | INF / low | **HIGH — same persona** |
| ED drugs | US | 2024: ~$1.5-2B | 2030: ~$2-2.5B | ~4-5% | Grand View Research | TP / low | MOD — anchor SKU |

### 2.12 At-home lab testing / longevity diagnostics
| Definition | Geo | Base | Forecast | CAGR | Source | Type / Conf | Applicability |
|---|---|---|---|---|---|---|---|
| DTC laboratory testing | Global | 2024: ~$2.5-3.5B | 2030: ~$5-7B | ~10-13% | Grand View Research | TP / low | HIGH — on-ramp |
| Function Health / Superpower | US | Function: $499/yr, ~160 biomarkers, >200k members (2025), ~$2.5B valuation (Nov-2025, ~$298M Series B), Ezra acquired May-2025; Superpower: $499/yr, $30M Series A (Mar-2025) | — | — | Company / TechCrunch / Bloomberg | CR / med | HIGH — membership economics |
| Quest QuestHealth / Labcorp OnDemand consumer-initiated | US | ~$100-200M each, +20%+ | — | — | Earnings calls | CR / low | MOD — lab supply |

---

## 3. TASK B — Public-company & funding benchmarks (recalled, unverified)

### 3.1 Public comps
| Company | Metric | Value (recalled) | Conf |
|---|---|---|---|
| **Hims & Hers** | FY2024 revenue / subscribers | $1.48B (+69%) / 2.2M (+45%); adj. EBITDA ~$177M | high |
| | FY2024 weight-loss revenue | ~$225M | med |
| | FY2025 guidance (Feb-2025) | Revenue $2.3-2.4B; adj. EBITDA $270-320M; weight loss ~$725M (restated after May-2025 wind-down of commercial-scale compounded semaglutide) | med |
| | Q1-25 / Q2-25 / Q3-25 revenue | $586M / $545M / ~$599M; subscribers 2.4M / 2.4M / ~2.5M | med |
| | Gross margin | 73-77% in 2025 (from ~81% in 2023) | high |
| | Marketing % revenue | ~40-48% (FY2024 ~43-46%; 2025 quarters ~35-45%) | med |
| | Implied marketing $/net-new subscriber | ~$800-950 (FY2024); gross-add CAC est. $150-300 | low |
| | Q4-2025 / FY2025 actuals; FY2026 guidance; Q1-Q2 2026 | **GAP — not reliably recalled; pull from IR site** | — |
| | Long-term targets | $6.5B revenue / $1.3B adj. EBITDA by 2030 | med |
| | Peptide/longevity moves | Trybe Labs (Feb-25), Zava (Jun-25), at-home labs + low-T + menopause programs (~Sep-Nov-25), Canada generic semaglutide plan (Jan-26). No confirmed branded peptide launch known as of mid-2026 | low |
| **LifeMD** | FY2024 revenue | ~$212.5M (+43%); telehealth ~$151M; telehealth GM ~88-90% | med |
| | Active patients | ~290-300k; weight-mgmt ~80-100k; LillyDirect/NovoCare partnerships 2025 | med |
| | FY2025 | Guide $235-240M; Q1 $65.7M, Q2 ~$62.5M, Q3 ~$66-70M | low |
| **WW** | Restructuring | Ch.11 6-May-2025 (~$1.15B debt cut); emerged 24-Jun-2025; clinical subs ~130-140k; clinical revenue ~$25-35M/qtr (2025) | low |

### 3.2 Private comps
| Company | Funding / valuation | Pricing / revenue | Conf |
|---|---|---|---|
| **Ro** | ~$1B raised; ~$7B valuation (Series D, Feb-2022) | >$1B annualized revenue (2025 statements); Body program ~$99/mo + drug; Serena Williams campaign Aug-2025 (record sign-ups claimed; terms undisclosed) | med/low |
| **Noom** | ~$650M raised; ~$3.7B (2021) | Noom Med compounded semaglutide $149/mo (2024); revenue est. ~$400-500M (2024) | low |
| **Function Health** | $53M Series A (Nov-2024, a16z; celebrity investors Damon, Efron, Hart, Pascal); ~$298M Series B at ~$2.5B (Nov-2025, led by Redpoint) [xref] | $499/yr; ~160 biomarkers; >200k members; Ezra MRI from ~$499; co-founder/CMO Dr. Mark Hyman was the primary early acquisition channel | med |
| **Superpower** | $30M Series A announced 22-Apr-2025 (Forerunner; >$300M post-money; investors Logan Paul, Steve Aoki, Vanessa Hudgens, Giannis) [xref] | $499/yr (100+ biomarkers); ~$199 tier discussed | med |
| **Lifeforce** | ~$12M Series A (2022) + ~$12M Series B (2023-24); Robbins/Diamandis | $129/mo after ~$549 diagnostic; TRT, HRT, peptides (sermorelin), NAD+ — closest single analog | med |
| **Fountain Life** | Private (Diamandis, Robbins, Kapp, Hariri; formed Oct-2020); raised $18M Aug-2025 [xref] | Memberships reported $10.5K-$85K/yr (APEX ~$19.5K recalled); explicitly offers peptide therapy + NAD+ | med |
| **Marek Health** | Private | Labs ~$300-600 + consult; TRT ~$100-250/mo; peptides per protocol | low |
| **Henry Meds** | Private | Semaglutide ~$297/mo (promos ~$249); tirzepatide ~$449/mo | med |
| **Eden** | Private | Semaglutide ~$196-296/mo; tirzepatide ~$299-399/mo | low |
| **Mochi** | Private | ~$79/mo membership + meds ~$99-200/mo | low |
| **Ivim** | Private | Membership ~$99-149/mo; meds ~$149-349/mo | low |
| **Ways2Well** [xref] | Private (founder Brigham Buhler; 3x JRE guest) | $99 peptide consult then mail-order compounded vials; lists Joe Rogan as client; credited with Jelly Roll / Russell Crowe transformations (AP/CNN Nov-2025) | low |
| **Neko Health** [xref] | $260M Series B at $1.8B (Jan-2025); $700M Series C (Jul-2026) | $299/scan; 100k waitlist; US launch pending | med |
| **Lemme** (Kourtney Kardashian) [xref] | Private | GLP-1 Daily ($90 / $72 sub) >$30M revenue in 16 months; $13M single month on TikTok Shop (Nov-2025) — unaudited; class actions 2025; rebranded 'Lemme Reset' | low |

### 3.3 Unit-economics inputs for the model
| Input | Recalled range | Basis | Conf |
|---|---|---|---|
| CAC (gross new subscriber), telehealth | $100-300 | Hims implied; sell-side; operator interviews | low |
| Monthly churn | 5-10% general DTC health; 8-15% GLP-1; 2-4% TRT/hormone | Subscription benchmarks; Prime Therapeutics persistence (32-46% at 12 mo) | med |
| Gross margin, compounded GLP-1 telehealth | 70-80% bundled; 85-90% visit/membership-only | Hims, LifeMD | med |
| Clinician cost per async visit | $20-60 (sync video $50-120) | Wheel / OpenLoop / SteadyMD | med |
| Compounded peptide retail (monthly) | Sermorelin $100-350; tesamorelin $300-700; CJC/ipamorelin $200-450; NAD+ inj $150-400; GHK-Cu $100-250; MOTS-c $200-400; BPC-157 $100-300 (Cat-2, not lawfully compoundable) | Clinic price pages | low |
| Peptide pharmacy COGS | $30-120/month → 60-80% GM | Operator quotes | low |
| Compounded GLP-1 retail | Semaglutide $149-399; tirzepatide $299-599; branded self-pay Wegovy $499→$349/$199 (Nov-2025), Zepbound vials $349-499 | Price pages | med |
| Lab costs | DTC: CBC ~$29, CMP ~$39-49, testosterone ~$49-69, wellness panels $99-300; wholesale 50-100-biomarker panel $60-150; draw fee $10-25 | Quest/Labcorp; operators | med |
| Payment processing | 2.9%+$0.30 standard; Shopify Plus ~2.15-2.4%; high-risk healthcare MIDs 3.5-5% | Stripe/Shopify | high |
| Shopify Plus | From $2,300/mo (3-yr) / ~$2,500 (1-yr); 0.35-0.40% variable above $800k/mo | Shopify | high |
| Telehealth vendors | Wheel/OpenLoop/SteadyMD $25-75/visit + $5-25k setup + $2-10k/mo minimums; Healthie $0-149+/provider/mo; Tebra ~$300-500/provider/mo; MSO/PC legal setup $50-150k | Vendor sites | low |
| LegitScript | Telehealth: ~$1-2k application + ~$1-2.5k/yr; compounding pharmacy ~$3-6k initial | LegitScript | low |
| Insurance | NP/PA malpractice $1-3k/yr; MD $5-15k; entity telemed liability $10-40k/yr; supplement product liability $2-15k/yr (~$1-3 per $1k sales); cyber $2-10k | Broker rules of thumb | low |
| Celebrity economics [xref] | Rules of thumb: licensing royalties 5-15% of net sales; ambassador equity 1-5% early-stage + $0.5-5M/yr cash for A-list. Founder-equity outcomes: Rhode→e.l.f. $1B ($800M + earnout; Bieber >$300M at close, May/Aug-2025); Onnit→Unilever (Rogan equity partner; est. $100-400M, Apr-2021); Centr→HighPost ~$200M (Mar-2022); Ladder (LeBron/Schwarzenegger) only ~$4M revenue in 2 yrs. Board/stake: Oprah ~10% of WW; stock +100% on entry (2015), -25% in a day on exit (Feb-2024). Investor cohort: AG1 $115M at $1.2B (Jan-2022) with single-digit % celebrity stakes (unverified). Ambassador: Aniston/Vital Proteins (2020, undisclosed equity); Serena/Ro (Aug-2025, undisclosed). Key-person risk: Brecka/10X Health split → $100M vs $13M suits (settled Apr-2025) | 03_celebrity_database.json; press; Licensing International norms | med |
| Affiliate/influencer | Affiliate 10-30% first order; TikTok Shop 10-20%; nano $50-500, micro $500-5k, macro $5-50k, celebrity $50k-1M+/post; CPM $10-30; podcast host-read $18-50 CPM | IMH / industry | med |
| Email / SMS | Email open 35-50%, click 1-2%, placed-order 0.1-0.2%, RPR $0.05-0.20; flows 3-5x campaigns; email+SMS 20-35% of revenue. SMS CTR 6-10%, conv 1-3%, $0.10-0.50/msg | Klaviyo/Attentive benchmarks | med |

### 3.4 Regulatory anchors [xref: 05_regulatory_brief.md — third-party reports unless noted]
- **Compounded GLP-1 wind-down:** tirzepatide off shortage list Dec-2024; semaglutide Feb-2025; enforcement-discretion periods expired spring 2025 (consistent reporting). FDA warning letters: 55+ (16-Sep-2025), ~30 to telehealth firms (Mar-2026), ~25 more (Jun-2026); >1,700 adverse events by 21-May-2026. **30-Apr-2026:** FDA proposed excluding semaglutide/tirzepatide/liraglutide from the 503B bulks list. Novo has filed 130+ suits in 40 states; sued **Hims & Hers 8-9-Feb-2026**, dismissed Mar-2026 after a Wegovy partnership. **Model implication: treat compounded GLP-1 as a wind-down; route GLP-1 demand to branded DTC/affiliate (LillyDirect $299-449; NovoCare $199 intro → $349; TrumpRx ~$350; Wegovy pill $149 → $199).**
- **Peptide Category-2 reversal (2026):** Sept-2023 PCAC put ~19 longevity peptides (BPC-157, CJC-1295, ipamorelin, GHK-Cu, AOD-9604, MOTS-c, Ta1, TB-500, selank, semax, KPV, epitalon, etc.) in 503A **Category 2**. **27-Feb-2026:** HHS Sec. Kennedy announced ~14 of 19 would move out; **15-Apr-2026** FDA updated the 503A bulks document (effective ~23-Apr); **23-24-Jul-2026** PCAC narrowly recommended **BPC-157, KPV, TB-500, MOTS-c, semax, epitalon** for the 503A list over FDA staff objections. Melanotan II, GHRP-2/6, LL-37, PEG-MGF remain Category 2. Sermorelin and NAD+ remained compoundable throughout; tesamorelin is an approved drug. Not approval; final rulemaking pending; reversal risk. **This is simultaneously the binding constraint and the 2026 upside for Model B's formulary.**
- **RUO loophole closed:** seven FDA warning letters dated 31-Mar-2026 (published 7-Apr-2026) hold that "research use only" disclaimers do not negate intended use. Model A must never sell or affiliate-link RUO peptides.
- **FTC:** NextMed final order 3-Dec-2025 ($150k; fake reviews, fabricated before/after, hidden fees) — verified by sibling session; FTC + state AGs sued Hims & Hers in 2026 over health-data sharing and subscription billing (Shumaker alert; details unverified). Click-to-Cancel vacated 8-Jul-2025; ROSCA still enforced; new ANPRM 11-Mar-2026.
- **Ad platforms / payments:** Meta health-wellness data restrictions (2025) degrade lower-funnel optimization → higher effective CAC for A/C; Google/Meta Rx ads require LegitScript (4-12 weeks); Stripe/Shopify Payments treat RUO peptides as prohibited; expect high-risk MCCs, 5-15% rolling reserves, 3.5-5% all-in processing for Model B.

---

## 4. TASK C — Search demand, content & channel benchmarks (recalled, unverified)

**Search (Google Trends, not fetched — pull series when access is restored):**
- "peptides" (US): roughly 2-3x from 2023 to 2025, all-time highs in 2025, sustained into 2026.
- "BPC-157": ~3x+ 2023→2025; spikes around Rogan/Huberman/RFK Jr. mentions and FDA Category-2 news.
- "peptide therapy near me" and "sermorelin": from near-zero (2022) to measurable, rising volume; sermorelin ~2x 2023→2025.
- "GLP-1": ~5x 2022→2025 as the generic category term; "Ozempic" peaked 2023-24; "compounded semaglutide" peaked H1-2025 then fell after FDA enforcement.

**Podcasts / creators:** Huberman Lab peptide episode ("Benefits & Risks of Peptide Therapeutics…", 2023-24 — verify date); Peter Attia (The Drive) peptide episodes/AMAs 2024-25; Joe Rogan's repeated BPC-157 endorsements (2019-2025) and 2025 longevity-guest episodes; Rich Roll, Dave Asprey, Ben Greenfield, Gary Brecka, More Plates More Dates. TikTok #peptides/#bpc157 in the hundreds of millions to billions of views (2025); YouTube explainers routinely 1M+ views.

**Mainstream press "peptide boom" (2025-26):** NYT features on peptide clinics/"peptide bros"; WSJ on peptides as the wellness obsession and grey-market "research peptides"; Bloomberg on longevity/peptide investors; Vox "The peptide craze, explained"; The Atlantic; GQ/Men's Health/Esquire guides; STAT/NBC on FDA & RFK Jr. peptide policy. (Headlines/dates must be verified.)

**Public figures [xref]:** Joe Rogan — BPC-157 mentioned in 31+ JRE episodes (Psychology Today, Aug-2026), credited with the peptide's mainstream take-off; Ways2Well founder on JRE #1873/#2079/#2376. **RFK Jr.** — 27-Feb-2026 announcement moving ~14 peptides out of FDA Category 2 is the single largest regulatory-sentiment catalyst (NPR 31-Mar-2026). Dana White — Oct-2023 Brecka podcast, credited a protocol incl. 'common peptides' with reversing metabolic syndrome. Dave Asprey; Gary Brecka; Bryan Johnson (Netflix 'Don't Die', Jan-2025; NYT Mar-2025 on Blueprint missing break-even); Mel Gibson/Rogan anecdotes (2025). **Scott Disick** confirmed Mounjaro use on The Kardashians (Feb-2025) and appears to have posted promotional GLP-1 content (brand/disclosure unverified — potential exclusivity conflict).

**Consumer surveys:** KFF (May-2024): 12% of adults ever used a GLP-1, 6% currently; 54% of users find it hard to afford; 2025 polls (KFF, Gallup, RAND) ~12-13% ever / ~6-8% current. McKinsey 2025: ~60% of US consumers rate healthy aging a top priority; 82% call wellness a top/important priority. **No credible representative survey on peptide use recalled — a primary survey is recommended.**

**Channel benchmarks:** see §3.3 (affiliate/influencer, email/SMS).

---

## 5. Verification checklist (priority order, when web access is available)
1. **Hims & Hers** Q4-2025, Q1-2026, Q2-2026 releases and FY2026 guidance; 10-K FY2025 marketing % and any peptide/longevity launches (investors.hims.com; SEC EDGAR CIK 0001773751).
2. **LifeMD** Q4-2025 through Q2-2026 (ir.lifemd.com); **WW** FY2025 10-K clinical revenue.
3. **Function Health** latest member count / valuation (Nov-2025 Series B); **Superpower** 2026 funding & tiers; **Lifeforce** latest round.
4. **Ro** revenue statements and any Serena campaign metrics.
5. Syndicated market reports: Grand View (peptides, US compounding, US telehealth, anti-aging, TRT, HRT, DTC lab testing, US supplements, personalized nutrition, personalized medicine), Precedence (peptides, longevity), Fortune BI (503B) — confirm base year/value/CAGR and publication dates.
6. **McKinsey Future of Wellness 2025** (and any 2026 edition) exact figures; **KFF** 2025 GLP-1 polls.
7. **FDA** compounding pages: Category-2 list status and any 2025-26 reconsideration of peptide bulks; DOJ/FDA enforcement letters to telehealth firms.
8. Google Trends series for the five terms; podcast episode dates; press headlines/dates.
9. Vendor pricing pages (Wheel, OpenLoop, SteadyMD, Healthie, Hint, Tebra, LegitScript, Shopify Plus, Stripe).
10. **[xref items]** Open the primary pages behind sibling-file snippets: FDA 503A bulks document (15-Apr-2026 update) and PCAC 23-24-Jul-2026 materials; STAT/AJMC/Pharmacy Times peptide-reversal articles; CNBC 9-Feb-2026 Novo v. Hims; Shumaker alert on FTC v. Hims; Fierce Healthcare 650% traffic-spike report; Lemme revenue case studies; Yahoo headline on Disick's GLP-1 promotional post (identify brand, date, disclosure).
