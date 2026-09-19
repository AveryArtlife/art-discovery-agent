# Reserve Clinic — Deliverables index (prepared 2026-09-02; margin and growth pack added 2026-09-18)

Proposed concept. Scott Disick and Dr. Michael Azziz are referenced only as *proposed* principals; no public confirmation of any relationship to Reserve Clinic was found. Nothing here is legal, medical, or investment advice.

| File | Contents |
|---|---|
| `ReserveClinic_Margins_and_Growth_Proposal.pdf` | **25-page partner-facing proposal on profit margins and growth potential** (added 2026-09-18): the one-page answer, why break-even is quarter one, the wholesale dropship trade-off, the two-line business, per-unit margin anatomy, the four audience dials, the three-tier targeted media plan and the derived CAC advantage, what the partnership is worth against a no-partner counterfactual, single-factor stress analysis, retention sensitivity, category context, capital requirement, illustrative partner economics, and a 90-day plan |
| `09_ReserveClinic_Margin_and_Growth_Model.xlsx` | **Driver-based 36-month margin-and-growth model** (added 2026-09-18): 83 drivers, 98 model lines, six columns — conservative/baseline/aggressive, baseline-with-no-brand-partner, and two single-factor stress columns (weak audience, weak retention). Unit economics per order and per member-month, targeted paid media as three separately-priced tiers with incrementality haircuts, four closed-form sensitivity grids, partner economics, a 20-question provider diligence checklist, and the 22-benchmark evidence sheet. Recalculated with LibreOffice: 22,358 formulas, zero errors |
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
a turnkey provider at a flat $600/month, wholesale dropship fulfilment, and the proposed brand partner
as promoter.

Headline model outputs, which are arithmetic consequences of stated drivers and not forecasts:

| | Conservative | Baseline | Aggressive | No partner | Weak audience only | Weak retention only |
|---|---|---|---|---|---|---|
| Net revenue, year 1 | $375k | $5.6M | $49.7M | $580k | $1.2M | $5.2M |
| Net revenue, year 3 | $711k | $15.5M | $330.7M | $3.9M | $4.7M | $12.5M |
| EBITDA, year 3 | ($387k) | $2.6M | $122.3M | $280k | $104k | $2.0M |
| EBITDA margin, year 3 | -54% | 17% | 37% | 7% | 2% | 16% |
| First profitable month | never | **month 2** | month 2 | month 24 | month 24 | month 2 |
| Capital required | $1.2M | **$48k** | $77k | $1.1M | $785k | $48k |

Nine findings worth carrying forward:

1. **Overhead, not demand, decides break-even — and the first version of this model got it wrong.** That draft
   assumed $104k/month of fixed cost (venture-scale team, legal and creative) on top of a plug-and-play operation,
   which pushed break-even to month 10 and the capital need to $803k. The unit economics were identical and were
   never the constraint. Corrected to the structure actually described — $600 provider, founder plus one media
   buyer, partner supplying most of the creative — the fixed base is ~$57k/month and the business is EBITDA-positive
   in **month 3** on **$265k** of capital. What was *not* cut: provider fee, certification, insurance, medical
   director, and the percent-of-revenue floors that stop opex staying flat as revenue scales.
2. **Wholesale dropship is close to margin-neutral and hands back the working capital.** The wholesaler holds the
   stock and ships on order, so the brand never pays for inventory. Like-for-like per order: $44.61 of contribution
   (59.0%) on wholesale dropship against $45.69 (60.4%) owning manufacturing runs — **$1.08 an order, about 1.4% of
   net revenue, is the whole price of never touching inventory.** In exchange the cash trough drops to $37k and the
   capital requirement to **$48k**. Two real costs remain: there is no COGS improvement curve (an owned run falls
   toward ~$4/unit at 5,000 units; a wholesale price does not, and closing that gap would be worth ~$1.5M/yr of
   gross profit at year-3 volumes, so in-house manufacturing is a quantifiable second-stage lever), and the product
   is not proprietary, so the moat is brand and audience rather than formulation.
3. **The dropship arrangement moves the stock, not the liability.** FDA treats an own-label distributor as
   ultimately responsible for product quality and has stated a firm "cannot contract out its ultimate
   responsibility" for cGMP compliance. A supplier's "GMP certified" claim transfers nothing; FDA and FTC hold the
   brand owner responsible for label and marketing claims. With a named public figure on the bottle, a third party's
   quality failure is his reputational problem and the company's legal one — which is why independent third-party
   testing, per-lot certificate-of-analysis review, and a supplier quality agreement with audit rights are budgeted
   as a standing function rather than cut alongside the inventory line. Separately: a wholesaler sized for ordinary
   DTC volumes can be cleared out by one post to 27M followers, so get a committed stock allocation in writing.
4. **The $600 fee is modelled as a platform fee only.** Published pricing for comparable turnkey telehealth
   infrastructure is $3,000–$6,000/month plus $5,000–$10,000 onboarding plus per-consult fees, so every
   variable cost — medication, per-consult clinician time, cold-chain shipping, card processing — is carried
   separately. The `Provider_Diligence` sheet holds the 20 questions that need written answers.
5. **Fifty-state coverage applies to the non-prescription line only.** The prescription line ramps from
   26–45% of the US population to a 70–88% ceiling because of licensure, asynchronous-prescribing rules,
   corporate-practice-of-medicine limits and the section 503A(b)(3) five-percent interstate cap.
6. **Prescription retention hurts but does not break it — the audience does.** Single-factor stress, holding
   everything else at baseline: weak retention alone costs 18% of year-3 revenue and the business is still
   profitable from month 3 with $4.0M of cumulative EBITDA. Weak *audience* alone removes 68% of year-3 revenue,
   pushes break-even to month 23 and turns 36-month EBITDA negative. It takes the audience underperforming **and**
   everything else going wrong at once to reach the conservative $710k. So the 439x conservative-to-aggressive band
   is compound pessimism against compound optimism; the practical planning range is baseline to aggressive, with
   weak-audience as the downside to hold capital against.
7. **Prescription retention remains the key clinical-economics risk.** Above roughly 15% monthly churn
   the prescription line does not pay for its own acquisition at any plausible CAC, and the outside evidence
   on the comparable population points that way.
8. **The celebrity CAC advantage is derived, not assumed.** Paid media is split into three tiers — branded
   and intent search, retargeting, and cold prospecting with partner creative. The partnership creates cheap
   warm inventory (branded search from post views, engagement audiences from post engagers) and discounts the
   cold tier through better creative. Both warm tiers carry an incrementality haircut, because holdout tests
   show only 25–30% of retargeting conversions are incremental. The like-for-like result is a **21–27% CAC
   advantage at equal spend**, largest on the first tranche of budget. Blended CAC still *rises* with spend in
   every scenario — that is the auction, and a model where it falls with scale has no competition in it.
9. **The partnership is worth more than it costs, on these assumptions.** Against an identical business with
   no partner: +$25.6M of 36-month revenue,
   +$5.7M of 36-month EBITDA, break-even
   22 months earlier,
   and $1.0M less capital, against
   $2.10M of illustrative partner cash. That conclusion rests on two unmeasured
   audience dials, and it assumes the partner's likeness can be licensed for *paid* media — organic posting
   rights and paid-usage rights are separate grants.
