# GemBreak — Blender Animator Briefs: Watch Reveal Animations

_Compiled 2026-07-29. Two ready-to-hand briefs for a Blender artist. Prompt A = the signature GemBreak
mystery-pack watch reveal (elevated version of the IcyBox-style opening — dopamine-engineered, replayable).
Prompt B = the separate "crystal case shatter" concept. Note: the reference video couldn't be decoded in
this environment, so Prompt A is built from the mystery-pack reveal format itself, pushed to be more
impressive/impactful._

---

## The psychology to engineer (both briefs obey this)
A reveal creates a "core memory you want to replay" by hitting these beats in order:
1. **Anticipation** — quiet, slow, tension building (silence before the drop).
2. **Escalation in stages** — never one beat; build → build → BREAK (dopamine loves the staircase).
3. **A fake-out / near-miss** — a half-second where it looks ordinary, then it isn't.
4. **The HIT** — sudden multi-sensory payoff (light burst + bass + particles) on one frame.
5. **Rarity signal** — the reward's tier is unmistakable (color, aura, scale).
6. **Savor** — slow-motion + a clean hero shot lingered on (let them breathe it in).
7. **Loopable resolution** — ends where it could restart (rewatch value).

---

# PROMPT A — "GemBreak Signature Watch Reveal" (hand this to the Blender artist)

Create a **~7–9 second, 9:16 vertical (1080×1920), 60fps** cinematic product-reveal animation in Blender
(Cycles for caustics/realism; EEVEE Next acceptable for speed). A premium mystery "gem pack" floats in a
dark, moody void and violently reveals a luxury watch. The feel: **Apple-keynote polish meets a slot-machine
jackpot** — restrained, then explosive.

**Scene & staging**
- Environment: near-black studio void, subtle radial gradient, faint volumetric haze (god-rays later).
- Hero object at start: a **faceted gemstone/crystal "pack"** (GemBreak's motif) suspended center-frame,
  slowly rotating, catching light on its edges. Inside, a watch is dimly visible through the refraction.
- Ground: a subtle reflective floor (soft reflection, not a mirror) for grounding + light bounce.

**Beat sheet (with frame timing @ 60fps)**
- **0.0–2.0s (Anticipation):** camera slow dolly-in on the rotating gem; ambient hum; a single rim light
  traces the facets; everything quiet and premium. A faint heartbeat-like pulse of inner light (tease).
- **2.0–3.0s (Escalation):** the gem starts to **vibrate/shudder**, inner light intensifies in pulses (each
  pulse brighter), micro-cracks of light appear along the facets, dust particles lift off. Camera pushes
  closer, slight handheld shake added.
- **3.0–3.3s (Fake-out):** everything **freezes and dims for ~8 frames** — dead silence, near-black. (The
  pause is the dopamine setup — do not skip it.)
- **3.3s (THE HIT — one frame):** the gem **detonates** — a white-hot light burst fills frame, shards +
  energy particles explode outward with heavy **motion blur**, a shockwave ring distorts the haze. This is
  the bass-drop frame.
- **3.3–5.5s (Reveal, slow-mo):** **time ramps to ~30% speed.** As the light blooms down, the **watch
  emerges** rotating slowly from the core, suspended in a beam, shards drifting past in slow motion, a
  **tier-colored aura** (see below) radiating behind it. Caustics/refraction sparkle across the dial and
  crystal. Camera orbits ~30° around it.
- **5.5–8.0s (Savor + hero):** speed ramps back to normal; the watch settles into a clean **hero
  three-quarter shot**, rim-lit, a slow specular glint travels across the crystal and bracelet; a soft
  particle shimmer settles; the GemBreak wordmark can fade in lower-third. Ends on a held, loop-ready frame.

**Rarity aura (make this a swappable parameter)** — the burst + aura color signals the tier so one rig
serves all tiers: **Quartz = cool white/silver · Emerald = green · Sapphire = deep blue · Diamond = prismatic
rainbow caustics + gold sparks.** Bigger tier = bigger burst, more particles, longer slow-mo.

**Technical direction (Blender specifics)**
- **Shatter:** Cell Fracture add-on on the gem → Rigid Body World, bake the explosion; add a Force Field
  (Explode/Wind) at the hit frame for the outward blast.
- **Particles:** one system for glass shards (instanced low-poly crystals), one for glowing energy sparks
  (emission, size-over-life), one for lingering dust (volumetric-lit).
- **Materials:** gem = Glass BSDF + volume absorption tinted to tier + strong IOR (~1.8) for caustics;
  watch = realistic metal/PBR (polished steel/gold), sapphire-crystal dial with clearcoat. Enable Cycles
  caustics (or bake fake caustics via projected light).
- **Lighting:** 3-point (key area light, cool rim, warm kicker) + an animated **burst light** that spikes to
  huge strength for ~3 frames at the hit; HDRI at low strength for reflections.
- **Camera:** 35–50mm, shallow **DOF** (racks focus from gem shell → watch dial on reveal), **motion blur ON**,
  subtle handheld noise via a constraint; the **speed ramp** via Time Remapping / the graph editor.
- **Compositor:** heavy **Bloom/Glare** (fog glow) on the hit, **lens distortion + chromatic aberration**
  pulse on the shockwave frame, slight film grain, a vignette, and a final **bloom bleed** on the watch glints.
- **Motion polish:** ease-in/ease-out on every camera move; the hit should be on a single sharp keyframe
  (no ease) so it snaps.

**Sound cues (for the editor, so animation syncs to audio)** — rising sub-drone through 0–3s → a sucking
"silence" at the fake-out → a **massive bass drop + glass-shatter + choir/synth stab** on the hit frame →
airy shimmer/reverb tail through the reveal. Every visual accent lands on a transient.

**Deliverables:** the master 7–9s clip + a **3s "hit-only" cut** (fake-out → HIT → reveal) for short-form,
+ an **alpha/transparent-background** render of the shatter and the watch beam so the editor can composite it
over live pack-opening footage or any background.

---

# PROMPT B — "Crystal Case Shatter Reveal" (the separate concept)

Create a **~6–8s, 9:16 vertical, 60fps** Blender animation. A luxury watch sits sealed inside a **solid
crystal/glass case** in a dark, premium void. An **invisible force** strikes the case in escalating hits
until it shatters, revealing the watch.

**Beat sheet**
- **0.0–1.5s:** the crystal watch case floats center-frame, slowly rotating, catching sharp rim light;
  caustics dance on the floor; the watch is visible but distorted through the thick refracting glass.
  Calm, expensive, quiet.
- **1.5–2.0s (Hit 1):** an **unseen impact** — the case jolts (sharp position/rotation snap + settle), a
  **single hairline crack** spiders across the front glass with a bright fracture-line flash; a few dust
  particles puff off; a low "tink." Camera micro-shake on impact.
- **2.5–3.0s (Hit 2):** **stronger jolt** — the case shakes harder, the crack **branches into a web**, a
  second and third fracture join it, a small chunk or two loosens, light leaks brighter from inside. Tension
  rising.
- **3.5–3.8s (Hit 3 — the shatter):** a **massive invisible blow** — the entire case **explodes into
  glass**, shards flying outward toward camera in **slow-motion (~25–35% speed)** with heavy motion blur,
  refraction/caustics scattering rainbow light through every shard, a shockwave ring in the haze.
- **3.8–6.0s (Reveal, slow-mo):** as shards drift past and fall, the **watch is revealed** suspended in a
  light beam, rotating slowly, pristine, a tier-colored aura behind it, glints traveling across the dial.
- **6.0–8.0s (Hero + settle):** speed returns to normal, shards settle/dissolve, the watch lands in a clean
  hero shot, specular glint sweep, GemBreak wordmark optional, loop-ready end frame.

**Technical direction (Blender specifics)**
- **Progressive cracks:** don't fully fracture until Hit 3. For Hits 1–2, animate **emissive crack decals /
  animated textures** (or a growing "fracture line" mesh with an emission shader) across the glass surface so
  the cracks *spread* on cue. Use a **Build/mask or animated factor** to reveal the crack network over time.
- **The shatter:** **Cell Fracture** the case into ~150–400 shards (mix sizes; smaller near impact),
  pre-fractured but held together by Rigid Body Constraints; **break the constraints on Hit 3** and fire an
  **Explode/Force Field** from the impact point so glass flies toward camera. Bake the sim.
- **Invisible force:** sell it with **secondary motion** — the case's jolt (snap keyframes), a subtle
  air-distortion/heat-haze ripple at each impact (compositor lens/displace), and dust/particle puffs at the
  contact point. No visible object — the reaction *is* the force.
- **Glass material:** Glass BSDF, high IOR (~1.6–1.8), slight roughness variation, volume absorption for a
  faint tint; **Cycles caustics ON** (or projected fake caustics) so shards throw colored light. Dispersion
  (RGB IOR split) on the shatter shards = the rainbow-glass money shot.
- **Particles:** glass shards (instanced), glass dust/powder (fine, volumetric-lit), a few bright sparks on
  each hit, prismatic light motes on the shatter.
- **Camera:** slow push-in through Hits 1–2, then a **snap-and-orbit** on the shatter with racked focus onto
  the watch; **DOF + motion blur + speed ramp**; micro-shake keyed to each impact.
- **Compositor:** bloom/glare, chromatic aberration + lens distortion pulse on each hit (biggest on Hit 3),
  slight grain, vignette, and a prismatic dispersion glow on the flying shards.
- **Timing psychology:** escalate the interval and intensity — Hit 1 small, Hit 2 bigger and sooner-feeling,
  a **held beat of silence** right before Hit 3, then the shatter is the loudest single frame.

**Sound cues:** delicate "tink" on Hit 1 → heavier "crack + low thud" on Hit 2 → **held silence** → a
**huge glass-shatter + bass drop + shimmer** on Hit 3 → airy reverb tail over the reveal.

**Deliverables:** master clip + a 3s short-form cut (Hit 2 → shatter → reveal) + **alpha/transparent
renders** of the shattering glass and the watch beam for compositing over any footage. Provide the aura
color as a swappable parameter so one file serves every pack tier.

---

### Note for whoever runs this
Both are built to **composite over real pack-opening or creator-reaction footage** (alpha deliverables), so
they slot straight into the clipping/AI-editor pipeline. Keep the **fake-out silence before the hit** and the
**slow-mo savor after** — those two beats are what make it replayable; cutting them for time kills the dopamine.
