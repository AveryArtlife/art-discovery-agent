#!/usr/bin/env python3
"""Merge every research file into one de-duplicated master list of podcasts.

Inputs (all optional):
  data/tier*.json              curated 47-show target list (most detailed, wins on conflicts)
  data/wide/*.json             wide category audits
  data/tier2-feeders/*.json    entry-level shows that fed Tier 2 shows
  data/feeders/*.json          shows that fed the gateway shows
  data/south_florida.json      South Florida map

Outputs: data/master_list.json, podcast-master.csv, podcast-master.html
"""
import csv
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
SOFLA = re.compile(r"miami|fort lauderdale|ft\.? lauderdale|boca|palm beach|wynwood|south florida|coral gables|coconut grove|hollywood, fl|aventura", re.I)
UNKNOWN = {"", "unverified", "unknown", "null", "none", "n/a", "remote/unknown"}
FIT_RANK = {"high": 0, "medium": 1, "low": 2}


def norm(name):
    n = re.sub(r"\(.*?\)", "", str(name or "")).lower()
    n = re.sub(r"\bpodcast\b|\bshow\b|\bwith\b.*$|^the\s+|[^a-z0-9 ]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def known(v):
    return v is not None and str(v).strip().lower() not in UNKNOWN


def first(*vals):
    return next((v for v in vals if known(v)), None)


def rec(**kw):
    r = {k: kw.get(k) for k in ("name", "hosts", "tier", "category", "audience", "location", "accepts_guests",
                                "booking", "url", "angle", "fit", "verified", "source")}
    r["feeds_into"] = [f for f in kw.get("feeds_into") or [] if known(f)]
    r["origins"] = [kw["origin"]]
    return r


def hosts_str(h):
    if isinstance(h, list):
        return ", ".join(x.get("name", "") if isinstance(x, dict) else str(x) for x in h)
    return h


def load_json(p):
    try:
        return json.loads(p.read_text())
    except (OSError, ValueError):
        return None


def curated():
    for p in sorted(DATA.glob("tier*.json")):
        for s in load_json(p) or []:
            b = s.get("booking_contact") or {}
            angles = s.get("fit_angles") or []
            yield rec(name=s.get("name"), hosts=hosts_str(s.get("hosts")), tier=s.get("tier"), category=s.get("genre"),
                      audience=s.get("audience_size"), location=None, accepts_guests=None,
                      booking=b.get("route"), url=first(s.get("spotify_url"), s.get("website_url")),
                      angle=angles[0].get("hook") if angles else None, fit=None, verified=True,
                      source=b.get("source_url"), origin="curated list")


def wide():
    for p in sorted((DATA / "wide").glob("*.json")):
        for s in load_json(p) or []:
            yield rec(name=s.get("name"), hosts=hosts_str(s.get("hosts")), tier=s.get("tier"), category=s.get("category"),
                      audience=s.get("audience_indicator"), location=s.get("records_location"),
                      accepts_guests=s.get("accepts_guests"), booking=s.get("booking_route"), url=s.get("url"),
                      angle=s.get("avery_angle"), fit=s.get("fit"), verified=s.get("verified"),
                      source=s.get("source_url"), feeds_into=[s.get("feeds_into")], origin=f"wide audit: {p.stem}")


def tier2_feeders():
    for p in sorted((DATA / "tier2-feeders").glob("*.json")):
        for t in load_json(p) or []:
            for f in t.get("entry_feeders", []):
                angles = f.get("angles") or []
                yield rec(name=f.get("show"), hosts=f.get("hosts"), tier=1, category=f.get("genre"),
                          audience=f.get("audience"), location=f.get("records_location"),
                          accepts_guests=f.get("accepts_guest_applications"), booking=f.get("booking_route"),
                          url=first(f.get("spotify_url"), f.get("website_url")),
                          angle=angles[0].get("hook") if angles else None, fit=f.get("avery_fit"), verified=True,
                          source=f.get("booking_source"), feeds_into=[t.get("target")], origin="tier 2 feeder research")


def gateway_feeders():
    for p in sorted((DATA / "feeders").glob("*.json")):
        t = load_json(p) or {}
        for f in t.get("top_feeders", []):
            angles = f.get("angles") or []
            yield rec(name=f.get("show"), hosts=f.get("hosts"), tier=2, category=f.get("genre"),
                      audience=f.get("audience"), location=None, accepts_guests=None, booking=f.get("booking_route"),
                      url=first(f.get("spotify_url"), f.get("website_url")),
                      angle=angles[0].get("hook") if angles else None, fit=f.get("avery_fit"), verified=True,
                      source=f.get("booking_source"), feeds_into=[t.get("target")], origin="gateway feeder research")


SOFLA_TIER = {"cardone zone": 2, "i am athlete": 2, "pomp": 2, "caresha please": 2, "ogs": 2}


def south_florida():
    sf = load_json(DATA / "south_florida.json") or {}
    for s in sf.get("shows", []):
        angles = s.get("angles") or []
        tier = next((v for k, v in SOFLA_TIER.items() if k in norm(s.get("name"))), 1)
        r = rec(name=s.get("name"), hosts=s.get("hosts"), tier=tier, category=s.get("genre"), audience=s.get("audience"),
                location=s.get("city") or "South Florida", accepts_guests=s.get("accepts_guest_applications"),
                booking=s.get("booking_route"), url=first(s.get("website_url"), s.get("spotify_url"), s.get("youtube_url")),
                angle=angles[0].get("hook") if angles else None, fit=s.get("avery_fit"), verified=True,
                source=s.get("booking_source"), feeds_into=[e.get("went_to") for e in s.get("track_evidence", [])],
                origin="South Florida map")
        r["south_florida"] = True
        yield r


GROUPS = [
    ("Art, design & fashion", r"\bart\b|\barts\b|art-|\bartist|design|fashion|street.art|creative|galler|museum|\bcollect(ing|or|ors)?\b(?! car)|nft|digital.art"),
    ("Luxury & high net worth", r"luxury|hnw|high.net|\bwatch|yacht|\bcars?\b|automotive|lifestyle"),
    ("Wealth, investing & real estate", r"financ|invest|wealth|real.estate|money|crypto|web3|bitcoin|alt-asset|alternative"),
    ("Latin & regional business", r"latin|hispanic|regional"),
    ("Philanthropy & community", r"philanthrop|nonprofit|giving|chamber|civic"),
    ("Business & founders", r"business|founder|entrepreneur|startup|\bvc\b|venture|marketing|sales|operator|\bceo|small"),
    ("Culture, hip-hop & celebrity", r"hip.?hop|music|celebrity|entertainment|culture|comedy|longform|long-form|conversation|athlete|sport"),
    ("Ideas, politics & true stories", r"idea|interview|politic|news|crime|insider|scam|tech|\bai\b|science|self.improve|personal development|psychology|wellness|health"),
]


def group(m):
    """One consistent category group per show, from its category, else its angle and name."""
    for text in (str(m.get("category") or ""), f"{m.get('angle') or ''} {m['name']}"):
        for name, rx in GROUPS:
            if re.search(rx, text.lower()):
                return name
    return "Other"


# The same show under names the prefix rule can't catch.
ALIASES = {
    "andrewschulzsflagrant": "flagrant",
    "tombilyeusimpacttheory": "impacttheory",
    "matthewcoxinsidetruecrime": "insidetruecrime",
}


def merge(records):
    out = {}
    for r in records:
        if not known(r.get("name")):
            continue
        k = norm(r["name"]).replace(" ", "")
        k = ALIASES.get(k, k)
        # Same show listed under a longer or shorter title ("The Angels' Wing" / "The Angels' Wing NFT Art Podcast").
        k = next((ok for ok in out if len(min(ok, k, key=len)) >= 10 and (ok.startswith(k) or k.startswith(ok))), k)
        if k not in out:
            out[k] = r
            continue
        m = out[k]
        for field in r:
            if field in ("feeds_into", "origins"):
                m[field] = list(dict.fromkeys(m[field] + r[field]))
            elif field == "south_florida":
                m[field] = m.get(field) or r[field]
            elif field == "verified":
                m[field] = bool(m.get(field)) or bool(r.get(field))
            elif not known(m.get(field)) and known(r.get(field)):
                m[field] = r[field]
    for m in out.values():
        m["south_florida"] = bool(m.get("south_florida")) or bool(SOFLA.search(str(m.get("location") or "")))
        try:
            m["tier"] = int(m["tier"])
        except (TypeError, ValueError):
            m["tier"] = 1
        m["fit"] = str(m["fit"]).lower() if known(m.get("fit")) else None
        m["feeds_into"] = list({norm(f).replace(" ", "")[:20]: f for f in m["feeds_into"]}.values())
        m["group"] = group(m)
    return sorted(out.values(), key=lambda m: (m["tier"], not m["south_florida"], FIT_RANK.get(m["fit"], 3), m["name"].lower()))


METRICS = ("listeners_per_episode", "monthly_listeners", "youtube_subscribers", "instagram_followers", "other_followers", "apple_ratings")


def apply_size(rows):
    """Merge audience metrics and recording locations from data/size/*.json (keyed by exact show name)."""
    found = {}
    for p in sorted((DATA / "size").glob("*.json")):  # later files only fill gaps or add a search result
        for name, fields in (load_json(p) or {}).items():
            merged = found.setdefault(name, {})
            for f, v in fields.items():
                if known(v) and (not known(merged.get(f)) or f in ("searched", "location", "location_basis") and fields.get("location_basis") == "search"):
                    merged[f] = v
    by_key = {ALIASES.get(norm(k).replace(" ", ""), norm(k).replace(" ", "")): v for k, v in found.items()}
    for m in rows:
        k = norm(m["name"]).replace(" ", "")
        s = dict(found.get(m["name"]) or by_key.get(ALIASES.get(k, k)) or {})
        s["monthly_listeners"] = s.get("monthly_listeners") or s.get("monthly_listeners_est")
        m["size_checked"] = bool(s.get("searched"))
        for f, mf in (("hosts", "hosts"), ("url", "url"), ("booking_route", "booking")):
            if not known(m.get(mf)) and known(s.get(f)):
                m[mf] = s[f]
        for f in METRICS + ("metrics_source", "metrics_as_of"):
            m[f] = s.get(f) if known(s.get(f)) else None
        loc = m.get("location")
        messy = not known(loc) or "unverified" in str(loc).lower() or "unknown" in str(loc).lower()
        if known(s.get("location")) and (messy or s.get("location_basis") == "search"):
            m["location"], m["location_basis"] = s["location"], s.get("location_basis")
        else:
            m["location_basis"] = "research" if known(loc) and not messy else None
            if messy:
                m["location"] = None
        m["south_florida"] = m["south_florida"] or bool(SOFLA.search(str(m.get("location") or "")))
    return rows


def size_summary(m):
    """One-line audience size, e.g. '~2.4K/ep · YT ~120K · IG ~45K'."""
    parts = [f"Per episode {m['listeners_per_episode']}" if m.get("listeners_per_episode") else None,
             f"Monthly {m['monthly_listeners']}" if m.get("monthly_listeners") else None,
             f"YT {m['youtube_subscribers']}" if m.get("youtube_subscribers") else None,
             f"IG {m['instagram_followers']}" if m.get("instagram_followers") else None,
             m.get("other_followers"),
             f"Apple {m['apple_ratings']}" if m.get("apple_ratings") else None]
    if not any(parts) and m.get("tier") == 3 and known(m.get("audience")):
        return str(m["audience"])
    return " · ".join(str(x) for x in parts if x)


COLS = ["Tier", "Podcast", "Host(s)", "Category group", "Category", "South Florida", "Location", "Location basis",
        "Listeners per episode", "Monthly listeners / downloads", "YouTube subscribers", "Instagram followers", "Other followers", "Apple ratings",
        "Metrics source", "Audience notes", "Accepts guests",
        "Booking route", "URL", "Feeds into", "Avery angle", "Fit", "Verified this session", "Found via",
        "Status", "Date pitched", "Result"]


def write_csv(rows):
    with open(HERE / "podcast-master.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        for m in rows:
            w.writerow([m["tier"], m["name"], m.get("hosts"), m["group"], m.get("category"), "yes" if m["south_florida"] else "",
                        m.get("location") or "", m.get("location_basis") or "",
                        *[m.get(f) or "" for f in METRICS], m.get("metrics_source") or "", m.get("audience"), m.get("accepts_guests"),
                        m.get("booking"), m.get("url"), "; ".join(m["feeds_into"]), m.get("angle"), m.get("fit"),
                        "yes" if m.get("verified") else "no", "; ".join(m["origins"]), "Not contacted", "", ""])


def e(x):
    return html.escape(str(x)) if known(x) else ""


def write_html(rows):
    def row(m):
        url = f'<a href="{e(m["url"])}" target="_blank" rel="noopener">link</a>' if str(m.get("url") or "").startswith("http") else ""
        booking = e(m.get("booking"))
        if str(m.get("booking") or "").startswith("http"):
            booking = f'<a href="{e(m["booking"])}" target="_blank" rel="noopener">{booking}</a>'
        sf = '<span class="sf">SoFla</span>' if m["south_florida"] else ""
        fit = f'<span class="fit fit-{e(m["fit"])}">{e(m["fit"])}</span>' if m.get("fit") else ""
        feeds = "".join(f'<span class="feed">→ {e(x)}</span>' for x in m["feeds_into"])
        search = " ".join(str(m.get(k) or "") for k in ("name", "hosts", "category", "angle", "location")).lower()
        return (f'<tr data-tier="{m["tier"]}" data-sf="{int(m["south_florida"])}" data-search="{e(search)}">'
                f'<td class="n">{m["tier"]}</td><td><b>{e(m["name"])}</b> {sf}<br><small>{e(m.get("hosts"))}</small></td>'
                f'<td><small>{e(m["group"])}</small></td><td><small>{e(size_summary(m))}</small></td><td><small>{e(m.get("location"))}</small></td><td>{fit}</td><td><small>{e(m.get("angle"))}</small>{feeds}</td>'
                f'<td><small>{booking}</small> {url}</td></tr>')
    counts = {t: sum(1 for m in rows if m["tier"] == t) for t in (1, 2, 3)}
    sf = sum(1 for m in rows if m["south_florida"])
    page = (TEMPLATE.replace("{{ROWS}}", "".join(row(m) for m in rows)).replace("{{TOTAL}}", str(len(rows)))
            .replace("{{C1}}", str(counts[1])).replace("{{C2}}", str(counts[2])).replace("{{C3}}", str(counts[3]))
            .replace("{{SF}}", str(sf)))
    (HERE / "podcast-master.html").write_text(page)


TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Podcast Master List</title><style>
:root{--bg:#0b0c10;--panel:#14161d;--text:#f1f1f3;--muted:#8a8e99;--line:#2a2d36;--blue:#4a6cf7;--blue-soft:#9aa9f5;--green:#3fb37f;--amber:#d9a441;--red:#e5484d;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px/1.5 Inter,system-ui,-apple-system,sans-serif}
.wrap{max-width:1200px;margin:0 auto;padding:0 16px 64px}a{color:var(--blue-soft)}
h1{font:400 clamp(36px,6vw,60px)/1 Anton,Impact,"Arial Narrow",sans-serif;text-transform:uppercase;margin:40px 0 8px}
.sub{color:var(--muted);margin:0 0 16px}
.bar{position:sticky;top:0;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);display:flex;gap:8px;flex-wrap:wrap;z-index:2}
.bar button{font:inherit;padding:6px 12px;border:1px solid var(--line);background:var(--panel);color:var(--text);cursor:pointer}
.bar button.on{background:var(--blue);border-color:var(--blue)}
.bar input{flex:1;min-width:180px;font:inherit;padding:7px 12px;border:1px solid var(--line);background:var(--panel);color:var(--text)}
.tablewrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;margin-top:8px}th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line)}
th{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);position:sticky;top:58px;background:var(--bg)}
td.n{font-weight:700;color:var(--blue-soft)}small{color:var(--muted)}
.sf{font:700 10px/1 ui-monospace,monospace;letter-spacing:.08em;background:var(--blue);color:#fff;padding:2px 6px;margin-left:4px}
.fit{font:700 10px/1 ui-monospace,monospace;text-transform:uppercase;padding:3px 6px;border:1px solid}
.fit-high{color:var(--green)}.fit-medium{color:var(--amber)}.fit-low{color:var(--red)}
.feed{display:inline-block;margin:4px 6px 0 0;font-size:11px;color:var(--blue-soft)}
tr.hidden{display:none}
</style></head><body><div class="wrap">
<h1>Podcast master list</h1>
<p class="sub">{{TOTAL}} shows · Tier 1: {{C1}} · Tier 2: {{C2}} · Tier 3: {{C3}} · South Florida: {{SF}}. Sorted by tier, then South Florida, then fit. Re-verify booking routes before pitching.</p>
<div class="bar"><button class="on" data-f="all">All</button><button data-f="1">Tier 1</button><button data-f="2">Tier 2</button><button data-f="3">Tier 3</button><button data-f="sf">South Florida</button><input type="search" placeholder="Search shows, hosts, categories, angles…" aria-label="Search"></div>
<div class="tablewrap"><table><thead><tr><th>Tier</th><th>Show</th><th>Category</th><th>Size</th><th>Location</th><th>Fit</th><th>Avery angle / feeds into</th><th>Booking</th></tr></thead><tbody>{{ROWS}}</tbody></table></div>
</div><script>
const b=[...document.querySelectorAll('.bar button')],q=document.querySelector('.bar input');let f='all';
function go(){const t=q.value.toLowerCase();document.querySelectorAll('tbody tr').forEach(r=>{const ok=(f==='all'||(f==='sf'?r.dataset.sf==='1':r.dataset.tier===f))&&r.dataset.search.includes(t);r.classList.toggle('hidden',!ok)})}
b.forEach(x=>x.onclick=()=>{b.forEach(y=>y.classList.remove('on'));x.classList.add('on');f=x.dataset.f;go()});q.oninput=go;
</script></body></html>"""


if __name__ == "__main__":
    rows = apply_size(merge([*curated(), *wide(), *tier2_feeders(), *gateway_feeders(), *south_florida()]))
    (DATA / "master_list.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False))
    write_csv(rows)
    write_html(rows)
    by = {t: sum(1 for m in rows if m["tier"] == t) for t in (1, 2, 3)}
    print(f"{len(rows)} shows · tiers {by} · South Florida {sum(m['south_florida'] for m in rows)}")
