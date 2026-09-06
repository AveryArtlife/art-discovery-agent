# GemBreak Sound Design — Phase 2: Sound Specification

**Version:** 1.2
**Status:** Phase 2 deliverable, revised on client direction during Phase 3. Built on `audit/competitor-audit.md`. Feeds `audit/sourcing-plan.md`, `audit/library-structure.md` and `audit/licenses.csv`.
**Date:** 2026-09-06
**Scope:** Every sound GemBreak ships, with trigger, duration, character, pitch relationship, loudness, interruptibility and haptic pairing, plus the rules that make them one product.

### Change log

**1.2 (this version).** Client direction after reviewing the sourcing candidates: the recorded-material candidates read as "too authentic"; the set should sound like opening a loot box in a video game, and the cycle should sound like scrolling through item options in a game or casino. Changes from 1.1:

- The palette is now **designed-first**. The Designed layer is the voice of the set; Steel, Sapphire and Cloth become recorded accents layered into designed sounds so the product still sounds like a watch app rather than a generic game.
- The cycle's default mode is a **classic decelerating item scroll with a per-item tick**, the grammar of CS:GO cases, prize wheels and item roulettes. The client has confirmed this twice, which lifts the original brief's line on reel-stop clicks. The v1.1 accelerate-and-snap remains as an alternative mode. Guardrails that remain: ticks carry no tier information, the stop is a lock rather than a slot reel stop, the hush before the stop is short, and there is no second spin.
- Open-sequence characters are rewritten in game terms: charge-ups, energy release, sparkle bursts, stingers with sub and pad layers.
- `open_cycle_blur` is renamed `open_cycle_tension`: the under-layer for the final phase of the cycle in either mode.
- Prohibitions retained from the brief: near-miss audio, coin cascades and counters, jackpot or second-chance spinners, casino bed music, rapid re-fire.

**1.1.** Client direction: the set should lean toward polished video-game FX in the register of Triumph Rips, PackDraw and Skin.Club, and the open sequence is built around six core moments: a button pressed when the box is chosen, the box partially opened, the box fully opened, watches cycling through, the final watch selected, and a watch case being opened. Changes from 1.0:

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

### 1.1 The concept: a game, with the watch in its accents

The client's direction is that the set should feel like a polished game: designed, bright, weighty, satisfying on a phone speaker. Game audio is built from synthesis and heavily processed source, with recorded elements used as accents. GemBreak follows that order. The Designed layer is the voice; three recorded layers taken from a luxury watch and its box are the accents that make it GemBreak's game rather than anyone's. Four layers, one family:

| Layer | Source | Role in the set | Character in words |
|---|---|---|---|
| **Designed** | Synthesis and processed source: designed clicks and blips, whooshes, charge-up risers, impacts with sub, sparkle and shimmer bursts, tonal stingers, pad beds, scroll ticks | The primary layer of every sound in the set. UI sounds may be entirely designed. | Bright, clean, weighty. The register of a premium mobile game menu and loot reveal. Never 8-bit, never orchestral-trailer. |
| **Steel** | Deployant clasp, bracelet links, crown and bezel ratchets, case-back click | Accent transients inside designed sounds: the click in the confirm, the mechanical bite in the lock, the latch in the case open | Dry, small, precise. A few milliseconds that say "watch". |
| **Sapphire** | Struck and bowed crystal and tuned glass, pitched | Accent tone inside confirmations and stingers; the glass ring in the reveal strike | Clear, bell-like. Sits inside the designed stinger, not instead of it. |
| **Cloth** | Tissue, velour, leather lid, air in a box | Texture inside whooshes, sheet transitions and the settle | Soft noise with shape, under the designed air. |

**Rules:**
- Every sound is a designed game sound first. It must work on its own as a game sound before any accent is added.
- The reveal strike, the selection lock, the box open, purchase confirmed and the vault lock each carry at least one recorded accent. UI sounds may be purely designed.
- The accents are what stop the set sounding like a stock pack. If a sound could be dropped into any other mystery-box app unchanged, it is not finished.

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
| Cycle ticks | −16 during the fast phase, −12 during the slowdown | −30 → −26 LUFS |
| Harmonic bed | −18, ducking to −24 under payoffs | −32 / −38 LUFS |
| UI taps, toggles, tabs, sheets, back, refresh | −20 to −22 | −34 to −36 LUFS |
| Empty state, disabled | −24 to −26 | −38 to −40 LUFS |
| Loading loop | −28 | −42 LUFS |

Only 2 LU separates each tier. Tiers escalate in weight, layers and length (Section 5), not in loudness.

---

## 2. Design rules as requirements

| # | Rule | Requirement | How it is verified |
|---|---|---|---|
| R1 | One sonic family | Every asset is a designed sound in the shared register (1.1); the reveal, lock, box open, purchase and vault sounds carry a recorded accent. Every pitched asset is in E major (1.2). | Asset review against the source-material log; spectral check for out-of-key partials. |
| R2 | Short | All UI-family sounds ≤ 150 ms to −40 dB. Only the open sequence and purchase confirmed exceed it. | Automated duration check on delivery. |
| R3 | Tension from rhythm and pitch, not volume | The cycle rises no more than 6 LU end to end. Its tension comes from the tick rate and spacing and a riser under the slowdown, resolved by the lock and the reveal (4.3). | Level plot of the cycle; listening test. |
| R4 | Frequency separation | UI assets high-passed at 800 Hz, no sustained energy below 1.2 kHz. Payoff body between 250 Hz and 1.2 kHz. | Spectrogram check per asset. |
| R5 | Repetition safety | Every sound heard more than three times per typical session has round-robin variants, pitch or velocity variation, and a rapid-repeat volume taper (Section 6). | Runtime rules in the audio manager; session-log check. |
| R6 | Survives a phone speaker | Every asset remains identifiable with a 300 Hz high-pass applied and played from a phone speaker at arm's length at 50 % volume (Section 9). | Device protocol, signed off per asset. |
| R7 | No near-miss, no coins, no jackpot layer | Per-item ticks and a decelerating scroll are permitted by client direction (4.3). Prohibited: tier-coded or near-miss audio, coin cascades and counters, jackpot or second-chance spinners, casino bed music, rapid re-fire (Section 10). | Exclusion checklist plus a naive-listener test. |
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
| `open_box_select` ★ | The button pressed when the box is chosen | 160 | A premium game "select": designed press with a tonal body, a short whoosh-swell, and a clasp-click accent on the transient. Heavier than `ui_tap`; this one commits. | E5 body, glint at B5 | −12 | No | Medium impact then a light echo at +80 ms / `PRIMITIVE_CLICK`, `PRIMITIVE_TICK` | 3 |
| `open_box_enter` | Box animates to centre and comes to rest (skip if already centred) | 500 | Box sliding on cloth, set down on wood and leather. Soft knock with a designed low body. | Unpitched; knock around E3–E4 | −14 | No | Soft heavy transient at set-down (0.6, sharpness 0.2) / `PRIMITIVE_THUD` | 2 |
| `open_bed` | Starts at the box crack; runs to the end of settle | Loop, 8000 per cycle | Warm pad: bowed sapphire drone with a soft designed pad under it, root and fifth. A room with a glow. | E3 + B3 (headphone body), E4 + B4 (speaker-audible) | −18, ducks to −24 during payoffs | Fade 400 | None | 1 loop, seamless |
| `open_box_crack` ★ | Box partially opens: lid lifts a few degrees, light spills | 600 | A charge-up: latch-release accent, then a light-leak riser (filtered noise and a rising tonal glow) with a shimmer swell. The loot-box tease. | Rising glow E4→G♯4 | −12 | No | Soft continuous 200 ms, intensity 0.3, then a light transient at the latch | 2 |
| `open_tell_t2` | Layered on `open_box_crack` when the outcome is tier 2 | 450 | One added sapphire note in the spilled light | B4 | −12 | No | Continuous extends to 250 ms, 0.4 | 1 |
| `open_tell_t3` | Layered on `open_box_crack` when the outcome is tier 3 | 600 | The light gains the major-seventh shimmer and a soft sparkle tail | D♯5 shimmer | −10 | No | Continuous extends to 300 ms, 0.5 | 1 |
| `open_tell_t4` | Follows `open_box_crack` when the outcome is tier 4 | 400 | **Silence.** The bed does not start. The crack is followed by 400 ms of nothing before the full open. | None | Silence | No | Continuous 300 ms, 0.3, then nothing | Logic, no asset |
| `open_box_open` ★ | Box fully opens: lid swings to rest | 700 | Energy release: whoosh out, an impact with a soft sub, a sparkle burst spraying upward, and the lid landing on its stop with a steel-tick accent. Tier 4 uses a deeper, wider variant. | Open tone E4 with a fifth; sparkle in E pentatonic; T4 adds E3 body | −6 | No | Transient 0.8, sharpness 0.4, then soft continuous 300 ms / `PRIMITIVE_THUD`, `PRIMITIVE_SLOW_RISE` | 2 + 1 tier-4 variant |
| `open_cycle_pass` ★ | Each watch passing the pointer during the cycle | 30–60 | The item-scroll tick: a designed peg-clack with a short tonal ping, in the register of a game item roulette or prize wheel. Uniform across items and tiers. Six variants with a slight upward pitch spread so long runs do not machine-gun. | Ping around E6 with ±1 semitone spread across variants; no scale ascent | −16 fast phase, −12 slowdown | Cut (per-item) | Light transient per tick, intensity 0.25→0.5 as the ticks spread out / `PRIMITIVE_TICK`; `SLOW_RISE` on devices with poor per-event latency | 6 variants × 2 = 12 |
| `open_cycle_tension` | Under-layer for the final phase of the cycle (mode A: the slowdown; mode B: the blur) | 1200 | A tension riser: filtered noise and a low tonal swell rising as the ticks spread out, cut dead by the lock | Rises toward B4, unresolved; the lock resolves to E5 | −12 | Cut by the lock | Continuous 1200 ms, 0.3→0.7 / `SLOW_RISE` | 1 |
| `open_select_lock` ★ | The final watch is selected; the cycle stops | 300 | The lock-in: a designed clunk with a sub thump and a 250–400 Hz knock, a steel-latch accent on the transient, and a short tonal stab. A "selection confirmed" hit, not a slot reel stop. **Identical for every tier.** | E5 stab; knock in the E3–E4 region | −6 | No | Transient 1.0, sharpness 0.8 / `PRIMITIVE_CLICK` at full scale | 3, ±10 cents |
| `open_case_open` ★ | The selected watch's presentation case opens: the reveal | 600 | The loot-box break: a short riser tail into an impact, a glass-shatter-like sparkle burst spraying outward, an energy whoosh, with the sapphire strike ringing inside it and a case-latch accent on the transient. The payoff carrier. | Strike E5 inside the burst | −4 | No | Transient 1.0, sharpness 0.7, then payoff haptics | 3, ±10 cents |
| `open_payoff_t1` | Layered from the strike, tier 1 | 800 | A short "item revealed" chime with a sparkle tail. The common-drop sound. | E5 with a B5 grace | −6 | Skip after 40 % → 200 ms fade to settle | None beyond the strike | 2 |
| `open_payoff_t2` | Layered from the strike, tier 2 | 1300 | A two-note rising chime, longer sparkle, a soft pad swell underneath. The rare-drop sound. | E5→B5 | −4 | Skip after 40 % → 200 ms fade | One echo transient at +150 ms, 0.5 | 2 |
| `open_payoff_t3` | Layered from the strike, tier 3 | 2200 | An ascending arpeggio stinger over a sub thump with a choir-like pad swell holding the major-seventh colour, then an afterglow chime at +600 ms. The epic-drop sound. | E5→G♯5→B5, afterglow E6; pad with D♯ | −2 | Skip after 40 % → 300 ms fade | Double echo (+150, +300 ms; 0.5, 0.4) then 400 ms continuous decay | 1 |
| `open_payoff_t4` | Layered from the strike, tier 4 | 3800 | Out of the silence: the break, a soft bass drop, a low crystal bell, a four-note ascending stinger to the high octave held over a wide pad, and a long sparkle tail. The legendary-drop sound, and the one true stinger in the app. | Break and strike E5; bass drop to E1/E2 (headphone) with E3 body (speaker); bell E4; figure E5→G♯5→B5→E6; post-bed E major add 9 with D♯ | 0 (anchor) | Skip only after 1000 ms → 500 ms fade | Continuous 1200 ms swell from +250 ms, 0.3→0.9→0, sharpness 0.2 / `SLOW_RISE` then `QUICK_FALL` | 1 |
| `open_bed_t4_post` | Begins with `open_payoff_t4`; runs through settle | Loop, 12000 per cycle | The room after the bell. Wide, slow, warm. Never heard anywhere else. | E major add 9 with D♯ | −16, fading through settle | Fade 800 | None | 1 |
| `open_settle` | Payoff ends | 1000 | Pad fades out; a last sparkle drift; a soft cloth accent as the card settles. Then silence. | Unpitched | −16 fading to silence | Fade 200 | None | 2 |

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

**Count:** 38 event IDs (37 carry audio; the tier-4 tell is logic), 3 loops, and 107 audio files once round-robin variants and velocity layers are included. `audit/library-structure.md` enumerates them.

---

## 4. The open sequence

The only place in the product where sound is allowed length. It has to deliver the game-like satisfaction of the client's references without a single casino cue.

### 4.1 The six moments

| # | Client's moment | Asset | What the sound is doing |
|---|---|---|---|
| 1 | A button being pressed when the box is chosen | `open_box_select` | Commitment. Heavier than any other button in the app. |
| 2 | A box being partially opened | `open_box_crack` (+ `open_tell_*`) | The tease, and the honest tier tell: the spilled light is tinted and voiced by tier. |
| 3 | A box being fully opened | `open_box_open` | Release. Air, a resonant open, the lid settling. Launches the cycle. |
| 4 | Watches cycling through | `open_cycle_pass` ×N, `open_cycle_tension` | The item scroll: fast uniform ticks, then a slowdown with a riser under it. Uniform per item. |
| 5 | Final watch being selected | `open_select_lock` | The lock-in. Mechanical, decisive, identical for every tier. |
| 6 | A watch case being opened | `open_case_open` (+ `open_payoff_t*`) | The reveal. The loot-box break, the sparkle burst, the tier stinger. |

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
| 1900 (T4: 2300) | Cycle begins: fast phase | `open_cycle_pass` | Constant ~12 ticks/s for 1800 ms |
| +1800 | Slowdown begins | `open_cycle_pass` + `open_cycle_tension` | Ticks spread from ~12/s to ~3/s over 1200 ms on an ease-out; riser under |
| +3000 (4900; T4: 5300) | Selection | `open_select_lock` | The last tick is the lock. Tension layer cuts. |
| +300 (5200; T4: 5600) | Hold | | Near-silence. The selected watch sits in frame. |
| 5200 (T4: 5600) | Case opens | `open_case_open` | The break: riser tail, impact, sparkle burst, strike |
| 5200 | Payoff | `open_payoff_t1…t4` | Layered from the strike |
| 5800 | Tier 3 afterglow | (within `open_payoff_t3`) | E6 chime |
| 6000 / 6500 / 7400 / 9400 | Payoff ends, T1 / T2 / T3 / T4 | | |
| +1000 | Settle ends | `open_settle` | Pad gone. Item card interactive. |

Totals from the press to interactive: **T1 ≈ 7.0 s, T2 ≈ 7.5 s, T3 ≈ 8.4 s, T4 ≈ 10.4 s.** The cycle itself is 3.0 s, about half a CS:GO reel, and skippable (4.6).

### 4.3 The cycle: the item scroll

The client's direction is that this should sound like scrolling through item options in a game or casino. Two modes are specified. Mode A is the default.

**Mode A: decelerating item scroll (default).** The grammar of CS:GO cases, prize wheels and item roulettes.
- **Fast phase**, 1800 ms: watches pass the pointer at a constant rate of about 12 per second. Each pass plays `open_cycle_pass`, a designed peg-clack with a short tonal ping. Six variants with a slight pitch spread are shuffled so the run never machine-guns.
- **Slowdown**, 1200 ms: the rate eases from about 12 per second to about 3 on an ease-out curve. The ticks spread out; the gaps are the tension. `open_cycle_tension`, a filtered-noise and low tonal riser, comes in under the slowdown and rises toward B4 without resolving.
- **The stop.** The final tick is replaced by `open_select_lock`: a clunk with sub, knock and a tonal stab on E5, resolving the riser. The tension layer cuts dead on the same frame.
- **Hold**, 300 ms of near-silence, then `open_case_open`.
- The last gap before the lock is capped at 400 ms. Longer hushes are the slot machine's suspense beat and are not used.

**Mode B: accelerate and snap (alternative, from v1.1).** Passes accelerate to a blur with `open_cycle_tension` as the sweep, then snap to the lock with no deceleration. Available if the product wants a less casino-adjacent feel, or as the Quick open behaviour.

**Guardrails in both modes.** These are what keep the scroll a game menu rather than a slot reel, and they come from the brief's remaining prohibitions and the audit's regulatory findings.
1. **Ticks carry no tier information.** Every pass sound is identical in kind regardless of the watch on screen. Nothing in the audio hints at what is coming.
2. **The stop is a lock, not a reel stop.** `open_select_lock` is a "selection confirmed" hit with a tonal resolution, not a mechanical reel "chunk".
3. **No second spin.** No jackpot wheel, upgrade spin or re-roll after the lock.
4. **No coin cascade, counter or cash-register sound** anywhere in the sequence.
5. **The tell is earlier and honest.** The tier was told at the crack (4.4). The scroll reveals identity, not tier.
6. **Visual rule the audio depends on:** the watches shown beside the selection at the stop should not be visibly higher-tier than the selection. The sound cannot fix a near-miss the picture creates.

**What the named references actually document.** Rips by Triumph's only described cue is that "the reveal makes a knocking sound and brief vibration": one transient synchronised to a haptic, which is what `open_select_lock` is. PackDraw and Skin.Club are reel flows; the clone codebases that imitate them show the polish comes from a layered stinger (transient, detuned tonal partials staggered by tens of milliseconds, a short high-passed air tail), a deliberate hold of about a second before the result, small per-tier steps in gain and length, and a rule that nothing else plays over the stinger. Valve's own event tables give reveal sounds an instance limit of one and block the inspect click for a second. All of that is adopted here.

### 4.4 The tell: honest by construction

The tier tell fires at the partial open, before the cycle. Three rules:

1. The tell is selected from the **resolved outcome**. The tier is known before the sequence begins. No random draw at tell time, no ambiguous state.
2. Each tier has exactly one tell. Tier 1 is the bare crack. Tier 2 adds one note in the light. Tier 3 adds the major-seventh shimmer. Tier 4 is followed by silence, and its bed never starts. Silence is the rarest thing in the app, so silence is the top tell.
3. No tell is ever followed by a different tier's payoff. A code-level assertion fails the build if `open_tell_tN` is followed by `open_payoff_tM` with M ≠ N.

Placing the tell before the cycle splits the curiosity in two: the crack answers "how good", the scroll and case answer "which watch". Tier and identity are revealed by different moments, which keeps the scroll interesting after an honest tell and removes the near-miss from the audio entirely.

### 4.5 Interaction

- The sequence is tap-driven from `open_box_select`. Everything after the press runs automatically.
- **Optional hold-to-crack.** If product wants a tactile tease, a press-and-hold on the box plays `open_box_crack` while held and `open_box_open` on release. Releasing early closes the lid with `ui_sheet_close` and returns to the pre-press state. The tell fires at the crack either way.
- If the app is backgrounded mid-sequence, all sound stops immediately. On return the sequence restarts from `open_box_crack`. No catch-up audio.

### 4.6 Skipping

- During the cycle: a tap jumps to the slowdown's last 400 ms and the lock. The outcome is already fixed, so skipping costs nothing. This is the references' "fast open", offered on request rather than as a mode.
- After the lock, tiers 1 to 3: a tap skips to `open_settle` once 40 % of the payoff has played, fading over 200–300 ms.
- After the lock, tier 4: skip is available only after 1000 ms, fading over 500 ms.
- **Quick open** (setting, default off) runs the cycle in mode B at 800 ms and removes the 300 ms hold. Nothing else changes.
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
| Scroll and lock | Identical | Identical | Identical | Identical |
| Case open strike | E5, identical | E5, identical | E5, identical | E5, identical |
| Payoff figure | E5 chime with B5 grace | E5→B5 | E5→G♯5→B5 arpeggio, afterglow E6 | E5→G♯5→B5→E6 held; low bell E4; bass drop under |
| Designed layers | Short sparkle | Longer sparkle, pad swell | Sub thump, arpeggio stinger, choir-like pad, sparkle | Bass drop, low bell, long sparkle, wide post-bed |
| Payoff length | 800 ms | 1300 ms | 2200 ms | 3800 ms |
| Level | −6 | −4 | −2 | 0 |
| Lowest fundamental | E5 | E5 | E5 with sub under | E4 with bass drop under |
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
| **Round-robin** | All UI, `open_box_select`, `open_cycle_pass` (12 variants), `open_select_lock`, `open_case_open`, `sys_refresh_*`, T1 and T2 payoffs | Variants cycle in a shuffled order with no immediate repeat. Cycle ticks additionally avoid repeating any variant within four ticks. |
| **Pitch variation** | Steel and cloth cores (unpitched) | ±20 cents random per trigger. |
| | Sapphire and designed glints (pitched) | ±10 cents random per trigger. Never applied to the lock or the T3 and T4 figures, which stay exactly in tune with the bed. Cycle ticks use ±25 cents. |
| **Velocity layers** | `ui_tap`, `ui_toggle_*`, `open_select_lock`, `open_case_open`, `vault_added` | Two dynamic layers per variant; the manager picks by a random 0.8–1.0 velocity. |
| **Rapid-repeat taper** | All UI-family sounds | Same ID more than three times within 2 s: each further trigger 3 dB quieter, floor −9 dB. Recovers after 1.5 s idle. |
| **Voice limit** | UI family | Maximum two UI voices at once; a third steals the oldest. Open-sequence events and the bed are never stolen. Cycle ticks are capped at three overlapping voices; older ticks fade in 20 ms. |
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
| `open_cycle_pass` | Core Haptics transient per tick, 0.25 in the fast phase rising to 0.5 as ticks spread out, sharpness 0.6, generated at runtime | `Composition` of `PRIMITIVE_TICK` per tick; or `PRIMITIVE_SLOW_RISE` for the slowdown where per-event latency is poor | waveform with falling density |
| `open_cycle_tension` | Continuous 1200 ms, 0.3→0.7 | `PRIMITIVE_SLOW_RISE` | one-shot 400 ms, amplitude 100 |
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
- Cycle ticks are scheduled from the animation clock so that tick audio, tick haptic and the watch crossing the pointer line up; the audio engine receives the tick timestamps ahead of time rather than reacting to frames.

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
- **Reduce Motion:** the cycle's per-tick haptics are replaced by the single `open_cycle_tension` continuous event; Quick open is suggested on first run; sounds are unchanged.
- **Every sound has a visual twin.** No state is communicated by sound alone.

---

## 9. Phone-speaker verification protocol

The set is mixed for phone speakers and checked on them. Headphones are for authoring, not sign-off.

1. **Authoring pre-check.** Monitor every asset through a 300 Hz high-pass and a −6 dB shelf above 8 kHz, in mono. If an asset loses its identity, fix the asset, not the filter. Sub layers on the lock and the top two payoffs must be accompanied by a 250–400 Hz component that carries the weight on a speaker.
2. **Reference devices.** A current base-model iPhone, a mid-range Android with a single bottom-firing speaker, and one Android at least four years old. Add a stereo-speaker device to check nothing depends on width.
3. **Conditions.** Each device at 50 % volume in a quiet room at arm's length; at 100 % in a noisy room (café-level, around 65 dB A); face up on a table; face down on a table. The scroll ticks, the lock, the case open and the purchase confirmation must be identifiable in all four. UI sounds must be identifiable in the first two.
4. **Screen recording.** Record a full T1 open and a full T4 open with the OS screen recorder on each device. Play the recordings back on another phone's speaker. The lock, the strike and the tier difference must survive.
5. **Sign-off.** Each asset ID gets a pass on each device, logged. No asset ships on a fail.

---

## 10. Slot-machine exclusion

| Prohibited | Why | GemBreak's alternative |
|---|---|---|
| Tier-coded ticks, or any change in the tick as a particular item approaches | Near-miss; the slot's "almost" cue | Ticks are uniform in kind for every item and tier (4.3 guardrail 1) |
| A slot reel "chunk" stop, or staggered multi-reel stops | Reel stop | `open_select_lock`, a lock-in with a tonal resolution, identical for all tiers |
| A long hush before the stop | Slot suspense beat | The last gap before the lock is capped at 400 ms; the only other silences are T4's tell and the 300 ms hold after the lock |
| *Permitted by client direction (v1.2):* per-item ticks and a decelerating scroll | The client wants the game item-scroll grammar | Mode A in 4.3, under the guardrails above |
| Tier-coded pass sounds or any audio hinting at a tier the user did not get | Near-miss; Zendle et al. | Passes are uniform; the tell is a pure function of the resolved tier |
| Coin cascades, cash counters ticking up, Plinko drops | Coin Master, Monopoly Go | Value is shown, not rained |
| A second spinner, "jackpot", "upgrade" or "double or nothing" moment | HypeDrop, battle sites | None exists |
| Per-tier loudness escalation, sparks-and-fire fanfares, klaxons | Key-Drop, Whatnot host layer | 2 LU per tier; escalation by note, layer and length; one short stinger at T4 |
| Rapid re-fire, auto-open, mass open, "open 4" | KSA "rapid successive opening" | One open at a time; next box chosen explicitly; skip on request |
| Casino or slot-lobby bed music | Coin Master village themes | A warm pad at −18 LU that behaves like a room |

**Naive-listener test.** Before sign-off, play the full auto-mode open at T1 and T3 to five people who have not seen the app, on a phone speaker, without the screen. Ask what they think it is. "Game", "loot box", "opening a pack" and "prize wheel" are passes. "Slot machine", "casino" and "jackpot" from two or more of the five means the scroll is retuned (shorter slowdown, lighter tick, mode B) before shipping. Run the test on the scroll alone as well as on the full sequence.

---

## 11. Decisions this spec assumes

1. **The flow is the client's six moments in this order:** box chosen, partial open, full open, cycle, selection, case open. The watch case is placed last as the climax (4.1).
2. **Four sonic tiers.** Mapping rules in 5.1 handle three or five product tiers.
3. **The cycle is a decelerating item scroll with per-item ticks (mode A)**, by client direction, under the guardrails in 4.3. Mode B remains available.
4. **The tell lives at the partial open**, before the cycle, and the cycle is uniform.
5. **A harmonic bed exists during the open sequence only.** No app-wide music.
6. **Silent switch is respected everywhere**, including the reveal.
7. **E major.** Changing the key changes every asset.
8. **Designed-first with recorded accents.** The sourcing plan sources the designed layer from game libraries and marketplaces, commissions the coherent tier-stinger family and the sapphire accents, and records the steel and cloth accents in a short session.
