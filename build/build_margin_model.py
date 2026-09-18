"""Build 09_ReserveClinic_Margin_and_Growth_Model.xlsx.

Purpose-built for the operating structure the project owner specified: a brand/commerce company
using a turnkey compliance-and-fulfilment provider at a flat $600/month, a non-prescription
supplement line that can trade in all fifty states, and a prescription telehealth line fulfilled
by 503A/503B pharmacies whose footprint expands state by state.

Conventions: blue = editable input, black = formula, green = cross-sheet link, yellow fill =
high-sensitivity driver. Every model cell is a formula; nothing is hard-coded into the monthly grid.
A pure-Python replica of the same arithmetic is written to build/margin_values.json for charting,
and check_margin_model.py reconciles it against the LibreOffice-recalculated workbook.
"""
import json, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment

OUT = sys.argv[1] if len(sys.argv) > 1 else "outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx"
MONTHS = 36
FONT = "Arial"
BLUE = Font(name=FONT, color="0000FF", size=10)
BLACK = Font(name=FONT, color="000000", size=10)
GREEN = Font(name=FONT, color="008000", size=10)
BOLD = Font(name=FONT, bold=True, size=10)
BOLDG = Font(name=FONT, bold=True, size=10, color="008000")
H1 = Font(name=FONT, bold=True, size=14)
H2 = Font(name=FONT, bold=True, size=11, color="FFFFFF")
SMALL = Font(name=FONT, size=9)
ITAL = Font(name=FONT, italic=True, size=9)
YELLOW = PatternFill("solid", fgColor="FFFF00")
HDR = PatternFill("solid", fgColor="1F3D33")
SUB = PatternFill("solid", fgColor="E8EFEA")
WARN = PatternFill("solid", fgColor="FDEBE7")
CUR = '$#,##0;($#,##0);-'
CUR2 = '$#,##0.00;($#,##0.00);-'
PCT = '0.0%'
PCT2 = '0.00%'
NUM = '#,##0;(#,##0);-'
DEC = '#,##0.00'

wb = Workbook()

# ================================================================= ASSUMPTIONS
# (key, label, unit, conservative, baseline, aggressive, rationale, confidence, sensitivity, validation)
A = [
 ("SECTION", "Timing and sequencing"),
 ("nonrx_launch", "Non-prescription line goes live (model month)", "month", 3, 2, 2,
  "Supplement line needs only manufacturing, label/claims review and a storefront. Conservative allows one month of slippage on label review.", "High", "Medium", "Phase exit checklist"),
 ("rx_launch", "Prescription telehealth line goes live (model month)", "month", 9, 7, 5,
  "Requires the provider agreement, physician entity, pharmacy contracts, LegitScript certification and a state-by-state licensure map. Benchmark B10, B11.", "Medium", "High", "Counsel and provider go-live sign-off"),
 ("SECTION", "Audience engine (the proposed brand partner's reach)"),
 ("followers", "Proposed brand partner Instagram followers", "#", 27400000, 27400000, 27400000,
  "Third-party trackers report 27,410,219 as of June 2026 (range 27.0M-28.3M). Benchmark B16. Held constant across scenarios because it is measured, not chosen. NOT an audited or first-party figure.", "Medium", "High", "First-party creator analytics export"),
 ("posts_per_month", "Brand posts per month by the partner (feed plus reels)", "#", 2, 4, 6,
  "A contract deliverable, not a market variable. Set to whatever the agreement actually obliges.", "n/a", "High", "Signed content schedule"),
 ("reach_pct", "Reach per brand post as a share of followers", "%", 0.04, 0.07, 0.11,
  "Analyst assumption bounded by benchmark B15: the 10M-plus tier averages ~1.77% ENGAGEMENT; reach exceeds engagement but organic reach at this tier is heavily throttled and branded content more so. Reels reach higher than static.", "Low", "High", "Creator-account reach data, first 60 days"),
 ("ctr_reach", "Click-through to site per reached impression", "%", 0.0035, 0.0060, 0.0090,
  "Analyst assumption. No tier-level link-click benchmark was retrievable (benchmark B15 notes this gap). This is the single least-evidenced driver in the model.", "Low", "High", "UTM-tagged link data, first 30 days"),
 ("attn_decay", "Monthly decay of partner-driven traffic toward a floor", "%", 0.72, 0.80, 0.86,
  "Analyst assumption. Celebrity launch demand spikes then settles; benchmark B14 notes IM8's founders deliberately did not rely on fame for durability.", "Low", "High", "Cohort traffic by source, monthly"),
 ("attn_floor", "Floor for partner-driven traffic as a share of the launch peak", "%", 0.28, 0.36, 0.45,
  "Analyst assumption. Represents the durable follower demand that persists after novelty.", "Low", "High", "Cohort traffic by source, monthly"),
 ("launch_spike", "Launch-month multiplier on partner-driven traffic", "x", 1.6, 2.2, 3.0,
  "Announcement window concentrates attention. Analyst assumption.", "Low", "Medium", "Launch-week analytics"),
 ("SECTION", "Other traffic"),
 ("organic_m1", "Organic and direct sessions, month 1", "sessions", 1200, 2200, 3500,
  "New domain with an editorial library. Analyst assumption.", "Low", "Low", "GA4 after month 1"),
 ("organic_growth", "Organic monthly growth rate", "%", 0.06, 0.09, 0.12,
  "Content-led SEO compounding from a small base. Analyst inference.", "Low", "Medium", "Search Console trend"),
 ("organic_cap", "Organic and direct sessions ceiling", "sessions", 90000, 180000, 320000,
  "Caps compounding; category search demand is finite. Analyst inference.", "Low", "Medium", "Search Console"),
 ("cps", "Cost per paid session, blended", "$", 2.60, 2.15, 1.85,
  "Health and wellness CPC proxies; restricted-category ad review raises cost. LegitScript certification is a precondition for scaled healthcare advertising (benchmark B10).", "Medium", "High", "Ad platform reports"),
 ("paid_pre", "Paid media per month before the non-Rx launch", "$", 4000, 8000, 15000,
  "Waitlist and audience building only.", "Medium", "Low", "Budget actuals"),
 ("paid_floor", "Minimum paid media per month after launch", "$", 10000, 30000, 60000,
  "Keeps a spend floor while revenue is small.", "Medium", "Medium", "Budget actuals"),
 ("paid_pct", "Paid media as a share of prior-month net revenue", "%", 0.30, 0.24, 0.20,
  "Benchmark B02: the closest listed telehealth comparable ran marketing at 35-40% of revenue. A celebrity-led brand should sit WELL below that, because the point of the partnership is that owned audience substitutes for bought audience; if this driver has to rise toward 35% the partnership is not working. Prior-month basis avoids a circular reference.", "Medium", "High", "Monthly payback review"),
 ("launch_push", "One-time launch marketing and PR, non-Rx launch month", "$", 40000, 150000, 400000,
  "Announcement window spend: PR, production, seeding, paid amplification. Concentrated in a single month by design.", "Medium", "Medium", "Agency scopes"),
 ("paid_cap", "Maximum paid media per month", "$", 200000, 900000, 2500000,
  "A budget ceiling and a reality check. Without one, a percent-of-revenue rule compounds without limit. At the Aggressive ceiling this is roughly 25-30% of revenue at scale, in line with benchmark B02.", "Medium", "High", "Board-approved budget"),
 ("paid_elast", "Paid response elasticity (sessions per marginal dollar)", "x", 0.68, 0.75, 0.82,
  "Diminishing returns. Sessions scale as (spend / floor) raised to this power, so at ten times the floor spend the effective cost per session rises about 1.8x at 0.75. Below 1.0 is the whole point: auction competition and audience exhaustion mean the second million never buys what the first did. Analyst assumption, standard media-mix practice.", "Low", "High", "Marginal CAC by spend decile"),
 ("SECTION", "Non-prescription line: funnel and pricing"),
 ("cap_m1", "Orders the supply chain can ship in the first live month", "#", 600, 1500, 3000,
  "Manufacturing minimum order quantities, batch lead times, label print runs and 3PL onboarding all gate the first months. Demand above this ceiling is treated as LOST, not backlogged, which is the conservative treatment. Analyst assumption; replace with the contract manufacturer's actual run schedule.", "Low", "High", "Manufacturer run schedule and 3PL onboarding plan"),
 ("cap_growth", "Monthly growth in shippable capacity", "x", 1.25, 1.35, 1.45,
  "How fast production and fulfilment can be scaled. Binds hard in the first year of the Aggressive case and stops binding thereafter. Analyst assumption.", "Low", "High", "Purchase-order lead times"),
 ("shop_conv", "Order conversion rate, all sessions", "%", 0.009, 0.014, 0.019,
  "DTC supplement conversion commonly 0.5-1.5%; a warm follower audience should sit at the top of or above that band, but benchmark B15 warns mega-tier audiences convert worse than their reach implies.", "Low", "High", "Shopify analytics"),
 ("nonrx_aov", "Average order value", "$", 68, 78, 88,
  "Above the $30-65 monthly band in benchmark B06, reflecting a premium multi-product basket. Requires validation.", "Medium", "High", "Shopify analytics"),
 ("sub_attach", "Share of new customers taking a subscription", "%", 0.30, 0.40, 0.50,
  "Subscribe-and-save attach on consumables. Analyst assumption.", "Low", "High", "Subscription app data"),
 ("sub_churn", "Monthly subscription churn", "%", 0.090, 0.070, 0.055,
  "Benchmark B05: 4-7% monthly well run, 8-12% category average, 12-20% churning in month one alone.", "Medium", "High", "Cohort analysis"),
 ("onetime_repeat", "Monthly reorder rate of one-time buyers", "%", 0.08, 0.11, 0.14,
  "Approximation: applied to the prior month's one-time cohort only, which understates a long tail and is deliberately conservative.", "Low", "Medium", "Cohort analysis"),
 ("SECTION", "Non-prescription line: cost of revenue"),
 ("nonrx_cogs_pct", "Landed product COGS as a share of retail", "%", 0.30, 0.26, 0.22,
  "Benchmark B03: landed COGS 20-30% of retail for DTC supplements, giving 70-80% product gross margin.", "Medium", "High", "Contract manufacturer quotes"),
 ("nonrx_fulfil", "Pick, pack and ship per order (ambient)", "$", 8.50, 7.50, 6.50,
  "3PL pick-pack plus domestic parcel. Ambient, not cold chain.", "Medium", "Low", "3PL quotes"),
 ("SECTION", "Prescription line: funnel"),
 ("rx_intent", "Eligibility-quiz start rate, all sessions", "%", 0.012, 0.018, 0.025,
  "Analyst assumption. Prescription intent is a small slice of brand traffic.", "Low", "High", "Analytics"),
 ("quiz_complete", "Quiz completion rate", "%", 0.60, 0.70, 0.76,
  "One-question-per-screen intake typically 55-75%.", "Medium", "Medium", "Analytics"),
 ("eligible_rate", "Share of completions with a clinically eligible outcome", "%", 0.50, 0.58, 0.64,
  "Red-flag screening removes a material share. Never a target; a safety control.", "Medium", "Medium", "Medical director audit"),
 ("state_cov_launch", "US population covered by served states at Rx launch", "%", 0.26, 0.36, 0.45,
  "Licensure, asynchronous-prescribing rules and corporate-practice-of-medicine limits gate this. Fifty-state prescription coverage is NOT available on day one.", "Medium", "High", "State readiness tracker"),
 ("state_cov_step", "Monthly increase in covered population", "%", 0.015, 0.025, 0.035,
  "Tranche-based state expansion.", "Medium", "Medium", "State readiness tracker"),
 ("state_cov_cap", "Maximum covered population", "%", 0.70, 0.82, 0.88,
  "Some states stay excluded on asynchronous or CPOM grounds.", "Medium", "Medium", "Counsel memo"),
 ("intake_submit", "Intake submission rate, eligible to intake", "%", 0.48, 0.56, 0.62,
  "Identity verification and consent friction.", "Medium", "High", "Analytics"),
 ("consult_complete", "Consult completion rate", "%", 0.76, 0.83, 0.88,
  "Asynchronous review completes above video.", "Medium", "Medium", "EHR data"),
 ("rx_rate", "Clinician prescribing rate", "%", 0.55, 0.62, 0.68,
  "A clinical decision, never a target. Observed telehealth ranges 50-70%. Monitored solely for safety and for evidence of undue influence.", "Low", "High", "Independent medical audit"),
 ("enroll_rate", "Paid enrolment rate after a prescription is issued", "%", 0.58, 0.66, 0.70,
  "Price friction at the plan step; all-in pricing shown before intake improves this.", "Medium", "High", "Analytics"),
 ("rx_churn", "Monthly churn, prescription programmes", "%", 0.130, 0.110, 0.095,
  "Benchmark B17: ~65% discontinuation within 12 months in the comparable telehealth population, 84.4% by 24 months. THE most damaging driver if wrong.", "Medium", "High", "Cohort analysis, monthly"),
 ("SECTION", "Prescription line: pricing"),
 ("rx_price", "Programme price per member-month, blended", "$", 199, 249, 299,
  "Benchmark B07: sermorelin $96-199 telehealth, tissue protocols $100-300, stacks $80-180, combinations $350-600.", "Medium", "High", "Van Westendorp plus live price tests"),
 ("consult_fee", "Consultation fee charged at intake", "$", 49, 59, 79,
  "Benchmark B08: asynchronous visits price at $15-40 commonly, up to $60 for longer reviews. Charged whether or not a prescription follows; refunded if screened ineligible.", "Medium", "Medium", "Pricing test"),
 ("SECTION", "Prescription line: cost of revenue"),
 ("pharm_cost", "Pharmacy medication cost per member-month", "$", 105, 88, 75,
  "503A compounded peptide cost to a telehealth sponsor, volume-tiered. Not independently verified; obtain a written tiered schedule.", "Low", "High", "Pharmacy contract schedule"),
 ("consult_cost", "Clinician cost per completed consult", "$", 45, 38, 32,
  "Benchmark B08 cites provider time around $30 per programme plus platform and support. One-time at enrolment.", "Medium", "Medium", "Provider network contract"),
 ("refill_cost", "Clinician cost per active member-month (monitoring and refill review)", "$", 10.00, 8.00, 6.50,
  "Recurring clinical review. Must be paid per unit of clinical work, never as a share of revenue.", "Medium", "Medium", "Provider network contract"),
 ("coldchain_ship", "Cold-chain fulfilment and shipping per fill", "$", 22, 18, 15,
  "Benchmark B09: $1.95 base pack rate plus cold storage, insulated mailers, gel packs and a 2-day temperature-controlled lane. The pack rate alone is NOT the landed cost.", "Medium", "High", "Pharmacy and carrier quotes"),
 ("rx_support", "Non-clinical support cost per active member-month", "$", 6.00, 4.50, 3.50,
  "Tooling plus staffed support per member.", "Medium", "Low", "Support actuals"),
 ("SECTION", "Shared cost of revenue"),
 ("pay_fee", "Payment processing", "%", 0.032, 0.029, 0.027,
  "Card fees 2.7-3.2%. Healthcare and supplement merchants are frequently underwritten as elevated risk, which raises the rate and makes LegitScript certification close to a prerequisite (benchmark B10).", "High", "Medium", "Processor statements"),
 ("refund_pct", "Refunds and chargebacks", "%", 0.040, 0.030, 0.022,
  "2-5% typical. Auto-renewal programmes attract chargebacks; ROSCA-compliant cancellation reduces them.", "Medium", "Medium", "Finance actuals"),
 ("SECTION", "Operating expenses"),
 ("provider_fee", "Turnkey compliance and fulfilment provider, flat fee", "$", 600, 600, 600,
  "As specified by the project owner. Modelled as a PLATFORM fee only. Published market pricing for comparable turnkey telehealth infrastructure is $3,000-6,000/month plus $5,000-10,000 onboarding plus per-consult fees (benchmark B11), so a $600 fee is very unlikely to absorb medication, per-consult, cold-chain or processing costs. Those are carried separately above. See the Provider_Diligence sheet.", "Low", "Medium", "Executed agreement and fee schedule"),
 ("cert_cost", "Certification and registrations per month", "$", 320, 280, 260,
  "Benchmark B10: ~$3,125 year one and ~$2,150/yr thereafter per site for LegitScript, plus state registrations and renewals; amortised monthly.", "Medium", "Low", "Live fee schedule"),
 ("team_pre", "Team per month before the non-Rx launch", "$", 8000, 18000, 25000,
  "Founder or GM plus fractional operations and contract creative. Small because the provider carries clinical and fulfilment operations. The Conservative column is deliberately a LEAN operator, not a normal operator with weak demand, so that the Conservative outcome reflects demand risk rather than an arbitrary spending choice.", "Medium", "Medium", "Hiring plan"),
 ("team_p1", "Team per month, non-Rx launch through month 12", "$", 16000, 45000, 70000,
  "Adds brand, retention, support oversight and a compliance lead.", "Medium", "Medium", "Hiring plan"),
 ("team_p2", "Team per month, months 13-24", "$", 24000, 62000, 140000,
  "Scales with order volume and state count, but stays small relative to revenue because the provider carries clinical operations and fulfilment. A brand at this revenue running team above roughly 15% of net revenue has rebuilt in-house what it is already paying the provider for.", "Low", "Medium", "Hiring plan"),
 ("team_p3", "Team per month, months 25-36", "$", 32000, 92000, 230000,
  "", "Low", "Medium", "Hiring plan"),
 ("med_lead", "Medical director and clinical oversight per month", "$", 5000, 9000, 14000,
  "Fractional medical director retainer. Compensation must never vary with prescription volume or revenue.", "Medium", "Low", "Executed agreement"),
 ("tech", "Technology and software per month", "$", 1500, 2500, 4000,
  "Storefront, subscription management, analytics, consent management, CRM, helpdesk. Separate from the provider fee.", "High", "Low", "Vendor invoices"),
 ("legal_p0", "Legal and regulatory per month, months 1-4", "$", 14000, 25000, 32000,
  "Entity structure and MSO or friendly-PC review, provider agreement review, formulary eligibility opinion, claims and label review, endorsement and disclosure protocol, trademark, privacy. Front-loaded deliberately.", "Medium", "Low", "Counsel estimates"),
 ("legal_ongoing", "Legal and compliance per month thereafter", "$", 4000, 9000, 12000,
  "Ongoing claims review, state expansion opinions, FDA list monitoring, contract maintenance.", "Medium", "Medium", "Counsel estimates"),
 ("insurance", "Insurance per month from the non-Rx launch", "$", 2000, 3500, 5000,
  "Product liability, professional, cyber and D&O. A vendor contract does not transfer the brand's own liability.", "Medium", "Low", "Broker quotes"),
 ("creative", "Creative, content and organic social per month", "$", 4500, 12000, 26000,
  "Production the brand controls, distinct from paid media and from partner compensation.", "Medium", "Medium", "Agency quotes"),
 ("SECTION", "Proposed brand-partner economics (hypothetical; no terms offered or accepted)"),
 ("partner_cash", "Partner cash retainer per month from the non-Rx launch", "$", 0, 15000, 25000,
  "Illustrative only. Structure, amount and mix are entirely unnegotiated. Conservative case models an equity-only deal with no cash retainer.", "n/a", "High", "Negotiation"),
 ("partner_royalty", "Partner royalty on net revenue", "%", 0.050, 0.050, 0.050,
  "Illustrative. Consumer-brand licensing royalties commonly 3-10%. Held flat across scenarios so the scenarios isolate business performance rather than deal terms.", "n/a", "High", "Negotiation"),
 ("partner_equity", "Partner equity, fully diluted (reference only)", "%", 0.10, 0.15, 0.20,
  "Illustrative. Non-cash; shown on the Partner_Economics sheet for reference and NOT charged to EBITDA.", "n/a", "n/a", "Negotiation"),
 ("SECTION", "Working capital"),
 ("inv_months", "Non-Rx inventory held, in months of COGS", "months", 2.5, 2.0, 2.0,
  "Supplement manufacturing runs have long lead times and minimum order quantities, so inventory is the main working-capital draw. The Rx line carries no inventory; the pharmacy does.", "Medium", "Medium", "Purchase orders"),
]

ws = wb.active; ws.title = "Assumptions"
ws["A1"] = "Reserve Clinic - Margin and Growth Model: Assumptions"; ws["A1"].font = H1
ws["A2"] = ("Blue cells are the only inputs. Three scenario columns drive Model_Conservative, Model_Baseline and Model_Aggressive. "
            "Yellow fill marks high-sensitivity drivers. Prepared 2026-09-18. Proposed concept: the brand partner's and the medical "
            "co-founder's participation is unverified and subject to definitive agreements. Not legal, medical, tax or investment advice.")
ws["A2"].font = ITAL
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:J2"); ws.row_dimensions[2].height = 42
hdrs = ["Key", "Driver", "Unit", "Conservative", "Baseline", "Aggressive", "Rationale / source", "Confidence", "Sensitivity", "Validation method"]
for i, h in enumerate(hdrs, 1):
    c = ws.cell(row=4, column=i, value=h); c.font = H2; c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="bottom")
ROW = {}
VAL = {}
r = 5
for item in A:
    if item[0] == "SECTION":
        c = ws.cell(row=r, column=1, value=item[1]); c.font = BOLD
        for col in range(1, 11): ws.cell(row=r, column=col).fill = SUB
        r += 1; continue
    key, label, unit, cons, base, up, rat, conf, sens, valm = item
    ws.cell(row=r, column=1, value=key).font = Font(name=FONT, size=8, color="777777")
    ws.cell(row=r, column=2, value=label).font = BLACK
    ws.cell(row=r, column=3, value=unit).font = BLACK
    for col, v in zip((4, 5, 6), (cons, base, up)):
        c = ws.cell(row=r, column=col, value=v); c.font = BLUE
        c.number_format = (PCT2 if unit == "%" and abs(float(v)) < 0.02 else PCT) if unit == "%" else (
            (CUR2 if unit == "$" and float(v) != int(float(v)) else CUR) if unit == "$" else (
                DEC if unit == "x" else ('0.0' if unit == "months" else NUM)))
        if sens == "High": c.fill = YELLOW
    cc = ws.cell(row=r, column=7, value=rat); cc.font = SMALL; cc.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=r, column=8, value=conf).font = BLACK
    ws.cell(row=r, column=9, value=sens).font = BLACK
    vc = ws.cell(row=r, column=10, value=valm); vc.font = SMALL; vc.alignment = Alignment(wrap_text=True, vertical="top")
    ROW[key] = r
    VAL[key] = {"Conservative": cons, "Baseline": base, "Aggressive": up}
    r += 1
for col, w in zip("ABCDEFGHIJ", (17, 56, 10, 14, 14, 14, 78, 12, 12, 30)):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "D5"
ws.sheet_view.zoomScale = 90

SCN = {"Conservative": "D", "Baseline": "E", "Aggressive": "F"}

# ================================================================= MONTHLY MODEL
R = {}
ORDER = []

def build_model(name, col):
    """col is the Assumptions scenario column letter."""
    sh = wb.create_sheet(f"Model_{name}")
    sh["A1"] = f"Reserve Clinic - {name} scenario, months 1-36"; sh["A1"].font = H1
    sh["A2"] = "Every cell is a formula. Inputs live on Assumptions only. Green = link to Assumptions."; sh["A2"].font = ITAL
    sh["A4"] = "Line"; sh["B4"] = "Unit"; sh["A4"].font = H2; sh["B4"].font = H2
    sh["A4"].fill = HDR; sh["B4"].fill = HDR
    sh.cell(row=4, column=MONTHS + 3, value="Total / final").font = H2
    sh.cell(row=4, column=MONTHS + 3).fill = HDR
    for m in range(1, MONTHS + 1):
        c = sh.cell(row=4, column=2 + m, value=f"M{m}"); c.font = H2; c.fill = HDR; c.alignment = Alignment(horizontal="center")
    # row 5: month index, row 6: year
    sh["A5"] = "Month index"; sh["B5"] = "#"
    sh["A6"] = "Year"; sh["B6"] = "#"
    for m in range(1, MONTHS + 1):
        sh.cell(row=5, column=2 + m, value=m).font = BLACK
        sh.cell(row=6, column=2 + m, value=f"=ROUNDUP({L(2+m)}$5/12,0)").font = BLACK
    return sh

def A_(col, key):
    return f"Assumptions!${col}${ROW[key]}"

def ref(sh_row_key, colletter):
    return f"{colletter}{R[sh_row_key]}"

def make_lines():
    """Definition list shared by all three scenario sheets.
    Each entry: (key, label, unit, formula_fn, number_format, aggregate)
    formula_fn(m, c, p) where m is month number, c current col letter, p previous col letter or None.
    aggregate: 'sum', 'last', 'avg', or None."""
    Lz = []
    def add(key, label, unit, fn, fmt=CUR, agg="sum", bold=False):
        Lz.append((key, label, unit, fn, fmt, agg, bold))
    # ---- flags
    add("is_nonrx", "Non-Rx line live (1/0)", "flag",
        lambda m, c, p, a: f"IF({c}$5>={a('nonrx_launch')},1,0)", '0', None)
    add("is_rx", "Rx line live (1/0)", "flag",
        lambda m, c, p, a: f"IF({c}$5>={a('rx_launch')},1,0)", '0', None)
    add("months_live", "Months since non-Rx launch", "#",
        lambda m, c, p, a: f"MAX(0,{c}$5-{a('nonrx_launch')})", '0', None)
    # ---- audience engine
    add("partner_peak", "Partner-driven sessions at launch peak", "sessions",
        lambda m, c, p, a: f"{a('followers')}*{a('posts_per_month')}*{a('reach_pct')}*{a('ctr_reach')}", NUM, None)
    add("attn_index", "Attention index (decay toward floor)", "x",
        lambda m, c, p, a: (f"IF({ref('is_nonrx',c)}=0,0,IF({ref('months_live',c)}=0,{a('launch_spike')},"
                            f"{a('attn_floor')}+(1-{a('attn_floor')})*{a('attn_decay')}^{ref('months_live',c)}))"), DEC, None)
    add("partner_sessions", "Partner-driven sessions", "sessions",
        lambda m, c, p, a: f"{ref('partner_peak',c)}*{ref('attn_index',c)}", NUM, "sum")
    add("organic_sessions", "Organic and direct sessions", "sessions",
        lambda m, c, p, a: f"MIN({a('organic_cap')},{a('organic_m1')}*(1+{a('organic_growth')})^({c}$5-1))", NUM, "sum")
    add("paid_spend", "Paid media spend", "$",
        lambda m, c, p, a: (f"{a('paid_pre')}" if p is None else
                            f"IF({ref('is_nonrx',c)}=0,{a('paid_pre')},MIN({a('paid_cap')},MAX({a('paid_floor')},{ref('net_rev',p)}*{a('paid_pct')})))"), CUR, "sum")
    add("paid_sessions", "Paid sessions (diminishing returns applied)", "sessions",
        lambda m, c, p, a: (f"({a('paid_floor')}/{a('cps')})*({ref('paid_spend',c)}/{a('paid_floor')})^{a('paid_elast')}"), NUM, "sum")
    add("eff_cps", "Effective cost per paid session", "$",
        lambda m, c, p, a: f"IFERROR({ref('paid_spend',c)}/{ref('paid_sessions',c)},0)", CUR2, "avg")
    add("sessions", "Total sessions", "sessions",
        lambda m, c, p, a: f"{ref('partner_sessions',c)}+{ref('organic_sessions',c)}+{ref('paid_sessions',c)}", NUM, "sum", True)
    # ---- non-Rx funnel
    add("nonrx_capacity", "Shippable new-order capacity", "#",
        lambda m, c, p, a: f"{ref('is_nonrx',c)}*{a('cap_m1')}*{a('cap_growth')}^{ref('months_live',c)}", NUM, "last")
    add("nonrx_demand", "New non-Rx customer demand", "#",
        lambda m, c, p, a: f"{ref('sessions',c)}*{a('shop_conv')}*{ref('is_nonrx',c)}", NUM, "sum")
    add("nonrx_new_cust", "New non-Rx customers served", "#",
        lambda m, c, p, a: f"MIN({ref('nonrx_demand',c)},{ref('nonrx_capacity',c)})", NUM, "sum", True)
    add("nonrx_lost", "Demand lost to capacity", "#",
        lambda m, c, p, a: f"MAX(0,{ref('nonrx_demand',c)}-{ref('nonrx_capacity',c)})", NUM, "sum")
    add("nonrx_new_subs", "New subscribers", "#",
        lambda m, c, p, a: f"{ref('nonrx_new_cust',c)}*{a('sub_attach')}", NUM, "sum")
    add("nonrx_new_onetime", "New one-time buyers", "#",
        lambda m, c, p, a: f"{ref('nonrx_new_cust',c)}*(1-{a('sub_attach')})", NUM, "sum")
    add("nonrx_subs_active", "Active subscribers (end of month)", "#",
        lambda m, c, p, a: (f"{ref('nonrx_new_subs',c)}" if p is None else
                            f"{ref('nonrx_subs_active',p)}*(1-{a('sub_churn')})+{ref('nonrx_new_subs',c)}"), NUM, "last", True)
    add("nonrx_subs_churned", "Subscribers churned", "#",
        lambda m, c, p, a: ("0" if p is None else f"{ref('nonrx_subs_active',p)}*{a('sub_churn')}"), NUM, "sum")
    add("nonrx_repeat_orders", "Repeat orders from one-time buyers", "#",
        lambda m, c, p, a: ("0" if p is None else f"{ref('nonrx_new_onetime',p)}*{a('onetime_repeat')}"), NUM, "sum")
    add("nonrx_orders", "Non-Rx orders shipped", "#",
        lambda m, c, p, a: f"{ref('nonrx_new_onetime',c)}+{ref('nonrx_subs_active',c)}+{ref('nonrx_repeat_orders',c)}", NUM, "sum", True)
    add("nonrx_rev_gross", "Non-Rx gross revenue", "$",
        lambda m, c, p, a: f"{ref('nonrx_orders',c)}*{a('nonrx_aov')}", CUR, "sum")
    add("nonrx_refunds", "Non-Rx refunds and chargebacks", "$",
        lambda m, c, p, a: f"-{ref('nonrx_rev_gross',c)}*{a('refund_pct')}", CUR, "sum")
    add("nonrx_rev_net", "Non-Rx net revenue", "$",
        lambda m, c, p, a: f"{ref('nonrx_rev_gross',c)}+{ref('nonrx_refunds',c)}", CUR, "sum", True)
    add("nonrx_cogs", "Non-Rx product COGS", "$",
        lambda m, c, p, a: f"-{ref('nonrx_rev_gross',c)}*{a('nonrx_cogs_pct')}", CUR, "sum")
    add("nonrx_fulfil_c", "Non-Rx pick, pack and ship", "$",
        lambda m, c, p, a: f"-{ref('nonrx_orders',c)}*{a('nonrx_fulfil')}", CUR, "sum")
    add("nonrx_proc", "Non-Rx payment processing", "$",
        lambda m, c, p, a: f"-{ref('nonrx_rev_net',c)}*{a('pay_fee')}", CUR, "sum")
    add("nonrx_gp", "Non-Rx gross profit", "$",
        lambda m, c, p, a: f"{ref('nonrx_rev_net',c)}+{ref('nonrx_cogs',c)}+{ref('nonrx_fulfil_c',c)}+{ref('nonrx_proc',c)}", CUR, "sum", True)
    add("nonrx_gm", "Non-Rx gross margin", "%",
        lambda m, c, p, a: f"IFERROR({ref('nonrx_gp',c)}/{ref('nonrx_rev_net',c)},0)", PCT, "avg")
    # ---- Rx funnel
    add("state_cov", "US population covered by served states", "%",
        lambda m, c, p, a: (f"IF({ref('is_rx',c)}=0,0,MIN({a('state_cov_cap')},"
                            f"{a('state_cov_launch')}+{a('state_cov_step')}*({c}$5-{a('rx_launch')})))"), PCT, "last")
    add("rx_quiz_starts", "Eligibility quiz starts", "#",
        lambda m, c, p, a: f"{ref('sessions',c)}*{a('rx_intent')}*{ref('is_rx',c)}", NUM, "sum")
    add("rx_quiz_completes", "Quiz completions", "#",
        lambda m, c, p, a: f"{ref('rx_quiz_starts',c)}*{a('quiz_complete')}", NUM, "sum")
    add("rx_eligible", "Eligible outcomes (clinical screen and state)", "#",
        lambda m, c, p, a: f"{ref('rx_quiz_completes',c)}*{a('eligible_rate')}*{ref('state_cov',c)}", NUM, "sum")
    add("rx_intakes", "Intakes submitted (consult fee charged)", "#",
        lambda m, c, p, a: f"{ref('rx_eligible',c)}*{a('intake_submit')}", NUM, "sum")
    add("rx_consults", "Consults completed", "#",
        lambda m, c, p, a: f"{ref('rx_intakes',c)}*{a('consult_complete')}", NUM, "sum")
    add("rx_prescribed", "Prescriptions issued (clinician decision)", "#",
        lambda m, c, p, a: f"{ref('rx_consults',c)}*{a('rx_rate')}", NUM, "sum")
    add("rx_new", "New paying programme members", "#",
        lambda m, c, p, a: f"{ref('rx_prescribed',c)}*{a('enroll_rate')}", NUM, "sum")
    add("rx_active", "Active programme members (end of month)", "#",
        lambda m, c, p, a: (f"{ref('rx_new',c)}" if p is None else
                            f"{ref('rx_active',p)}*(1-{a('rx_churn')})+{ref('rx_new',c)}"), NUM, "last", True)
    add("rx_churned", "Programme members churned", "#",
        lambda m, c, p, a: ("0" if p is None else f"{ref('rx_active',p)}*{a('rx_churn')}"), NUM, "sum")
    add("rx_prog_rev", "Programme subscription revenue", "$",
        lambda m, c, p, a: f"{ref('rx_active',c)}*{a('rx_price')}", CUR, "sum")
    add("rx_consult_rev", "Consultation fee revenue", "$",
        lambda m, c, p, a: f"{ref('rx_intakes',c)}*{a('consult_fee')}", CUR, "sum")
    add("rx_rev_gross", "Rx gross revenue", "$",
        lambda m, c, p, a: f"{ref('rx_prog_rev',c)}+{ref('rx_consult_rev',c)}", CUR, "sum")
    add("rx_refunds", "Rx refunds and chargebacks", "$",
        lambda m, c, p, a: f"-{ref('rx_rev_gross',c)}*{a('refund_pct')}", CUR, "sum")
    add("rx_rev_net", "Rx net revenue", "$",
        lambda m, c, p, a: f"{ref('rx_rev_gross',c)}+{ref('rx_refunds',c)}", CUR, "sum", True)
    add("rx_pharm", "Pharmacy medication cost", "$",
        lambda m, c, p, a: f"-{ref('rx_active',c)}*{a('pharm_cost')}", CUR, "sum")
    add("rx_clin_new", "Clinician cost, new consults", "$",
        lambda m, c, p, a: f"-{ref('rx_consults',c)}*{a('consult_cost')}", CUR, "sum")
    add("rx_clin_refill", "Clinician cost, monitoring and refills", "$",
        lambda m, c, p, a: f"-{ref('rx_active',c)}*{a('refill_cost')}", CUR, "sum")
    add("rx_ship", "Cold-chain fulfilment and shipping", "$",
        lambda m, c, p, a: f"-{ref('rx_active',c)}*{a('coldchain_ship')}", CUR, "sum")
    add("rx_supp", "Rx support cost", "$",
        lambda m, c, p, a: f"-{ref('rx_active',c)}*{a('rx_support')}", CUR, "sum")
    add("rx_proc", "Rx payment processing", "$",
        lambda m, c, p, a: f"-{ref('rx_rev_net',c)}*{a('pay_fee')}", CUR, "sum")
    add("rx_gp", "Rx gross profit", "$",
        lambda m, c, p, a: ("+".join([ref('rx_rev_net', c), ref('rx_pharm', c), ref('rx_clin_new', c),
                                      ref('rx_clin_refill', c), ref('rx_ship', c), ref('rx_supp', c), ref('rx_proc', c)])), CUR, "sum", True)
    add("rx_gm", "Rx gross margin", "%",
        lambda m, c, p, a: f"IFERROR({ref('rx_gp',c)}/{ref('rx_rev_net',c)},0)", PCT, "avg")
    # ---- totals
    add("net_rev", "TOTAL NET REVENUE", "$",
        lambda m, c, p, a: f"{ref('nonrx_rev_net',c)}+{ref('rx_rev_net',c)}", CUR, "sum", True)
    add("gross_profit", "TOTAL GROSS PROFIT", "$",
        lambda m, c, p, a: f"{ref('nonrx_gp',c)}+{ref('rx_gp',c)}", CUR, "sum", True)
    add("gross_margin", "Blended gross margin", "%",
        lambda m, c, p, a: f"IFERROR({ref('gross_profit',c)}/{ref('net_rev',c)},0)", PCT, "avg", True)
    # ---- opex
    add("ox_provider", "Provider flat fee", "$",
        lambda m, c, p, a: f"-{a('provider_fee')}", CUR, "sum")
    add("ox_cert", "Certification and registrations", "$",
        lambda m, c, p, a: f"-{a('cert_cost')}", CUR, "sum")
    add("ox_team", "Team", "$",
        lambda m, c, p, a: (f"-IF({ref('is_nonrx',c)}=0,{a('team_pre')},IF({c}$5<=12,{a('team_p1')},"
                            f"IF({c}$5<=24,{a('team_p2')},{a('team_p3')})))"), CUR, "sum")
    add("ox_med", "Medical director and clinical oversight", "$",
        lambda m, c, p, a: f"-IF({c}$5>={a('rx_launch')}-2,{a('med_lead')},0)", CUR, "sum")
    add("ox_tech", "Technology and software", "$",
        lambda m, c, p, a: f"-{a('tech')}", CUR, "sum")
    add("ox_legal", "Legal, regulatory and compliance", "$",
        lambda m, c, p, a: f"-IF({c}$5<=4,{a('legal_p0')},{a('legal_ongoing')})", CUR, "sum")
    add("ox_ins", "Insurance", "$",
        lambda m, c, p, a: f"-{ref('is_nonrx',c)}*{a('insurance')}", CUR, "sum")
    add("ox_creative", "Creative and content", "$",
        lambda m, c, p, a: f"-{a('creative')}", CUR, "sum")
    add("ox_paid", "Paid media", "$",
        lambda m, c, p, a: f"-{ref('paid_spend',c)}", CUR, "sum")
    add("ox_launch", "One-time launch marketing and PR", "$",
        lambda m, c, p, a: f"-IF({c}$5={a('nonrx_launch')},{a('launch_push')},0)", CUR, "sum")
    add("ox_partner_cash", "Partner cash retainer", "$",
        lambda m, c, p, a: f"-{ref('is_nonrx',c)}*{a('partner_cash')}", CUR, "sum")
    add("ox_partner_roy", "Partner royalty on net revenue", "$",
        lambda m, c, p, a: f"-{ref('net_rev',c)}*{a('partner_royalty')}", CUR, "sum")
    add("total_opex", "TOTAL OPERATING EXPENSE", "$",
        lambda m, c, p, a: "+".join(ref(k, c) for k in ("ox_provider", "ox_cert", "ox_team", "ox_med", "ox_tech",
                                                        "ox_legal", "ox_ins", "ox_creative", "ox_paid", "ox_launch",
                                                        "ox_partner_cash", "ox_partner_roy")), CUR, "sum", True)
    add("ebitda", "EBITDA", "$",
        lambda m, c, p, a: f"{ref('gross_profit',c)}+{ref('total_opex',c)}", CUR, "sum", True)
    add("ebitda_margin", "EBITDA margin", "%",
        lambda m, c, p, a: f"IFERROR({ref('ebitda',c)}/{ref('net_rev',c)},0)", PCT, "avg", True)
    # ---- cash
    add("inv_balance", "Non-Rx inventory balance", "$",
        lambda m, c, p, a: f"-{ref('nonrx_cogs',c)}*{a('inv_months')}", CUR, "last")
    add("inv_invest", "Inventory investment (increase in stock)", "$",
        lambda m, c, p, a: (f"-{ref('inv_balance',c)}" if p is None else
                            f"-({ref('inv_balance',c)}-{ref('inv_balance',p)})"), CUR, "sum")
    add("net_cash", "Net cash flow", "$",
        lambda m, c, p, a: f"{ref('ebitda',c)}+{ref('inv_invest',c)}", CUR, "sum")
    add("cum_cash", "Cumulative cash flow", "$",
        lambda m, c, p, a: (f"{ref('net_cash',c)}" if p is None else f"{ref('cum_cash',p)}+{ref('net_cash',c)}"), CUR, "last", True)
    add("be_helper", "Break-even helper (month if EBITDA positive, else 999)", "#",
        lambda m, c, p, a: f"IF({ref('ebitda',c)}>0,{c}$5,999)", '0', None)
    # ---- efficiency
    add("new_cust_all", "New customers, both lines", "#",
        lambda m, c, p, a: f"{ref('nonrx_new_cust',c)}+{ref('rx_new',c)}", NUM, "sum")
    add("cac_blended", "Blended CAC (paid media plus creative)", "$",
        lambda m, c, p, a: f"IFERROR(({ref('paid_spend',c)}-{ref('ox_creative',c)})/{ref('new_cust_all',c)},0)", CUR2, "avg", True)
    add("rx_contrib_mm", "Rx contribution per member-month, steady state", "$",
        lambda m, c, p, a: (f"{a('rx_price')}*(1-{a('refund_pct')})*(1-{a('pay_fee')})-{a('pharm_cost')}"
                            f"-{a('refill_cost')}-{a('coldchain_ship')}-{a('rx_support')}"), CUR2, "avg")
    add("rx_ltv", "Rx gross LTV (contribution / churn)", "$",
        lambda m, c, p, a: f"{ref('rx_contrib_mm',c)}/{a('rx_churn')}", CUR, "avg")
    add("nonrx_contrib_order", "Non-Rx contribution per order", "$",
        lambda m, c, p, a: (f"{a('nonrx_aov')}*(1-{a('refund_pct')})*(1-{a('pay_fee')})"
                            f"-{a('nonrx_aov')}*{a('nonrx_cogs_pct')}-{a('nonrx_fulfil')}"), CUR2, "avg")
    add("nonrx_ltv", "Non-Rx subscriber gross LTV", "$",
        lambda m, c, p, a: f"{ref('nonrx_contrib_order',c)}/{a('sub_churn')}", CUR, "avg")
    return Lz

LINES = make_lines()
for i, (key, *_rest) in enumerate(LINES):
    R[key] = 8 + i
    ORDER.append(key)

for name, acol in SCN.items():
    sh = build_model(name, acol)
    a = lambda k, _c=acol: A_(_c, k)
    for key, label, unit, fn, fmt, agg, bold in LINES:
        row = R[key]
        lc = sh.cell(row=row, column=1, value=label); lc.font = BOLD if bold else BLACK
        sh.cell(row=row, column=2, value=unit).font = Font(name=FONT, size=8, color="777777")
        for m in range(1, MONTHS + 1):
            c = L(2 + m); p = L(1 + m) if m > 1 else None
            cell = sh.cell(row=row, column=2 + m, value="=" + fn(m, c, p, a))
            cell.number_format = fmt
            cell.font = BOLD if bold else BLACK
        tc = sh.cell(row=row, column=MONTHS + 3)
        rng = f"{L(3)}{row}:{L(MONTHS+2)}{row}"
        if agg == "sum": tc.value = f"=SUM({rng})"
        elif agg == "last": tc.value = f"={L(MONTHS+2)}{row}"
        elif agg == "avg": tc.value = f"=AVERAGE({L(3+11)}{row}:{L(MONTHS+2)}{row})"
        else: tc.value = None
        tc.number_format = fmt; tc.font = BOLD if bold else BLACK
    sh.column_dimensions["A"].width = 46
    sh.column_dimensions["B"].width = 9
    for m in range(1, MONTHS + 1): sh.column_dimensions[L(2 + m)].width = 12
    sh.column_dimensions[L(MONTHS + 3)].width = 15
    sh.freeze_panes = "C8"
    sh.sheet_view.zoomScale = 80

# ================================================================= SUMMARY
sm = wb.create_sheet("Summary", 1)
sm["A1"] = "Reserve Clinic - Margin and Growth Summary"; sm["A1"].font = H1
sm["A2"] = ("All figures are model outputs, not forecasts. They follow arithmetically from the drivers on Assumptions. "
            "Read them as a band produced by a stated set of assumptions, each of which is listed with its confidence and "
            "its validation method. Proposed concept; partner participation unverified.")
sm["A2"].font = ITAL; sm["A2"].alignment = Alignment(wrap_text=True, vertical="top")
sm.merge_cells("A2:E2"); sm.row_dimensions[2].height = 44

def mrange(scn, key, y):
    c0 = L(3 + (y - 1) * 12); c1 = L(2 + y * 12)
    return f"Model_{scn}!{c0}{R[key]}:{c1}{R[key]}"

metrics = [
 ("Net revenue, year 1", lambda s: f"=SUM({mrange(s,'net_rev',1)})", CUR),
 ("Net revenue, year 2", lambda s: f"=SUM({mrange(s,'net_rev',2)})", CUR),
 ("Net revenue, year 3", lambda s: f"=SUM({mrange(s,'net_rev',3)})", CUR),
 ("Net revenue, 36-month total", lambda s: f"=SUM(Model_{s}!{L(3)}{R['net_rev']}:{L(MONTHS+2)}{R['net_rev']})", CUR),
 ("SPACER", None, None),
 ("Gross profit, year 3", lambda s: f"=SUM({mrange(s,'gross_profit',3)})", CUR),
 ("Blended gross margin, year 1", lambda s: f"=IFERROR(SUM({mrange(s,'gross_profit',1)})/SUM({mrange(s,'net_rev',1)}),0)", PCT),
 ("Blended gross margin, year 3", lambda s: f"=IFERROR(SUM({mrange(s,'gross_profit',3)})/SUM({mrange(s,'net_rev',3)}),0)", PCT),
 ("Non-Rx gross margin, year 3", lambda s: f"=IFERROR(SUM({mrange(s,'nonrx_gp',3)})/SUM({mrange(s,'nonrx_rev_net',3)}),0)", PCT),
 ("Rx gross margin, year 3", lambda s: f"=IFERROR(SUM({mrange(s,'rx_gp',3)})/SUM({mrange(s,'rx_rev_net',3)}),0)", PCT),
 ("SPACER", None, None),
 ("EBITDA, year 1", lambda s: f"=SUM({mrange(s,'ebitda',1)})", CUR),
 ("EBITDA, year 2", lambda s: f"=SUM({mrange(s,'ebitda',2)})", CUR),
 ("EBITDA, year 3", lambda s: f"=SUM({mrange(s,'ebitda',3)})", CUR),
 ("EBITDA margin, year 3", lambda s: f"=IFERROR(SUM({mrange(s,'ebitda',3)})/SUM({mrange(s,'net_rev',3)}),0)", PCT),
 ("EBITDA, 36-month total", lambda s: f"=SUM(Model_{s}!{L(3)}{R['ebitda']}:{L(MONTHS+2)}{R['ebitda']})", CUR),
 ("SPACER", None, None),
 ("First EBITDA-positive month", lambda s: (f"=IF(MIN(Model_{s}!{L(3)}{R['be_helper']}:{L(MONTHS+2)}{R['be_helper']})=999,"
                                            f"\"Not within 36 months\",MIN(Model_{s}!{L(3)}{R['be_helper']}:{L(MONTHS+2)}{R['be_helper']}))"), '0'),
 ("Peak cumulative cash deficit", lambda s: f"=MIN(0,MIN(Model_{s}!{L(3)}{R['cum_cash']}:{L(MONTHS+2)}{R['cum_cash']}))", CUR),
 ("Capital required (deficit plus 30% buffer)", lambda s: f"=-MIN(0,MIN(Model_{s}!{L(3)}{R['cum_cash']}:{L(MONTHS+2)}{R['cum_cash']}))*1.3", CUR),
 ("Cumulative cash at month 36", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['cum_cash']}", CUR),
 ("SPACER", None, None),
 ("Active subscribers at month 36 (non-Rx)", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['nonrx_subs_active']}", NUM),
 ("Active programme members at month 36 (Rx)", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['rx_active']}", NUM),
 ("Non-Rx share of year-3 net revenue", lambda s: f"=IFERROR(SUM({mrange(s,'nonrx_rev_net',3)})/SUM({mrange(s,'net_rev',3)}),0)", PCT),
 ("SPACER", None, None),
 ("Rx contribution per member-month", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['rx_contrib_mm']}", CUR2),
 ("Rx gross LTV", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['rx_ltv']}", CUR),
 ("Non-Rx contribution per order", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['nonrx_contrib_order']}", CUR2),
 ("Non-Rx subscriber gross LTV", lambda s: f"=Model_{s}!{L(MONTHS+2)}{R['nonrx_ltv']}", CUR),
 ("Blended CAC, year 3 average", lambda s: (f"=IFERROR((SUM({mrange(s,'paid_spend',3)})-SUM({mrange(s,'ox_creative',3)}))"
                                            f"/SUM({mrange(s,'new_cust_all',3)}),0)"), CUR2),
 ("Non-Rx LTV:CAC, year 3", lambda s: (f"=IFERROR(Model_{s}!{L(MONTHS+2)}{R['nonrx_ltv']}/((SUM({mrange(s,'paid_spend',3)})"
                                       f"-SUM({mrange(s,'ox_creative',3)}))/SUM({mrange(s,'new_cust_all',3)})),0)"), DEC),
]
for j, h in enumerate(["Metric", "Conservative", "Baseline", "Aggressive"], 1):
    c = sm.cell(row=4, column=j, value=h); c.font = H2; c.fill = HDR
rr = 5
for label, fn, fmt in metrics:
    if label == "SPACER":
        rr += 1; continue
    sm.cell(row=rr, column=1, value=label).font = BOLD
    for j, s in enumerate(("Conservative", "Baseline", "Aggressive"), 2):
        c = sm.cell(row=rr, column=j, value=fn(s)); c.number_format = fmt; c.font = GREEN
    rr += 1
for col, w in zip("ABCD", (44, 20, 20, 20)): sm.column_dimensions[col].width = w
sm.freeze_panes = "B5"

# ================================================================= UNIT ECONOMICS
ue = wb.create_sheet("Unit_Economics", 2)
ue["A1"] = "Unit economics: where the margin actually comes from"; ue["A1"].font = H1
ue["A2"] = ("Two separate businesses with very different shapes. The non-prescription line is a high-margin consumer product that can "
            "trade in all fifty states. The prescription line carries medication, clinician and cold-chain cost on every single fill, "
            "so its margin is structurally lower and its retention risk structurally higher.")
ue["A2"].font = ITAL; ue["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ue.merge_cells("A2:E2"); ue.row_dimensions[2].height = 40

def ue_block(title, rows, start):
    ue.cell(row=start, column=1, value=title).font = Font(name=FONT, bold=True, size=11)
    for j, h in enumerate(["Line item", "Conservative", "Baseline", "Aggressive"], 1):
        c = ue.cell(row=start + 1, column=j, value=h); c.font = H2; c.fill = HDR
    r0 = start + 2
    for k, (lab, fn, fmt, bold) in enumerate(rows):
        ue.cell(row=r0 + k, column=1, value=lab).font = BOLD if bold else BLACK
        for j, s in enumerate(("Conservative", "Baseline", "Aggressive"), 2):
            col = SCN[s]
            c = ue.cell(row=r0 + k, column=j, value=fn(col, r0 + k))
            c.number_format = fmt; c.font = BOLD if bold else GREEN
    return r0 + len(rows) + 2

Ax = lambda col, k: A_(col, k)
nonrx_rows = [
 ("Average order value", lambda c, r: f"={Ax(c,'nonrx_aov')}", CUR2, False),
 ("less refunds and chargebacks", lambda c, r: f"=-{Ax(c,'nonrx_aov')}*{Ax(c,'refund_pct')}", CUR2, False),
 ("Net revenue per order", lambda c, r: f"=SUM({c}{r-2}:{c}{r-1})".replace(c, "", 0) if False else f"={L(2+list(SCN).index([k for k,v in SCN.items() if v==c][0]))}{r-2}+{L(2+list(SCN).index([k for k,v in SCN.items() if v==c][0]))}{r-1}", CUR2, True),
]
# simpler: build with explicit column letters on the UE sheet
def ue_col(scn): return {"Conservative": "B", "Baseline": "C", "Aggressive": "D"}[scn]

def ue_block2(title, rows, start):
    ue.cell(row=start, column=1, value=title).font = Font(name=FONT, bold=True, size=11)
    for j, h in enumerate(["Line item", "Conservative", "Baseline", "Aggressive"], 1):
        c = ue.cell(row=start + 1, column=j, value=h); c.font = H2; c.fill = HDR
    r0 = start + 2
    idx = {}
    for k, (tag, lab, fn, fmt, bold) in enumerate(rows):
        idx[tag] = r0 + k
    for k, (tag, lab, fn, fmt, bold) in enumerate(rows):
        row = r0 + k
        ue.cell(row=row, column=1, value=lab).font = BOLD if bold else BLACK
        for scn in ("Conservative", "Baseline", "Aggressive"):
            uc = ue_col(scn); ac = SCN[scn]
            c = ue.cell(row=row, column=ue.max_column if False else {"B": 2, "C": 3, "D": 4}[uc],
                        value="=" + fn(lambda k2: A_(ac, k2), lambda t: f"{uc}{idx[t]}"))
            c.number_format = fmt; c.font = BOLD if bold else GREEN
    return r0 + len(rows) + 2, idx

nxt, _ = ue_block2("A. Non-prescription order (one shipment)", [
 ("aov", "Average order value", lambda a, x: f"{a('nonrx_aov')}", CUR2, False),
 ("ref", "less refunds and chargebacks", lambda a, x: f"-{a('nonrx_aov')}*{a('refund_pct')}", CUR2, False),
 ("net", "Net revenue per order", lambda a, x: f"{x('aov')}+{x('ref')}", CUR2, True),
 ("cogs", "less landed product COGS", lambda a, x: f"-{a('nonrx_aov')}*{a('nonrx_cogs_pct')}", CUR2, False),
 ("ful", "less pick, pack and ship", lambda a, x: f"-{a('nonrx_fulfil')}", CUR2, False),
 ("prc", "less payment processing", lambda a, x: f"-{x('net')}*{a('pay_fee')}", CUR2, False),
 ("cm", "Contribution per order", lambda a, x: f"{x('net')}+{x('cogs')}+{x('ful')}+{x('prc')}", CUR2, True),
 ("cmp", "Contribution margin", lambda a, x: f"IFERROR({x('cm')}/{x('net')},0)", PCT, True),
 ("chn", "Monthly subscription churn", lambda a, x: f"{a('sub_churn')}", PCT, False),
 ("life", "Implied subscriber life", lambda a, x: f"1/{a('sub_churn')}", DEC, False),
 ("ltv", "Subscriber gross LTV", lambda a, x: f"{x('cm')}/{a('sub_churn')}", CUR, True),
], 4)

nxt2, _ = ue_block2("B. Prescription programme member (steady-state month)", [
 ("pp", "Programme price per member-month", lambda a, x: f"{a('rx_price')}", CUR2, False),
 ("ref", "less refunds and chargebacks", lambda a, x: f"-{a('rx_price')}*{a('refund_pct')}", CUR2, False),
 ("net", "Net revenue per member-month", lambda a, x: f"{x('pp')}+{x('ref')}", CUR2, True),
 ("ph", "less pharmacy medication cost", lambda a, x: f"-{a('pharm_cost')}", CUR2, False),
 ("cl", "less clinician monitoring and refill review", lambda a, x: f"-{a('refill_cost')}", CUR2, False),
 ("sh", "less cold-chain fulfilment and shipping", lambda a, x: f"-{a('coldchain_ship')}", CUR2, False),
 ("su", "less non-clinical support", lambda a, x: f"-{a('rx_support')}", CUR2, False),
 ("prc", "less payment processing", lambda a, x: f"-{x('net')}*{a('pay_fee')}", CUR2, False),
 ("cm", "Contribution per member-month", lambda a, x: f"{x('net')}+{x('ph')}+{x('cl')}+{x('sh')}+{x('su')}+{x('prc')}", CUR2, True),
 ("cmp", "Contribution margin", lambda a, x: f"IFERROR({x('cm')}/{x('net')},0)", PCT, True),
 ("chn", "Monthly churn", lambda a, x: f"{a('rx_churn')}", PCT, False),
 ("life", "Implied member life, months", lambda a, x: f"1/{a('rx_churn')}", DEC, False),
 ("ltv", "Member gross LTV", lambda a, x: f"{x('cm')}/{a('rx_churn')}", CUR, True),
], nxt)

nxt3, _ = ue_block2("C. Prescription enrolment (one-time, at intake)", [
 ("cf", "Consultation fee charged", lambda a, x: f"{a('consult_fee')}", CUR2, False),
 ("cc", "less clinician cost per completed consult", lambda a, x: f"-{a('consult_cost')}", CUR2, False),
 ("net", "Net on the consultation step", lambda a, x: f"{x('cf')}+{x('cc')}", CUR2, True),
 ("note", "Consults per enrolled member (1 / enrolment rate)", lambda a, x: f"1/{a('enroll_rate')}", DEC, False),
 ("load", "Consultation-step cost carried per enrolled member", lambda a, x: f"{x('net')}*{x('note')}", CUR2, True),
], nxt2)

ue.cell(row=nxt3, column=1, value="D. What the flat $600/month provider fee changes, and what it does not").font = Font(name=FONT, bold=True, size=11)
notes = [
 "The flat fee removes most FIXED operating cost from the model. It does not remove VARIABLE cost. Medication, per-consult clinician time, cold-chain shipping and card processing all scale with every order and every fill, and they are carried as separate drivers above.",
 "Published pricing for comparable turnkey telehealth infrastructure is $3,000-6,000 per month by tier, plus $5,000-10,000 onboarding, plus per-consult fees (benchmark B11). A $600 flat fee sits at roughly one fifth of the low end of that range.",
 "Read that two ways. Either the fee genuinely covers only software and compliance administration, which is the assumption used here and is the safe way to model it, or the scope is narrower than expected. Both readings lead to the same action: get the fee schedule in writing and confirm line by line what is and is not included.",
 "A vendor contract does not transfer the brand's own legal exposure. The brand remains responsible for its own advertising claims, its own endorsement disclosures, its own auto-renewal terms and its own privacy practices, whoever operates the platform.",
 "At $600 per month the provider has no economic stake in volume. That is good for margin and bad for alignment: nothing in the fee structure funds the provider's scaling, so capacity, turnaround time and service levels need to be contractual rather than assumed.",
]
for i, n in enumerate(notes):
    c = ue.cell(row=nxt3 + 1 + i, column=1, value=n); c.font = SMALL
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ue.merge_cells(start_row=nxt3 + 1 + i, start_column=1, end_row=nxt3 + 1 + i, end_column=4)
    ue.row_dimensions[nxt3 + 1 + i].height = 46
    for col in range(1, 5): ue.cell(row=nxt3 + 1 + i, column=col).fill = WARN
for col, w in zip("ABCD", (56, 17, 17, 17)): ue.column_dimensions[col].width = w

# ================================================================= SENSITIVITY
sv = wb.create_sheet("Sensitivity", 3)
sv["A1"] = "Sensitivity: which assumptions actually decide the outcome"; sv["A1"].font = H1
sv["A2"] = ("Closed-form grids computed from the Baseline column of Assumptions, so they recalculate with the rest of the workbook "
            "rather than needing a what-if table. Change the Baseline inputs and these move.")
sv["A2"].font = ITAL; sv["A2"].alignment = Alignment(wrap_text=True, vertical="top")
sv.merge_cells("A2:H2"); sv.row_dimensions[2].height = 30

B = "E"  # baseline column on Assumptions
sv["A4"] = "Grid 1. Prescription LTV:CAC by monthly churn and blended CAC"; sv["A4"].font = Font(name=FONT, bold=True, size=11)
sv["A5"] = "Rx contribution per member-month (Baseline drivers)"; sv["A5"].font = BOLD
sv["D5"] = (f"={A_(B,'rx_price')}*(1-{A_(B,'refund_pct')})*(1-{A_(B,'pay_fee')})-{A_(B,'pharm_cost')}"
            f"-{A_(B,'refill_cost')}-{A_(B,'coldchain_ship')}-{A_(B,'rx_support')}")
sv["D5"].number_format = CUR2; sv["D5"].font = GREEN
sv["A6"] = "Below 3.0x the programme does not pay for its own acquisition. Cells at or above 3.0x are viable."; sv["A6"].font = SMALL
churns = [0.080, 0.095, 0.110, 0.130, 0.150, 0.180]
cacs = [150, 250, 350, 450, 600, 800]
sv.cell(row=8, column=1, value="Monthly churn \\ CAC").font = H2
sv.cell(row=8, column=1).fill = HDR
for j, cv in enumerate(cacs, 2):
    c = sv.cell(row=8, column=j, value=cv); c.font = H2; c.fill = HDR; c.number_format = CUR
for i, ch in enumerate(churns, 9):
    c = sv.cell(row=i, column=1, value=ch); c.font = BOLD; c.number_format = PCT
    for j, cv in enumerate(cacs, 2):
        cc = sv.cell(row=i, column=j, value=f"=($D$5/$A{i})/{L(j)}$8")
        cc.number_format = DEC; cc.font = BLACK
sv.cell(row=15, column=1, value=f"Baseline churn is {VAL['rx_churn']['Baseline']:.1%}. Benchmark B17 puts real-world discontinuation near 65% at 12 months, which is roughly 8.4% monthly, and 84.4% at 24 months, roughly 7.4% monthly. Churn worse than about 15% monthly makes the prescription line unviable at any plausible CAC.").font = SMALL
sv.merge_cells("A15:H15"); sv.row_dimensions[15].height = 30
sv.cell(row=15, column=1).alignment = Alignment(wrap_text=True, vertical="top")

sv["A18"] = "Grid 2. Month-12 partner-driven sessions by reach per post and click-through"; sv["A18"].font = Font(name=FONT, bold=True, size=11)
sv["A19"] = "These two drivers are the least evidenced in the model and they multiply, so the band they produce is wide by construction."; sv["A19"].font = SMALL
sv.merge_cells("A19:H19")
reaches = [0.02, 0.04, 0.07, 0.11, 0.15]
ctrs = [0.002, 0.0035, 0.006, 0.009, 0.013]
sv.cell(row=21, column=1, value="Reach % \\ CTR").font = H2; sv.cell(row=21, column=1).fill = HDR
for j, cv in enumerate(ctrs, 2):
    c = sv.cell(row=21, column=j, value=cv); c.font = H2; c.fill = HDR; c.number_format = PCT2
for i, rv in enumerate(reaches, 22):
    c = sv.cell(row=i, column=1, value=rv); c.font = BOLD; c.number_format = PCT
    for j, cv in enumerate(ctrs, 2):
        cc = sv.cell(row=i, column=j,
                     value=(f"={A_(B,'followers')}*{A_(B,'posts_per_month')}*$A{i}*{L(j)}$21"
                            f"*({A_(B,'attn_floor')}+(1-{A_(B,'attn_floor')})*{A_(B,'attn_decay')}^(12-{A_(B,'nonrx_launch')}))"))
        cc.number_format = NUM; cc.font = BLACK

sv["A29"] = "Grid 3. Year-3 blended gross margin by non-Rx COGS share and pharmacy cost per member-month"; sv["A29"].font = Font(name=FONT, bold=True, size=11)
sv["A30"] = ("Approximated at the Baseline year-3 revenue mix so the grid is readable. Non-Rx share of year-3 net revenue is taken "
             "from the Summary sheet.")
sv["A30"].font = SMALL; sv.merge_cells("A30:H30")
sv["A31"] = "Non-Rx share of year-3 net revenue (Baseline)"; sv["A31"].font = BOLD
sv["E31"] = "=Summary!C29"; sv["E31"].number_format = PCT; sv["E31"].font = GREEN
cogs_opts = [0.20, 0.24, 0.28, 0.32, 0.38]
pharm_opts = [60, 75, 90, 105, 130]
sv.cell(row=33, column=1, value="Non-Rx COGS % \\ pharmacy $/mm").font = H2; sv.cell(row=33, column=1).fill = HDR
for j, pv in enumerate(pharm_opts, 2):
    c = sv.cell(row=33, column=j, value=pv); c.font = H2; c.fill = HDR; c.number_format = CUR
for i, gv in enumerate(cogs_opts, 34):
    c = sv.cell(row=i, column=1, value=gv); c.font = BOLD; c.number_format = PCT
    for j, pv in enumerate(pharm_opts, 2):
        # non-Rx margin per $1 net revenue
        nx = (f"(1-$A{i}/(1-{A_(B,'refund_pct')})-{A_(B,'nonrx_fulfil')}/({A_(B,'nonrx_aov')}*(1-{A_(B,'refund_pct')}))-{A_(B,'pay_fee')})")
        rxm = (f"(1-({L(j)}$33+{A_(B,'refill_cost')}+{A_(B,'coldchain_ship')}+{A_(B,'rx_support')})"
               f"/({A_(B,'rx_price')}*(1-{A_(B,'refund_pct')}))-{A_(B,'pay_fee')})")
        cc = sv.cell(row=i, column=j, value=f"=$E$31*{nx}+(1-$E$31)*{rxm}")
        cc.number_format = PCT; cc.font = BLACK
for col, w in zip("ABCDEFGH", (32, 14, 14, 14, 14, 14, 14, 14)): sv.column_dimensions[col].width = w

# ================================================================= PARTNER ECONOMICS
pe = wb.create_sheet("Partner_Economics", 4)
pe["A1"] = "Proposed brand-partner economics - illustrative only"; pe["A1"].font = H1
pe["A2"] = ("No terms have been offered, negotiated or accepted. Nothing on this sheet is an offer. The structure below exists so the "
            "conversation can start from arithmetic instead of adjectives. The equity figures use an illustrative revenue multiple and "
            "are NOT a valuation; a valuation requires an actual process.")
pe["A2"].font = ITAL; pe["A2"].alignment = Alignment(wrap_text=True, vertical="top")
pe.merge_cells("A2:E2"); pe.row_dimensions[2].height = 44
pe["A4"] = "Illustrative revenue multiple on year-3 net revenue"; pe["A4"].font = BOLD
pe["C4"] = 3.0; pe["C4"].font = BLUE; pe["C4"].number_format = DEC
pe["D4"] = "Editable. DTC and telehealth multiples move with growth, margin and rate cycles; 2-5x net revenue is a commonly quoted range for profitable consumer health at scale. Not a valuation."
pe["D4"].font = SMALL; pe["D4"].alignment = Alignment(wrap_text=True, vertical="top")
prow = [
 ("Cash retainer over 36 months", lambda s: f"=-SUM(Model_{s}!{L(3)}{R['ox_partner_cash']}:{L(MONTHS+2)}{R['ox_partner_cash']})", CUR),
 ("Royalty over 36 months", lambda s: f"=-SUM(Model_{s}!{L(3)}{R['ox_partner_roy']}:{L(MONTHS+2)}{R['ox_partner_roy']})", CUR),
 ("Total cash to partner over 36 months", None, CUR),
 ("Royalty in year 3 alone", lambda s: f"=-SUM({mrange(s,'ox_partner_roy',3)})", CUR),
 ("Partner equity, fully diluted", lambda s: f"={A_(SCN[s],'partner_equity')}", PCT),
 ("Illustrative equity value at year-3 revenue multiple", None, CUR),
 ("Total illustrative 36-month partner value", None, CUR),
 ("Partner cash as a share of 36-month net revenue", None, PCT),
]
for j, h in enumerate(["Item", "Conservative", "Baseline", "Aggressive"], 1):
    c = pe.cell(row=6, column=j, value=h); c.font = H2; c.fill = HDR
rr = 7
pmap = {}
for label, fn, fmt in prow:
    pe.cell(row=rr, column=1, value=label).font = BOLD
    pmap[label] = rr
    rr += 1
for j, s in enumerate(("Conservative", "Baseline", "Aggressive"), 2):
    cl = L(j)
    pe.cell(row=pmap["Cash retainer over 36 months"], column=j,
            value=prow[0][1](s)).number_format = CUR
    pe.cell(row=pmap["Royalty over 36 months"], column=j, value=prow[1][1](s)).number_format = CUR
    pe.cell(row=pmap["Total cash to partner over 36 months"], column=j,
            value=f"={cl}{pmap['Cash retainer over 36 months']}+{cl}{pmap['Royalty over 36 months']}").number_format = CUR
    pe.cell(row=pmap["Royalty in year 3 alone"], column=j, value=prow[3][1](s)).number_format = CUR
    pe.cell(row=pmap["Partner equity, fully diluted"], column=j, value=prow[4][1](s)).number_format = PCT
    pe.cell(row=pmap["Illustrative equity value at year-3 revenue multiple"], column=j,
            value=f"=Summary!{cl}7*$C$4*{cl}{pmap['Partner equity, fully diluted']}").number_format = CUR
    pe.cell(row=pmap["Total illustrative 36-month partner value"], column=j,
            value=f"={cl}{pmap['Total cash to partner over 36 months']}+{cl}{pmap['Illustrative equity value at year-3 revenue multiple']}").number_format = CUR
    pe.cell(row=pmap["Partner cash as a share of 36-month net revenue"], column=j,
            value=f"=IFERROR({cl}{pmap['Total cash to partner over 36 months']}/Summary!{cl}8,0)").number_format = PCT
    for k in pmap.values(): pe.cell(row=k, column=j).font = GREEN
gr = rr + 1
pe.cell(row=gr, column=1, value="Constraints that shape any deal here").font = Font(name=FONT, bold=True, size=11)
pcon = [
 "The partner can promote the brand and the non-prescription line. The partner should not promote specific compounded prescription drugs. 503A compounders operate under advertising and promotion limits, prescription-drug advertising carries its own disclosure requirements, and celebrity promotion of a prescription product invites exactly the scrutiny a new brand cannot absorb. Separating what is promotable from what is prescribable is a design requirement, not a preference.",
 "Every paid or equity-holding endorsement needs a clear and conspicuous disclosure of the material connection, on every post and in every format, under the FTC Endorsement Guides. A founder's equity stake is a material connection. Earlier research in this project found the proposed partner named on the FTC's September 2017 list of influencers sent warning letters about undisclosed endorsements, which makes disclosure discipline a specific and personal risk here rather than a generic one.",
 "Compensation to the medical entity and to clinicians must never vary with prescription volume, programme enrolments or revenue. Partner compensation may be tied to revenue; clinical compensation may not. Keeping those two facts in separate contracts is the point of the structure.",
 "A prior or concurrent promotion of a competing weight-management or GLP-1 product may create a category-exclusivity conflict. Earlier research in this project flagged a possible prior GLP-1-adjacent promotion; brand and paid status were not verified. Resolve it in diligence before any announcement.",
 "Nothing here is an offer, and nothing here should be shared as though terms exist. Until definitive agreements are signed the brand is a proposed concept and the partner's role is proposed.",
]
for i, n in enumerate(pcon):
    c = pe.cell(row=gr + 1 + i, column=1, value=n); c.font = SMALL
    c.alignment = Alignment(wrap_text=True, vertical="top")
    pe.merge_cells(start_row=gr + 1 + i, start_column=1, end_row=gr + 1 + i, end_column=4)
    pe.row_dimensions[gr + 1 + i].height = 60
for col, w in zip("ABCD", (52, 20, 20, 20)): pe.column_dimensions[col].width = w
pe.column_dimensions["D"].width = 20

# ================================================================= PROVIDER DILIGENCE
pd_ = wb.create_sheet("Provider_Diligence", 5)
pd_["A1"] = "Turnkey provider at $600/month - what to confirm before signing"; pd_["A1"].font = H1
pd_["A2"] = ("The whole model rests on this vendor. At this fee the vendor carries no volume risk, so scope has to be contractual. "
             "Every row is a question to put in writing; the Why column says what breaks in the model if the answer is not what you expect.")
pd_["A2"].font = ITAL; pd_["A2"].alignment = Alignment(wrap_text=True, vertical="top")
pd_.merge_cells("A2:D2"); pd_.row_dimensions[2].height = 40
for j, h in enumerate(["#", "Question to put in writing", "Why it matters to the model", "Status"], 1):
    c = pd_.cell(row=4, column=j, value=h); c.font = H2; c.fill = HDR
qs = [
 ("Does the $600 include per-consult clinician fees, or are those billed separately per visit?",
  "The model assumes separately, at $32-45 per completed consult. If included, Rx gross margin improves by roughly the consult cost divided by enrolments. If excluded and higher than assumed, enrolment economics compress."),
 ("Does the $600 include medication cost, or does the pharmacy bill per fill?",
  "The model assumes the pharmacy bills per fill at $75-105 per member-month. This is the largest single variable cost in the Rx line; a written tiered schedule is essential."),
 ("Does the $600 include cold-chain shipping and packaging, or is that billed per shipment?",
  "The model assumes per shipment at $15-22. Benchmark B09 shows a $1.95 pack rate is only the pack step, not the landed temperature-controlled cost."),
 ("Is payment processing inside the fee, and at what rate and risk classification?",
  "The model carries 2.7-3.2% separately. Healthcare and supplement merchants are frequently underwritten as elevated risk."),
 ("Which specific pharmacies fulfil, under which licences, and in which states?",
  "Drives the state-coverage ramp, which is the gate on the whole Rx funnel. Name the pharmacies; do not accept a count."),
 ("For each pharmacy: 503A, 503B, or both, and which is used for which product?",
  "503A compounds pursuant to individual patient prescriptions. 503B outsourcing facilities are built for non-patient-specific office stock. They are not interchangeable for a consumer-direct model, and assuming they are is a common and expensive error."),
 ("How does the arrangement handle interstate distribution limits for 503A pharmacies?",
  "Section 503A(b)(3) caps interstate distribution of compounded drugs at 5% of total prescription orders unless the pharmacy's state has signed the FDA memorandum of understanding. FDA's compounding MOU index currently lists only three MOUs, all suspended, and FDA has repeatedly deferred enforcement of the 5% limit pending rulemaking. Deferred enforcement is discretionary and revocable, so a national single-pharmacy Rx model is a policy bet, not a settled structure."),
 ("Which peptides are on the current FDA 503A Category 1 bulks list, as of the signing date?",
  "Determines the formulary. Benchmark B18: FDA removed 12 peptides from Category 2 in April 2026, the PCAC met in July 2026 on three more and will meet again before the end of February 2027 on five others. The list moves; the contract should require the provider to track it."),
 ("Is any product 'essentially a copy' of an approved drug?",
  "Section 503A limits compounding of drugs that are essentially copies of commercially available products. This is where compounded-GLP-1 programmes have drawn enforcement."),
 ("Who holds the LegitScript healthcare merchant certification, and for which website?",
  "Certification is site-specific and gates healthcare advertising across Google, Meta, Microsoft and TikTok. If it is the provider's certification on the provider's domain, the brand's own site may not be covered. No certification means no scaled paid acquisition, which removes most of the paid-traffic line from the model."),
 ("What is the legal structure: MSO and friendly-PC, and who owns the physician entity?",
  "Corporate-practice-of-medicine rules in many states bar a non-physician company from owning a medical practice or splitting professional fees. Get the structure opinion, not a reassurance."),
 ("How are clinicians compensated, and does any element vary with prescribing or revenue?",
  "Any volume- or revenue-linked clinical compensation is a fee-splitting and kickback problem and undermines the clinical-independence position the whole model depends on."),
 ("Who owns the patient relationship, the medical records and the customer data on exit?",
  "Determines whether the brand has an asset or a rental. Ask for the data-portability and records-transfer terms in the termination clause."),
 ("Who is the named party on advertising claims, and who indemnifies whom?",
  "A vendor contract does not transfer the brand's own advertising liability. Read the indemnity in both directions and check the cap against the insurance limits."),
 ("What are the service levels: consult turnaround, fill turnaround, ship-by, support response?",
  "At a flat fee the provider has no economic incentive to scale with you. Without contractual service levels, growth degrades the customer experience exactly when volume arrives."),
 ("What are the capacity ceilings, and what happens when the brand exceeds them?",
  "The aggressive scenario implies order volumes that a $600/month arrangement is unlikely to have been sized for. Get the ceiling in writing and the repricing mechanism with it."),
 ("What are the termination terms, notice period and post-termination continuity of care?",
  "Members on active prescription programmes cannot simply be dropped. Continuity-of-care obligations survive the contract and belong in the plan."),
 ("What insurance does the provider carry, at what limits, and is the brand an additional insured?",
  "Determines the real gap the brand's own product-liability, professional and cyber cover has to fill."),
 ("Has the provider or any affiliated pharmacy or clinician been subject to FDA, DEA, state board or FTC action?",
  "Basic counterparty diligence. A provider's enforcement history becomes the brand's reputational problem on day one."),
 ("Auto-renewal mechanics: consent capture, renewal reminders, cancellation path, and who is liable?",
  "ROSCA and state auto-renewal laws are the most common source of consumer-protection claims in subscription health. The cancellation path must be as easy as the sign-up path, and the brand is liable for it whoever built it."),
]
for i, (q, why) in enumerate(qs, 1):
    row = 4 + i
    pd_.cell(row=row, column=1, value=i).font = BOLD
    c = pd_.cell(row=row, column=2, value=q); c.font = BLACK; c.alignment = Alignment(wrap_text=True, vertical="top")
    c2 = pd_.cell(row=row, column=3, value=why); c2.font = SMALL; c2.alignment = Alignment(wrap_text=True, vertical="top")
    pd_.cell(row=row, column=4, value="Open").font = BLACK
    pd_.row_dimensions[row].height = 58
for col, w in zip("ABCD", (5, 60, 78, 12)): pd_.column_dimensions[col].width = w
pd_.freeze_panes = "A5"

# ================================================================= BENCHMARKS
bm = wb.create_sheet("Benchmarks", 6)
bm["A1"] = "Benchmarks behind the drivers"; bm["A1"].font = H1
bm["A2"] = ("Third-party unless marked as an analyst assumption. Figures were taken from search-result summaries during a session in "
            "which direct page loads were restricted; load-bearing figures were corroborated across two independent queries. "
            "Ranges are ranges, not measurements.")
bm["A2"].font = ITAL; bm["A2"].alignment = Alignment(wrap_text=True, vertical="top")
bm.merge_cells("A2:F2"); bm.row_dimensions[2].height = 40
for j, h in enumerate(["ID", "Topic", "Finding", "How it is used", "Confidence", "Sources"], 1):
    c = bm.cell(row=4, column=j, value=h); c.font = H2; c.fill = HDR
bdata = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research", "07_margin_growth_benchmarks.json")))
for i, b in enumerate(bdata["benchmarks"]):
    row = 5 + i
    bm.cell(row=row, column=1, value=b["id"]).font = BOLD
    for col, key in ((2, "topic"), (3, "finding"), (4, "use_in_model"), (5, "confidence")):
        c = bm.cell(row=row, column=col, value=b[key]); c.font = SMALL if col in (3, 4) else BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
    c = bm.cell(row=row, column=6, value="\n".join(b["sources"])); c.font = Font(name=FONT, size=7)
    c.alignment = Alignment(wrap_text=True, vertical="top")
    bm.row_dimensions[row].height = 92
nrow = 5 + len(bdata["benchmarks"]) + 1
bm.cell(row=nrow, column=1, value="Not retrievable in this environment").font = Font(name=FONT, bold=True, size=11)
for i, n in enumerate(bdata["not_retrievable"]):
    c = bm.cell(row=nrow + 1 + i, column=2, value=n); c.font = SMALL
    c.alignment = Alignment(wrap_text=True, vertical="top")
    bm.merge_cells(start_row=nrow + 1 + i, start_column=2, end_row=nrow + 1 + i, end_column=6)
    bm.row_dimensions[nrow + 1 + i].height = 30
for col, w in zip("ABCDEF", (7, 34, 62, 58, 14, 46)): bm.column_dimensions[col].width = w
bm.freeze_panes = "A5"

# ================================================================= READ ME
rm = wb.create_sheet("Read_Me", 0)
rm["A1"] = "Reserve Clinic - Margin and Growth Model"; rm["A1"].font = Font(name=FONT, bold=True, size=16)
blocks = [
 ("What this is",
  "A driver-based 36-month model of a two-line peptide and supplement business: a non-prescription supplement line that can trade in "
  "all fifty states, and a prescription telehealth line fulfilled by 503A and 503B pharmacies whose state footprint expands over time. "
  "It is built for the specific operating structure the project owner described, including a turnkey compliance-and-fulfilment provider "
  "at a flat $600 per month. Three scenarios: Conservative, Baseline, Aggressive."),
 ("What it is not",
  "Not a forecast, not a valuation, and not legal, medical, tax or investment advice. The outputs follow arithmetically from the drivers "
  "on the Assumptions sheet. Change a driver and the answer changes. Several of the most consequential drivers rest on analyst "
  "assumptions rather than measurements, and those are labelled Low confidence with a stated validation method."),
 ("Status of the people named",
  "The proposed brand partner and the proposed medical co-founder are treated strictly as proposed. No public evidence connects either "
  "to this venture, no agreement exists, and nothing in this workbook is an offer or implies endorsement, ownership or authorisation. "
  "Partner compensation figures are illustrative arithmetic, not terms."),
 ("Colour key",
  "Blue = editable input, on the Assumptions sheet only. Black = formula. Green = link to another sheet. Yellow fill = high-sensitivity "
  "driver: get these wrong and the answer changes materially. Peach fill = a caution the reader should not skip."),
 ("Sheet order",
  "Summary reads the three scenarios side by side. Unit_Economics shows where margin comes from per order and per member-month. "
  "Sensitivity shows which assumptions decide the outcome. Partner_Economics is illustrative deal arithmetic. Provider_Diligence is the "
  "twenty questions to answer in writing before signing. Benchmarks is the evidence. Assumptions holds every input. "
  "Model_Conservative, Model_Baseline and Model_Aggressive are the monthly grids."),
 ("The three things most likely to be wrong",
  "1. Audience conversion. Reach per post and click-through are multiplied together and neither is measured; Sensitivity grid 2 shows the "
  "spread. 2. Prescription retention. Benchmark B17 puts real-world discontinuation near 65% at twelve months; Sensitivity grid 1 shows "
  "that above roughly 15% monthly churn the prescription line does not pay for its own acquisition at any plausible CAC. "
  "3. The provider's scope. A $600 flat fee is roughly one fifth of the low end of published market pricing for comparable turnkey "
  "telehealth infrastructure, so the model assumes it covers software and administration only and carries every variable cost separately."),
 ("Structural limits the model encodes deliberately",
  "Fifty-state coverage applies to the non-prescription line only. The prescription line ramps from 26-45% of the US population at launch "
  "to a 70-88% ceiling, because asynchronous-prescribing rules, corporate-practice-of-medicine limits and the section 503A(b)(3) five "
  "percent interstate distribution cap all constrain it. FDA's compounding memorandum-of-understanding index currently lists three MOUs, "
  "all suspended, and FDA has repeatedly deferred enforcement of the five percent limit pending rulemaking. Deferred enforcement is "
  "discretionary and revocable. Every one of these areas needs qualified counsel: FDA and pharmacy regulatory, corporate practice of "
  "medicine, healthcare privacy, advertising and endorsement, consumer protection and auto-renewal, and intellectual property."),
 ("Prepared", "2026-09-18. Rebuild with: python3 build/build_margin_model.py outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx"),
]
r = 3
for head, body in blocks:
    c = rm.cell(row=r, column=1, value=head); c.font = Font(name=FONT, bold=True, size=11)
    c2 = rm.cell(row=r + 1, column=1, value=body); c2.font = Font(name=FONT, size=10)
    c2.alignment = Alignment(wrap_text=True, vertical="top")
    rm.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=6)
    rm.row_dimensions[r + 1].height = max(30, 13 * (len(body) // 118 + 1))
    r += 3
rm.column_dimensions["A"].width = 26
for col in "BCDEF": rm.column_dimensions[col].width = 22

wb.save(OUT)
print(f"wrote {OUT}")
json.dump({"assumption_rows": ROW, "line_rows": R, "values": VAL, "order": ORDER},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "margin_layout.json"), "w"), indent=1)
print(f"{len(ROW)} drivers, {len(LINES)} model lines, {MONTHS} months, 3 scenarios")
