"""Helpers and charts for the AminoLord business plan PDF."""
import json, os, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether,
                                BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, CondPageBreak, Flowable)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Sans", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif", FD + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", FD + "DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mono", FD + "DejaVuSansMono.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")
registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif", boldItalic="Serif-Bold")

INK = colors.HexColor("#14171C"); MOSS = colors.HexColor("#1F3D33"); BRASS = colors.HexColor("#B08D57")
BONE = colors.HexColor("#F6F3EE"); MUTED = colors.HexColor("#5B6069"); LINE = colors.HexColor("#D9D4CB"); PALE = colors.HexColor("#EEF2EF")
# validated categorical palette (dataviz skill reference instance)
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300"]
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
GRID = "#e1e0d9"; AXIS = "#c3c2b7"; INK_MUTED = "#898781"

PAGE_W, PAGE_H = letter
LM = RM = 0.85 * inch; TM = 0.9 * inch; BM = 0.85 * inch
CW = PAGE_W - LM - RM

S = {}
S["body"] = ParagraphStyle("body", fontName="Sans", fontSize=9.6, leading=13.6, textColor=INK, spaceAfter=6, alignment=TA_LEFT)
S["small"] = ParagraphStyle("small", parent=S["body"], fontSize=8.2, leading=11, textColor=MUTED, spaceAfter=4)
S["src"] = ParagraphStyle("src", parent=S["body"], fontSize=7.6, leading=10, textColor=MUTED, spaceBefore=2, spaceAfter=8)
S["h1"] = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=20, leading=24, textColor=MOSS, spaceBefore=18, spaceAfter=10, keepWithNext=1)
S["h2"] = ParagraphStyle("h2", fontName="Serif-Bold", fontSize=13, leading=16, textColor=INK, spaceBefore=12, spaceAfter=5, keepWithNext=1)
S["h3"] = ParagraphStyle("h3", fontName="Sans-Bold", fontSize=10, leading=13, textColor=MOSS, spaceBefore=8, spaceAfter=3, keepWithNext=1)
S["kicker"] = ParagraphStyle("kicker", fontName="Sans-Bold", fontSize=8, leading=10, textColor=BRASS, spaceAfter=2)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=12, bulletIndent=2, spaceAfter=3)
S["cell"] = ParagraphStyle("cell", fontName="Sans", fontSize=7.8, leading=10, textColor=INK)
S["cellb"] = ParagraphStyle("cellb", fontName="Sans-Bold", fontSize=7.8, leading=10, textColor=colors.white)
S["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=6.6, leading=8.2, textColor=INK)
S["callout"] = ParagraphStyle("callout", parent=S["body"], fontName="Sans", fontSize=9.4, leading=13, textColor=INK, backColor=PALE, borderPadding=(8, 10, 8, 10), spaceBefore=16, spaceAfter=14)
S["toc0"] = ParagraphStyle("toc0", fontName="Sans", fontSize=9.6, leading=14, textColor=INK)
S["toc1"] = ParagraphStyle("toc1", fontName="Sans", fontSize=8.4, leading=12, leftIndent=14, textColor=MUTED)
S["cover_t"] = ParagraphStyle("cover_t", fontName="Serif-Bold", fontSize=34, leading=40, textColor=colors.white)
S["cover_s"] = ParagraphStyle("cover_s", fontName="Sans", fontSize=13, leading=18, textColor=colors.HexColor("#DCE5DF"))
S["cover_m"] = ParagraphStyle("cover_m", fontName="Sans", fontSize=9, leading=13, textColor=colors.HexColor("#C9D3CC"))
S["big"] = ParagraphStyle("big", fontName="Serif-Bold", fontSize=18, leading=21, textColor=MOSS)
S["biglabel"] = ParagraphStyle("biglabel", fontName="Sans", fontSize=7.8, leading=10, textColor=MUTED)

def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def md(t):
    """minimal inline markup: **bold** → <b>"""
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t

def P(t, style="body"): return Paragraph(md(t), S[style])
def SRC(t): return Paragraph("<b>Source / label:</b> " + md(t), S["src"])
def CALLOUT(t): return Paragraph(md(t), S["callout"])
def BUL(items, style="bullet"):
    return [Paragraph(md(i), S[style], bulletText="•") for i in items]
def KICK(t): return Paragraph(md(t), S["kicker"])

class Anchor(Flowable):
    def __init__(self, key): super().__init__(); self.key = key; self.width = 0; self.height = 0
    def draw(self): self.canv.bookmarkPage(self.key)

def H1(t, num=None):
    txt = (f"{num}  " if num else "") + t
    p = Paragraph(md(txt), S["h1"]); p._toc = (0, txt)
    return p
def H2(t):
    p = Paragraph(md(t), S["h2"]); p._toc = (1, t)
    return p
def H3(t): return Paragraph(md(t), S["h3"])

def T(data, widths=None, header=True, font=7.8, zebra=True, align_right_cols=()):
    rows = []
    for i, row in enumerate(data):
        cells = []
        for j, v in enumerate(row):
            st = S["cellb"] if (header and i == 0) else S["cell"]
            if isinstance(v, str):
                cells.append(Paragraph(md(v), ParagraphStyle("c", parent=st, fontSize=font, leading=font + 2.4, alignment=(2 if j in align_right_cols and i > 0 else 0))))
            else: cells.append(v)
        rows.append(cells)
    if widths is None:
        n = len(data[0]); widths = [CW / n] * n
    tb = Table(rows, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.3, LINE),
             ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    if header: style += [("BACKGROUND", (0, 0), (-1, 0), MOSS), ("LINEBELOW", (0, 0), (-1, 0), 0.6, MOSS)]
    if zebra:
        for i in range(1 if header else 0, len(rows)):
            if i % 2 == 0: style.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F7F5F1")))
    tb.setStyle(TableStyle(style))
    return tb

def IMG(path, width=CW, maxh=None):
    from reportlab.lib.utils import ImageReader
    ir = ImageReader(path); iw, ih = ir.getSize(); h = width * ih / iw
    if maxh and h > maxh: width = width * maxh / h; h = maxh
    return Image(path, width=width, height=h)

def MONO(text):
    lines = [esc(l) for l in text.rstrip("\n").split("\n")]
    p = Paragraph("<br/>".join(l.replace(" ", "&nbsp;") for l in lines), S["mono"])
    tb = Table([[p]], colWidths=[CW]); tb.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FBFAF7")), ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return tb

def STATS(items):
    """items: list of (value, label)"""
    cells = [[Paragraph(esc(v), S["big"]) for v, _ in items], [Paragraph(esc(l), S["biglabel"]) for _, l in items]]
    tb = Table(cells, colWidths=[CW / len(items)] * len(items), hAlign="LEFT")
    tb.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.8, BRASS), ("TOPPADDING", (0, 0), (-1, 0), 8), ("BOTTOMPADDING", (0, 1), (-1, 1), 8), ("LEFTPADDING", (0, 0), (-1, -1), 2)]))
    return tb

def money(v, dec=1):
    if v is None or v == "": return "n/a"
    if isinstance(v, str): return v
    a = abs(v)
    if a >= 1e6: s = f"${a/1e6:.{dec}f}M"
    elif a >= 1e3: s = f"${a/1e3:.0f}k"
    else: s = f"${a:.0f}"
    return f"({s})" if v < 0 else s
def num(v): return "n/a" if v in (None, "") else (v if isinstance(v, str) else f"{v:,.0f}")

# ------------------------------------------------------------------ charts
def _style(ax, title=None):
    ax.set_facecolor("#fcfcfb")
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"): ax.spines[sp].set_color(AXIS)
    ax.tick_params(colors=INK_MUTED, labelsize=8)
    ax.yaxis.grid(True, color=GRID, linewidth=0.6); ax.set_axisbelow(True)
    if title: ax.set_title(title, loc="left", fontsize=10, color="#0b0b0b", pad=10)

def chart_scenarios(mv, path):
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.4), dpi=200)
    for ax, key, ttl, fmt in ((axes[0], "Net revenue", "Monthly net revenue by scenario ($k)", 1e3), (axes[1], "Cumulative cash flow", "Cumulative cash flow by scenario ($M)", 1e6)):
        _style(ax, ttl)
        for i, sc in enumerate(("Conservative", "Base", "Upside")):
            y = [v / fmt for v in mv["monthly"][sc][key]]
            ax.plot(range(1, 37), y, color=CAT[i], linewidth=2, label=sc)
            ax.annotate(sc, (36, y[-1]), xytext=(3, 0), textcoords="offset points", fontsize=7.5, color="#52514e", va="center")
        ax.set_xlabel("Model month", fontsize=8, color=INK_MUTED); ax.set_xlim(1, 41)
        if key == "Cumulative cash flow": ax.axhline(0, color=AXIS, linewidth=0.8)
    axes[0].legend(frameon=False, fontsize=7.5, loc="upper left")
    fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_funnel(mv, path):
    m = mv["monthly"]["Base"]; col = 23  # month 24
    steps = [("Sessions", "Total sessions"), ("Quiz starts", "Eligibility quiz starts"), ("Quiz completes", "Quiz completions"), ("Eligible", "Eligible outcomes (screen + state)"), ("Intakes", "Intakes submitted (consult fee charged)"), ("Consults", "Consults completed"), ("Prescribed", "Prescriptions issued (clinician decision)"), ("Paying Rx members", "New paying Rx program members")]
    vals = [m[k][col] for _, k in steps]
    fig, ax = plt.subplots(figsize=(9.2, 3.3), dpi=200); _style(ax, "Base scenario monthly funnel, month 24 (log scale)")
    ax.bar([s for s, _ in steps], vals, color=[CAT[0]] * 7 + [CAT[2]], width=0.62)
    ax.set_yscale("log"); ax.yaxis.grid(True, which="both", color=GRID, linewidth=0.5)
    for i, v in enumerate(vals): ax.annotate(f"{v:,.0f}", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=7.5, color="#52514e")
    ax.tick_params(axis="x", labelsize=7.5); fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_market(path):
    layers = [("Peptide therapeutics (global, pharma-dominated)", 47.5, "context only"), ("US wellness market (McKinsey)", 480, "context only"), ("Branded GLP-1 obesity drugs, US", 22.5, "demand engine"), ("Cash-pay DTC telehealth, US", 5.0, "core SAM"), ("Cash-pay hormone / peptide optimization, US", 4.0, "core SAM"), ("US 503A/503B compounding (supply)", 6.0, "supply"), ("DTC lab testing / longevity diagnostics (global)", 3.0, "on-ramp"), ("Wellness-peptide niche, US (bottom-up order of magnitude)", 2.0, "direct")]
    fig, ax = plt.subplots(figsize=(9.2, 3.8), dpi=200); _style(ax, "Market layers used for sizing ($B, midpoints of recalled ranges; unverified)")
    names = [n for n, _, _ in layers][::-1]; v = [x for _, x, _ in layers][::-1]; tags = [t for _, _, t in layers][::-1]
    cmap = {"context only": "#c3c2b7", "demand engine": CAT[1], "core SAM": CAT[0], "supply": CAT[3], "on-ramp": CAT[2], "direct": CAT[4]}
    ax.barh(names, v, color=[cmap[t] for t in tags], height=0.6); ax.set_xscale("log"); ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.yaxis.grid(False)
    for i, (x, t) in enumerate(zip(v, tags)): ax.annotate(f"${x:g}B · {t}", (x, i), xytext=(4, 0), textcoords="offset points", va="center", fontsize=7.5, color="#52514e")
    ax.set_xlim(1, 2000); ax.tick_params(axis="y", labelsize=7.5); fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_bars(labels, values, title, path, color=CAT[0], fmt="{:,.0f}", figsize=(9.2, 3.0), horizontal=False):
    fig, ax = plt.subplots(figsize=figsize, dpi=200); _style(ax, title)
    if horizontal:
        ax.barh(labels[::-1], values[::-1], color=color, height=0.6); ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.yaxis.grid(False)
        for i, v in enumerate(values[::-1]): ax.annotate(fmt.format(v), (v, i), xytext=(4, 0), textcoords="offset points", va="center", fontsize=7.5, color="#52514e")
    else:
        ax.bar(labels, values, color=color, width=0.6)
        for i, v in enumerate(values): ax.annotate(fmt.format(v), (i, v), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=7.5, color="#52514e")
    ax.tick_params(labelsize=7.5); fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_ltv(mv, path):
    cm = mv["monthly"]["Base"]["Contribution per Rx member-month before acquisition"][0]
    churns = [0.06, 0.08, 0.10, 0.11, 0.12, 0.14, 0.16]
    fig, ax = plt.subplots(figsize=(9.2, 3.0), dpi=200); _style(ax, f"LTV:CAC sensitivity — Base contribution ${cm:.0f} per Rx member-month")
    for i, cac in enumerate((200, 300, 400, 500)):
        y = [(cm / c) / cac for c in churns]; ax.plot([c * 100 for c in churns], y, color=CAT[i], linewidth=2, marker="o", markersize=4, label=f"CAC ${cac}")
        ax.annotate(f"CAC ${cac}", (16, y[-1]), xytext=(4, 0), textcoords="offset points", fontsize=7.5, color="#52514e", va="center")
    ax.axhline(3, color=AXIS, linewidth=0.8, linestyle="--"); ax.annotate("3.0x target", (6, 3.05), fontsize=7.5, color=INK_MUTED)
    ax.set_xlabel("Monthly churn (%)", fontsize=8, color=INK_MUTED); ax.set_ylabel("LTV : CAC", fontsize=8, color=INK_MUTED); ax.set_xlim(5.5, 18); ax.legend(frameon=False, fontsize=7.5)
    fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_gantt(path):
    phases = [("Phase 0 Foundation & compliance", 0, 3), ("Phase 1 Internal pilot", 3, 4.5), ("Phase 2 Private beta", 4.5, 6.5), ("Phase 3 Waitlist & early access", 5, 7.5), ("Phase 4 Public launch", 7.5, 8.5), ("Phase 5 Expansion", 8.5, 24)]
    fig, ax = plt.subplots(figsize=(9.2, 2.8), dpi=200); _style(ax, "Phased launch timeline (months from project start)")
    for i, (n, a, b) in enumerate(phases[::-1]):
        ax.barh(n, b - a, left=a, color=CAT[(len(phases) - 1 - i) % 4] if i != 0 else SEQ[4], height=0.55)
    ax.set_xlim(0, 24); ax.set_xticks(range(0, 25, 3)); ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.yaxis.grid(False); ax.tick_params(axis="y", labelsize=7.5)
    ax.axvline(8, color=AXIS, linewidth=0.8, linestyle="--"); ax.annotate("Public launch (Base: month 8)", (8.2, 5.3), fontsize=7.5, color=INK_MUTED)
    fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

def chart_pricebands(path):
    bands = [("Sermorelin (compounded)", 79, 400), ("NAD+ injections", 119, 395), ("Tesamorelin (approved; off-label)", 300, 700), ("CJC-1295 / ipamorelin", 200, 450), ("Compounded semaglutide (wind-down)", 149, 399), ("Branded GLP-1 DTC", 149, 449), ("TRT telehealth", 79, 350), ("Telehealth memberships", 39, 199), ("AminoLord all-in program (assumption)", 249, 299)]
    fig, ax = plt.subplots(figsize=(9.2, 3.4), dpi=200); _style(ax, "Observed monthly price bands, US, 2026 (third-party unless noted)")
    for i, (n, lo, hi) in enumerate(bands[::-1]):
        c = CAT[2] if "AminoLord" in n else CAT[0]
        ax.plot([lo, hi], [i, i], color=c, linewidth=6, solid_capstyle="round"); ax.annotate(f"${lo}–${hi}", (hi, i), xytext=(6, 0), textcoords="offset points", va="center", fontsize=7.5, color="#52514e")
    ax.set_yticks(range(len(bands))); ax.set_yticklabels([n for n, _, _ in bands[::-1]], fontsize=7.5); ax.xaxis.grid(True, color=GRID, linewidth=0.6); ax.yaxis.grid(False); ax.set_xlim(0, 800); ax.set_xlabel("$ per month", fontsize=8, color=INK_MUTED)
    fig.patch.set_facecolor("#fcfcfb"); fig.tight_layout(); fig.savefig(path); plt.close(fig)

# ------------------------------------------------------------------ document
class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=letter, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM, title="AminoLord Business Plan and Proposal", author="Prepared for the AminoLord project owner", **kw)
        self.section = ""
        frame = Frame(LM, BM, CW, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover = Frame(0, 0, PAGE_W, PAGE_H, id="c", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="cover", frames=[cover], onPage=self._cover), PageTemplate(id="main", frames=[frame], onPageEnd=self._main)])
    def _cover(self, canv, doc):
        canv.saveState(); canv.setFillColor(MOSS); canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        canv.setFillColor(BRASS); canv.rect(LM, PAGE_H * 0.36, 60, 3, fill=1, stroke=0); canv.restoreState()
    def _main(self, canv, doc):
        canv.saveState(); canv.setFont("Sans", 7.2); canv.setFillColor(MUTED)
        canv.drawString(LM, PAGE_H - 0.55 * inch, "AminoLord — Peptide Market Audit, E-Commerce Strategy and Business Proposal")
        canv.drawRightString(PAGE_W - RM, PAGE_H - 0.55 * inch, self.section[:80])
        canv.setStrokeColor(LINE); canv.setLineWidth(0.5); canv.line(LM, PAGE_H - 0.62 * inch, PAGE_W - RM, PAGE_H - 0.62 * inch)
        canv.line(LM, 0.62 * inch, PAGE_W - RM, 0.62 * inch)
        canv.drawString(LM, 0.42 * inch, "Proposed concept · Confidential working draft · Prepared 2026-09-02 · Not legal, medical, or investment advice")
        canv.drawRightString(PAGE_W - RM, 0.42 * inch, f"Page {doc.page}")
        canv.restoreState()
    def beforeDocument(self):
        self.section = ""
    def afterFlowable(self, fl):
        if hasattr(fl, "_toc"):
            lvl, txt = fl._toc
            key = "h%d" % id(fl); self.canv.bookmarkPage(key)
            self.notify("TOCEntry", (lvl, txt, self.page, key))
            if lvl == 0: self.section = re.sub(r"^\d+\s+", "", txt)
            self.canv.addOutlineEntry(re.sub(r"<[^>]+>", "", txt), key, level=lvl, closed=(lvl > 0))


# ------------------------------------------------------------------ wireframes (drawn)
from reportlab.graphics.shapes import Drawing, Rect, String, Line
def WIRE(panels, height=3.2 * inch):
    """panels: list of (title, panel_w_fraction, boxes); boxes: (x, y, w, h, lines, kind) in 0-100 units of the panel; y from top."""
    d = Drawing(CW, height + 14)
    x0 = 0; gap = 10
    total = sum(f for _, f, _ in panels)
    for title, frac, boxes in panels:
        pw = (CW - gap * (len(panels) - 1)) * frac / total
        d.add(String(x0, height + 4, title, fontName="Sans-Bold", fontSize=7, fillColor=MOSS))
        d.add(Rect(x0, 0, pw, height, strokeColor=INK, strokeWidth=0.8, fillColor=colors.white))
        for (bx, by, bw, bh, lines, kind) in boxes:
            X = x0 + pw * bx / 100; Wd = pw * bw / 100; Hh = height * bh / 100; Yb = height - height * (by + bh) / 100
            fill = {"cta": MOSS, "cta2": colors.white, "media": colors.HexColor("#E4E7E3"), "chip": PALE, "warn": colors.HexColor("#F8E9E7"), "box": colors.white, "band": colors.HexColor("#F3F0EA")}.get(kind, colors.white)
            d.add(Rect(X, Yb, Wd, Hh, strokeColor=(MOSS if kind in ("cta", "cta2") else LINE), strokeWidth=0.6, fillColor=fill))
            fs = 5.2 if Hh > 12 else 4.6
            for i, ln in enumerate(lines):
                ty = Yb + Hh - 7 - i * (fs + 1.6)
                if ty < Yb + 1: break
                d.add(String(X + 3, ty, ln, fontName=("Sans-Bold" if (kind in ("cta", "cta2") or i == 0) else "Sans"), fontSize=fs, fillColor=(colors.white if kind == "cta" else INK)))
        x0 += pw + gap
    return d
