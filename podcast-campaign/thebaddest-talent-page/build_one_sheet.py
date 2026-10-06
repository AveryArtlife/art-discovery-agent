#!/usr/bin/env python3
"""Build Avery Andon's one-page talent one-sheet (Letter, clickable links).

Output: public/talent/avery-andon/avery-andon-one-sheet.pdf (the talent page links to it).
Prints HTML to PDF with headless Chromium via the globally installed Playwright.
"""
import base64
import os
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
ASSET = HERE / "public" / "talent" / "avery-andon"
# Outlet logos: <slug>.svg or .png in PRESS_DIR (default ./press). Until a file is there, the outlet's name shows in type.
PRESS_DIR = Path(os.environ.get("PRESS_DIR", HERE / "press"))
PRESS = [("The Wall Street Journal", "wsj"), ("Financial Times", "financial-times"), ("Forbes", "forbes"),
         ("Vanity Fair", "vanity-fair"), ("New York Post", "new-york-post"), ("Rolling Stone", "rolling-stone")]
INSTAGRAM_FOLLOWERS = "153K"


def press_html():
    out = []
    for name, slug in PRESS:
        f = next((PRESS_DIR / f"{slug}.{ext}" for ext in ("svg", "png") if (PRESS_DIR / f"{slug}.{ext}").exists()), None)
        if f:
            mime = "image/svg+xml" if f.suffix == ".svg" else "image/png"
            out.append(f'<img src="data:{mime};base64,{b64(f)}" alt="{name}">')
        else:
            out.append(f"<span>{name}</span>")
    return "".join(out)
FONTS = HERE.parent / "assets" / "fonts"
PAGE_URL = "https://www.thebaddest.com/talent/avery-andon"


def b64(path):
    return base64.b64encode(path.read_bytes()).decode()


def face(name, file, weight):
    return f"@font-face{{font-family:'{name}';font-weight:{weight};src:url(data:font/woff2;base64,{b64(FONTS / file)}) format('woff2')}}"


EPISODES = [
    ("09", "Brandon Boyd", "Incubus frontman on singing, painting and the artist's life",
     "https://creators.spotify.com/pod/profile/artlife-podcast/episodes/09---Brandon-Boyd-Lead-Singer-INCUBUS--Artist-e2fmj5t"),
    ("08", "Brian Clarke", "Executor of the Francis Bacon and Zaha Hadid estates",
     "https://creators.spotify.com/pod/profile/artlife-podcast/episodes/08---Brian-Clarke-Executor-of-Francis-Bacon--Zaha-Hadids-Estates-e2fmj68"),
    ("02", "Said Taghmaoui", "Actor on art, film and identity", "https://open.spotify.com/episode/2iflEr47JgHmhi1PXRzv2V"),
    ("15", "PJ, Exotic Car Hacks", "Cars and watches as collectibles and investments",
     "https://creators.spotify.com/pod/profile/artlife-podcast/episodes/15---PJ-Exotic-Car-Hacks-e2pbsgk"),
]
TOPICS = [
    ("Entrepreneurship", "Building ArtLife and the “Click & Mortar” model"),
    ("Brand building", "How an artist becomes a brand: the Alec Monopoly playbook"),
    ("Art & money", "What really sets the price of art, and what buyers get wrong"),
    ("Celebrity & culture", "Advising celebrities and hip-hop's collectors"),
    ("Early adopter", "Blue-chip art online since 2015, NFTs and what AI changes"),
    ("Giving back", "Children's causes and conservation"),
]


def html():
    eps = "".join(f'<li><a href="{u}"><span class="n">{n}</span><span><b>{g}</b> · {d}</span></a></li>' for n, g, d, u in EPISODES)
    topics = "".join(f"<li><b>{t}</b>{d}</li>" for t, d in TOPICS)
    fonts = "".join([face("Anton", "anton-latin-400-normal.woff2", 400), face("Inter", "inter-latin-400-normal.woff2", 400),
                     face("Inter", "inter-latin-600-normal.woff2", 600), face("JetBrains Mono", "jetbrains-mono-latin-700-normal.woff2", 700)])
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Avery Andon | One-sheet | The Baddest Agency</title><style>
{fonts}
@page{{size:Letter;margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0}}
body{{width:8.5in;height:11in;overflow:hidden;font:8.6pt/1.45 Inter,Helvetica,sans-serif;color:#15161a;background:#fff}}
a{{color:#2f4fd6;text-decoration:none}}
.top{{background:#0b0c10;color:#f1f1f3;display:grid;grid-template-columns:2.55in 1fr;height:3.55in}}
.photo{{background:url(data:image/jpeg;base64,{b64(ASSET / 'headshot.jpg')}) 50% 15%/cover}}
.id{{padding:.32in .4in .28in;display:flex;flex-direction:column}}
.brand{{display:flex;justify-content:space-between;align-items:baseline}}
.brand b{{font:400 11pt Anton,Impact,sans-serif;letter-spacing:.03em}}
.mono{{font:700 6.6pt 'JetBrains Mono',monospace;letter-spacing:.24em;text-transform:uppercase}}
.brand .mono{{color:#8a8e99}}
h1{{font:400 46pt/.86 Anton,Impact,sans-serif;text-transform:uppercase;margin:.2in 0 0}}
h1 span{{display:block;color:transparent;-webkit-text-stroke:1.4px #f1f1f3}}
.role{{color:#9aa9f5;margin:.13in 0 .1in}}
.lede{{font-size:10pt;line-height:1.45;color:#d6d8de;margin:0}}.lede b{{color:#fff;font-weight:600}}
.press{{margin-top:auto;padding-top:.12in;border-top:1px solid #2a2d36;font:600 8.6pt Georgia,serif;color:#f1f1f3;display:flex;flex-wrap:wrap;gap:3px 14px}}
.press .mono{{color:#4a6cf7;width:100%;margin-bottom:2px}}
.press{{align-items:center}}.press img{{height:15px;width:auto;max-width:1.2in;filter:brightness(0) invert(1);opacity:.92}}
.body{{display:grid;grid-template-columns:1fr 2.55in;gap:.32in;padding:.3in .4in 0}}
h2{{font:700 7pt 'JetBrains Mono',monospace;letter-spacing:.22em;text-transform:uppercase;color:#2f4fd6;margin:0 0 .07in}}
h2::before{{content:"/ ";color:#9a9da6}}
p{{margin:0 0 .08in}}
.block{{margin-bottom:.17in}}
ul{{list-style:none;margin:0;padding:0}}
.topics{{display:grid;grid-template-columns:1fr 1fr;gap:5px 16px}}
.topics li b{{display:block;font:400 10.5pt/1.1 Anton,Impact,sans-serif;text-transform:uppercase;letter-spacing:.01em}}
.topics li{{color:#4a4d57;font-size:8pt}}
.eps li a{{display:grid;grid-template-columns:22px 1fr;gap:6px;padding:4px 0;border-top:.6px solid #e1e2e6;color:#15161a}}
.eps .n{{font:700 7.4pt 'JetBrains Mono',monospace;color:#2f4fd6}}
.eps b{{color:#2f4fd6}}
.side{{border-left:.6px solid #e1e2e6;padding-left:.24in}}
.facts li{{padding:4px 0;border-top:.6px solid #e1e2e6}}
.facts .mono{{display:block;color:#8a8e99;font-size:6pt;margin-bottom:1px}}
.links li{{padding:3px 0}}
.links a{{font-weight:600}}
.ig{{display:block;color:#15161a;border:.6px solid #e1e2e6;padding:7px 10px 8px;margin-bottom:5px}}.ig .mono{{display:block;color:#8a8e99;font-size:6pt}}.ig b{{font:400 26pt/1 Anton,Impact,sans-serif;color:#2f4fd6;margin-right:5px}}.ig .lbl{{font-weight:600}}
.book{{background:#4a6cf7;color:#fff;padding:.16in .18in;margin-top:.04in}}
.book b{{display:block;font:400 17pt/1 Anton,Impact,sans-serif;text-transform:uppercase}}
.book .mono{{display:block;color:rgba(255,255,255,.85);margin:4px 0 7px;font-size:6.2pt}}
.book a{{color:#fff;display:block;font-weight:600;padding:2px 0}}
.foot{{position:absolute;left:.4in;right:.4in;bottom:.22in;display:flex;justify-content:space-between;border-top:.6px solid #e1e2e6;padding-top:6px;color:#8a8e99}}
.foot a{{color:#2f4fd6}}
</style></head><body>
<div class="top"><div class="photo" role="img" aria-label="Avery Andon"></div><div class="id">
<div class="brand"><b>THE BADDEST AGENCY</b><span class="mono">Talent one-sheet</span></div>
<h1>Avery<span>Andon</span></h1>
<div class="role mono">Art dealer · Entrepreneur · Podcast host · Miami</div>
<p class="lede">The Miami art dealer who turned <b>Street Artist Alec Monopoly into a global brand</b>, and one of the innovators of online art sales: he launched ArtLife.com as an online blue-chip art gallery back in 2015.</p>
<div class="press"><span class="mono">As featured in</span>{press_html()}</div>
</div></div>
<div class="body"><div>
<div class="block"><h2>Bio</h2>
<p>Avery Andon is a Miami-based art dealer, entrepreneur and philanthropist, best known for developing Alec Monopoly into a global name, with sold-out exhibitions from New York to Morocco and brand partnerships that established him among the world's most profitable street artists.</p>
<p>An innovator of online art sales, he launched <a href="https://www.artlife.com">ArtLife.com</a> in 2015 as one of the first online-only blue-chip galleries, and coined “Click &amp; Mortar” for its model of social-first marketing plus curated pop-ups. An early champion of Hebru Brantley and Jammie Holmes, he advises celebrities, collectors and companies on art. He hosts <i>ArtLife with Avery Andon</i>, and supports UCLA Mattel Children's Hospital, MindUP, City Seats with the New York Yankees, WildAid and the Amazon Conservation Team.</p></div>
<div class="block"><h2>Conversation topics</h2><ul class="topics">{topics}</ul></div>
<div class="block"><h2>Highlights: ArtLife with Avery Andon (Spotify)</h2><ul class="eps">{eps}</ul></div>
</div><div class="side">
<div class="block"><h2>At a glance</h2><ul class="facts">
<li><span class="mono">Based in</span>Miami, FL</li>
<li><span class="mono">Records</span>In studio, on location or remote</li>
<li><span class="mono">Launched</span>ArtLife.com, 2015</li>
<li><span class="mono">Hosts</span>ArtLife with Avery Andon</li></ul></div>
<div class="block"><h2>Full-length interviews</h2><ul class="links">
<li><a href="https://www.youtube.com/watch?v=-Uf38sTS_TU">Paint The Town Podcast, Ep. 109</a> (YouTube)</li>
<li><a href="https://cleanbreakpodcast.com/episodes/avery-andon">Clean Break with Matt Gondek, Ep. 139</a></li>
<li><a href="https://open.spotify.com/show/0wGmV3avezL7l1dAS5zHM6">ArtLife with Avery Andon, all episodes</a></li></ul></div>
<div class="block"><h2>Social snapshot</h2><a class="ig" href="https://instagram.com/averyandon"><span class="mono">Instagram · @averyandon</span><b>{INSTAGRAM_FOLLOWERS}</b><span class="lbl">followers</span></a><ul class="links">
<li><a href="https://instagram.com/artlifepodcast">@artlifepodcast</a> · <a href="https://open.spotify.com/show/0wGmV3avezL7l1dAS5zHM6">ArtLife Podcast</a></li>
<li><a href="https://instagram.com/artlife">@artlife</a> · <a href="https://www.artlife.com">artlife.com</a></li></ul></div>
<div class="book"><b>Book Avery</b><span class="mono">David Harris · VP / Talent Coordinator</span>
<a href="mailto:David@thebaddest.com?subject=Booking%20request%3A%20Avery%20Andon">David@thebaddest.com</a>
<a href="tel:+13057919990">(305) 791-9990</a>
<a href="https://instagram.com/thebaddestagency">@thebaddestagency</a></div>
</div></div>
<div class="foot mono"><span>The Baddest Agency · Est. 2016</span><a href="{PAGE_URL}">thebaddest.com/talent/avery-andon</a></div>
</body></html>"""


NODE = r"""
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[1]); await p.waitForTimeout(300);
  await p.pdf({ path: process.argv[2], format: 'Letter', printBackground: true, preferCSSPageSize: true, pageRanges: '1' });
  await b.close(); })();
"""

if __name__ == "__main__":
    tmp = HERE / "one-sheet.tmp.html"
    tmp.write_text(html())
    out = ASSET / "avery-andon-one-sheet.pdf"
    subprocess.run(["node", "-e", NODE, str(tmp.resolve()), str(out.resolve())], check=True)
    tmp.unlink()
    print(f"Wrote {out.relative_to(HERE)}")
