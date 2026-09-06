# GemBreak Sound Design — Phase 3: Library Structure

**Status:** Phase 3 deliverable. Companion to `audit/sound-spec.md` (v1.1) and `audit/sourcing-plan.md`.
**Date:** 2026-09-06
**Purpose:** The folder tree, naming convention, delivery formats and variant organisation, so engineering can wire the set from a manifest without guessing, and so any file can be traced back to its source and licence.

---

## 0. Principles

1. **Engineering wires against IDs, never filenames.** A JSON manifest maps each event ID from the spec to its files, variants, layers, loop points, gain trim and haptic pattern. Filenames can change; IDs cannot.
2. **One master, two distributions.** Every asset has one 48 kHz / 24-bit WAV master. iOS and Android bundles are exported from it by a script, never edited by hand.
3. **Nothing ships that is not in the manifest, and nothing is in the manifest without a licence row** in `audit/licenses.csv`.
4. **Timing lives in data.** The open sequence is a timeline file that references IDs and offsets, so the sound designer can tune it without an app build.

---

## 1. Folder tree

Two roots: the **source library** (a private repository or shared drive, never shipped) and the **app bundles** (generated, committed to the app repo).

```
gembreak-audio/                          # source library, private
├── README.md
├── manifest.json                        # ID → files, variants, layers, loops, gain, haptics
├── timeline/
│   ├── open_sequence.json               # auto-mode timeline, per tier
│   └── open_sequence_quick.json         # Quick open variant
├── licenses.csv                         # mirror of audit/licenses.csv, kept in sync
├── masters/                             # 48 kHz / 24-bit WAV, trimmed, normalised to the LU ladder
│   ├── ui/
│   ├── com/
│   ├── open/
│   ├── vault/
│   ├── notif/
│   └── sys/
├── stems/                               # per-layer stems for every master (steel / sapphire / cloth / designed)
│   └── <same family folders>/
├── recordings/                          # raw field and studio recordings, untouched
│   ├── 2026-MM-DD_watch-hardware/       # clasp, bracelet, crown, bezel, movement
│   ├── 2026-MM-DD_presentation-box/     # hinge, lid, tissue, velour, set-down
│   └── 2026-MM-DD_sapphire-session/     # struck and bowed crystal, tuned set
├── sourced/                             # third-party files exactly as downloaded, one folder per source
│   ├── freesound/<sound-id>_<slug>/     # file + a LICENSE.txt with URL, uploader, licence, date
│   ├── kenney/<pack>/
│   ├── sonniss-gdc/<year>/<library>/
│   └── <vendor>/<library>/
├── sessions/                            # DAW sessions, one per family plus one per open-sequence tier
├── haptics/
│   ├── ios/*.ahap                       # Core Haptics patterns for composite events
│   └── android/*.json                   # composition-primitive descriptors with fallback waveforms
├── qa/
│   ├── speaker-signoff.csv              # per-asset, per-device pass/fail (spec section 9)
│   └── loudness-report.csv              # measured LUFS-M/S max, dBTP, LU vs anchor per master
└── tools/
    ├── export_ios.sh                    # masters → dist/ios (CAF LPCM 16-bit)
    ├── export_android.sh                # masters → dist/android (OGG Vorbis)
    ├── validate_manifest.py             # every ID has files, every file has a licence row, durations within spec
    └── measure_loudness.py              # writes qa/loudness-report.csv
```

Generated into the app repository:

```
ios/GemBreak/Resources/Audio/            # flat; Xcode resource folder reference
│   ├── manifest.json
│   ├── ui_tap_r01_l1.caf
│   ├── ...
│   └── Haptics/*.ahap
android/app/src/main/res/raw/            # flat; Android resource rules apply (see 2.3)
│   ├── ui_tap_r01_l1.ogg
│   └── ...
android/app/src/main/assets/audio/
    ├── manifest.json
    └── haptics/*.json
```

Both bundles are flat because iOS resource lookups and Android `res/raw` are flat namespaces. Family is carried in the filename prefix.

---

## 2. Naming convention

### 2.1 Pattern

```
{family}_{event}[_{tier}][_{step}][_{rr}][_{layer}][_loop].{ext}
```

| Token | Values | Meaning |
|---|---|---|
| `family` | `ui` `com` `open` `vault` `ship` `notif` `sys` | Matches the spec's ID prefix |
| `event` | lowercase, underscores | Matches the spec's ID |
| `tier` | `t1` `t2` `t3` `t4` | Rarity tier, only on tier-specific assets |
| `step` | `s1` … `s6` | Pitch step in the cycle pass set |
| `rr` | `r01` … `r99` | Round-robin variant index |
| `layer` | `l1` `l2` | Velocity layer: `l1` soft, `l2` hard |
| `loop` | literal `_loop` | Seamless loop; loop points in the manifest |
| `ext` | `wav` (master) `caf` (iOS) `ogg` (Android) | |

Rules:
- Lowercase ASCII letters, digits and underscores only. No hyphens, no spaces, no leading digit. This is the Android `res/raw` rule and it is applied everywhere so the three trees have identical basenames.
- No version numbers in filenames. Versions are tracked in git and in the manifest's `version` field per ID.
- A file with no `_rNN` is a single-variant asset. A file with no `_lN` is a single-layer asset.
- Tier-specific variants of a shared event (the tier-4 full open) carry the tier token: `open_box_open_t4_r01`.

### 2.2 Examples

| ID (spec) | Files |
|---|---|
| `ui_tap` | `ui_tap_r01_l1` … `ui_tap_r04_l2` (8) |
| `ui_sheet_open` | `ui_sheet_open_r01` … `_r03` (3) |
| `com_purchase_confirmed` | `com_purchase_confirmed` (1) |
| `open_box_open` | `open_box_open_r01`, `open_box_open_r02`, `open_box_open_t4_r01` (3) |
| `open_cycle_pass` | `open_cycle_pass_s1_r01` … `open_cycle_pass_s6_r02` (12) |
| `open_select_lock` | `open_select_lock_r01_l1` … `_r03_l2` (6) |
| `open_payoff_t3` | `open_payoff_t3` (1) |
| `open_bed` | `open_bed_loop` (1) |
| `open_bed_t4_post` | `open_bed_t4_post_loop` (1) |
| `sys_loading_loop` | `sys_loading_loop` (1; the `_loop` suffix is already in the ID) |

### 2.3 Platform constraints the convention satisfies

- **Android `res/raw`:** names must match `[a-z0-9_]+` and not start with a digit; the resource ID is generated from the basename, so basenames must be unique across the folder. Satisfied.
- **iOS:** any name works, but keeping the identical basename lets one manifest serve both platforms.
- **Notification sounds:** iOS requires the file in the main bundle and referenced by filename in the payload; Android references a `res/raw` resource URI on the notification channel. Both use the same basename (`notif_shipped`, `notif_delivered`, `sys_notification`).

---

## 3. Format specification

### 3.1 Masters

| Property | Value | Why |
|---|---|---|
| Container | WAV (RIFF), PCM | Universal, lossless |
| Sample rate | 48 000 Hz | Matches iOS and Android hardware output; no runtime resampling |
| Bit depth | 24-bit | Headroom for processing; dithered down for iOS |
| Channels | Mono for every one-shot. Stereo only for `open_bed_loop` and `open_bed_t4_post_loop`, and those must pass a mono-fold check with no more than 1 dB loss | Phone speakers are effectively mono; mono files are half the size and never phase-cancel |
| Peak | ≤ −1.0 dBTP | Spec ceiling |
| Loudness | Normalised to the LU ladder in the spec (LUFS-M max for ≤ 1 s, LUFS-S max above), measured and logged in `qa/loudness-report.csv` | The ladder is baked into the files so runtime gain is trim only |
| Head | Trim to the first sample above −60 dBFS, then a 1 ms fade-in | Zero latency to onset; no click |
| Tail | Trim at the point the signal falls below −60 dBFS, then a 5 ms fade-out | No truncated tails, no dead air |
| DC offset | Removed | |
| Loops | Cut at zero crossings; loop start and end stored in the manifest as sample positions; verified by rendering three consecutive passes and inspecting the seam | Gapless on both platforms |
| Metadata | `INFO` chunk: `IART` source or recordist, `ICMT` licence and source URL, `ISFT` GemBreak audio pipeline version | Traceability inside the file itself |
| Sub content | Anything below 60 Hz high-passed out except on `open_select_lock`, `open_payoff_t3`, `open_payoff_t4`, `open_box_open_t4` | Spec frequency plan; keeps the rest of the set speaker-safe |

### 3.2 iOS distribution

| Property | Value | Why |
|---|---|---|
| Container | CAF | Apple's native container; supports every codec and gapless loops |
| Codec | Linear PCM, 16-bit little-endian, 48 kHz | Zero decode latency for UI sounds; required for notification sounds (which must be PCM, IMA4, µ-law or a-law, ≤ 30 s) |
| Dither | TPDF on the 24 → 16 conversion | |
| Channels | As master | |
| Size budget | ≈ 9 MB total for ~107 files. The two beds are the bulk (≈ 1.5 MB and ≈ 2.3 MB stereo). If bundle size becomes a constraint, the beds may be delivered as AAC in CAF with explicit loop points; UI and open-sequence one-shots stay PCM. Not recommended by default. | |
| Playback | Preload every UI and open-sequence file into memory at launch via `AVAudioEngine` player nodes or a comparable low-latency layer. `AVAudioPlayer` is acceptable only for notifications and the loading loop. | 12 ms trigger-to-onset target |
| Session | `AVAudioSession` category `.ambient` (spec 8.1) | Obeys the silent switch, mixes with other audio |

### 3.3 Android distribution

| Property | Value | Why |
|---|---|---|
| Container / codec | Ogg Vorbis, quality 6 (≈ 110 kbps mono VBR), 48 kHz | Small, gapless (Vorbis has no encoder padding), decoded to PCM at load by `SoundPool` or Oboe so runtime latency is unaffected |
| Location | `res/raw/` for everything playable and for notification sounds; `assets/audio/manifest.json` for the manifest | Notification channels need a resource URI; the manifest is easier to load from assets |
| Size budget | ≈ 2 MB total | |
| Playback | `SoundPool` with `AudioAttributes` usage `USAGE_GAME`, content type `CONTENT_TYPE_SONIFICATION`, max streams 8, all sounds loaded at launch; or Oboe for the open sequence where per-pass scheduling needs sample-accurate timing | Media volume, mixes with other apps, low latency |
| Loops | `SoundPool.play(..., loop = -1)` for beds and the loading loop; loop points are whole-file, so the OGG must be exported exactly from the master's loop region | Gapless |
| Fallback | Devices where `SoundPool` latency exceeds 40 ms on test: switch the open sequence to Oboe with pre-decoded PCM buffers | |

### 3.4 Haptics

| Platform | Simple events | Composite events |
|---|---|---|
| iOS | System generators named in the manifest (`impact.light`, `selection`, `notification.success`, …) | `.ahap` files in `Haptics/`, one per composite event, played through `CHHapticEngine`; each AHAP carries its audio offset so the haptic transient lands within 10 ms of the audio onset |
| Android | `HapticFeedbackConstants` names in the manifest | JSON descriptors listing `VibrationEffect.Composition` primitives with delays and scales, plus a `fallback` waveform for devices without primitive support |

AHAP and JSON files use the event ID as basename: `open_payoff_t4.ahap`, `open_payoff_t4.json`.

---

## 4. The manifest

`manifest.json` is the single source of truth engineering loads at startup. Schema, with one example per shape:

```json
{
  "schema": 1,
  "anchor_lufs": -14.0,
  "families": {
    "ui": { "voice_limit": 2, "taper": { "window_ms": 2000, "count": 3, "step_db": -3, "floor_db": -9, "recover_ms": 1500 } },
    "open": { "voice_limit": 8, "pass_voice_limit": 3 }
  },
  "events": {
    "ui_tap": {
      "version": 3,
      "family": "ui",
      "lu": -22,
      "trim_db": 0.0,
      "interrupt": "cut",
      "pitch_random_cents": 20,
      "round_robin": "shuffle_no_repeat",
      "variants": [
        { "layers": { "l1": "ui_tap_r01_l1", "l2": "ui_tap_r01_l2" } },
        { "layers": { "l1": "ui_tap_r02_l1", "l2": "ui_tap_r02_l2" } },
        { "layers": { "l1": "ui_tap_r03_l1", "l2": "ui_tap_r03_l2" } },
        { "layers": { "l1": "ui_tap_r04_l1", "l2": "ui_tap_r04_l2" } }
      ],
      "layer_split_velocity": 0.9,
      "haptic": { "ios": "impact.light", "android": "CLOCK_TICK" }
    },
    "open_cycle_pass": {
      "version": 1,
      "family": "open",
      "lu_start": -16,
      "lu_end": -10,
      "interrupt": "cut",
      "pitch_random_cents": 0,
      "steps": [
        { "step": 1, "note": "E5",  "variants": ["open_cycle_pass_s1_r01", "open_cycle_pass_s1_r02"] },
        { "step": 2, "note": "F#5", "variants": ["open_cycle_pass_s2_r01", "open_cycle_pass_s2_r02"] },
        { "step": 3, "note": "G#5", "variants": ["open_cycle_pass_s3_r01", "open_cycle_pass_s3_r02"] },
        { "step": 4, "note": "B5",  "variants": ["open_cycle_pass_s4_r01", "open_cycle_pass_s4_r02"] },
        { "step": 5, "note": "C#6", "variants": ["open_cycle_pass_s5_r01", "open_cycle_pass_s5_r02"] },
        { "step": 6, "note": "C#6", "variants": ["open_cycle_pass_s6_r01", "open_cycle_pass_s6_r02"] }
      ],
      "haptic": { "ios": "ahap:open_cycle_pass", "android": "json:open_cycle_pass" }
    },
    "open_bed": {
      "version": 1,
      "family": "open",
      "lu": -18,
      "duck_lu": -24,
      "interrupt": "fade:400",
      "loop": { "file": "open_bed_loop", "start_sample": 0, "end_sample": 384000 },
      "haptic": null
    },
    "open_payoff_t4": {
      "version": 1,
      "family": "open",
      "lu": 0,
      "interrupt": "skip_after_ms:1000,fade:500",
      "reserved": true,
      "variants": [ { "layers": { "l1": "open_payoff_t4" } } ],
      "haptic": { "ios": "ahap:open_payoff_t4", "android": "json:open_payoff_t4" }
    }
  }
}
```

Field notes:
- `lu` is the level relative to the anchor as delivered in the file. `trim_db` is a runtime adjustment of ±3 dB at most, for device tuning without re-export. Anything larger goes back to the master.
- `interrupt` encodes the spec's interruptibility column: `cut`, `fade:<ms>`, `no`, `skip_after_pct:<n>,fade:<ms>`, `skip_after_ms:<n>,fade:<ms>`.
- `reserved: true` marks tier-4 assets. The audio manager refuses to play a reserved event unless the caller passes the current open's resolved tier and it is 4, or the replay's stored tier is 4. This is the code-level enforcement of spec 5.3.
- `steps` exists only on `open_cycle_pass`. The open-sequence timeline decides which step plays at which pass.
- Loops store sample positions, not seconds.

`tools/validate_manifest.py` fails the build if any ID in the spec is missing, any referenced file is absent from `masters/`, any file lacks a row in `licenses.csv`, any UI-family master exceeds 150 ms to −40 dB, or any master's measured level is more than 1 LU from its declared `lu`.

---

## 5. The open-sequence timeline

`timeline/open_sequence.json` expresses spec section 4.2 as data. Times are milliseconds from the box-select press; `tier` blocks override the base.

```json
{
  "base": [
    { "t": 0,    "play": "open_box_select" },
    { "t": 300,  "play": "open_box_enter", "if": "box_not_centred" },
    { "t": 900,  "play": "open_box_crack" },
    { "t": 900,  "start_loop": "open_bed", "fade_in_ms": 400 },
    { "t": 1500, "play": "open_box_open" },
    { "t": 1900, "start_cycle": { "duration_ms": 2000, "rate_start_hz": 5, "rate_end_hz": 15,
                                  "steps_at_ms": [0, 500, 1000, 1400, 1700], "blur_ms": 400 } },
    { "t": 4300, "play": "open_select_lock", "stop_cycle": true },
    { "t": 4600, "play": "open_case_open" },
    { "t": 4600, "play": "open_payoff_{tier}" },
    { "t": "payoff_end", "play": "open_settle", "stop_loop": "open_bed", "fade_out_ms": 800 }
  ],
  "tiers": {
    "t2": { "add": [ { "t": 900, "play": "open_tell_t2" } ] },
    "t3": { "add": [ { "t": 900, "play": "open_tell_t3" } ] },
    "t4": {
      "remove": [ "start_loop:open_bed" ],
      "shift_after_ms": { "from": 900, "by": 400 },
      "replace": { "open_box_open": "open_box_open_t4" },
      "add": [ { "t": "case_open", "start_loop": "open_bed_t4_post" } ]
    }
  },
  "skip": {
    "during_cycle": "jump_to:open_select_lock",
    "after_lock": { "t1": "pct:40,fade:200", "t2": "pct:40,fade:200", "t3": "pct:40,fade:300", "t4": "ms:1000,fade:500" }
  }
}
```

The cycle's per-pass scheduling is computed by the audio manager from `rate_start_hz`, `rate_end_hz` and the animation clock, so audio, haptic and the on-screen watch stay aligned. `steps_at_ms` selects which pitch step is active for passes after each offset. Passes are scheduled ahead on the audio thread, not fired from render frames.

---

## 6. File inventory

Every file the set ships, derived from the spec's variant column. Basenames only; add `.wav`, `.caf`, `.ogg` per tree.

| ID | Files | Count |
|---|---|---|
| `ui_tap` | `ui_tap_r01..r04` × `l1,l2` | 8 |
| `ui_toggle_on` | `ui_toggle_on_r01..r03` × `l1,l2` | 6 |
| `ui_toggle_off` | `ui_toggle_off_r01..r03` × `l1,l2` | 6 |
| `ui_tab` | `ui_tab_r01..r04` | 4 |
| `ui_sheet_open` | `ui_sheet_open_r01..r03` | 3 |
| `ui_sheet_close` | `ui_sheet_close_r01..r03` | 3 |
| `ui_back` | `ui_back_r01..r03` | 3 |
| `ui_error` | `ui_error_r01..r02` | 2 |
| `ui_success` | `ui_success_r01..r02` | 2 |
| `ui_disabled` | `ui_disabled_r01..r02` | 2 |
| `com_add_to_cart` | `com_add_to_cart_r01..r02` | 2 |
| `com_purchase_confirmed` | `com_purchase_confirmed` | 1 |
| `com_payment_failed` | `com_payment_failed` | 1 |
| `open_box_select` | `open_box_select_r01..r03` | 3 |
| `open_box_enter` | `open_box_enter_r01..r02` | 2 |
| `open_bed` | `open_bed_loop` | 1 |
| `open_box_crack` | `open_box_crack_r01..r02` | 2 |
| `open_tell_t2` | `open_tell_t2` | 1 |
| `open_tell_t3` | `open_tell_t3` | 1 |
| `open_box_open` | `open_box_open_r01..r02`, `open_box_open_t4_r01` | 3 |
| `open_cycle_pass` | `open_cycle_pass_s1..s6` × `r01,r02` | 12 |
| `open_cycle_blur` | `open_cycle_blur` | 1 |
| `open_select_lock` | `open_select_lock_r01..r03` × `l1,l2` | 6 |
| `open_case_open` | `open_case_open_r01..r03` × `l1,l2` | 6 |
| `open_payoff_t1` | `open_payoff_t1_r01..r02` | 2 |
| `open_payoff_t2` | `open_payoff_t2_r01..r02` | 2 |
| `open_payoff_t3` | `open_payoff_t3` | 1 |
| `open_payoff_t4` | `open_payoff_t4` | 1 |
| `open_bed_t4_post` | `open_bed_t4_post_loop` | 1 |
| `open_settle` | `open_settle_r01..r02` | 2 |
| `vault_added` | `vault_added_r01..r02` × `l1,l2` | 4 |
| `ship_requested` | `ship_requested` | 1 |
| `notif_shipped` | `notif_shipped` | 1 |
| `notif_delivered` | `notif_delivered` | 1 |
| `sys_notification` | `sys_notification` | 1 |
| `sys_refresh_threshold` | `sys_refresh_threshold_r01..r03` | 3 |
| `sys_refresh_complete` | `sys_refresh_complete_r01..r03` | 3 |
| `sys_loading_loop` | `sys_loading_loop` (rendered from 2 tick + 2 tock recordings; ship the loop only) | 1 |
| `sys_empty_state` | `sys_empty_state_r01..r02` | 2 |
| **Total** | | **107** |

Stems are not shipped. Every master has four stem files at most (steel, sapphire, cloth, designed), kept in `stems/` for re-mixes.

---

## 7. Handover checklist for engineering

1. Load `manifest.json` at launch; preload every file in families `ui`, `com`, `open`, `vault`, `sys` into memory. Notifications are loaded by the OS.
2. Implement the audio manager against the manifest: round-robin state per ID, velocity layer selection, pitch randomisation within `pitch_random_cents`, the rapid-repeat taper per family, voice limits, `interrupt` semantics, loop start and stop with fades, ducking of `open_bed` under payoffs, and the `reserved` guard.
3. Implement the open sequence as a player of `timeline/open_sequence.json`, with the cycle scheduler driven from the animation clock.
4. Wire haptics from the manifest's `haptic` field: system generators by name, AHAP or JSON by reference. Prepare generators on touch-down.
5. Honour the two user toggles and the silent switch / ringer mode per spec section 8.
6. Run `tools/validate_manifest.py` in CI on the audio repo, and a lightweight check in the app repo that every basename in the manifest exists in both bundles.
