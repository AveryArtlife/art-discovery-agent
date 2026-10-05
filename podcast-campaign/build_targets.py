#!/usr/bin/env python3
"""Build podcast-targets.csv and podcast-targets.html from data/tier*.json."""
import csv
import html
import json
from pathlib import Path

HERE = Path(__file__).parent
TIER_NAMES = {
    1: ("Tier 1: Launchpad", "Small and niche shows that build reps, clips and a booking record."),
    2: ("Tier 2: Momentum", "Mid-size, successful shows with solid followings. Pitch them with Tier 1 proof."),
    3: ("Tier 3: The Big Leagues", "The biggest shows in the world, with The Joe Rogan Experience as the end goal. Mostly booked through referrals and visibility."),
}


def load():
    shows = []
    for tier in (1, 2, 3):
        path = HERE / "data" / f"tier{tier}.json"
        if path.exists():
            for s in json.loads(path.read_text()):
                s["tier"] = tier
                shows.append(s)
    return shows


def hosts_text(s):
    return "; ".join(f"{h.get('name','')}: {h.get('bio','')}" for h in s.get("hosts", []))


def angles_text(s):
    return " | ".join(f"[{a.get('angle_category','')}] {a.get('hook','')}" for a in s.get("fit_angles", []))


def write_csv(shows):
    cols = ["Tier", "Podcast", "Host(s)", "Genre", "Audience", "Audience source", "Example topics",
            "Stances", "Booking route", "Booking source type", "Booking source URL", "Booking notes",
            "Spotify", "Website", "YouTube", "Proposed angles", "Fit notes",
            "Status", "Date pitched", "Follow-up date", "Result"]
    with open(HERE / "podcast-targets.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for s in shows:
            b = s.get("booking_contact", {}) or {}
            w.writerow([s["tier"], s.get("name"), hosts_text(s), s.get("genre"), s.get("audience_size"),
                        s.get("audience_source"), "; ".join(s.get("topics", [])), s.get("stances"),
                        b.get("route"), b.get("type"), b.get("source_url"), b.get("notes"),
                        s.get("spotify_url"), s.get("website_url"), s.get("youtube_url"),
                        angles_text(s), s.get("avery_fit_notes"), "Not contacted", "", "", ""])


def e(x):
    return html.escape(str(x or ""))


def link(url, label):
    if not url or not str(url).startswith("http"):
        return ""
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>'


def sources(text):
    """Turn a field that may hold several URLs (and notes) into short numbered links."""
    import re
    urls = re.findall(r"https?://[^\s;,]+", str(text or ""))
    rest = re.sub(r"https?://[^\s;,]+", "", str(text or "")).strip(" ;,")
    links = " ".join(link(u, f"source {i}" if len(urls) > 1 else "source") for i, u in enumerate(urls, 1))
    return " ".join(x for x in [e(rest), links] if x)


def card(s):
    b = s.get("booking_contact", {}) or {}
    hosts = "".join(f"<li><b>{e(h.get('name'))}</b>: {e(h.get('bio'))}</li>" for h in s.get("hosts", []))
    topics = "".join(f"<li>{e(t)}</li>" for t in s.get("topics", []))
    angles = "".join(
        f'<li><span class="tag">{e(a.get("angle_category"))}</span><b>{e(a.get("hook"))}</b>'
        f'<span class="why">{e(a.get("why"))}</span></li>' for a in s.get("fit_angles", []))
    links = " · ".join(x for x in [link(s.get("spotify_url"), "Spotify"), link(s.get("website_url"), "Website"),
                                    link(s.get("youtube_url"), "YouTube")] if x)
    route = e(b.get("route"))
    if str(b.get("route", "")).startswith("http"):
        route = link(b["route"], b["route"])
    src = sources(b.get("source_url"))
    search = " ".join([s.get("name", ""), hosts_text(s), s.get("genre", ""), angles_text(s)]).lower()
    return f'''
<article class="show" data-tier="{s["tier"]}" data-search="{e(search)}">
  <header>
    <div><h3>{e(s.get("name"))}</h3><div class="genre">{e(s.get("genre"))}</div></div>
    <div class="aud"><b>{e(s.get("audience_size"))}</b><span>{sources(s.get("audience_source"))}</span></div>
  </header>
  <div class="links">{links}</div>
  <div class="grid">
    <div><h4>Host(s)</h4><ul>{hosts}</ul></div>
    <div><h4>Example topics</h4><ul>{topics}</ul></div>
  </div>
  <div class="grid">
    <div><h4>Standout positions</h4><p>{e(s.get("stances"))}</p></div>
    <div class="book"><h4>Booking contact</h4><p>{route}</p>
      <p class="meta">{e(b.get("type"))} {src}</p><p class="meta">{e(b.get("notes"))}</p></div>
  </div>
  <h4>Proposed angles for Avery</h4><ul class="angles">{angles}</ul>
  <p class="fit"><b>Fit notes:</b> {e(s.get("avery_fit_notes"))}</p>
</article>'''


def write_html(shows):
    sections = []
    for tier in (1, 2, 3):
        tier_shows = [s for s in shows if s["tier"] == tier]
        if not tier_shows:
            continue
        title, blurb = TIER_NAMES[tier]
        sections.append(f'<section class="tier" id="tier{tier}"><h2>{title} <small>{len(tier_shows)} shows</small></h2>'
                        f'<p class="blurb">{blurb}</p>{"".join(card(s) for s in tier_shows)}</section>')
    counts = {t: sum(1 for s in shows if s["tier"] == t) for t in (1, 2, 3)}
    page = TEMPLATE.replace("{{SECTIONS}}", "".join(sections)) \
        .replace("{{TOTAL}}", str(len(shows))) \
        .replace("{{C1}}", str(counts[1])).replace("{{C2}}", str(counts[2])).replace("{{C3}}", str(counts[3]))
    (HERE / "podcast-targets.html").write_text(page)


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Avery Andon Podcast Targets</title>
<style>
:root{--bg:#fafaf8;--card:#fff;--text:#141414;--muted:#626262;--line:#e4e4df;--accent:#d40a00;--tag:#f1efe9}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111;--card:#1a1a1a;--text:#eee;--muted:#a0a0a0;--line:#2c2c2c;--accent:#ff3b30;--tag:#262626}}
:root[data-theme="dark"]{--bg:#111;--card:#1a1a1a;--text:#eee;--muted:#a0a0a0;--line:#2c2c2c;--accent:#ff3b30;--tag:#262626}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:0 16px 64px}
.top{padding:40px 0 16px}h1{font-size:clamp(26px,4vw,38px);margin:0 0 6px;letter-spacing:-.01em}
.sub{color:var(--muted);margin:0}
.bar{position:sticky;top:0;z-index:2;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.bar button{font:inherit;padding:6px 12px;border:1px solid var(--line);background:var(--card);color:var(--text);border-radius:999px;cursor:pointer}
.bar button.on{background:var(--text);color:var(--bg);border-color:var(--text)}
.bar input{flex:1;min-width:160px;font:inherit;padding:7px 12px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--text)}
h2{font-size:24px;margin:40px 0 4px}h2 small{font-size:14px;color:var(--muted);font-weight:500}
.blurb{color:var(--muted);margin:0 0 16px}
.show{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:20px;margin:14px 0}
.show header{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.show h3{margin:0;font-size:19px}.genre{color:var(--muted);font-size:14px}
.aud{text-align:right;max-width:320px}.aud b{display:block;font-size:14px}.aud span{font-size:12px;color:var(--muted);overflow-wrap:anywhere}.aud a{color:var(--accent)}
.links{margin:8px 0 4px;font-size:14px}.links a{color:var(--accent)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}
h4{font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:16px 0 6px}
ul{margin:0;padding-left:18px}p{margin:0}
.book p{overflow-wrap:anywhere}.meta{font-size:13px;color:var(--muted);margin-top:4px}.meta a{color:var(--accent)}
.angles{list-style:none;padding:0}.angles li{padding:8px 0;border-top:1px solid var(--line)}
.angles .tag{display:inline-block;background:var(--tag);font-size:11px;padding:2px 8px;border-radius:4px;margin-right:8px;text-transform:uppercase;letter-spacing:.05em}
.angles .why{display:block;color:var(--muted);font-size:14px}
.fit{margin-top:12px;font-size:14px;padding:10px 12px;background:var(--tag);border-radius:6px}
.hidden{display:none}
@media (max-width:700px){.grid{grid-template-columns:1fr;gap:0}.aud{text-align:left}}
</style></head><body><div class="wrap">
<div class="top"><h1>Avery Andon: Podcast Target List</h1>
<p class="sub">{{TOTAL}} shows in three tiers · Prepared by The Baddest Agency · Re-verify booking contacts before sending</p></div>
<div class="bar">
<button class="on" data-f="all">All ({{TOTAL}})</button><button data-f="1">Tier 1 ({{C1}})</button>
<button data-f="2">Tier 2 ({{C2}})</button><button data-f="3">Tier 3 ({{C3}})</button>
<input type="search" placeholder="Search shows, hosts, angles…" aria-label="Search">
</div>
{{SECTIONS}}
</div>
<script>
const btns=[...document.querySelectorAll('.bar button')],q=document.querySelector('.bar input');let f='all';
function apply(){const t=q.value.toLowerCase();document.querySelectorAll('.show').forEach(s=>{
s.classList.toggle('hidden',!((f==='all'||s.dataset.tier===f)&&s.dataset.search.includes(t)))});
document.querySelectorAll('.tier').forEach(sec=>sec.classList.toggle('hidden',!sec.querySelector('.show:not(.hidden)')))}
btns.forEach(b=>b.onclick=()=>{btns.forEach(x=>x.classList.remove('on'));b.classList.add('on');f=b.dataset.f;apply()});q.oninput=apply;
</script></body></html>"""


if __name__ == "__main__":
    shows = load()
    write_csv(shows)
    write_html(shows)
    print(f"Built {len(shows)} shows")
