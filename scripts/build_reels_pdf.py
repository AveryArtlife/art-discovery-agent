from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    PageBreak,
    KeepTogether,
)

OUTPUT = "art_market_reels_script.pdf"

TITLE = "IG REELS SCRIPT: The Art Market Just Woke Up"
SUBTITLE = (
    "Total runtime: ~55 seconds &nbsp;|&nbsp; Visual: fast cuts, auction footage, "
    "paddle raises, price tickers &nbsp;|&nbsp; Structure: MrBeast retention model"
)

SECTIONS = [
    {
        "time": "[0:00 &ndash; 0:03] &nbsp;HOOK",
        "label": "MrBeast Rule #1: Promise the payoff instantly.",
        "vo": (
            "<b>VOICEOVER (urgent, hushed):</b> &ldquo;In ten minutes, five "
            "billionaires fought over a single painting &mdash; and the art "
            "market just flipped a switch.&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;Someone just paid $181 MILLION for paint splatter.&rdquo;",
        "visual": "<b>VISUAL:</b> Pollock <i>Number 1A, 1948</i> zoom-in &rarr; gavel slam &rarr; price ticker spinning up.",
    },
    {
        "time": "[0:03 &ndash; 0:12] &nbsp;RESTATE THE STAKES",
        "label": "Hook the skeptic with the receipts.",
        "vo": (
            "<b>VOICEOVER:</b> &ldquo;Last night at Christie&rsquo;s, a Jackson "
            "Pollock drip painting sold for <b>$181.2 million</b>. Sixty bids. "
            "A ten-minute war. New world record.&rdquo;<br/><br/>"
            "<b>VOICEOVER:</b> &ldquo;Then a Brancusi bronze the size of a melon "
            "went for <b>$107 million</b>. Also a record.&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;$181,200,000&rdquo; stamps in. &ldquo;RECORD&rdquo; flashing.",
        "visual": "<b>VISUAL:</b> Cut between Pollock canvas and the Brancusi bronze head rotating on a pedestal.",
    },
    {
        "time": "[0:12 &ndash; 0:25] &nbsp;ESCALATION",
        "label": "MrBeast Rule: bigger number every beat.",
        "vo": (
            "<b>VOICEOVER:</b> &ldquo;Both came from one collection &mdash; S.I. "
            "Newhouse. Sixteen lots. <b>$630 million</b> in a single night.&rdquo;"
            "<br/><br/>"
            "<b>VOICEOVER:</b> &ldquo;But here&rsquo;s why it actually matters&hellip;&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> Stack-of-bills graphic counting up to $630M.",
        "visual": "<b>VISUAL:</b> Smash cut to black after the line. One beat of silence.",
    },
    {
        "time": "[0:25 &ndash; 0:42] &nbsp;THE BIGGER STORY",
        "label": "Pay off the hook with the macro thesis.",
        "vo": (
            "<b>VOICEOVER:</b> &ldquo;U.S. auction sales just jumped <b>23%</b> "
            "&mdash; the first growth year since 2022. Christie&rsquo;s is "
            "targeting one-and-a-half billion this May alone. Sotheby&rsquo;s set "
            "their estimate <b>70% higher</b> than last year.&rdquo;<br/><br/>"
            "<b>VOICEOVER:</b> &ldquo;Since 1995, contemporary art has returned "
            "<b>11.4% a year</b> &mdash; that&rsquo;s 43% more than the S&amp;P 500.&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> Bar chart climbing. Headlines: &ldquo;Market Rebounds.&rdquo; &ldquo;First Growth Since 2022.&rdquo;",
        "visual": "<b>VISUAL:</b> Split-screen art index vs. S&amp;P line chart.",
    },
    {
        "time": "[0:42 &ndash; 0:52] &nbsp;THE THESIS",
        "label": "Why the viewer should care.",
        "vo": (
            "<b>VOICEOVER (slower, serious):</b> &ldquo;Wealth managers are "
            "calling it the next trillion-dollar asset class. Younger collectors "
            "are putting up to <b>30%</b> of their portfolios into art. And the "
            "smart money? It&rsquo;s not waiting anymore.&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;$2.86 TRILLION by 2026&rdquo; &mdash; Pollock painting fades in behind.",
        "visual": "<b>VISUAL:</b> Slow push-in on the Pollock. Music swells.",
    },
    {
        "time": "[0:52 &ndash; 0:55] &nbsp;CLOSE",
        "label": "Loop / CTA. Never let energy drop.",
        "vo": (
            "<b>VOICEOVER:</b> &ldquo;The art market didn&rsquo;t crash. It was "
            "just loading. Follow for what they&rsquo;re buying next.&rdquo;"
        ),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;FOLLOW &rarr;&rdquo; pulse.",
        "visual": "<b>VISUAL:</b> Cut to gavel slam from the opening. Loop-ready ending.",
    },
]

PRODUCTION_NOTES = [
    "<b>Hook A/B variant:</b> &ldquo;A painting that looks like spilled coffee just sold for $181 million.&rdquo;",
    "<b>Caption:</b> &ldquo;The art market just had its loudest night since 2022. Pollock $181M. Brancusi $107M. One night. $630M. The shift is on.&rdquo;",
    "First 3 frames MUST contain price + artwork. IG retention dies after second 2.",
    "<b>Audio:</b> Tense cinematic build (Zimmer-lite). Drop music entirely on &ldquo;but here&rsquo;s why it matters&rdquo; for contrast.",
    "<b>Aspect:</b> 9:16, 1080&times;1920. Caption-burn all VO for sound-off viewing.",
]

SOURCES = [
    ("Pollock and Brancusi Join the $100M Club", "dnyuz.com &mdash; May 18, 2026"),
    ("$181.2M Pollock, $107.6M Brancusi Sell at Christie&rsquo;s", "Artnet News"),
    ("Christie&rsquo;s S.I. Newhouse Sale Totals $630.8M", "ARTnews"),
    ("U.S. Art Market Rebounds, +23% in Auction Sales", "Bank of America &mdash; March 2026"),
    ("NY Auctions Test Recovery with $2.6B on Offer", "Prism News"),
    ("Art as the Next Trillion-Dollar Frontier", "Maddox Gallery"),
    ("Christie&rsquo;s, Sotheby&rsquo;s Report Annual Sales Increases", "Artnet News"),
]


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawString(20 * mm, height - 12 * mm, "IG REELS  /  ART MARKET RECOVERY")
    canvas.drawRightString(width - 20 * mm, height - 12 * mm, "MrBeast Structure")
    canvas.setStrokeColor(colors.HexColor("#dddddd"))
    canvas.line(20 * mm, height - 15 * mm, width - 20 * mm, height - 15 * mm)
    canvas.setFont("Helvetica-Oblique", 8)
    canvas.setFillColor(colors.HexColor("#999999"))
    canvas.drawCentredString(width / 2.0, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=22 * mm,
        bottomMargin=18 * mm,
        title="IG Reels Script - Art Market Recovery",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "Title", parent=styles["Heading1"], fontSize=20, leading=24,
        textColor=colors.HexColor("#111111"), spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle", parent=styles["BodyText"], fontSize=10, leading=13,
        textColor=colors.HexColor("#666666"), spaceAfter=14,
    )
    time_style = ParagraphStyle(
        "Time", parent=styles["Heading2"], fontSize=13, leading=16,
        textColor=colors.HexColor("#B81818"), spaceAfter=2,
    )
    label_style = ParagraphStyle(
        "Label", parent=styles["BodyText"], fontSize=9, leading=12,
        textColor=colors.HexColor("#777777"), fontName="Helvetica-Oblique",
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body", parent=styles["BodyText"], fontSize=10.5, leading=14.5,
        textColor=colors.HexColor("#1a1a1a"), spaceAfter=6,
    )
    section_head = ParagraphStyle(
        "SectionHead", parent=styles["Heading2"], fontSize=15, leading=18,
        textColor=colors.HexColor("#111111"), spaceAfter=8,
    )
    source_title = ParagraphStyle(
        "SourceTitle", parent=styles["BodyText"], fontSize=10.5, leading=13,
        textColor=colors.HexColor("#1a1a1a"), fontName="Helvetica-Bold",
    )
    source_pub = ParagraphStyle(
        "SourcePub", parent=styles["BodyText"], fontSize=9, leading=12,
        textColor=colors.HexColor("#777777"), fontName="Helvetica-Oblique",
        spaceAfter=6,
    )

    story = []
    story.append(Paragraph(TITLE, title_style))
    story.append(Paragraph(SUBTITLE, subtitle_style))
    story.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#dddddd")))
    story.append(Spacer(1, 10))

    for s in SECTIONS:
        block = [
            Paragraph(s["time"], time_style),
            Paragraph(s["label"], label_style),
            Paragraph(s["vo"], body_style),
            Paragraph(s["on_screen"], body_style),
            Paragraph(s["visual"], body_style),
            HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#eaeaea")),
            Spacer(1, 8),
        ]
        story.append(KeepTogether(block))

    story.append(PageBreak())
    story.append(Paragraph("Production Notes", section_head))
    for note in PRODUCTION_NOTES:
        story.append(Paragraph("&bull; &nbsp;" + note, body_style))
    story.append(Spacer(1, 14))

    story.append(Paragraph("Sources", section_head))
    for title, pub in SOURCES:
        story.append(Paragraph(title, source_title))
        story.append(Paragraph(pub, source_pub))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)


if __name__ == "__main__":
    build()
    print(f"wrote {OUTPUT}")
