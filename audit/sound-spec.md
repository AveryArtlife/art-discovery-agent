# GemBreak Sound Design — Phase 2: Sound Specification

**Status:** Phase 2 deliverable. Built on `audit/competitor-audit.md`. Feeds Phase 3 (sourcing plan and library structure).
**Date:** 2026-09-06
**Scope:** Every sound GemBreak ships, with trigger, duration, character, pitch relationship, loudness, interruptibility and haptic pairing, plus the rules that make them one product.

---

## 0. How to read this document

- **Section 1** defines the sonic identity: the three material layers, the key, the interval grammar, the frequency plan and the loudness anchor. Everything in the inventory is derived from it.
- **Section 2** restates the brief's design rules as testable requirements.
- **Section 3** is the master inventory table. Every row is one asset or one asset group.
- **Sections 4 and 5** detail the open sequence and the rarity ladder, which are the only places the spec allows length.
- **Sections 6 to 10** cover repetition, haptics, platform behaviour, the phone-speaker check and the slot-machine exclusion test.
- **Section 11** lists the product decisions this spec assumes and flags for confirmation.

**Loudness convention.** Sounds of 1 s or less are measured as momentary LUFS maximum (400 ms window). Longer sounds are measured as short-term LUFS maximum (3 s window). All levels are given relative to one anchor, the top-tier payoff, expressed in LU. The anchor is set at −14 LUFS-S max with a −1 dBTP ceiling; every other sound carries a −1 dBTP ceiling too. The absolute anchor is a starting point to be tuned on device; the relative ladder is the specification.

**Duration convention.** Durations are the audible length from onset to the point where the tail falls 40 dB below peak, in milliseconds. A "tail" is the natural decay after the last struck event, not reverb added in the mix.

**IDs.** Every asset has a stable ID of the form `family_event[_variant]`. Engineering wires against IDs, not filenames. Phase 3 maps IDs to files.

---

## 1. Sonic identity

### 1.1 The concept: the watch is the instrument

The audit's strongest craft finding was that premium products record the real object. Apple struck actual watch housings; Pokémon TCG Pocket's art director opened physical packs. GemBreak's whole sound set is made from a luxury watch and the box it arrives in. Nothing is a synth preset. Three material layers make one family:

| Layer | Source material | Role in the set | Character in words |
|---|---|---|---|
| **Steel** | Bracelet links, deployant clasp, bezel ratchet, crown winding, case set down on wood and leather | Every UI transient, every mechanical event in the open sequence | Dry, small, precise, close-miked. Short. Never rings on its own. |
| **Sapphire** | Struck and bowed sapphire crystal and tuned glass, pitched | Every confirmation, the reveal strike, every tier payoff, notifications | Clear, bell-like, fast attack, clean decay. The only pitched voice in the set. |
| **Cloth** | Tissue paper, velour lining, leather lid, breath of air in a box | Transitions, sheets, the anticipation riser, the settle | Soft noise with shape. Air moving. Never whooshy in the cinema sense. |

**Rule:** any sound that cannot be traced to one of these three sources does not belong in GemBreak.

### 1.2 Key and interval grammar

One key for the entire product: **E major**, with the pentatonic subset (E, F♯, G♯, B, C♯) for all UI and confirmation sounds. Two notes are reserved:

- **D♯ (the major seventh)** appears only in the harmonic bed for the top two tiers. It is the colour that says "this is not an ordinary open".
- **E6 (the high octave, 1319 Hz)** appears only at completion moments: purchase confirmed, the tier-3 afterglow, the tier-4 top note, and the "delivered" notification.

Interval grammar, applied everywhere:

| Meaning | Interval | Example |
|---|---|---|
| Yes, done, confirmed | Rising perfect fifth, E→B | Purchase confirmed, success |
| In progress, added, staged | Single G♯ (the third) | Add to cart, delivery requested |
| Arrival, complete cycle | Rising fifth plus octave, E→B→E′ | Delivered, tier 4 |
| No, blocked, failed | No pitch. A damped steel stop with a slight downward bend | Error, payment failed, disabled |
| Navigation | Unpitched steel or cloth, filtered to ring faintly at E7 (2637 Hz) or B7 (3951 Hz) | Tap, tab, back, sheets |

Failure is deliberately non-tonal. Duolingo's descending tritone is designed to make the learner "feel bad". A luxury buyer who mistypes a card number should feel "not yet", not punished. A quiet physical stop does that.

### 1.3 Frequency plan

The brief requires UI sounds to stay out of the range the payoff occupies. The plan below is enforced with high-pass filters baked into the assets, not applied at runtime.

| Band | Owner | Rule |
|---|---|---|
| Below 250 Hz | Nobody | Phone speakers do not reproduce it. Content may exist for headphones but nothing may depend on it. |
| 250–1200 Hz | **Payoff body** (sapphire fundamentals E4 at 330 Hz and E5 at 659 Hz, the pack set-down knock, the harmonic bed) | UI sounds are high-passed at 800 Hz and carry no sustained energy here. |
| 1.2–6 kHz | **UI steel transients** and sapphire upper partials | UI sounds live here and only here. Payoff sounds pass through this band on attack but do not sustain in it. |
| 6–12 kHz | Air: cloth layer, sapphire shimmer | Shared, low level. Nothing structural lives here. |

Consequence: a UI tap fired during a payoff tail is audible as a separate object and never masks the payoff, and a payoff never sounds like a loud UI sound.

### 1.4 Loudness ladder

Relative to the anchor (tier-4 payoff = 0 LU):

| Group | Level (LU) | Absolute at the stated anchor |
|---|---|---|
| Tier payoffs | 0 / −2 / −4 / −6 (T4 → T1) | −14 to −20 LUFS |
| Reveal strike | −4 | −18 LUFS |
| Purchase confirmed, notifications | −8 | −22 LUFS |
| Vault lock, delivery requested, payment failed, pack set-down | −10 to −14 | −24 to −28 LUFS |
| Success, error, add to cart | −14 to −16 | −28 to −30 LUFS |
| Harmonic bed | −18, ducking to −24 under payoffs | −32 / −38 LUFS |
| Anticipation build | −18 rising to −8 across the build | −32 → −22 LUFS |
| UI taps, toggles, tabs, sheets, back, refresh | −20 to −22 | −34 to −36 LUFS |
| Empty state, disabled | −24 to −26 | −38 to −40 LUFS |
| Loading loop | −28 | −42 LUFS |

Note the tier ladder: only 2 LU per tier. Tiers escalate in weight and length (Section 5), not in loudness. A louder-per-tier ladder is the slot machine's escalation curve.

---

## 2. Design rules as requirements

Each rule from the brief, restated so it can be checked.

| # | Rule | Requirement | How it is verified |
|---|---|---|---|
| R1 | One sonic family | Every asset is made from Steel, Sapphire or Cloth (1.1). Every pitched asset is in E major (1.2). | Asset review against source-material log; spectral check for out-of-key partials. |
| R2 | Short | All UI-family sounds ≤ 150 ms to −40 dB. Only the open sequence and purchase confirmed exceed it. | Automated duration check on delivery. |
| R3 | Tension from pitch and rhythm, not volume | The build rises no more than 10 LU end to end and does so smoothly. Its tension comes from an accelerating ratchet and a four-step pentatonic ascent that resolves on the strike (4.2). | Level plot of the build; listening test. |
| R4 | Frequency separation | UI assets high-passed at 800 Hz, no sustained energy below 1.2 kHz. Payoff body between 250 Hz and 1.2 kHz. | Spectrogram check per asset. |
| R5 | Repetition safety | Every sound heard more than three times per typical session has round-robin variants, pitch or velocity variation, and a rapid-repeat volume taper (Section 6). | Runtime rules implemented in the audio manager; session-log check. |
| R6 | Survives a phone speaker | Every asset remains identifiable with a 300 Hz high-pass applied and played from a phone speaker at arm's length at 50 % volume (Section 9). | Device protocol, signed off per asset. |
| R7 | Nothing sounds like a slot machine | No decelerating tick train, no reel stop, no coin cascade, no near-miss audio, no jackpot fanfare ladder, no casino bed music (Section 10). | Exclusion checklist plus a naive-listener test. |
| R8 | The top tier stays special | Tier-4 audio is never played outside a genuine tier-4 open or the owner's own vault replay of it (5.3). | Code review of every call site for the T4 asset IDs. |
| R9 | Honest tells | The pre-reveal register shift is a deterministic function of the actual tier. No probabilistic, ambiguous or "could be either" state exists (4.4). | Code review; the tell is selected from the resolved outcome, never from a random draw. |
| R10 | Silence is a design choice | Navigation that does not change state (scrolling, focus, hover) is silent. Errors are quieter than successes. | Trigger map review. |

---

## 3. Master inventory

Columns: **ID** · **Trigger** · **Duration (ms)** · **Character** · **Pitch relationship** · **Level (LU vs anchor)** · **Interruptible** · **Haptic (iOS / Android)** · **Variants**

"Interruptible: cut" means a new trigger stops it instantly. "Fade" means a new trigger fades it over the stated time. "No" means it always plays to completion.

### 3.1 UI

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `ui_tap` | Any primary or secondary button press, list row select | 40 | One bracelet link touching another. Dry, tiny, close. | Unpitched; faint ring at E7 | −22 | Cut | Light impact / `CLOCK_TICK` | 4 round-robin, ±20 cents |
| `ui_toggle_on` | Switch or checkbox to on | 60 | Clasp half-click with a tiny bright ping | E6 ping, very short | −20 | Cut | Rigid light / `CONTEXT_CLICK` | 3 |
| `ui_toggle_off` | Switch or checkbox to off | 50 | Same clasp, damped, no ping | B5 damped | −20 | Cut | Soft light / `CLOCK_TICK` | 3 |
| `ui_tab` | Tab bar or segmented control change | 55 | Cloth brush with a steel tick inside it | Unpitched; ring at B7 | −22 | Cut | Selection / `CLOCK_TICK` | 4, ±20 cents |
| `ui_sheet_open` | Bottom sheet or modal presents | 120 | Tissue lifting, pitch of the air rising | Noise rising toward E6 region | −20 | Fade 30 | Soft medium / `PRIMITIVE_TICK` | 3 |
| `ui_sheet_close` | Sheet or modal dismisses | 100 | Tissue settling, pitch falling | Noise falling from E6 region | −22 | Fade 30 | None | 3 |
| `ui_back` | Back navigation (button or edge swipe completes) | 70 | Single steel tick, slightly lower than `ui_tap` | B5 damped | −22 | Cut | None | 3 |
| `ui_error` | Inline validation fails, action rejected | 140 | Damped steel stop, as if a clasp refused to close, with a slight downward bend | Unpitched, bend from ~B4 downward | −14 | No | Notification error / `REJECT` | 2 |
| `ui_success` | Inline success not covered by a commerce or vault sound (saved, copied, verified) | 140 | Two quick sapphire notes, short tail | E5→B5 | −14 | No | Notification success / `CONFIRM` | 2, ±10 cents |
| `ui_disabled` | Press on a disabled control | 30 | Dull damped tick. Nothing moves. | Unpitched, ~1 kHz | −26 | Cut | None by default (optional rigid light) | 2 |

### 3.2 Commerce

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `com_add_to_cart` | Pack added to cart or bag | 90 | Clasp half-click plus one soft sapphire note | G♯5 | −16 | Cut | Medium impact / `PRIMITIVE_CLICK` | 2 |
| `com_purchase_confirmed` | Payment authorised; confirmation screen appears | 450 | Two clear sapphire notes with a brief high shimmer. Confident, not celebratory. The Apple Pay register: "not too serious, and clearly a confirmation". | E5→B5, shimmer at E6 | −8 | No | Two transients 120 ms apart, intensity 0.7 then 1.0, sharpness 0.6 (Core Haptics / `Composition`: CLICK, CLICK) | 1 |
| `com_payment_failed` | Payment declined or errored | 220 | Heavier version of `ui_error`: clasp refuses, then a low damped settle | Unpitched, bend downward, no tonal centre | −12 | No | Notification error / `REJECT` | 1 |

### 3.3 The open sequence

Detailed in Section 4. Durations here are per asset; the sequence timeline is in 4.3.

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `open_pack_select` | Pack chosen from the shelf or carousel | 80 | Steel tick with a hint of cloth | E5 tick | −18 | Cut | Light impact / `CLOCK_TICK` | 3 |
| `open_pack_enter` | Pack animates into frame and comes to rest | 600 | Box sliding on cloth, then set down on wood and leather. Soft knock. | Unpitched; knock resonance around E3–E4 | −14 | No | Soft heavy transient at the set-down (intensity 0.6, sharpness 0.2) / `PRIMITIVE_THUD` | 2 |
| `open_bed` | Starts 200 ms after set-down; runs to end of settle | Loop, 8000 per cycle | Bowed sapphire drone, root and fifth, barely there. A room, not a track. | E3 + B3 (headphone body), E4 + B4 (speaker-audible) | −18, ducks to −24 during payoffs | Fade 400 | None | 1 loop, seamless |
| `open_build` | Hold-to-wind begins (or auto-open starts) | 2400 nominal; gesture-driven | Crown-winding ratchet accelerating from 4 to 14 clicks per second, a cloth riser sweeping upward, and four sapphire steps ascending | Steps E4 → F♯4 → G♯4 → B4 at 0 %, 25 %, 50 %, 75 %; riser noise from ~400 Hz to ~4 kHz | −18 rising to −8 | Pauses on release (holds position with a soft click); stops on background | Per-click transients, intensity 0.3 → 0.6, sharpness 0.8, following the ratchet / `Composition` of TICK primitives, or `SLOW_RISE` on devices without per-click support | Ratchet: 5 click samples round-robin; riser and steps: 1 each |
| `open_tell_t1` | Build reaches 70 %, outcome is tier 1 | 700 | Bed unchanged. One soft sapphire G♯4 added. | G♯4 | −14 | No | Soft continuous 200 ms, intensity 0.3 | 1 |
| `open_tell_t2` | Build reaches 70 %, outcome is tier 2 | 700 | Bed gains its fifth, one soft B4 added | B4 over E+B bed | −12 | No | Soft continuous 250 ms, intensity 0.4 | 1 |
| `open_tell_t3` | Build reaches 70 %, outcome is tier 3 | 700 | Bed brightens and gains the major seventh shimmer | D♯5 shimmer over the bed | −10 | No | Soft continuous 300 ms, intensity 0.5 | 1 |
| `open_tell_t4` | Build reaches 70 %, outcome is tier 4 | 700 | **The bed cuts to silence.** Ratchet and riser continue alone, then stop 120 ms before the strike. The room goes quiet. | None | Silence | No | Continuous 300 ms, intensity 0.3, then nothing until the strike | Bed-cut logic, no asset |
| `open_reveal_strike` | Build reaches 100 %; lid opens, crystal catches light | 350 | One struck sapphire crystal, fast attack, clean ring. **Identical for every tier.** This is the honest constant: "the box is open." | E5 (659 Hz) | −4 | No | Transient intensity 1.0, sharpness 0.7 / `PRIMITIVE_CLICK` at full scale | 3, ±10 cents |
| `open_payoff_t1` | Immediately after the strike, tier 1 | 700 | The strike's ring is allowed to decay naturally. Nothing added. | E5 decaying | −6 | Skip after 40 % → 200 ms fade to settle | None beyond the strike | 2 |
| `open_payoff_t2` | Immediately after the strike, tier 2 | 1200 | A second sapphire note answers the strike. Bed swells gently. | E5→B5 | −4 | Skip after 40 % → 200 ms fade | One echo transient at +150 ms, intensity 0.5 | 2 |
| `open_payoff_t3` | Immediately after the strike, tier 3 | 2000 | Three-note rising figure, then a separate afterglow chime at +600 ms. Bed holds the major-seventh colour. | E5→G♯5→B5, afterglow E6 | −2 | Skip after 40 % → 300 ms fade | Double echo (+150, +300 ms, 0.5, 0.4) then 400 ms continuous decay | 1 |
| `open_payoff_t4` | Immediately after the strike, tier 4 | 3500 | Out of the silence: the strike, then a large low sapphire bell under it, then the four-note figure to the high octave, held. A wide, slow post-bed enters and stays through the settle. | Strike E5; low bell E4 (330 Hz) at +50 ms; figure E5→G♯5→B5→E6; post-bed E major add 9 with D♯, spread | 0 (anchor) | Skip only after 1000 ms → 500 ms fade | Continuous 1200 ms swell starting +250 ms, intensity 0.3→0.9→0, sharpness 0.2 / `SLOW_RISE` then `QUICK_FALL` | 1 |
| `open_bed_t4_post` | Begins with `open_payoff_t4`; runs through settle | Loop, 12000 per cycle | The room after the bell. Wide, slow, warm. Never heard anywhere else. | E major add 9 with D♯ | −16, fading through settle | Fade 800 | None | 1 |
| `open_settle` | Payoff ends | 1200 | Bed fades to nothing. One last soft cloth movement, as if tissue is laid back. Ends in room tone, then silence. | Unpitched | −16 fading to silence | Fade 200 | None | 2 |

### 3.4 Vault and fulfilment

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `vault_added` | Item committed to vault | 300 | Deployant clasp closing fully, then one short sapphire note. A lock. | E5 | −10 | No | Rigid medium / `PRIMITIVE_CLICK` + `PRIMITIVE_LOW_TICK` | 2 |
| `ship_requested` | Delivery request confirmed | 350 | Cloth folding (the box being wrapped) and one soft sapphire note | G♯5 | −12 | No | Notification success / `CONFIRM` | 1 |
| `notif_shipped` | Push: item shipped (also plays in-app if foregrounded) | 500 | Two rising sapphire notes, bell-like, slightly longer tail than `ui_success` | E5→G♯5 | −8 | No | System notification haptic | 1 |
| `notif_delivered` | Push: item delivered | 700 | Three rising sapphire notes to the high octave. The arrival. | E5→B5→E6 | −8 | No | System notification haptic | 1 |

### 3.5 System

| ID | Trigger | Duration | Character | Pitch | Level | Interruptible | Haptic | Variants |
|---|---|---|---|---|---|---|---|---|
| `sys_notification` | Any push not covered above; in-app banner | 400 | Two sapphire notes struck together, short | E5 + B5 dyad | −8 | No | System notification haptic | 1 |
| `sys_refresh_threshold` | Pull-to-refresh crosses the trigger threshold | 50 | Single steel tick | B5 tick | −22 | Cut | Light impact at threshold (platform convention) / `CLOCK_TICK` | 3 |
| `sys_refresh_complete` | Refresh finishes and content settles | 90 | Slightly brighter steel tick | C♯6 tick | −20 | Cut | None | 3 |
| `sys_loading_loop` | Any load exceeding 800 ms | Loop, 4000 seamless | A mechanical movement ticking: 8 beats per second, alternating tick and tock, very quiet, high-passed. A watch running while you wait. | Unpitched; tick ~3.2 kHz, tock ~2.9 kHz | −28 | Fade 200 on completion; auto-fades to silence after 20 s | None | 1 loop with 2 tick and 2 tock samples randomised |
| `sys_empty_state` | Empty state view first renders (vault empty, no orders) | 200 | Soft cloth hush, once | Unpitched | −24 | Fade 50 | None | 2 |

**Count:** 37 event IDs (36 carry audio; the tier-4 tell is bed-cut logic, not an asset), 3 loops, and roughly 100 audio files once round-robin variants and velocity layers are included. Phase 3 enumerates them.

---

## 4. The open sequence

This is the only place in the product where sound is allowed length, and it has to carry everything the live-break host's voice carries on Whatnot and Fanatics without a single casino cue.

### 4.1 Arc

The audit found four arcs in the genre: the roulette reel, the cinematic strike, the tactile rip and the physical unwrap. GemBreak uses a **physical unwrap driven by the user's own gesture**, modelled on the category-native ritual the audit documented: sleeve, box, seal, pillow, clasp, each a small dry event with air between. The build is the user winding a crown. Winding stores energy; the reveal releases it. That is the structural opposite of a reel that spins down.

### 4.2 The build: tension from rhythm and pitch

Three layers run together for the nominal 2400 ms:

1. **Ratchet.** A crown-winding click train that accelerates from 4 clicks per second to 14. It never decelerates. It is tied to the user's gesture (4.5), so it is causal in Apple's sense: the user is making the sound.
2. **Riser.** A cloth-and-air noise band sweeping upward from around 400 Hz to around 4 kHz. Level rises gently from −18 to −8 LU. That 10 LU is the total dynamic range of the build. Volume is not the tension.
3. **Steps.** Four sapphire notes ascending the pentatonic scale, one at each quarter of the build: E4, F♯4, G♯4, B4. The ear hears an unfinished scale. The strike completes it on E5.

At 70 % the **tell** fires (4.4). At 100 % the **strike** fires. The strike is the same for every tier.

### 4.3 Timeline, auto mode

Times in ms from the pack beginning to enter frame. Auto mode is used when the user taps "Open" instead of holding, and for accessibility.

| Time | Event | Asset | Note |
|---|---|---|---|
| 0 | Pack begins entering frame | `open_pack_enter` | Slide on cloth |
| 450 | Pack set down | (within `open_pack_enter`) | Knock and soft heavy haptic |
| 650 | Bed fades in over 400 ms | `open_bed` | −18 LU |
| 800 | Build starts | `open_build` | Ratchet at 4 clicks/s, step E4 |
| 1400 | 25 % | | Step F♯4 |
| 2000 | 50 % | | Step G♯4 |
| 2480 | 70 %: tell | `open_tell_t1…t4` | Tier-specific register shift; runs to the strike |
| 2600 | 75 % | | Step B4 |
| 3080 | Tier 4 only: ratchet and riser stop | | 120 ms of silence before the strike |
| 3200 | 100 %: strike | `open_reveal_strike` | E5. Lid opens. Heavy haptic. |
| 3200 | Payoff begins | `open_payoff_t1…t4` | Overlaps the strike's ring |
| 3800 | Tier 3 afterglow | (within `open_payoff_t3`) | E6 chime |
| 3900 / 4400 / 5200 / 6700 | Payoff ends, T1 / T2 / T3 / T4 | | |
| +1200 | Settle ends | `open_settle` | Bed gone. Room tone, then silence. Item card is interactive. |

Totals from pack-enter to interactive: **T1 ≈ 5.1 s, T2 ≈ 5.6 s, T3 ≈ 6.4 s, T4 ≈ 7.9 s.** Shorter than a CS:GO reel plus card for the common case, and the length is concentrated where the value is.

### 4.4 The tell: honest by construction

Every flow in the audit shifts register before the object appears, and users love it when it is truthful (Honkai: Star Rail's "early hype") and resent it when it is not (near-miss reels). GemBreak's tell obeys three rules:

1. The tell is selected from the **resolved outcome**. The tier is known before the build begins. There is no random draw at tell time and no state that "could go either way".
2. Each tier has exactly one tell. Tier 1 adds one soft note. Tier 2 adds the fifth. Tier 3 adds the major-seventh shimmer. Tier 4 takes the bed away entirely. Silence is the rarest thing in the app, so silence is the top tell.
3. No tell is ever followed by a lower tier's payoff. A code-level assertion should fail the build if `open_tell_tN` is followed by `open_payoff_tM` with M ≠ N.

### 4.5 Gesture mode: hold to wind

The default open is a press-and-hold on a crown-shaped control.

- The build advances only while the finger is down. The ratchet's click rate follows elapsed hold time on the acceleration curve; each audio click is paired with a haptic click on the same frame.
- Releasing before 100 % **pauses** the build. One soft click plays, the visual holds position, nothing rewinds. Resuming continues from where it stopped. There is no penalty and no tease; the pack simply waits.
- Reaching 100 % **triggers the strike automatically**. The user cannot hover at 99 %. This prevents a self-inflicted near-miss loop.
- If the app is backgrounded mid-build, all sound stops immediately. On return the sequence restarts from `open_pack_enter`. No catch-up audio.
- Auto mode (tap "Open") runs the same 2400 ms curve without gesture input. It is the default when Reduce Motion is on or when the user has chosen "Quick open" in settings, and it is available to every user as a secondary control.

### 4.6 Skipping

- Before the strike: no skip. The build is at most 2.4 s and is user-controlled.
- After the strike, tiers 1 to 3: a tap anywhere skips to `open_settle` once 40 % of the payoff has played. The payoff fades over 200–300 ms rather than cutting.
- After the strike, tier 4: skip is available only after 1000 ms, and fades over 500 ms.
- Rapid re-fire is not possible. A new open cannot begin until the previous settle has finished or been skipped, and the next pack must be selected explicitly. No "open 4" row, no auto-open queue.

### 4.7 Replays

The vault replays an open with the same audio, including tier 4. Replays are the "relive the hit" moment Fanatics built, and they are the owner's own memory, so tier-4 exclusivity is not diluted. Replays skip `open_pack_select` and start at `open_pack_enter`, run in auto mode, and can be skipped at any point after the strike.

---

## 5. The rarity ladder

### 5.1 Tier mapping

This spec assumes four sonic tiers. The product's actual tier structure maps onto them as follows; if the product has three tiers, drop T2; if five, T4 must still map to the rarest tier and the two middle product tiers share T2 and T3.

| Sonic tier | Suggested label | Product tier | Intended frequency |
|---|---|---|---|
| T1 | Standard | Base outcomes | Most opens |
| T2 | Select | Above-base outcomes | Regular but noticed |
| T3 | Reserve | High-value outcomes | Occasional; a session event |
| T4 | Grail | The rarest outcomes | Rare enough to stay special. Recommendation: no more than one in two hundred opens app-wide. If the product's top tier is more common than that, map T4 to a rarer sub-tier or reserve it for a defined "grail" class. |

Labels are watch-collector language, not gaming language. The product owns final naming.

### 5.2 Escalation by weight and length

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Tell | +G♯4, bed unchanged | +B4, bed gains fifth | +D♯5 shimmer, bed brightens | Bed cuts to silence |
| Pre-strike silence | None | None | None | 120 ms |
| Strike | E5, identical | E5, identical | E5, identical | E5, identical |
| Payoff figure | E5 decays | E5→B5 | E5→G♯5→B5, afterglow E6 | E5→G♯5→B5→E6 held, low bell E4 under |
| Payoff length | 700 ms | 1200 ms | 2000 ms | 3500 ms |
| Level | −6 | −4 | −2 | 0 |
| Lowest fundamental | E5 (659 Hz) | E5 | E5 | E4 (330 Hz) |
| Bed after | Fades | Fades | Holds D♯ colour, fades | New post-bed, wide, fades through settle |
| Haptic | Strike only | Strike + one echo | Strike + double echo + 400 ms decay | Strike + 1200 ms swell |
| Variants | 2 | 2 | 1 | 1 |

The ladder adds one note, one layer and one haptic element per step. It never adds a fanfare, a counter, a cascade or a loop.

### 5.3 Keeping tier 4 special

- `open_tell_t4`, `open_payoff_t4` and `open_bed_t4_post` are played by exactly one code path: a genuine tier-4 open or the owner's own vault replay of one.
- They are never used in onboarding, tutorials, demo packs, marketing screens, app-store previews, push notifications, social or activity feeds, "someone just pulled" surfaces, or A/B tests of other features.
- Any demo or tutorial open resolves at T1.
- T4 assets are not shipped in any preview build that can be captured for marketing without the product lead's sign-off.

---

## 6. Repetition and variation

Every sound a user hears more than a few times per session needs relief. The rules below are implemented once in the audio manager and applied by ID.

| Mechanism | Applies to | Rule |
|---|---|---|
| **Round-robin** | All UI, `open_pack_select`, ratchet clicks, `open_reveal_strike`, `sys_refresh_*`, T1 and T2 payoffs | Variants cycle in a shuffled order with no immediate repeat. Counts per row in Section 3. |
| **Pitch variation** | Steel and cloth (unpitched) | ±20 cents random per trigger. |
| | Sapphire (pitched) | ±10 cents random per trigger. Imperceptible as detuning, enough to break sameness. Never applied to the four build steps or the T3 and T4 figures, which must stay exactly in tune with the bed. |
| **Velocity layers** | `ui_tap`, `ui_toggle_*`, `open_reveal_strike`, `vault_added` | Two dynamic layers per variant; the manager picks by a random 0.8–1.0 velocity. |
| **Rapid-repeat taper** | All UI-family sounds | If the same ID fires more than three times within 2 s, each further trigger plays 3 dB quieter, down to a floor of −9 dB. Recovers fully after 1.5 s idle. This is Apple's keyboard-click principle. |
| **Voice limit** | UI family | Maximum two UI voices at once; a third trigger steals the oldest. Payoffs and the bed are never stolen. |
| **Rate limits** | `sys_notification` in-app | At most once per 60 s; further banners in that window are silent. |
| | `sys_empty_state` | At most once per 30 s per screen. |
| | `sys_loading_loop` | Starts only after 800 ms of loading; fades to silence after 20 s even if still loading; restarts only on a new load. |
| **Session decay** | Open sequence | None. The reveal is the product. It stays whole by default and is skippable on request (4.6). |

---

## 7. Haptic mapping

Principles, from the audit's Apple sources: haptic and audio are two instruments playing the same tempo; sync within 10 ms; prepare generators before the gesture; the haptic may lead the sound for anticipation, never lag it; if a haptic is not obviously caused by something the user did or saw, remove it.

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
| `open_pack_enter` (set-down) | Core Haptics transient, intensity 0.6, sharpness 0.2 | `PRIMITIVE_THUD` | one-shot 25 ms, amplitude 150 |
| `open_build` ratchet | Core Haptics transients per click, intensity 0.3→0.6, sharpness 0.8, generated at runtime from the gesture | `Composition` of `PRIMITIVE_TICK` per click; or `PRIMITIVE_SLOW_RISE` for the whole build where per-click latency is poor | waveform with rising density |
| `open_tell_*` | Core Haptics continuous 200–300 ms, intensity 0.3–0.5, sharpness 0.1 | `PRIMITIVE_LOW_TICK` | none |
| `open_reveal_strike` | Core Haptics transient, intensity 1.0, sharpness 0.7 | `PRIMITIVE_CLICK` (1.0) | one-shot 30 ms, amplitude 255 |
| `open_payoff_t2` echo | Transient +150 ms, 0.5 | `PRIMITIVE_TICK` | none |
| `open_payoff_t3` | Transients +150 / +300 ms (0.5, 0.4), then continuous 400 ms, 0.4→0 | `TICK, TICK, QUICK_FALL` | none |
| `open_payoff_t4` | Continuous 1200 ms from +250 ms, intensity curve 0.3→0.9→0, sharpness 0.2 | `SLOW_RISE` then `QUICK_FALL` | one-shot 400 ms, amplitude 120 |
| `vault_added` | `.rigid`, intensity 0.8 | `PRIMITIVE_CLICK` + `PRIMITIVE_LOW_TICK` | one-shot 20 ms |
| `sys_refresh_threshold` | `.light` at threshold | `CLOCK_TICK` | one-shot 8 ms |
| Notifications | System | Notification channel default | System |
| Everything else | None | None | None |

Rules:
- Call `prepare()` on iOS generators, and warm the Android vibrator, when the user's finger lands on a control that will fire a haptic, not when it fires.
- Check `Vibrator.areAllPrimitivesSupported()` on Android at launch and select the fallback column per device once.
- Haptics obey a separate "Haptics" toggle (8.3) and the system's haptic settings. When haptics are off, nothing in the audio changes.
- No haptic fires while the device is face down on a surface if that state is detectable; the buzz against a table is louder than the sound.

---

## 8. Platform behaviour

### 8.1 Audio session and mixing

- **iOS:** `AVAudioSession` category `.ambient`. App sounds obey the ring/silent switch, mix with the user's own music or podcast, and never duck it. Apple classes app sound effects as nonessential; a user listening to something else should not be interrupted by a reveal. If the product decides the reveal should play even in silent mode, that is a deliberate exception to Apple's guidance and needs a product-level decision; this spec does not recommend it.
- **Android:** UI and reveal sounds through a low-latency engine (SoundPool or Oboe) with `AudioAttributes` usage `USAGE_GAME` and content type `CONTENT_TYPE_SONIFICATION`, so they follow media volume and mix with other apps. In addition, suppress all app sounds when `AudioManager.ringerMode` is silent or vibrate, so the two platforms behave alike. Notifications go through notification channels with the custom sounds attached.
- The harmonic bed is the only sound longer than a few seconds and it still uses the same session; it never claims audio focus.

### 8.2 Latency and sync

- Preload every UI-family asset at launch. Each is under 100 KB.
- Target audio start within 12 ms of the trigger. Fire the haptic on the same frame as the audio call; on iOS the haptic engine's own latency then lands within the 10 ms window the audio-haptic research calls out.
- The ratchet in gesture mode is generated per click from the gesture's elapsed time, so audio and haptic clicks are scheduled from the same timestamp.

### 8.3 Settings exposed to the user

Two toggles, both default on, both in the app's settings and reachable from the open screen's overflow menu:

- **Sounds.** Master toggle for every app sound including the open sequence and bed. Notification sounds are governed by the OS.
- **Haptics.** Master toggle for every app haptic.

One additional option: **Quick open**, default off. When on, the open sequence uses auto mode and the build runs at 1200 ms instead of 2400. The tell still fires (at 70 %), the strike and payoffs are unchanged. This is the relief valve for the fiftieth open, offered rather than forced.

### 8.4 Interruptions and lifecycle

- Incoming call, Siri, or another app taking audio focus: all app sounds stop. Nothing resumes on return; the open sequence restarts from `open_pack_enter`.
- App backgrounded: stop everything immediately, including the loading loop.
- Low Power Mode: no change to audio; haptics reduce to the strike and the purchase confirmation only.

### 8.5 Accessibility

- **VoiceOver / TalkBack running:** suppress the UI family (the screen reader has its own feedback), keep commerce, vault, notification and open-sequence sounds, and duck them 6 dB while the screen reader is speaking.
- **Reduce Motion:** auto mode is the default open; the ratchet's haptic is replaced by the single `open_tell` continuous event; sounds are unchanged.
- **Every sound has a visual twin.** No state is communicated by sound alone. The tell has a light change; the strike has the lid; each tier has its own visual treatment; errors shake or outline.

---

## 9. Phone-speaker verification protocol

The set is mixed for phone speakers and checked on them. Headphones are for authoring, not sign-off.

1. **Authoring pre-check.** In the DAW, monitor every asset through a 300 Hz high-pass and a −6 dB shelf above 8 kHz, in mono. If an asset loses its identity, fix the asset, not the filter.
2. **Reference devices.** A current base-model iPhone, a mid-range Android with a single bottom-firing speaker, and one Android at least four years old. Add a device with stereo speakers to check nothing depends on width.
3. **Conditions.** Each device at 50 % volume in a quiet room at arm's length; at 100 % in a noisy room (café-level, around 65 dB A); face up on a table; face down on a table. The reveal and purchase confirmation must be identifiable in all four. UI sounds must be identifiable in the first two and are allowed to vanish in the noisy room.
4. **Screen recording.** Record a full T1 open and a full T4 open with the OS screen recorder on each iPhone and Android device. Play the recordings back on another phone's speaker. The strike and the tier difference must survive.
5. **Sign-off.** Each asset ID gets a pass on each device, logged. No asset ships on a fail.

---

## 10. Slot-machine exclusion

The following are prohibited outright, with the audit's source for each.

| Prohibited | Why | GemBreak's alternative |
|---|---|---|
| Any click train that decelerates to a stop | The CS:GO reel tick; named by regulators as the slot signature | The winding ratchet accelerates and is stopped by the user reaching 100 %, never by a curve running out |
| A horizontal or vertical reel, carousel or wheel that "lands" | Same | The lid opens |
| A hush that precedes a stop during a spin | Slot suspense beat | The only pre-strike silence is T4's tell, which follows a fully deterministic outcome and is not during any spin |
| Coin cascades, cash counters ticking up, Plinko drops | Coin Master, Monopoly Go | Value is shown, not rained |
| A second spinner, "jackpot", "upgrade" or "double or nothing" moment | HypeDrop, battle sites | None exists |
| Per-tier loudness escalation, sparks-and-fire fanfares, klaxons | Key-Drop, Whatnot host layer | 2 LU per tier; escalation by note, layer and length |
| Any audio cue that hints at a tier the user did not get | Near-miss; Zendle et al. | Tell is a pure function of the resolved tier |
| Rapid re-fire, auto-open, mass open, "open 4" | KSA "rapid successive opening" | One open at a time; next pack selected explicitly |
| Casino or slot-lobby bed music | Coin Master village themes | A bowed sapphire drone at −18 LU that behaves like a room |

**Naive-listener test.** Before sign-off, play the full auto-mode open at T1 and T3 to five people who have not seen the app, on a phone speaker, without the screen. Ask what they think it is. If any of the five says "slot machine", "casino", "roulette", "spin" or "jackpot", the sequence is redesigned before shipping.

---

## 11. Decisions this spec assumes

Each of these is a product decision, stated here so it can be confirmed or changed before Phase 3 sourcing.

1. **Four sonic tiers.** Mapping rules in 5.1 handle three or five product tiers, but T4 must map to something rare enough to stay special.
2. **Hold-to-wind is the default open**, with tap-to-open available and Quick open as a setting. If product prefers tap-to-open as default, the build still runs at 2400 ms; only the gesture layer changes.
3. **A harmonic bed exists during the open sequence only.** There is no app-wide music. If product wants no bed at all, the tells for T2 and T3 move into the step notes (a fifth added to the B4 step for T2, the D♯5 shimmer added for T3) and T4's tell becomes the 120 ms pre-strike silence alone.
4. **Silent switch is respected everywhere.** No sound plays in silent mode, including the reveal.
5. **E major.** Any key works structurally; E was chosen so that the UI notes E5 to E6 sit where phone speakers are strongest and the payoff's E4 remains audible. Changing the key changes every asset.
6. **Recorded materials, not synthesis.** Phase 3 will show that the Sapphire layer in particular is unlikely to exist in stock libraries at the required consistency, which is the main argument for commissioning the hero set.
