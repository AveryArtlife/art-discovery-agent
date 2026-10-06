#!/usr/bin/env python3
"""Export data/master_list.json to podcast-master.pdf with clickable links.

Builds a print-layout HTML page and prints it with headless Chromium through Playwright
(links stay clickable in Chromium's PDF output). Run build_master.py first.
"""
import base64
import html
import json
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path

from build_master import size_summary

HERE = Path(__file__).parent
GROUPS = ["Art, design & fashion", "Business & founders", "Culture, hip-hop & celebrity",
          "Ideas, politics & true stories", "Wealth, investing & real estate", "Latin & regional business",
          "Luxury & high net worth", "Philanthropy & community", "Other"]
TIERS = {1: ("Tier 1: Entry-level", "The widest net, worked in volume. South Florida and high-fit shows first."),
         2: ("Tier 2: Mid-size", "Pitch with Tier 1 appearances as proof."),
         3: ("Tier 3: Major", "The gateway shows and the goal. Mostly booked through introductions and visibility.")}
FIT_RANK = {"high": 0, "medium": 1, "low": 2}
URL = re.compile(r"https?://[^\s;,)]+")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def e(x):
    return html.escape(str(x or ""))


def blank(x):
    return not x or str(x).strip().lower().startswith(("unverified", "unknown", "none", "null", "host unverified", "hosts unverified"))


def short(x, n):
    x = re.sub(r"\s+", " ", str(x or "")).strip()
    return x if len(x) <= n else x[:n].rsplit(" ", 1)[0].rstrip(",;:-") + "…"


def linkify(text):
    """Escape text, turning URLs and email addresses into clickable links."""
    out, pos = [], 0
    for m in sorted([*URL.finditer(text), *EMAIL.finditer(text)], key=lambda m: m.start()):
        if m.start() < pos:
            continue
        out.append(e(text[pos:m.start()]))
        target = m.group(0).rstrip(".")
        href = target if target.startswith("http") else f"mailto:{target}"
        label = re.sub(r"^https?://(www\.)?", "", target).rstrip("/")
        out.append(f'<a href="{e(href)}">{e(label)}</a>')
        pos = m.start() + len(target)
    out.append(e(text[pos:]))
    return "".join(out)


def font_face(name, file, weight):
    data = base64.b64encode((HERE / "assets" / "fonts" / file).read_bytes()).decode()
    return f"@font-face{{font-family:'{name}';font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}"


def row(m):
    name = e(short(m["name"], 60))
    if str(m.get("url") or "").startswith("http"):
        name = f'<a href="{e(m["url"])}">{name}</a>'
    badge = '<span class="sf">SoFla</span>' if m["south_florida"] else ""
    hosts = "" if blank(m.get("hosts")) else e(short(re.sub(r"\s*\([^)]*\)?", "", str(m["hosts"])), 60))
    leads = []
    if m["feeds_into"]:
        leads.append('<span class="feed">→ ' + e(", ".join(short(re.sub(r"\s*\([^)]*\)?", "", f), 34) for f in m["feeds_into"][:2])) + "</span>")
    if not blank(m.get("booking")):
        leads.append(linkify(short(m["booking"], 110)))
    fit = m.get("fit") or ""
    size = e(size_summary(m)).replace(" · ", "<br>") or (
        '<span class="na">not published</span>' if m.get("size_checked") else '<span class="na">to check</span>')
    loc = e(m.get("location") or "")
    if loc and m.get("location_basis") == "est.":
        loc += ' <span class="na">(est.)</span>'
    return (f'<tr><td class="show">{name} {badge}<div class="hosts">{hosts}</div></td>'
            f'<td class="size">{size}</td><td class="loc">{loc}</td>'
            f'<td><span class="fit fit-{e(fit)}">{e(fit)}</span></td>'
            f'<td>{e(short(m.get("angle"), 130))}</td><td class="lead">{"<br>".join(leads)}</td></tr>')


def build_html(rows):
    by_tier = Counter(m["tier"] for m in rows)
    by_group = Counter((m["group"], m["tier"]) for m in rows)
    sf = sum(m["south_florida"] for m in rows)
    summary = "".join(
        f'<tr><td>{e(g)}</td>' + "".join(f'<td class="n">{by_group[(g, t)]}</td>' for t in (1, 2, 3)) + "</tr>"
        for g in GROUPS if any(by_group[(g, t)] for t in (1, 2, 3)))
    sections = []
    for t, (title, blurb) in TIERS.items():
        parts = [f'<section class="tier"><h2>{title} <span>{by_tier[t]} shows</span></h2><p class="blurb">{blurb}</p>']
        for g in GROUPS:
            group_rows = sorted((m for m in rows if m["tier"] == t and m["group"] == g),
                                key=lambda m: (not m["south_florida"], FIT_RANK.get(m.get("fit"), 3), m["name"].lower()))
            if not group_rows:
                continue
            parts.append(f'<h3>{e(g)} <span>({len(group_rows)})</span></h3><table><colgroup><col class="c1"><col class="cs"><col class="cl"><col class="c2"><col class="c3"><col class="c4"></colgroup>'
                         '<thead><tr><th>Show / host(s)</th><th>Size</th><th>Location</th><th>Fit</th><th>Avery\'s angle</th><th>Leads to / booking</th></tr></thead><tbody>'
                         + "".join(row(m) for m in group_rows) + "</tbody></table>")
        parts.append("</section>")
        sections.append("".join(parts))
    fonts = "".join([font_face("Anton", "anton-latin-400-normal.woff2", 400),
                     font_face("Inter", "inter-latin-400-normal.woff2", 400),
                     font_face("Inter", "inter-latin-600-normal.woff2", 600),
                     font_face("JetBrains Mono", "jetbrains-mono-latin-700-normal.woff2", 700)])
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Avery Andon: Podcast Master List</title><style>
{fonts}
@page{{size:Letter landscape;margin:0.5in 0.45in 0.6in}}
*{{box-sizing:border-box}}
body{{margin:0;font:8.6pt/1.35 Inter,Helvetica,Arial,sans-serif;color:#15161a}}
a{{color:#2f4fd6;text-decoration:none}}
.cover{{background:#0b0c10;color:#f1f1f3;padding:28px 32px 26px;margin-bottom:18px}}
.eyebrow{{font:700 8pt 'JetBrains Mono',monospace;letter-spacing:.24em;color:#4a6cf7;text-transform:uppercase}}
.eyebrow::before{{content:"/ ";color:#8a8e99}}
h1{{font:400 44pt/0.95 Anton,Impact,sans-serif;text-transform:uppercase;margin:10px 0 8px}}
.cover p{{margin:0;color:#b7bac3;font-size:10pt;max-width:760px}}
.stats{{display:flex;gap:28px;margin-top:16px}}
.stats div b{{display:block;font:400 24pt/1 Anton,Impact,sans-serif;color:#fff}}
.stats div span{{font:700 7pt 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#8a8e99}}
.summary{{width:60%;margin:0 0 6px;table-layout:auto}}
.summary td,.summary th{{padding:3px 8px}}
.legend{{color:#5b5f6b;font-size:8pt;margin:6px 0 0}}
h2{{font:400 22pt/1 Anton,Impact,sans-serif;text-transform:uppercase;margin:0 0 4px;break-after:avoid}}
h2 span{{font:600 9pt Inter,sans-serif;color:#5b5f6b;text-transform:none;margin-left:8px}}
.tier{{break-before:page}}
.blurb{{margin:0 0 10px;color:#5b5f6b}}
h3{{font:700 8.5pt 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#2f4fd6;margin:14px 0 4px;break-after:avoid}}
h3 span{{color:#8a8e99}}
table{{width:100%;border-collapse:collapse;table-layout:fixed}}
col.c1{{width:22%}}col.cs{{width:11%}}col.cl{{width:10%}}col.c2{{width:5.5%}}col.c3{{width:28%}}col.c4{{width:23.5%}}
thead{{display:table-header-group}}
th{{text-align:left;font:700 6.8pt 'JetBrains Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:#5b5f6b;border-bottom:1.2px solid #15161a;padding:4px 6px}}
td{{vertical-align:top;padding:4px 6px;border-bottom:.5px solid #dcdde2;overflow-wrap:anywhere}}
tr{{break-inside:avoid}}
td.show a{{font-weight:600}}
td.show{{font-weight:600}}
.hosts{{font-weight:400;color:#5b5f6b;font-size:7.8pt}}
.sf{{font:700 6pt 'JetBrains Mono',monospace;letter-spacing:.08em;background:#4a6cf7;color:#fff;padding:1px 4px;vertical-align:1px}}
.fit{{font:700 6.4pt 'JetBrains Mono',monospace;text-transform:uppercase}}
.fit-high{{color:#1f8a5a}}.fit-medium{{color:#a8741a}}.fit-low{{color:#c0383d}}
.lead{{font-size:7.8pt;color:#3a3d46}}
.feed{{color:#2f4fd6;font-weight:600}}
.size,.loc{{font-size:7.6pt}}.size{{font-weight:600}}.na{{color:#9a9da6;font-weight:400}}
td.n{{text-align:center;font-weight:600}}
</style></head><body>
<div class="cover"><div class="eyebrow">Avery Andon · Podcast campaign · The Baddest Agency</div>
<h1>Podcast master list</h1>
<p>Every show on the ladder from entry-level to Joe Rogan, by tier and category. Show names and booking routes are clickable. Re-verify each booking route before pitching.</p>
<div class="stats"><div><b>{len(rows)}</b><span>Shows</span></div><div><b>{by_tier[1]}</b><span>Tier 1 entry</span></div><div><b>{by_tier[2]}</b><span>Tier 2 mid</span></div><div><b>{by_tier[3]}</b><span>Tier 3 major</span></div><div><b>{sf}</b><span>South Florida</span></div></div></div>
<table class="summary"><thead><tr><th>Category</th><th>Tier 1</th><th>Tier 2</th><th>Tier 3</th></tr></thead><tbody>{summary}</tbody></table>
<p class="legend"><span class="sf">SoFla</span> records in South Florida · <b>Size</b>: listeners per episode, YouTube and Instagram followers, Apple ratings, where published; \u201cto check\u201d = not yet researched · <b>Fit</b> for Avery: high, medium, low · <span class="feed">→</span> a guest of this show later appeared on the show named · As of {date.today():%B %-d, %Y}</p>
{"".join(sections)}
</body></html>"""


NODE = r"""
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[1]); await p.waitForTimeout(300);
  await p.pdf({ path: process.argv[2], format: 'Letter', landscape: true, printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font:7px Helvetica;color:#8a8e99;padding:0 0.45in;display:flex;justify-content:space-between"><span>Avery Andon · Podcast master list · The Baddest Agency</span><span><span class=pageNumber></span> / <span class=totalPages></span></span></div>' });
  await b.close();
})();
"""

if __name__ == "__main__":
    rows = json.loads((HERE / "data" / "master_list.json").read_text())
    page = HERE / "podcast-master-print.html"
    page.write_text(build_html(rows))
    subprocess.run(["node", "-e", NODE, str(page.resolve()), str((HERE / "podcast-master.pdf").resolve())], check=True)
    page.unlink()
    print("Wrote podcast-master.pdf")
