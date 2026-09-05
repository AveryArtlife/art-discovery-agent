# GemBreak Sound Design — Phase 1: Competitor Audit

**Status:** Phase 1 deliverable. Feeds Phase 2 (sound spec) and Phase 3 (sourcing plan).
**Date:** 2026-09-05
**Scope:** How sound is used across mystery-pack platforms, the CS:GO case-opening lineage, mobile gacha/loot systems, and four restraint-and-polish references. Analysis of design patterns only.

---

## 0. Method and how to read this document

**What was done.** Text-only desk research across product help centres, release notes, app-store listings and reviews, developer interviews, WWDC session transcripts, Apple Human Interface Guidelines, academic papers, regulator publications, patents, community threads, video titles/descriptions/comments, and open-source case-opening simulators whose code names the sound events they imitate.

**What was not done.** No audio was downloaded, extracted, ripped, transcribed from audio, or reused from any product. No game files or sound banks were opened. Every description of a sound below is a description in words, from written sources or from stated inference.

**Network caveat.** This session's egress proxy blocked full-page fetches for most content domains, including YouTube, TikTok, Reddit, Fandom wikis, app stores, Trustpilot and the mystery-box sites themselves. Apple's developer documentation and GitHub source were fetchable in full. Everything else rests on search-engine snippets of the cited page. That is why the evidence grade matters.

**Evidence grades used throughout.**

| Grade | Meaning |
|---|---|
| **V** | Verified from a fetched primary source (full page read). |
| **V-s** | Verified at snippet level: the cited page's text was returned by a search engine, but the page itself could not be opened. Quoted wording is near-verbatim. |
| **I** | Inferred from genre lineage, indirect evidence (video titles, thread titles, code), or product familiarity. Not documented. |

**Durations.** No product in this audit publishes millisecond figures for its sounds. Where a duration is given it is either a stated approximation from a source (marked) or an inference from animation length. Phase 2 will set targets from first principles, not from these estimates.

---

## 1. Comparison table

Terse by design. Section 2 carries the detail and the sources.

| Product | Category | Owned sounds (what exists) | Where they fire | Duration profile | Tension → payoff | Rarity differentiation | Repetition handling | Casino tells | Grade |
|---|---|---|---|---|---|---|---|---|---|
| **Whatnot** | Live breaking | OS push tone (recognisable enough to be meme'd); in-stream UI near-silent; confetti on win (visual) | Auction win, go-live push, @mention | Confetti ~1.5–3 s (I) | Host voice + countdown that resets on late bids; skull "Sudden Death" hard stop | None sonically; binary confetti; value carried by host | Per-seller notification tiers (All / Personalized / None); no in-app sound toggle found | Resetting-clock near-misses, skull timer, host airhorns and hype music (external) | V-s / I |
| **DripShop Instant Packs** | Digital pack rip | Wrapper-tear ASMR sound (only app-owned SFX evidenced in this group); progressive OPEN button; rarity-tinted background animation | Purchase → OPEN → tear → card lands | ~2–4 s per open (I); "turbo reveal" collapses it | User-driven build via progressive OPEN; rarity tint primes the outcome *before* the card lands | common / rare / chase; background animation varies by tier; sound tiering unverified | Turbo reveal toggle; no mute found | Sell-back-and-re-rip loop, in-app currency; visual language is tactile not slot | V-s / I |
| **Fanatics Live Instant Rips** | Digital pack rip | No app-owned SFX evidenced; broadcast-style graphics | Buyer/breaker decides when to open; reveal animation | "Faster" than old wheel (V-s); ~2–4 s (I) | Elimination fade-through of candidates landing with a shimmer; human pause before open | **Visual tell in the animation:** base / chase / grail pack shown before the card (V-s); no sonic tiering documented | Per-break notifications; reaction-animation caps; auto-vault with instant replay | Retired the spinning wheel on purpose; sports-TV register | V-s / I |
| **HypeDrop** | Web mystery box | Carousel tick, decel, stop, tier sting, jackpot spinner, HypeSpin riser (I); reviewers confirm "sound effects adding to the suspense" | Open → spin → stop → reveal card; battles; jackpot | Spin ~5–7 s (I); Fast Mode ~1 s/round | CS:GO roulette: ticks thin out as easing flattens; hush before stop | Colour glow grey→gold; louder/longer sting top tiers (I) | Fast Mode battles, multi-box; browser-tab mute is the de facto control | Users say "casino"; jackpot spinners; regulator warnings (DK geo-block, WA State, FR DGCCRF) | V-s / I |
| **Lootie** (defunct 2025) | Web mystery box | Same carousel grammar (I) | Same | ~5 s (I) | Same | Same | Unknown | Trust collapse; fairness red flags | I |
| **Cases.gg** | Web mystery box | Full CS:GO-site kit (I); "flashy", "glossy UI" (V-s) | Open, battles (simultaneous reels), jackpot | ~5 s/spin (I) | Roulette | Colour-coded odds and stings | Genre peers document "Quick Unbox" / "Fast Mode" | Framed as "sweepstakes casino twist"; high-risk MCC | V-s / I |
| **RillaBox** | Web mystery box | 3D box-unwrap animation with foley-type build (I on sound); reveal sting | Open → unwrap → item bursts out | Unwrap ~4–6 s (I); Fast Mode "straight to results in seconds" (V-s) | Riser-to-impact, **no tick**; anticipation is the box physically opening | Colour glow; longer tails top tiers (I) | Lightning-bolt Fast Mode; 1/2/3/4 multi-open row | Crash and Plinko games sit beside it; the unwrap itself is the most premium opener in the group | V-s / I |
| **SNKRS / StockX / GOAT drops** | Drop mechanics | None bespoke; OS notification tone + system haptic | "GOT 'EM" push; bid pushes | Minutes of silent pending; instant static result | Scarcity, not sound; silence → binary | None | N/A | None in audio; "virtual slot machine" is a user description of the odds, not the UI | V-s / I |
| **Sotheby's / Christie's apps** | Auction | Live auctioneer audio only; push/email on outbid | Bidding, outbid | Human cadence | Human voice and hammer | None | N/A | None; the restrained benchmark | V-s |
| **CS:GO / CS2 (Valve)** | Case opening (genre origin) | Unlock/key turn; single-sample per-item tick; slowdown transition cue; **tier reveal sting** (4 tiers + knife showcase); **tier "awarded" sting**; inventory ping | Unlock → ~6 s reel → stop → reveal card → awarded | ~6 s spin (V-s Steam); fan replicas use 5 s ease-out; knife two-stage payoff ~+1.6 s / +2.1 s (plugin timing) | Tempo alone: one tick sample, intervals widen on the ease-out curve; two-hit payoff (reveal sting then awarded sting) | Per-tier reveal + awarded stings across Mil-Spec → Covert → Gold (simulators agree on the ladder, differ on exact file-to-tier mapping); gold adds a famous sustained sweep-and-shimmer | No official skip or multi-open; clicking the inventory mid-spin skips to the drop; FR/DE replaced the reel with an X-Ray scanner | Regulator-cited near-miss reel (NY AG 2026, Belgian GC 2018); gold near-miss removed 2018 but reds still land adjacent | V-s + code |
| **CS:GO third-party sites** (Key-Drop, CSGORoll, Skin.Club, CSGOFast, CSGOEmpire, DaddySkins) | Case opening clones | Reel tick/stop/tier stings; "sparks and fire" (Key-Drop); battle-win stings; generic "crescendo of audio cues" | Open, multi-open, battles with parallel reels | ~5 s; skip / fast / mass modes everywhere | Roulette; "higher suspense individual reveals" as a marketed mode | Colour "quality stripe"; escalating win screens | Skip, Fast Mode, mass open, battle Fast mode | Jackpot/Crazy/Terminal battle modes; CSGOEmpire markets itself as *not* having "animations and sound effects" | V-s / I |
| **Genshin Impact Wish** | Gacha | Menu music; meteor-fall whoosh; approach hold; **colour-coded strike** (blue/purple/gold); per-card reveal taps; 5★ longer-tailed hit | Confirm → cinematic → per-item cards → summary | Single ~8–10 s; 10-pull ~30 s watched (I) | Rising whoosh → held approach → strike whose colour and tone are the tell; rarest card revealed last | Three tiers = three strikes; 5★ brightest and longest; "Capturing Radiance" purple-turns-gold variant | Skip button before the colour reveals; music/SFX sliders (I) | No reels or coins; the purple-with-gold-flash tell is the one near-miss analogue | V-s / I |
| **Honkai: Star Rail Warp** | Gacha (data point) | Ticket kiosk; **music switches to a more upbeat track when a 5★ is in the pull** | Same structure as Genshin | Similar | Music bed carries the tell rather than an impact sting | 5★ = rainbow/blur ticket + music change | Skip | Same as Genshin | V-s |
| **Monopoly Go** | Casual loot | Dice clatter synced to haptics; per-tile land; cash roll-up; Bank Heist reels; Peg-E Plinko; wheel ticks; sticker pack tear/flip | Every roll; minigames; sticker packs | Roll-to-settle ~1.5–2.5 s, tempo-tuned so a 2 and a 12 feel equal (V-s) | Compressed: clatter → settle → payoff; minigames carry the slot arc | Stickers 1–6★ + gold; Wild Sticker sequence | Single sound toggle; multipliers compress feedback | Bank Heist 3-symbol reels, Plinko, wheel ticks, roll-up counters are slot cues; dice+haptic is not | V-s / I |
| **Coin Master** | Social casino | Three-reel slot hub; staggered reel stops; win-line chime; coin cascade; attack/raid/shield stings; per-village theme rotation | Every spin | Spin ~2–3 s; hold-to-auto-spin | Textbook slot: whir → stop, stop… stop; near-miss designed in | Bet multipliers, jackpot events | Auto-spin; multipliers | All of it. The anti-reference. | V-s |
| **Pokémon TCG Pocket** | Digital pack rip | Carousel tick; **swipe-to-tear** (hero cue, tuned against real packs by the art director); card slide; per-card flip; rare card-back glow + sting; **Immersive cards switch the music** | Select → tear → five flips → summary | Tear ~1 s; flip ~0.7–1 s; pack ~15–25 s watched (I) | Physical-tactile: foil tear → flips whose card back sets expectation before the turn | ◆ plain → ★ sparkle + sting → Immersive music change + camera dive → Crown heaviest | Fast-forward exists but "only speeds up one animation" per tap; players petition for a real skip; haptics toggle | Almost none; shine-before-flip is a soft near-miss analogue | V-s / I |
| **Duolingo** | Craft ref | Correct (F♯→A♯ major third up), incorrect (F♯→C tritone down), lesson-complete jingle, streak celebrations, app-launch sound | Every answer; lesson end; milestones | Correct = two sixteenth notes (V-s) | Per-answer micro-reward → lesson-boundary jingle + confetti | Streak milestones get dedicated celebrations | Single opt-out toggle; every sound has a visual twin; heavy "how to turn off" search demand | Bright, high, major-key, mascot-voiced: the anti-restraint reference. The *system* is borrowable. | V-s |
| **Apple Pay / iOS system sounds** | Craft ref | Apple Pay success (two-note) + two-tap haptic; failure "try again" sound; notification tones; keyboard clicks; Watch sounds recorded from real housings | Payment success/failure; system events | Sub-second; sync sensitivity ±10 ms (V) | Watch alarm: haptic ramps, cuts, sound answers it | By modality and vocabulary (success/warning/error, light/medium/heavy), not loudness | Keyboard clicks taper as typing speeds up; silent switch mutes all UI sounds; toggle required | None; Apple rejected candidates as "too happy and frivolous" or "a little too harsh" | V |
| **Things 3** | Craft ref | One completion sound on check-off (I); nothing else | Task complete | Sub-second (I) | None; the act is the reward | Flat: same sound for a task and a project | Silent-switch governed | None; "one timbre, one moment" | I |
| **Headspace** | Craft ref | Session start/end bells baked into narration; soft UI cues; opt-in haptic assistance | Session boundaries | Long-decay bell at close (I) | Resolution by decay into silence, not cadence | Minimal | Bells not user-configurable; haptics opt-in | None; "let decay do the luxury" | V-s / I |
| **Physical luxury-watch unboxing** (Rolex, AP; ASMR videos) | Category-native ritual | Sleeve slide, lid hinge, seal tag, tissue and velour hush, bracelet chatter, clasp click, bezel click; room tone between | Layered packaging: sleeve → box → seal → pillow → watch | Minutes, gapped; many small dry mechanical events | Rolex "design layering to deliberately extend the experience of anticipation and discovery" (V-s); no riser, no drop | None; the object is the payoff | N/A | None; the opposite of a slot: "Put your sound on", "no talking" | V-s / I |

---

## 2. Product notes

### 2.1 Live-commerce breaking platforms

The striking result here is negative. Across roughly 45 queries, **no written source describes a single in-app UI sound for Whatnot, DripShop or Fanatics Live**, apart from one reviewer's line about DripShop's tear. These products delegate the payoff to a human breaker's voice and the room. The app's own audio is an OS push tone and, at most, a wrapper tear.

**Whatnot.**
- Winning a bid triggers "a digital confetti explosion" (V-s, Fortune via Yahoo). Sound for that moment is not described anywhere.
- Notifications are the dominant app-owned sound. Per-seller bell tiers All / Personalized / None exist (V-s, Help Center); a reviewer calls them "extremely annoying… all on or all off"; a YouTube title reads "Mute The Auction Alerts!" (V-s). A TikTok discover topic "Whatnot App Notification Sounds Like" and a Blerp "Whatnot Soundboard" show the notification tone is recognisable enough to be memed (V-s existence only; timbre undocumented).
- Break randomizer wheel with "Quick Spin" (default on) or a "slower, more drawn-out animation" (V-s). Skull icon marks Sudden Death timers that never extend and end at 00:01; standard auctions reset to 10 s on late bids (V-s).
- Host sound effects are external: OBS support, TikTok guides on adding sound effects to a Whatnot stream, and a third-party OBS randomizer spinner sold on Whatnot itself (V-s).
- Whatnot Engineering names "quantity and quality of messages" as the top notification concern (V-s, Medium).
- Inferred: the in-stream UI is near-silent under the host mic; a bid-tap tick and outbid alert probably exist but are undocumented.

**DripShop Instant Packs.**
- Press release: "an immersive animated opening sequence that recreates the anticipation of physical ripping", "water-textured custom pack art and dynamic background animations that reflect item rarity", "a progressive 'OPEN' button [that] heightens anticipation", UI "clean, celebratory, and optimized for content capture" (V-s).
- Blockworks: "an ASMR card-opening experience with an emphasis on the shiny wrapper and that ripping sound" (V-s). This is the only textual evidence of an app-owned sound effect in the whole live-breaking group.
- Changelog: "turbo reveal in off-stream product details" (V-s, App Store). Tiers named common / rare / chase (V-s, Help Center).
- Arc: odds shown before purchase → progressive OPEN (the user generates the build) → rarity-tinted background primes the outcome before the card lands → full-screen celebratory frame built for screen recording.
- The reveal also runs on the web dashboard, so audio there must be gesture-gated (I).

**Fanatics Live Instant Rips and Fanatics Collect.**
- Release notes: the random-break winner reveal replaced the spinning wheel; "names and team logos fade through one at a time and land on the winner with a shimmer effect — cleaner, faster, and built to feel like a real reveal moment"; viewer reaction animations are capped for performance (V-s).
- Instant Rips: "a digital sealed pack is revealed, and when the buyer or breaker decides to open, the graphic animation starts revealing the card"; hits are auto-vaulted and replayable, "relive your biggest pulls" (V-s, support FAQ).
- Odyssey repacks span roughly $90 to $3,800 (V-s, cllct). The reveal animation carries a tier tell: "that graphic animation is also a tell, it shows whether the card in the batch is a base pack, chase pack, or the top dog 'grail' pack" (V-s, Sports Collectors Daily). No sonic tiering is documented. "Stash or Pass" above a value threshold is a decision prompt, not a celebration.
- Zero textual evidence of any app-owned sound. Inferred near-silent UI with OS push only.

**Genre context.** Card breaks are "a bit of theater" that aim to "recreate the high-energy, thrill-filled environment of a casino", with loud music and shouted pitches (V-s, All Vintage Cards). Fanatics frames breakers as entertainers who "make sure every reveal feels electric" (V-s). Psychology Today attributes the pull to an anticipation-then-outcome loop amplified by group uncertainty and parasocial attachment (V-s). The pause before the flip is also a trust act: "every assignment and opening happens live, on camera" (V-s, Whatnot Trust Center). For a solo in-app reveal, the voice layer is missing and must be replaced by design, not by louder effects.

### 2.2 Web mystery-box platforms

None of the four sites publishes a sound inventory. The grammar is inherited wholesale from CS:GO (Section 2.4), with RillaBox as the one structural deviation.

**HypeDrop.** Reviewers: the interface "resembles a casino game, with animations and sound effects adding to the suspense" (V-s, hypeskins); "spinning wheels revealing which prize you'll receive" (V-s, deadspin). Trustpilot users describe "watching items spin down and slowly land on their ticketed item" and one wished they "could actually tell where it's going to stop", to which HypeDrop replied "the spin is just visual and doesn't affect the outcome" (V-s). Battle modes Crazy / Shared / Group / Terminal / Jackpot, where "a final spinner decides the winner"; HypeSpin add-on "guarantees a high-value item" (spectacle with no uncertainty); Fast Mode battles are "over in the blink of an eye" (V-s). Geo-blocked in Denmark; Washington State Gambling Commission and French DGCCRF have warned its influencers (V-s). No mute toggle documented.

**Lootie.** Stopped fulfilling orders in 2025, paid site credits, went offline; a server-seed fairness red flag was reported (V-s). Same carousel grammar (I). A cautionary case on trust, not a sound reference.

**Cases.gg.** "Flashy design", "slick UX", "glossy UI"; odds colour-coded on hover; battles open simultaneously (V-s). Framed by casinos.org as "a unique twist on sweepstakes casinos" (V-s). Genre peers document the repetition tools: Clash.gg "Quick Unbox" opens "instantly with no waiting through animations"; Rain.gg has a "Fast Mode" battle modifier (V-s).

**RillaBox.** The outlier. Boxes are "built in full 3D, and when you click Open you see animations showing how the box unwraps itself"; "new animated unveilings enhance the excitement but may slow down performance on older devices" (V-s, betterchecked). Fast Mode "cuts out the extra animations… straight to the results in just seconds"; a "1 2 3 4" multi-open row sits beside the button (V-s). The arc is riser-to-impact with no decelerating tick: anticipation is the box physically opening, payoff is the item emerging. But Crash and Plinko games "push RillaBox out of 'online retail mystery box' and into 'lightly-regulated crypto casino with a mystery box lobby attached'" (V-s).

### 2.3 Drop mechanics and auction apps

**SNKRS, StockX, GOAT.** Draw results arrive as a "GOT 'EM" push plus email; shock-drop pushes vibrate (V-s). StockX pushes new bids (V-s). None of these ship bespoke win audio: the OS notification tone and system haptic are the entire payoff (I). Anticipation is minutes of silent pending; the reward is a static screen that becomes a social trophy. A user calls SNKRS "a virtual slot machine for the chance to actually spend money" (V-s), which is a comment on odds, not on audio. Gamified without audio juice.

**Sotheby's and Christie's apps.** "Follow the bidding… by listening to the auctioneer" (V-s, Sotheby's help); Christie's LIVE is a streaming-video window with bid entry (V-s). The only sound is a live person. This is the restrained end of the spectrum for a luxury buyer.

### 2.4 CS:GO / CS2 case opening (the genre's origin)

This lineage defines the mystery-box genre, and it is the best-documented flow in the audit because open-source simulators name the sound events they imitate. Event names below were surfaced by GitHub code search in third-party plugin and simulator source; role descriptions are those authors' words. No game files were opened.

**Sequence and where sounds fire.**
1. Select case → "Unlock Container" → key consumed. Unlock/key-turn cue (`case_unlock` / `crate_open`).
2. Horizontal reel starts: "a roulette wheel will start, with a stream of skins flying past" (V-s). One short click per item crossing the pointer (`crate_item_scroll`, described as "Tick sound as items scroll past"). It is a single fixed sample.
3. A slowdown transition cue fires as the reel decelerates (`crate_display`, "Wheel slows down — transition to reveal").
4. Stop. A tier-selected **reveal sting** (`case_reveal_{rare|mythical|legendary|ancient}`; one simulator maps these to Mil-Spec / Restricted / Classified / Covert-and-Special).
5. Card animates in; a tier-selected **awarded sting** (`case_awarded_{common … ancient}`). Simulators agree there is one per tier up to knives and gloves but disagree on the exact file-to-tier mapping, so treat the ladder as verified and the mapping as approximate. A simulator's sound documentation (fetched in full) lists `csgo_ui_crate_open` for "Case opening starts", `csgo_ui_crate_item_scroll` for "During wheel spin", `csgo_ui_crate_display` for "Wheel slows down", six `case_awarded_*` files from Mil-Spec to "Rare knives/gloves", legacy `item_drop1_common … item_drop6_ancient` and `item_reveal3_rare … item_reveal6_ancient` "reveal sparkle" files, and separate `case_unlock`, `case_drop` and `case_scroll` UI cues (V).
6. Knives and gloves get an additional showcase cue (`item_showcase_knife`). One plugin fakes a knife drop by firing unlock at 0 s, knife showcase at +1.6 s, top-tier awarded at +2.1 s (V code; timing is the plugin's, treated as an approximation of Valve's two-stage payoff).
7. Inventory ping when the item lands (`inventory_new_item`). Sticker capsules have their own tick (`UI.StickerItemScroll`).

**Durations.** "The case opening animation takes about 6 seconds" (V-s, Steam thread). Fan replicas encode a 5 s CSS ease-out, `cubic-bezier(0,0,.3,1)` (V code), which is the community's perceptual model of Valve's curve. Unlock-to-spin about 1 s; the reveal hold is user-terminated (I).

**Tension → payoff.** Because the tick is one sample, tempo alone carries the tension: dense at launch, spreading as the ease-out flattens, so the last three or four ticks land at visibly increasing intervals (I). There is no documented explicit silence beat; the perceived gap is the last widened interval before the pointer settles. The payoff is two hits: reveal sting, then awarded sting after the card animates in. Academic description: "a spinning, roulette-wheel-like reel of various items that gradually slows over time until it eventually stops" (V-s, Zendle, Meyer & Over 2019).

**Rarity tiers.** Odds: Mil-Spec 79.92 %, Restricted 15.98 %, Classified 3.20 %, Covert 0.64 %, Gold 0.26 % (V-s). Distinct stings exist for at least four tiers plus the knife showcase. The gold reveal is community-famous: "The special knife sound can be heard when you obtain an 'Exceedingly Rare Special Item'" (V-s, video description). In words (I, from the two-event structure): a longer, brighter, sustained sweep-and-shimmer layered over the standard sting, distinctive enough that a CS2 exploit let players trigger it in-match via radio commands until Valve patched it (V-s, guide title). CS2 shipped a new opening animation in September 2023 (V-s). In France and Germany the X-Ray Scanner replaces the roulette entirely: "you must scan it first and reveal the item inside… you cannot skip a bad result" (V-s). Belgium and the Netherlands have had opening disabled since 2018 (V-s).

**Near-miss.** The NY Attorney General's 2026 complaint: "This visual gives users the impression that they 'almost' won the valuable item, a design feature associated with slot machines known as a 'near miss'" (V-s). Counter-evidence: "it is not possible to get a 'near miss' on a gold item in Counter-Strike 2. This change was implemented in 2018" (V-s, gHacks/Notebookcheck); a Steam thread agrees the yellow stripe stopped appearing adjacent after the 2018 Horizon UI update. Reds still land next to the winner, giving the "illusion of almost winning" (V-s, esports.net). Because there is no rarity-specific tick, **there is no audio near-miss tell in Valve's client**; the near-miss is purely the colour stripe under the pointer (I).

**Repetition.** No official skip and no multi-open in the Valve client. A Steam thread reports that "clicking on your inventory while the case is opening gets your drop instantly", and `host_timescale` works only offline (V-s). Heavy users bypass the whole audio arc. The persistence of the full 6 s loop is what third-party "fast open" toggles monetise (I).

**Third-party sites.** All keep Valve's horizontal reel and colour stripes; clones label the tier bar "Quality Stripe — KeyDrop Style" (V code). Deviations: Skin.Club "watch the roll animation and then use skip for fast case opening" (V-s); CSGOFast "fast or mass open options… sessions are meant to be quick" (V-s); Key-Drop multi-open plus "flashy case reveals and effects like sparks and fire" (V-s); DaddySkins markets both "quickly opening cases in rapid succession or higher suspense individual reveals" (V-s); CSGORoll runs seven battle modes "Classic, Shared, Fast, Jackpot, Clutch, Crazy, and Terminal" with parallel reels (V-s); CSGOEmpire markets its roulette as "straightforward, unlike other platforms which feature animations and sound effects" (V-s). Sound is documented only generically: "the clinking of virtual keys or triumphant fanfare upon revealing rare items", "a crescendo of audio cues", "a simple metallic clink… manipulated to sound more resonant" through pitch-shift and reverb (V-s, mercora.com).

### 2.5 Gacha and mobile loot systems

**Genshin Impact Wish.** Flow: banner screen with looping menu music → Wish ×1/×10 → cinematic "A Wish Upon Shooting Stars" (V-s title) where meteors streak and strike → per-item reveal cards tapped through → summary grid. Rarity is signalled during the meteor phase: blue = 3★, purple = 4★, gold = 5★ (V-s). Version 5.0 added "Capturing Radiance", where "your golden light turns purple and extra sparkly" (V-s). Fans isolate distinct per-rarity wish sound effects (V-s, video titles). Arc: rising whoosh as the stars fall, a held moment as the meteor approaches, then a strike whose colour and tone are the tell; the gold variant adds a brighter, longer-tailed hit with a particle cascade (I). In a 10-pull the rarest card is revealed last (I, standard behaviour). A Skip control exists during the cinematic; a HoYoLAB thread titled "Skip your 10 pulls before seeing the wishes' colour" confirms players treat the colour phase as a spoiler (V-s). No native mobile haptics on the wish (I). Casino vocabulary is absent; the one near-miss analogue is a purple meteor with a hidden gold pre-flash (I, community lore).

**Honkai: Star Rail and Zenless Zone Zero (data points).** HSR: a 5★ pull makes the warp ticket blurry with a rainbow effect, and "the music will be a lot more upbeat if your pull contains a 5-Star" (V-s). The tell is a **music-track switch**, not an impact sting. ZZZ has an official Haptic Feedback FAQ (V-s), making it the HoYo title with first-class mobile haptics.

**Monopoly Go.** Tap GO → "two dice clatter across the board, with the phone's haptics rumbling in sync" (V-s, Fast Company ME) → token hops with per-tile sounds → cash counter ticks up. The team tuned tempo explicitly: on a roll of 2 "the dice teeter between numbers to compensate for the short movement"; on a 12 "the game piece starts moving early before the numbers settle" to keep "an even, satisfying tempo" (V-s). Founding brief: "I Can't Stop Rolling" (V-s). Bank Heist "plays like a slot machine; each turn you spin to reveal three matching symbols"; Peg-E is "a Plinko-style slot machine" (V-s). Sticker packs run 1–6★ plus gold with a first-time Wild Sticker sequence (V-s). Sound is a single on/off from the settings gear (V-s). **Slot cues:** Bank Heist reels, Peg-E, wheel ticks, cash roll-up counters. **Not slot cues:** dice clatter with synced haptic, token hops, sticker tear and flip.

**Coin Master.** A single three-reel slot "handles all spins and serves as the main hub" (V-s, Deconstructor of Fun). Three matching middle-row symbols trigger coins, shields, Attack or Raid. Per-village themes rotate to mimic "different slot machines in traditional slots lobbies" (V-s, GameRefinery). Near-miss is designed in: "spinning reels, sound effects, and near-miss moments where two icons align but the third falls short are all documented design choices… researchers associate with regulated casino machines" (V-s, Lawfold). Hold-to-auto-spin and bet multipliers are the repetition tools. Art direction softens the casino look, but the audio grammar is entirely slot-derived: reel whir, staggered stops, win-line chime, coin cascade, near-miss silence-then-fail, bet-up escalation, jackpot fanfares. **This is the anti-reference for GemBreak.**

**Pokémon TCG Pocket.** Select pack on a carousel → swipe across the top to tear → five cards fan → tap or swipe each to flip → summary. The developers "paid particular attention to the sound packs make when opening"; art director Satoru Nagaya "searched for pleasant sounds while actually opening physical packs" and spent "considerable time testing and perfecting the pack opening sound effect… to find 'a sound that evokes a sense of excitement'" (V-s, GoNintendo and Google Play developer interview). A back-side opening exists: turn the pack over, lift, "open it with two fingers" (V-s). Rare cards show a different back before the flip, "a rainbow border glow or golden coloring. Cards may also sparkle" (V-s), and players peek edges by spreading the stack (V-s). Immersive (3★) cards "swoop into the frame… accompanied by unique music" (V-s, Wargamer): the top tier is protected by a **music change**, not a louder effect. A fast-forward button exists but "only speeds up one animation, and players have to keep tapping it to get through the whole process, barely saving any time" (V-s, ComicBook.com); Dexerto: "the pack opening ceremony takes too long—especially with promo packs and Immersive Art cards" (V-s). Players petition for "a less animation heavy way to open packs or make it skippable" (V-s, Pokémon forums). "The pack opening process uses haptic feedback from your device" (V-s); haptics can be toggled (V-s). Almost no casino tells; the shine-before-flip is a soft near-miss analogue (I). Reads premium and ASMR-like.

### 2.6 Craft references

**Apple (system sounds, Apple Pay, audio-haptic design).** All of the following is from fetched primary sources (V).
- The Apple Pay brief: "It should feel positive, like confirming a successful transaction," and match the checkmark. Three candidates were tried: one "too happy and frivolous", one that "worked really well with the check mark… but… a little too harsh", and the winner, "not too serious, and it's clearly a confirmation" (WWDC19 810).
- The haptic: the first idea was to mirror the sound's waveform; "two simple taps actually did a better job… two instruments; one that you can hear and one that you can feel… they do have to play in the same tempo" (WWDC19 810). Timing sensitivity: "pushing it back or forward by as little as ten milliseconds sometimes makes a difference" (WWDC17 803). Apple Watch alarm inverts the order: the haptic ramps, cuts, then the sound plays "as an answer to the haptic", creating anticipation.
- Principles: Causality, Harmony ("things should feel the way they look, the way they sound"), Utility ("If you're tempted to add more? Well, maybe don't").
- Watch sounds were recorded by striking the actual steel, aluminium and gold housings so "what you hear… [is] made by the device itself" (WWDC17).
- Volume discipline: UI sounds sit at "a much lower volume than a notification sound"; long notification sounds duck other audio "for a very long time, so it becomes annoying"; filter out low frequencies the speaker cannot reproduce; "silence is golden… the absence of sound is as important as adding sound" (WWDC17).
- Repetition: keyboard clicks drop slightly in volume as typing speeds up. Test protocol: live with a sound "for a week or so"; "imagine using it 100 times more… take away all the things that don't feel compelling".
- Rules: sound effects are "nonessential" and must obey the silent switch (HIG Playing audio); "If you do add UI sounds, also add the option for people to turn them off" (WWDC17); reserve confirmation "for activities that are sufficiently important" (HIG Feedback); "the best haptic experience is one that people may not be conscious of, but miss when it's turned off" (HIG Playing haptics). No Apple document states a fixed haptic-before-audio offset; the published rule is same tempo plus ±10 ms experimentation.

**Duolingo.** Correct answer is two sixteenth notes, F♯→A♯, an ascending major third descended from doorbells, store chimes and Westminster Quarters; incorrect is F♯→C, a descending tritone "designed to make you feel bad" (V-s, losdoggies). One tonal root, two intervals. Lesson end escalates to a jingle plus confetti; streak milestones get dedicated celebrations (V-s). Sound effects are a single opt-out toggle and every sound has a visual twin so muted users lose nothing (V-s). The density of "how to turn off Duolingo sound effects" tutorials is itself evidence of long-use fatigue (I). Duolingo is the anti-restraint reference; the borrowable part is the system.

**Things 3.** A single short completion sound on check-off paired with the checkbox fill, and nothing else (I; no Cultured Code post about the sound could be located). Flat by design: a project completing sounds like a task completing. Cultured Code's restraint is documented elsewhere: the interface "doesn't turn overdue tasks red, making users feel guilty" (V-s, MacStories). The "one timbre, one moment" reference.

**Headspace.** Session bells are baked into the narrated audio, "controlled by the narrator rather than the user" (V-s). Opt-in "haptic assistance" exists per session (V-s, help centre). Secondary commentary describes "consistent use of specific wind chime-like tones across the app" (V-s, weak source). Resolution is by decay into silence rather than melodic cadence (I). The closest documented meditation-app sonic identity is Sonic Minds' work for Moments of Space, where start, end, milestone and notification sounds are kept "soft" so they never disrupt practice (V-s).

---

## 3. Evidence from pack-rip and case-opening videos

A dedicated sweep treated creator videos as a text source: titles, descriptions, article write-ups of specific videos, discover-page topics and forum threads that reference them. Video and social hosts were egress-blocked, so **no comments, chapter markers or caption tracks could be read**, and there is no timestamped evidence. What the text around the videos does establish:

**DripShop.** The reveal is marketed entirely on visuals: "water-textured custom pack art, dynamic background animations that reflect item rarity, and a progressive 'OPEN' button to heighten anticipation" (V-s). The web path is a one-click "Open pack" button with no tear gesture described (V-s, Help Center); the animated tear is app-side. No creator title, caption or review describing the Instant Pack audio surfaced. Inferred: sound is under-designed relative to the animation.

**Fanatics Instant Rips.** "When the buyer or breaker decides to open, the graphic animation starts revealing the card. Interestingly enough, that graphic animation is also a tell, it shows whether the card in the batch is a base pack, chase pack, or the top dog 'grail' pack" (V-s, Sports Collectors Daily). "Fanatics Live also features instant replays, so collectors can look back at the moment they acquired the card" (V-s). Show titles ("Grail Chasing! With Owen on Fanatics Live") confirm the reveal lives inside a hosted stream under a live mic. No sound described anywhere.

**Whatnot.** The visible spin wheel is a third-party overlay, not native: "How To ACTUALLY Add Whatnot Spin Wheel (Whatnot Randomizer Substitute)", "$120 a wheel spin" (V-s, video and TikTok titles). Native Surprise Sets allocate at random with no wheel and "re-randomization is not permitted" (V-s, Help Center). Physical "Rip & Ship" only; no digital pack reveal exists (V-s, absence).

**Pokémon TCG Pocket.** The community treats sparkles and sound as a decodable rarity system: "Sparkles & sound effects in pack openings explained" (V-s, video title, Nov 2024). Discover topics exist for "Pokemon Pocket Pack Sound", "Asmr Pokemon Card Pack Opening" and "How to Skip Pack Animation Tcg" (V-s). Users cite "great sound effects when you tear the packs open" and "the satisfaction of hearing the sound of opening 10x packs" (V-s). Creators overlay their own ASMR ("close whispering, mic scratching") over 40-pack openings (V-s), so the app's audio rarely reaches the audience. A pinch-zoom card flip prompted "just got my dopamine fix from this" (V-s, ScreenRant), which shows appetite for re-triggerable micro-moments. Fatigue complaints target gesture friction and multi-stage gating, not the sound itself.

**CS:GO / CS2.** The case-opening sound is a standalone cultural artefact: soundboard entries, an osu! beatmap titled "Valve - case opening sound cs:go", a Voicemod "csgo knife opening effect", and videos titled "CS:GO Case Opening and Gold sound 1 HOUR" (V-s). A separately named gold/knife sting exists and is the shareable unit. A sound-design write-up describes "a crescendo of audio cues" with "timing and rhythm of sound effects synchronized with visual actions" and community praise for "crispness and clarity" (V-s, mercora). Overwatch's developers, on the same lineage: "When you start opening a loot box, we want to build anticipation. We do this in a lot of ways—animations, camera work, spinning plates, and sounds" (V-s, Kotaku). Heavy users skip the whole arc via the inventory click.

**HypeDrop, RillaBox, Cases.gg.** Reviews describe speed ("fast, transparent reveal", "animated spinner roll") and fairness, never audio. RillaBox "updated their unboxing with 3D animations and new unveiling effects" (V-s). Audio is not a review criterion in this category at all.

**Genshin and Honkai: Star Rail.** HSR creators teach the tell: "How to tell if your warp is a 5 star BEFORE the golden door! Rainbow Ticket means EARLY HYPE!!" and "the music changes if it's a 5-star pull" (V-s, TikTok). Per-rarity sound-effect uploads exist for both games ("5 star Wish Sound Effect", "Honkai Star Rail | 5 Star/SSR Pull SFX") (V-s titles). HSR is the only flow in the audit where text claims an **audible** pre-reveal tell.

**Physical luxury-watch unboxings.** Titles instruct the viewer: "Put your sound on", "no talking, just pure relaxing ASMR sounds", "Rolex Unboxing ASMR: Hear the Elegance" (V-s). The packaging is described as deliberate pacing: "Rolex uses design layering to deliberately extend the experience of anticipation and discovery, with the removal of the outer sleeve leading to the unwrapping of the presentation box with neatly sorted compartments before finally unloading the timepiece inside its supportive bed of pillows" (V-s). Hardware has its own vocabulary: "Authentic Rolex clasps open and close with a satisfying click"; the "super satisfying sound a bezel makes when it clicks into place"; forum threads on clasp noise (V-s). Inferred sequence: sleeve slide → lid hinge → seal rustle → tissue and velour hush → bracelet-link chatter → clasp click, with room tone between events. Many small, dry mechanical sounds with gaps. The opposite of a riser and a drop.

**What the video layer adds to the audit.**
1. Every digital flow's pre-reveal tell is visual; only HSR has text claiming an audible one.
2. The shareable unit is a sub-2-second rarity sting, not the build-up. Stings become named, extractable assets.
3. Skip culture is universal. Long ceremonies are tolerated once and resented at volume.
4. Creators routinely replace app audio with their own. A reveal sound that matters must be short, clean and survive a phone-speaker screen recording.
5. Card-platform marketing sells animation and speed, never sound. Sound is under-designed in GemBreak's nearest neighbours, which is an opening.
6. The category-native luxury ritual is layered and gapped. That is the palette and the pacing model.

---

## 4. Anatomy of the open sequence across the genre

Four structurally different arcs exist. Everything in the audit is a variant of one of them.

| Arc | Origin | Tension mechanism | Payoff shape | Tell placement | Regulator exposure |
|---|---|---|---|---|---|
| **Roulette reel** | CS:GO → every clone, HypeDrop, Cases.gg | Per-item tick thinning on an ease-out over ~5–6 s | Two hits: reveal sting, then awarded sting | Colour stripe under pointer as it slows (visual near-miss) | Highest: named in NY AG, KSA, GambleAware, Belgian GC |
| **Cinematic strike** | Genshin, HSR | Rising whoosh, held approach | Single impact, tier-coloured, long tail; HSR swaps the music bed | In the approach (colour) or the music | Low: no reels or coins; the purple-gold fake-out is the one caveat |
| **Tactile rip** | Pokémon TCG Pocket, DripShop | The user's own gesture; the tear | Per-card flips; rare card back glows before the turn; top tier switches music | On the card back before the flip | Lowest: reads as physical ritual |
| **Physical unwrap** | RillaBox | 3D box opening; riser to impact, no tick | Item emerges; sting | None until emergence | Low for the opener itself; high for the site around it |

Live breaking (Whatnot, Fanatics) is a fifth case where the arc is human: countdown, host voice, pause, flip, reaction. Fanatics' elimination-fade winner reveal is the one app-owned mechanic that translates that cadence into UI without a wheel.

---

## 5. Patterns worth stealing (conceptually)

These are principles, not assets. Each names the product that demonstrates it and how it translates to a luxury watch reveal.

1. **Put the tell before the reveal, and make it honest.** Genshin's meteor colour, Pokémon TCG Pocket's glowing card back and DripShop's rarity-tinted background all shift the register *before* the object appears, so the payoff confirms rather than surprises. For GemBreak the pre-reveal light and tone should change once, truthfully, per tier. Never a fake-out (see Section 6, item 2).

2. **Signal the top tier with a change of music, not a louder effect.** Honkai: Star Rail switches to a more upbeat track when a 5★ is present; Pokémon TCG Pocket's Immersive cards arrive "accompanied by unique music". A key or texture change reads as an event; a bigger fanfare reads as a slot.

3. **Two-stage payoff: the hit and the afterglow.** Valve fires a reveal sting, then an "awarded" sting once the card has animated in, and gives knives a separate showcase cue about 1.6 s later. A luxury reveal wants the same: a confident arrival, then a settle that lets the object breathe.

4. **Record the real material.** Pokémon TCG Pocket's art director opened physical packs to find the sound; Apple struck real watch housings so the Watch's sounds are "made by the device itself". GemBreak's palette should come from a watch box hinge, tissue, a sapphire crystal, a bracelet, a clasp closing. No synth presets.

5. **Let tempo carry tension, never volume.** Valve's reel uses one tick sample and gets all of its suspense from interval spacing on an ease-out; Monopoly Go tunes roll length so a 2 and a 12 feel the same. Steal the principle: an accelerating or rising figure that resolves on the reveal. Do not steal the tick.

6. **Compose haptic and audio as two instruments in one tempo.** Apple Pay's success is two taps and two notes on the same beat, synchronised within about 10 ms. For anticipation, Apple's Watch alarm plays the haptic first and lets the sound answer it.

7. **One tonal root, opposite intervals for opposite outcomes.** Duolingo's grammar is F♯ with a major third up for yes and a tritone down for no. GemBreak needs the same discipline: success resolves upward and consonant, failure or "no" resolves downward, all in one key.

8. **Reserve confirmation for moments that matter, and design the silence.** Apple's HIG says to save Apple-Pay-grade confirmation for "sufficiently important" activities. Things gives one sound to one moment. SNKRS and the auction houses deliver the biggest moments of their categories with no bespoke audio at all. Navigation, tabs and browsing get haptics or nothing.

9. **Replace the wheel with an elimination fade.** Fanatics retired its spinning wheel for candidates that "fade through one at a time and land on the winner with a shimmer". Broadcast-graphics language, no roulette signifier.

10. **Taper on rapid repetition.** Apple's keyboard clicks get slightly quieter as typing speeds up. Any sound heard many times per session needs that kind of built-in relief, plus round-robin or pitch variation.

11. **Offer a skip, keep the ritual as the default.** HoYo offers Skip; DripShop offers turbo reveal; Pokémon TCG Pocket refuses a skip and players petition for one. The reveal should stay whole by default and be interruptible on request. Never rapid-fire.

12. **Design the payoff to be re-watched and screen-recorded.** Fanatics auto-vaults hits with replay; DripShop's UI is "optimized for content capture". The reveal audio has to survive a phone-speaker recording and stand on its own in someone else's feed.

13. **End on decay, not on a button.** Headspace closes a session with a single resonant bell into silence. The settle after a reveal can end the same way.

14. **Match the object's register.** Apple's rejected Apple Pay candidates define the corridor: not "too happy and frivolous", not "a little too harsh". A luxury watch reveal lives at "not too serious, and clearly a confirmation".

15. **Borrow the physical ritual's pacing: layered and gapped.** Rolex packaging is built to "deliberately extend the experience of anticipation and discovery" through sleeve, box, seal, pillow and clasp, each a small dry mechanical sound with room tone between. The build for a digital pack can be a sequence of quiet mechanical events with space around them, rather than one continuous riser.

---

## 6. Patterns that read as cheap or casino-like (do not use)

Each is named by at least one regulator, researcher or reviewer in this audit, or is the defining feature of the products users themselves call "casino".

1. **The horizontal roulette reel with per-item ticks and a deceleration curve.** CS:GO and every clone, HypeDrop, Cases.gg. Named as slot-derived by the NY Attorney General, the Dutch KSA, GambleAware and the Belgian Gaming Commission. Patents describe the slowdown as a tunable "suspense factor". This is the single most recognisable casino signifier in the category and GemBreak must not have one, even dressed up.

2. **Near-miss adjacency and fake-out tells.** Reds landing next to the winner; a purple meteor with a hidden gold flash; two reel symbols aligning while the third "falls short" (Coin Master, cited in litigation). Zendle et al. found near-miss presentation strengthened the spend-to-problem-gambling link. Any pre-reveal tell must be truthful.

3. **Staggered reel stops and three-symbol matches.** Coin Master's core loop; Monopoly Go's Bank Heist. The stop-stop-stop rhythm is the slot machine.

4. **Coin cascades, cash roll-up counters and Plinko drops.** Coin Master's bank fill; Monopoly Go's counters and Peg-E. Value should be stated, not rained.

5. **Jackpot spinners and "second chance" spectacle.** HypeDrop's Jackpot battles where "a final spinner decides the winner" and HypeSpin's guaranteed-win riser. A second wheel after the first is pure casino.

6. **Rapid re-fire.** Fast Mode, Quick Unbox, mass open, hold-to-auto-spin, "1 2 3 4" multi-open rows. The KSA specifically asked for the removal of "rapid successive opening". A skip is fine; a machine-gun is not.

7. **Escalating "big win" fanfare ladders, sparks and fire.** Key-Drop's "flashy case reveals and effects like sparks and fire"; the "crescendo of audio cues" reviewers describe. Louder-per-tier is the slot escalation curve. Tier difference should come from weight, length, key and texture.

8. **Klaxons, airhorns and binary confetti.** Whatnot's win confetti and host airhorns read arcade and auction-house. Fine for a live break, wrong for a luxury object.

9. **Sudden-death skulls and resetting-clock countdowns.** Whatnot's timer mechanics create serial near-misses. GemBreak has no auction, so this pattern has no place.

10. **Background casino music loops and slot-lobby theme rotation.** Coin Master's per-village themes are explicitly modelled on a slots lobby. Any bed music must sound like a room, not a floor.

11. **Bright, high, major-key mascot chirps on every tap.** Duolingo's grammar works for a children's-education register and generates "how do I turn this off" search demand. It is the anti-restraint reference.

12. **"Too happy and frivolous" or "a little too harsh" confirmations.** Apple's two rejected Apple Pay candidates. Both read cheap in a luxury context.

13. **Sounds that ignore the silent switch or have no toggle.** Apple: "the last thing we want is for people to always hit the ringer switch, or even worse, delete your app."

---

## 7. Regulatory and research backdrop

Sound is explicitly in scope for regulators, not just visuals.

- **Dutch Kansspelautoriteit.** Chair René Jansen: loot boxes are "designed like gambling games with all sorts of sound effects and visual effects when you open such a loot box." The KSA called for removing "near-win" effects, visual effects and rapid successive opening (V-s). A 2025 narrative review reports the Netherlands "proposed limits on animations and sound effects that might mislead players" and UK Gambling Commission guidance on "how outcomes are presented" (V-s).
- **GambleAware, "Lifting the Lid on Loot-Boxes".** Shared slot and loot-box features include "near-miss features, plus visual and sound cues associated with participation and reward… well known to trigger urges to play along with increased excitement and faster play"; reels "that slow down, highlight 'almost obtained' rewards, or display rare items in the reel even when they are not awarded" (V-s).
- **NY Attorney General v. Valve (2026).** Pleads the "animated spinning wheel" and near-miss design as slot-like (V-s). Belgian Gaming Commission (2018) found CS:GO cases meet every element of a game of chance (V-s).
- **Zendle, Meyer & Over (2019).** "Loot box displays typically imply that players have almost received valuable items—in other words, that they are 'near misses'"; uses CS:GO's slowing reel as the exemplar (V-s).
- **Larche, Chini, Lee, Dixon & Fernandes (2021).** Rarer loot-box rewards produce longer post-reinforcement pauses, larger skin-conductance and force responses and greater urge, "similar to the way slots gamblers treat rare large wins" (V-s). The rarity-escalated audiovisual reveal is the manipulated cue.
- **Brooks & Clark (2019).** "Opening a loot box generates audiovisual feedback that often reflects the style of the game and is sometimes reminiscent of slot machines" (V-s).
- **Patents.** Roulette-ball deceleration parameterised at "6 or 8 slots" out (US 9,582,958); "slot machine with variable suspense factor" (US 9,659,445) (V-s).

GemBreak is purchase-first and every pack contains a real watch, which puts it outside the loot-box definition in most jurisdictions. The audio should nonetheless be built so that a screenshot or screen recording of the reveal could not be mistaken for any of the products in Section 6.

---

## 8. What carries into Phase 2

Not the spec. The constraints the audit imposes on it.

- **Arc:** tactile rip or physical unwrap, not a reel. The user's gesture starts the build; the build is rising pitch or accelerating figure, or a layered sequence of quiet mechanical events, never volume; one honest tier tell before the reveal; two-stage payoff (arrival, then settle into decay).
- **Palette:** recorded watch-box and watch materials as the single sonic family, tuned to one root with consonant-up for success and down for failure.
- **Tiers:** differentiated by weight, length, key and texture, with the top tier signalled by a change in the music or harmonic bed rather than a louder sting.
- **UI:** sub-150 ms, quiet, high-passed for phone speakers, kept out of the payoff's frequency range, haptic-first where possible, silent for navigation.
- **Repetition:** round-robin and pitch variation on anything heard more than a few times per session; volume taper on rapid re-triggers; skip available, never auto-repeat.
- **Platform:** obey the silent switch, expose a toggle, pair with haptics in the same tempo, and make the reveal survive a phone-speaker screen recording.

---

## 9. Sources

Grouped by section. Access level as noted in Section 0: Apple developer pages and GitHub source were read in full; all others were verified at search-snippet level.

**Live breaking (2.1)**
- https://finance.yahoo.com/news/inside-rise-whatnot-wildly-entertaining-140731017.html
- https://help.whatnot.com/hc/en-us/articles/9429224729101-Set-notifications-in-the-app
- https://help.whatnot.com/hc/en-us/articles/9779931101837-Start-an-auction-during-your-show
- https://help.whatnot.com/hc/en-us/articles/26596362677389-Breaks-feature-for-sellers
- https://help.whatnot.com/hc/en-us/articles/34107510260237-Surprise-Sets-Policy
- https://trust.whatnot.com/card-breaks
- https://medium.com/whatnot-engineering/powering-real-time-magic-moments-through-notifications-36cd833f898e
- https://racklify.com/encyclopedia/whatnot-sudden-death-vs-live-extend-auctions/
- https://justuseapp.com/en/app/1488269261/whatnot-buy-sell-go-live/reviews
- https://blockworks.com/news/drip-shop-live-instant-packs-trading-cards
- https://news.marketersmedia.com/drip-shop-live-launches-instant-packs-247-mystery-pack-ripping-now-with-crypto-payments-and-creator-tools/89162009
- https://help.dripshop.live/en/articles/11649444-how-to-reveal-open-your-instant-packs
- https://help.dripshop.live/en/articles/10771512-what-is-a-pull-box-instant-packs-on-drip
- https://apps.apple.com/us/app/drip-shop-live-card-breaks/id1568026219
- https://www.fanaticscollect.com/releases
- https://about.fanatics.live/post/fanatics-live-v1-4-product-update
- https://about.fanatics.live/post/sports-card-breaking-basics
- https://support.fanatics.live/hc/en-us/articles/27876644814493-Instant-Rips-Frequently-Asked-Questions
- https://www.fanatics.live/instantrips
- https://www.cllct.com/sports-collectibles/sports-cards/fanatics-enters-repack-market-with-instant-rips-1
- https://allvintagecards.com/why-everyone-is-obsessed-with-sports-card-breaks/
- https://www.psychologytoday.com/us/blog/positively-media/202306/what-drives-the-success-of-trading-card-box-breaks

**Web mystery boxes and drops (2.2, 2.3)**
- https://hypeskins.com/reviews/hypedrop
- https://www.trustpilot.com/review/hypedrop.com
- https://deadspin.com/mystery-boxes/hypedrop/
- https://www.hypedrop.com/blog/what-are-the-different-pvp-modes-on-hypedrop/
- https://casinorankr.com/reviews/hypedrop
- https://tech-insider.org/mystery-boxes/platforms/hypedrop-review/
- https://track360.io/blog/loot-box-vs-mystery-box-gambling-regulation-map-2026
- https://www.betterchecked.com/post/need-to-try-new-unboxing-mechanics-on-rillabox-cb5655eb
- https://unpacked.gg/mystery-boxes/rillabox-review/
- https://bitcoinist.com/rillabox-review/
- https://unpacked.gg/mystery-boxes/lootie-review/
- https://cases.gg/case-battles
- https://bitcoinist.com/cases-gg-review/
- https://casinos.org/cases-gg/
- https://clash.gg/csgo-case-battles
- https://rain.gg/games/case-battles
- https://soho-london.co.uk/hypedrop-review-legit-or-scam
- https://yukaichou.com/advanced-gamification/decoding-the-mystery-box-a-dive-into-the-intricacies-of-reward-design/
- https://snobette.com/2020/12/nike-snkrs-app-tutorial-reservation-draw/
- https://kyw.substack.com/p/the-kicks-you-wear-vol-282-snkrs
- https://taplytics.com/blog/stockx-sends-push-notifications-to-alert-users-of-new-bids-on-sneakers/
- https://support.goat.com/hc/en-us/articles/25250350430093-What-are-GOAT-Drops
- https://help.sothebys.com/en/support/solutions/articles/44002297462-how-can-i-bid-in-an-auction-
- https://www.christies.com.cn/en/help/buying-guide/register-and-bid

**CS:GO lineage (2.4)**
- https://skinvault.gg/blog/ultimate-guide-to-cs2-cases/
- https://steamcommunity.com/app/730/discussions/0/618458030652954083
- https://steamcommunity.com/app/730/discussions/0/2263565217499621509/
- https://steamcommunity.com/sharedfiles/filedetails/?id=3338922208
- https://www.youtube.com/watch?v=0YQPHTrHbvA (description text only)
- https://www.thespike.gg/counter-strike-2/beginner-guides/cases-xray-scanner-cs2
- https://ag.ny.gov/press-release/2026/attorney-general-james-sues-game-developer-promoting-illegal-gambling-through
- https://www.ghacks.net/2026/05/21/valve-files-motion-to-dismiss-new-york-counter-strike-loot-box-lawsuit-compares-item-cases-to-baseball-cards/
- https://www.esports.net/news/counter-strike/case-opening-psychology/
- https://www.mercora.com/sound-design-in-cs2-case-opening-animations/
- https://github.com/NaathySz/Store-Cases (README; sound-event roles)
- https://github.com/immortal-seeker/cs2-simulator-docs (docs/sounds.md)
- https://github.com/Keel62155/CS-GO-Case-Opener (README; tier mapping)
- https://github.com/EmoteFroggy/7tvCases (script.js; awarded-tier mapping)
- https://github.com/ThaPwned/WCS (wcs.py; knife-drop timing)
- https://github.com/bachwebsite/bachwebsite.github.io (case-clicker; 5 s ease-out)
- https://play.google.com/store/apps/details?id=cases.opener.csgo&hl=en_US
- https://csgofast.gg/faq/games/cases
- https://cs2platforms.com/case-opening/keydrop-review/
- https://blockonomi.com/daddyskins-review/
- https://riskyskins.com/cs2-gambling-sites/csgoroll/
- https://cs2surge.com/csgoempire-coinflip/

**Gacha and mobile loot (2.5)**
- https://www.destructoid.com/genshin-impact-event-wishes-explained-character-vs-weapon-banners-updated-5-0/
- https://sportskeeda.com/esports/genshin-impact-capturing-radiance-guide-boosted-5-star-drop-rate-characters-explained
- https://www.hoyolab.com/article/187166
- https://www.hoyolab.com/article/1943029
- https://www.ginx.tv/en/4-star-5-star-warp-animation-differences
- https://twinfinite.net/guides/difference-between-4-star-5-star-pulls-in-honkai-star-rail/
- https://www.hoyolab.com/article/43567051
- https://fastcompanyme.com/technology/inside-the-addictive-design-behind-the-hit-monopoly-go-mobile-game/
- https://www.ezg.com/blog/monopoly-go-how-to-earn-cash-by-playing-shutdown-bank-heist
- https://www.dexerto.com/monopoly-go/monopoly-go-all-sticker-pack-types-and-odds-explained-2792686/
- https://www.deconstructoroffun.com/blog/2019/3/4/is-coin-master-the-new-face-of-social-casino
- https://lawfold.com/coin-master-class-action-lawsuit/
- https://www.gamerefinery.com/how-coin-masters-approachable-art-defined-casual-slot-genre/
- https://gonintendo.com/contents/40485-pokemon-trading-card-game-pocket-dev-on-why-sound-design-is-key-to-a-satisfying
- https://play.google.com/store/apps/editorial?id=mc_games_editorialmd_pokemontcgpocket_interview_ryotsujikawa_and_satorunagaya_fcp&hl=en_US
- https://www.wargamer.com/pokemon-tcg-pocket/rarity
- https://www.thegamer.com/psa-turn-your-booster-packs-around-in-pokemon-tcg-pocket/
- https://www.thegamer.com/pokemon-tcg-pocket-rarest-cards-triumphant-light/
- https://community.pokemon.com/en-us/discussion/18429/add-a-less-animation-heavy-way-to-open-packs-or-make-it-skippable
- https://www.iphoneincanada.ca/2024/10/30/pokemon-trading-card-game-pocket-available-ios-android/
- https://uism.co.jp/en/blog/why-are-people-obsessed-with-gacha-what-capsule-toys-can-teach-us-about-ux-engagement-strategy/
- https://www.sciencedirect.com/science/article/pii/S2451958824000381

**Craft references (2.6)** — Apple pages read in full
- https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- https://developer.apple.com/design/human-interface-guidelines/playing-audio
- https://developer.apple.com/design/human-interface-guidelines/feedback
- https://developer.apple.com/videos/play/wwdc2019/810 (Designing Audio-Haptic Experiences)
- https://developer.apple.com/videos/play/wwdc2019/223/ (Expanding the Sensory Experience with Core Haptics)
- https://developer.apple.com/videos/play/wwdc2021/10278 (Practice audio haptic design)
- https://developer.apple.com/videos/play/wwdc2017/803/ (Designing Sound)
- https://developer.apple.com/documentation/uikit/uinotificationfeedbackgenerator
- https://www.losdoggies.com/archives/8816 and https://www.losdoggies.com/archives/8842
- https://lingoly.io/turn-off-sound-effects-duolingo/
- https://duolingo.fandom.com/wiki/Frequently_asked_questions/Accessibility
- https://blog.duolingo.com/streak-celebration-parties/
- https://propersounds.co/Duolingo
- https://www.macstories.net/reviews/things-3-beauty-and-delight-in-a-task-manager/
- https://help.headspace.com/hc/en-us/articles/1260804149670-Closed-Captions-and-Haptic-Assistance-Options
- https://mindtime.app/resources/mindtime-vs-headspace
- https://sonicmindsagency.com/work/moments-of-space/
- https://www.20k.org/episodes/the-sound-of-apple

**Rip-video and physical-ritual evidence (3)** — all snippet level; video hosts blocked
- https://www.sportscollectorsdaily.com/fanatics-live-odyssey-repacks/
- https://sportscollectorsdigest.com/news/fanatics-live-launches-new-breaking-experience-featuring-modern-baseball-card-packs
- https://help.whatnot.com/hc/en-us/articles/34545407302797-Surprise-Set-Feature-for-Sellers
- https://www.youtube.com/watch?v=MawMX_8UgL0 (title only: "Sparkles & sound effects in pack openings explained")
- https://www.dexerto.com/pokemon/pokemon-tcg-pocket-desperately-needs-one-key-qol-feature-3005478/
- https://comicbook.com/gaming/news/pokemon-tcg-pocket-promo-packs-opening-screen/
- https://screenrant.com/pokemon-tcg-pocket-card-flipping-animation/
- https://steamcommunity.com/sharedfiles/filedetails/?id=513879285
- https://osu.ppy.sh/beatmapsets/2325904
- https://kotaku.com/why-opening-loot-boxes-feels-like-christmas-according-1793446800
- https://boxsniper.com/reviews/hypedrop
- https://www.tiktok.com/@malnoxx/video/7227224424003423534 (caption only)
- https://www.hoyolab.com/article/709174
- https://www.everestbands.com/blogs/bezel-barrel/what-does-a-complete-rolex-box-and-papers-look-like-today
- https://eliterigidboxes.com/blog/rolex-packaging-guide/
- https://www.rolexforums.com/showthread.php?t=694993

**Regulation and research (7)**
- https://kansspelautoriteit.nl/over-ons/bestuur-organisatie-samenwerking/bestuur-organisatie/blogs-rene-jansen-voorzitter/loot-boxes/
- https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2022/09/the-ultimate-loot-drop-the-netherlands-is-planning-to-ban-loot.html
- https://www.gambleaware.org/our-research/publication-library/articles/lifting-the-lid-on-loot-boxes/
- https://rozprawyspoleczne.edu.pl/Loot-boxes-gambling-like-mechanisms-hidden-in-digital-games-A-narrative-review-of,216647,0,2.html
- https://www.sciencedirect.com/science/article/abs/pii/S0747563219302468 (Zendle, Meyer & Over 2019)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7882574/ (Larche et al. 2021)
- https://www.sciencedirect.com/science/article/abs/pii/S0306460318315077 (Brooks & Clark 2019)
- https://www.nature.com/articles/s41562-018-0360-1 (Drummond & Sauer 2018)
- https://www.gamingcommission.be/sites/default/files/2021-08/onderzoeksrapport-loot-boxen-Engels-publicatie.pdf
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9582958
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9659445
