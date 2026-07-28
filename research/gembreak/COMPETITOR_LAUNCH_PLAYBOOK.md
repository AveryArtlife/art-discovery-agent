# Competitor Launch Playbook — How the mystery-box brands started their socials

_Compiled 2026-07-28. What IcyBox, Courtyard, Cases.gg, PackDraw (+ HypeDrop, RillaBox) actually did with
their FIRST social content and launch. Honest constraint: the literal "first 10 posts" per platform are
NOT retrievable from the open web (TikTok/IG/X/YouTube 403 automated access and show newest-first;
archive.org is blocked here). The Apify inputs (`competitor_firstposts_*`) pull each profile's full history
so we can sort oldest-first and get the exact first 10 — run those for the literal list. Below is what IS
knowable: launch dates, earliest-content DNA, and the launch strategy each used._

---

## The four archetypes (the useful pattern)
Every one of these launched with **one of two engines**, plus a shared content DNA:
- **A) Founder / creator front-man** — a personality posts the "day zero" announcement and lends
  credibility (PackDraw's DOOM13, IcyBox's Ted Park).
- **B) Audience inheritance** — launch off an existing community you already own (Cases.gg off Clash.gg;
  Courtyard off its 2021 NFT/Discord base).
- **Shared earliest-content DNA:** **big-pull reveal/reaction clips + giveaways + promo codes** — never
  polished ads. Plus a **trust line from post #1** (odds upfront / instant buyback / fulfillment proof).

---

## PackDraw — founder-led, giveaway + big-pull engine
- **Day zero:** founder **DOOM13** announced it from his **personal X (@DoomisGod), Aug 2, 2023** — a
  "year and a half in the making" reveal — *then* propagated to the brand handle. Dev implied since ~2022.
- **Earliest content DNA:** **X giveaways** (follow + RT + tag friends for $100–$250 cash/pack credit) +
  **big-pull hype clips** (screen-recorded openings landing high-value cards, e.g. a ~$550k sealed box
  pulled from a ~$600 pack). A separate **@PackDrawClaims** account posted fulfillment proof ("$3M+
  fulfilled") — trust as content.
- **Note:** the SteveWillDoIt deal was **mid-2025 (growth phase), NOT launch.** They started small and
  founder-authentic, not with a mega-creator.
- Now IG **~102K**; corporate = PackDraw Ltd (Cyprus) + PackDraw US LLC (Delaware).

## IcyBox — TikTok-first, rapper front-man, watch-pull reactions
- **Day zero:** built around **Ted Park (@tedparkboi)** — a Korean-American rapper running "marketing &
  partnerships @icyboxapp," promo code **ICYTED**. Launch post: *"If you told me 6 months ago I'd launch
  the first lootbox app for watches…"* (iOS conceived ~Oct 2025; X joined Jan 2026; Google Play Mar 2026).
- **Earliest content DNA:** **watch-pull reaction/reveal videos** ("I almost crashed out from this pull"),
  **themed limited boxes** as hooks (e.g. "The Independence Box," $250 → Rolex Meteorite / Omega / TAG),
  **free-watch giveaways tied to app downloads**, creator promo codes, and an **IRL Coachella activation**
  (handing out watches on camera).
- **Platform priority: TikTok (~148K) dwarfs everything;** X is an afterthought (~310). This is the
  closest analog to a modern, from-zero, TikTok-first launch.

## Cases.gg — audience inheritance (the shortcut)
- **Day zero:** site live **Aug 15, 2024**, run by **CGG Entertainment — the same operator as Clash.gg**,
  so it launched **off Clash.gg's existing CS2/skins community**, not from zero. This is the biggest
  single launch advantage of the four.
- **Content DNA:** high-cadence **promo-code drops** on X, **provably-fair / blockchain-verifiable** trust
  messaging, **luxury-prize aspiration** (Patek Nautilus, Lamborghini Urus), and **case-battle** clips.
- Handles (corrected): **X @casesdotgg (~23.4K) · IG @cases_dotgg (~5.3K)**, TikTok @cases.gg.

## Courtyard — the two-phase pivot (NFT base → consumer rip content)
- **Phase 1 (2021–2023):** launched as a crypto/NFT project — **Twitter + Discord**, presale/whitelist
  spots, "physically-backed NFT" narrative, PR partnerships (**Brink's, OpenSea, YC W2022, Chainlink**).
  Community-and-PR-led, not reveal-content-led.
- **Phase 2 (Mar 2024→):** re-launched for the mainstream with the **Vending Machine (TikTok post Mar 21,
  2024)** — *"rip Pokémon packs… $25 packs on-demand… instant buyback… odds upfront. Click, rip, repeat."*
  Pivoted to **pack-ripping demo content + creator seeding** (@100charizards etc.), code **TIKTOKPACK**,
  and **odds-upfront / instant-buyback** trust framing.
- **IG ~89K is its biggest channel; TikTok ~4.5K.** Raised **$37.5M**. Heavy press (Forbes, Polygon, PH).

## HypeDrop & RillaBox (secondary)
- **HypeDrop:** launched **Jan 8, 2019** in the sneaker/streetwear box niche (amid the Jake Paul/RiceGum
  "MysteryBrand" scandal era); shut V1 down Mar 2024, **relaunched V2** Aug/Sep 2024.
- **RillaBox (~2021):** **community-first** — a 50K+ Discord, daily challenges/races/badges, **referral-code
  virality** and **user unboxing UGC** as the growth loop, rather than streamer seeding. IG @rillaboxofficial.

---

## What GemBreak should copy for next week's launch
1. **Use BOTH engines you have** — a **founder "day zero" post** (Avery's story, like DOOM13/Ted Park) AND
   **audience inheritance** (the 414K YouTube channel + Atlas creator network). Most competitors had only one.
2. **First posts = big-pull reveal clips + a giveaway + promo codes**, not a polished ad. Seed 5–8 creators
   with codes on day one (your golf bench: Rick Shiels / Good Good / Bob Does Sports).
3. **Lead with trust from post #1** — "odds upfront, transparent buyback, fulfillment proof." This is your
   wedge (IcyBox's #1 complaint is opaque valuations; you show the number). Stand up a "GemBreak Claims"-style
   fulfillment-proof account like PackDraw did.
4. **TikTok-first** (IcyBox proved the from-zero TikTok path: 148K there vs 310 on X), + the clipping engine.
5. **A launch stunt** — IcyBox's Coachella-style IRL giveaway is a repeatable spike; do a golf-world version
   (a course/Topgolf activation or a grail giveaway).
6. **A giveaway mechanic** (follow + tag / free-pack-on-signup) to farm the first followers fast.

---

## Get the LITERAL first 10 (run these)
`scraper_inputs/competitor_firstposts_tiktok_input.json` (clockworks/tiktok-scraper, full history) +
`scraper_inputs/competitor_firstposts_ig_input.json` (apify/instagram-scraper, corrected handles). They pull
each profile's full post history; send me the JSON and I'll **sort oldest-first and hand back the exact first
10 posts per brand** with caption, date, format, and view/like counts. Verify TikTok handles in-app first
(icybox, cases.gg vary), and bump `resultsPerPage`/`resultsLimit` if a brand has >300 posts.
