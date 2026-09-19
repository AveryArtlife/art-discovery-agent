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
 ("posts_per_month", "Brand posts per month by the partner (feed plus reels)", "#", 3, 5, 7,
  "A contract deliverable, not a market variable. Set to whatever the agreement actually obliges.", "n/a", "High", "Signed content schedule"),
 ("reach_pct", "Reach per brand post as a share of followers", "%", 0.055, 0.08, 0.105,
  "Analyst assumption bounded by benchmark B15: the 10M-plus tier averages ~1.77% ENGAGEMENT; reach exceeds engagement but organic reach at this tier is heavily throttled and branded content more so. Reels reach higher than static.", "Low", "High", "Creator-account reach data, first 60 days"),
 ("ctr_reach", "Click-through to site per reached impression", "%", 0.0050, 0.0070, 0.0095,
  "Analyst assumption. No tier-level link-click benchmark was retrievable (benchmark B15 notes this gap). This is the single least-evidenced driver in the model.", "Low", "High", "UTM-tagged link data, first 30 days"),
 ("attn_decay", "Monthly decay of partner-driven traffic toward a floor", "%", 0.72, 0.80, 0.86,
  "Analyst assumption. Celebrity launch demand spikes then settles; benchmark B14 notes IM8's founders deliberately did not rely on fame for durability.", "Low", "High", "Cohort traffic by source, monthly"),
 ("attn_floor", "Floor for partner-driven traffic as a share of the launch peak", "%", 0.32, 0.38, 0.44,
  "Analyst assumption. Represents the durable follower demand that persists after novelty.", "Low", "High", "Cohort traffic by source, monthly"),
 ("launch_spike", "Launch-month multiplier on partner-driven traffic", "x", 1.8, 2.3, 2.8,
  "Announcement window concentrates attention. Analyst assumption.", "Low", "Medium", "Launch-week analytics"),
 ("SECTION", "Other traffic"),
 ("organic_m1", "Organic and direct sessions, month 1", "sessions", 1200, 2200, 3500,
  "New domain with an editorial library. Analyst assumption.", "Low", "Low", "GA4 after month 1"),
 ("organic_growth", "Organic monthly growth rate", "%", 0.06, 0.09, 0.12,
  "Content-led SEO compounding from a small base. Analyst inference.", "Low", "Medium", "Search Console trend"),
 ("organic_cap", "Organic and direct sessions ceiling", "sessions", 90000, 180000, 280000,
  "Caps compounding; category search demand is finite. Analyst inference.", "Low", "Medium", "Search Console"),
 ("paid_pre", "Paid media per month before the non-Rx launch", "$", 4000, 8000, 15000,
  "Waitlist and audience building only.", "Medium", "Low", "Budget actuals"),
 ("paid_floor", "Minimum paid media per month after launch", "$", 10000, 30000, 60000,
  "Keeps a spend floor while revenue is small.", "Medium", "Medium", "Budget actuals"),
 ("paid_pct", "Paid media as a share of prior-month net revenue", "%", 0.30, 0.24, 0.20,
  "Benchmark B02: the closest listed telehealth comparable ran marketing at 35-40% of revenue. A celebrity-led brand should sit WELL below that, because the point of the partnership is that owned audience substitutes for bought audience; if this driver has to rise toward 35% the partnership is not working. Prior-month basis avoids a circular reference.", "Medium", "High", "Monthly payback review"),
 ("launch_push", "One-time launch marketing and PR, non-Rx launch month", "$", 20000, 60000, 150000,
  "Announcement window spend. Deliberately modest: the point of a founder with a large audience is that the launch does not have to be bought. A brand spending heavily here is paying twice for the same attention.", "Medium", "Medium", "Agency scopes"),
 ("paid_cap", "Maximum paid media per month", "$", 300000, 1500000, 4000000,
  "A budget ceiling and a backstop. Diminishing returns and the fulfilment capacity ramp now do most of the work of bounding growth, so this is set high enough that the percent-of-revenue rule governs rather than the cap. At the Aggressive ceiling it is roughly 27% of revenue at scale, in line with benchmark B02.", "Medium", "Medium", "Board-approved budget"),
 ("paid_elast", "Paid response elasticity (sessions per marginal dollar)", "x", 0.70, 0.74, 0.78,
  "Diminishing returns on the cold prospecting tier. Sessions scale as (spend / reference spend) raised to this power, so at ten times the reference the effective cost per session rises about 1.8x at 0.74. Below 1.0 is the whole point: auction competition and audience exhaustion mean the second million never buys what the first did. Analyst assumption, standard media-mix practice.", "Low", "High", "Marginal CAC by spend decile"),
 ("SECTION", "Targeted paid media, tier 1: branded and intent search (harvests demand the partner creates)"),
 ("bsearch_per_reach", "Branded searches generated per reached impression", "%", 0.0008, 0.0015, 0.0025,
  "Each brand post sends some viewers to a search engine rather than to the link. Analyst assumption; no tier-level benchmark was retrievable. This is the mechanism by which celebrity promotion creates cheap paid inventory rather than just free traffic.", "Low", "High", "Branded-query volume in Search Console and Google Ads"),
 ("bsearch_organic_factor", "Branded and intent searches per organic session", "%", 0.05, 0.08, 0.11,
  "Baseline brand-name and category-intent search that exists independently of the partner. Analyst assumption.", "Low", "Medium", "Search Console"),
 ("bsearch_capture", "Share of available branded and intent search bought", "%", 0.55, 0.65, 0.75,
  "You cannot buy every query, and you should not: some arrive free through organic listings. Analyst assumption.", "Medium", "Medium", "Impression share in Google Ads"),
 ("cps_search", "Cost per session, branded and intent search", "$", 1.30, 1.10, 0.95,
  "Branded queries are the cheapest paid inventory a brand owns because it faces little auction competition on its own name. Analyst assumption anchored to health-category CPC proxies.", "Medium", "High", "Google Ads cost per click"),
 ("conv_mult_search", "Conversion multiplier, branded and intent search", "x", 2.2, 2.8, 3.4,
  "High-intent traffic converts well above the site average. Analyst assumption; no branded-search multiplier benchmark was retrievable (B19 notes the gap).", "Low", "High", "Conversion rate by channel"),
 ("search_increment", "Share of branded-search conversions that are incremental", "%", 0.35, 0.45, 0.55,
  "THE HONEST HAIRCUT. Paying for a query you would rank for organically buys a click you already had. Benchmark B19 makes the same point about retargeting. Without this factor the model would double-count the partner's organic traffic and the paid search that harvests it.", "Medium", "High", "Paid-search holdout or geo test"),
 ("SECTION", "Targeted paid media, tier 2: retargeting site visitors and the partner's engagers"),
 ("retarget_pool_sessions", "Share of prior-month sessions addressable for retargeting", "%", 0.45, 0.55, 0.65,
  "Cookie and consent loss, app-tracking opt-outs and platform matching all shrink the pool. Analyst assumption.", "Medium", "Medium", "Custom-audience sizes in the ad platforms"),
 ("retarget_pool_engagers", "Partner-post engagers addressable per reached impression", "%", 0.006, 0.010, 0.016,
  "People who engaged with a brand post can be retargeted from the platform's engagement audience. This is the second mechanism by which the partnership creates cheap, warm ad inventory. Analyst assumption bounded by benchmark B15: the 10M-plus tier averages about 1.77% engagement.", "Low", "High", "Engagement-audience size in Meta"),
 ("retarget_freq", "Sessions bought per addressable pool member per month", "%", 0.18, 0.25, 0.32,
  "How hard the warm pool is worked before fatigue. Analyst assumption.", "Low", "Medium", "Frequency and pool-decay reports"),
 ("cps_retarget", "Cost per session, retargeting", "$", 1.70, 1.45, 1.25,
  "Warm audiences cost less per click than cold. Benchmark B19: retargeting CPA runs 40-70% below cold acquisition.", "Medium", "High", "Ad platform reports"),
 ("conv_mult_retarget", "Conversion multiplier, retargeting", "x", 1.6, 2.0, 2.4,
  "Benchmark B19: retargeting ROAS averages about 4.2x against 1.5-3x for cold prospecting, roughly 71% higher.", "Medium", "High", "Conversion rate by channel"),
 ("retarget_increment", "Share of retargeting conversions that are incremental", "%", 0.25, 0.30, 0.40,
  "THE SECOND HONEST HAIRCUT, and the one most often ignored. Benchmark B19: holdout tests show true incremental lift of 25-30%, meaning up to 75% of retargeting conversions would have happened anyway. Retargeting mostly harvests demand that the partner's organic posts and the prospecting tier already created.", "Medium", "High", "Retargeting holdout test, month 2 onward"),
 ("SECTION", "Targeted paid media, tier 3: cold prospecting with partner creative"),
 ("cps_prospect", "Cost per session, cold prospecting, generic creative", "$", 2.80, 2.35, 2.00,
  "Health and wellness CPC proxies; restricted-category ad review raises cost. LegitScript certification is a precondition for scaled healthcare advertising (benchmark B10). Instagram feed ad click-through commonly 0.22-0.88% (B20).", "Medium", "High", "Ad platform reports"),
 ("creative_disc", "Cost-per-session discount from partner creative", "x", 0.88, 0.80, 0.72,
  "A recognisable face and partner-voiced video should raise click-through and so lower cost per session. NO celebrity-specific benchmark was retrievable; the supporting evidence is only general (video creative 30-50% higher click-through, faces in visuals recommended) per B20. Treat as an analyst assumption, and note that using the partner's likeness in PAID media needs broader licensing than organic posting and faces additional health-category ad review.", "Low", "High", "Creative A/B test with and without the partner, month 1"),
 ("conv_mult_prospect", "Conversion multiplier, cold prospecting", "x", 1.0, 1.0, 1.0,
  "The reference tier. Held at 1.0 by definition so the other multipliers are read relative to cold traffic.", "n/a", "Low", "Conversion rate by channel"),
 ("conv_mult_partner_organic", "Conversion multiplier, the partner's own organic traffic", "x", 1.4, 1.7, 2.0,
  "Followers arriving from a brand post are warmer than cold prospects but colder than someone searching the brand by name. Analyst assumption.", "Low", "High", "Conversion rate by channel"),
 ("rx_celeb_factor", "Prescription-intent factor on partner-driven and cold-prospecting traffic", "x", 0.45, 0.60, 0.75,
  "A follower who clicks a supplement post is much less likely to start a prescription consult than someone who searched for peptide therapy. The partner also cannot promote compounded prescription products, so prescription intent has to come from search, organic content and on-site cross-sell rather than from partner creative. Analyst assumption.", "Low", "High", "Quiz-start rate by traffic source"),
 ("SECTION", "Non-prescription line: funnel and pricing"),
 ("cap_m1", "Orders the wholesaler can ship in the first live month", "#", 3000, 8000, 15000,
  "Now the wholesaler's stock position rather than a manufacturing run, so it is far higher than an owned-inventory launch would allow. It is NOT unlimited: a wholesaler sized for ordinary DTC volumes can be cleared out by a single post to a 27-million-follower audience, and demand above the ceiling is treated as LOST rather than backlogged. Analyst assumption; replace with a committed stock allocation in writing.", "Low", "High", "Committed stock allocation from the wholesaler"),
 ("cap_growth", "Monthly growth in shippable capacity", "x", 1.35, 1.45, 1.55,
  "How fast the wholesaler can scale allocation. Binds only in the opening months of the Aggressive case now. Analyst assumption.", "Low", "Medium", "Wholesaler capacity commitment"),
 ("shop_conv", "Order conversion rate, all sessions", "%", 0.010, 0.015, 0.020,
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
 ("nonrx_cogs_pct", "All-in wholesale cost of goods as a share of retail (includes the wholesaler's pick, pack and ship)", "%", 0.44, 0.37, 0.32,
  "The arrangement described: wholesale unit pricing from a wholesaler who holds the stock and ships to the customer. Benchmark B21. This is ALL-IN, so the separate fulfilment driver below is zero. Compare like for like: owning runs at the benchmark 26% landed COGS plus $7.50 of separate fulfilment is about 36% of retail on a $78 order, so this arrangement is close to margin-neutral and hands back the working capital. Replace the range with the wholesaler's actual price schedule.", "Medium", "High", "Wholesaler price schedule, by volume tier"),
 ("nonrx_fulfil", "Additional per-order shipping billed to the brand", "$", 0, 0, 0,
  "Zero because the wholesale dropship price is all-in. Set this above zero if the wholesaler bills shipping separately, or if the brand subsidises expedited delivery. Kept as a live driver precisely so that can be tested.", "High", "Medium", "Wholesaler fee schedule"),
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
 ("team_pre", "Team per month before the non-Rx launch", "$", 4000, 6000, 9000,
  "Founder or GM plus fractional operations and contract creative. Small because the provider carries clinical and fulfilment operations. The Conservative column is deliberately a LEAN operator, not a normal operator with weak demand, so that the Conservative outcome reflects demand risk rather than an arbitrary spending choice.", "Medium", "Medium", "Hiring plan"),
 ("team_p1", "Team per month, non-Rx launch through month 12", "$", 10000, 16000, 26000,
  "A founder or general manager, one capable performance-media buyer, and part-time support. Deliberately small: the provider carries clinical operations, fulfilment and compliance administration, and the brand partner supplies much of the creative. A team larger than this is rebuilding in-house what the $600 fee already covers.", "Medium", "Medium", "Hiring plan"),
 ("team_p2", "Team per month, months 13-24", "$", 18000, 34000, 65000,
  "Scales with order volume and state count, but stays small relative to revenue because the provider carries clinical operations and fulfilment. A brand at this revenue running team above roughly 15% of net revenue has rebuilt in-house what it is already paying the provider for.", "Low", "Medium", "Hiring plan"),
 ("team_p3", "Team per month, months 25-36", "$", 26000, 55000, 110000,
  "", "Low", "Medium", "Hiring plan"),
 ("team_pct_floor", "Team cost floor as a share of net revenue", "%", 0.070, 0.060, 0.050,
  "Flat headcount steps are the classic way a model overstates profitability at scale: a brand doing tens of millions a month cannot be run by the team that ran it at one million. Team cost is therefore the GREATER of the step above and this share of revenue. It does not bind at Conservative or Baseline volumes; it binds hard in the Aggressive case, which is the point.", "Medium", "High", "Headcount plan against revenue per employee"),
 ("creative_pct_floor", "Creative and content floor as a share of net revenue", "%", 0.030, 0.025, 0.020,
  "Same correction applied to production. Creative volume has to grow with spend or the ads fatigue; 2-3% of revenue is a modest allowance for a brand whose whole acquisition model is creative-led.", "Medium", "Medium", "Agency scopes against spend"),
 ("tech_pct_floor", "Technology floor as a share of net revenue", "%", 0.010, 0.008, 0.006,
  "Storefront, subscription, support, data and consent tooling all price on volume. Flat SaaS line items stop being flat.", "Medium", "Low", "Vendor invoices against order volume"),
 ("med_lead", "Medical director and clinical oversight per month", "$", 5000, 9000, 14000,
  "Fractional medical director retainer. Compensation must never vary with prescription volume or revenue.", "Medium", "Low", "Executed agreement"),
 ("tech", "Technology and software per month", "$", 900, 1200, 2000,
  "Storefront, subscription management, analytics, consent management, CRM, helpdesk. Separate from the provider fee.", "High", "Low", "Vendor invoices"),
 ("legal_p0", "Legal and regulatory per month, months 1-3", "$", 12000, 15000, 20000,
  "Entity structure and MSO or friendly-PC review, provider agreement review, formulary eligibility opinion, claims and label review, endorsement and disclosure protocol, trademark, privacy. Front-loaded deliberately.", "Medium", "Low", "Counsel estimates"),
 ("legal_ongoing", "Legal and compliance per month thereafter", "$", 3000, 4500, 7000,
  "Ongoing claims review, state expansion opinions, FDA list monitoring, contract maintenance.", "Medium", "Medium", "Counsel estimates"),
 ("insurance", "Insurance per month from the non-Rx launch", "$", 1800, 2500, 3500,
  "Product liability, professional, cyber and D&O. A vendor contract does not transfer the brand's own liability.", "Medium", "Low", "Broker quotes"),
 ("creative", "Creative, content and organic social per month", "$", 3000, 6000, 12000,
  "Production the brand controls, distinct from paid media and from partner compensation. Materially lower than a comparable brand would spend, because a founder-partner posting several times a month supplies usable creative as a by-product. That saving is one of the concrete economic benefits of the partnership.", "Medium", "Medium", "Agency quotes"),
 ("SECTION", "Proposed brand-partner economics (hypothetical; no terms offered or accepted)"),
 ("partner_cash", "Partner cash retainer per month from the non-Rx launch", "$", 0, 15000, 25000,
  "Illustrative only. Structure, amount and mix are entirely unnegotiated. Conservative case models an equity-only deal with no cash retainer.", "n/a", "High", "Negotiation"),
 ("partner_royalty", "Partner royalty on net revenue", "%", 0.050, 0.050, 0.050,
  "Illustrative. Consumer-brand licensing royalties commonly 3-10%. Held flat across scenarios so the scenarios isolate business performance rather than deal terms.", "n/a", "High", "Negotiation"),
 ("partner_equity", "Partner equity, fully diluted (reference only)", "%", 0.10, 0.15, 0.20,
  "Illustrative. Non-cash; shown on the Partner_Economics sheet for reference and NOT charged to EBITDA.", "n/a", "n/a", "Negotiation"),
 ("SECTION", "Working capital"),
 ("inv_months", "Non-Rx inventory held, in months of COGS", "months", 0, 0, 0,
  "Zero: the wholesaler holds the stock and ships on order, so the brand never pays for inventory. This removes what was previously the largest single item in the cash trough. Set this above zero only if the brand later brings stock in-house, which is what a volume-tier manufacturing deal would require. The Rx line likewise carries no inventory; the pharmacy holds it.", "High", "Medium", "Wholesaler agreement"),
]

# A fourth scenario column: the Baseline business with NO brand partner. Every driver equals the
# Baseline value except the ones the partnership actually supplies. It exists so the partnership's
# contribution can be read as a number rather than asserted. Organic/SEO, pricing, cost structure and
# the whole operating base are deliberately held identical, so the difference isolates exactly four
# things: the partner's own social traffic, the branded-search and engagement-retargeting inventory
# that traffic creates, the creative lift on cold prospecting, and the partner's compensation.
NOPARTNER = {
    "followers": 0,                 # no partner audience
    "posts_per_month": 0,
    "launch_spike": 1.0,            # no announcement window
    "bsearch_per_reach": 0.0,       # no partner-driven branded search
    "retarget_pool_engagers": 0.0,  # no engagement audience to retarget
    "creative_disc": 1.00,          # no partner creative lift on cold prospecting
    "conv_mult_partner_organic": 1.0,
    "launch_push": 20000,           # a launch without a celebrity buys less attention
    "partner_cash": 0,
    "partner_royalty": 0.0,
    "partner_equity": 0.0,
    "creative": 12000,              # and it has to pay for all its own creative
}

# Two single-factor stress columns. A Conservative case built by setting EVERY driver to its low end is
# closer to a 1-in-100 outcome than a 1-in-10 one, because the pessimism compounds. These columns move one
# factor group at a time to the Conservative value and leave everything else at Baseline, which is what
# shows whether any single thing can sink the business on its own.
WEAK_AUDIENCE = ["posts_per_month", "reach_pct", "ctr_reach", "attn_floor", "launch_spike", "shop_conv"]
WEAK_RETENTION = ["sub_churn", "rx_churn", "onetime_repeat"]

ws = wb.active; ws.title = "Assumptions"
ws["A1"] = "Reserve Clinic - Margin and Growth Model: Assumptions"; ws["A1"].font = H1
ws["A2"] = ("Blue cells are the only inputs. Six scenario columns drive the six Model_ sheets. Columns G, H and I each equal "
            "Baseline on every driver except the ones shown in bold: G removes the brand partnership, H moves only the "
            "audience drivers to their Conservative values, and I moves only the churn drivers. G measures what the "
            "partnership contributes; H and I test whether any single factor can sink the business on its own. "
            "Yellow fill marks high-sensitivity drivers. Prepared 2026-09-18. Proposed concept: the brand partner's and the medical "
            "co-founder's participation is unverified and subject to definitive agreements. Not legal, medical, tax or investment advice.")
ws["A2"].font = ITAL
ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ws.merge_cells("A2:M2"); ws.row_dimensions[2].height = 58
EXTRA = [("G", "Baseline, no partner", None),
         ("H", "Baseline, weak audience", WEAK_AUDIENCE),
         ("I", "Baseline, weak retention", WEAK_RETENTION)]
hdrs = (["Key", "Driver", "Unit", "Conservative", "Baseline", "Aggressive"]
        + [lab for _, lab, _ in EXTRA]
        + ["Rationale / source", "Confidence", "Sensitivity", "Validation method"])
for i, h in enumerate(hdrs, 1):
    c = ws.cell(row=4, column=i, value=h); c.font = H2; c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="bottom")
GREYFILL = PatternFill("solid", fgColor="EDEDEA")
ROW = {}
VAL = {}
r = 5
for item in A:
    if item[0] == "SECTION":
        c = ws.cell(row=r, column=1, value=item[1]); c.font = BOLD
        for col in range(1, 14): ws.cell(row=r, column=col).fill = SUB
        r += 1; continue
    key, label, unit, cons, base, up, rat, conf, sens, valm = item
    ws.cell(row=r, column=1, value=key).font = Font(name=FONT, size=8, color="777777")
    ws.cell(row=r, column=2, value=label).font = BLACK
    ws.cell(row=r, column=3, value=unit).font = BLACK
    fmt_of = lambda v: ((PCT2 if unit == "%" and abs(float(v)) < 0.02 else PCT) if unit == "%" else (
        (CUR2 if unit == "$" and float(v) != int(float(v)) else CUR) if unit == "$" else (
            DEC if unit == "x" else ('0.0' if unit == "months" else NUM))))
    extras = {}
    for colL, lab, keys in EXTRA:
        if keys is None:
            extras[colL] = (NOPARTNER.get(key, base), key in NOPARTNER)
        else:
            extras[colL] = ((cons, True) if key in keys else (base, False))
    for col, v in zip((4, 5, 6), (cons, base, up)):
        c = ws.cell(row=r, column=col, value=v); c.font = BLUE
        c.number_format = fmt_of(v)
        if sens == "High": c.fill = YELLOW
    for i, (colL, lab, keys) in enumerate(EXTRA):
        v, overridden = extras[colL]
        c = ws.cell(row=r, column=7 + i, value=v)
        c.number_format = fmt_of(base); c.fill = GREYFILL
        c.font = Font(name=FONT, color="0000FF", size=10, bold=True) if overridden else BLUE
    base_col = 7 + len(EXTRA)
    cc = ws.cell(row=r, column=base_col, value=rat); cc.font = SMALL; cc.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=r, column=base_col + 1, value=conf).font = BLACK
    ws.cell(row=r, column=base_col + 2, value=sens).font = BLACK
    vc = ws.cell(row=r, column=base_col + 3, value=valm); vc.font = SMALL
    vc.alignment = Alignment(wrap_text=True, vertical="top")
    ROW[key] = r
    VAL[key] = {"Conservative": cons, "Baseline": base, "Aggressive": up,
                **{lab: extras[colL][0] for colL, lab, _ in EXTRA}}
    r += 1
for col, w in zip("ABCDEFGHIJKLM", (17, 52, 10, 12, 12, 12, 14, 14, 14, 70, 11, 11, 26)):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "D5"
ws.sheet_view.zoomScale = 90

SCN = {"Conservative": "D", "Baseline": "E", "Aggressive": "F", "No_Partner": "G",
       "Weak_Audience": "H", "Weak_Retention": "I"}
SCN_LABEL = {"Conservative": "Conservative", "Baseline": "Baseline", "Aggressive": "Aggressive",
             "No_Partner": "Baseline, no partner", "Weak_Audience": "Baseline, weak audience",
             "Weak_Retention": "Baseline, weak retention"}

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
    add("partner_impressions", "Partner-post impressions reached", "impressions",
        lambda m, c, p, a: (f"{a('followers')}*{a('posts_per_month')}*{a('reach_pct')}*{ref('attn_index',c)}"), NUM, "sum")
    add("organic_sessions", "Organic and direct sessions", "sessions",
        lambda m, c, p, a: f"MIN({a('organic_cap')},{a('organic_m1')}*(1+{a('organic_growth')})^({c}$5-1))", NUM, "sum")
    # ---- paid media budget, then allocated cheapest-CAC-first across three tiers
    add("paid_budget", "Paid media budget", "$",
        lambda m, c, p, a: (f"{a('paid_pre')}" if p is None else
                            f"IF({ref('is_nonrx',c)}=0,{a('paid_pre')},MIN({a('paid_cap')},MAX({a('paid_floor')},{ref('net_rev',p)}*{a('paid_pct')})))"), CUR, "sum", True)
    # tier 1: branded and intent search. Volume is capped by the demand the partner's posts create.
    add("search_available", "Branded and intent sessions available to buy", "sessions",
        lambda m, c, p, a: (f"({ref('partner_impressions',c)}*{a('bsearch_per_reach')}"
                            f"+{ref('organic_sessions',c)}*{a('bsearch_organic_factor')})*{a('bsearch_capture')}*{ref('is_nonrx',c)}"), NUM, "sum")
    add("search_spend", "Spend, branded and intent search", "$",
        lambda m, c, p, a: f"MIN({ref('paid_budget',c)},{ref('search_available',c)}*{a('cps_search')})", CUR, "sum")
    add("search_sessions", "Sessions, branded and intent search", "sessions",
        lambda m, c, p, a: f"{ref('search_spend',c)}/{a('cps_search')}", NUM, "sum")
    # tier 2: retargeting. Pool is site visitors plus the partner's post engagers.
    add("retarget_pool", "Addressable retargeting pool", "#",
        lambda m, c, p, a: (f"{ref('is_nonrx',c)}*({a('retarget_pool_engagers')}*{ref('partner_impressions',c)}"
                            + (")" if p is None else f"+{a('retarget_pool_sessions')}*{ref('sessions',p)})")), NUM, "last")
    add("retarget_available", "Retargeting sessions available to buy", "sessions",
        lambda m, c, p, a: f"{ref('retarget_pool',c)}*{a('retarget_freq')}", NUM, "sum")
    add("retarget_spend", "Spend, retargeting", "$",
        lambda m, c, p, a: (f"MIN(MAX(0,{ref('paid_budget',c)}-{ref('search_spend',c)}),"
                            f"{ref('retarget_available',c)}*{a('cps_retarget')})"), CUR, "sum")
    add("retarget_sessions", "Sessions, retargeting", "sessions",
        lambda m, c, p, a: f"{ref('retarget_spend',c)}/{a('cps_retarget')}", NUM, "sum")
    # tier 3: cold prospecting with partner creative. Takes the residual budget, with diminishing returns.
    add("prospect_spend", "Spend, cold prospecting", "$",
        lambda m, c, p, a: f"MAX(0,{ref('paid_budget',c)}-{ref('search_spend',c)}-{ref('retarget_spend',c)})", CUR, "sum")
    add("prospect_sessions", "Sessions, cold prospecting (diminishing returns and creative lift applied)", "sessions",
        lambda m, c, p, a: (f"({a('paid_floor')}/({a('cps_prospect')}*{a('creative_disc')}))"
                            f"*({ref('prospect_spend',c)}/{a('paid_floor')})^{a('paid_elast')}"), NUM, "sum")
    add("paid_spend", "Paid media spend, all tiers", "$",
        lambda m, c, p, a: f"{ref('search_spend',c)}+{ref('retarget_spend',c)}+{ref('prospect_spend',c)}", CUR, "sum", True)
    add("paid_sessions", "Paid sessions, all tiers", "sessions",
        lambda m, c, p, a: f"{ref('search_sessions',c)}+{ref('retarget_sessions',c)}+{ref('prospect_sessions',c)}", NUM, "sum")
    add("eff_cps", "Blended effective cost per paid session", "$",
        lambda m, c, p, a: f"IFERROR({ref('paid_spend',c)}/{ref('paid_sessions',c)},0)", CUR2, "avg")
    add("sessions", "Total sessions", "sessions",
        lambda m, c, p, a: f"{ref('partner_sessions',c)}+{ref('organic_sessions',c)}+{ref('paid_sessions',c)}", NUM, "sum", True)
    # ---- non-Rx funnel
    add("nonrx_capacity", "Shippable new-order capacity", "#",
        lambda m, c, p, a: f"{ref('is_nonrx',c)}*{a('cap_m1')}*{a('cap_growth')}^{ref('months_live',c)}", NUM, "last")
    add("nonrx_demand", "New non-Rx customer demand (conversion-weighted by source)", "#",
        lambda m, c, p, a: (f"{a('shop_conv')}*{ref('is_nonrx',c)}*("
                            f"{ref('organic_sessions',c)}"
                            f"+{ref('partner_sessions',c)}*{a('conv_mult_partner_organic')}"
                            f"+{ref('search_sessions',c)}*{a('conv_mult_search')}*{a('search_increment')}"
                            f"+{ref('retarget_sessions',c)}*{a('conv_mult_retarget')}*{a('retarget_increment')}"
                            f"+{ref('prospect_sessions',c)}*{a('conv_mult_prospect')})"), NUM, "sum")
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
    add("rx_weighted_sessions", "Prescription-intent-weighted sessions", "sessions",
        lambda m, c, p, a: (f"{ref('organic_sessions',c)}+{ref('search_sessions',c)}+{ref('retarget_sessions',c)}"
                            f"+({ref('partner_sessions',c)}+{ref('prospect_sessions',c)})*{a('rx_celeb_factor')}"), NUM, "sum")
    add("rx_quiz_starts", "Eligibility quiz starts", "#",
        lambda m, c, p, a: f"{ref('rx_weighted_sessions',c)}*{a('rx_intent')}*{ref('is_rx',c)}", NUM, "sum")
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
        lambda m, c, p, a: (f"-MAX(IF({ref('is_nonrx',c)}=0,{a('team_pre')},IF({c}$5<=12,{a('team_p1')},"
                            f"IF({c}$5<=24,{a('team_p2')},{a('team_p3')})))"
                            + ("" if p is None else f",{ref('net_rev',p)}*{a('team_pct_floor')}") + ")"), CUR, "sum")
    add("ox_med", "Medical director and clinical oversight", "$",
        lambda m, c, p, a: f"-IF({c}$5>={a('rx_launch')}-2,{a('med_lead')},0)", CUR, "sum")
    add("ox_tech", "Technology and software", "$",
        lambda m, c, p, a: ("-" + (f"{a('tech')}" if p is None else
                                   f"MAX({a('tech')},{ref('net_rev',p)}*{a('tech_pct_floor')})")), CUR, "sum")
    add("ox_legal", "Legal, regulatory and compliance", "$",
        lambda m, c, p, a: f"-IF({c}$5<=3,{a('legal_p0')},{a('legal_ongoing')})", CUR, "sum")
    add("ox_ins", "Insurance", "$",
        lambda m, c, p, a: f"-{ref('is_nonrx',c)}*{a('insurance')}", CUR, "sum")
    add("ox_creative", "Creative and content", "$",
        lambda m, c, p, a: ("-" + (f"{a('creative')}" if p is None else
                                   f"MAX({a('creative')},{ref('net_rev',p)}*{a('creative_pct_floor')})")), CUR, "sum")
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
    add("inv_balance", "Non-Rx inventory balance (zero under the wholesale dropship arrangement)", "$",
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
    add("cac_search", "CAC, branded and intent search (incremental)", "$",
        lambda m, c, p, a: (f"IFERROR({ref('search_spend',c)}/({ref('search_sessions',c)}*{a('shop_conv')}"
                            f"*{a('conv_mult_search')}*{a('search_increment')}),0)"), CUR2, "avg")
    add("cac_retarget", "CAC, retargeting (incremental)", "$",
        lambda m, c, p, a: (f"IFERROR({ref('retarget_spend',c)}/({ref('retarget_sessions',c)}*{a('shop_conv')}"
                            f"*{a('conv_mult_retarget')}*{a('retarget_increment')}),0)"), CUR2, "avg")
    add("cac_prospect", "CAC, cold prospecting", "$",
        lambda m, c, p, a: (f"IFERROR({ref('prospect_spend',c)}/({ref('prospect_sessions',c)}*{a('shop_conv')}"
                            f"*{a('conv_mult_prospect')}),0)"), CUR2, "avg")
    add("cac_paid_nonrx", "CAC, all paid tiers, non-Rx", "$",
        lambda m, c, p, a: (f"IFERROR({ref('paid_spend',c)}/(({ref('search_sessions',c)}*{a('conv_mult_search')}*{a('search_increment')}"
                            f"+{ref('retarget_sessions',c)}*{a('conv_mult_retarget')}*{a('retarget_increment')}"
                            f"+{ref('prospect_sessions',c)}*{a('conv_mult_prospect')})*{a('shop_conv')}),0)"), CUR2, "avg", True)
    add("payback_months", "Months for a non-Rx subscriber to repay paid CAC", "months",
        lambda m, c, p, a: f"IFERROR({ref('cac_paid_nonrx',c)}/{ref('nonrx_contrib_order',c)},0)", DEC, "avg", True)
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
for j, h in enumerate(["Metric", "Conservative", "Baseline", "Aggressive", "Baseline,\nno partner",
                       "Baseline,\nweak audience", "Baseline,\nweak retention"], 1):
    c = sm.cell(row=4, column=j, value=h); c.font = H2; c.fill = HDR
    c.alignment = Alignment(wrap_text=True, vertical="bottom")
rr = 5
for label, fn, fmt in metrics:
    if label == "SPACER":
        rr += 1; continue
    sm.cell(row=rr, column=1, value=label).font = BOLD
    for j, s in enumerate(("Conservative", "Baseline", "Aggressive", "No_Partner", "Weak_Audience", "Weak_Retention"), 2):
        c = sm.cell(row=rr, column=j, value=fn(s)); c.number_format = fmt; c.font = GREEN
        if s in ("No_Partner", "Weak_Audience", "Weak_Retention"): c.fill = GREYFILL
    rr += 1
for col, w in zip("ABCDEFG", (42, 16, 16, 16, 17, 17, 17)): sm.column_dimensions[col].width = w
sm.freeze_panes = "B5"

# ================================================================= UNIT ECONOMICS
ue = wb.create_sheet("Unit_Economics", 2)
ue["A1"] = "Unit economics: where the margin actually comes from"; ue["A1"].font = H1
ue["A2"] = ("Two separate businesses with very different shapes. The non-prescription line is a high-margin consumer product that can "
            "trade in all fifty states. The prescription line carries medication, clinician and cold-chain cost on every single fill, "
            "so its margin is structurally lower and its retention risk structurally higher.")
ue["A2"].font = ITAL; ue["A2"].alignment = Alignment(wrap_text=True, vertical="top")
ue.merge_cells("A2:F2"); ue.row_dimensions[2].height = 40

def ue_block(title, rows, start):
    ue.cell(row=start, column=1, value=title).font = Font(name=FONT, bold=True, size=11)
    for j, h in enumerate(["Line item", "Conservative", "Baseline", "Aggressive", "Baseline, no partner"], 1):
        c = ue.cell(row=start + 1, column=j, value=h); c.font = H2; c.fill = HDR
    r0 = start + 2
    for k, (lab, fn, fmt, bold) in enumerate(rows):
        ue.cell(row=r0 + k, column=1, value=lab).font = BOLD if bold else BLACK
        for j, s in enumerate(("Conservative", "Baseline", "Aggressive", "No_Partner"), 2):
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
def ue_col(scn): return {"Conservative": "B", "Baseline": "C", "Aggressive": "D", "No_Partner": "E"}[scn]

def ue_block2(title, rows, start):
    ue.cell(row=start, column=1, value=title).font = Font(name=FONT, bold=True, size=11)
    for j, h in enumerate(["Line item", "Conservative", "Baseline", "Aggressive", "Baseline, no partner"], 1):
        c = ue.cell(row=start + 1, column=j, value=h); c.font = H2; c.fill = HDR
    r0 = start + 2
    idx = {}
    for k, (tag, lab, fn, fmt, bold) in enumerate(rows):
        idx[tag] = r0 + k
    for k, (tag, lab, fn, fmt, bold) in enumerate(rows):
        row = r0 + k
        ue.cell(row=row, column=1, value=lab).font = BOLD if bold else BLACK
        for scn in ("Conservative", "Baseline", "Aggressive", "No_Partner"):
            uc = ue_col(scn); ac = SCN[scn]
            c = ue.cell(row=row, column={"B": 2, "C": 3, "D": 4, "E": 5}[uc],
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
    ue.merge_cells(start_row=nxt3 + 1 + i, start_column=1, end_row=nxt3 + 1 + i, end_column=5)
    ue.row_dimensions[nxt3 + 1 + i].height = 46
    for col in range(1, 6): ue.cell(row=nxt3 + 1 + i, column=col).fill = WARN
for col, w in zip("ABCDE", (56, 16, 16, 16, 19)): ue.column_dimensions[col].width = w

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
MREF = 24  # reference month for audience conditions
MC = L(2 + MREF)
sv["A42"] = "Grid 4. Paid CAC by monthly spend, with and without the brand partner"; sv["A42"].font = Font(name=FONT, bold=True, size=11)
sv["A43"] = ("The like-for-like answer to whether the partnership buys a better CAC. Both columns use identical Baseline "
             "drivers, identical prices and identical conversion rates. They differ only in the audience conditions of "
             f"month {MREF}: partner impressions, and the warm pools those impressions create. Read down: CAC rises with "
             "spend in both cases, because of the auction. Read across: at every spend level the partner column is cheaper, "
             "and the gap is what the partnership is actually buying.")
sv["A43"].font = SMALL; sv["A43"].alignment = Alignment(wrap_text=True, vertical="top")
sv.merge_cells("A43:H43"); sv.row_dimensions[43].height = 44
for j, h in enumerate(["Monthly paid spend", "Paid CAC, with partner", "Paid CAC, no partner",
                       "CAC advantage", "Advantage %"], 1):
    c = sv.cell(row=45, column=j, value=h); c.font = H2; c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="bottom")
spends = [15000, 30000, 60000, 120000, 250000, 500000, 1000000, 2500000]
for i, sp in enumerate(spends):
    row = 46 + i
    c = sv.cell(row=row, column=1, value=sp); c.font = BOLD; c.number_format = CUR
    for k, (scn, col) in enumerate((("Baseline", 2), ("No_Partner", 3))):
        # available warm volume at the reference month, taken straight from the recalculated model sheets
        avail_s = f"Model_{scn}!{MC}{R['search_available']}"
        avail_r = f"Model_{scn}!{MC}{R['retarget_available']}"
        ss = f"MIN($A{row},{avail_s}*{A_(B,'cps_search')})/{A_(B,'cps_search')}"
        rs = f"MIN(MAX(0,$A{row}-MIN($A{row},{avail_s}*{A_(B,'cps_search')})),{avail_r}*{A_(B,'cps_retarget')})/{A_(B,'cps_retarget')}"
        pspend = f"MAX(0,$A{row}-MIN($A{row},{avail_s}*{A_(B,'cps_search')})-MIN(MAX(0,$A{row}-MIN($A{row},{avail_s}*{A_(B,'cps_search')})),{avail_r}*{A_(B,'cps_retarget')}))"
        disc = A_(B, 'creative_disc') if scn == "Baseline" else A_("G", 'creative_disc')
        ps = f"({A_(B,'paid_floor')}/({A_(B,'cps_prospect')}*{disc}))*({pspend}/{A_(B,'paid_floor')})^{A_(B,'paid_elast')}"
        cust = (f"({ss}*{A_(B,'conv_mult_search')}*{A_(B,'search_increment')}"
                f"+{rs}*{A_(B,'conv_mult_retarget')}*{A_(B,'retarget_increment')}"
                f"+{ps}*{A_(B,'conv_mult_prospect')})*{A_(B,'shop_conv')}")
        cc = sv.cell(row=row, column=col, value=f"=IFERROR($A{row}/({cust}),0)")
        cc.number_format = CUR2; cc.font = BLACK
    sv.cell(row=row, column=4, value=f"=C{row}-B{row}").number_format = CUR2
    sv.cell(row=row, column=5, value=f"=IFERROR((C{row}-B{row})/C{row},0)").number_format = PCT
    sv.cell(row=row, column=4).font = BOLD; sv.cell(row=row, column=5).font = BOLD
sv.cell(row=55, column=1, value=("Note the shape. The advantage is largest at low spend, where the partner's cheap warm inventory is a big "
                                 "share of a small budget, and it narrows as budget grows and cold prospecting dominates. That is the correct "
                                 "reading of a celebrity partnership: it is a strong subsidy on the first tranche of spend, not a permanent "
                                 "discount on all of it.")).font = SMALL
sv.merge_cells("A55:H55"); sv.row_dimensions[55].height = 40
sv.cell(row=55, column=1).alignment = Alignment(wrap_text=True, vertical="top")

for col, w in zip("ABCDEFGH", (32, 14, 14, 14, 14, 14, 14, 14)): sv.column_dimensions[col].width = w

# ================================================================= PAID MEDIA
pm = wb.create_sheet("Paid_Media", 4)
pm["A1"] = "Targeted paid media: three tiers, allocated cheapest first"; pm["A1"].font = H1
pm["A2"] = ("The brand partnership does not lower the cost of advertising by magic. It works through three specific, "
            "measurable mechanisms, and each one is a separate tier below with its own volume ceiling, its own cost per "
            "session, its own conversion rate and its own incrementality haircut. The budget is set as a share of the "
            "prior month's net revenue, then filled from the cheapest tier upward: search first, retargeting second, "
            "cold prospecting takes whatever is left.")
pm["A2"].font = ITAL; pm["A2"].alignment = Alignment(wrap_text=True, vertical="top")
pm.merge_cells("A2:F2"); pm.row_dimensions[2].height = 58

hdr = ["Tier", "What it is", "How the partnership creates it", "Volume ceiling", "Incrementality haircut"]
for j, h in enumerate(hdr, 1):
    c = pm.cell(row=4, column=j, value=h); c.font = H2; c.fill = HDR; c.alignment = Alignment(wrap_text=True, vertical="bottom")
tiers = [
 ("1. Branded and intent search",
  "Paid search against the brand name and against category-intent queries. The cheapest inventory a brand owns, because it faces little auction competition on its own name.",
  "Every brand post sends some viewers to a search engine instead of to the link. That converts partner reach into cheap, high-intent paid inventory. Without the partner this tier is almost empty.",
  "Capped by the queries that actually exist: partner impressions times the branded-search rate, plus a baseline from organic, times the share you choose to buy.",
  "35-55% incremental. Paying for a query you would rank for organically buys a click you already had. Without this haircut the model would count the partner's organic traffic twice."),
 ("2. Retargeting",
  "Site visitors plus the partner's post engagers, reached again through platform custom and engagement audiences.",
  "Anyone who engaged with a brand post enters the platform's engagement audience. The partner's reach therefore builds a large warm pool at no media cost.",
  "Capped by the pool: addressable share of prior-month sessions, plus engagers generated per partner impression, times how hard the pool can be worked before fatigue.",
  "25-40% incremental, and this is the number that matters most. Benchmark B19: holdout tests show true incremental lift of only 25-30%, so up to 75% of retargeting conversions would have happened anyway."),
 ("3. Cold prospecting with partner creative",
  "Lookalike and broad audiences, run on creative featuring the partner.",
  "A recognisable face and partner-voiced video should raise click-through and so lower cost per session. This is the only tier where the partnership improves efficiency rather than creating volume.",
  "Effectively unlimited volume, but subject to diminishing returns: sessions scale as spend raised to the elasticity, so effective cost per session rises as spend grows.",
  "100%. Cold prospecting creates the demand the other two tiers harvest, which is exactly why it cannot be starved."),
]
r = 5
for t in tiers:
    for j, v in enumerate(t, 1):
        c = pm.cell(row=r, column=j, value=v)
        c.font = BOLD if j == 1 else SMALL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    pm.row_dimensions[r].height = 104
    r += 1

r += 1
pm.cell(row=r, column=1, value="What this structure does and does not claim").font = Font(name=FONT, bold=True, size=11)
claims = [
 "IT DOES claim the partnership lowers blended acquisition cost AT A GIVEN LEVEL OF SPEND, because it shifts the mix toward cheap high-intent inventory and discounts the cold tier through better creative. The grid on the Sensitivity sheet measures exactly that, holding everything else equal.",
 "IT DOES NOT claim blended CAC falls as the business grows. It rises, in every scenario, because scale pushes spend further out on the diminishing-returns curve. A model showing CAC falling with scale is a model with no auction in it. The partnership's real benefit is that it raises the spend level at which CAC stays acceptable.",
 "IT DOES NOT take the widely quoted 40-70% retargeting CPA advantage at face value. After the incrementality haircut, retargeting's INCREMENTAL cost per customer comes out roughly level with cold prospecting at Baseline drivers. Run a holdout test in month two: if incrementality lands at the low end of the band, that budget belongs in prospecting instead.",
 "IT ASSUMES the partner's likeness can be used in paid media. Organic posting rights and paid-usage rights are licensed separately, and paid healthcare creative additionally faces platform ad review and needs LegitScript certification. Confirm both before building the paid plan around partner creative.",
 "IT EXCLUDES the prescription line from partner creative entirely. Compounded prescription products are not promoted by the partner, so prescription intent is weighted down on partner-driven and cold-prospecting traffic and comes instead from search, editorial content and on-site cross-sell.",
]
for i, n in enumerate(claims):
    c = pm.cell(row=r + 1 + i, column=1, value=n); c.font = SMALL
    c.alignment = Alignment(wrap_text=True, vertical="top")
    pm.merge_cells(start_row=r + 1 + i, start_column=1, end_row=r + 1 + i, end_column=5)
    pm.row_dimensions[r + 1 + i].height = 52
    for col in range(1, 6): pm.cell(row=r + 1 + i, column=col).fill = WARN
for col, w in zip("ABCDE", (30, 44, 44, 44, 50)): pm.column_dimensions[col].width = w

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
for j, h in enumerate(["Item", "Conservative", "Baseline", "Aggressive"], 1):  # no-partner column omitted by design
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
  "at a flat $600 per month. Paid media is modelled as three separately-priced tiers rather than one blended "
  "number, because that is the mechanism by which a brand partner's audience lowers acquisition cost. "
  "Four columns: Conservative, Baseline, Aggressive, and Baseline with no brand partner at all."),
 ("What it is not",
  "Not a forecast, not a valuation, and not legal, medical, tax or investment advice. The outputs follow arithmetically from the drivers "
  "on the Assumptions sheet. Change a driver and the answer changes. Several of the most consequential drivers rest on analyst "
  "assumptions rather than measurements, and those are labelled Low confidence with a stated validation method."),
 ("Status of the people named",
  "The proposed brand partner and the proposed medical co-founder are treated strictly as proposed. No public evidence connects either "
  "to this venture, no agreement exists, and nothing in this workbook is an offer or implies endorsement, ownership or authorisation. "
  "Partner compensation figures are illustrative arithmetic, not terms."),
 ("Colour key",
  "Blue = editable input, on the Assumptions sheet only; bold blue in the last column marks a driver the no-partner case overrides. "
  "Black = formula. Green = link to another sheet. Yellow fill = high-sensitivity driver: get these wrong and the answer changes "
  "materially. Grey fill = the no-partner comparison column. Peach fill = a caution the reader should not skip."),
 ("Sheet order",
  "Summary reads the four columns side by side. Unit_Economics shows where margin comes from per order and per member-month. "
  "Paid_Media explains the three ad tiers and what the structure does and does not claim. Sensitivity holds four grids: "
  "prescription LTV:CAC by churn and CAC, partner-driven sessions by reach and click-through, blended gross margin by "
  "COGS and pharmacy cost, and paid CAC by spend level with and without the partner. Partner_Economics is illustrative "
  "deal arithmetic. Provider_Diligence is the twenty questions to answer in writing before signing. Benchmarks is the "
  "evidence. Assumptions holds every input. The four Model_ sheets are the monthly grids."),
 ("What the fourth column is for",
  "Model_No_Partner is the same business with no brand partner. Organic search, pricing, cost structure, the provider, "
  "the team plan and the whole operating base are held identical; only the four things the partnership actually supplies "
  "differ, namely the partner's own social traffic, the branded-search and engagement-retargeting inventory that traffic "
  "creates, the creative lift on cold prospecting, and the partner's compensation. It exists so that the partnership's "
  "contribution is a number rather than an assertion. Holding organic and press identical understates rather than "
  "flatters the partnership."),
 ("On the claim that a celebrity buys a better CAC",
  "The model does not assume it. It derives it, through three mechanisms with explicit ceilings, and then applies an "
  "incrementality haircut to the two warm tiers because the evidence demands one: holdout tests show only 25-30% of "
  "retargeting conversions are incremental. Sensitivity grid 4 is the like-for-like answer, holding everything else "
  "equal. Two results matter. Blended CAC RISES with spend in every scenario, because of the auction; any model where "
  "it falls with scale has no competition in it. And the partnership's advantage is largest on the first tranche of "
  "spend and narrows as budget grows, which is an argument for spending into it early rather than trickling it."),
 ("The four things most likely to be wrong",
  "1. Audience conversion. Reach per post and click-through are multiplied together and neither is measured; Sensitivity grid 2 shows the "
  "spread. 2. The partner-creative cost discount. No study quantifying celebrity or recognisable-face advertising lift was retrievable "
  "(B20); the supporting evidence is only general. A creative A/B test with and without the partner in month one is how this stops being "
  "an assumption. 3. Prescription retention. Benchmark B17 puts real-world discontinuation near 65% at twelve months; Sensitivity grid 1 "
  "shows that above roughly 15% monthly churn the prescription line does not pay for its own acquisition at any plausible CAC. "
  "4. The provider's scope. A $600 flat fee is roughly one fifth of the low end of published market pricing for comparable turnkey "
  "telehealth infrastructure, so the model assumes it covers software and administration only and carries every variable cost separately."),
 ("Structural limits the model encodes deliberately",
  "Fifty-state coverage applies to the non-prescription line only. The prescription line ramps from 26-45% of the US population at launch "
  "to a 70-88% ceiling, because asynchronous-prescribing rules, corporate-practice-of-medicine limits and the section 503A(b)(3) five "
  "percent interstate distribution cap all constrain it. FDA's compounding memorandum-of-understanding index currently lists three MOUs, "
  "all suspended, and FDA has repeatedly deferred enforcement of the five percent limit pending rulemaking. Deferred enforcement is "
  "discretionary and revocable. Every one of these areas needs qualified counsel: FDA and pharmacy regulatory, corporate practice of "
  "medicine, healthcare privacy, advertising and endorsement, consumer protection and auto-renewal, and intellectual property."),
 ("Prepared", "2026-09-18. Rebuild with: python3 build/build_margin_model.py outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx, "
  "then recalculate with LibreOffice, then python3 build/extract_margin_values.py and python3 build/build_margin_proposal.py."),
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
print(f"{len(ROW)} drivers, {len(LINES)} model lines, {MONTHS} months, {len(SCN)} scenarios")
