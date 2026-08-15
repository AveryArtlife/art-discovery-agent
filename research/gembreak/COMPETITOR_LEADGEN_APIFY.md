# GemBreak — Competitor Ecosystem Lead-Gen with Apify

_How to build a large, extensive GemBreak lead list by harvesting the audiences and creator networks
of PackDraw, IcyBox, Cases.gg, Courtyard, HypeDrop, RillaBox, EmpireDrop, Jemlit, Clash.gg, MrLoot,
and the CS-skin/gambling sites. Compiled 2026-07-22._

---

## The core idea: stop scraping hashtags, start harvesting competitors

Hashtag scraping (what we've done) finds people *using a topic*. The far richer vein is the
competitors' **own ecosystems** — the creators and fans already engaged with a rival product are the
warmest possible GemBreak leads. Five sources, ranked by lead quality:

| # | Source | What it yields | Apify actor | Reliability |
|---|---|---|---|---|
| **1** | **Mentions/tags** of the brand | Creators who already **promote** competitors (affiliates) | `apify/instagram-mention-scraper` · X: `apidojo/tweet-scraper` | High |
| **2** | **Comments** on the brand's posts | Engaged fans + creators in the brand's audience | `apify/instagram-comment-scraper` · `clockworks/tiktok-comments-scraper` | High (2-step) |
| **3** | **Promo-code hashtags** (`#packdrawcode`) | Active **affiliates** (warmest of all) | IG/TikTok hashtag scraper | High |
| **4** | Who the brand **follows** | The brand's own **partnered creator roster** | `apify/instagram-following-scraper` | Medium (ToS-sensitive) |
| **5** | **Reposters / clip accounts** of brand content | Meme/clip accounts amplifying the brand | TikTok/YouTube search of brand name | High |

## The competitor set (handles)

- **Mystery-box:** PackDraw `@packdraw` · IcyBox `@icyboxapp` · Cases.gg `@cases.gg` ·
  Courtyard `@courtyard.io` · HypeDrop `@hypedrop` · RillaBox `@rillabox` · EmpireDrop `@empiredrop` ·
  Jemlit `@jemlit` · MrLoot `@mrloot` · Clash.gg `@clash.gg`
- **CS-skin cases:** CSGORoll · SkinClub · Gamdom · DatDrop · Hellcase · KeyDrop · DaddySkins · LuxDrop
- **Gambling-adjacent (bigger audiences):** Stake · Roobet · Rainbet

> ⚠️ A few handles need a 5-second verify in-app before running (Cases.gg's exact IG handle, some
> TikTok variants). Mention/comment scrapers return **empty on a wrong handle** — confirm first.

---

## The pipeline (how it all comes together)

```
HARVEST (5 sources × competitor set)
      │  raw creators + fans (tens of thousands)
      ▼
DEDUPE  →  FILTER to creators (drop pure-fan accounts: <1k followers & no content)
      ▼
GRADE   →  our stress-test + view-efficiency + brainrot scoring
      ▼
ENRICH  →  profile pass (followers/email) + Contact Details Scraper (bio-links)
      ▼
MERGE   →  into the graded master / focus list, tagged source = "competitor:PackDraw" etc.
```

The **`source` tag** matters: a creator pulled from "mentions of PackDraw" is a documented competitor
promoter — that's a killer personalization hook for Atlas ("saw you work with PackDraw…").

---

## Run order (highest ROI first) — 4 ready inputs committed in `scraper_inputs/`

### ① Competitor MENTIONS — IG  → `competitor_ig_mentions_input.json`
`apify/instagram-mention-scraper` · finds creators who **tag** the brands (documented promoters).
```json
{ "usernames": ["packdraw","icyboxapp","courtyard.io","cases.gg","hypedrop","rillabox","empiredrop","jemlit","mrloot","clash.gg", "...skins/gambling..."], "resultsLimit": 200 }
```

### ② Competitor PROMO-CODE hashtags — IG  → `competitor_promocode_ig_input.json`
The warmest leads — affiliates posting `#packdrawcode`, `#hypedropcode`, etc. `apify/instagram-scraper`.

### ③ Competitor PROFILES — TikTok  → `competitor_tiktok_profiles_input.json`
`clockworks/tiktok-scraper` with the brands as `profiles` → returns their videos. **Step 2:** take the
top video URLs and run `clockworks/tiktok-comments-scraper` to harvest **every commenter** (their
engaged audience + creators).

### ④ Competitor MENTIONS — X/Twitter  → `competitor_x_mentions_input.json`
`apidojo/tweet-scraper` · @-mentions + code tags. X is where a lot of gambling/case-opening promo
lives. Returns handles that tweet about the brands.

### Two-step plays (biggest volume)
- **Comment harvest (IG):** run a profile/post scrape of each brand → feed the post URLs into
  `apify/instagram-comment-scraper` → thousands of engaged commenters.
- **Following roster:** `apify/instagram-following-scraper` on `@packdraw` etc. → the accounts the
  brand follows are usually its **paid creators** (highest-value, but ToS-sensitive — run small).

---

## Volume & cost expectations
- Mentions + promo tags + comments across ~15 brands can realistically surface **10,000–50,000 raw
  accounts**. After dedupe + creator-filter, expect **a few thousand genuine creator leads** — a
  massive expansion of the current list.
- Budget: keep TikTok `resultsPerPage` and IG `resultsLimit` moderate (30–40) per brand; the
  Contact/enrichment passes are the pricier step, so enrich only the graded top slice.

## What I do after you run them
1. Dedupe against the existing 4,000+ and each other.
2. Filter out pure-fan accounts (no content / tiny) — keep creators.
3. Grade + score (fit, view-efficiency, brainrot) and tag `source = competitor:<brand>`.
4. Feed the graded top into the Focus list + contact-enrichment.

**Start with ① and ② (mentions + promo tags)** — highest lead quality, directly runnable, no 2-step.
Send the JSONs back and I'll process them into graded, source-tagged leads.
