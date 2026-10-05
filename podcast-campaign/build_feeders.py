#!/usr/bin/env python3
"""Build feeder-map.html from data/feeders/*.json.

Each JSON file traces where one target show's recent guests appeared
beforehand. Shows that feed more than one target are ranked first.
"""
import html
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
FIT_ORDER = {"high": 0, "medium": 1, "low": 2}


def e(x):
    return html.escape(str(x or ""))


def norm(name):
    """Loose key so 'The Diary of a CEO' and 'Diary Of A CEO' match."""
    n = re.sub(r"\(.*?\)", "", str(name or "")).lower()
    n = re.sub(r"^the\s+|\s+podcast$|\s+show$|[^a-z0-9 ]", "", n.strip())
    return re.sub(r"\s+", " ", n).strip()


def link(url, label):
    if not url or not str(url).startswith("http"):
        return ""
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>'


def sources(text):
    urls = re.findall(r"https?://[^\s;,]+", str(text or ""))
    rest = re.sub(r"https?://[^\s;,]+", "", str(text or "")).strip(" ;,")
    links = " ".join(link(u, f"source {i}" if len(urls) > 1 else "source") for i, u in enumerate(urls, 1))
    return " ".join(x for x in [e(rest), links] if x)


def load():
    return [json.loads(p.read_text()) for p in sorted((HERE / "data" / "feeders").glob("*.json"))]


def unknown(v):
    return not v or str(v).strip().lower() in ("unverified", "null", "none")


def known_shows():
    """Shows already researched in the tier lists, keyed by normalized name."""
    known = {}
    for path in sorted((HERE / "data").glob("tier*.json")):
        for s in json.loads(path.read_text()):
            known[norm(s.get("name"))] = s
    return known


def enrich(targets):
    """Fill missing feeder fields from the tier research, and note which tier a feeder is already in."""
    known = known_shows()
    for t in targets:
        for f in t.get("top_feeders", []):
            k = norm(f.get("show"))
            s = known.get(k) or next((v for kk, v in known.items() if k and (k in kk or kk in k)), None)
            if not s:
                continue
            f["in_tier"] = s.get("tier")
            b = s.get("booking_contact") or {}
            if unknown(f.get("booking_route")) and b.get("route"):
                f["booking_route"], f["booking_type"], f["booking_source"] = b.get("route"), b.get("type"), b.get("source_url")
            if unknown(f.get("audience")) and s.get("audience_size"):
                f["audience"], f["audience_source"] = s.get("audience_size"), s.get("audience_source")
            for field in ("spotify_url", "website_url"):
                if unknown(f.get(field)) and str(s.get(field) or "").startswith("http"):
                    f[field] = s[field]
    return targets


def cross_feeders(targets):
    """Shows appearing in two or more targets' feeder tallies."""
    seen = defaultdict(lambda: {"name": None, "targets": {}})
    for t in targets:
        for row in t.get("feeder_tally", []):
            k = norm(row.get("show"))
            if not k:
                continue
            seen[k]["name"] = seen[k]["name"] or row.get("show")
            seen[k]["targets"][t["target"]] = row.get("count", 0)
    rows = [v for v in seen.values() if len(v["targets"]) > 1]
    return sorted(rows, key=lambda v: (-len(v["targets"]), -sum(v["targets"].values())))


def feeder_card(f):
    angles = "".join(f'<li><span class="tag">{e(a.get("category"))}</span>{e(a.get("hook"))}</li>' for a in f.get("angles", []))
    fit = str(f.get("avery_fit", "")).lower()
    links = " · ".join(x for x in [link(f.get("spotify_url"), "Spotify"), link(f.get("website_url"), "Website")] if x)
    route = e(f.get("booking_route"))
    if str(f.get("booking_route", "")).startswith("http"):
        route = link(f["booking_route"], f["booking_route"])
    return f'''<article class="feeder">
  <header><h4>{e(f.get("show"))}{f' <span class="tier">Tier {f["in_tier"]}</span>' if f.get("in_tier") else ""}</h4><span class="fit fit-{e(fit)}">Fit: {e(fit or "?")}</span></header>
  <div class="meta">{e(f.get("hosts"))} · {e(f.get("genre"))}</div>
  <div class="count"><b>{e(f.get("feeder_count"))}</b> guests later booked · {e(f.get("feeder_evidence"))}</div>
  <div class="row"><span>Audience</span>{"<em>unverified</em>" if unknown(f.get("audience")) else e(f.get("audience")) + " " + ("" if unknown(f.get("audience_source")) else sources(f.get("audience_source")))}</div>
  <div class="row"><span>Booking</span>{"<em>unverified</em>" if unknown(f.get("booking_route")) else route + ("" if unknown(f.get("booking_type")) else f" <em>({e(f.get('booking_type'))})</em>") + ("" if unknown(f.get("booking_source")) else " " + sources(f.get("booking_source")))}</div>
  <div class="row"><span>Why</span>{e(f.get("avery_fit_reason"))}</div>
  <ul class="angles">{angles}</ul>
  <div class="links">{links}</div>
</article>'''


def target_section(t):
    feeders = sorted(t.get("top_feeders", []),
                     key=lambda f: (FIT_ORDER.get(str(f.get("avery_fit", "")).lower(), 3), -(f.get("feeder_count") or 0)))
    tally = "".join(f'<tr><td>{e(r.get("show"))}</td><td class="n">{e(r.get("count"))}</td>'
                    f'<td>{e(", ".join(r.get("guests", [])))}</td></tr>' for r in t.get("feeder_tally", [])[:15])
    guests = ""
    for g in t.get("guests", []):
        prior = "; ".join(f'{e(p.get("show"))} ({e(p.get("date"))}) {link(p.get("source_url"), "↗")}'
                          for p in g.get("prior_appearances", []))
        guests += (f'<tr><td><b>{e(g.get("name"))}</b><br><small>{e(g.get("known_for"))}</small></td>'
                   f'<td>{e(g.get("target_episode_date"))}</td><td>{prior or "<em>none found</em>"}</td></tr>')
    slug = norm(t["target"]).replace(" ", "-")
    return f'''<section class="target" id="{slug}">
  <h2>{e(t["target"])}</h2>
  <div class="path"><h3>Avery's path</h3><p>{e(t.get("avery_path"))}</p></div>
  <p class="patterns"><b>How guests get here:</b> {e(t.get("patterns"))}</p>
  <h3>Top feeder shows, ranked by fit for Avery</h3>
  <div class="feeders">{"".join(feeder_card(f) for f in feeders)}</div>
  <details><summary>Full feeder tally</summary>
    <table><thead><tr><th>Show</th><th>Guests</th><th>Who</th></tr></thead><tbody>{tally}</tbody></table></details>
  <details><summary>Guest-by-guest evidence ({len(t.get("guests", []))} guests traced)</summary>
    <table><thead><tr><th>Guest</th><th>Episode</th><th>Earlier appearances</th></tr></thead><tbody>{guests}</tbody></table>
    <p class="note">{e(t.get("method_notes"))}</p></details>
</section>'''


def build():
    targets = enrich(load())
    cross = cross_feeders(targets)
    names = [t["target"] for t in targets]
    head = "".join(f"<th>{e(n)}</th>" for n in names)
    cross_rows = "".join(
        f'<tr><td><b>{e(c["name"])}</b></td>' + "".join(f'<td class="n">{e(c["targets"].get(n, "–"))}</td>' for n in names) + "</tr>"
        for c in cross)
    cross_html = (f'<table class="cross"><thead><tr><th>Show</th>{head}</tr></thead><tbody>{cross_rows}</tbody></table>'
                  if cross else '<p class="note">No show appeared in more than one target\'s feeder tally.</p>')
    nav = " · ".join(f'<a href="#{norm(n).replace(" ", "-")}">{e(n)}</a>' for n in names)
    page = TEMPLATE.replace("{{NAV}}", nav).replace("{{CROSS}}", cross_html) \
        .replace("{{SECTIONS}}", "".join(target_section(t) for t in targets))
    (HERE / "feeder-map.html").write_text(page)
    print(f"Built feeder map for {len(targets)} targets, {len(cross)} cross-feeders")


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Podcast Feeder Map</title>
<style>
:root{--bg:#0b0c10;--panel:#14161d;--text:#f1f1f3;--muted:#8a8e99;--line:#2a2d36;--blue:#4a6cf7;--blue-soft:#9aa9f5;--green:#3fb37f;--amber:#d9a441;--red:#e5484d;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 Inter,system-ui,-apple-system,sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding:0 16px 80px}
a{color:var(--blue-soft)}
.eyebrow{font:700 12px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.24em;text-transform:uppercase;color:var(--blue);margin:48px 0 14px}
h1{font:400 clamp(40px,7vw,72px)/.95 Anton,Impact,"Arial Narrow",sans-serif;text-transform:uppercase;margin:0 0 16px}
h2{font:400 clamp(30px,5vw,48px)/1 Anton,Impact,"Arial Narrow",sans-serif;text-transform:uppercase;margin:0 0 20px}
h3{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:28px 0 12px}
.lede{color:var(--muted);max-width:68ch}
nav{margin:20px 0;font-weight:600}
.target{border-top:1px solid var(--line);padding-top:48px;margin-top:56px}
.path{background:var(--blue);color:#fff;padding:20px 24px}.path h3{color:rgba(255,255,255,.8);margin:0 0 8px}.path p{margin:0;font-size:17px}
.patterns{color:var(--muted);margin:20px 0}
.feeders{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:14px}
.feeder{background:var(--panel);border:1px solid var(--line);padding:18px}
.feeder header{display:flex;justify-content:space-between;gap:10px;align-items:start}
.feeder h4{margin:0;font-size:18px}.feeder .tier{font:700 10px/1 ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;background:var(--blue);color:#fff;padding:3px 6px;vertical-align:middle;margin-left:6px}
.fit{font:700 11px/1 ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;padding:5px 8px;border:1px solid;white-space:nowrap}
.fit-high{color:var(--green)}.fit-medium{color:var(--amber)}.fit-low{color:var(--red)}
.meta{color:var(--muted);font-size:13px;margin:4px 0 10px}
.count{font-size:14px;margin-bottom:10px}.count b{color:var(--blue-soft);font-size:18px}
.row{font-size:14px;margin:6px 0;overflow-wrap:anywhere}.row span{display:inline-block;min-width:74px;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.08em}
.angles{list-style:none;padding:0;margin:12px 0 8px}.angles li{border-top:1px solid var(--line);padding:7px 0;font-size:14px}
.tag{display:inline-block;font-size:10px;text-transform:uppercase;letter-spacing:.08em;background:var(--line);padding:2px 6px;margin-right:8px}
.links{font-size:13px}
table{width:100%;border-collapse:collapse;font-size:14px;margin:8px 0}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}
th{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
td.n{text-align:center;font-weight:700;color:var(--blue-soft)}
.cross td:first-child{width:40%}
details{margin-top:18px;background:var(--panel);border:1px solid var(--line);padding:12px 16px}
summary{cursor:pointer;font-weight:600}
.note{color:var(--muted);font-size:13px}
small{color:var(--muted)}
.ladder{list-style:none;padding:0;margin:0 0 20px;border-left:2px solid var(--blue)}
.ladder li{padding:14px 0 14px 22px;position:relative}
.ladder li::before{content:"";position:absolute;left:-7px;top:20px;width:12px;height:12px;background:var(--bg);border:2px solid var(--blue);border-radius:50%}
.ladder li:last-child::before{background:var(--blue)}
.ladder .step{display:inline-block;font:700 11px/1 ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);min-width:64px}
.ladder b{font-size:17px}
.ladder p{margin:6px 0 0;color:var(--muted);max-width:72ch}
.tier{font:700 10px/1 ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;background:var(--blue);color:#fff;padding:3px 6px;vertical-align:middle;margin-left:6px}
@media (max-width:640px){table{display:block;overflow-x:auto}}
</style></head><body><div class="wrap">
<div class="eyebrow">/ Avery Andon · Podcast campaign</div>
<h1>Feeder map</h1>
<p class="lede">Where recent guests of the big shows appeared before they were booked. The shows that keep turning up are the stepping stones. Shows that feed more than one target give the most leverage.</p>
<nav>{{NAV}}</nav>
<h3>The recommended route</h3>
<ol class="ladder">
  <li><span class="step">Step 1</span><b>The Jordan Harbinger Show</b> <span class="tier">Tier 2</span>
    <p>Fed 3 Modern Wisdom guests and 1 Shawn Ryan guest. It has a public guest contact page, takes business and outlier-story guests, and is a high fit. This is the first big step.</p></li>
  <li><span class="step">Step 1</span><b>PBD Podcast</b> <span class="tier">Tier 3</span>
    <p>Fed 2 Shawn Ryan guests and 1 Theo Von guest. It records in Fort Lauderdale, a short drive from Avery, and Valuetainment publishes a guest-application page. A high fit on entrepreneurship, wealth and luxury.</p></li>
  <li><span class="step">Step 2</span><b>The Diary of a CEO</b> <span class="tier">Tier 3</span>
    <p>Fed 3 Modern Wisdom guests and 1 Shawn Ryan guest, and Chris Williamson and Steven Bartlett often share guests. It has a published bookings email. Pitch once Steps 1 and 2 have produced clips.</p></li>
  <li><span class="step">Step 2</span><b>High-fit feeders for a single target</b>
    <p>For Modern Wisdom: School of Greatness (Tier 2) and The Skinny Confidential Him &amp; Her. For Theo Von: Full Send (Tier 3). Use them to fill gaps on the way.</p></li>
  <li><span class="step">Step 3</span><b>Modern Wisdom · Theo Von · Shawn Ryan</b>
    <p>Pitch each target with appearances on its own feeders as proof. Each section below gives the angle and route for that show.</p></li>
  <li><span class="step">Goal</span><b>The Joe Rogan Experience</b> <span class="tier">Tier 3</span>
    <p>JRE shows up in all three feeder tallies: Rogan shares guests with Theo Von (3), Shawn Ryan (2) and Modern Wisdom (1). Landing two of the three targets puts Avery in the guest pool Rogan books from.</p></li>
</ol>
<p class="note">Weighed and left off the main route: Rich Roll and TRIGGERnometry each feed two targets but fit Avery poorly. The Tucker Carlson Show feeds Shawn Ryan and Theo Von but is politically charged, so it's a deliberate call to make, not a default step.</p>
<h3>Shows that feed more than one target</h3>
{{CROSS}}
{{SECTIONS}}
<p class="note" style="margin-top:48px">Compiled from web search results. Re-verify booking routes before pitching. Guest counts are evidence of a pattern, not a guarantee.</p>
</div></body></html>"""

if __name__ == "__main__":
    build()
