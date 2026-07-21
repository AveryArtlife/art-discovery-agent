# GemBreak "BrainRot" Creator Strategy — viral meme-native promo

_Compiled 2026-07-20. A separate track from the graded influencer program: hire creators who make
**repeatedly-viral, hyper-stimulating "brainrot" content** and blend GemBreak's pack-opening into it.
Kept fully separate from the main lists (workbook tab **🧠 BrainRot**)._

---

## Why brainrot fits GemBreak better than almost any product

Brainrot content and mystery-pack psychology run on the **same dopamine loop** — fast reward, chaotic
stimulation, "just one more." A pack pull *is* already a brainrot beat (build-up → reveal → reaction).
The audience (Gen-Z/Gen-Alpha, impulsive, mobile-first) is exactly GemBreak's converter. This is the
highest-virality, lowest-production-cost creative lane available to the brand.

## What "brainrot" actually is (2026 style + structure)

- **Aesthetic:** loud, lo-fi, cursed, surreal, "low-effort high." Random imagery + bizarrely
  infectious audio. Fast cuts, zoom-punches, caption spam, AI voices, green-screen reactions.
- **Core mechanic:** one dumb, instantly-cloneable concept → remixed into an inescapable loop.
  Virality comes from **repetition + remix**, not polish. Minimal effort, maximum engagement.
- **Current formats (last ~90 days):** Italian brainrot / AI-creature memes, Skibidi/Ohio residue,
  "6-7" & slang chants, NPC bits, ragebait, "Steal a Brainrot" (Roblox) tie-ins, split-screen +
  subway-surfers/gameplay under a talking clip, sludge compilations, streamer-clip reposts.
- **Hook science:** the first 0.5–1.5s must be a pattern-interrupt (loud sound, on-screen text
  question, absurd visual). No slow intros. Payoff (the reveal/punchline) must land before ~7s.

## How brands blend promo without killing the virality

Winning brand examples (Netflix, Duolingo, Mazda SG) share one rule: **be native, not an ad.** The
brand is the *joke's vehicle*, not the interruption. For GemBreak:

- **The pull IS the payoff.** Structure: brainrot hook → escalating absurd build → **GemBreak pack
  reveal as the punchline/climax** → chaotic reaction → code on screen. The promo *is* the drop.
- **Don't script it corporate.** Give creators the mechanic + code + 2-3 "must-hits" (show the site,
  say the code, real reaction) and let them brainrot it their way. Creator-native > brand-scripted.
- **Ride a live format,** don't invent one. Map GemBreak onto whatever meme/audio is peaking that week
  (this is why we scrape every ~30 days — formats rot fast).
- **Volume + remix beats perfection.** Fund many cheap variations of a proven concept; amplify the
  ones that pop (feeds directly into the paid-amplification engine in CAMPAIGN_PLAYBOOK.md).

## Who to hire — 5 account archetypes (in priority order for GemBreak)

1. **Gambling/streamer CLIP accounts** — repost viral casino/Kick/Adin-style clips; already
   gambling-adjacent, brainrot-paced, micro following, cheap. **Best fit** (13 in our BrainRot tab
   are already gambling-adjacent, e.g. `@doomhq`, `@adin_clip`, `@kickclipsofficial_`, `@staketoast`).
2. **Meme / viral-culture pages** — daily meme posters with repeat virality (e.g. `@korinial`); huge
   reach-per-dollar, native to the format.
3. **Original brainrot creators** — make their own absurd bits (the highest-value but hardest to find
   at micro scale → the fresh Apify pull targets these).
4. **Card/pack "brainrot-break" creators** — unboxers who already film in a hyper, meme-y style (bridges
   our Pokémon/breaker list into brainrot).
5. **Edit / capcut-template accounts** — fast-cut editors whose templates go viral; can template-ize
   a GemBreak pull.

⚠️ **Quality caveat:** many clip/aggregator accounts are fan/repost pages (some impersonation). They
*do* repeatedly go viral and can make promo videos, but vet for (a) originality, (b) no impersonation
of a real streamer, (c) FTC-disclosure willingness before hiring.

## The BrainRot tab (starter list — needs view verification)

`brainrot_candidates.csv` / **🧠 BrainRot** tab = **68 accounts** mined from our existing scrapes that
carry brainrot signals at micro scale (TikTok 60, IG 6, YT 2): 45 clip/aggregator, 8 meme pages, 8
brainrot/viral, 5 comedy, 2 edits; **13 gambling-adjacent, 32 with a contact.** Every row is flagged
`needs_view_check = yes` — because "**repeatedly viral**" can only be confirmed with fresh per-video
view data, which needs the scrape below.

## Getting the *repeatedly-viral, last-90-days* accounts (fresh pull)

Follower count ≠ virality. To find micro accounts with **multiple recent high-view videos**, run these
(inputs committed in `scraper_inputs/`), then filter for **accounts whose median recent-video views ≫
their follower count** (the true "repeated viral micro" signal):

- **`brainrot_tiktok_input.json`** — 24 brainrot + clip + unboxing hashtags (TikTok has `playCount`
  per video → the key viral signal).
- **`brainrot_ig_input.json`** — 16 brainrot/meme Reels hashtags.
- **`brainrot_youtube_shorts_input.json`** — 12 Shorts searches (`viewCount` per short).
- **X/Twitter:** no reliable public scraper in our stack; use LunarCrush (already connected) to pull
  viral X meme/clip accounts by keyword when needed.

**Filter recipe after scraping (I'll run it):** keep authors where ≥2 videos in 90 days exceed, say,
5–10× their follower count in views, followers ≤500K, brainrot-format bio/tags, and not pure
impersonation. That yields the real "repeated viral micro" shortlist → merge into the BrainRot tab.

## Deal model for brainrot creators

- **Cheap + volume + performance.** These creators are low-cost; buy **many** at **$75–400/video**
  (nano/micro bands) or **pure affiliate** (promo code + signup bounty + pack %). Bonus on a **view
  threshold** (they're built to hit it — like the $1,250+$1k@1M-views anchor deal).
- **Batch briefs:** one mechanic + code, 5–15 creators make their own brainrot version same week →
  amplify the 2–3 that pop as Spark Ads.

## Next steps
1. Run the 3 brainrot scrapes → I filter for repeated-viral micro accounts and expand the tab.
2. I can draft **3 brainrot creative briefs** (hook → build → pack-reveal payoff → code) as a starting
   template for creators.
3. Fold winners into the affiliate/amplification flywheel (CAMPAIGN_PLAYBOOK.md).
