# GemBreak Sound Design — Phase 3: Sourcing Plan

**Version:** 1.2 (matches `audit/sound-spec.md` v1.2)
**Status:** Phase 3 deliverable. Companions: `audit/library-structure.md`, `audit/licenses.csv`.
**Date:** 2026-09-06
**Rule of the document:** royalty-free does not mean free, and it does not always mean app-distributable. Any source whose coverage of a paid mobile app, or of embedding files in a distributed binary, is not clearly stated in licence text we could read is marked unclear and is not recommended.

### Change log

**1.2.** Client reviewed the 1.1 candidates and found them too authentic. The plan is rebuilt around game-style sources: game-asset marketplaces (Unity Asset Store, Fab, GameDev Market, Ovani, Epic Stock Media), the Sonniss #GameAudioGDC bundles, Kenney and OpenGameArt, with the earlier foley candidates demoted to accents and fallbacks. New Section 3 answers what a loot-box open and an item scroll sound like and lists gamified candidates for each of the six core moments. Licence table gains nine marketplace rows. Commission scope and costs revised.

**1.1.** First sourcing plan.

---

## 0. Method and caveats

- **Nothing was downloaded.** Every candidate is a link to a page plus the licence facts we could establish.
- **Network limits.** Every sound-library and marketplace domain was egress-blocked from this environment. Licence texts marked **Full** were read from mirrors we could reach: the Creative Commons legal code, Kenney's pack `LICENSE.txt`, the Sonniss bundle licence, the Pixabay and Mixkit licences, the OpenGameArt FAQ and OGA-BY text, the Zapsplat and Pro Sound Effects EULA PDFs, the Splice Terms of Use, the Sound Ideas EULA, and, for 1.2, the Unity Asset Store EULA (4 Dec 2024), the Fab EULA (1 Oct 2024), the GameDev Market Pro Licence, the Ovani Terms of Service, the Epic Stock Media EULA and the itch.io Terms. Everything marked **Snippet** rests on search-engine excerpts of the cited page. Prices are promotional and regional; confirm at checkout.
- **Sonniss bundle file names** come from the public index of the bundles, which lists three or four sample files per library. Each hit is a pointer to a whole library folder inside the free zip.
- **Freesound licences** are recorded as shown in the search snippet or page wording. Every Freesound row must be confirmed on the sound page at download time (Section 7).

---

## 1. Strategy

### 1.1 Priority order, as briefed, applied to game sources

1. **CC0 and free-for-commercial**: Kenney, the Sonniss #GameAudioGDC bundles (free, no attribution, proprietary licence), OpenGameArt CC0/OGA-BY, BigSoundBank, Freesound filtered to CC0.
2. **Flat-fee game packs**: Unity Asset Store (non-Restricted assets), Fab, GameDev Market, Epic Stock Media, Ovani, BOOM Library MAGIC UI, A Sound Effect indie libraries. All licences read in full or at strong snippet level; all name games or apps.
3. **Subscription**: Zapsplat Premium only.
4. **Commissioned custom** for the coherent tier-stinger family, the case-open composite and the sapphire accents.

### 1.2 What changed from 1.1

- **Designed-first.** The spec's primary layer is now designed game audio. The best sources are game packs and the free GDC bundles, not foley libraries. Steel, sapphire and cloth become short recorded accents inside those sounds.
- **The free tier is stronger than expected.** The Sonniss bundles alone contain designed loot latches, charge-ups, impacts, shatter bursts, risers, Shepard-tone drones, UI selects and scroll ticks from CB Sounddesign, Epic Stock Media, Eiravaein, 344 Audio, Bluezone, Gamemaster Audio and others, all under one royalty-free licence. Kenney's Interface Sounds and Casino Audio cover ticks and prototyping.
- **Finished loot-box composites are cheap.** AD Sounds' Rewards & Loots ($9.99) and Cyberwave's Fantasy Loot Chest ($17.99–31.90) ship complete opens with layers split, under the Unity or Fab licence.
- **Two things still cannot be bought.** A coherent four-tier stinger family in GemBreak's key with a reserved tier 4, and the reveal composite with the watch's own crystal inside it. Both are commissioned, and the commission is smaller than in 1.1.
- **The accent session shrinks** to half a day: clasp, latch, tissue and a handful of crystal strikes. It can be done by the designer with a portable rig.

### 1.3 Sourcing tiers per layer

| Layer | Primary | Fallback | Prototyping placeholder |
|---|---|---|---|
| Designed (primary) | Sonniss GDC libraries; BOOM MAGIC UI; AD Sounds Rewards & Loots; Ovani UI & Menus; Vadi Casual Game Achievements | Unity/Fab loot and UI packs; Epic Stock Media; WOW Sound (Rare tier) | Kenney Interface Sounds, Casino Audio, Impact Sounds |
| Stinger family and reveal composite | Commission | Advanced Loot, Epic Reward (prices unverified) | AD Sounds Rewards & Loots |
| Steel, cloth accents | Half-day accent session | Freesound CC0 (Breviceps clicks, DesignDean ratchet), Eiravaein Latchlocker | Kenney RPG Audio metalLatch |
| Sapphire accents | Same session (five crystal strikes) | Hzandbits Bells & Bowls | Kenney Interface glass_00x |

---

## 2. Licence reference: every source checked

| Source | Exact licence | Attribution | Paid mobile app | Embed in app binary | Cost | Evidence | Verdict |
|---|---|---|---|---|---|---|---|
| [Kenney.nl](https://kenney.nl/assets/category:Audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Full (LICENSE.txt mirror) | **Use** |
| [Sonniss #GameAudioGDC bundle](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Full (2016 text) / Snippet (2026) | **Use; archive the licence at download** |
| [Freesound (CC0 filter)](https://freesound.org/search/?f=license:%22Creative+Commons+0%22) | CC0 1.0 Universal | No | Yes | Yes | Free | Full (CC0 text); per-sound label to confirm on page | **Use; confirm licence on the sound page** |
| [OpenGameArt (CC0 / OGA-BY)](https://opengameart.org/art-search-advanced) | CC0 1.0 or OGA-BY 3.0 | CC0 no; OGA-BY yes | Yes | Yes | Free | Full (FAQ and OGA-BY mirrors) | **Use; filter out BY-SA and GPL** |
| [BigSoundBank](https://bigsoundbank.com/licenses.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | Snippet | **Use; confirm per file** |
| [Freesound (CC BY 4.0)](https://freesound.org/) | CC BY 4.0 | Yes: creator, title, URL, licence, changes | Yes | Yes, with the technological-measures caveat | Free | Full (CC BY text) | **Use sparingly** |
| [Unity Asset Store](https://unity.com/legal/as-terms) | Asset Store Terms of Service and EULA, Appendix 1 (4 Dec 2024) | No | Yes for non-Restricted assets (§2.2.1; no engine limitation) | Yes ("incorporated and embedded") | $5–50 per pack | Full (mirror) | **Use; avoid packs labelled Restricted** |
| [Fab (Epic Games)](https://www.fab.com/eula) | Fab End User License Agreement (1 Oct 2024), Standard License | No | Yes, any engine | Yes; you must restrict end users from extracting the content | $10–190 per pack | Full (mirror) | **Use; add a no-extraction clause to the app EULA** |
| [GameDev Market](https://www.gamedevmarket.net/about/licences) | GDM Pro Licence (LICENCE (A), post 15 Jan 2019) | No | Likely ("Monetized Media Products" incl. in-app purchase; "Media Product" definition not captured) | Yes; must prevent extraction | $5–20 per pack | Full (mirror) | **Use; confirm team seats** |
| [Epic Stock Media](https://epicstockmedia.com/licensing-agreement/) | Epic Stock Media End User License Agreement (2020 text) | No | Yes ("mobile apps, video games") | Yes; not standalone or in a library | ~$49 per pack | Full (mirror) | **Use; one seat per user** |
| [Ovani Sound](https://ovanisound.com/policies/terms-of-service) | Ovani Terms of Service §2.1 royalty-free licence | No (appreciated) | Likely ("interactive media, games... and the like"; soundboards prohibited) | Yes | UI & Menus $20; others unverified | Full (mirror) | **Use; confirm non-game app scope in writing** |
| [BOOM Library](https://www.boomlibrary.com/end-user-license-agreement/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Snippet (EULA mirrors) | **Use; one seat per active user** |
| [A Sound Effect (indie libraries)](https://www.asoundeffect.com/license-agreement/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Snippet | **Use; check each vendor's EULA and seats** |
| [Zapsplat Premium](https://zapsplat-assets.s3.amazonaws.com/ZapSplat-EULA-Standard-License.pdf) | ZapSplat EULA (29 Sep 2025) | Premium: No | Yes (§4 "Games, apps, and software") | Yes | ~US$15/mo or Gold ~£30/yr | Full (EULA PDF) | **Use; single-user seat** |
| [Sound Ideas](https://sound-ideas.com/pages/sound-ideas-end-user-license-agreement) | Sound Ideas End User License Agreement | No | Yes ("synchronized content for Apps", games) | Yes | Per product | Full (mirror) | **Use if needed** |
| [Envato Elements / AudioJungle](https://audiojungle.net/licenses/terms/audio_sfx_media_single) | SFX Single Use / Elements per-project registration | No | Yes | Yes | Elements $16.50/mo | Snippet | **Acceptable; register once per app** |
| [Gamemaster Audio](https://www.gamemasteraudio.com/product/pro-sound-collection/) | Own EULA (text unseen) | No (site) | Yes per site ("games, film, video, apps") | Unclear | Pro Sound Collection $47 | Snippet | **Buy via Unity or Fab so a read licence applies** |
| [WOW Sound](https://wowsound.com/terms-of-use.aspx) | WOW Sound Terms of Use (sync licence tiers) | No | Rare or Legendary tier only; Common is games-only | Yes | Game UI & Puzzle Pack $99 | Snippet | **Confirm first** |
| [itch.io sound packs](https://itch.io/game-assets/tag-sound-effects) | Per pack (CC0 / CC BY / CC BY-NC / custom) | Per pack | Per pack | Per pack | $0–20 | Full (itch ToS) | **Check each pack's licence field** |
| [Sound Ex Machina (direct)](https://soundexmachina.itch.io/ui-sounds-musical) | No licence text located | ? | Unclear | Unclear | UI Sounds: Musical $29 | None | **Buy via A Sound Effect if at all** |
| [Pixabay](https://pixabay.com/service/license-summary/) | Pixabay Content License (Apr 2023) | No | Yes | Yes if not Standalone | Free | Full (mirror) | **Fallback only; flag** |
| [Mixkit](https://mixkit.co/license/) | Mixkit Sound Effects Free License | No | Yes | Yes; never in a public repo | Free | Full (mirror) | **Fallback only; flag** |
| [Soundsnap](https://www.soundsnap.com/licence) | Soundsnap Sound Effects License | No | Stated yes; full text unread | Unclear | $149/6 mo; $199–269/yr | Snippet | **Not recommended until confirmed** |
| [Soundly Pro](https://getsoundly.com/soundly-eula/) | Soundly EULA (4 Nov 2024) | No | Games yes; apps unnamed | Likely | $14.99/mo | Snippet | **Not recommended until confirmed** |
| [Splice Sounds](https://splice.com/terms) | Splice Terms of Use §3.1 (22 Aug 2024) | No | Unclear | Unclear | $12.99–39.99/mo | Full (mirror) | **Not recommended** |
| [Pro Sound Effects (Individual EULA)](https://prosoundeffects.s3.amazonaws.com/Pro%20Sound%20Effects%20Individual%20End%20User%20License%20Agreement.pdf) | PSE Individual EULA (Oct 2024) | Credit if others credited | Unclear (synchronised use only) | Custom Application License only | CORE $1,499–11,999 | Full (EULA PDF) | **Not recommended without a Custom Application License** |
| [Epidemic Sound](https://www.epidemicsound.com/policy/business-subscription/) | Personal / Commercial / Business policies | No | No on self-serve; Enterprise only | No | $9.99–30/mo | Snippet | **Do not use** |
| [Artlist](https://artlist.io/help-center/privacy-terms/artlist-license/) | Artlist License (15 Feb 2026) §11 | No | No (Enterprise case) | No | $9.99–39.99/mo | Snippet (strong) | **Do not use** |
| [Uppbeat](https://uppbeat.io/user-agreement) | Uppbeat User Agreement | Free yes / paid no | Unclear | Unclear | Business $18.99/mo | Snippet | **Do not use** |
| [Motion Array](https://help.motionarray.com/hc/en-us/articles/9442171935005-How-Does-The-License-Work) | Standard / Business | No | No | No | n/a | Snippet | **Do not use** |
| [BBC Sound Effects (RemArc)](https://sound-effects.bbcrewind.co.uk/licensing) | RemArc Licence | Yes | No (non-commercial) | No | Free | Full (PDF) | **Do not use** |

**Reading the verdicts.** *Use*: licence text we read, or a strong snippet, names games or apps and permits distribution inside a product. *Confirm first*: favourable but the text was unread, apps are unnamed, or team seats are not addressed. *Fallback only; flag*: permitted but with a clause that is easy to breach in practice. *Do not use*: apps, software or games are excluded on the plans a small team would buy, or the licence is non-commercial.

**Marketplace specifics.**
- **Unity Asset Store.** The EULA licenses assets for "an electronic application or digital media" with no engine limitation; Unity Support confirms non-Restricted assets may be used "in other engines and software". Check each listing for the Restricted label. Seats are entity-wide for audio.
- **Fab.** One Standard License with Personal and Professional price tiers (the split is a revenue threshold, the rights are identical). Any engine. You must "restrict end users from extracting" the content, so the app EULA needs a no-extraction clause and the files ship inside the bundle, not as user-accessible downloads.
- **GameDev Market.** One Pro Licence covering monetised products including in-app purchase; must prevent extraction; granted to the purchaser, so confirm how a team shares it.
- **Epic Stock Media.** Names mobile apps; single user per licence; a Custom Application License is needed only where end users control playback (a soundboard), which GemBreak is not.
- **Ovani and Gamemaster Audio.** Ovani's terms name interactive media and games and prohibit soundboards; confirm a non-game app in writing. Gamemaster's EULA could not be read; buy its Pro Sound Collection through Unity or Fab so a read licence applies.
- **Soundboard exclusion.** Ovani, Epic Stock Media, Zapsplat, A Sound Effect, Fab and Unity all exclude products whose primary value is playing the sounds. GemBreak sells watches; the exclusion does not apply.

---

## 3. What it should sound like, and where to get it

### 3.1 Opening a loot box in a video game

Five beats, always in this order.

1. **Anticipation.** A riser or shimmer swell of one to three seconds, often over a low pulse, while the box shakes or glows. Blizzard's Overwatch designer put it as "all about building the anticipation".
2. **The break.** A whoosh into a designed impact: a crack or glass-like shatter, a sub thump underneath, an energy-release tail. Overwatch's box "bursts open and sends four disks into the sky".
3. **Item pops.** Short bright plucks or chimes as each item lands.
4. **The rarity stinger.** One stinger per tier, escalating in length and harmony, not just loudness. Hearthstone's team describes "a rhythmic and musical approach" with legendary stingers borrowing orchestral material; Apex's team says "each rarity tier of loot has a unique sound".
5. **The settle.** A warm pad or sparkle tail decays under the result.

BOOM Library's MAGIC UI design brief states the rule for the whole hierarchy: each sound "scales in proportion to the moment it marks". In the spec, beats 1–2 are `open_box_crack` and `open_box_open`, the break at the reveal is `open_case_open`, beat 4 is `open_payoff_t1…t4`, beat 5 is `open_settle`.

### 3.2 Scrolling through item options in a game or casino

- **The tick.** One short sample retriggered per item. Valve's CS:GO and CS2 event data fixes the reel tick at constant pitch and low volume; the felt slowdown comes entirely from timing. Character ranges from a wooden flapper (prize wheel) to a synthetic peg-clack (item roulette) to a card flick (card cyclers).
- **The rate curve.** Constant, then decelerating, then a hold. An open-source roulette plugin encodes a typical curve: twenty ticks at 50 ms, then ten ticks whose gaps grow toward half a second, then a 1.5 s hold before the result. Prize-wheel recordings are described the same way: "rapid ticking… gradually slows down before stopping, often ending with a celebratory sound or chime".
- **The layer under it.** A riser, a drone or a whir loop that rises as the ticks spread out.
- **The stop.** A thunk, a mechanical lock or a chime stab, then the reveal.
- **How slots differ.** A continuous reel whir, reels stopping one at a time with separate "chunk" sounds, a near-miss "teasing tonal rise", a moment of silence before a shift, and win jingles with coin roll-up counters. That is the casino register. The game-menu register is a dry single tick, a short mechanical stop and a rarity stinger. The spec's mode A uses the game-menu register: `open_cycle_pass` is the tick, `open_cycle_tension` is the riser, `open_select_lock` is the stop.

### 3.3 Gamified candidates for the six core moments

Sources with clear licences first. Sonniss entries give library, file and bundle year/part.

**1. A watch case being opened (the reveal)**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Unity / itch / Fab | AD Sounds: Rewards & Loots – Sound Effects, 229 WAV, Open_Chest folder with layers split | https://assetstore.unity.com/packages/audio/sound-fx/rewards-loots-sound-effects-217967 | Unity EULA / Fab / itch per store | $9.99 | Finished open-plus-reward; bright, casual |
| Unity / itch / Fab | Cyberwave Orchestra: Fantasy Loot Chest, Crate and Lootbox Sounds, 30 designed | https://assetstore.unity.com/packages/audio/sound-fx/fantasy-loot-chest-crate-and-lootbox-sounds-297065 | Unity EULA / Fab | $31.90 (itch $17.99) | Use the designed set |
| A Sound Effect / Sonniss | Advanced Loot, 312 files: Loot Containers, Loot Types, Rarity Stingers | https://www.asoundeffect.com/sound-library/advanced-loot/ | A Sound Effect EULA (vendor to confirm) | Unverified | Case opens and tiered stingers in one set |
| Sonniss GDC 2026/2 | Epic Stock Media Anime Game: Power Up Bright Positive Successful Light Saturation Crash Shimmer 05 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Closest single free file to "the break" |
| Sonniss GDC 2019/2 | Impact Soundworks Super FX: Misc_Glass_Crystal_Shatter | https://sonniss.com/gameaudiogdc | GDC licence | Free | Shatter layer |
| Freesound | NeoSpica: Loot box open.wav | https://freesound.org/people/NeoSpica/sounds/423518/ | CC0 per page wording; confirm | Free | Audition |

**2. A button being pressed when the box is chosen**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Sonniss GDC 2019/5 | Sound Ex Machina UI Sounds Futuristic: Select_heavy_complex_hi-tech_tone_01 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Heavy tonal select |
| Sonniss GDC 2018/3 | Game Audio Factory SFX11 ExoInterface: Action Confirm – Long 05 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Designed confirm with tail |
| Ovani | UI & Menus Sound FX Pack, 154 files | https://ovanisound.com/products/ui-menus-sound-fx-pack | Ovani ToS | $20 | Snappy presses with weight |
| Sound Ex Machina via A Sound Effect | UI Sounds: Musical, 300 sounds | https://soundexmachina.itch.io/ui-sounds-musical | Buy via A Sound Effect | $29 | Musical selects |
| Kenney | Interface Sounds: confirmation_001–004, select_001–008, glass_001–006 | https://kenney.nl/assets/interface-sounds | CC0 | Free | Prototype; layer confirmation + glass |

**3. A box being partially opened (the tease)**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Sonniss GDC 2018/3 | Gamemaster Audio Magic and Spell Sounds: casting_charge_matter_grow_04 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Magic charge-up |
| Sonniss GDC 2019/1 | 3maze Zwoosh: glow_med_C_002 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Glow build |
| Sonniss GDC 2023/2 | CB Sound Design Dreamcatcher: Harp_Glissando_10b, Enchanting_Bells_4 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Shimmer swell for the light leak |
| Sonniss GDC 2020/3 | Federico Soler Fernández Effective Trailer Risers: Riser 027 / 035 / 078 / 088, trimmed to 1–3 s | https://sonniss.com/gameaudiogdc | GDC licence | Free | Light-leak risers |
| Ovani | Simple Magic Sound FX Pack, 191 files | https://ovanisound.com/products/simple-magic-sound-fx-pack-vol-1 | Ovani ToS | Unverified | Charge and glow variants |
| Gamemaster via Unity | Magic and Spell Sounds full pack | https://www.gamemasteraudio.com/product/magic-and-spell-sounds/ | Unity EULA if bought there | From $24.99 | Full library |

**4. A box being fully opened (the release)**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Sonniss GDC 2019/1 | Airborne Sound Crisis Accents: Impact, Whoosh to Hit, Resonant Hit; Impact, Hit, Chime, Tinkle, Fast | https://sonniss.com/gameaudiogdc | GDC licence | Free | Whoosh-to-hit with chime tail |
| Sonniss GDC 2026/2 | Epic Stock Media Tower Defense Game: ICEBrk Skill Freeze Whoosh Break Impact Layered Movement Shatter 03 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Whoosh plus shatter burst |
| Sonniss GDC 2024/1 | Bluezone Modern Cinematic Impact: impact_022, impact_boom_003 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Clean designed impact |
| Sonniss GDC 2019/3 | PMSFX Forgotten Neons: Spawns_Portals_Teleports_1 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Portal-open energy |
| Kenney | Impact Sounds: impactGlass_heavy_000–004, impactBell_heavy_000–004 | https://kenney.nl/assets/impact-sounds | CC0 | Free | Sweeteners |

**5. Watches cycling through (the item scroll)**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Kenney | Interface Sounds: tick_001–004, switch_001–007, scroll_001; OpenGameArt mirror "51 UI sound effects" with 38 switches | https://kenney.nl/assets/interface-sounds | CC0 | Free | Tick material; retrigger with pitch spread |
| Freesound | door15studio: spin-tick.mp3, made to repeat per wheel element | https://freesound.org/s/244774/ | CC0 per page wording; confirm | Free | Re-render from MP3 |
| Sonniss GDC 2024/1 | BluezoneCorp Tiny Gears: small_mechanism_click_003, click_complex_011 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Mechanical micro-click |
| Sonniss GDC 2015/2 | Kpow Sounds UI Soundpacks: Scroll v09, Scroll Version04 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Designed scroll blips |
| Sonniss GDC 2021–23/1 | 344 Audio Nuts and Bolts: Ratchet Clicking, Spin Once To Slow, Spin Twice To Slow | https://sonniss.com/gameaudiogdc | GDC licence | Free | Real decelerating spins for reference and layers |
| Sonniss GDC 2020/3, 2020/12 | Effective Trailer Risers; Sound Spark Drone Shepard Tones: Two_Toned_Shepard_Tone_Pitch_Rising | https://sonniss.com/gameaudiogdc | GDC licence | Free | Under-layer for the slowdown |
| Zapsplat | Wheel of fortune style carnival wheel spin to stop 1 and 2; wooden wheel short/constant/medium/slow spins | https://www.zapsplat.com/music/wheel-of-fortune-style-carnival-wheel-spin-to-stop-1/ | Zapsplat EULA (Premium) | ~£30/yr | Complete decelerating spins with stop |
| Kenney | Casino Audio: cardSlide1–8, cardShove1–4, cardFan1–2 | https://kenney.nl/assets/casino-audio | CC0 | Free | Card-flick alternative (mode B) |
| Gravity Sound via GameDev Market / Fab | Casino Slot Machine SFX, 170 WAV | https://www.gamedevmarket.net/asset/casino-slot-machine-sfx | GDM Pro Licence / Fab | $9.99 | Only if product wants the casino register |
| Fusehive via Sonniss / GDM | Universal Slots SFX Library, 430 files: reel spins, reel stops, anticipation wind-ups | https://sonniss.com/product/universal-slots-sound-effects-library | Fusehive royalty-free | $299.99 | Full casino vocabulary; not recommended for GemBreak's register |

**6. Final watch being selected (the lock-in)**

| Source | Candidate | URL | Licence | Cost | Notes |
|---|---|---|---|---|---|
| Sonniss GDC 2017/3 | Eiravaein Sound Latchlocker: design, FutureLoot, score, plunder | https://sonniss.com/gameaudiogdc | GDC licence | Free | Designed loot latch; strongest match |
| Sonniss GDC 2026/2 | Epic Stock Media HD Lock and Mechanism Kit: Click Deep Mechanism Latch Button Nearfield Thunk 02 | https://sonniss.com/gameaudiogdc | GDC licence | Free | The thunk |
| Sonniss GDC 2019/2 | InspectorJ UI Mechanical: UI_Mechanical_Confirm_04_FX | https://sonniss.com/gameaudiogdc | GDC licence | Free | Processed mechanical clunk |
| Sonniss GDC 2018/3 | Game Audio Factory SFX05 Casual Games: sfx_unlock_level_02 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Unlock stinger |
| Sonniss GDC 2023/2 | Justsoundeffects Futuristic Interface: UIAlert Confirm Access Granted 02 | https://sonniss.com/gameaudiogdc | GDC licence | Free | Locked-in confirm |
| Kenney | RPG Audio: metalLatch, metalClick | https://kenney.nl/assets/rpg-audio | CC0 | Free | Prototype |

**Supporting: rarity stingers, risers, sparkle, sub, pads**

| Need | Candidates |
|---|---|
| Rarity stinger ladder | Advanced Loot (Rarity Stingers); Sound Boosters Epic Reward (226 files, 96k/24, A Sound Effect); Vadi Sound Casual Game Achievements (136 files, $14.90); AD Sounds Rewards & Loots; Kenney Music Jingles (CC0) |
| Risers 1–3 s | GDC 344 Audio Trailer Instruments Designed: Riser 9, Stinger 8; L.A. Sounds Transitions: Riser Reverb Synth Tone 01, Reverse Flutter Riser 01; SoundMorph Sinematic Risers |
| Sparkle and shimmer | Freesound smokinghotdog Magic Stars Retro Sparkle, opticaillusions Sparkly (CC0 per page); GDC Articulated Sounds Magic Elements vol.2 processed-glass shimmer; GDC Epic Stock Media Strange Game Ambient Loops 3 shimmer loop; GDC Sound Villain Fireworks Malta sparkle crackle |
| Sub drops | GDC 344 Audio Sub Drop 2; 344 Audio Epic Impacts Vol. 1; Freesound Stereo Surgeon Bass Drop Pitch Sweep (CC0 per page) |
| Pads | GDC CB Sound Design Dreamcatcher Synth_Pad_12, Dream_Drone_09; Systematic Sound Tonal Elements; Alexander Kopeikin Emotion and Magic; Freesound bassimat Warm Pad (CC0) |

### 3.4 Best packs to buy

| Pack | Covers | Price | Licence | Buy via |
|---|---|---|---|---|
| Sonniss #GameAudioGDC bundles | Most designed layers in the set | Free | Sonniss GDC licence | sonniss.com |
| AD Sounds Rewards & Loots | Case open composite, box open, lock, reward pops | $9.99 | Unity EULA | Unity Asset Store |
| BOOM Library MAGIC UI Designed (or Bundle) | Entire UI family with a built-in hover-to-loot hierarchy | $139 / $269 intro | BOOM single-user EULA | boomlibrary.com |
| Gamemaster Audio Pro Sound Collection | 8,076 sounds: casual, magic, UI, whooshes | $47 | Unity EULA if bought there | Unity Asset Store |
| Vadi Sound Casual Game Achievements | Tiered win cues as stinger fallbacks | $14.90 | A Sound Effect EULA | asoundeffect.com |
| Ovani UI & Menus | Premium select and press alternatives | $20 | Ovani ToS (confirm app scope) | ovanisound.com |
| Cyberwave Fantasy Loot Chest | Designed chest opens | $17.99–31.90 | Unity EULA / itch per pack | Unity or itch |
| Zapsplat Premium | Wheel spins for reference, fill sounds | ~£30/yr | Zapsplat EULA | zapsplat.com |

---

## 4. Full inventory: sourcing table for every sound in the spec

For each event ID: layer composition (spec v1.2), the plan, and the candidates in priority order. The first candidate is the primary and is the one recorded in `audit/licenses.csv`. "Accent session" is the half-day recording of clasp, latch, tissue and crystal strikes.

#### UI

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `ui_tap` | Designed click + steel accent | Design from a game UI pack; clasp-tick accent | BOOM Library: [MAGIC UI (Designed): click family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary pack for the whole UI family; audition the crystal/glass tonal layer first |
|  |  |  | Kenney.nl: [Interface Sounds: click_001–005](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 prototype and fallback |
|  |  |  | Ovani Sound: [UI & Menus Sound FX Pack (154 files)](https://ovanisound.com/products/ui-menus-sound-fx-pack) | Ovani Terms of Service §2.1 royalty-free licence | No (appreciated) | Likely ("interactive media, games... and the like"; soundboards prohibited) | Yes | UI & Menus $20; others unverified | $20 alternative pack |
| `ui_toggle_on` | Designed toggle + bright ping | Design from pack | BOOM Library: [MAGIC UI (Designed): toggle/switch family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: toggle_001–004, switch_001–007](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
| `ui_toggle_off` | Designed toggle, lower | Design from pack | BOOM Library: [MAGIC UI (Designed): toggle/switch family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: toggle_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
| `ui_tab` | Designed swish-tick | Design from pack | BOOM Library: [MAGIC UI (Designed): hover/select family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: scroll_001–005, tick_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Sonniss #GameAudioGDC bundle: [Kpow Sounds UI Soundpacks: Scroll v09 / Version04 (GDC 2015 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Designed scroll blips |
| `ui_sheet_open` | Designed whoosh-swell up | Design from pack | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation 2: UI Zooms (GDC 2024 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary designed zoom |
|  |  |  | OpenGameArt (CC0 / OGA-BY): [Swishes Sound Pack (13 WAV)](https://opengameart.org/content/swishes-sound-pack) | CC0 1.0 or OGA-BY 3.0 | CC0 no; OGA-BY yes | Yes | Yes | Free | CC0 fallback |
|  |  |  | Kenney.nl: [Foley Sounds: woosh1–8](https://kenney.nl/assets/foley-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 air layer |
| `ui_sheet_close` | Designed whoosh-swell down | Design from pack | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation 2: UI Zooms, reversed (GDC 2024 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | OpenGameArt (CC0 / OGA-BY): [Swishes Sound Pack, reversed](https://opengameart.org/content/swishes-sound-pack) | CC0 1.0 or OGA-BY 3.0 | CC0 no; OGA-BY yes | Yes | Yes | Free | CC0 fallback |
| `ui_back` | Designed click, lower | Design from pack | BOOM Library: [MAGIC UI (Designed): back/cancel family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: back_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Sonniss #GameAudioGDC bundle: [Kpow Sounds UI Soundpacks: Back Version4 (GDC 2015 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Designed alternative |
| `ui_error` | Designed soft denial + low thud | Design from pack | Sonniss #GameAudioGDC bundle: [David Dumais UI Menu: Access_Denied_High_DDM16 (GDC 2020 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary designed denial |
|  |  |  | Kenney.nl: [Interface Sounds: error_001, error_004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation UI & HUD: Negative_Notification_25 (GDC 2018 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Alternative |
| `ui_success` | Designed two-note chime + sparkle; sapphire accent | Design from pack; sapphire accent from the hero session | Sonniss #GameAudioGDC bundle: [Chris Logsdon Ambient Puzzle: Success 2a, Menu Confirm (GDC 2019 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_001–004, glass_001–006](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | A Sound Effect (indie libraries): [Vadi Sound: Casual Game Achievements (136 files, $14.90)](https://www.asoundeffect.com/sound-library/casual-game-achievements/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Tiered win cues |
| `ui_disabled` | Dull designed tick | Design from pack | Kenney.nl: [Interface Sounds: tick_004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Primary CC0 |
|  |  |  | BOOM Library: [MAGIC UI (Designed): disabled/locked](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Alternative |

#### Commerce

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `com_add_to_cart` | Designed confirm blip + clasp accent | Design from pack | BOOM Library: [MAGIC UI (Designed): confirm family](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_001](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Ovani Sound: [UI & Menus Sound FX Pack](https://ovanisound.com/products/ui-menus-sound-fx-pack) | Ovani Terms of Service §2.1 royalty-free licence | No (appreciated) | Likely ("interactive media, games... and the like"; soundboards prohibited) | Yes | UI & Menus $20; others unverified | Alternative |
| `com_purchase_confirmed` | Designed two-note confirm with shimmer; sapphire accent | Commission (part of the hero set) | Commission (sound designer, work for hire): Two-note confirmation in the stinger family, paired AHAP | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; the hero confirmation |
|  |  |  | Sonniss #GameAudioGDC bundle: [G4F SFX11 ExoInterface: Action Confirm – Long 05 (GDC 2018 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Designed fallback |
|  |  |  | A Sound Effect (indie libraries): [Vadi Sound: Casual Game Achievements](https://www.asoundeffect.com/sound-library/casual-game-achievements/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Fallback |
| `com_payment_failed` | Heavier designed denial + thud | Design from pack | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation UI & HUD: Negative_Notification_25 (GDC 2018 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [Transverse Audio Digital UI: Cancel Action_3 (GDC 2020 pt 14)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Alternative |
|  |  |  | Kenney.nl: [Interface Sounds: error_004; Digital Audio: lowDown](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |

#### Open sequence

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `open_box_select` | Premium game select: designed press + tonal body + whoosh-swell; clasp accent | Design from pack; clasp accent | Sonniss #GameAudioGDC bundle: [Sound Ex Machina UI Sounds Futuristic: Select_heavy_complex_hi-tech_tone_01 (GDC 2019 pt 5)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary heavy select |
|  |  |  | Sonniss #GameAudioGDC bundle: [G4F SFX11 ExoInterface: Action Confirm – Long 05 (GDC 2018 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Alternative |
|  |  |  | Ovani Sound: [UI & Menus Sound FX Pack (154 files, $20)](https://ovanisound.com/products/ui-menus-sound-fx-pack) | Ovani Terms of Service §2.1 royalty-free licence | No (appreciated) | Likely ("interactive media, games... and the like"; soundboards prohibited) | Yes | UI & Menus $20; others unverified | Pack alternative |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_00x layered with glass_00x](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 prototype |
| `open_box_enter` | Soft designed impact + low body; box set-down accent | Design from pack; record accent | Sonniss #GameAudioGDC bundle: [Bluezone Modern Cinematic Impact: impact_022 (soft take) (GDC 2024 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Kenney.nl: [Impact Sounds: impactSoft_heavy_000–004](https://kenney.nl/assets/impact-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Record in-house (accent session): Presentation box set down on leather (accent session) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Accent |
| `open_bed` | Warm game pad, root and fifth, 8 s loop | Design from pack | Sonniss #GameAudioGDC bundle: [CB Sound Design Dreamcatcher: Synth_Pad_12, Dream_Drone_09 (GDC 2023 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary; key-match to E |
|  |  |  | Freesound (CC0 filter): [bassimat: Warm Pad Essentials Drone by Mantice](https://freesound.org/people/bassimat/sounds/854842/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 fallback; confirm licence |
|  |  |  | Commission (sound designer, work for hire): Bowed-crystal pad if the stock pads do not sit in the key | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Fallback commission |
| `open_box_crack` | Charge-up: latch accent + light-leak riser + shimmer swell | Design from packs; latch accent | Sonniss #GameAudioGDC bundle: [Gamemaster Audio Magic and Spell Sounds: casting_charge_matter_grow_04 (GDC 2018 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary charge-up |
|  |  |  | Sonniss #GameAudioGDC bundle: [3maze Zwoosh: glow_med_C_002 (GDC 2019 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Glow layer |
|  |  |  | Sonniss #GameAudioGDC bundle: [CB Sound Design Dreamcatcher: Harp_Glissando_10b, Enchanting_Bells_4 (GDC 2023 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Shimmer swell |
|  |  |  | Ovani Sound: [Simple Magic Sound FX Pack (191 files)](https://ovanisound.com/products/simple-magic-sound-fx-pack-vol-1) | Ovani Terms of Service §2.1 royalty-free licence | No (appreciated) | Likely ("interactive media, games... and the like"; soundboards prohibited) | Yes | UI & Menus $20; others unverified | Pack alternative; price unverified |
| `open_tell_t2` | Added sapphire-style note in the glow | Commission (accent from the hero set) | Commission (sound designer, work for hire): B4 glass note from the sapphire accent set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: glass_003](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 placeholder |
| `open_tell_t3` | Major-seventh shimmer + sparkle | Commission (accent from the hero set) | Commission (sound designer, work for hire): D♯5 glass shimmer with designed sparkle | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [CB Sound Design Dreamcatcher: Enchanting_Bells_4 (GDC 2023 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Fallback |
| `open_box_open` | Energy release: whoosh + impact with sub + sparkle burst + lid-stop tick | Design from packs | Sonniss #GameAudioGDC bundle: [Airborne Sound Crisis Accents: Impact, Whoosh to Hit, Resonant Hit / Hit, Chime, Tinkle, Fast (GDC 2019 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary whoosh-to-hit |
|  |  |  | Sonniss #GameAudioGDC bundle: [Epic Stock Media Tower Defense Game: ICEBrk Whoosh Break Impact Layered Shatter 03 (GDC 2026 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Shatter burst layer |
|  |  |  | Unity Asset Store: [AD Sounds: Rewards & Loots – Sound Effects (229 WAV; Open_Chest folder) $9.99](https://assetstore.unity.com/packages/audio/sound-fx/rewards-loots-sound-effects-217967) | Asset Store Terms of Service and EULA, Appendix 1 (4 Dec 2024) | No | Yes for non-Restricted assets (§2.2.1; no engine limitation) | Yes ("incorporated and embedded") | $5–50 per pack | Finished composite alternative |
|  |  |  | Kenney.nl: [Impact Sounds: impactGlass_heavy, impactBell_heavy](https://kenney.nl/assets/impact-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 sweeteners |
| `open_cycle_pass` | Item-scroll tick: designed peg-clack + short ping | Design from packs (12 variants) | Kenney.nl: [Interface Sounds: tick_001–004, switch_001–007; OGA mirror 51 UI sound effects (38 switches)](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Primary CC0 tick material |
|  |  |  | Freesound (CC0 filter): [door15studio: spin-tick.mp3 (made to repeat per wheel element)](https://freesound.org/s/244774/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 per page wording; confirm; MP3 so re-render |
|  |  |  | Sonniss #GameAudioGDC bundle: [BluezoneCorp Tiny Gears: small_mechanism_click_003, click_complex_011 (GDC 2024 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Mechanical micro-click |
|  |  |  | Zapsplat Premium: [Wooden wheel of fortune spins (tick material) and carnival wheel spin-to-stop 1/2](https://www.zapsplat.com/music/wheel-of-fortune-style-carnival-wheel-spin-to-stop-1/) | ZapSplat EULA (29 Sep 2025) | Premium: No | Yes (§4 "Games, apps, and software") | Yes | ~US$15/mo or Gold ~£30/yr | Premium seat; complete spins for reference |
| `open_cycle_tension` | Tension riser under the slowdown | Design from packs | Sonniss #GameAudioGDC bundle: [Federico Soler Fernández Effective Trailer Risers: Riser 027/035/078/088, trimmed (GDC 2020 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [Sound Spark Drone Shepard Tones: Two_Toned_Shepard_Tone_Pitch_Rising (GDC 2020 pt 12)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Endless-rise alternative |
|  |  |  | Freesound (CC0 filter): [Joao_Janz: Roulette Wheel Spin Loop 1_1 (2.4 s synth loop)](https://freesound.org/people/Joao_Janz/sounds/482663/) | CC0 1.0 Universal | No | Yes | Yes | Free | Whir under-layer; confirm licence |
| `open_select_lock` | Lock-in: designed clunk + sub + tonal stab; clasp accent | Design from packs; clasp accent | Sonniss #GameAudioGDC bundle: [Eiravaein Sound Latchlocker: design, FutureLoot, score, plunder (GDC 2017 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary; a designed loot latch |
|  |  |  | Sonniss #GameAudioGDC bundle: [Epic Stock Media HD Lock and Mechanism Kit: Deep Mechanism Latch Button Nearfield Thunk 02 (GDC 2026 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | The thunk layer |
|  |  |  | Sonniss #GameAudioGDC bundle: [G4F SFX05 Casual Games: sfx_unlock_level_02 (GDC 2018 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Unlock stab |
|  |  |  | Record in-house (accent session): Deployant clasp full lock (accent session) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Accent transient |
| `open_case_open` | The loot-box break: riser tail + impact + sparkle-shatter burst + whoosh; sapphire strike and latch accent | Commission the composite from pack layers plus accents | Commission (sound designer, work for hire): Composite built from the layers below with the sapphire strike inside it | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; the hero |
|  |  |  | Unity Asset Store: [AD Sounds: Rewards & Loots (Open_Chest layers) $9.99](https://assetstore.unity.com/packages/audio/sound-fx/rewards-loots-sound-effects-217967) | Asset Store Terms of Service and EULA, Appendix 1 (4 Dec 2024) | No | Yes for non-Restricted assets (§2.2.1; no engine limitation) | Yes ("incorporated and embedded") | $5–50 per pack | Finished-composite reference and layer source |
|  |  |  | Unity Asset Store: [Cyberwave Orchestra: Fantasy Loot Chest, Crate and Lootbox Sounds (30 designed) $31.90; itch $17.99](https://assetstore.unity.com/packages/audio/sound-fx/fantasy-loot-chest-crate-and-lootbox-sounds-297065) | Asset Store Terms of Service and EULA, Appendix 1 (4 Dec 2024) | No | Yes for non-Restricted assets (§2.2.1; no engine limitation) | Yes ("incorporated and embedded") | $5–50 per pack | Designed set |
|  |  |  | Sonniss #GameAudioGDC bundle: [Epic Stock Media Anime Game: Power Up Bright Positive Successful Crash Shimmer 05 (GDC 2026 pt 2); Impact Soundworks Super FX: Misc_Glass_Crystal_Shatter (GDC 2019 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Break and shatter layers |
|  |  |  | A Sound Effect (indie libraries): [Advanced Loot (312 files: Loot Containers, Loot Types, Rarity Stingers)](https://www.asoundeffect.com/sound-library/advanced-loot/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Price unverified; covers case open and stingers |
| `open_payoff_t1` | Common-drop chime + sparkle | Commission (stinger family) | Commission (sound designer, work for hire): Tier-1 stinger in the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | A Sound Effect (indie libraries): [Vadi Sound: Casual Game Achievements $14.90](https://www.asoundeffect.com/sound-library/casual-game-achievements/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Fallback |
|  |  |  | Kenney.nl: [Music Jingles: pizzicato/steel short jingles](https://kenney.nl/assets/music-jingles) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 placeholder |
| `open_payoff_t2` | Rare-drop two-note chime + pad swell | Commission (stinger family) | Commission (sound designer, work for hire): Tier-2 stinger in the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | A Sound Effect (indie libraries): [Sound Boosters: Epic Reward (226 files, 96k/24)](https://www.asoundeffect.com/sound-library/epic-reward/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Fallback; price unverified |
|  |  |  | Unity Asset Store: [AD Sounds: Rewards & Loots (reward folders)](https://assetstore.unity.com/packages/audio/sound-fx/rewards-loots-sound-effects-217967) | Asset Store Terms of Service and EULA, Appendix 1 (4 Dec 2024) | No | Yes for non-Restricted assets (§2.2.1; no engine limitation) | Yes ("incorporated and embedded") | $5–50 per pack | Fallback |
| `open_payoff_t3` | Epic-drop arpeggio stinger + sub + choir-like pad | Commission (stinger family) | Commission (sound designer, work for hire): Tier-3 stinger in the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | A Sound Effect (indie libraries): [Advanced Loot: Rarity Stingers](https://www.asoundeffect.com/sound-library/advanced-loot/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes | Tens of USD per pack | Fallback |
|  |  |  | Sonniss #GameAudioGDC bundle: [344 Audio Trailer Instruments Designed: Sub Drop 2 (GDC 2020 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Sub layer |
| `open_payoff_t4` | Legendary stinger: bass drop + low bell + ascending figure + long sparkle; reserved | Commission (stinger family) | Commission (sound designer, work for hire): Tier-4 stinger; exclusive to GemBreak | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; must never be a stock sound |
|  |  |  | Sonniss #GameAudioGDC bundle: [344 Audio Trailer Instruments Designed: Sub Drop 2; Articulated Sounds Magic Elements vol.2: Shimmer, Processed Glass (GDC 2020 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Layer material only |
| `open_bed_t4_post` | Wide post-bed, E major add 9; reserved | Commission | Commission (sound designer, work for hire): 12 s seamless pad; exclusive | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [Systematic Sound Tonal Elements High Tech Soul: DSGNDron pads (GDC 2023 pt 13)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Layer material |
| `open_settle` | Pad fade + sparkle drift + cloth accent | Design from packs | Sonniss #GameAudioGDC bundle: [Epic Stock Media Strange Game Ambient Loops 3: MAGShim Shimmer Loop Small Bell Metal Taps (GDC 2026 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary sparkle drift |
|  |  |  | Freesound (CC0 filter): [smokinghotdog: Magic Stars Retro Sparkle](https://freesound.org/people/smokinghotdog/sounds/584244/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 fallback; confirm |
|  |  |  | Record in-house (accent session): Tissue settle (accent session) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Accent |

#### Vault

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `vault_added` | Designed lock body + glass note; clasp accent | Design from packs; clasp accent | Sonniss #GameAudioGDC bundle: [Epic Stock Media HD Lock and Mechanism Kit: Latch Thunk 02 (GDC 2026 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Kenney.nl: [RPG Audio: metalLatch + Interface glass_001](https://kenney.nl/assets/rpg-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
|  |  |  | Record in-house (accent session): Deployant clasp full close (accent session) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Accent |

#### Fulfilment

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `ship_requested` | Designed confirm + cloth accent | Design from packs | Sonniss #GameAudioGDC bundle: [G4F SFX05 Casual Games: sfx_combo_succeed_03 (GDC 2018 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Primary |
|  |  |  | Kenney.nl: [Casino Audio: cardTakeOutPackage1–2 (cloth layer)](https://kenney.nl/assets/casino-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 layer |

#### Notifications

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `notif_shipped` | Two-note chime from the stinger family | Commission (stinger family) | Commission (sound designer, work for hire): Notification master from the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | BigSoundBank: [Notification lasomarie 1–5](https://bigsoundbank.com/notification-lasomarie-1-s2059.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | CC0 fallback |
| `notif_delivered` | Three-note arrival chime | Commission (stinger family) | Commission (sound designer, work for hire): Notification master from the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [mpaol2023: 3-tone chime](https://freesound.org/people/mpaol2023/sounds/370179/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 fallback; confirm |

#### System

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `sys_notification` | Dyad chime + glint | Commission (stinger family) | Commission (sound designer, work for hire): Notification master from the family | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | CC0 fallback |
| `sys_refresh_threshold` | Designed tick | Design from packs | Kenney.nl: [Interface Sounds: tick_001](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Primary CC0 |
|  |  |  | BOOM Library: [MAGIC UI (Designed): tick](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Alternative |
| `sys_refresh_complete` | Brighter designed tick | Design from packs | Kenney.nl: [Interface Sounds: tick_002](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Primary CC0 |
|  |  |  | BOOM Library: [MAGIC UI (Designed): tick](https://www.boomlibrary.com/) | BOOM Library Single-User EULA; MULA for teams | No | Yes ("video games and mobile applications") | Yes | MAGIC UI Designed $139 / Bundle $269 (intro to 15 Sep 2026) | Alternative |
| `sys_loading_loop` | Watch movement ticking, processed to sit in the game register | Source CC0; the one authentic accent kept as an identity cue | Freesound (CC0 filter): [hannagreen: wristwatch-ticking-SE_mono (~19 s)](https://freesound.org/people/hannagreen/sounds/256212/) | CC0 1.0 Universal | No | Yes | Yes | Free | Primary if beat rate is 4 Hz; confirm licence |
|  |  |  | Sonniss #GameAudioGDC bundle: [PMSFX Mechanical Morphs: Rhythmical_Movement_Tick_LoopConstructionKit_21 (GDC 2020 pt 5)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects") | Yes, as part of the project; never as raw files | Free | Designed tick-loop alternative |
|  |  |  | Freesound (CC BY 4.0): [bySeb: Omega Seamaster ETA 2892 (exactly 4 Hz)](https://freesound.org/people/bySeb/sounds/326478/) | CC BY 4.0 | Yes: creator, title, URL, licence, changes | Yes | Yes, with the technological-measures caveat | Free | Attribution required |
| `sys_empty_state` | Soft designed hush | Design from packs | OpenGameArt (CC0 / OGA-BY): [Swishes Sound Pack, softest](https://opengameart.org/content/swishes-sound-pack) | CC0 1.0 or OGA-BY 3.0 | CC0 no; OGA-BY yes | Yes | Yes | Free | Primary CC0 |
|  |  |  | Kenney.nl: [Foley Sounds: woosh (softest)](https://kenney.nl/assets/foley-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Fallback |

---

## 5. What is commissioned instead of sourced

### 5.1 The commission

One sound designer on work-for-hire terms (worldwide, perpetual, all media including marketing and haptic derivatives), delivering:

| Deliverable | Files | Why it cannot be bought |
|---|---|---|
| Tier stinger family T1–T4 (T1 and T2 with round-robins), in E major, escalating by length and harmony | 6 | A coherent ladder in one key; tier 4 must be exclusive to GemBreak |
| Case-open reveal composite: pack layers plus the watch's own crystal strike and latch accent, 3 round-robins × 2 velocities | 6 | The hero; must not be a stock sound |
| Selection lock composite, 3 × 2 | 6 | Same |
| Purchase confirmed, three notification chimes, two tier tells | 6 | Built from the same family so the app sounds like one product |
| Both beds (8 s and 12 s seamless loops), if the stock pads do not sit in the key | 2 | Harmonic identity; tier-4 post-bed exclusive |
| Production of the remaining ~81 files from pack sources: layering, key-matching, accent placement, loudness to the ladder, exports | ~81 | Editing, not purchasing |
| Haptic patterns: AHAP and Android JSON for 14 composite events, QA on three device classes | 28 | Audio-haptic sync is part of the sound |

### 5.2 The accent session

Half a day. Two steel-bracelet watches with deployant clasps, the presentation box and watch case, tissue and velour, five tuned crystal glasses and a felt mallet. Captures the clasp half and full engage, the case latch, the lid crack, tissue lift and settle, and struck crystal at E4, E5, G♯5, B5 and E6. The designer can self-record with a portable rig; a treated room is optional.

### 5.3 Rights language for the brief

Work for hire; assignment of all rights in the commissioned masters; worldwide, perpetual, all media including in-app, marketing, store previews, video and haptic derivatives; no reuse of the stinger family or any tier-4 material in other projects; portfolio credit permitted. Expect this to add 25–50 % over a non-exclusive quote.

---

## 6. Cost

### 6.1 Recommended

| Line | Basis | Low | High |
|---|---|---|---|
| Game packs: BOOM MAGIC UI Designed, AD Sounds Rewards & Loots, Gamemaster Pro Sound Collection via Unity, Vadi Casual Game Achievements, Ovani UI & Menus, Cyberwave Fantasy Loot Chest, Zapsplat Premium | Prices above; Advanced Loot or Epic Reward if priced under $100 | 290 | 650 |
| Free sources: Sonniss GDC, Kenney, OpenGameArt, BigSoundBank, Freesound CC0 | Optional Kenney donation | 0 | 20 |
| Commission: hero set, ~26 files at 150–400 each | Per-asset benchmark for bespoke work with revisions | 3,900 | 10,400 |
| Commission: production of the remaining ~81 files, mix, master, exports | 5–8 designer days at 450–650 | 2,250 | 5,200 |
| Haptic authoring and device QA | 3–5 designer days | 1,500 | 5,000 |
| Accent session: designer self-records | 1 day rate plus crystal glasses | 500 | 800 |
| Accent session: treated room with engineer (optional) | Half day | 0 | 1,500 |
| Contingency 15 % | | 1,270 | 3,540 |
| **Total** | | **≈ 9,700** | **≈ 27,000** |

A realistic midpoint is **≈ $15,000**.

### 6.2 Lean

Packs only (~$250: Rewards & Loots, Casual Game Achievements, Ovani UI & Menus, Zapsplat) plus Sonniss GDC and Kenney; commission only the four tier stingers, the case-open composite and the lock (~10 hero files at 150–250: 1,500–2,500); four production days (1,800–2,600); two haptic days (900–1,300); designer self-records accents in half a day (250–350). **≈ $4,700–7,000.** The cost is a thinner variant set and stock beds.

### 6.3 Studio sonic identity

A sonic-branding studio delivering identity, full set and haptics: **≈ $35,000–80,000**, with published agency ranges from about €30,000 into six figures.

### 6.4 Not in these numbers

Second audio seats for BOOM or Epic Stock Media, ongoing subscriptions after delivery (none needed), localisation, a music score.

---

## 7. Flags: unclear or excluded for commercial app distribution

| Source | Problem | Action if it must be used |
|---|---|---|
| Unity Asset Store "Restricted Assets" | Own terms may forbid use outside Unity | Check the listing label; skip Restricted packs |
| Fab | Content must not be extractable by end users | Ship inside the app bundle only; add a no-extraction clause to the app EULA |
| GameDev Market, Ovani, A Sound Effect vendors, Rogue Waves, Eiravaein (direct) | No team-seat language captured | Confirm in writing how a second audio user is covered |
| Gamemaster Audio direct | EULA text unseen | Buy through Unity or Fab |
| WOW Sound | Common tier is games-only; sync-licence wording for apps unclear | Rare or Legendary tier and written confirmation |
| Sound Ex Machina direct | No licence text located | Buy through A Sound Effect if at all |
| itch.io | itch's terms grant no commercial licence; each pack sets its own | Read the pack's licence field; CC BY-NC excludes a paid app |
| Humble Bundle audio bundles | Humble grants nothing; vendor licence ships in the download | Keep the vendor licence file with the assets |
| Epidemic Sound Personal / Commercial | Video and podcast sync only; games routed to Enterprise | Enterprise agreement |
| Artlist self-serve | §11: apps, software and games are an Enterprise case | Enterprise agreement |
| Motion Array | Apps, software, games need a dedicated business licence | Business licence |
| Uppbeat | Apps, games, software never named | Written confirmation |
| Splice | "Video games" named, apps not; sublicensing sounds "in isolation" barred | Do not use for one-shots |
| Pro Sound Effects Individual EULA | Synchronised use only; interactive needs a Custom Application License | Custom Application License |
| Soundsnap, Soundly, Storyblocks | Favourable wording, unread or apps unnamed | Written confirmation |
| Pixabay, Mixkit | Never name apps; "standalone" and "with source files" clauses | Fallback only; private storage |
| Sonniss GDC v2.0 | Bars supplying sounds "as sound effects" in an SDK or similar | Never expose raw files to users; archive the licence at download |
| Freesound CC BY | Attribution workable; technological-measures clause predates app-store DRM | Prefer CC0; credit fully if used |
| Freesound CC BY-NC, Sampling+; BBC RemArc | Non-commercial | Never |

---

## 8. Process: from plan to licensed files

1. **At download**, for every third-party file: screenshot the page showing the licence, save the licence text as `LICENSE.txt` beside the file in `sourced/<source>/<id>/`, and complete the row in `licenses.csv` (status `confirmed`, licence as shown, date, downloader).
2. **Freesound**: use the CC0 filter; confirm the licence badge on each sound page before download.
3. **Sonniss**: keep the bundle's licence file with the bundle; record year and part per file.
4. **Marketplaces**: save the invoice and the EULA version in force at purchase; on Unity check for the Restricted label; on Fab note the no-extraction duty; one seat per active audio user where the licence is per user.
5. **Commission**: signed agreement with the rights language in 5.3 before work starts; deliverables include stems, masters, session files and the loudness report.
6. **Attribution screen**: an "Audio credits" entry in Settings → About listing any CC BY file, Kenney by courtesy, and "Sound effects: Sonniss #GameAudioGDC" by courtesy. Nothing else in the set requires credit.
7. **Legal review** of `licenses.csv` before the first TestFlight or Play internal build containing third-party audio.
8. **Validation**: `tools/validate_manifest.py` (see `audit/library-structure.md`) refuses to build if any shipped file lacks a `confirmed` licence row.
