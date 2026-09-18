# Reserve Clinic — Deliverables index (prepared 2026-09-02; margin and growth pack added 2026-09-18)

Proposed concept. Scott Disick and Dr. Michael Azziz are referenced only as *proposed* principals; no public confirmation of any relationship to Reserve Clinic was found. Nothing here is legal, medical, or investment advice.

| File | Contents |
|---|---|
| `ReserveClinic_Margins_and_Growth_Proposal.pdf` | **21-page partner-facing proposal on profit margins and growth potential** (added 2026-09-18): the one-page answer, the two-line structure, per-unit margin anatomy, the four audience dials, the three-tier targeted media plan and the derived CAC advantage, what the partnership is worth against a no-partner counterfactual, three scenarios, retention sensitivity, category context, capital requirement, illustrative partner economics, and a 90-day plan |
| `09_ReserveClinic_Margin_and_Growth_Model.xlsx` | **Driver-based 36-month margin-and-growth model** (added 2026-09-18): 83 drivers, 98 model lines, four columns — conservative/baseline/aggressive plus baseline-with-no-brand-partner. Unit economics per order and per member-month, targeted paid media as three separately-priced tiers with incrementality haircuts, four closed-form sensitivity grids, partner economics, a 20-question provider diligence checklist, and the 20-benchmark evidence sheet. Recalculated with LibreOffice: 14,992 formulas, zero errors |
| `ReserveClinic_Brief_for_Scott_Disick.pdf` | 6-page abridged brief for the proposed brand partner: the moment, the idea, the landscape and celebrity lessons, the proposed role, the plan and the decisions needed. Drawn illustrations; proposal-only framing |
| `ReserveClinic_Business_Plan_and_Proposal.pdf` | 43-page investor/partner proposal (executive summary, market, competition, celebrity findings, positioning, principals, business model, website concept, wireframes, technology, compliance, launch, financials, risks, go/no-go, next steps, sources) |
| `01_Peptide_Market_Landscape.csv` | 109 companies by segment with legal model, business model, pricing examples, within-segment rank, evidence confidence, source |
| `02_Competitor_Website_Audit.xlsx` | 23-criterion framework, scores with assessment status, score notes, company profiles, journey and medical notes, messaging and claims, channels, segment rankings, 374 sources |
| `03_Peptide_Product_and_Pricing_Audit.xlsx` | 136-item product inventory, price bands, monetization patterns, claims classification, regulatory legend, pricing research plan |
| `04_Celebrity_Founder_Database.xlsx` | 59 classified relationships, classification summary (formulas), lessons, principal watchlist, sources |
| `05_ReserveClinic_Website_Strategy.md` | Experience principles, design system, sitemap, page specifications, user flows, wireframes, draft copy, technology comparison and recommended stack |
| `06_ReserveClinic_Launch_Plan.md` | Phases 0–5 with objectives, owners, dependencies, budgets, KPIs, risks, exit criteria; 30/60/90-day, 6- and 12-month roadmap; measurement framework; team; budget; pricing research plan; go/no-go checklist |
| `07_ReserveClinic_Financial_Model.xlsx` | Driver-based, editable 36-month model with conservative/base/upside scenarios, sensitivity grids, hypothetical celebrity-economics structures, assumptions register |
| `08_ReserveClinic_Evidence_Ledger.xlsx` | 790 evidence entries with URLs, dates and labels; principal verification; market size; benchmarks; compliance matrix; model-assumption traceability; verification backlog |

## Material research limitation
The research environment blocked direct page loads of company websites, regulators, review sites, ad libraries and traffic tools, and capped web searches. Company facts come from dated search-result excerpts (2026-09-02); website UI/UX scores are "not assessed" or low-confidence inferences; traffic/social/ad data were not retrievable; the market-size and benchmark workstream is recalled/unverified; USPTO, NPI and state-board checks for the proposed principals were blocked. The verification backlog in `08_ReserveClinic_Evidence_Ledger.xlsx` lists what to re-run before external use.

## Rebuilding
Research artifacts are in `../research/`. Build scripts are in `../build/`:

| Script | Produces |
|---|---|
| `build_research_workbooks.py` | `01_*.csv`, `02/03/04/08_*.xlsx` |
| `build_financial_model.py` | `07_ReserveClinic_Financial_Model.xlsx` |
| `build_pdf.py` | `ReserveClinic_Business_Plan_and_Proposal.pdf` |
| `build_brief.py` | `ReserveClinic_Brief_for_Scott_Disick.pdf` |
| `build_margin_model.py` | `09_ReserveClinic_Margin_and_Growth_Model.xlsx` |
| `extract_margin_values.py` | pulls the recalculated workbook into `margin_values.json` |
| `margin_charts.py` | charts for the margin proposal |
| `build_margin_proposal.py` | `ReserveClinic_Margins_and_Growth_Proposal.pdf` |
| `logo.py` | `brand/` logo variants |

Recalculate the workbooks with LibreOffice after regenerating. The margin pack is a four-step build:
`build_margin_model.py` → recalculate with LibreOffice → `extract_margin_values.py` →
`build_margin_proposal.py` (which regenerates its own charts). The workbook is the single source of truth;
nothing is recomputed in Python for the document.

## The margin and growth pack (2026-09-18)

Added in response to a specific question: estimated profit margins and growth potential for a fully
compliant fifty-state peptide and supplement business using a telehealth model, 503A and 503B pharmacies,
a turnkey provider at a flat $600/month, and the proposed brand partner as promoter.

Headline model outputs, which are arithmetic consequences of stated drivers and not forecasts:

| | Conservative | Baseline | Aggressive | Baseline, no partner |
|---|---|---|---|---|
| Net revenue, year 3 | $377k | $10.0M | $356M | $3.7M |
| Blended gross margin, year 3 | 49% | 57% | 66% | 57% |
| EBITDA margin, year 3 | -147% | 11% | 36% | -8% |
| First profitable month | not within 36 months | month 10 | month 3 | month 34 |
| Capital required | $2.0M | $803k | $927k | $2.8M |

Five findings worth carrying forward:

1. **The $600 fee is modelled as a platform fee only.** Published pricing for comparable turnkey telehealth
   infrastructure is $3,000–$6,000/month plus $5,000–$10,000 onboarding plus per-consult fees, so every
   variable cost — medication, per-consult clinician time, cold-chain shipping, card processing — is carried
   separately. The `Provider_Diligence` sheet holds the 20 questions that need written answers.
2. **Fifty-state coverage applies to the non-prescription line only.** The prescription line ramps from
   26–45% of the US population to a 70–88% ceiling because of licensure, asynchronous-prescribing rules,
   corporate-practice-of-medicine limits and the section 503A(b)(3) five-percent interstate cap.
3. **Prescription retention is the driver most likely to break the model.** Above roughly 15% monthly churn
   the prescription line does not pay for its own acquisition at any plausible CAC, and the outside evidence
   on the comparable population points that way.
4. **The celebrity CAC advantage is derived, not assumed.** Paid media is split into three tiers — branded
   and intent search, retargeting, and cold prospecting with partner creative. The partnership creates cheap
   warm inventory (branded search from post views, engagement audiences from post engagers) and discounts the
   cold tier through better creative. Both warm tiers carry an incrementality haircut, because holdout tests
   show only 25–30% of retargeting conversions are incremental. The like-for-like result is a **21–27% CAC
   advantage at equal spend**, largest on the first tranche of budget. Blended CAC still *rises* with spend in
   every scenario — that is the auction, and a model where it falls with scale has no competition in it.
5. **The partnership is worth more than it costs, on these assumptions.** Against an identical business with
   no partner: +$13.0M of 36-month revenue, +$3.1M of 36-month EBITDA, break-even 24 months earlier, and
   $2.0M less capital, against $1.45M of illustrative partner cash. That conclusion rests on two unmeasured
   audience dials, and it assumes the partner's likeness can be licensed for *paid* media — organic posting
   rights and paid-usage rights are separate grants.
