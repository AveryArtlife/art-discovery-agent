"""Build ReserveClinic_Margins_and_Growth_Proposal.pdf.

A partner-facing proposal on profit margins and growth potential for the proposed Reserve Clinic
peptide and supplement business: three scenarios, the unit economics beneath them, what has to be
true, and what to do next. Every figure traces to outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx
or to research/07_margin_growth_benchmarks.json.
"""
import json, os, re, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, CondPageBreak, Flowable)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdf_lib import (S, P, SRC, CALLOUT, BUL, KICK, H1, H2, H3, T, IMG, MONO, STATS, md, esc,
                     INK, MOSS, BRASS, BONE, MUTED, LINE, PALE, CAT, PAGE_W, PAGE_H, LM, RM, TM, BM, CW,
                     money, num)
from logo import draw_logo
import margin_charts as MC

OUT = sys.argv[1] if len(sys.argv) > 1 else "outputs/ReserveClinic_Margins_and_Growth_Proposal.pdf"
MV = json.load(open(os.path.join(HERE, "margin_values.json")))
BM_ = json.load(open(os.path.join(HERE, "..", "research", "07_margin_growth_benchmarks.json")))
CH = MC.build_all(MV, os.path.join(HERE, "charts"))
ch = lambda n: os.path.join(CH, n)

SUM = MV["summary"]; ASM = MV["assum"]; MON = MV["monthly"]
SCN = ["Conservative", "Baseline", "Aggressive"]
DATE = "18 September 2026"


def sv(metric, scn):
    return SUM[metric][scn]


def m3(metric, fmt=money, **kw):
    return [fmt(sv(metric, s), **kw) if not isinstance(sv(metric, s), str) else sv(metric, s) for s in SCN]


def pct(v, dec=0):
    return "n/a" if v is None else f"{v*100:.{dec}f}%"


def a3(key, fmt=None):
    d = ASM[key]
    out = []
    for s in SCN:
        v = d[s]
        if fmt: out.append(fmt(v))
        elif d["unit"] == "%": out.append(pct(v, 2 if abs(v) < 0.01 else (1 if abs(v) < 0.1 else 0)))
        elif d["unit"] == "$": out.append(f"${v:,.0f}" if float(v) == int(float(v)) else f"${v:,.2f}")
        elif d["unit"] == "x": out.append(f"{v:.2f}x")
        else: out.append(f"{v:,.0f}")
    return out


# ------------------------------------------------------------------ document shell
class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=letter, leftMargin=LM, rightMargin=RM, topMargin=TM,
                         bottomMargin=BM, title="Reserve Clinic - Margins and Growth Proposal",
                         author="Prepared for the Reserve Clinic project owner", **kw)
        self.section = ""
        frame = Frame(LM, BM, CW, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        cover = Frame(0, 0, PAGE_W, PAGE_H, id="c", leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[cover], onPage=self._cover),
                               PageTemplate(id="main", frames=[frame], onPageEnd=self._main)])

    def _cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(MOSS); canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        draw_logo(canv, LM, PAGE_H - 1.7 * inch, 0.78 * inch, on_dark=True)
        canv.setFillColor(BRASS); canv.rect(LM, PAGE_H * 0.655, 62, 3, fill=1, stroke=0)
        canv.restoreState()

    def _main(self, canv, doc):
        canv.saveState()
        canv.setFont("Sans", 7.2); canv.setFillColor(MUTED)
        canv.drawString(LM, PAGE_H - 0.55 * inch, "Reserve Clinic - Profit Margins and Growth Potential")
        canv.drawRightString(PAGE_W - RM, PAGE_H - 0.55 * inch, self.section[:74])
        canv.setStrokeColor(LINE); canv.setLineWidth(0.5)
        canv.line(LM, PAGE_H - 0.62 * inch, PAGE_W - RM, PAGE_H - 0.62 * inch)
        canv.line(LM, 0.62 * inch, PAGE_W - RM, 0.62 * inch)
        canv.drawString(LM, 0.42 * inch,
                        f"Proposed concept - confidential working draft - {DATE} - not legal, medical, tax or investment advice")
        canv.drawRightString(PAGE_W - RM, 0.42 * inch, f"Page {doc.page}")
        canv.restoreState()

    def afterFlowable(self, fl):
        if hasattr(fl, "_toc"):
            lvl, txt = fl._toc
            key = "h%d" % id(fl); self.canv.bookmarkPage(key)
            self.notify("TOCEntry", (lvl, txt, self.page, key))
            if lvl == 0: self.section = re.sub(r"^\d+\.\s+", "", txt)
            self.canv.addOutlineEntry(re.sub(r"<[^>]+>", "", txt), key, level=lvl, closed=(lvl > 0))


def cover_para(t, style): return Paragraph(t, S[style])  # raw: cover text carries its own <br/> markup

F = []
# ================================================================= COVER
F += [Spacer(1, PAGE_H * 0.395),
      Table([[cover_para("Profit Margins and<br/>Growth Potential", "cover_t")]],
            colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LM), ("TOPPADDING", (0, 0), (-1, -1), 0)]),
      Spacer(1, 16),
      Table([[cover_para("A three-scenario view of the proposed Reserve Clinic peptide and supplement business", "cover_s")]],
            colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LM)]),
      Spacer(1, 46),
      Table([[cover_para(
          f"Prepared for review by the proposed brand partner &amp; the project owner<br/>"
          f"{DATE}<br/><br/>"
          "Proposed concept. The brand partner's and the medical co-founder's participation is unverified "
          "and subject to definitive agreements. Nothing in this document is an offer, an endorsement, or "
          "a representation that anyone has agreed to anything. Every figure is a model output produced by "
          "stated assumptions, not a forecast. Not legal, medical, tax or investment advice.", "cover_m")]],
          colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LM)]),
      NextPageTemplate("main"), PageBreak()]

# ================================================================= 1. THE ANSWER
F += [H1("1.  The answer, in one page")]
F += [P("You asked two questions: what the margins look like, and how big this could get. Here they are, "
        "before any of the reasoning.")]

be = {s: sv("First EBITDA-positive month", s) for s in SCN}
F += [Spacer(1, 4),
      T([["", "Conservative", "Baseline", "Aggressive"],
         ["Net revenue, year 1"] + m3("Net revenue, year 1"),
         ["Net revenue, year 3"] + m3("Net revenue, year 3"),
         ["Net revenue, 36 months"] + m3("Net revenue, 36-month total"),
         ["Blended gross margin, year 3"] + [pct(sv("Blended gross margin, year 3", s), 0) for s in SCN],
         ["EBITDA, year 3"] + m3("EBITDA, year 3"),
         ["EBITDA margin, year 3"] + [pct(sv("EBITDA margin, year 3", s), 0) for s in SCN],
         ["First profitable month"] + [(be[s] if isinstance(be[s], str) else f"month {be[s]:.0f}") for s in SCN],
         ["Capital required"] + m3("Capital required (deficit plus 30% buffer)"),
         ], widths=[2.3 * inch, (CW - 2.3 * inch) / 3, (CW - 2.3 * inch) / 3, (CW - 2.3 * inch) / 3],
        font=8.6, align_right_cols=(1, 2, 3))]
F += [SRC("outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx, Summary sheet. Model outputs, not forecasts. "
          "Capital required is the deepest cumulative cash trough plus a 30% buffer.")]

F += [H2("The margin answer")]
NX_CM_PCT = MON["Baseline"]["nonrx_contrib_order"][-1] / (ASM["nonrx_aov"]["Baseline"] * (1 - ASM["refund_pct"]["Baseline"]))
F += [P("**Gross margins are genuinely good, and they are good for two different reasons.** The supplement line "
        f"keeps about {pct(NX_CM_PCT, 0)} of each order after product cost, shipping and card fees — "
        f"${MON['Baseline']['nonrx_contrib_order'][-1]:,.0f} of contribution on a "
        f"${ASM['nonrx_aov']['Baseline']:,.0f} order. The prescription line keeps less of each dollar, about "
        f"{pct(sv('Rx gross margin, year 3','Baseline'),0)}, but each dollar is larger and it recurs: "
        f"${MON['Baseline']['rx_contrib_mm'][-1]:,.0f} of contribution per member per month.")]
F += [P("**The constraint is not margin. It is retention and reach.** At baseline drivers a prescription member is "
        f"worth roughly ${MON['Baseline']['rx_ltv'][-1]:,.0f} in gross lifetime contribution and a supplement subscriber "
        f"roughly ${MON['Baseline']['nonrx_ltv'][-1]:,.0f}. Both comfortably clear a "
        f"${sv('Blended CAC, year 3 average','Baseline'):,.0f} acquisition cost. Whether the business is a "
        "$700 thousand curiosity or a $139 million company over three years turns almost entirely on how many people "
        "the audience actually delivers, and how long they stay.")]

F += [H2("The growth answer")]
F += [P(f"**Baseline builds a real but modest business:** ${sv('Net revenue, year 3','Baseline')/1e6:.1f}M of year-3 "
        f"revenue, roughly break-even, on about ${sv('Capital required (deficit plus 30% buffer)','Baseline')/1e6:.1f}M "
        f"of capital, with {SUM['Active subscribers at month 36 (non-Rx)']['Baseline']:,.0f} "
        f"supplement subscribers and {SUM['Active programme members at month 36 (Rx)']['Baseline']:,.0f} prescription members "
        "on the books at month 36. The value in that case is the asset, not the year-three cash.")]
F += [P(f"**Aggressive is the case the comparables say is possible:** ${sv('Net revenue, year 3','Aggressive')/1e6:.0f}M "
        f"of year-3 revenue at a {pct(sv('EBITDA margin, year 3','Aggressive'),0)} EBITDA margin. For scale, IM8 — "
        "co-founded by David Beckham, whose Instagram audience is roughly three times larger — reportedly reached $100 million "
        f"in eleven months. Our aggressive case reaches ${sv('Net revenue, year 1','Aggressive')/1e6:.1f}M in year one. "
        "The aggressive scenario here is less aggressive than the best celebrity supplement launch on record.")]
F += [P("**Conservative is the case worth reading twice.** If the audience converts at the low end, the business never "
        "covers its own fixed cost base within three years and consumes about "
        f"${sv('Capital required (deficit plus 30% buffer)','Conservative')/1e6:.1f}M finding that out. That is not a "
        "pessimism exercise; it is the arithmetic of running a compliance-grade operation — counsel, a medical director, "
        "insurance, certification — on top of a business doing $35 thousand a month.")]

F += [CALLOUT("**The single most useful thing in this document is not a number, it is a sequence.** "
              "The supplement line can trade in all fifty states, needs no prescriber, carries the better margin, and is the "
              "only line the brand partner can promote. The prescription line needs the provider, the pharmacies, the "
              "state-by-state licensure map and a medical director, and it is the line that cannot be promoted by a "
              "celebrity. Launching the first and earning the right to the second is both the cheaper path and the "
              "defensible one.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 2. TWO BUSINESSES
F += [H1("2.  This is two businesses, and they behave differently")]
F += [P("Treating the venture as one company with one margin is the most common way these models go wrong. "
        "The two lines have different legal footprints, different cost structures, different growth ceilings and "
        "different promotional rules. The model keeps them separate throughout.")]
F += [Spacer(1, 6),
      T([["", "Non-prescription supplement line", "Prescription telehealth line"],
         ["What it is", "DSHEA-compliant supplements and topicals sold through an open consumer checkout.",
          "Compounded peptide programmes prescribed after a clinical consult and dispensed by a licensed pharmacy."],
         ["Geographic reach", "All fifty states from day one.",
          f"Starts at {pct(ASM['state_cov_launch']['Baseline'],0)} of the US population and ramps toward a "
          f"{pct(ASM['state_cov_cap']['Baseline'],0)} ceiling. Fifty-state prescription coverage is not available on day one."],
         ["Gross margin (year 3, baseline)", pct(sv("Non-Rx gross margin, year 3", "Baseline"), 0),
          pct(sv("Rx gross margin, year 3", "Baseline"), 0)],
         ["Unit of value", f"${MON['Baseline']['nonrx_contrib_order'][-1]:,.0f} contribution per order; "
                           f"${MON['Baseline']['nonrx_ltv'][-1]:,.0f} per subscriber over their life.",
          f"${MON['Baseline']['rx_contrib_mm'][-1]:,.0f} contribution per member-month; "
          f"${MON['Baseline']['rx_ltv'][-1]:,.0f} per member over their life."],
         ["Main risk", "Retention and the cost of paid acquisition once the audience effect fades.",
          "Retention, which is materially worse in this category, plus regulatory dependence on which peptides remain compoundable."],
         ["Can the brand partner promote it?", "Yes, with clear and conspicuous disclosure of the material connection on every post.",
          "No. Specific compounded prescription products should not be promoted by a celebrity partner. This is a design "
          "constraint, not a preference."],
         ["Share of year-3 revenue (baseline)", pct(sv("Non-Rx share of year-3 net revenue", "Baseline"), 0),
          pct(1 - sv("Non-Rx share of year-3 net revenue", "Baseline"), 0)],
         ], widths=[1.45 * inch, (CW - 1.45 * inch) / 2, (CW - 1.45 * inch) / 2], font=8.0)]
F += [SRC("Model outputs plus the regulatory constraints recorded in research/07_margin_growth_benchmarks.json (B18) and the "
          "compliance matrix in the main business plan. Every legal statement here needs confirmation by qualified FDA, "
          "pharmacy, corporate-practice-of-medicine and advertising counsel before it is relied on.")]

F += [H2("Why the prescription line cannot simply be switched on nationally")]
F += [P("Three separate constraints stack on top of each other, and each one is live rather than theoretical:")]
F += BUL([
  "**Licensure and asynchronous prescribing.** A clinician must be licensed in the patient's state, and states differ on "
  "whether a questionnaire-based visit is enough to establish a prescriber-patient relationship. Some states are simply "
  "excluded from an asynchronous model.",
  "**Corporate practice of medicine.** Many states bar a non-physician company from owning a medical practice or sharing "
  "professional fees. That is why the prescribing entity has to be a separate physician-owned company paid a flat, "
  "fair-market management fee — never a share of revenue or a payment per prescription.",
  "**The five percent interstate cap.** Section 503A(b)(3) limits a compounding pharmacy to distributing 5% of its "
  "prescription orders across state lines unless its state has signed FDA's memorandum of understanding. FDA's compounding "
  "MOU index currently lists three MOUs, and all three are suspended. FDA has repeatedly deferred enforcement of the 5% "
  "limit while rulemaking is pending. Deferred enforcement is discretionary and revocable, so a national single-pharmacy "
  "prescription model is a policy bet rather than a settled structure. A multi-state pharmacy network is the durable answer.",
])
F += [CALLOUT("**Read that as sequencing, not as a blocker.** The supplement line has none of these problems. It is the "
              "line that funds the licensure work, proves the audience converts, and builds the customer list the "
              "prescription line later sells into.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 3. MARGIN ANATOMY
F += [H1("3.  Where the margin actually comes from")]
F += [P("Both charts below show where each dollar of net revenue goes at baseline drivers. Nothing is allocated or "
        "averaged; these are the actual per-unit costs the business incurs on every order and every fill.")]
F += [Spacer(1, 4), IMG(ch("m_water.png"), width=CW), Spacer(1, 2)]
F += [SRC("Baseline column of the Assumptions sheet. Non-prescription costs benchmarked to a 20-30% landed-COGS band (B03); "
          "prescription costs to compounded-peptide programme pricing (B07), asynchronous consult cost (B08) and cold-chain "
          "fulfilment quotes (B09).")]

F += [H2("The three costs that decide the prescription margin")]
F += [P("Medication, clinician time and cold-chain shipping together consume about "
        f"{pct((ASM['pharm_cost']['Baseline']+ASM['refill_cost']['Baseline']+ASM['coldchain_ship']['Baseline'])/(ASM['rx_price']['Baseline']*(1-ASM['refund_pct']['Baseline'])),0)} "
        "of each prescription dollar. Two of those three are negotiable at volume and one is not:")]
F += [Spacer(1, 4),
      T([["Cost", "Baseline", "Negotiable?", "What moves it"],
         ["Pharmacy medication, per member-month", f"${ASM['pharm_cost']['Baseline']:,.0f}", "Yes, at volume",
          "A written tiered schedule. This is the largest single variable cost in the model and the first thing to get in writing."],
         ["Cold-chain fulfilment and shipping, per fill", f"${ASM['coldchain_ship']['Baseline']:,.0f}", "Barely",
          "Temperature-controlled two-day service has a floor. Longer refill cadences — 90-day supply instead of 30 — cut the "
          "number of cold shipments and are the real lever here."],
         ["Clinician monitoring, per member-month", f"${ASM['refill_cost']['Baseline']:,.0f}", "Somewhat",
          "Must be paid per unit of clinical work, never as a share of revenue. That constraint is not negotiable."],
         ], widths=[2.1 * inch, 0.8 * inch, 1.0 * inch, CW - 3.9 * inch], font=8.0)]
F += [P("**The shipping cadence is the most under-appreciated margin lever in the whole model.** Moving a member from a "
        "30-day to a 90-day fill removes two cold-chain shipments per quarter. At baseline that is "
        f"${ASM['coldchain_ship']['Baseline']*2:,.0f} of cost per member per quarter, which is roughly "
        f"{pct(ASM['coldchain_ship']['Baseline']*2/(ASM['rx_price']['Baseline']*3),0)} of quarterly revenue recovered "
        "with no price change and no new customer. Whether the formulary and stability data allow it is a clinical and "
        "pharmacy question worth asking early.")]

F += [H2("What the flat $600 monthly provider fee does and does not change")]
F += [P("The flat fee is genuinely powerful: it removes almost all fixed operating cost from the model. A conventional "
        "version of this business carries a telehealth platform, an EHR, a provider network, pharmacy operations and a "
        "compliance function as monthly overhead. Here that is $600.")]
F += [P("**It does not remove variable cost, and the model does not assume it does.** Medication, per-consult clinician "
        "time, cold-chain shipping and card processing all scale with every order and every fill, and each is carried as "
        "a separate driver. The reason for that caution is specific: published pricing for comparable turnkey telehealth "
        "infrastructure runs $3,000 to $6,000 per month by tier, plus $5,000 to $10,000 of onboarding, plus per-consult "
        "fees. A $600 flat fee sits at roughly one fifth of the low end of that range.")]
F += [CALLOUT("**That gap has only two explanations and both lead to the same action.** Either the fee covers software and "
              "compliance administration only — which is how this model treats it, and is the safe reading — or the scope "
              "is narrower than expected. Get the fee schedule in writing and confirm line by line what is included. "
              "The Provider_Diligence sheet in the workbook has the twenty questions, and the three that matter most are: "
              "are per-consult fees included, does the pharmacy bill per fill, and who holds the LegitScript certification "
              "and for which website.")]
F += [P("One further point that is easy to miss. At $600 a month the provider carries no volume risk and has no economic "
        "stake in the brand's growth. That is excellent for margin and poor for alignment: nothing in the fee structure "
        "funds the provider's own scaling. Consult turnaround, fill turnaround, capacity ceilings and what happens when "
        "they are exceeded all need to be contractual rather than assumed.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 4. THE ENGINE
F += [H1("4.  The growth engine is the audience, and it has four dials")]
F += [P("Most of the spread between the three scenarios comes from four numbers. They are multiplied together, which is "
        "why a plausible-looking change in each produces a very wide range in the answer. Stating them separately is the "
        "point: each one is measurable within weeks of going live, so the band narrows fast once there is real data.")]
F += [Spacer(1, 4), IMG(ch("m_aud.png"), width=CW), Spacer(1, 2)]
F += [SRC("Baseline drivers, model month 12. Follower count from third-party trackers (B16): 27,410,219 as of June 2026, "
          "range 27.0M to 28.3M across sources. Not an audited or first-party figure.")]
F += [Spacer(1, 6),
      T([["Dial", "Conservative", "Baseline", "Aggressive", "Evidence"],
         ["Brand posts per month"] + a3("posts_per_month") + ["A contract deliverable, not a market variable."],
         ["Reach per post, share of followers"] + a3("reach_pct") +
         ["Analyst assumption. The 10M-plus tier averages about 1.77% ENGAGEMENT (B15); reach exceeds engagement, but "
          "organic reach at this tier is heavily throttled and branded content more so."],
         ["Click-through per reached impression"] + a3("ctr_reach") +
         ["Analyst assumption. No tier-level link-click benchmark was retrievable. **This is the least evidenced number "
          "in the model.**"],
         ["Order conversion, all sessions"] + a3("shop_conv") +
         ["DTC supplement conversion is commonly 0.5-1.5%. A warm follower audience should sit at the top of that band, "
          "though sources warn mega-tier audiences convert worse than their reach implies (B15)."],
         ], widths=[1.45 * inch, 0.95 * inch, 0.88 * inch, 0.88 * inch, CW - 4.16 * inch], font=7.8,
        align_right_cols=(1, 2, 3))]
F += [Spacer(1, 8), IMG(ch("m_reach.png"), width=CW), Spacer(1, 2)]
F += [SRC("Sensitivity sheet, grid 2. Month-12 partner-driven sessions per month at baseline posting cadence and decay.")]
F += [P("The grid is the honest version of the growth question. Read down the rows and across the columns and the answer "
        "moves by two orders of magnitude on two numbers nobody can yet measure. Any single-point projection for this "
        "business is a guess dressed as an estimate.")]

F += [H2("Attention decays, and the model makes it decay")]
F += [P(f"Partner-driven traffic is modelled with a launch spike of {ASM['launch_spike']['Baseline']:.1f}x, then monthly "
        f"decay toward a floor of {pct(ASM['attn_floor']['Baseline'],0)} of the launch peak. That floor is the durable "
        "follower demand that persists after novelty. It matters because a model without decay makes a celebrity launch "
        "look like a permanent acquisition channel, and it is not one. Notably, IM8's founders said publicly that they "
        "deliberately did not lean on the fame, but on whether the product worked. The floor is where product quality "
        "shows up in the arithmetic.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 5. SCENARIOS
F += [H1("5.  The three scenarios")]
F += [P("Same cost structure, same product, same provider. What differs is how much the audience delivers, how long "
        "customers stay, how fast the supply chain can scale, and how disciplined the spend is.")]
F += [Spacer(1, 4), IMG(ch("m_traj.png"), width=CW), Spacer(1, 6), IMG(ch("m_years.png"), width=CW), Spacer(1, 2)]
F += [SRC("Model outputs. Left panel is log-scaled because the three scenarios differ by roughly three orders of magnitude. "
          "Right-hand cash panel is clipped at $3M so the troughs stay legible.")]
F += [Spacer(1, 6),
      T([["Metric", "Conservative", "Baseline", "Aggressive"],
         ["Net revenue, year 1"] + m3("Net revenue, year 1"),
         ["Net revenue, year 2"] + m3("Net revenue, year 2"),
         ["Net revenue, year 3"] + m3("Net revenue, year 3"),
         ["Gross profit, year 3"] + m3("Gross profit, year 3"),
         ["Blended gross margin, year 3"] + [pct(sv("Blended gross margin, year 3", s), 1) for s in SCN],
         ["EBITDA, year 3"] + m3("EBITDA, year 3"),
         ["EBITDA margin, year 3"] + [pct(sv("EBITDA margin, year 3", s), 1) for s in SCN],
         ["EBITDA, 36-month cumulative"] + m3("EBITDA, 36-month total"),
         ["First EBITDA-positive month"] + [(be[s] if isinstance(be[s], str) else f"month {be[s]:.0f}") for s in SCN],
         ["Peak cumulative cash deficit"] + m3("Peak cumulative cash deficit"),
         ["Capital required, incl. 30% buffer"] + m3("Capital required (deficit plus 30% buffer)"),
         ["Supplement subscribers at month 36"] + [num(sv("Active subscribers at month 36 (non-Rx)", s)) for s in SCN],
         ["Prescription members at month 36"] + [num(sv("Active programme members at month 36 (Rx)", s)) for s in SCN],
         ["Blended CAC, year 3"] + [f"${sv('Blended CAC, year 3 average', s):,.0f}" for s in SCN],
         ["Supplement LTV:CAC, year 3"] + [f"{sv('Non-Rx LTV:CAC, year 3', s):.1f}x" for s in SCN],
         ], widths=[2.35 * inch, (CW - 2.35 * inch) / 3, (CW - 2.35 * inch) / 3, (CW - 2.35 * inch) / 3],
        font=8.2, align_right_cols=(1, 2, 3))]
F += [SRC("outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx, Summary sheet. Every cell traces to a formula over the "
          "Assumptions sheet; there are no hard-coded results.")]
F += [CondPageBreak(3.5 * inch)]

F += [H2("What separates the three")]
F += [Spacer(1, 2),
      T([["", "Conservative", "Baseline", "Aggressive"],
         ["The story", "The audience underperforms, the supplement line stays niche, the prescription line launches late "
                        "and small. Run lean and find out cheaply.",
          "The audience performs at the middle of the plausible range. A real brand gets built. Roughly break-even by "
          "year three, with the value sitting in the subscriber base.",
          "The audience performs like the best celebrity supplement launches on record, retention holds, and the supply "
          "chain keeps up."],
         ["Monthly churn, supplements"] + a3("sub_churn"),
         ["Monthly churn, prescription"] + a3("rx_churn"),
         ["Prescription line goes live"] + [f"month {ASM['rx_launch'][s]:.0f}" for s in SCN],
         ["Paid media, share of prior-month revenue"] + a3("paid_pct"),
         ["First-month shippable order capacity"] + a3("cap_m1"),
         ["What would make you believe it", "Month-one link-click data comes in at or below 0.35% of reached impressions.",
          "Month-one click-through near 0.6% and month-three subscription churn at or under 7%.",
          "Month-one click-through near 0.9%, conversion above 1.8%, and a manufacturer able to ship 3,000 orders in "
          "the first live month."],
         ], widths=[1.9 * inch, (CW - 1.9 * inch) / 3, (CW - 1.9 * inch) / 3, (CW - 1.9 * inch) / 3], font=7.8)]
F += [Spacer(1, 8), IMG(ch("m_mix.png"), width=CW), Spacer(1, 2)]
F += [SRC("Baseline scenario. The supplement line carries the revenue early and stays the majority of it; the prescription "
          "line adds revenue at a lower margin, which is why blended margin drifts down as it grows.")]
F += [P("That downward drift in the blended line is worth naming, because it looks like deterioration and is not. It is "
        "mix. Adding a 47%-margin prescription business to a 60%-margin supplement business lowers the average while "
        "increasing both total gross profit and revenue per customer. The question to ask of the prescription line is not "
        "whether it dilutes margin — it does — but whether its contribution per member covers its acquisition cost. "
        "At baseline it does, comfortably.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 6. WHAT DECIDES IT
F += [H1("6.  Retention is the thing most likely to break this")]
F += [P("Of every assumption in the model, prescription churn is the one where the outside evidence is strongest and least "
        "encouraging. In the closest comparable population, discontinuation approaches 65% within twelve months and 84.4% "
        "by twenty-four. A real-world telehealth provider reported programme retention of 78%, 63% and 58% at three, six "
        "and nine months. Trade commentary describes a 2026 retention cliff as the category's central problem.")]
F += [Spacer(1, 4), IMG(ch("m_ltvcac.png"), width=CW), Spacer(1, 2)]
F += [SRC("Sensitivity sheet, grid 1, computed from the baseline drivers. LTV is contribution per member-month divided by "
          "monthly churn; the 3.0x floor is the conventional minimum for a healthy subscription business (B06).")]
F += [P(f"The grid says something specific. At the baseline contribution of ${MV['sens']['contrib_mm']:.0f} per member-month, "
        "the prescription line clears the 3.0x floor across a wide range of acquisition costs as long as churn stays near "
        "11%. Above roughly 15% monthly churn it stops working at any plausible CAC. That is not a distant edge case: 15% "
        "monthly churn is what 84% annual discontinuation looks like.")]
F += [CALLOUT("**So retention is not a metric to monitor, it is the product roadmap.** Longer fill cadences, real clinical "
              "check-ins, outcome tracking, and honest expectation-setting at intake are the levers. A brand that solves "
              "retention in this category has a durable business; one that does not has an expensive customer treadmill, "
              "whatever the gross margin says.")]

F += [H2("Three other things that would change the answer materially")]
F += [Spacer(1, 2),
      T([["Risk", "Why it bites", "What to do about it now"],
         ["Which peptides stay compoundable",
          "The formulary is set by FDA's 503A bulk drug substances list, and it moves. FDA removed twelve peptides from "
          "Category 2 in April 2026; the advisory committee met in July 2026 on three more and will meet again before the "
          "end of February 2027 on five others. A product can become uncompoundable between signing and launch.",
          "Verify the formulary against the live FDA list on the day you sign, not from any summary including this one. "
          "Put a tracking obligation on the provider in the contract. Do not build the revenue plan on a single molecule."],
         ["LegitScript certification",
          "Certification is site-specific and gates healthcare advertising on Google, Meta, Microsoft and TikTok, and is "
          "close to a prerequisite for card-not-present acceptance. If the provider holds it on the provider's domain, "
          "your site may not be covered. Without it, most of the paid-acquisition line in the model disappears.",
          "Confirm in writing who holds it and for which website. Budget about $3,100 in year one and $2,150 a year after "
          "that per site, and confirm the live schedule."],
         ["Endorsement disclosure",
          "Every paid or equity-holding endorsement requires a clear and conspicuous disclosure of the material connection, "
          "on every post and in every format. A founder's equity stake is a material connection. Earlier research in this "
          "project found the proposed partner named on the FTC's September 2017 list of influencers sent warning letters "
          "about undisclosed endorsements, so this is a specific and personal exposure here rather than a generic one.",
          "Write the disclosure protocol before the first post, not after. Require pre-publication review of brand content. "
          "Keep the partner away from prescription-product claims entirely."],
         ], widths=[1.35 * inch, (CW - 1.35 * inch) * 0.52, (CW - 1.35 * inch) * 0.48], font=7.6)]
F += [SRC("research/07_margin_growth_benchmarks.json entries B10, B15, B18, plus the compliance matrix and celebrity-founder "
          "research in the main business plan. All of this requires confirmation by qualified counsel.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 7. CATEGORY CONTEXT
F += [H1("7.  Category context, honestly labelled")]
F += [P("Market-size numbers in this category are routinely misused, so here is the version with the labels attached. "
        "The large figures are not addressable by a cash-pay consumer brand; the addressable slice is the bottom two rows.")]
F += [Spacer(1, 4), IMG(ch("m_market.png"), width=CW), Spacer(1, 2)]
F += [SRC("Vendor market reports with wide disagreement between firms; 2026 estimate to 2030 estimate. Peptide "
          "therapeutics estimates alone range from $54.6B to $164B depending on scope. The bottom two rows are "
          "order-of-magnitude analyst estimates, not measurements. Treat all of it as directional.")]
F += [P("Two things in that picture are genuinely useful. First, the direction and the pace: cited growth rates of 7-11% "
        "a year across both the supplement and peptide categories mean the tide is moving the right way, which is not "
        "true of every consumer category right now. Second, the size of the directly addressable niche — a few billion "
        f"dollars — is large enough that the aggressive case (${sv('Net revenue, year 3','Aggressive')/1e6:.0f}M of year-3 "
        "revenue) represents a low single-digit share of it. The model is not assuming category dominance.")]

F += [H2("What the comparables actually show")]
F += [Spacer(1, 2),
      T([["Comparable", "Audience", "Reported outcome", "What it tells us"],
         ["IM8 (David Beckham)", "~88M Instagram followers",
          "Reportedly $100M in eleven months; about $120M ARR in year one.",
          "The aggressive case is achievable. Note the founders stated they deliberately did not rely on the fame but on "
          "whether the product worked."],
         ["Gruns", "Celebrity-backed, creator-led",
          "Profitable fourteen months in; nine-figure ARR; a reported $500M valuation.",
          "Profitability at scale is reachable, but it took over a year even with a strong launch."],
         ["SHREDZ", "Influencer-led",
          "$90k in its first year (2012); $5M the following year.",
          "The downside case is real. The spread between SHREDZ and IM8 is roughly three orders of magnitude, which is "
          "exactly why the scenario band here is wide."],
         ["Hims & Hers", "Listed telehealth, no celebrity founder",
          "74% gross margin in FY2025 falling to 63.8% in Q2 2026; marketing about 35-40% of revenue.",
          "The margin ceiling for a telehealth business at scale, and a warning: their margin fell as they added "
          "fulfilment-heavy weight-loss offerings. Ours carries cold chain from day one."],
         ], widths=[1.2 * inch, 1.15 * inch, (CW - 2.35 * inch) * 0.46, (CW - 2.35 * inch) * 0.54], font=7.7)]
F += [SRC("Press reporting and self-reported revenue for the private companies; company filings and earnings releases for "
          "Hims & Hers. None of the private figures is audited. Full citations in research/07_margin_growth_benchmarks.json "
          "entries B01, B02 and B14.")]
F += [P("The Hims & Hers row deserves a second look, because it is the only audited comparable in the table and it "
        "carries a specific warning. Their gross margin fell roughly ten points as weight-loss offerings with shorter "
        "shipping cadences and higher fulfilment costs grew into the mix. That is precisely the dynamic our prescription "
        "line has from day one. It is the reason this model carries cold-chain shipping as an explicit per-fill cost "
        "rather than burying it in a blended margin assumption.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 8. CAPITAL
F += [H1("8.  What it costs to find out")]
F += [Spacer(1, 2), IMG(ch("m_cap.png"), width=CW), Spacer(1, 2)]
F += [SRC("Capital required is the deepest cumulative cash trough in each scenario plus a 30% buffer. It excludes any "
          "cash retainer to the brand partner beyond what is modelled, and excludes a valuation event.")]
F += [P("The counter-intuitive result is worth explaining: **the aggressive case needs the least capital.** That is not a "
        "modelling error. Celebrity-driven traffic carries no media cost, so in the aggressive case revenue arrives before "
        "most of the spending does and the business funds itself from month three. In the conservative case the same "
        "fixed cost base — counsel, medical director, insurance, certification, a small team — has to be carried for three "
        "years against revenue that never catches it.")]
F += [CALLOUT("**Which means the real capital question is not how much, it is how long before you know.** The four dials "
              f"in section 4 are all measurable within sixty days of the supplement line going live. A staged commitment — "
              f"fund the supplement launch, read the dials, then decide on the prescription build — converts a "
              f"${sv('Capital required (deficit plus 30% buffer)','Conservative')/1e6:.1f}M open-ended bet into a much "
              "smaller, time-boxed one.")]

F += [H2("Where the money goes, baseline, first twelve months")]
b12 = lambda k: sum(MON["Baseline"][k][:12])
items = [("Paid media", -b12("ox_paid")), ("Creative and content", -b12("ox_creative"))]
F += [Spacer(1, 2),
      T([["Category", "First 12 months, baseline", "Note"],
         ["Paid media", money(-b12("ox_paid")), "Scales with revenue, capped, and subject to a payback gate."],
         ["Creative and content", money(-b12("ox_creative")), "Production the brand controls. Separate from partner compensation."],
         ["Team", money(12 * ASM["team_p1"]["Baseline"]), "Deliberately small; the provider carries clinical operations and fulfilment."],
         ["Legal and regulatory", money(4 * ASM["legal_p0"]["Baseline"] + 8 * ASM["legal_ongoing"]["Baseline"]),
          "Front-loaded on purpose: entity structure, provider agreement review, formulary opinion, claims and label review, "
          "endorsement protocol, privacy."],
         ["Medical oversight", money(9 * ASM["med_lead"]["Baseline"]), "Fractional medical director. Never compensated on prescription volume."],
         ["Launch marketing and PR", money(ASM["launch_push"]["Baseline"]), "One-time, concentrated in the launch month."],
         ["Provider fee", money(12 * ASM["provider_fee"]["Baseline"]), "$600 a month. The whole point of the structure."],
         ["Certification, technology, insurance", money(12 * (ASM["cert_cost"]["Baseline"] + ASM["tech"]["Baseline"] + ASM["insurance"]["Baseline"])),
          "LegitScript, storefront and subscription tooling, product and professional liability cover."],
         ["Partner cash retainer", money(11 * ASM["partner_cash"]["Baseline"]), "Illustrative only. No terms offered or accepted."],
         ], widths=[1.9 * inch, 1.3 * inch, CW - 3.2 * inch], font=8.0, align_right_cols=(1,))]
F += [P("Note the shape of that list. Legal and regulatory spend is comparable to team cost in year one, and that is "
        "correct rather than excessive. In this category the compliance work is not overhead on the business; it is the "
        "part that makes the business sellable, bankable and insurable.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 9. PARTNER ECONOMICS
F += [H1("9.  Illustrative partner economics")]
F += [CALLOUT("**No terms have been offered, negotiated or accepted, and nothing on this page is an offer.** It exists so "
              "the conversation can start from arithmetic rather than adjectives. The equity figures apply an illustrative "
              "revenue multiple and are not a valuation.")]
F += [P(f"The structure modelled is a {pct(ASM['partner_royalty']['Baseline'],0)} royalty on net revenue, a monthly cash "
        "retainer, and an equity stake. The royalty is held identical across all three scenarios on purpose, so the "
        "scenarios compare business performance rather than deal terms.")]
F += [Spacer(1, 4),
      T([["", "Conservative", "Baseline", "Aggressive"],
         ["Cash retainer, per month"] + a3("partner_cash"),
         ["Royalty on net revenue"] + a3("partner_royalty"),
         ["Equity, fully diluted (reference)"] + a3("partner_equity"),
         ["Cash retainer over 36 months"] + [money(ASM["partner_cash"][s] * 34) for s in SCN],
         ["Royalty over 36 months"] + [money(sv("Net revenue, 36-month total", s) * ASM["partner_royalty"][s]) for s in SCN],
         ["Total cash over 36 months"] + [money(ASM["partner_cash"][s] * 34 + sv("Net revenue, 36-month total", s) * ASM["partner_royalty"][s]) for s in SCN],
         ["Royalty in year 3 alone"] + [money(sv("Net revenue, year 3", s) * ASM["partner_royalty"][s]) for s in SCN],
         ["Illustrative equity value at 3x year-3 revenue"] + [money(sv("Net revenue, year 3", s) * 3.0 * ASM["partner_equity"][s]) for s in SCN],
         ], widths=[2.6 * inch, (CW - 2.6 * inch) / 3, (CW - 2.6 * inch) / 3, (CW - 2.6 * inch) / 3],
        font=8.2, align_right_cols=(1, 2, 3))]
F += [SRC("Partner_Economics sheet. The 3x revenue multiple is editable in the workbook and is illustrative: 2-5x net "
          "revenue is a commonly quoted range for profitable consumer health at scale, but multiples move with growth, "
          "margin and rate cycles. This is not a valuation and no valuation process has been run.")]

F += [H2("Four constraints any deal here has to respect")]
F += BUL([
  "**The partner promotes the brand and the supplement line, never specific compounded prescription products.** 503A "
  "compounders operate under advertising and promotion limits, prescription-drug promotion carries its own disclosure "
  "requirements, and celebrity promotion of a prescription product invites exactly the scrutiny a new brand cannot "
  "absorb. Separating what is promotable from what is prescribable is a design requirement.",
  "**Every endorsement carries a clear and conspicuous disclosure of the material connection, on every post, in every "
  "format.** A founder's equity stake is a material connection. Given the FTC warning-letter history noted in section 6, "
  "this needs a written protocol and pre-publication review, not good intentions.",
  "**Clinical compensation may never vary with prescribing or revenue.** Partner compensation may be tied to revenue; "
  "the medical entity's and the clinicians' may not. Keeping those two facts in separate contracts is the entire point of "
  "the three-entity structure.",
  "**Category exclusivity has to be resolved before any announcement.** Earlier research in this project flagged a "
  "possible prior GLP-1-adjacent promotion by the proposed partner; the brand and whether it was paid were not verified. "
  "A concurrent or recent competing endorsement is a diligence item, not a footnote.",
])
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 10. NEXT 90 DAYS
F += [H1("10.  The first ninety days")]
F += [P("Everything above is a model. The purpose of the next ninety days is to replace its four weakest assumptions with "
        "measurements, and to do the structural work that cannot be shortcut, before committing serious capital.")]
F += [Spacer(1, 4),
      T([["Weeks", "Work", "What it settles"],
         ["1-2", "Provider diligence. Put all twenty questions on the Provider_Diligence sheet in writing and get written "
                 "answers. Priority: are per-consult fees inside the $600, does the pharmacy bill per fill, who holds "
                 "LegitScript and for which site, which pharmacies and which states, and 503A versus 503B for each product.",
          "Whether the cost structure in this model is the real one. Nothing else is worth doing until this is answered."],
         ["1-4", "Counsel engagement across five areas: entity structure and corporate practice of medicine, the provider "
                 "and pharmacy agreements, product and claims review for the supplement line, the endorsement and "
                 "disclosure protocol, and auto-renewal and privacy compliance.",
          "Whether the structure is defensible. This is the spend that makes the rest insurable and financeable."],
         ["2-6", "Supplement line build: contract manufacturer selection and run schedule, label and claims review, 3PL "
                 "onboarding, storefront, subscription mechanics with a cancellation path as easy as the sign-up path.",
          "The first-month shippable capacity number, which binds hard in the aggressive case."],
         ["4-8", "Formulary verification against the live FDA 503A bulk drug substances list, plus a written tracking "
                 "obligation on the provider. Confirm nothing in the planned range is essentially a copy of an approved drug.",
          "Which prescription products can legally exist. Do not take this from any summary, including this document."],
         ["6-10", "Audience test. A small number of disclosed brand posts driving UTM-tagged traffic to a live storefront "
                  "with real inventory. Measure reach per post, click-through per reached impression, order conversion and "
                  "first-cohort subscription attach.",
          "Three of the four dials in section 4. This single test narrows the scenario band more than any other activity."],
         ["10-13", "Read the data and decide. Re-run the model on measured drivers. Decide whether to fund the prescription "
                   "build, extend the supplement-only test, or stop.",
          "Whether this is the baseline case, the aggressive case, or the conservative case. You will know by month three, "
          "not month thirty."],
         ], widths=[0.62 * inch, (CW - 0.62 * inch) * 0.56, (CW - 0.62 * inch) * 0.44], font=7.8)]
F += [CALLOUT("**The recommendation is to launch the supplement line first and alone.** It is fifty-state legal, carries "
              "the better margin, is the only line the partner can promote, needs no prescriber or pharmacy, and it "
              "measures all four growth dials for a fraction of the cost of the full build. If the dials come in at "
              "baseline or better, the prescription line becomes a funded decision made on evidence. If they come in at "
              "conservative, you have learned that for a few hundred thousand dollars instead of two million.")]
F += [CondPageBreak(3.5 * inch)]

# ================================================================= 11. HOW BUILT
F += [H1("11.  How these numbers were built, and what to distrust")]
F += [P("Every figure in this document is a formula over the Assumptions sheet of "
        "outputs/09_ReserveClinic_Margin_and_Growth_Model.xlsx. There are no hard-coded results in the monthly grids. "
        "The workbook recalculates cleanly: 9,361 formulas, zero errors. Change any driver and every number here moves.")]
F += [H2("The three things most likely to be wrong")]
F += BUL([
  "**Audience conversion.** Reach per post and click-through are multiplied together and neither is measured. Section 4's "
  "grid shows the spread. This is the largest source of uncertainty in the document by a wide margin.",
  "**Prescription retention.** The outside evidence points to worse retention than the model assumes at baseline. "
  "Section 6 shows where it stops working.",
  "**The provider's scope.** A $600 flat fee is roughly one fifth of the low end of published market pricing for "
  "comparable turnkey infrastructure. The model assumes it covers software and administration only, and carries every "
  "variable cost separately. If that assumption is wrong in the generous direction, margins improve; if the scope is "
  "narrower than described, the whole structure needs rethinking.",
])
F += [H2("What could not be verified in this environment")]
F += BUL([b for b in BM_["not_retrievable"]])
F += [H2("Evidence base")]
F += [P(f"The model's drivers rest on {len(BM_['benchmarks'])} documented benchmarks recorded in "
        "research/07_margin_growth_benchmarks.json and reproduced on the Benchmarks sheet of the workbook, each with its "
        "finding, how it is used, a confidence rating and its sources. Figures were taken from search-result summaries "
        "during a session in which direct page loads were restricted; load-bearing figures were corroborated across two "
        "independent queries. Ranges are ranges, not measurements.")]
F += [Spacer(1, 4),
      T([["ID", "Topic", "Confidence"]] +
        [[b["id"], b["topic"], b["confidence"]] for b in BM_["benchmarks"]],
        widths=[0.5 * inch, CW - 1.9 * inch, 1.4 * inch], font=7.6)]
F += [H2("Status of the people named, restated")]
F += [P("Scott Disick and Dr Michael Azziz are treated strictly as proposed participants. No public evidence connects "
        "either to this venture. No agreement exists. Nothing in this document implies endorsement, ownership or "
        "authorisation, and no part of it should be shared as though terms exist. Earlier research in this project could "
        "not verify a physician with the exact spelling 'Michael Azziz'; the closest candidate was identified at roughly "
        "60% confidence and requires direct confirmation of identity, licensure and credentials before any use of the name.")]
F += [H2("Required professional review")]
F += [P("This document identifies legal and regulatory issues; it is not legal, medical, tax or investment advice and must "
        "not be used as any of them. Before acting on any part of it, obtain review from qualified counsel in each of: FDA "
        "and drug-compounding regulation; state pharmacy law; corporate practice of medicine and fee-splitting; telehealth "
        "licensure and asynchronous prescribing; healthcare privacy including HIPAA, the FTC Health Breach Notification "
        "Rule and state health-data statutes; advertising, endorsement and claims substantiation; consumer protection and "
        "auto-renewal including ROSCA and state analogues; product liability; and intellectual property. Clinical protocol "
        "design, formulary selection and patient safety are decisions for licensed clinicians, not for this model.")]

doc = Doc(OUT)
toc = TableOfContents(); toc.levelStyles = [S["toc0"], S["toc1"]]
doc.multiBuild(F)
print(f"wrote {OUT}")
