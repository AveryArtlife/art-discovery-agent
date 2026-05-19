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


# ---------- shared styles / chrome ---------------------------------------

def make_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "T", parent=base["Heading1"], fontSize=22, leading=26,
            textColor=colors.HexColor("#0f0f0f"), spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "S", parent=base["BodyText"], fontSize=10.5, leading=14,
            textColor=colors.HexColor("#666666"), spaceAfter=14,
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontSize=15, leading=19,
            textColor=colors.HexColor("#0f0f0f"),
            spaceBefore=10, spaceAfter=6,
        ),
        "lede": ParagraphStyle(
            "Lede", parent=base["BodyText"], fontSize=12, leading=17,
            textColor=colors.HexColor("#111111"),
            fontName="Helvetica-Bold", spaceAfter=8,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontSize=10.5, leading=15,
            textColor=colors.HexColor("#1a1a1a"), spaceAfter=6,
        ),
        "callout": ParagraphStyle(
            "Callout", parent=base["BodyText"], fontSize=11.5, leading=16,
            textColor=colors.HexColor("#B81818"),
            fontName="Helvetica-Bold", spaceBefore=4, spaceAfter=10,
            leftIndent=8, borderPadding=6,
        ),
        "time": ParagraphStyle(
            "Time", parent=base["Heading2"], fontSize=13, leading=16,
            textColor=colors.HexColor("#B81818"), spaceAfter=2,
        ),
        "label": ParagraphStyle(
            "Label", parent=base["BodyText"], fontSize=9, leading=12,
            textColor=colors.HexColor("#777777"),
            fontName="Helvetica-Oblique", spaceAfter=6,
        ),
        "source_title": ParagraphStyle(
            "ST", parent=base["BodyText"], fontSize=10.5, leading=13,
            textColor=colors.HexColor("#1a1a1a"),
            fontName="Helvetica-Bold",
        ),
        "source_pub": ParagraphStyle(
            "SP", parent=base["BodyText"], fontSize=9, leading=12,
            textColor=colors.HexColor("#777777"),
            fontName="Helvetica-Oblique", spaceAfter=6,
        ),
    }


def make_header_footer(left_label):
    def fn(canvas, doc):
        canvas.saveState()
        width, height = A4
        canvas.setFont("Helvetica-Bold", 8)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawString(20 * mm, height - 12 * mm, left_label)
        canvas.drawRightString(width - 20 * mm, height - 12 * mm, "ART MARKET 2026")
        canvas.setStrokeColor(colors.HexColor("#dddddd"))
        canvas.line(20 * mm, height - 15 * mm, width - 20 * mm, height - 15 * mm)
        canvas.setFont("Helvetica-Oblique", 8)
        canvas.setFillColor(colors.HexColor("#999999"))
        canvas.drawCentredString(width / 2.0, 12 * mm, f"Page {doc.page}")
        canvas.restoreState()
    return fn


def new_doc(filename, title):
    return SimpleDocTemplate(
        filename, pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=22 * mm, bottomMargin=18 * mm,
        title=title,
    )


# ---------- DEEP-DIVE ANALYSIS PDF ---------------------------------------

ANALYSIS_TITLE = "The Real Story Behind the $630 Million Night"
ANALYSIS_SUB = (
    "Why the ultra-wealthy paid record prices for a Pollock and a Brancusi "
    "&mdash; and what it signals about where capital is moving in 2026."
)

ANALYSIS_BODY = [
    ("lede", "This wasn&rsquo;t a recovery. It was a signal."),
    ("body",
     "The Pollock didn&rsquo;t sell because the art market is healthy. It sold "
     "because the ultra-wealthy are rotating into hard assets &mdash; and they "
     "want everyone to know."),
    ("callout", "This is a defensive move dressed up as a cultural moment."),

    ("h2", "The market is K-shaped. Just like the economy."),
    ("body", "The top is booming. The middle is collapsing. The base is hollowing out."),
    ("body",
     "Trophy lots &mdash; works above $10M &mdash; now drive the single largest "
     "share of auction value. Everything below $1M is bleeding."),
    ("callout", "Only billionaires are buying. Everyone else has left the room."),

    ("h2", "There are only ~30 whales in the entire art market."),
    ("body", "That&rsquo;s it. Roughly thirty people decide whether a major auction sinks or swims."),
    ("body",
     "When five of them fight over one Pollock for ten minutes, that isn&rsquo;t a "
     "market. That&rsquo;s an oligopoly flexing."),
    ("callout", "$181 million isn&rsquo;t a price. It&rsquo;s a message."),

    ("h2", "What the message says"),
    ("body",
     "The richest 0.001% &mdash; about 60,000 people &mdash; now control more "
     "wealth than the bottom half of humanity. Their wealth has grown 8% a year "
     "since the 1990s. Twice the rate of everyone below them."),
    ("body", "They&rsquo;re sitting on historic liquidity. And they&rsquo;re nervous."),
    ("body",
     "&bull;&nbsp; Inflation won&rsquo;t die.<br/>"
     "&bull;&nbsp; Rates stay higher for longer.<br/>"
     "&bull;&nbsp; Geopolitical risk keeps rewriting the rules.<br/>"
     "&bull;&nbsp; Cash is losing value every quarter.<br/>"
     "&bull;&nbsp; Bonds aren&rsquo;t safe anymore.<br/>"
     "&bull;&nbsp; Real estate is illiquid and politically exposed."),
    ("body", "So where does the money go?"),
    ("callout",
     "Into things you can hang on a wall, fly across a border, and pass to "
     "your children tax-efficiently."),

    ("h2", "Art is the ultimate portable wealth vehicle"),
    ("body",
     "A $100M painting fits in a crate. It crosses any border. It survives "
     "regime changes. It survives currency collapses. It survives wars."),
    ("body",
     "Gold does that. Diamonds do that. Blue-chip art does that &mdash; "
     "and it appreciates."),
    ("body",
     "Since 1995, contemporary art has returned 11.4% a year. That&rsquo;s "
     "43% above the S&amp;P 500. With no quarterly earnings, no political "
     "headlines, no margin calls."),
    ("callout", "For a billionaire? It&rsquo;s not an investment. It&rsquo;s insurance."),

    ("h2", "The numbers prove the thesis"),
    ("body",
     "&bull;&nbsp; <b>27%</b> of billionaires plan to <i>increase</i> art exposure in 2026. Only 8% plan to reduce.<br/>"
     "&bull;&nbsp; <b>Single-owner sales</b> went from 7% of NY auction value (2015&ndash;2020) to <b>38% in 2025</b>. Estates are being unloaded &mdash; wealth is being repositioned.<br/>"
     "&bull;&nbsp; <b>Auction guarantees</b> are everywhere now. Risk is being structured out before the gavel falls.<br/>"
     "&bull;&nbsp; The Brancusi blew past its old $71M record <b>in the first few bids</b>. That&rsquo;s not bidding &mdash; that&rsquo;s pent-up demand exploding."),
    ("callout", "The smart money already moved. The auction is just where we get to watch."),

    ("h2", "What they are NOT buying"),
    ("body", "Wet paint. Hype. Instagram artists. NFTs. Anything speculative."),
    ("body", "The &ldquo;buy-anything&rdquo; era is over. Capital is retreating to provenance."),
    ("body",
     "<b>What&rsquo;s bid up:</b> museum-validated, art-historical, irreplaceable, "
     "dead-artist, blue-chip works with a paper trail going back 70 years."),
    ("body",
     "<b>What&rsquo;s collapsing:</b> emerging contemporary. Mid-career "
     "speculation. Anything that depends on a story instead of a record."),
    ("callout", "This is a flight to quality. In art form."),

    ("h2", "The bigger picture"),
    ("body",
     "The Pollock sale isn&rsquo;t telling you the economy is fine. It&rsquo;s "
     "telling you the people with the most information about the next ten "
     "years are quietly moving capital into things that can&rsquo;t be printed, "
     "hacked, sanctioned, or devalued by a central bank."),
    ("body", "Art is the new gold."),
    ("body", "But better &mdash; because gold doesn&rsquo;t go up on a museum wall in St. Moritz."),

    ("h2", "The takeaway in one sentence"),
    ("callout",
     "When billionaires pay $181 million for paint on canvas, they&rsquo;re "
     "not buying art. They&rsquo;re buying a parachute."),
]

SOURCES = [
    ("In a &lsquo;K-shaped&rsquo; economy, the art market&rsquo;s recovery could rely on the super-rich",
     "The Art Newspaper &mdash; Jan 2026"),
    ("State of the Art Market: Trophy Lots and the New Competitive Auction Landscape",
     "Artnet News"),
    ("Christie&rsquo;s sells $1.1 billion in art in one night",
     "CNN &mdash; May 19, 2026"),
    ("Will the Recent Art Market Momentum Continue Into 2026?",
     "Artnet News"),
    ("Art Market 2026 Exposed: Critical Wealth Strategies &amp; Trends",
     "Aurora Athena"),
    ("Smart Billions Are Quietly Moving to Art",
     "Medium &mdash; Jan 2026"),
    ("Why Do Billionaires Invest in Art?", "MyArtBroker"),
    ("Art as a Safe Haven in 2026: Inflation, Rates &amp; Geopolitical Risk",
     "Galeria Cortina"),
    ("Art Market Update Spring 2026",
     "Bank of America Private Bank"),
]


def build_analysis(filename="art_market_analysis.pdf"):
    s = make_styles()
    doc = new_doc(filename, "Art Market Analysis - The Real Story")
    story = [
        Paragraph(ANALYSIS_TITLE, s["title"]),
        Paragraph(ANALYSIS_SUB, s["subtitle"]),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#dddddd")),
        Spacer(1, 8),
    ]
    for kind, text in ANALYSIS_BODY:
        story.append(Paragraph(text, s[kind]))
    story.append(PageBreak())
    story.append(Paragraph("Sources", s["h2"]))
    for title, pub in SOURCES:
        story.append(Paragraph(title, s["source_title"]))
        story.append(Paragraph(pub, s["source_pub"]))
    doc.build(
        story,
        onFirstPage=make_header_footer("DEEP DIVE  /  $630M NIGHT"),
        onLaterPages=make_header_footer("DEEP DIVE  /  $630M NIGHT"),
    )
    print(f"wrote {filename}")


# ---------- REWRITTEN REELS SCRIPT (V2: "Parachute, not painting") -------

V2_TITLE = "IG REELS SCRIPT v2: A Parachute, Not a Painting"
V2_SUB = (
    "Runtime: ~60 seconds &nbsp;|&nbsp; Tone: serious, analytical, viral "
    "&nbsp;|&nbsp; Structure: MrBeast retention &mdash; hook, escalate, reframe, "
    "thesis, loop"
)

V2_SECTIONS = [
    {
        "time": "[0:00 &ndash; 0:03] &nbsp;HOOK",
        "label": "Reframe the headline. Subvert the obvious read.",
        "vo": ("<b>VOICEOVER (low, deliberate):</b> &ldquo;Five billionaires just "
               "fought for ten minutes over a Pollock. They didn&rsquo;t buy a "
               "painting. They bought a parachute.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;$181 MILLION&rdquo; over Pollock canvas.",
        "visual": "<b>VISUAL:</b> Slow zoom on the Pollock. Gavel slam. Title card hits hard.",
    },
    {
        "time": "[0:03 &ndash; 0:14] &nbsp;THE EVENT",
        "label": "Anchor the viewer in the receipts.",
        "vo": ("<b>VOICEOVER:</b> &ldquo;Last week at Christie&rsquo;s &mdash; one "
               "night, sixteen lots from the Newhouse estate, <b>$630 million</b> "
               "sold. A Pollock at $181M. A Brancusi at $107M. Both records.&rdquo;"
               "<br/><br/>"
               "<b>VOICEOVER:</b> &ldquo;The Brancusi broke its old record in the "
               "first few bids.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> Headline cards stack up. &ldquo;RECORD.&rdquo; &ldquo;RECORD.&rdquo;",
        "visual": "<b>VISUAL:</b> Cut between paddle raises, the Brancusi rotating, price ticker.",
    },
    {
        "time": "[0:14 &ndash; 0:25] &nbsp;THE REFRAME",
        "label": "Drop the analytical bomb. This is where the video earns the share.",
        "vo": ("<b>VOICEOVER:</b> &ldquo;Here&rsquo;s what the headlines miss. "
               "There are only about <b>thirty whales</b> in the entire global "
               "art market. Five of them were in that room.&rdquo;<br/><br/>"
               "<b>VOICEOVER:</b> &ldquo;This isn&rsquo;t a market. It&rsquo;s an "
               "oligopoly flexing.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;30 WHALES = 1 MARKET.&rdquo;",
        "visual": "<b>VISUAL:</b> Graphic: 30 dots on a global map. Five glow red.",
    },
    {
        "time": "[0:25 &ndash; 0:40] &nbsp;THE WHY",
        "label": "Explain the macro pressure cooker driving the move.",
        "vo": ("<b>VOICEOVER:</b> &ldquo;Inflation won&rsquo;t die. Rates stay "
               "higher for longer. Cash is losing value every quarter.&rdquo;"
               "<br/><br/>"
               "<b>VOICEOVER:</b> &ldquo;So the richest 0.001 percent are doing "
               "what they&rsquo;ve done in every crisis for 500 years. They&rsquo;re "
               "buying things you can&rsquo;t print, can&rsquo;t hack, "
               "can&rsquo;t sanction, and can&rsquo;t devalue.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> Checklist crosses off: &ldquo;CASH. BONDS. REAL ESTATE.&rdquo; Then: &ldquo;ART.&rdquo; circled.",
        "visual": "<b>VISUAL:</b> News chyrons of inflation / war / banking stress flash by.",
    },
    {
        "time": "[0:40 &ndash; 0:50] &nbsp;THE THESIS",
        "label": "Make the abstract concrete. Land the metaphor.",
        "vo": ("<b>VOICEOVER:</b> &ldquo;A $100 million painting fits in a "
               "crate. It crosses any border. It survives regime changes, "
               "currency collapses, and wars.&rdquo;<br/><br/>"
               "<b>VOICEOVER:</b> &ldquo;Gold does that. Diamonds do that. "
               "Art does it <i>and</i> appreciates 11 percent a year.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;ART = NEW GOLD&rdquo;",
        "visual": "<b>VISUAL:</b> Painting in a crate being loaded into a private jet.",
    },
    {
        "time": "[0:50 &ndash; 0:57] &nbsp;THE PROOF",
        "label": "Hit them with stats while the thesis is hot.",
        "vo": ("<b>VOICEOVER:</b> &ldquo;Twenty-seven percent of billionaires "
               "plan to <i>increase</i> their art exposure this year. Only "
               "eight percent are pulling back.&rdquo;<br/><br/>"
               "<b>VOICEOVER:</b> &ldquo;The smart money already moved. The "
               "auction is just where we get to watch.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;27% IN.  8% OUT.&rdquo;",
        "visual": "<b>VISUAL:</b> Two-bar chart slams in. Red dwarfed by green.",
    },
    {
        "time": "[0:57 &ndash; 1:00] &nbsp;CLOSE",
        "label": "Land the loop. Quote-bait the caption.",
        "vo": ("<b>VOICEOVER (slow):</b> &ldquo;They&rsquo;re not buying "
               "paintings. They&rsquo;re buying parachutes. Follow if you want "
               "to know what they&rsquo;re buying next.&rdquo;"),
        "on_screen": "<b>ON SCREEN:</b> &ldquo;FOLLOW &rarr;&rdquo;",
        "visual": "<b>VISUAL:</b> Cut to the opening gavel slam. Loop-ready.",
    },
]

V2_NOTES = [
    "<b>Hook variants to A/B test:</b>",
    "&nbsp;&nbsp;&bull; &ldquo;Five billionaires just fought over a painting. They weren&rsquo;t buying art &mdash; they were buying insurance.&rdquo;",
    "&nbsp;&nbsp;&bull; &ldquo;The richest people on earth just spent $630 million in one night. Here&rsquo;s what they actually bought.&rdquo;",
    "&nbsp;&nbsp;&bull; &ldquo;A painting sold for $181 million this week. The real story isn&rsquo;t the price.&rdquo;",
    "<b>Caption:</b> &ldquo;30 whales. 1 market. $630M in one night. They&rsquo;re not buying paintings &mdash; they&rsquo;re buying parachutes. Here&rsquo;s where the smart money is going.&rdquo;",
    "<b>Pace:</b> No shot longer than 1.5 seconds before the reframe at 0:14. Slow down deliberately at 0:50&ndash;1:00 to let the thesis land.",
    "<b>Audio:</b> Tense cinematic build. Cut the music dead at the &ldquo;oligopoly flexing&rdquo; line. Drop bass back in on &ldquo;art = new gold.&rdquo;",
    "<b>Aspect:</b> 9:16, 1080&times;1920. Burn captions for sound-off retention.",
    "<b>Posting:</b> Lead carousel slide should be the &ldquo;parachute&rdquo; line. Cross-post to TikTok and YouTube Shorts unchanged.",
]


def build_script_v2(filename="art_market_reels_script_v2.pdf"):
    s = make_styles()
    doc = new_doc(filename, "IG Reels Script v2 - Parachute Not Painting")
    story = [
        Paragraph(V2_TITLE, s["title"]),
        Paragraph(V2_SUB, s["subtitle"]),
        HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#dddddd")),
        Spacer(1, 10),
    ]
    for sec in V2_SECTIONS:
        block = [
            Paragraph(sec["time"], s["time"]),
            Paragraph(sec["label"], s["label"]),
            Paragraph(sec["vo"], s["body"]),
            Paragraph(sec["on_screen"], s["body"]),
            Paragraph(sec["visual"], s["body"]),
            HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#eaeaea")),
            Spacer(1, 8),
        ]
        story.append(KeepTogether(block))
    story.append(PageBreak())
    story.append(Paragraph("Production Notes", s["h2"]))
    for note in V2_NOTES:
        story.append(Paragraph(note, s["body"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Sources", s["h2"]))
    for title, pub in SOURCES:
        story.append(Paragraph(title, s["source_title"]))
        story.append(Paragraph(pub, s["source_pub"]))
    doc.build(
        story,
        onFirstPage=make_header_footer("IG REELS v2  /  PARACHUTE"),
        onLaterPages=make_header_footer("IG REELS v2  /  PARACHUTE"),
    )
    print(f"wrote {filename}")


if __name__ == "__main__":
    build_analysis()
    build_script_v2()
