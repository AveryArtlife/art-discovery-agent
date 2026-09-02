"""Reserve Clinic logo: serif 'R' inside a thin brass ring + tracked serif wordmark. Vector (reportlab canvas) plus SVG/PNG exports."""
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
LIB = "/usr/share/fonts/truetype/liberation/"
for n, f in (("LSerif", "LiberationSerif-Regular.ttf"), ("LSerif-Bold", "LiberationSerif-Bold.ttf")):
    if n not in pdfmetrics.getRegisteredFontNames(): pdfmetrics.registerFont(TTFont(n, LIB + f))
MOSS = "#1F3D33"; BRASS = "#B08D57"; BONE = "#F6F3EE"

def draw_mark(c, cx, cy, r, on_dark=False):
    c.saveState(); c.setStrokeColor(colors.HexColor(BRASS)); c.setLineWidth(max(0.6, r * 0.07)); c.circle(cx, cy, r, stroke=1, fill=0)
    c.setFillColor(colors.HexColor(BONE if on_dark else MOSS)); size = r * 1.32; c.setFont("LSerif", size)
    w = pdfmetrics.stringWidth("R", "LSerif", size); c.drawString(cx - w / 2 + r * 0.02, cy - size * 0.35, "R"); c.restoreState()

def draw_wordmark(c, x, y, h, on_dark=False, align="left"):
    """x,y = left/baseline of RESERVE; h = cap height budget. Returns width."""
    s1 = h * 0.78; s2 = h * 0.34; t1 = s1 * 0.22; t2 = s2 * 0.42
    w1 = pdfmetrics.stringWidth("RESERVE", "LSerif", s1) + t1 * 6; w2 = pdfmetrics.stringWidth("CLINIC", "LSerif", s2) + t2 * 5
    if align == "center": x1 = x - w1 / 2; x2 = x - w2 / 2
    else: x1 = x; x2 = x + (w1 - w2) / 2
    c.saveState(); t = c.beginText(x1, y); t.setFont("LSerif", s1); t.setCharSpace(t1); t.setFillColor(colors.HexColor(BONE if on_dark else MOSS)); t.textOut("RESERVE"); c.drawText(t)
    t = c.beginText(x2, y - s2 * 1.45); t.setFont("LSerif", s2); t.setCharSpace(t2); t.setFillColor(colors.HexColor(BRASS)); t.textOut("CLINIC"); c.drawText(t); c.restoreState()
    return w1

def draw_logo(c, x, y, h, on_dark=False):
    """horizontal lockup; x,y = bottom-left; h = total height. Returns width."""
    r = h * 0.42; draw_mark(c, x + r + h * 0.04, y + h * 0.5, r, on_dark)
    w = draw_wordmark(c, x + 2 * r + h * 0.34, y + h * 0.47, h * 0.72, on_dark)
    return 2 * r + h * 0.34 + w

def draw_logo_stacked(c, cx, y, h, on_dark=False):
    r = h * 0.28; draw_mark(c, cx, y + h - r - h * 0.02, r, on_dark)
    draw_wordmark(c, cx, y + h * 0.22, h * 0.36, on_dark, align="center")

def svg(variant="horizontal", on_dark=False):
    ink = BONE if on_dark else MOSS; bg = MOSS if on_dark else "none"
    ff = "'Cormorant Garamond','Liberation Serif','Times New Roman',serif"
    if variant == "mark":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120"><rect width="120" height="120" fill="{bg}"/><circle cx="60" cy="60" r="50" fill="none" stroke="{BRASS}" stroke-width="3.5"/><text x="61" y="84" text-anchor="middle" font-family="{ff}" font-size="66" fill="{ink}">R</text></svg>'''
    if variant == "stacked":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 220" width="320" height="220"><rect width="320" height="220" fill="{bg}"/><circle cx="160" cy="62" r="46" fill="none" stroke="{BRASS}" stroke-width="3.2"/><text x="161" y="84" text-anchor="middle" font-family="{ff}" font-size="60" fill="{ink}">R</text><text x="160" y="164" text-anchor="middle" font-family="{ff}" font-size="40" letter-spacing="9" fill="{ink}">RESERVE</text><text x="160" y="196" text-anchor="middle" font-family="{ff}" font-size="16" letter-spacing="7" fill="{BRASS}">CLINIC</text></svg>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="520" height="120"><rect width="520" height="120" fill="{bg}"/><circle cx="60" cy="60" r="46" fill="none" stroke="{BRASS}" stroke-width="3.2"/><text x="61" y="82" text-anchor="middle" font-family="{ff}" font-size="60" fill="{ink}">R</text><text x="130" y="70" font-family="{ff}" font-size="48" letter-spacing="10" fill="{ink}">RESERVE</text><text x="134" y="98" font-family="{ff}" font-size="18" letter-spacing="8" fill="{BRASS}">CLINIC</text></svg>'''

if __name__ == "__main__":
    import os
    from reportlab.pdfgen import canvas
    import pypdfium2 as pdfium
    os.makedirs("outputs/brand", exist_ok=True)
    specs = [("horizontal-light", (520, 120), False, "horizontal"), ("horizontal-dark", (520, 120), True, "horizontal"), ("stacked-light", (320, 220), False, "stacked"), ("stacked-dark", (320, 220), True, "stacked"), ("mark-light", (120, 120), False, "mark")]
    for name, (w, h), dark, var in specs:
        open(f"outputs/brand/reserve-clinic-logo-{name}.svg", "w").write(svg(var, dark))
        pdfp = f"outputs/brand/reserve-clinic-logo-{name}.pdf"; c = canvas.Canvas(pdfp, pagesize=(w, h))
        if dark: c.setFillColor(colors.HexColor(MOSS)); c.rect(0, 0, w, h, fill=1, stroke=0)
        if var == "horizontal": draw_logo(c, 14, 10, 100, dark)
        elif var == "stacked": draw_logo_stacked(c, w / 2, 14, 190, dark)
        else: draw_mark(c, 60, 60, 50, dark)
        c.save(); pg = pdfium.PdfDocument(pdfp)[0]; pg.render(scale=4).to_pil().save(f"outputs/brand/reserve-clinic-logo-{name}.png")
    print("brand assets written")
