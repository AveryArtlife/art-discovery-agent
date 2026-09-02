"""Abridged 6-page brief for the proposed brand partner. Reuses pdf_lib fonts/styles; illustrations drawn with reportlab.graphics."""
import sys, json
sys.path.insert(0, "build")
from pdf_lib import *
from reportlab.graphics.shapes import Drawing, Rect, Circle, Line, String, Polygon, Wedge, Path
from reportlab.graphics import renderPDF
from reportlab.platypus import Flowable, KeepTogether

mv = json.load(open("build/model_values.json")); SM = mv["summary"]
BE = int(SM["Break-even month (first positive EBITDA)"]["Base"]); CAP = money(SM["Capital required (peak burn + 15% contingency)"]["Base"]); Y3 = money(SM["Year 3 net revenue"]["Base"])

MOSS_H = "#1F3D33"; BRASS_H = "#B08D57"; BONE_H = "#F6F3EE"; INK_H = "#14171C"; MUTED_H = "#6B7079"; PALE_H = "#E7EDE9"; ROSE_H = "#F3E3DF"; SAGE_H = "#CFE0D6"
B = {}
B["body"] = ParagraphStyle("bb", fontName="Sans", fontSize=10.6, leading=15.5, textColor=INK, spaceAfter=7)
B["lead"] = ParagraphStyle("bl", fontName="Sans", fontSize=11.8, leading=16.5, textColor=INK, spaceAfter=8)
B["h1"] = ParagraphStyle("bh1", fontName="Serif-Bold", fontSize=26, leading=30, textColor=MOSS, spaceAfter=8)
B["h2"] = ParagraphStyle("bh2", fontName="Serif-Bold", fontSize=14.5, leading=18, textColor=INK, spaceBefore=10, spaceAfter=5)
B["kick"] = ParagraphStyle("bk", fontName="Sans-Bold", fontSize=8.5, leading=11, textColor=BRASS, spaceAfter=3)
B["small"] = ParagraphStyle("bs", fontName="Sans", fontSize=8.4, leading=11.5, textColor=MUTED, spaceAfter=4)
B["bul"] = ParagraphStyle("bbul", parent=B["body"], leftIndent=14, bulletIndent=3, spaceAfter=4)
B["card_t"] = ParagraphStyle("ct", fontName="Sans-Bold", fontSize=10.5, leading=13, textColor=INK)
B["card_b"] = ParagraphStyle("cb", fontName="Sans", fontSize=8.8, leading=11.8, textColor=INK)
B["big"] = ParagraphStyle("bg", fontName="Serif-Bold", fontSize=21, leading=24, textColor=MOSS)
B["biglabel"] = ParagraphStyle("bgl", fontName="Sans", fontSize=8.6, leading=11, textColor=MUTED)
B["cover_t"] = ParagraphStyle("bct", fontName="Serif-Bold", fontSize=40, leading=44, textColor=colors.white)
B["cover_s"] = ParagraphStyle("bcs", fontName="Serif", fontSize=17, leading=23, textColor=colors.HexColor("#E6E9E3"))
B["cover_m"] = ParagraphStyle("bcm", fontName="Sans", fontSize=10, leading=14.5, textColor=colors.HexColor("#C9D3CC"))

def p(t, s="body"): return Paragraph(md(t), B[s])
def bul(items): return [Paragraph(md(i), B["bul"], bulletText="•") for i in items]

class D(Flowable):
    """wrap a Drawing"""
    def __init__(self, d): super().__init__(); self.d = d; self.width = d.width; self.height = d.height
    def draw(self): renderPDF.draw(self.d, self.canv, 0, 0)

def rrect(d, x, y, w, h, fill, stroke=None, r=8, sw=0.8):
    rc = Rect(x, y, w, h, rx=r, ry=r, fillColor=colors.HexColor(fill), strokeColor=(colors.HexColor(stroke) if stroke else None), strokeWidth=sw); d.add(rc)
def txt(d, x, y, s, size=9, font="Sans", color=INK_H, anchor="start"):
    d.add(String(x, y, s, fontName=font, fontSize=size, fillColor=colors.HexColor(color), textAnchor=anchor))
def arrow(d, x1, y1, x2, y2, color=MUTED_H, w=1.2):
    d.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor(color), strokeWidth=w))
    import math
    ang = math.atan2(y2 - y1, x2 - x1); L = 6
    d.add(Polygon([x2, y2, x2 - L * math.cos(ang - 0.45), y2 - L * math.sin(ang - 0.45), x2 - L * math.cos(ang + 0.45), y2 - L * math.sin(ang + 0.45)], fillColor=colors.HexColor(color), strokeColor=None))

# ---------------- icons (abstract, monochrome)
def icon_book(d, cx, cy, c=MOSS_H):
    rrect(d, cx - 13, cy - 10, 26, 20, "#FFFFFF", c, r=3, sw=1.4); d.add(Line(cx, cy - 10, cx, cy + 10, strokeColor=colors.HexColor(c), strokeWidth=1.4))
    for i, dy in enumerate((5, 0, -5)):
        d.add(Line(cx - 9, cy + dy, cx - 3, cy + dy, strokeColor=colors.HexColor(c), strokeWidth=1)); d.add(Line(cx + 3, cy + dy, cx + 9, cy + dy, strokeColor=colors.HexColor(c), strokeWidth=1))
def icon_shield(d, cx, cy, c=MOSS_H):
    d.add(Polygon([cx - 12, cy + 9, cx, cy + 13, cx + 12, cy + 9, cx + 11, cy - 4, cx, cy - 13, cx - 11, cy - 4], fillColor=colors.white, strokeColor=colors.HexColor(c), strokeWidth=1.4))
    d.add(Line(cx - 5, cy, cx - 1, cy - 4, strokeColor=colors.HexColor(c), strokeWidth=1.8)); d.add(Line(cx - 1, cy - 4, cx + 6, cy + 5, strokeColor=colors.HexColor(c), strokeWidth=1.8))
def icon_bag(d, cx, cy, c=MOSS_H):
    rrect(d, cx - 11, cy - 11, 22, 18, "#FFFFFF", c, r=3, sw=1.4)
    d.add(Path(points=None, fillColor=None, strokeColor=colors.HexColor(c), strokeWidth=1.4))
    d.add(Wedge(cx, cy + 6, 6, 0, 180, strokeColor=colors.HexColor(c), strokeWidth=1.4, fillColor=None))
def icon_person(d, cx, cy, c=MOSS_H):
    d.add(Circle(cx, cy + 6, 5, fillColor=colors.white, strokeColor=colors.HexColor(c), strokeWidth=1.4))
    d.add(Wedge(cx, cy - 11, 12, 0, 180, fillColor=colors.white, strokeColor=colors.HexColor(c), strokeWidth=1.4))
def icon_check(d, cx, cy, c=MOSS_H):
    d.add(Circle(cx, cy, 12, fillColor=colors.HexColor(SAGE_H), strokeColor=None)); d.add(Line(cx - 6, cy, cx - 2, cy - 4, strokeColor=colors.HexColor(c), strokeWidth=2)); d.add(Line(cx - 2, cy - 4, cx + 7, cy + 5, strokeColor=colors.HexColor(c), strokeWidth=2))
def icon_x(d, cx, cy, c="#9E3B2E"):
    d.add(Circle(cx, cy, 12, fillColor=colors.HexColor(ROSE_H), strokeColor=None)); d.add(Line(cx - 5, cy - 5, cx + 5, cy + 5, strokeColor=colors.HexColor(c), strokeWidth=2)); d.add(Line(cx - 5, cy + 5, cx + 5, cy - 5, strokeColor=colors.HexColor(c), strokeWidth=2))
def icon_pill(d, cx, cy, c=MOSS_H):
    rrect(d, cx - 14, cy - 6, 28, 12, "#FFFFFF", c, r=6, sw=1.4); d.add(Line(cx, cy - 6, cx, cy + 6, strokeColor=colors.HexColor(c), strokeWidth=1.4))
def icon_flask(d, cx, cy, c=MOSS_H):
    d.add(Polygon([cx - 4, cy + 12, cx + 4, cy + 12, cx + 4, cy + 2, cx + 12, cy - 11, cx - 12, cy - 11, cx - 4, cy + 2], fillColor=colors.white, strokeColor=colors.HexColor(c), strokeWidth=1.4))
    d.add(Polygon([cx - 8, cy - 5, cx + 8, cy - 5, cx + 11, cy - 10, cx - 11, cy - 10], fillColor=colors.HexColor(SAGE_H), strokeColor=None))

# ---------------- illustrations
def ill_timeline():
    d = Drawing(CW, 118); y = 58
    d.add(Line(30, y, CW - 30, y, strokeColor=colors.HexColor("#C9CDC8"), strokeWidth=2))
    nodes = [("2023", "FDA restricts ~19 popular\npeptides for compounding", MUTED_H), ("2024–25", "GLP-1s go mainstream;\npodcasts make peptides a\nhousehold word", MUTED_H), ("2025–26", "FDA and DOJ clear out\n'research-use-only' sellers\nand misleading GLP-1 ads", MUTED_H), ("2026", "Federal reversal reopens\ncompounding for several\npeptides (final rule pending)", MOSS_H)]
    xs = [60, 60 + (CW - 120) / 3, 60 + 2 * (CW - 120) / 3, CW - 60]
    for (yr, lab, c), x in zip(nodes, xs):
        d.add(Circle(x, y, 9 if c == MOSS_H else 7, fillColor=colors.HexColor(BRASS_H if c == MOSS_H else "#FFFFFF"), strokeColor=colors.HexColor(c), strokeWidth=2))
        txt(d, x, y + 18, yr, 10, "Sans-Bold", c, "middle")
        for i, l in enumerate(lab.split("\n")): txt(d, x, y - 22 - i * 11, l, 8.2, "Sans", INK_H, "middle")
    return D(d)

def ill_layers():
    d = Drawing(CW, 132); w = (CW - 24) / 3
    cards = [("Learn", icon_book, "A plain-language library. Every peptide gets an FDA-status badge and an honest evidence grade — including the ones we don't sell."), ("Get care", icon_shield, "A 3-minute eligibility check, then an independent licensed clinician decides. Licensed US pharmacies fill it. No open cart for prescriptions."), ("Shop", icon_bag, "A separate store for non-prescription products that meet our standards. Nothing 'research-use-only', ever.")]
    for i, (t, ic, body) in enumerate(cards):
        x = i * (w + 12)
        rrect(d, x, 4, w, 124, BONE_H, "#E3DED4", r=12, sw=0.8)
        ic(d, x + 26, 106); txt(d, x + 48, 101, t, 13, "Serif-Bold", MOSS_H)
        # wrap body text manually
        words = body.split(); lines = []; cur = ""
        for wd in words:
            if pdfmetrics.stringWidth(cur + " " + wd, "Sans", 8.6) > w - 28: lines.append(cur); cur = wd
            else: cur = (cur + " " + wd).strip()
        lines.append(cur)
        for j, l in enumerate(lines[:7]): txt(d, x + 14, 82 - j * 11.5, l, 8.4)
    return D(d)

def ill_journey():
    d = Drawing(CW, 80); steps = [("1", "Learn", "library, videos"), ("2", "Check eligibility", "3-minute screen"), ("3", "Clinician decides", "independent, licensed"), ("4", "Pharmacy ships", "licensed, tracked"), ("5", "Ongoing care", "check-ins, refills")]
    n = len(steps); gap = (CW - 60) / (n - 1)
    for i, (num, t, s) in enumerate(steps):
        x = 30 + i * gap
        if i < n - 1: arrow(d, x + 18, 50, x + gap - 18, 50, "#A9B4AD", 1.2)
        d.add(Circle(x, 50, 14, fillColor=colors.HexColor(MOSS_H if i != 2 else BRASS_H), strokeColor=None)); txt(d, x, 46, num, 11, "Sans-Bold", "#FFFFFF", "middle")
        txt(d, x, 24, t, 9, "Sans-Bold", INK_H, "middle"); txt(d, x, 12, s, 7.8, "Sans", MUTED_H, "middle")
    return D(d)

def ill_map():
    W, H = CW, 250; d = Drawing(W, H); x0, y0, x1, y1 = 70, 34, W - 20, H - 24
    rrect(d, x0, y0, x1 - x0, y1 - y0, "#FBFAF7", "#E3DED4", r=10)
    d.add(Line(x0, (y0 + y1) / 2, x1, (y0 + y1) / 2, strokeColor=colors.HexColor("#E3DED4"), strokeWidth=1)); d.add(Line((x0 + x1) / 2, y0, (x0 + x1) / 2, y1, strokeColor=colors.HexColor("#E3DED4"), strokeWidth=1))
    txt(d, (x0 + x1) / 2, y0 - 16, "Hype-led  ◄──────────────────►  Evidence-led", 8.5, "Sans", MUTED_H, "middle")
    d.add(String(0, 0, "", fontName="Sans"))
    for i, l in enumerate(["Premium", "▲", "", "", "", "", "", "▼", "Budget"]): txt(d, 30, y1 - 14 - i * ((y1 - y0 - 24) / 8), l, 8.5, "Sans", MUTED_H, "middle")
    bubbles = [("'Research-use-only' vendors\n(under enforcement)", 0.13, 0.32, 26, ROSE_H, "#9E3B2E"), ("Budget hormone clinics", 0.38, 0.22, 22, "#EFEDE8", MUTED_H), ("Big telehealth generalists\n(Hims, Ro)", 0.5, 0.5, 28, "#EFEDE8", MUTED_H), ("Diagnostics platforms\n(Function, Superpower)", 0.8, 0.62, 28, "#EFEDE8", MUTED_H), ("Luxury longevity clinics\n($10K–$85K/yr)", 0.42, 0.86, 20, "#EFEDE8", MUTED_H), ("AminoLord", 0.87, 0.86, 34, MOSS_H, MOSS_H)]
    for lab, fx, fy, r, fill, stroke in bubbles:
        cx = x0 + fx * (x1 - x0); cy = y0 + fy * (y1 - y0)
        d.add(Circle(cx, cy, r, fillColor=colors.HexColor(fill), strokeColor=colors.HexColor(stroke), strokeWidth=1))
        lines = lab.split("\n")
        if fill == MOSS_H: txt(d, cx, cy - 4, lab, 10, "Serif-Bold", "#FFFFFF", "middle")
        else:
            for j, l in enumerate(lines): txt(d, cx, cy - r - 10 - j * 10, l, 7.8, "Sans", INK_H, "middle")
    return D(d)

def ill_phases():
    d = Drawing(CW, 136); phases = [("Foundation & compliance", 0, 3, MUTED_H), ("Internal pilot", 3, 4.5, MUTED_H), ("Private beta (4–6 states)", 4.5, 6.5, MOSS_H), ("Waitlist & early access", 5, 7.5, MOSS_H), ("Public launch", 7.5, 8.5, BRASS_H), ("Expand state by state", 8.5, 18, MOSS_H)]
    x0 = 150; scale = (CW - x0 - 10) / 18; top = 120
    for m in range(0, 19, 3):
        x = x0 + m * scale; d.add(Line(x, 22, x, top + 6, strokeColor=colors.HexColor("#ECE9E2"), strokeWidth=0.8)); txt(d, x, 8, f"M{m}", 7.5, "Sans", MUTED_H, "middle")
    for i, (n, a, b, c) in enumerate(phases):
        y = top - i * 18
        txt(d, x0 - 8, y - 4, n, 8.4, "Sans", INK_H, "end")
        rrect(d, x0 + a * scale, y - 7, (b - a) * scale, 13, c, None, r=6)
    return D(d)

def stats(items):
    cells = [[Paragraph(esc(v), B["big"]) for v, _ in items], [Paragraph(esc(l), B["biglabel"]) for _, l in items]]
    tb = Table(cells, colWidths=[CW / len(items)] * len(items), hAlign="LEFT")
    tb.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 1, BRASS), ("TOPPADDING", (0, 0), (-1, 0), 10), ("BOTTOMPADDING", (0, 1), (-1, 1), 8), ("LEFTPADDING", (0, 0), (-1, -1), 2)]))
    return tb

def cards(items, fills=None, icon=None):
    """items: list of (title, body); two columns"""
    n = len(items); rows = []
    for i in range(0, n, 2):
        row = []
        for j in range(2):
            if i + j < n:
                t, b = items[i + j]
                dr = Drawing(28, 26); (icon[i + j] if icon else icon_check)(dr, 14, 12)
                inner = Table([[D(dr), Paragraph(md(t), B["card_t"])], ["", Paragraph(md(b), B["card_b"])]], colWidths=[32, CW / 2 - 60])
                inner.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("SPAN", (0, 0), (0, 1)), ("LEFTPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, 0), 1), ("TOPPADDING", (0, 1), (-1, 1), 0)]))
                row.append(inner)
            else: row.append("")
        rows.append(row)
    tb = Table(rows, colWidths=[CW / 2] * 2, hAlign="LEFT")
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]
    for r in range(len(rows)):
        for c in range(2):
            f = (fills[r * 2 + c] if fills and r * 2 + c < len(fills) else BONE_H)
            st.append(("BACKGROUND", (c, r), (c, r), colors.HexColor(f)))
    st += [("LINEBELOW", (0, 0), (-1, -1), 3, colors.white), ("LINEAFTER", (0, 0), (0, -1), 3, colors.white)]
    tb.setStyle(TableStyle(st)); return tb

class Brief(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(path, pagesize=letter, leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.85 * inch, bottomMargin=0.8 * inch, title="AminoLord — Brief for Scott Disick (proposed)", author="AminoLord project")
        fr = Frame(0.9 * inch, 0.8 * inch, CW, PAGE_H - 1.65 * inch, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cv = Frame(0, 0, PAGE_W, PAGE_H, id="c", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[cv], onPage=self._cover), PageTemplate(id="main", frames=[fr], onPageEnd=self._main)])
    def _cover(self, c, doc):
        c.saveState(); c.setFillColor(MOSS); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        # abstract illustration: concentric rings + brass dot
        c.setStrokeColor(colors.HexColor("#2E5446")); c.setLineWidth(1.2)
        for r in (60, 95, 130, 165): c.circle(PAGE_W - 1.6 * inch, PAGE_H - 2.0 * inch, r, stroke=1, fill=0)
        c.setFillColor(BRASS); c.circle(PAGE_W - 1.6 * inch, PAGE_H - 2.0 * inch, 9, stroke=0, fill=1)
        c.setFillColor(BRASS); c.rect(0.9 * inch, PAGE_H * 0.33, 64, 3, fill=1, stroke=0); c.restoreState()
    def _main(self, c, doc):
        c.saveState(); c.setFont("Sans", 7.5); c.setFillColor(MUTED)
        c.drawString(0.9 * inch, 0.5 * inch, "AminoLord · proposed concept · brief for review · not an offer, not medical or legal advice · 2026-09-02")
        c.drawRightString(PAGE_W - 0.9 * inch, 0.5 * inch, f"{doc.page} / 6"); c.restoreState()

story = []
LMx = 0.9 * inch
story += [Spacer(1, 2.6 * inch),
 Table([[Paragraph("AminoLord", B["cover_t"])]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LMx)]),
 Table([[Paragraph("Peptide health, done properly.", B["cover_s"])]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LMx)]),
 Spacer(1, 1.35 * inch),
 Table([[Paragraph("A short brief for Scott Disick<br/>on a proposed brand partnership<br/><br/>Six pages. What the opportunity is, what the company would be, what your role could look like, and what we'd need to decide together.<br/><br/>This is a proposal for your review only. Nothing here is agreed, and nothing implies your involvement or endorsement. The full 43-page plan, research files and financial model sit behind it.", B["cover_m"])]], colWidths=[CW], style=[("LEFTPADDING", (0, 0), (-1, -1), LMx)]),
 NextPageTemplate("main"), PageBreak()]

# Page 2 — The moment
story += [p("THE MOMENT", "kick"), Paragraph("Peptides went mainstream. Trust didn't.", B["h1"]),
 p("Between 2023 and 2026 peptides moved from gym-bro forums to dinner-party conversation, pulled along by GLP-1s, podcasts and a wave of press about the 'peptide boom'. But the way people actually buy them is a mess: sketchy 'research-use-only' websites, budget hormone clinics, and a few giant telehealth brands adding peptides late. Regulators have spent the last eighteen months clearing out the bottom of the market. Nobody has built the trustworthy front door.", "lead"),
 ill_timeline(),
 Spacer(1, 6),
 stats([("109", "companies we mapped"), ("75", "audited in detail"), ("23", "of 36 legal issues rated high-risk"), ("0", "brands doing all of: named doctors, honest evidence, all-in pricing")]),
 Paragraph("Why this matters for a brand", B["h2"]),
 *bul(["**The demand is real and growing.** Search interest in peptides, BPC-157 and sermorelin has climbed for three years; roughly one in eight US adults says they've used a GLP-1 drug.",
       "**The rules just moved in our favor.** In 2026 the federal government reversed course and began reopening prescription compounding for several popular peptides. It is not final yet, which is exactly why a compliance-first brand wins: it can move the moment the rule lands.",
       "**The competition is either cheap or clinical.** Budget clinics feel like steroid shops; diagnostics platforms feel like a lab report. Neither feels premium, calm, or honest about what's proven and what isn't."]),
 p("Sources and labels for every figure are in the full plan and evidence ledger. Some market figures could not be independently verified during the research window and are flagged there.", "small"),
 PageBreak()]

# Page 3 — What AminoLord is
story += [p("THE IDEA", "kick"), Paragraph("A premium, doctor-led home for peptide health.", B["h1"]),
 p("Three connected parts: a library people trust, care from independent clinicians, and a small store for things that don't need a prescription. The brand's promise is transparency: we show what's approved, what's compounded, what's still unproven, and what we refuse to sell.", "lead"),
 ill_layers(), Spacer(1, 8),
 Paragraph("How it works for a member", B["h2"]), ill_journey(), Spacer(1, 4),
 Paragraph("What we will never do", B["h2"]),
 cards([("Sell 'research-use-only' peptides", "The FDA now treats those websites as unapproved-drug sellers. Several owners have been prosecuted in 2025–26."), ("Promise results", "No before-and-after photos, no miracle claims, no 'same as Ozempic'. Honest evidence grades instead."), ("Hide fees or trap people in subscriptions", "All-in pricing before anyone starts, and cancellation in two clicks. This is also what the FTC is suing over right now."), ("Let marketing touch medical decisions", "Clinicians are independent and never paid by the prescription. That protects members, and it protects you.")], fills=[ROSE_H] * 4, icon=[icon_x] * 4),
 PageBreak()]

# Page 4 — Market and celebrity lessons
story += [p("THE LANDSCAPE", "kick"), Paragraph("Where AminoLord sits, and what celebrity brands teach us.", B["h1"]),
 ill_map(),
 p("Analyst view based on the 75-company audit. Bubble size is rough scale; position is positioning, not revenue.", "small"),
 Paragraph("Celebrity-founded health brands: what actually worked", B["h2"]),
 cards([("Owner + real product = it works", "Hailey Bieber's Rhode launched with a peptide lip treatment as its hero and sold for $1B in 2025. Podcast hosts who owned equity in AG1 and Onnit built decade-long businesses."), ("A rented face doesn't convert", "Ladder (LeBron James and friends) reached ~$4M in sales with 180M+ combined followers. SKKN by Kim folded in 2025 despite the largest audience in our database."), ("Health trust breaks hard", "Goop paid $145K over unproven claims; Kim Kardashian paid $1.26M for an undisclosed promotion; Lemme's 'GLP-1 Daily' drew class actions within five months of launch."), ("The face can't be the whole brand", "TB12 lost its founder and had to rebrand. WeightWatchers' stock dropped ~25% in a day when Oprah left. Doctors and standards have to carry equal weight.")], icon=[icon_check, icon_x, icon_x, icon_person]),
 p("59 celebrity relationships were classified from company filings and press. Details and sources are in the full database.", "small"),
 PageBreak()]

# Page 5 — Your proposed role
story += [p("YOUR PROPOSED ROLE", "kick"), Paragraph("Creative direction and reach, with the medicine kept separate.", B["h1"]),
 p("This is a sketch for discussion, not an offer. The structure is designed so your name adds awareness and taste while independent doctors and published standards carry the trust.", "lead"),
 cards([("What you'd shape", "Brand vision and creative direction. Founder-led content and the launch moment. Partnerships and introductions. A seat in customer insight sessions."), ("What stays out of your lane", "Which peptides are offered, who qualifies, and what the site claims medically. That belongs to the medical director and compliance, by design and by law."), ("How it could be structured", "Cash retainer, equity that vests with deliverables, a capped royalty, or a mix. We modeled all of them. No terms have been proposed or discussed."), ("Time and obligations", "A defined number of content days per quarter, launch-week availability, and approved scripts for anything that touches health. Everything disclosed as a paid or ownership relationship, every time.")], icon=[icon_person, icon_shield, icon_pill, icon_check]),
 Paragraph("The honest part", B["h2"]),
 *bul(["**Disclosure has to be perfect.** The FTC's 2023 rules treat ownership and payment as things every post must disclose. Your name appears on the FTC's 2017 influencer warning-letter list; that history means reporters and regulators will look closely, so the program has to be spotless from day one.",
       "**Your GLP-1 history is a question, not a problem.** You've been open about Mounjaro. A peptide brand can work with that honesty. What we need to check first is whether any past GLP-1 promotion carries exclusivity that conflicts with this category.",
       "**Both sides get protection.** Mutual morality clauses, clear termination terms, and rules about how the brand can use your name after any exit."]),
 Paragraph("The medical cofounder", B["h2"]),
 p("A physician medical director would own the formulary, the protocols and every health claim, employed by the clinical entity rather than the brand, with pay that never depends on prescriptions. The doctor proposed for this role has not yet been verified; identity, licenses and board status must be confirmed before anyone is named publicly."),
 PageBreak()]

# Page 6 — Plan and ask
story += [p("THE PLAN", "kick"), Paragraph("Build quietly, prove it works, then switch on the reach.", B["h1"]),
 p("No single big-bang launch. We build the library, sign the clinical and pharmacy partners, run a private beta in a handful of states, grow a waitlist, and only then go public. Your audience is used only after contracts are signed, and it lands on a product that already works.", "lead"),
 ill_phases(), Spacer(1, 6),
 stats([("~9 mo", "to public launch"), (CAP, "capital needed, base case (assumption)"), (f"Month {BE}", "break-even, base case (assumption)"), (Y3, "year-3 revenue, base case (assumption)")]),
 p("These are modeling assumptions, not forecasts. The conservative case needs about $12.9M and does not break even within three years; the full model shows every input.", "small"),
 Paragraph("What we'd want to decide with you", B["h2"]),
 *bul(["Whether you want to explore this at all, and in what shape: brand partner, cofounder, or advisor.", "Who represents you, and whether any existing deal limits a health or GLP-1 category partnership.", "How much of the brand should be built around you versus around the doctors and standards. Our recommendation: the medicine leads, you amplify.", "Comfort with the disclosure and morality terms that a health brand requires."]),
 Paragraph("What happens next if you're interested", B["h2"]),
 *bul(["A conversation with your representatives about scope and category exclusivity.", "In parallel: verify the medical cofounder, engage healthcare counsel, clear the trademark, and build a working prototype of the library and eligibility flow so you can see and shape it before deciding."]),
 p("Prepared 2026-09-02 from a 43-page plan, a 36-month financial model and an evidence ledger of 790 sources. Some research could not be directly verified under network limits; those gaps are listed in the full plan.", "small")]

doc = Brief("outputs/AminoLord_Brief_for_Scott_Disick.pdf"); doc.build(story); print("brief built")
