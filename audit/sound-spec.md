# GemBreak Sound Design — Phase 2: Sound Specification

**Version:** 1.1
**Status:** Phase 2 deliverable, revised on client direction during Phase 3. Built on `audit/competitor-audit.md`. Feeds `audit/sourcing-plan.md`, `audit/library-structure.md` and `audit/licenses.csv`.
**Date:** 2026-09-06
**Scope:** Every sound GemBreak ships, with trigger, duration, character, pitch relationship, loudness, interruptibility and haptic pairing, plus the rules that make them one product.

### Change log

**1.1 (this version).** Client direction: the set should lean toward polished video-game FX in the register of Triumph Rips, PackDraw and Skin.Club, and the open sequence is built around six core moments: a button pressed when the box is chosen, the box partially opened, the box fully opened, watches cycling through, the final watch selected, and a watch case being opened. Changes from 1.0:

- A fourth palette layer, **Designed**, is added: synthetic sweeteners layered under recorded cores. Every UI sound gains a small designed glint; every reveal event gains sub, shimmer or tonal layers. The three recorded layers remain the identity.
- The hold-to-wind build is replaced by the six-moment sequence. The cycle is scored as an **accelerate-and-snap**, not a spin-down: per-item passes are air-and-tone flips with no click transient, the rate rises to a blur, and the selection lands as an instant mechanical lock. This keeps the game feel the client wants while holding the brief's bans on reel-stop clicks and near-miss audio.
- The honest tier tell moves to the **partial open**: light spills from the crack, tinted and voiced by tier. The **selection lock** is the constant moment, identical for every tier. The **case open** carries the tier payoff.
- Tier payoffs gain designed layers (shimmer tails, sub thumps on the top two tiers, a short stinger on tier 4). Coin cascades, klaxons and fanfare ladders remain prohibited.
- Loudness anchor, key, interval grammar, frequency plan, repetition rules, platform behaviour and the phone-speaker protocol are unchanged.

**1.0.** Initial spec.

---

## 0. How to read this document

- **Section 1** defines the sonic identity: the four layers, the key, the interval grammar, the frequency plan and the loudness anchor. Everything in the inventory is derived from it.
- **Section 2** restates the brief's design rules as testable requirements.
- **Section 3** is the master inventory table. Every row is one asset or one asset group.
- **Sections 4 and 5** detail the open sequence and the rarity ladder, which are the only places the spec allows length.
- **Sections 6 to 10** cover repetition, haptics, platform behaviour, the phone-speaker check and the slot-machine exclusion test.
- **Section 11** lists the product decisions this spec assumes and flags for confirmation.

**Loudness convention.** Sounds of 1 s or less are measured as momentary LUFS maximum (400 ms window). Longer sounds are measured as short-term LUFS maximum (3 s window). All levels are given relative to one anchor, the top-tier payoff, expressed in LU. The anchor is set at −14 LUFS-S max with a −1 dBTP ceiling; every other sound carries a −1 dBTP ceiling too. The absolute anchor is a starting point to be tuned on device; the relative ladder is the specification.

**Duration convention.** Durations are the audible length from onset to the point where the tail falls 40 dB below peak, in milliseconds. A "tail" is the natural decay after the last struck event, not reverb added in the mix.

**IDs.** Every asset has a stable ID of the form `family_event[_variant]`. Engineering wires against IDs, not filenames. `audit/library-structure.md` maps IDs to files.

---

## 1. Sonic identity

### 1.1 The concept: a watch, produced like a game

The audit's strongest craft finding was that premium products record the real object. The client's direction is that the result should feel like a polished game. Those are compatible: game audio is built exactly this way, a recorded core for authenticity with designed layers for weight, sparkle and clarity on small speakers. GemBreak's set is made from a luxury watch and its box, then produced with game-audio layering. Four layers, one family:

| Layer | Source | Role in the set | Character in words |
|---|---|---|---|
| **Steel** | Bracelet links, deployant clasp, bezel ratchet, crown, case set down on wood and leather, a latch locking | The core of every UI transient and every mechanical event | Dry, small, precise, close-miked. Short. |
| **Sapphire** | Struck and bowed sapphire crystal and tuned glass, pitched | The core of every confirmation, the reveal strike, every tier payoff, notifications | Clear, bell-like, fast attack, clean decay. The pitched voice. |
| **Cloth** | Tissue paper, velour lining, leather lid, air moving in a box | Transitions, sheets, the per-item pass in the cycle, the settle | Soft noise with shape. |
| **Designed** | Synthetic: sub thumps, tonal glints, shimmer and sparkle tails, filtered-noise risers, pad beds | Sweeteners layered under the three recorded cores. Never heard alone. | Bright where it needs to cut, warm where it needs weight. Clean. Never 8-bit, never trailer. |

**Rules:**
- Every sound has a recorded core from Steel, Sapphire or Cloth. Designed elements are added to it, never substituted for it.
- The Designed layer is what makes the set read as game-polished. It is also the first thing to reduce if a sound starts to feel cheap. If a sound works without its sweetener, ship it without.

### 1.2 Key and interval grammar

One key for the entire product: **E major**, with the pentatonic subset (E, F♯, G♯, B, C♯) for all UI and confirmation sounds. Two notes are reserved:

- **D♯ (the major seventh)** appears only in tier 3 and tier 4 material. It is the colour that says "this is not an ordinary open".
- **E6 (the high octave, 1319 Hz)** appears only at completion moments: purchase confirmed, the top of the cycle sweep, the tier-3 afterglow, the tier-4 top note, and the "delivered" notification.

Interval grammar, applied everywhere:

| Meaning | Interval | Example |
|---|---|---|
| Yes, done, confirmed | Rising perfect fifth, E→B | Purchase confirmed, success |
| In progress, added, staged | Single G♯ (the third) | Add to cart, delivery requested |
| Arrival, complete cycle | Rising fifth plus octave, E→B→E′ | Delivered, tier 4 |
| No, blocked, failed | No pitch. A damped steel stop with a slight downward bend and a low designed thud | Error, payment failed, disabled |
| Navigation | Unpitched steel or cloth with a faint designed glint at E7 (2637 Hz) or B7 (3951 Hz) | Tap, tab, back, sheets |
| Tension | Stepwise pentatonic ascent that stops one note short, resolved by the next event | The cycle sweep, resolved by the lock |

Failure is deliberately non-tonal. A luxury buyer who mistypes a card number should feel "not yet", not punished.

### 1.3 Frequency plan

UI sounds stay out of the range the payoff occupies. Enforced with high-pass filters baked into the assets.

| Band | Owner | Rule |
|---|---|---|
| Below 250 Hz | Designed sub layer only, on tier 3 and 4 payoffs and the selection lock | Headphone weight. Nothing may depend on it; the same events carry a 250–400 Hz knock so the weight reads on a phone speaker. |
| 250–1200 Hz | **Payoff body**: sapphire fundamentals E4 (330 Hz) and E5 (659 Hz), the box knock, the harmonic bed, the lock thump | UI sounds are high-passed at 800 Hz and carry no sustained energy here. |
| 1.2–6 kHz | **UI steel transients**, designed glints, sapphire upper partials, cycle passes | UI sounds live here and only here. Payoff sounds pass through this band on attack but do not sustain in it. |
| 6–12 kHz | Air: cloth, shimmer and sparkle tails | Shared, low level. Nothing structural lives here. |

### 1.4 Loudness ladder

Relative to the anchor (tier-4 payoff = 0 LU):

| Group | Level (LU) | Absolute at the stated anchor |
|---|---|---|
| Tier payoffs | 0 / −2 / −4 / −6 (T4 → T1) | −14 to −20 LUFS |
| Case open (the reveal strike) | −4 | −18 LUFS |
| Selection lock, box full open | −6 | −20 LUFS |
| Purchase confirmed, notifications | −8 | −22 LUFS |
| Box crack, box select, vault lock, delivery requested, payment failed | −10 to −14 | −24 to −28 LUFS |
| Success, error, add to cart | −14 to −16 | −28 to −30 LUFS |
| Cycle passes | −16 rising to −10 across the cycle | −30 → −24 LUFS |
| Harmonic bed | −18, ducking to −24 under payoffs | −32 / −38 LUFS |
| UI taps, toggles, tabs, sheets, back, refresh | −20 to −22 | −34 to −36 LUFS |
| Empty state, disabled | −24 to −26 | −38 to −40 LUFS |
| Loading loop | −28 | −42 LUFS |

Only 2 LU separates each tier. Tiers escalate in weight, layers and length (Section 5), not in loudness.

---

## 2. Design rules as requirements

| # | Rule | Requirement | How it is verified |
|---|---|---|---|
| R1 | One sonic family | Every asset has a Steel, Sapphire or Cloth core (1.1). Every pitched asset is in E major (1.2). Designed layers never appear alone. | Asset review against the source-material log; spectral check for out-of-key partials. |
| R2 | Short | All UI-family sounds ≤ 150 ms to −40 dB. Only the open sequence and purchase confirmed exceed it. | Automated duration check on delivery. |
| R3 | Tension from pitch and rhythm, not volume | The cycle rises no more than 6 LU end to end. Its tension comes from an accelerating pass rate and a pentatonic sweep that stops one note short and is resolved by the lock (4.3). | Level plot of the cycle; listening test. |
| R4 | Frequency separation | UI assets high-passed at 800 Hz, no sustained energy below 1.2 kHz. Payoff body between 250 Hz and 1.2 kHz. | Spectrogram check per asset. |
| R5 | Repetition safety | Every sound heard more than three times per typical session has round-robin variants, pitch or velocity variation, and a rapid-repeat volume taper (Section 6). | Runtime rules in the audio manager; session-log check. |
| R6 | Survives a phone speaker | Every asset remains identifiable with a 300 Hz high-pass applied and played from a phone speaker at arm's length at 50 % volume (Section 9). | Device protocol, signed off per asset. |
| R7 | Nothing sounds like a slot machine | No click-transient pass sounds, no decelerating tick train, no reel stop, no coin cascade, no near-miss audio, no jackpot fanfare ladder, no casino bed music (Section 10). The cycle accelerates and snaps. | Exclusion checklist plus a naive-listener test. |
| R8 | The top tier stays special | Tier-4 audio is never played outside a genuine tier-4 open or the owner's own vault replay of it (5.3). | Code review of every call site for the T4 asset IDs. |
| R9 | Honest tells | The tier tell at the partial open is a deterministic function of the actual tier. Cycle passes are uniform and carry no tier information. No probabilistic or "could be either" state exists (4.4). | Code review; the tell is selected from the resolved outcome, never from a random draw. |
| R10 | Silence is a design choice | Navigation that does not change state (scrolling, focus, hover) is silent. Errors are quieter than successes. | Trigger map review. |

---

## 3. Master inventory

Columns: **ID** · **Trigger** · **Duration (ms)** · **Character** · **Pitch relationship** · **Level (LU vs anchor)** · **Interruptible** · **Haptic (iOS / Android)** · **Variants**

"Interruptible: cut" means a new trigger stops it instantly. "Fade" means a new trigger fades it over the stated time. "No" means it always plays to completion.

### 3.1 UI

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `ui_tap` | Any primary or secondary button press, list row select | 40 | Bracelet-link tick with an 8 ms designed glint on top. Dry, tiny, bright. | Unpitched core; glint at E7 | −22 | Cut | Light impact / `CLOCK_TICK` | 4 round-robin, ±20 cents |
| `ui_toggle_on` | Switch or checkbox to on | 60 | Clasp half-click with a short bright ping | E6 ping | −20 | Cut | Rigid light / `CONTEXT_CLICK` | 3 |
| `ui_toggle_off` | Switch or checkbox to off | 50 | Same clasp, damped, lower ping | B5 damped | −20 | Cut | Soft light / `CLOCK_TICK` | 3 |
| `ui_tab` | Tab bar or segmented control change | 55 | Cloth brush with a steel tick and a glint inside it | Unpitched; glint at B7 | −22 | Cut | Selection / `CLOCK_TICK` | 4, ±20 cents |
| `ui_sheet_open` | Bottom sheet or modal presents | 120 | Tissue lifting with a soft designed air sweep rising | Noise rising toward E6 region | −20 | Fade 30 | Soft medium / `PRIMITIVE_TICK` | 3 |
| `ui_sheet_close` | Sheet or modal dismisses | 100 | Tissue settling, air sweep falling | Noise falling from E6 region | −22 | Fade 30 | None | 3 |
| `ui_back` | Back navigation (button or edge swipe completes) | 70 | Steel tick, slightly lower than `ui_tap`, glint falling | B5 damped | −22 | Cut | None | 3 |
| `ui_error` | Inline validation fails, action rejected | 140 | Damped steel stop with a low designed thud under it and a slight downward bend | Unpitched, bend from ~B4 downward | −14 | No | Notification error / `REJECT` | 2 |
| `ui_success` | Inline success not covered by a commerce or vault sound (saved, copied, verified) | 140 | Two quick sapphire notes with a tiny sparkle tail | E5→B5 | −14 | No | Notification success / `CONFIRM` | 2, ±10 cents |
| `ui_disabled` | Press on a disabled control | 30 | Dull damped tick. Nothing moves. | Unpitched, ~1 kHz | −26 | Cut | None by default (optional rigid light) | 2 |

### 3.2 Commerce

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `com_add_to_cart` | Pack added to cart or bag | 90 | Clasp half-click plus one soft sapphire note with a short glint | G♯5 | −16 | Cut | Medium impact / `PRIMITIVE_CLICK` | 2 |
| `com_purchase_confirmed` | Payment authorised; confirmation screen appears | 450 | Two clear sapphire notes with a brief high shimmer. Confident, not celebratory. | E5→B5, shimmer at E6 | −8 | No | Two transients 120 ms apart, intensity 0.7 then 1.0, sharpness 0.6 (Core Haptics / `Composition`: CLICK, CLICK) | 1 |
| `com_payment_failed` | Payment declined or errored | 220 | Heavier `ui_error`: clasp refuses, low thud, damped settle | Unpitched, bend downward, no tonal centre | −12 | No | Notification error / `REJECT` | 1 |

### 3.3 The open sequence

Detailed in Section 4. The six client-named moments are marked ★.

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `open_box_select` ★ | The button pressed when the box is chosen | 120 | A weighted press: clasp click core, a short designed body, a soft tonal confirm. Heavier than `ui_tap`; this one commits. | E5 glint | −12 | No | Medium impact then a light echo at +80 ms / `PRIMITIVE_CLICK`, `PRIMITIVE_TICK` | 3 |
| `open_box_enter` | Box animates to centre and comes to rest (skip if already centred) | 500 | Box sliding on cloth, set down on wood and leather. Soft knock with a designed low body. | Unpitched; knock around E3–E4 | −14 | No | Soft heavy transient at set-down (0.6, sharpness 0.2) / `PRIMITIVE_THUD` | 2 |
| `open_bed` | Starts at the box crack; runs to the end of settle | Loop, 8000 per cycle | Warm pad: bowed sapphire drone with a soft designed pad under it, root and fifth. A room with a glow. | E3 + B3 (headphone body), E4 + B4 (speaker-audible) | −18, ducks to −24 during payoffs | Fade 400 | None | 1 loop, seamless |
| `open_box_crack` ★ | Box partially opens: lid lifts a few degrees, light spills | 450 | Magnetic clasp release, a leather hinge taking weight, a thin band of designed light tone rising under it. The tease. | Rising glint E4→G♯4 | −12 | No | Soft continuous 200 ms, intensity 0.3, then a light transient at the clasp release | 2 |
| `open_tell_t2` | Layered on `open_box_crack` when the outcome is tier 2 | 450 | One added sapphire note in the spilled light | B4 | −12 | No | Continuous extends to 250 ms, 0.4 | 1 |
| `open_tell_t3` | Layered on `open_box_crack` when the outcome is tier 3 | 600 | The light gains the major-seventh shimmer and a soft sparkle tail | D♯5 shimmer | −10 | No | Continuous extends to 300 ms, 0.5 | 1 |
| `open_tell_t4` | Follows `open_box_crack` when the outcome is tier 4 | 400 | **Silence.** The bed does not start. The crack is followed by 400 ms of nothing before the full open. | None | Silence | No | Continuous 300 ms, 0.3, then nothing | Logic, no asset |
| `open_box_open` ★ | Box fully opens: lid swings to rest | 600 | Air rushing out as the lid swings, a resonant designed "open" tone, the lid settling on its stop with a soft steel tick. Tier 4 uses a deeper, wider variant. | Open tone E4 with a fifth; T4 variant adds E3 body | −6 | No | Transient 0.8, sharpness 0.4, then soft continuous 300 ms / `PRIMITIVE_THUD`, `PRIMITIVE_SLOW_RISE` | 2 + 1 tier-4 variant |
| `open_cycle_pass` ★ | Each watch passing through the frame during the cycle | 60–90 | An air-and-tone flip: a short cloth pass with a small glass glint. **No click transient.** Uniform across items; the glint steps up the scale as the cycle proceeds. | Glint steps E5, F♯5, G♯5, B5, C♯6, then holds C♯6 (one short of E6) | −16 rising to −10 | Cut (per-item) | Light transient per pass, intensity 0.25→0.5 following the rate / `PRIMITIVE_TICK`; or `SLOW_RISE` on devices where per-event latency is poor | 6 pitch steps × 2 = 12 |
| `open_cycle_blur` | Final 400 ms of the cycle when passes exceed ~12 per second | 400 | Passes merge into one continuous rising shimmer; filtered noise sweeps up with it | Sweep resolving toward E6, arriving as the lock lands | −10 | No | Continuous 400 ms, 0.4→0.7 / `QUICK_RISE` | 1 |
| `open_select_lock` ★ | The final watch is selected; the cycle stops instantly | 250 | A mechanism locking: steel latch core, a light sub thump under a 250–400 Hz knock, a clean tonic glint. Decisive. **Identical for every tier.** | E5 glint; knock in the E3–E4 region | −6 | No | Transient 1.0, sharpness 0.8 / `PRIMITIVE_CLICK` at full scale | 3, ±10 cents |
| `open_case_open` ★ | The selected watch's presentation case opens: the reveal | 500 | Case hinge and air, then the sapphire strike as the crystal catches light, with a designed shimmer tail. The payoff carrier. | Strike E5 | −4 | No | Transient 1.0, sharpness 0.7, then payoff haptics | 3, ±10 cents |
| `open_payoff_t1` | Layered from the strike, tier 1 | 700 | The strike's ring with a short sparkle tail. Nothing more. | E5 decaying | −6 | Skip after 40 % → 200 ms fade to settle | None beyond the strike | 2 |
| `open_payoff_t2` | Layered from the strike, tier 2 | 1200 | A second sapphire note answers the strike; sparkle tail lengthens; bed swells gently | E5→B5 | −4 | Skip after 40 % → 200 ms fade | One echo transient at +150 ms, 0.5 | 2 |
| `open_payoff_t3` | Layered from the strike, tier 3 | 2000 | Three-note rising figure over a soft sub thump, then a separate afterglow chime at +600 ms. Bed holds the major-seventh colour. A short designed stinger, not a fanfare. | E5→G♯5→B5, afterglow E6 | −2 | Skip after 40 % → 300 ms fade | Double echo (+150, +300 ms; 0.5, 0.4) then 400 ms continuous decay | 1 |
| `open_payoff_t4` | Layered from the strike, tier 4 | 3500 | Out of the silence: the strike, a large low sapphire bell under it with a sub thump, the four-note figure to the high octave, held, with a long sparkle tail. A wide post-bed enters and stays through the settle. The one true stinger in the app. | Strike E5; low bell E4 at +50 ms; figure E5→G♯5→B5→E6; post-bed E major add 9 with D♯ | 0 (anchor) | Skip only after 1000 ms → 500 ms fade | Continuous 1200 ms swell from +250 ms, 0.3→0.9→0, sharpness 0.2 / `SLOW_RISE` then `QUICK_FALL` | 1 |
| `open_bed_t4_post` | Begins with `open_payoff_t4`; runs through settle | Loop, 12000 per cycle | The room after the bell. Wide, slow, warm. Never heard anywhere else. | E major add 9 with D♯ | −16, fading through settle | Fade 800 | None | 1 |
| `open_settle` | Payoff ends | 1000 | Bed fades out. One last soft cloth movement. Room tone, then silence. | Unpitched | −16 fading to silence | Fade 200 | None | 2 |

### 3.4 Vault and fulfilment

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `vault_added` | Item committed to vault | 300 | Deployant clasp closing fully with a designed lock body, then one short sapphire note | E5 | −10 | No | Rigid medium / `PRIMITIVE_CLICK` + `PRIMITIVE_LOW_TICK` | 2 |
| `ship_requested` | Delivery request confirmed | 350 | Cloth folding (the box being wrapped) and one soft sapphire note | G♯5 | −12 | No | Notification success / `CONFIRM` | 1 |
| `notif_shipped` | Push: item shipped (also in-app if foregrounded) | 500 | Two rising sapphire notes with a light sparkle | E5→G♯5 | −8 | No | System notification haptic | 1 |
| `notif_delivered` | Push: item delivered | 700 | Three rising sapphire notes to the high octave. The arrival. | E5→B5→E6 | −8 | No | System notification haptic | 1 |

### 3.5 System

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `sys_notification` | Any push not covered above; in-app banner | 400 | Two sapphire notes struck together, short, with a glint | E5 + B5 dyad | −8 | No | System notification haptic | 1 |
| `sys_refresh_threshold` | Pull-to-refresh crosses the trigger threshold | 50 | Single steel tick with a glint | B5 | −22 | Cut | Light impact at threshold / `CLOCK_TICK` | 3 |
| `sys_refresh_complete` | Refresh finishes and content settles | 90 | Brighter steel tick | C♯6 | −20 | Cut | None | 3 |
| `sys_loading_loop` | Any load exceeding 800 ms | Loop, 4000 seamless | A mechanical movement ticking at 8 beats per second, very quiet, high-passed. A watch running while you wait. | Unpitched; tick ~3.2 kHz, tock ~2.9 kHz | −28 | Fade 200 on completion; auto-fades after 20 s | None | 1 loop from 2 tick and 2 tock samples |
| `sys_empty_state` | Empty state view first renders | 200 | Soft cloth hush, once | Unpitched | −24 | Fade 50 | None | 2 |

**Count:** 38 event IDs (37 carry audio; the tier-4 tell is logic), 3 loops, and roughly 110 audio files once round-robin variants and velocity layers are included. `audit/library-structure.md` enumerates them.

---

## 4. The open sequence

The only place in the product where sound is allowed length. It has to deliver the game-like satisfaction of the client's references without a single casino cue.

### 4.1 The six moments

| # | Client's moment | Asset | What the sound is doing |
|---|---|---|---|
| 1 | A button being pressed when the box is chosen | `open_box_select` | Commitment. Heavier than any other button in the app. |
| 2 | A box being partially opened | `open_box_crack` (+ `open_tell_*`) | The tease, and the honest tier tell: the spilled light is tinted and voiced by tier. |
| 3 | A box being fully opened | `open_box_open` | Release. Air, a resonant open, the lid settling. Launches the cycle. |
| 4 | Watches cycling through | `open_cycle_pass` ×N, `open_cycle_blur` | Tension by rate and pitch. Accelerates to a blur. Uniform per item. |
| 5 | Final watch being selected | `open_select_lock` | The snap. Instant, mechanical, decisive, identical for every tier. |
| 6 | A watch case being opened | `open_case_open` (+ `open_payoff_t*`) | The reveal. Hinge, air, the strike, the tier payoff. |

The client listed the watch case first. This spec places it last, as the climax, because the audit shows the shareable unit is the final reveal. If the product also opens a case at the start of the flow (for example, the pack shelf presented inside a case), `open_case_open` variant 1 at −10 LU serves that moment without its payoff layers.

### 4.2 Timeline, auto mode

Times in ms from the box-select press. Auto mode runs everything from that single press.

| Time | Event | Asset | Note |
|---|---|---|---|
| 0 | Box chosen | `open_box_select` | Press with echo haptic |
| 300 | Box centres (if needed) | `open_box_enter` | Slide and set-down |
| 900 | Partial open | `open_box_crack` + tier tell | Light spills; T2 adds B4, T3 adds D♯5 shimmer, T4 is followed by 400 ms silence |
| 900 | Bed fades in over 400 ms (T1–T3) | `open_bed` | −18 LU. Not for T4. |
| 1500 (T4: 1900) | Full open | `open_box_open` | Air, open tone, lid settles. T4 variant deeper. |
| 1900 (T4: 2300) | Cycle begins | `open_cycle_pass` | 5 passes/s, glint E5 |
| +500 | | | 8 passes/s, glint F♯5 |
| +1000 | | | 11 passes/s, glint G♯5 |
| +1400 | | | 13 passes/s, glint B5 |
| +1700 | | | 15 passes/s, glint C♯6 |
| +2000 | Blur | `open_cycle_blur` | Passes merge; sweep toward E6 |
| +2400 (4300; T4: 4700) | Selection | `open_select_lock` | Instant stop. Cycle audio hard-cuts with a 5 ms fade. E5. |
| +300 (4600; T4: 5000) | Pause | | Near-silence. The selected watch sits in frame. |
| 4600 (T4: 5000) | Case opens | `open_case_open` | Hinge, air, strike |
| 4600 | Payoff | `open_payoff_t1…t4` | Layered from the strike |
| 5200 | Tier 3 afterglow | (within `open_payoff_t3`) | E6 chime |
| 5300 / 5800 / 6600 / 8500 | Payoff ends, T1 / T2 / T3 / T4 | | |
| +1000 | Settle ends | `open_settle` | Bed gone. Item card interactive. |

Totals from the press to interactive: **T1 ≈ 6.3 s, T2 ≈ 6.8 s, T3 ≈ 7.6 s, T4 ≈ 9.5 s.** The cycle itself is 2.4 s, shorter than a CS:GO reel, and skippable (4.6).

### 4.3 The cycle: accelerate and snap

This is where the client's references and the brief's bans meet, so it is specified tightly.

**What the references do.** A horizontal reel decelerates over five to six seconds with a click per item, lands with a stop, and shows the neighbours of the winner. The click train and the landing are the two cues regulators and the research literature identify with slot machines, and the brief prohibits reel-stop clicks and near-miss audio.

**What GemBreak does instead.**
- **Passes are flips, not ticks.** Each watch passing the frame plays `open_cycle_pass`: a short cloth pass with a glass glint. There is no click transient anywhere in the pass sound. It reads as objects moving past, not pegs on a wheel.
- **Passes are uniform.** Every pass sound is the same family regardless of what watch is on screen. No tier information is in the cycle. Combined with the honest tell at the crack, there is nothing for a near-miss to attach to.
- **The rate accelerates.** From 5 passes per second to 15 over 2 s, then a 400 ms blur where individual passes merge into one rising shimmer. The cycle never slows.
- **The pitch rises and stops one note short.** The glint steps E5, F♯5, G♯5, B5, C♯6 as the rate rises. C♯6 is held through the blur; the ear is waiting for E6. The lock lands on E5, the tonic, and the case-open strike confirms it. The tension in the brief's words: rising pitch and accelerating rhythm, resolving on the reveal.
- **The stop is a snap.** `open_select_lock` fires and the cycle audio hard-cuts. No deceleration, no last-three-ticks, no landing.
- **The winner's neighbours carry no audio.** Whatever the visual shows beside the selected watch, the sound has already stopped. The visual team should avoid showing a higher-tier watch adjacent to the selection; that is a product rule this spec supports but cannot enforce.

**What the named references actually document.** Rips by Triumph's only described cue is that "the reveal makes a knocking sound and brief vibration": one foley transient synchronised to a haptic, which is exactly what `open_select_lock` is. PackDraw and Skin.Club are reel flows; the clone codebases that imitate them show the polish comes from a layered stinger (transient, detuned tonal partials staggered by tens of milliseconds, a short high-passed air tail), a deliberate hold of about a second before the result, small per-tier steps in gain and length, and a rule that nothing else plays over the stinger. Valve's own event tables give reveal sounds an instance limit of one and block the inspect click for a second. All of that is adopted here; the tick and the landing are not.

**If product insists on a decelerating cycle.** This spec does not recommend it. If it is adopted anyway, three conditions hold: pass sounds remain click-free flips, the final 500 ms of the deceleration is silent (no per-item audio at all as the cycle slows), and the selection is still marked by `open_select_lock` rather than a stop sound. Even so, the naive-listener test in Section 10 must pass.

### 4.4 The tell: honest by construction

The tier tell fires at the partial open, before the cycle. Three rules:

1. The tell is selected from the **resolved outcome**. The tier is known before the sequence begins. No random draw at tell time, no ambiguous state.
2. Each tier has exactly one tell. Tier 1 is the bare crack. Tier 2 adds one note in the light. Tier 3 adds the major-seventh shimmer. Tier 4 is followed by silence, and its bed never starts. Silence is the rarest thing in the app, so silence is the top tell.
3. No tell is ever followed by a different tier's payoff. A code-level assertion fails the build if `open_tell_tN` is followed by `open_payoff_tM` with M ≠ N.

Placing the tell before the cycle splits the curiosity in two: the crack answers "how good", the cycle and case answer "which watch". Tier and identity are revealed by different moments, which keeps the cycle interesting after an honest tell.

### 4.5 Interaction

- The sequence is tap-driven from `open_box_select`. Everything after the press runs automatically.
- **Optional hold-to-crack.** If product wants a tactile tease, a press-and-hold on the box plays `open_box_crack` while held and `open_box_open` on release. Releasing early closes the lid with `ui_sheet_close` and returns to the pre-press state. The tell fires at the crack either way.
- If the app is backgrounded mid-sequence, all sound stops immediately. On return the sequence restarts from `open_box_crack`. No catch-up audio.

### 4.6 Skipping

- During the cycle: a tap jumps to `open_select_lock` immediately. The outcome is already fixed, so skipping costs nothing and there is no reason to withhold it. This is the equivalent of the references' "fast open", offered on request rather than as a mode.
- After the lock, tiers 1 to 3: a tap skips to `open_settle` once 40 % of the payoff has played, fading over 200–300 ms.
- After the lock, tier 4: skip is available only after 1000 ms, fading over 500 ms.
- **Quick open** (setting, default off) shortens the cycle to 800 ms and removes the 300 ms pause. Nothing else changes.
- Rapid re-fire is not possible. A new open cannot begin until the previous settle has finished or been skipped, and the next box must be chosen explicitly. No "open 4" row, no auto-open queue.

### 4.7 Replays

The vault replays an open with the same audio, including tier 4, starting from `open_box_crack` in auto mode, skippable at any point after the lock. Replays are the owner's own memory, so tier-4 exclusivity is not diluted.

---

## 5. The rarity ladder

### 5.1 Tier mapping

Four sonic tiers. If the product has three tiers, drop T2; if five, T4 still maps to the rarest tier and the two middle product tiers share T2 and T3.

| Sonic tier | Suggested label | Product tier | Intended frequency |
|---|---|---|---|
| T1 | Standard | Base outcomes | Most opens |
| T2 | Select | Above-base outcomes | Regular but noticed |
| T3 | Reserve | High-value outcomes | Occasional; a session event |
| T4 | Grail | The rarest outcomes | Rare enough to stay special. Recommendation: no more than one in two hundred opens app-wide. If the product's top tier is more common, map T4 to a rarer sub-tier or a defined "grail" class. |

Labels are watch-collector language. The product owns final naming.

### 5.2 Escalation by weight, layers and length

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Tell at the crack | Bare crack | +B4 in the light | +D♯5 shimmer, sparkle tail | 400 ms silence follows; bed never starts |
| Full open | Standard | Standard | Standard | Deeper, wider variant |
| Cycle and lock | Identical | Identical | Identical | Identical |
| Case open strike | E5, identical | E5, identical | E5, identical | E5, identical |
| Payoff figure | E5 decays | E5→B5 | E5→G♯5→B5, afterglow E6 | E5→G♯5→B5→E6 held; low bell E4 under |
| Designed layers | Short sparkle | Longer sparkle, bed swell | Sub thump, short stinger, sparkle | Sub thump, low bell, long sparkle, post-bed |
| Payoff length | 700 ms | 1200 ms | 2000 ms | 3500 ms |
| Level | −6 | −4 | −2 | 0 |
| Lowest fundamental | E5 | E5 | E5 with sub under | E4 with sub under |
| Haptic | Strike only | Strike + one echo | Strike + double echo + 400 ms decay | Strike + 1200 ms swell |
| Variants | 2 | 2 | 1 | 1 |

Each step adds one note, one layer and one haptic element. None adds a fanfare, a counter, a cascade or a loop.

### 5.3 Keeping tier 4 special

- `open_tell_t4` logic, the T4 variant of `open_box_open`, `open_payoff_t4` and `open_bed_t4_post` are played by exactly one code path: a genuine tier-4 open or the owner's own vault replay of one.
- They are never used in onboarding, tutorials, demo packs, marketing screens, app-store previews, push notifications, social or activity feeds, "someone just pulled" surfaces, or A/B tests of other features.
- Any demo or tutorial open resolves at T1.
- T4 assets are not shipped in any preview build that can be captured for marketing without the product lead's sign-off.

---

## 6. Repetition and variation

| Mechanism | Applies to | Rule |
|---|---|---|
| **Round-robin** | All UI, `open_box_select`, `open_cycle_pass` (2 per pitch step), `open_select_lock`, `open_case_open`, `sys_refresh_*`, T1 and T2 payoffs | Variants cycle in a shuffled order with no immediate repeat. |
| **Pitch variation** | Steel and cloth cores (unpitched) | ±20 cents random per trigger. |
| | Sapphire and designed glints (pitched) | ±10 cents random per trigger. Never applied to the cycle's pitch steps, the lock, or the T3 and T4 figures, which stay exactly in tune with the bed. |
| **Velocity layers** | `ui_tap`, `ui_toggle_*`, `open_select_lock`, `open_case_open`, `vault_added` | Two dynamic layers per variant; the manager picks by a random 0.8–1.0 velocity. |
| **Rapid-repeat taper** | All UI-family sounds | Same ID more than three times within 2 s: each further trigger 3 dB quieter, floor −9 dB. Recovers after 1.5 s idle. |
| **Voice limit** | UI family | Maximum two UI voices at once; a third steals the oldest. Open-sequence events and the bed are never stolen. Cycle passes are capped at three overlapping voices; older passes fade in 20 ms. |
| **Reveal exclusivity** | `open_select_lock`, `open_case_open`, `open_payoff_*` | Instance limit of one. UI-family sounds are suppressed from 100 ms before the lock until 1000 ms after the case-open strike so nothing plays over the reveal. |
| **Rate limits** | `sys_notification` in-app | At most once per 60 s. |
| | `sys_empty_state` | At most once per 30 s per screen. |
| | `sys_loading_loop` | Starts after 800 ms of loading; fades to silence after 20 s; restarts only on a new load. |
| **Session decay** | Open sequence | None. The reveal stays whole by default and is skippable on request (4.6). |

---

## 7. Haptic mapping

Principles from the audit's Apple sources: haptic and audio are two instruments playing the same tempo; sync within 10 ms; prepare generators before the gesture; the haptic may lead the sound, never lag it; a haptic that is not obviously caused by something the user did or saw is removed.

| Event | iOS | Android (API 31+) | Android fallback |
|---|---|---|---|
| `ui_tap` | `UIImpactFeedbackGenerator(.light)` | `HapticFeedbackConstants.CLOCK_TICK` | `VibrationEffect.createOneShot(8, 40)` |
| `ui_toggle_on` | `.rigid`, intensity 0.6 | `CONTEXT_CLICK` | one-shot 10 ms |
| `ui_toggle_off` | `.soft`, intensity 0.5 | `CLOCK_TICK` | one-shot 8 ms |
| `ui_tab` | `UISelectionFeedbackGenerator` | `CLOCK_TICK` | one-shot 6 ms |
| `ui_sheet_open` | `.soft`, intensity 0.5 | `Composition: PRIMITIVE_TICK` | one-shot 10 ms |
| `ui_error`, `com_payment_failed` | `UINotificationFeedbackGenerator(.error)` | `REJECT` | waveform [0,30,40,30] |
| `ui_success`, `ship_requested` | `.success` | `CONFIRM` | waveform [0,20,60,20] |
| `com_add_to_cart` | `.medium` | `Composition: PRIMITIVE_CLICK` (0.7) | one-shot 15 ms |
| `com_purchase_confirmed` | Core Haptics: two transients at 0 and 120 ms, intensity 0.7 / 1.0, sharpness 0.6 | `Composition: CLICK (0.7), CLICK (1.0) delay 120` | waveform [0,20,100,30] |
| `open_box_select` | `.medium` then `.light` at +80 ms | `PRIMITIVE_CLICK` (0.8), `PRIMITIVE_TICK` delay 80 | waveform [0,20,60,10] |
| `open_box_enter` (set-down) | Core Haptics transient, 0.6, sharpness 0.2 | `PRIMITIVE_THUD` | one-shot 25 ms, amplitude 150 |
| `open_box_crack` + tell | Continuous 200–300 ms, 0.3–0.5, sharpness 0.1, then a light transient at the clasp release | `PRIMITIVE_LOW_TICK` then `PRIMITIVE_TICK` | one-shot 12 ms |
| `open_box_open` | Transient 0.8, sharpness 0.4, then continuous 300 ms, 0.3 | `PRIMITIVE_THUD`, `PRIMITIVE_SLOW_RISE` | one-shot 30 ms, amplitude 180 |
| `open_cycle_pass` | Core Haptics transient per pass, 0.25→0.5 following the rate, sharpness 0.6, generated at runtime | `Composition` of `PRIMITIVE_TICK` per pass; or `PRIMITIVE_SLOW_RISE` for the whole cycle where per-event latency is poor | waveform with rising density |
| `open_cycle_blur` | Continuous 400 ms, 0.4→0.7 | `PRIMITIVE_QUICK_RISE` | one-shot 200 ms, amplitude 100 |
| `open_select_lock` | Transient 1.0, sharpness 0.8 | `PRIMITIVE_CLICK` (1.0) | one-shot 30 ms, amplitude 255 |
| `open_case_open` | Transient 1.0, sharpness 0.7 | `PRIMITIVE_CLICK` (1.0) | one-shot 30 ms, amplitude 255 |
| `open_payoff_t2` echo | Transient +150 ms, 0.5 | `PRIMITIVE_TICK` | none |
| `open_payoff_t3` | Transients +150 / +300 ms (0.5, 0.4), then continuous 400 ms, 0.4→0 | `TICK, TICK, QUICK_FALL` | none |
| `open_payoff_t4` | Continuous 1200 ms from +250 ms, 0.3→0.9→0, sharpness 0.2 | `SLOW_RISE` then `QUICK_FALL` | one-shot 400 ms, amplitude 120 |
| `vault_added` | `.rigid`, intensity 0.8 | `PRIMITIVE_CLICK` + `PRIMITIVE_LOW_TICK` | one-shot 20 ms |
| `sys_refresh_threshold` | `.light` at threshold | `CLOCK_TICK` | one-shot 8 ms |
| Notifications | System | Notification channel default | System |
| Everything else | None | None | None |

Rules:
- Call `prepare()` on iOS generators, and warm the Android vibrator, when the finger lands on a control that will fire a haptic, not when it fires.
- Check `Vibrator.areAllPrimitivesSupported()` on Android at launch and select the fallback column per device once.
- Haptics obey a separate "Haptics" toggle (8.3) and the system's haptic settings. When haptics are off, nothing in the audio changes.
- No haptic fires while the device is face down on a surface if that state is detectable.

---

## 8. Platform behaviour

### 8.1 Audio session and mixing

- **iOS:** `AVAudioSession` category `.ambient`. App sounds obey the ring/silent switch, mix with the user's own music or podcast, and never duck it. Apple classes app sound effects as nonessential. If product decides the reveal should play in silent mode, that is a deliberate exception to Apple's guidance and needs a product-level decision; this spec does not recommend it.
- **Android:** UI and reveal sounds through a low-latency engine (SoundPool or Oboe) with `AudioAttributes` usage `USAGE_GAME` and content type `CONTENT_TYPE_SONIFICATION`, following media volume and mixing with other apps. Suppress all app sounds when `AudioManager.ringerMode` is silent or vibrate so the platforms behave alike. Notifications go through notification channels with the custom sounds attached.
- The harmonic bed never claims audio focus.

### 8.2 Latency and sync

- Preload every UI-family asset and the whole open-sequence set at launch. Each UI asset is under 100 KB; the open set is under 4 MB decoded.
- Target audio start within 12 ms of the trigger. Fire the haptic on the same frame as the audio call.
- Cycle passes are scheduled from the animation clock so that pass audio, pass haptic and the on-screen watch line up; the audio engine receives the pass timestamps ahead of time rather than reacting to frames.

### 8.3 Settings exposed to the user

Two toggles, both default on, in the app's settings and reachable from the open screen's overflow menu:

- **Sounds.** Master toggle for every app sound including the open sequence and bed. Notification sounds are governed by the OS.
- **Haptics.** Master toggle for every app haptic.

One additional option: **Quick open**, default off. Shortens the cycle to 800 ms and removes the post-lock pause. Tell, lock, strike and payoffs are unchanged. The relief valve for the fiftieth open, offered rather than forced.

### 8.4 Interruptions and lifecycle

- Incoming call, Siri, or another app taking audio focus: all app sounds stop. Nothing resumes on return; the open sequence restarts from `open_box_crack`.
- App backgrounded: stop everything immediately, including the loading loop.
- Low Power Mode: no change to audio; haptics reduce to the lock, the case-open strike and the purchase confirmation.

### 8.5 Accessibility

- **VoiceOver / TalkBack running:** suppress the UI family, keep commerce, vault, notification and open-sequence sounds, and duck them 6 dB while the screen reader is speaking.
- **Reduce Motion:** the cycle's per-pass haptics are replaced by the single `open_cycle_blur` continuous event; Quick open is suggested on first run; sounds are unchanged.
- **Every sound has a visual twin.** No state is communicated by sound alone.

---

## 9. Phone-speaker verification protocol

The set is mixed for phone speakers and checked on them. Headphones are for authoring, not sign-off.

1. **Authoring pre-check.** Monitor every asset through a 300 Hz high-pass and a −6 dB shelf above 8 kHz, in mono. If an asset loses its identity, fix the asset, not the filter. Sub layers on the lock and the top two payoffs must be accompanied by a 250–400 Hz component that carries the weight on a speaker.
2. **Reference devices.** A current base-model iPhone, a mid-range Android with a single bottom-firing speaker, and one Android at least four years old. Add a stereo-speaker device to check nothing depends on width.
3. **Conditions.** Each device at 50 % volume in a quiet room at arm's length; at 100 % in a noisy room (café-level, around 65 dB A); face up on a table; face down on a table. The lock, the case open and the purchase confirmation must be identifiable in all four. UI sounds must be identifiable in the first two.
4. **Screen recording.** Record a full T1 open and a full T4 open with the OS screen recorder on each device. Play the recordings back on another phone's speaker. The lock, the strike and the tier difference must survive.
5. **Sign-off.** Each asset ID gets a pass on each device, logged. No asset ships on a fail.

---

## 10. Slot-machine exclusion

| Prohibited | Why | GemBreak's alternative |
|---|---|---|
| Click-transient pass sounds during a cycle | The CS:GO reel tick; named by regulators as the slot signature | Passes are air-and-tone flips with no click |
| Any cycle that decelerates to a stop | The landing reel | The cycle accelerates to a blur and snaps |
| A "stop" or "landing" sound | Reel stop | `open_select_lock`, a mechanism locking, identical for all tiers |
| A hush during a spin before it stops | Slot suspense beat | The only silences are T4's tell (before the cycle, after a deterministic outcome) and the 300 ms pause after the lock (after the outcome is on screen) |
| Tier-coded pass sounds or any audio hinting at a tier the user did not get | Near-miss; Zendle et al. | Passes are uniform; the tell is a pure function of the resolved tier |
| Coin cascades, cash counters ticking up, Plinko drops | Coin Master, Monopoly Go | Value is shown, not rained |
| A second spinner, "jackpot", "upgrade" or "double or nothing" moment | HypeDrop, battle sites | None exists |
| Per-tier loudness escalation, sparks-and-fire fanfares, klaxons | Key-Drop, Whatnot host layer | 2 LU per tier; escalation by note, layer and length; one short stinger at T4 |
| Rapid re-fire, auto-open, mass open, "open 4" | KSA "rapid successive opening" | One open at a time; next box chosen explicitly; skip on request |
| Casino or slot-lobby bed music | Coin Master village themes | A warm pad at −18 LU that behaves like a room |

**Naive-listener test.** Before sign-off, play the full auto-mode open at T1 and T3 to five people who have not seen the app, on a phone speaker, without the screen. Ask what they think it is. If any of the five says "slot machine", "casino", "roulette", "spin" or "jackpot", the sequence is redesigned before shipping. Because the cycle is the most exposed element, run this test on the cycle alone as well as on the full sequence.

---

## 11. Decisions this spec assumes

1. **The flow is the client's six moments in this order:** box chosen, partial open, full open, cycle, selection, case open. The watch case is placed last as the climax (4.1).
2. **Four sonic tiers.** Mapping rules in 5.1 handle three or five product tiers.
3. **The cycle accelerates and snaps.** A decelerating cycle is not recommended; conditions for it are in 4.3.
4. **The tell lives at the partial open**, before the cycle, and the cycle is uniform.
5. **A harmonic bed exists during the open sequence only.** No app-wide music.
6. **Silent switch is respected everywhere**, including the reveal.
7. **E major.** Changing the key changes every asset.
8. **Recorded cores with designed layers.** The sourcing plan shows that the sapphire set and the tier stingers must be commissioned; steel, cloth and most designed sweeteners can be sourced and processed.
