# GemBreak Sound Design — Phase 3: Sourcing Plan

**Status:** Phase 3 deliverable. Built on `audit/sound-spec.md` v1.1. Companions: `audit/library-structure.md`, `audit/licenses.csv`.
**Date:** 2026-09-06
**Rule of the document:** royalty-free does not mean free, and it does not always mean app-distributable. Any source whose coverage of a paid mobile app, or of embedding files in a distributed binary, is not clearly stated in licence text we could read is marked unclear and is not recommended.

---

## 0. Method and caveats

- **Nothing was downloaded.** This is a plan. Every candidate is a link to a page plus the licence facts we could establish.
- **Network limits.** Every sound-library domain (Freesound, Zapsplat, Soundsnap, Epidemic Sound, Artlist, Splice, Kenney, Sonniss, Pixabay, Mixkit, BOOM, A Sound Effect, Soundly, Pro Sound Effects) and web.archive.org were egress-blocked from this environment. Licence texts marked **Full** were read in full from a mirror we could reach: the Creative Commons legal code, Kenney's pack `LICENSE.txt`, the Sonniss bundle licence (2016 text) and downloader ledgers, the Pixabay and Mixkit licences, the OpenGameArt FAQ and OGA-BY text, the Zapsplat and Pro Sound Effects EULA PDFs on S3, the Splice Terms of Use, and the Sound Ideas EULA. Everything marked **Snippet** rests on search-engine excerpts of the cited page. Prices are promotional and regional; confirm at checkout.
- **Candidate licences on Freesound** are recorded as shown in the search snippet or as cited by a project that credits the sound. Every Freesound row must be confirmed on the sound page at download time (Section 7).
- **Sound-event names** quoted for Sonniss bundles come from public file indexes of the bundles; cite bundle year and part in the licence register when a file is used.

---

## 1. Strategy

### 1.1 Priority order, as briefed

1. **CC0 and public domain**: Freesound filtered to CC0, Kenney, BigSoundBank, OpenGameArt CC0/OGA-BY, and Sonniss #GameAudioGDC (free, royalty-free, no attribution, but a proprietary licence rather than CC0).
2. **Flat-fee commercial**: BOOM Library (single-user seat), A Sound Effect indie libraries (check each vendor's EULA), Sound Ideas.
3. **Subscription**: Zapsplat Premium is the only subscription whose licence text we read in full and which names "Games, apps, and software". Envato Elements is acceptable with per-app registration. Soundsnap and Soundly have favourable wording but were not confirmed in full text.
4. **Commissioned custom** for the hero reveal set and everything built from the sapphire instrument.

### 1.2 What the research changed

The brief expected most sounds to be sourced and the hero moments commissioned. The candidate sweeps show the split is different for this product:

- **The recorded cores are cheaper to record than to source.** No free or flat-fee library has a deployant clasp, a watch bracelet, a crown ratchet, a leather-hinged presentation box or velour tissue at the required cleanliness. One half-day session with the actual product packaging and two steel-bracelet watches covers every Steel and Cloth core in the set. The free candidates listed for those rows are fallbacks and prototyping placeholders.
- **The sapphire instrument cannot be sourced.** The spec needs one instrument across five pitches plus a low bell and a bowed drone, dry, consistent, in tune. Stock glass and crystal sounds are single objects of unknown pitch. The two stock options that come close (Hzandbits *Bells & Bowls*, Soniccouture *Glass Works*) are a flat-fee library with unverified pricing and a Kontakt instrument whose EULA for shipping single rendered notes is unclear. Commission it.
- **The designed layer is in-house work, not a purchase.** Sub thumps, glints, sparkle tails, risers and pads are synthesised by the designer. Kenney, BigSoundBank and the Sonniss bundles supply sweeteners and prototyping material at zero licence cost.
- **Exclusivity matters for tier 4.** Kenney and Sonniss sounds appear in thousands of games. A reserved asset that a user has heard in another app is not reserved. Every tier payoff, the case-open strike and the lock are commissioned under work-for-hire terms.

### 1.3 Sourcing tiers per material layer

| Layer | Primary | Fallback | Prototyping placeholder |
|---|---|---|---|
| Steel | Record (session A: watch hardware) | Freesound CC0 (Breviceps UI clicks, DesignDean ratchets), Sonniss 3maze Buttons and Switches, Eiravaein Latchlocker | Kenney Interface Sounds, RPG Audio metalLatch |
| Sapphire | Commission (tuned crystal set, session C) | A Sound Effect: Hzandbits Bells & Bowls, Sonomar Crystal Sing | Kenney Interface glass_001–006 |
| Cloth | Record (session B: presentation box, tissue, velour) | Kenney Casino Audio card-slides, Foley woosh; BigSoundBank whooshes | Same |
| Designed | Synthesise in-house | Sonniss bundles (risers, sub drops, UI zooms), BOOM MAGIC UI or Casual UI for sweeteners | Kenney Digital Audio |

---

## 2. Licence reference: every source checked

| Source | Exact licence | Attribution | Paid mobile app | Embed in app binary | Cost | Evidence | Verdict |
|---|---|---|---|---|---|---|---|
| [Freesound (CC0 filter)](https://freesound.org/search/?f=license:%22Creative+Commons+0%22) | CC0 1.0 Universal | No | Yes | Yes | Free | Full (CC0 text) | **Use; confirm licence on the sound page at download** |
| [Kenney.nl](https://kenney.nl/assets/category:Audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Full (LICENSE.txt mirror) | **Use; prototyping and sweeteners** |
| [Sonniss #GameAudioGDC bundle](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Full (2016 text) / Snippet (2026 text) | **Use for sweeteners; archive the licence text at download** |
| [BigSoundBank](https://bigsoundbank.com/licenses.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | Snippet | **Use; confirm per file** |
| [OpenGameArt (CC0 / OGA-BY filter)](https://opengameart.org/art-search-advanced) | CC0 1.0 or OGA-BY 3.0 | CC0 no; OGA-BY yes | Yes | Yes | Free | Full (FAQ and OGA-BY text mirrors) | **Use; filter out BY-SA and GPL** |
| [Freesound (CC BY 4.0)](https://freesound.org/) | CC BY 4.0 | Yes: creator, title, URL, licence, changes, in a credits screen | Yes | Yes, with a caveat (2(a)(5)(C) technological-measures clause vs app-store DRM) | Free | Full (CC BY text) | **Use sparingly; prefer CC0** |
| [Pixabay](https://pixabay.com/service/license-summary/) | Pixabay Content License (Apr 2023) | No | Yes | Yes if not "Standalone" (licence never names apps) | Free | Full (licence mirror) | **Fallback only; flag** |
| [Mixkit](https://mixkit.co/license/) | Mixkit Sound Effects Free License | No | Yes ("video games", "End Product") | Yes; never in a public source repo ("with source files" clause) | Free | Full (licence mirror) | **Fallback only; flag** |
| [Zapsplat Premium (formerly Gold)](https://zapsplat-assets.s3.amazonaws.com/ZapSplat-EULA-Standard-License.pdf) | ZapSplat EULA (29 Sep 2025) | Premium: No. Basic: credit "ZapSplat" | Yes (§4 "Games, apps, and software") | Yes (not primary value; no redistribution) | ~US$15/mo; annual ~£30 | Full (EULA PDF) | **Use; single-user seat** |
| [BOOM Library](https://www.boomlibrary.com/end-user-license-agreement/) | BOOM Library Single-User EULA (Media License); MULA for teams | No | Yes ("video games and mobile applications") | Yes (pack assets; not as a sample library) | MAGIC UI $139 / CK $209 / bundle $269 intro to 15 Sep 2026; Casual UI CK $189–235; Mechanicals CK $189–235 | Snippet (EULA mirrors) / Snippet (prices) | **Use; one seat per active user** |
| [A Sound Effect (indie libraries)](https://www.asoundeffect.com/license-agreement/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes (incorporated and synchronised) | UI FX $39; others typically tens of USD (unverified) | Snippet | **Use; check each vendor's EULA before purchase** |
| [Sound Ideas](https://sound-ideas.com/pages/sound-ideas-end-user-license-agreement) | Sound Ideas End User License Agreement | No | Yes ("synchronized content for Apps", games) | Yes | Per product (unverified) | Full (mirror) | **Use if needed; one workstation** |
| [Envato Elements / AudioJungle](https://audiojungle.net/licenses/terms/audio_sfx_media_single) | Envato SFX Single Use / Elements per-project registration | No | Yes ("apps, games" as End Product) | Yes | Elements $16.50/mo annual | Snippet | **Acceptable; register once per app** |
| [Soundsnap](https://www.soundsnap.com/licence) | Soundsnap Sound Effects License | No | Stated yes ("apps, video games"); full text unread | Unclear | $149/6 mo; $199–269/yr | Snippet | **Not recommended until confirmed in writing** |
| [Soundly Pro](https://getsoundly.com/soundly-eula/) | Soundly EULA (4 Nov 2024) | No | Games yes; non-game apps unnamed | Likely | $14.99/mo | Snippet | **Not recommended until confirmed in writing** |
| [Splice Sounds](https://splice.com/terms) | Splice Terms of Use §3.1 (22 Aug 2024) | No | Unclear (video games named; apps not; one-shots "in isolation" clause) | Unclear | $12.99–39.99/mo | Full (ToU mirror) | **Not recommended** |
| [Pro Sound Effects (Individual EULA)](https://prosoundeffects.s3.amazonaws.com/Pro%20Sound%20Effects%20Individual%20End%20User%20License%20Agreement.pdf) | PSE Individual End User License Agreement (Oct 2024) | Credit if others credited | Unclear (synchronised use only; interactive needs Custom Application License) | Only with Custom Application License | CORE $1,499–11,999 lifetime | Full (EULA PDF) | **Not recommended without a Custom Application License** |
| [Soniccouture Glass Works (Kontakt instrument)](https://www.soniccouture.com/en/products/35-rare-and-unique/g14-glass-works/) | Soniccouture instrument EULA | No | Unclear for shipping single rendered notes as UI assets | Unclear | Unverified | Snippet | **Not recommended without written confirmation** |
| [Epidemic Sound](https://www.epidemicsound.com/policy/business-subscription/) | Personal / Commercial / Business subscription policies | No | No on self-serve (video and podcast sync only); Enterprise only | No | $9.99–30/mo; Enterprise custom | Snippet | **Do not use** |
| [Artlist](https://artlist.io/help-center/privacy-terms/artlist-license/) | Artlist License (15 Feb 2026) §11 | No | No ("App, Software, games and their end-users" = Enterprise) | No | $9.99–39.99/mo | Snippet (strong) | **Do not use** |
| [Uppbeat](https://uppbeat.io/user-agreement) | Uppbeat User Agreement | Free yes / paid no | Unclear (defined by publishing platforms; apps unnamed) | Unclear | Business $18.99/mo | Snippet | **Do not use** |
| [Motion Array](https://help.motionarray.com/hc/en-us/articles/9442171935005-How-Does-The-License-Work) | Standard / Business | No | No (apps, software, games need a dedicated business licence) | No | n/a | Snippet | **Do not use** |
| [BBC Sound Effects (RemArc)](https://sound-effects.bbcrewind.co.uk/licensing) | RemArc Licence | Yes | No (non-commercial only) | No | Free (commercial via PSE) | Full (PDF) | **Do not use** |

**Reading the verdicts.**
- *Use*: licence text we read, or a strong snippet, names games or apps and permits distribution inside a product.
- *Fallback only; flag*: permits the use but the licence never names apps (Pixabay), or carries a clause that is easy to breach in practice (Mixkit's "with source files").
- *Not recommended until confirmed*: wording is favourable but the full text was unread or apps are unnamed. Written confirmation from the vendor lifts this.
- *Do not use*: the licence excludes apps, software or games on the plans a small team would buy, or is non-commercial.

---

## 3. Sourcing table: every sound in the spec

For each event ID: the layer composition from the spec, the plan, and the candidates in priority order. The first candidate is the primary and is the one recorded in `audit/licenses.csv`. "Session A" is the watch-hardware recording, "Session B" the presentation-box and tissue recording, "Session C" the sapphire instrument recording; all three fit in one studio day (Section 4).

#### UI

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `ui_tap` | Steel core + designed glint | Record steel; synthesise glint | Record in-house (GemBreak session): Bracelet links, close-miked on felt (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary; 4 takes for round-robin |
|  |  |  | Freesound (CC0 filter): [Breviceps: Clicks, Buttons & UI sounds pack (metallic file select click)](https://freesound.org/people/Breviceps/packs/25371/) | CC0 1.0 Universal | No | Yes | Yes | Free | Fallback core; licence shown CC0 in snippet, confirm on page |
|  |  |  | Kenney.nl: [Interface Sounds: click_001–005, tick_001/002/004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder only; synthetic character |
| `ui_toggle_on` | Steel clasp half-click + E6 ping | Record clasp; commission ping | Record in-house (GemBreak session): Deployant clasp half-engage (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: toggle_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
|  |  |  | Sonniss #GameAudioGDC bundle: [3maze Buttons and Switches: switch_on_042 (GDC 2016 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Real mechanical click; sweetener |
| `ui_toggle_off` | Steel clasp, damped + B5 ping | Record clasp; commission ping | Record in-house (GemBreak session): Deployant clasp release, damped (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: toggle_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `ui_tab` | Cloth brush + steel tick + glint | Record cloth and tick | Record in-house (GemBreak session): Velour brush + link tick (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Casino Audio: card-slide-1–8 (cloth layer); Interface Sounds tick_001](https://kenney.nl/assets/casino-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Airy card pass; not slot-like |
|  |  |  | Sonniss #GameAudioGDC bundle: [L.A. Sounds Game & UI Interface 001: Hovers 03 (GDC 2019 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed alternative |
| `ui_sheet_open` | Tissue lift + designed air sweep | Record tissue; synthesise sweep | Record in-house (GemBreak session): Tissue paper lifted from the presentation box (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Foley Sounds: woosh1–8](https://kenney.nl/assets/foley-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Air layer |
|  |  |  | BigSoundBank: [Whoosh 9 (and 5/6/10)](https://bigsoundbank.com/whoosh-9-s1802.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | Short clean whoosh, CC0 |
| `ui_sheet_close` | Tissue settle + air falling | Record tissue; synthesise sweep | Record in-house (GemBreak session): Tissue laid down (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | BigSoundBank: [Whoosh 5/6 reversed](https://bigsoundbank.com/whoosh-9-s1802.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | Reverse for the fall |
|  |  |  | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation 2: UI Zooms (GDC 2024 pt 1)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed alternative |
| `ui_back` | Steel tick, lower + glint falling | Record | Record in-house (GemBreak session): Link tick, lower velocity (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: back_001–004 (61–94 ms)](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
|  |  |  | Sonniss #GameAudioGDC bundle: [Kpow Sounds UI Soundpacks: Back Version4 (GDC 2015 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed alternative |
| `ui_error` | Damped clasp refusal + designed low thud | Record clasp; synthesise thud | Record in-house (GemBreak session): Clasp pressed against its stop, damped (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [Raclure: Cancel/miss chime](https://freesound.org/people/Raclure/sounds/405548/) | CC0 1.0 Universal | No | Yes | Yes | Free | Soft tonal fallback; confirm licence |
|  |  |  | Sonniss #GameAudioGDC bundle: [David Dumais UI Menu: Access_Denied_High_DDM16 (GDC 2020 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed fallback |
| `ui_success` | Sapphire E5→B5 + sparkle | Commission (sapphire instrument) | Commission (sound designer, work for hire): Two notes from the tuned sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; same instrument as all confirmations |
|  |  |  | A Sound Effect (indie libraries): [Hzandbits: Bells & Bowls (14 tuned glass and ceramic bells, multisampled)](https://www.asoundeffect.com/sound-library/bells-bowls/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes (incorporated and synchronised) | UI FX $39; others typically tens of USD (unverified) | Closest stock one-instrument set; price unverified |
|  |  |  | Kenney.nl: [Interface Sounds: glass_001–006](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder; synthetic |
| `ui_disabled` | Dull damped tick | Record | Record in-house (GemBreak session): Link tick against cloth, heavily damped (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: tick_004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |

#### Commerce

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `com_add_to_cart` | Clasp half-click + sapphire G♯5 + glint | Record clasp; commission tone | Record in-house (GemBreak session): Clasp half-engage (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary core |
|  |  |  | Commission (sound designer, work for hire): G♯5 from the sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary tone |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_001](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `com_purchase_confirmed` | Sapphire E5→B5, E6 shimmer | Commission | Commission (sound designer, work for hire): Sapphire two-note figure with shimmer; paired AHAP | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; hero confirmation |
|  |  |  | Sonniss #GameAudioGDC bundle: [Chris Logsdon Ambient Puzzle: Success 2a (GDC 2019 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Reference and fallback |
|  |  |  | A Sound Effect (indie libraries): [Hzandbits: Bells & Bowls](https://www.asoundeffect.com/sound-library/bells-bowls/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes (incorporated and synchronised) | UI FX $39; others typically tens of USD (unverified) | Stock fallback |
| `com_payment_failed` | Clasp refusal + low thud + damped settle | Record clasp; synthesise thud | Record in-house (GemBreak session): Clasp refusal, two-stage (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [CB Sounddesign Activation UI & HUD: Negative_Notification_25 (GDC 2018 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed fallback |
|  |  |  | Kenney.nl: [Interface Sounds: error_004; Digital Audio lowDown](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |

#### Open sequence

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `open_box_select` | Clasp click + designed body + E5 confirm | Record clasp; synthesise body; commission glint | Record in-house (GemBreak session): Full clasp click, heavier take (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary core |
|  |  |  | Sonniss #GameAudioGDC bundle: [InspectorJ UI Mechanical: UI_Mechanical_Confirm_04_FX (GDC 2019 pt 2)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Designed fallback |
|  |  |  | Kenney.nl: [Interface Sounds: click_001 + confirmation_002](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `open_box_enter` | Box slide on cloth + set-down knock + low body | Record box | Record in-house (GemBreak session): Presentation box slid and set on wood and leather (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [VizAion: Wood, Hit, Inside Piano, Very Low](https://freesound.org/people/VizAion/sounds/795634/) | CC0 1.0 Universal | No | Yes | Yes | Free | Sub-thump layer; confirm licence |
|  |  |  | Kenney.nl: [Impact Sounds: impactSoft_heavy_000–004](https://kenney.nl/assets/impact-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Layering fallback |
| `open_bed` | Bowed sapphire drone + designed pad, E and B | Commission | Commission (sound designer, work for hire): Bowed crystal E3/E4 + B3/B4 with a soft pad, 8 s seamless loop | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [bassimat: Warm Pad Essentials Drone by Mantice](https://freesound.org/people/bassimat/sounds/854842/) | CC0 1.0 Universal | No | Yes | Yes | Free | Pad fallback; confirm licence |
|  |  |  | Freesound (CC BY 4.0): [InspectorJ: Glass Harp, C, Sustained (note series; paid attribution-free option offered)](https://freesound.org/people/InspectorJ/sounds/416279/) | CC BY 4.0 | Yes: creator, title, URL, licence, changes, in a credits screen | Yes | Yes, with a caveat (2(a)(5)(C) technological-measures clause vs app-store DRM) | Free | Bowed-glass fallback; attribution or buy the attribution-free licence |
| `open_box_crack` | Magnetic clasp release + leather hinge + rising light tone | Record box; synthesise light tone | Record in-house (GemBreak session): Presentation box lid cracked a few degrees, magnetic clasp (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [3maze Doors, Locks and Drawers; InMotionAudio Instrument Case (GDC)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Hinge and latch fallbacks |
|  |  |  | Freesound (CC0 filter): [wlabarron: Magnetic latch cupboard door](https://freesound.org/people/wlabarron/sounds/509112/) | CC0 1.0 Universal | No | Yes | Yes | Free | Licence not visible in snippet; verify before use |
| `open_tell_t2` | Sapphire B4 in the light | Commission | Commission (sound designer, work for hire): B4 from the sapphire set, soft mallet | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
| `open_tell_t3` | Sapphire D♯5 shimmer + sparkle tail | Commission | Commission (sound designer, work for hire): D♯5 from the sapphire set with designed sparkle | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
| `open_box_open` | Lid swing air + designed open tone + lid settle tick | Record lid; synthesise tone | Record in-house (GemBreak session): Lid swung fully open to its stop (session B); T4 variant with added E3 body | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [InMotionAudio Instrument Case; MatiasMacSD The Case; Sonic Bat Music Boxes (GDC)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Case-lid fallbacks |
|  |  |  | Kenney.nl: [RPG Audio: bookOpen (placeholder only)](https://kenney.nl/assets/rpg-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `open_cycle_pass` | Cloth pass + glass glint per pitch step | Layer sourced cloth with commissioned glint | Kenney.nl: [Casino Audio: card-slide-1–8 (cloth layer)](https://kenney.nl/assets/casino-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Airy pass, no click; not slot-like |
|  |  |  | BigSoundBank: [Whoosh 5/6/9/10 (0.37–0.54 s)](https://bigsoundbank.com/whoosh-9-s1802.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | Alternative air layer |
|  |  |  | Commission (sound designer, work for hire): Glint at E5, F♯5, G♯5, B5, C♯6 from the sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Tonal layer; commission if layered result lacks unity |
| `open_cycle_blur` | Continuous rising shimmer + filtered-noise sweep | Synthesise | Synthesise in-house: Filtered-noise sweep + granular smear of the pass glints, resolving toward E6 | Owned | No | Yes | Yes | Designer time | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [3maze Rise & Swell; Daumantas Ercmonas Uplifter pack (GDC)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Riser references and fallback |
| `open_select_lock` | Steel latch + sub thump + 250–400 Hz knock + E5 glint | Record latch; synthesise sub; commission glint | Record in-house (GemBreak session): Deployant clasp full lock and case-back click (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary core |
|  |  |  | Sonniss #GameAudioGDC bundle: [Eiravaein Sound Latchlocker: steel lever small close/snap (GDC 2017 pt 3)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Strongest stock match; sweetener |
|  |  |  | Kenney.nl: [RPG Audio: metalLatch, metalClick](https://kenney.nl/assets/rpg-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `open_case_open` | Case hinge + air + sapphire strike E5 + shimmer | Record hinge; commission strike | Record in-house (GemBreak session): Watch presentation case hinge and lid (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary mechanical layer |
|  |  |  | Commission (sound designer, work for hire): Sapphire strike E5, three takes, two velocities | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary tonal layer; hero |
|  |  |  | A Sound Effect (indie libraries): [Sonomar Collection: Crystal Sing (46 files, 192 kHz)](https://www.asoundeffect.com/sound-library/sonomar-collection-crystal-sing/) | A Sound Effect End-User License Agreement (some vendors attach their own) | No | Yes ("mobile apps... video games") | Yes (incorporated and synchronised) | UI FX $39; others typically tens of USD (unverified) | Stock fallback for the strike; price unverified |
| `open_payoff_t1` | Strike ring + short sparkle | Commission | Commission (sound designer, work for hire): Sapphire E5 decay with designed sparkle | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
| `open_payoff_t2` | Sapphire E5→B5 + sparkle + bed swell | Commission | Commission (sound designer, work for hire): Two-note figure from the sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
| `open_payoff_t3` | Three-note figure + sub thump + E6 afterglow | Commission | Commission (sound designer, work for hire): E5→G♯5→B5 with afterglow E6; short stinger | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [Cinematic Sound Design User Interface: Button Arp Twinkle (GDC 2026)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Reference only |
| `open_payoff_t4` | Strike + low bell E4 + sub + four-note figure + long sparkle | Commission | Commission (sound designer, work for hire): Full stinger with low crystal bowl E4; reserved asset | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary; must be exclusive to GemBreak |
|  |  |  | Freesound (CC0 filter): [zambolino: singing bowl (35 s, 44.1/24) as low-bell reference](https://freesound.org/people/zambolino/sounds/439235/) | CC0 1.0 Universal | No | Yes | Yes | Free | Reference only; metal bowl, pitch unstated |
| `open_bed_t4_post` | Wide slow post-bed, E major add 9 with D♯ | Commission | Commission (sound designer, work for hire): Bowed crystal chord, 12 s seamless loop; reserved asset | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Sonniss #GameAudioGDC bundle: [Airborne Sound: Light and Dark Drones; Raconteur Crystal Glasses Tones and Drones (GDC)](https://sonniss.com/gameaudiogdc) | Sonniss GDC Bundle License (v2.0, 2026) | No | Yes ("games... interactive projects"; the word app does not appear) | Yes, as part of the project; never as raw files | Free | Reference only |
| `open_settle` | Bed fade + soft cloth movement + room tone | Record tissue | Record in-house (GemBreak session): Tissue laid back into the box; room tone (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Foley Sounds: woosh (softest takes)](https://kenney.nl/assets/foley-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Fallback |

#### Vault

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `vault_added` | Clasp full close + designed lock body + sapphire E5 | Record clasp; synthesise body; commission tone | Record in-house (GemBreak session): Deployant clasp full close (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [RPG Audio: metalLatch + Interface glass_001](https://kenney.nl/assets/rpg-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |

#### Fulfilment

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `ship_requested` | Cloth fold + sapphire G♯5 | Record cloth; commission tone | Record in-house (GemBreak session): Tissue folded over the box (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Casino Audio: cards-pack-take-out-1/2](https://kenney.nl/assets/casino-audio) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Fallback cloth |

#### Notifications

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `notif_shipped` | Sapphire E5→G♯5 + sparkle | Commission | Commission (sound designer, work for hire): Two notes from the sapphire set, notification master (CAF/OGG) | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | BigSoundBank: [Notification lasomarie 1–5 (0.3–0.4 s)](https://bigsoundbank.com/notification-lasomarie-1-s2059.html) | CC0 1.0 / WTFPL | No | Yes | Yes | Free | CC0 fallback |
| `notif_delivered` | Sapphire E5→B5→E6 | Commission | Commission (sound designer, work for hire): Three notes from the sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [mpaol2023: 3-tone chime](https://freesound.org/people/mpaol2023/sounds/370179/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 fallback; confirm licence |

#### System

| ID | Layers | Plan | Candidate | Exact licence | Attribution | Paid app | Binary | Cost | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `sys_notification` | Sapphire E5 + B5 dyad + glint | Commission | Commission (sound designer, work for hire): Dyad from the sapphire set | Work for hire, worldwide, perpetual, all media | No | Yes | Yes | Per-asset fee (see §5) | Primary |
|  |  |  | Freesound (CC0 filter): [Jofae: Chime Notification (0.3 s)](https://freesound.org/people/Jofae/sounds/380482/) | CC0 1.0 Universal | No | Yes | Yes | Free | CC0 fallback; confirm licence |
|  |  |  | Kenney.nl: [Interface Sounds: confirmation_001–004](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `sys_refresh_threshold` | Steel tick B5 + glint | Record | Record in-house (GemBreak session): Link tick (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: tick_001](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `sys_refresh_complete` | Brighter steel tick C♯6 | Record | Record in-house (GemBreak session): Link tick, brighter (session A) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Interface Sounds: tick_002](https://kenney.nl/assets/interface-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Prototype placeholder |
| `sys_loading_loop` | Mechanical movement at 8 beats per second, 4 s seamless loop | Source CC0 or record | Freesound (CC0 filter): [hannagreen: wristwatch-ticking-SE_mono (~19 s, foam-isolated)](https://freesound.org/people/hannagreen/sounds/256212/) | CC0 1.0 Universal | No | Yes | Yes | Free | Primary if beat rate is 4 Hz; confirm licence on page |
|  |  |  | Freesound (CC BY 4.0): [bySeb: Automatic Wrist Watch Ticking, Omega Seamaster ETA 2892 (41 s)](https://freesound.org/people/bySeb/sounds/326478/) | CC BY 4.0 | Yes: creator, title, URL, licence, changes, in a credits screen | Yes | Yes, with a caveat (2(a)(5)(C) technological-measures clause vs app-store DRM) | Free | ETA 2892 = 28,800 vph = exactly 4 Hz; attribution "byseb.at"; check noise-reduction hiss |
|  |  |  | Record in-house (GemBreak session): Any 28,800 vph movement, contact mic, in the session | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Fallback; 15 minutes |
| `sys_empty_state` | Soft cloth hush | Record tissue | Record in-house (GemBreak session): Tissue settle, softest take (session B) | Work for hire / owned | No | Yes | Yes | Session cost (see §5) | Primary |
|  |  |  | Kenney.nl: [Foley Sounds: woosh (softest)](https://kenney.nl/assets/foley-sounds) | CC0 1.0 (pack LICENSE.txt) | No (optional) | Yes | Yes | Free | Fallback |

---

## 4. What is commissioned instead of sourced

### 4.1 The commission

One sound designer engaged on work-for-hire terms (worldwide, perpetual, all media including marketing, trailers and haptic derivatives), delivering:

| Deliverable | Files | Why it cannot be sourced |
|---|---|---|
| The sapphire instrument: tuned crystal set sampled at E4, E5, F♯5, G♯5, B5, C♯6, D♯5, E6 at two velocities with three round-robins, plus a low crystal bowl at E4 and bowed sustains at E3, E4, B3, B4 | Source recordings, not shipped | One instrument across every pitched sound in the app; no library provides it |
| Tier payoffs T1–T4 (with T1 and T2 round-robins) | 6 | Escalating family in one key with designed layers; T4 must be exclusive |
| Case-open strike (3 × 2 velocities) and selection lock tonal layer | 6 + glints | Constant reveal moment; exclusivity |
| Cycle pass glints for six pitch steps | 12 (layered with sourced cloth) | Pitch-locked to the key |
| Both beds (8 s and 12 s seamless loops) | 2 | Harmonic identity; T4 post-bed exclusive |
| Purchase confirmed, success, add-to-cart tone, vault tone, ship tone, three notification chimes, two tier tells, cycle blur | 11 | All built from the sapphire instrument |
| Production of the remaining recorded and sourced material into finished masters: UI family, box events, settle, loading loop | ~67 | Editing, layering with designed sweeteners, loudness normalisation to the ladder, exports |
| Haptic patterns: AHAP and Android JSON for the 14 composite events, QA on three device classes | 28 | Audio-haptic sync is part of the sound |

### 4.2 The recording day

| Session | Materials | Time | Captures |
|---|---|---|---|
| A: watch hardware | Two steel-bracelet watches with deployant clasps, one dive bezel, one 28,800 vph movement, felt pad, contact mic and a small-diaphragm condenser pair | 2 h | Bracelet chatter, clasp half and full engage and release, clasp refusal, crown ratchet singles and trains, bezel clicks, case-back click, movement ticking |
| B: presentation box | The actual GemBreak box and the watch case it contains, tissue, velour pouch, wood and leather surfaces | 2 h | Slide and set-down, lid crack with magnetic clasp, full open to stop, hinge of the watch case, tissue lift, lay and fold, velour brush, room tone |
| C: sapphire instrument | Five water-tuned crystal stems or a glass-harp set, one large crystal bowl, felt and rubber mallets, bow | 3 h | Struck tones at all target pitches, two velocities, three round-robins; bowed sustains; low bowl strikes |

A treated room with an engineer in London, New York or Los Angeles runs at the rates in Section 5. If the designer self-records, the day is charged at their day rate and the room cost falls away.

### 4.3 Rights language for the brief

State at brief stage: work for hire; assignment of all rights in the recordings and masters; worldwide, perpetual, all media including in-app, marketing, store previews, video and haptic derivatives; no reuse of the sapphire instrument or any tier-4 material in other projects; designer may keep a portfolio credit. Expect this to add 25–50 % over a non-exclusive quote, or to double a quote priced as a licence.

---

## 5. Cost

Three envelopes. Ranges are from the benchmarks gathered (day rates, per-asset rates, room rates, library prices) and are marked where estimated. Currency USD unless noted.

### 5.1 Recommended

| Line | Basis | Low | High |
|---|---|---|---|
| Recording day: treated room with engineer | Half to full day, LA/NY/London rates | 1,200 | 2,500 |
| Crystal set purchase (five tuned stems or glass-harp set, one bowl) | Estimate | 150 | 400 |
| Commission: hero set, ~30 files at 150–400 each | Per-asset benchmark for bespoke work with revisions | 4,500 | 12,000 |
| Commission: production of the remaining ~77 files, mix, master, exports | 6–10 designer days at 450–650 | 2,700 | 6,500 |
| Haptic authoring and device QA | 3–5 designer days | 1,500 | 5,000 |
| Zapsplat Premium, three months (or Gold annual ~£30) | Verified plan | 40 | 45 |
| BOOM Library MAGIC UI bundle (intro price to 15 Sep 2026) or Casual UI construction kit | Verified snippet | 189 | 269 |
| A Sound Effect: UI FX $39, Micro Mechanisms, Bells & Bowls, Paper Foley | UI FX verified; others estimated at 40–80 each | 160 | 280 |
| Kenney, Sonniss #GameAudioGDC, BigSoundBank, OpenGameArt | Free; optional Kenney donation | 0 | 20 |
| Contingency 15 % | | 1,560 | 4,050 |
| **Total** | | **≈ 12,000** | **≈ 31,000** |

A realistic midpoint is **≈ $18,000–20,000**.

### 5.2 Lean

Designer self-records in one day at their day rate (450–650) plus the crystal set (150–400); commission only the sapphire instrument, four tier payoffs, case-open strike and lock (~15 hero files at 150–250: 2,250–3,750); five production days (2,250–3,250); two haptic days (900–1,300); libraries limited to Zapsplat Gold and A Sound Effect UI FX (~80); everything else Kenney, Sonniss and BigSoundBank. **≈ $6,000–9,500.** The cost is fewer round-robins, no studio room, and a thinner designed layer.

### 5.3 Studio sonic identity

A sonic-branding studio delivering the identity, the full set and haptics: **≈ $35,000–80,000**, with published agency ranges running from about €30,000 into six figures. Worth it only if GemBreak wants the reveal motif to carry into advertising and brand audio from day one.

### 5.4 What is not in these numbers

Ongoing subscriptions after delivery (none are needed once files are downloaded under a perpetual licence; Zapsplat Premium downloads stay licensed for life), a second audio seat for BOOM or Pro Sound Effects, localisation, or a music score.

---

## 6. Flags: unclear or excluded for commercial app distribution

Do not use these without the stated action.

| Source | Problem | Action if it must be used |
|---|---|---|
| Epidemic Sound Personal / Commercial | Licence is video and podcast synchronisation; games routed to Enterprise; "Business Plus adds rights for apps" seen only in an unreadable snippet | Enterprise agreement in writing |
| Artlist, all self-serve plans | §11: "App, Software, games and their end-users" are an Enterprise case | Enterprise agreement in writing |
| Motion Array | Apps, software and games explicitly need a dedicated business licence | Business licence |
| Uppbeat | Coverage defined by publishing platforms; apps, games and software never named | Written confirmation |
| Splice | "Video games" named, apps not; the ban on sublicensing sounds "in isolation as sound effects" sits badly with shipping unmodified one-shots | Do not use for UI one-shots; written confirmation for anything else |
| Pro Sound Effects Individual EULA | Synchronised use only; interactive use needs a Custom Application License; one person, one computer | Custom Application License |
| Soundsnap | Wording says "apps, video games"; full text unread | Written confirmation, then acceptable |
| Soundly | Games yes; non-game apps unnamed | Written confirmation, then acceptable |
| Storyblocks | Games named; apps not; Individual licence is per person | Written confirmation and Business licence |
| Soniccouture Glass Works | Instrument EULA for shipping single rendered notes as UI assets is unclear | Written confirmation; otherwise commission the instrument |
| Pixabay | Licence never names apps; "Standalone" test is a judgement call for an unmodified click | Fallback only; modify or layer every file; keep files out of any public repo |
| Mixkit | "with source files" clause: any public repository containing the file is a literal breach | Fallback only; private storage |
| Sonniss #GameAudioGDC v2.0 (2026) | New clause bars supplying sounds "as sound effects" in any "software development kit or anything similar"; an app is not an SDK, but a user-facing sound picker or exported theme pack could be | Never expose raw files to users; archive the licence text at download |
| Freesound CC BY | Attribution is workable in a credits screen; the clause on "technological measures" was written before app-store DRM and OGA-BY exists because of it | Prefer CC0; keep CC BY to a few files, credit fully |
| Freesound CC BY-NC, Sampling+ | Non-commercial; advertising barred | Never |
| BBC Sound Effects (RemArc) | Non-commercial only | Never; commercial route is Pro Sound Effects |

---

## 7. Process: from plan to licensed files

1. **At download**, for every third-party file: screenshot the sound page showing the licence, save the licence text as `LICENSE.txt` beside the file in `sourced/<source>/<id>/`, and complete the row in `licenses.csv` (status `confirmed`, licence as shown, date, downloader).
2. **Freesound**: use the CC0 filter in search; on each sound page confirm the licence badge reads "Creative Commons 0" before download. Do not rely on the snippet.
3. **Sonniss**: keep the bundle's licence file with the bundle; record year and part per file.
4. **Purchases**: save the invoice and the EULA version in force at purchase; one seat per active audio user.
5. **Commission**: signed agreement with the rights language in 4.3 before the session; deliverables include stems, masters, session files and the loudness report.
6. **Attribution screen**: an "Audio credits" entry in Settings → About, listing every CC BY file (creator, title, URL, licence, changes), Kenney by courtesy, and "Sound effects: Sonniss #GameAudioGDC" by courtesy. Nothing else in the set requires credit.
7. **Legal review** of `licenses.csv` before the first TestFlight or Play internal build that contains third-party audio.
8. **Validation**: `tools/validate_manifest.py` (see `audit/library-structure.md`) refuses to build if any shipped file lacks a `confirmed` licence row.
