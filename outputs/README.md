# Reserve Clinic — Deliverables index (prepared 2026-09-02; margin and growth pack added 2026-09-18)

Proposed concept. Scott Disick and Dr. Michael Azziz are referenced only as *proposed* principals; no public confirmation of any relationship to Reserve Clinic was found. Nothing here is legal, medical, or investment advice.

| File | Contents |
|---|---|
| `ReserveClinic_Margins_and_Growth_Proposal.pdf` | **17-page partner-facing proposal on profit margins and growth potential** (added 2026-09-18), built for the operating structure with a turnkey compliance-and-fulfilment provider at a flat $600/month: the one-page answer, the two-line structure, per-unit margin anatomy, the four audience dials, three scenarios, retention sensitivity, category context, capital requirement, illustrative partner economics, and a 90-day plan |
| `09_ReserveClinic_Margin_and_Growth_Model.xlsx` | **Driver-based 36-month margin-and-growth model** (added 2026-09-18) with conservative/baseline/aggressive scenarios: 64 drivers, 81 model lines, unit economics per order and per member-month, three closed-form sensitivity grids, partner economics, a 20-question provider diligence checklist, and the 18-benchmark evidence sheet. Recalculated with LibreOffice: 9,361 formulas, zero errors |
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
| `margin_charts.py` | charts for the margin proposal |
| `build_margin_proposal.py` | `ReserveClinic_Margins_and_Growth_Proposal.pdf` |
| `logo.py` | `brand/` logo variants |

Recalculate the workbooks with LibreOffice after regenerating. The margin pack is a two-step build: run
`build_margin_model.py`, recalculate it, re-extract values, then run `build_margin_proposal.py`, which
regenerates its own charts.

## The margin and growth pack (2026-09-18)

Added in response to a specific question: estimated profit margins and growth potential for a fully
compliant fifty-state peptide and supplement business using a telehealth model, 503A and 503B pharmacies,
a turnkey provider at a flat $600/month, and the proposed brand partner as promoter.

Headline model outputs, which are arithmetic consequences of stated drivers and not forecasts:

| | Conservative | Baseline | Aggressive |
|---|---|---|---|
| Net revenue, year 3 | $352k | $7.1M | $138.5M |
| Blended gross margin, year 3 | 48% | 57% | 65% |
| EBITDA margin, year 3 | -161% | 4% | 39% |
| First profitable month | not within 36 months | month 22 | month 3 |
| Capital required | $2.1M | $1.4M | $942k |

Three findings worth carrying forward:

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
