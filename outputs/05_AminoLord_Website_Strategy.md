# AminoLord.com — Website Strategy, Experience Architecture, and Technology Plan

**Status:** Proposed concept. Prepared 2026-09-02. All copy in this document is DRAFT and must pass legal, medical, and compliance review before publication.
**Principals:** Scott Disick (proposed brand partner/cofounder) and Dr. Michael Azziz (proposed medical cofounder) are referenced only as *proposed* roles subject to definitive agreements. No endorsement, ownership, or authorization is implied. See `08_AminoLord_Evidence_Ledger.xlsx` (Principal Verification tab) for the current verification status.
**Labeling convention used throughout:** [VF] Verified fact · [CR] Company-reported claim · [TE] Third-party estimate · [AI] Analyst inference · [SR] Strategic recommendation · [FA] Financial assumption.

---

## 1. Experience principles

AminoLord.com should feel premium, confident, modern, medically credible, educational, discreet, human, transparent, easy to navigate, and mobile-first. [SR]

| Principle | What it means in practice | Anti-pattern we explicitly avoid |
|---|---|---|
| Premium, not loud | Editorial typography, generous whitespace, restrained palette, one accent color | Neon "biohacker" gradients, vial-and-syringe hero imagery, steroid-vendor aesthetics |
| Medically credible | Named, licensed clinicians; visible standards; evidence graded honestly | Anonymous "our doctors"; stock lab-coat photography; unsupported outcome claims |
| Educational first | Every program page links to a peptide-library entry with evidence grade and FDA status | Product pages with no science, or science-sounding copy with no citations |
| Discreet | Neutral packaging language, private account area, no social-share prompts on health pages | Public "transformation" galleries; before/after imagery |
| Transparent | All-in pricing shown before intake; cancellation shown before enrollment | Hidden consult fees; forced subscriptions; buried cancellation |
| Separation of Rx and retail | Prescription programs use "Check eligibility"/"Start consultation"; only non-Rx items use "Add to bag" | A single cart mixing Rx and retail as if equivalent |
| Human | Real people, real support hours, real names | Chatbot-only support; fake scarcity timers |

## 2. Brand and design-system direction

### 2.1 Visual identity [SR]
- **Name treatment:** "AminoLord" set in a high-contrast serif (e.g., Fraunces, Canela-style alternatives with open licenses such as *Instrument Serif* or *Fraunces*) for the wordmark; UI in a humanist sans (e.g., *Inter* or *Geist*). Pairing signals "editorial health" rather than "supplement store".
- **Palette:** Ink (#14171C) primary text; Bone (#F6F3EE) ground; Deep Moss (#1F3D33) as the single brand accent; Brass (#B08D57) for restrained highlights; Signal Red (#B3261E) only for warnings/adverse-event guidance; success/clinical Green (#2E7D5B). All pairings must pass WCAG 2.2 AA contrast (4.5:1 body text).
- **Photography:** Natural light, real clinicians and real members (with releases), lifestyle contexts (kitchen, gym, morning routine), never syringes-as-hero, never celebrity imagery unless contractually authorized. No before/after imagery.
- **Iconography:** 1.5px line icons, monochrome, used for standards/trust components only (licensed pharmacy, clinician-reviewed, tested, secure).
- **Motion:** Subtle; respects `prefers-reduced-motion`.

### 2.2 Component inventory [SR]
Global header (logo, primary nav, "Check eligibility" CTA, account), announcement bar (state availability), hero (headline + evidence line + dual CTA), standards strip (4 trust chips), program card, peptide-library card, evidence-grade badge (A/B/C/Insufficient), FDA-status badge (Approved / Compounded / Restricted / Supplement / Not offered), clinician card (name, license state(s), NPI-verifiable, credentials), pricing table (all-in), eligibility stepper, consent modal, FAQ accordion, safety/adverse-event banner, state-availability selector, testimonial card (with "individual results vary" and FTC-compliant disclosure), footer (legal, accessibility statement, contact, Rx disclaimer), member dashboard widgets (next refill, labs, messages, program status), cookie/consent manager (consumer-health-data aware).

### 2.3 Trust and compliance components (required on every relevant page) [SR]
- "How we decide what to offer" link (standards page) in footer and program pages.
- FDA-status badge on every peptide/program.
- "Prescription products require a consultation with an independent licensed clinician; not everyone qualifies" disclosure near any Rx CTA.
- Adverse-event/emergency banner on all program, safety, and dashboard pages ("If you are experiencing a medical emergency, call 911").
- Auto-renewal disclosure block adjacent to any subscription CTA (price, cadence, how to cancel), with affirmative checkbox.
- Consumer-health-data notice link on every page that collects health inputs (quiz, intake).

### 2.4 Accessibility requirements [SR]
WCAG 2.2 AA target; semantic landmarks; keyboard-operable quiz and checkout; focus states; 4.5:1 contrast; captions and transcripts for all video; form errors announced; no auto-playing media with sound; accessibility statement page; automated (axe) plus manual screen-reader test before launch and quarterly thereafter.

## 3. Sitemap

```
/                                  Homepage
/how-it-works                      How It Works (Rx path + non-Rx path)
/programs                          Health Goals / Programs hub
  /programs/recovery               Recovery & tissue support
  /programs/metabolic              Metabolic health & weight management (GLP-1 class, clinician-led)
  /programs/vitality               Energy, sleep & healthy aging
  /programs/performance            Performance & body composition
  /programs/sexual-health          Sexual health (PT-141/bremelanotide where lawful)
  /programs/skin                   Skin & topical peptides (non-Rx cosmetics)
/peptides                          Peptide & Ingredient Library (education; FDA status + evidence grade)
  /peptides/{slug}                 Ingredient detail page
/science                           Science & Standards (sourcing, testing, evidence grading, what we won't sell)
/medical-team                      Medical Team (clinician profiles; licensure by state)
/about                             About AminoLord (mission, principals if authorized, advisory board)
/pricing                           Pricing (all-in program, membership, consult, labs; cancellation)
/eligibility                       Eligibility Quiz (gated, consented; routes to intake or education)
/labs                              Lab & Monitoring Information
/safety                            Safety (contraindications, side effects, adverse-event reporting)
/evidence                          Results & Evidence (what the literature supports, honestly graded)
/learn                             Journal / Learn (articles, clinician Q&A, video)
  /learn/{slug}
/shop                              Non-prescription commerce (supplements/cosmetics only; standard cart)
  /shop/{slug}
/membership                        Membership (education + navigation + clinician access + member pricing)
/faq                               FAQs
/support                           Customer Support (hours, channels, SLAs)
/contact                           Contact
/state-availability                State Availability (Rx programs by state; non-Rx nationwide)
/account                           Member Dashboard (auth required)
  /account/program                 Program status, clinician messages, refills
  /account/subscriptions           Subscription Management (pause, change, cancel in ≤2 clicks)
  /account/labs                    Lab orders & results (via integrated portal)
  /account/orders                  Order history & tracking
  /account/privacy                 Data requests, consent history, delete account
/legal/privacy                     Privacy Policy
/legal/consumer-health-data        Consumer Health Data Privacy Policy (WA MHMDA / NV / CT compliant)
/legal/terms                       Terms of Service
/legal/telehealth-consent          Telehealth Informed Consent (per state)
/legal/shipping-returns            Shipping & Returns (Rx non-returnable; retail policy)
/legal/accessibility               Accessibility Statement
/legal/notice-of-privacy-practices HIPAA NPP (published by the affiliated medical practice)
/legal/disclosures                 Endorsement & material-connection disclosures (principals, influencers)
```
Rules: Rx programs never expose "Add to Cart". `/shop` is physically and visually separated (different header label "Shop" vs "Programs"; different checkout). Legal pages are published by the correct legal entity (brand/MSO vs. medical practice vs. pharmacy) — counsel to confirm. [SR]

## 4. Page specifications

For each major page: goal · audience · primary message · outline · CTAs · trust signals · required disclosures · media · SEO intent · analytics events · mobile notes. Headlines are DRAFT copy. [SR]

### 4.1 Homepage `/`
- **Goal:** Establish credibility in 5 seconds; route visitors to education, eligibility, or shop.
- **Audience:** Health-curious 30–55 year-olds, skewing male 60/40 [AI], who have heard about peptides from podcasts/social and want a trustworthy way in.
- **Primary message (draft):** "Peptide health, done properly." Sub: "Clinician-led programs, tested products, and plain-language science. No hype, no shortcuts."
- **Outline:** (1) Hero with dual CTA; (2) Standards strip (Licensed US pharmacies · Independent clinician review · Third-party tested · Transparent pricing); (3) "Choose your goal" program cards (6); (4) "How it works" 3-step (Learn → Check eligibility → Clinician plan); (5) Peptide library teaser with FDA-status badges; (6) Medical team preview (named clinicians); (7) "What we won't do" transparency block (no research-use-only products, no unapproved claims, no forced subscriptions); (8) Member stories (compliant testimonials or none at launch); (9) Learn articles; (10) FAQ short; (11) Footer with disclosures.
- **Primary CTA:** "Check eligibility" (Rx path). **Secondary:** "Explore the library" (education). Tertiary: "Shop non-prescription".
- **Trust signals:** Clinician names and license states; pharmacy licensure statement; LegitScript certification (once obtained); security badges; press logos only if earned.
- **Required disclosures:** Rx consultation disclaimer; "not all applicants qualify"; individual results vary; endorsement disclosure if principals shown.
- **Media:** 12–15s ambient hero video (muted, captions), clinician portraits, product-in-context stills.
- **SEO intent:** Brand + "peptide therapy", "peptide clinic online", "clinician-led peptides". 
- **Analytics events:** `hero_cta_click{cta}`, `program_card_click{program}`, `library_teaser_click`, `scroll_depth{25/50/75/100}`, `faq_expand{q}`.
- **Mobile:** Sticky bottom CTA bar; program cards as horizontal snap-scroll; standards strip as 2×2 grid.

### 4.2 How It Works `/how-it-works`
- **Goal:** Explain the two paths (Rx via consultation; non-Rx via shop) and set expectations for time, cost, and clinician independence.
- **Outline:** Path selector → Rx path timeline (Quiz 3 min → Intake 10 min → Clinician review ≤48h (async) or video → Plan & pricing → Pharmacy ships 3–7 days → Check-ins & refills) → Non-Rx path → "Who qualifies / who doesn't" → Pricing summary → FAQ.
- **CTAs:** Primary "Check eligibility"; secondary "See pricing".
- **Disclosures:** Clinician independence statement; state availability; async vs. synchronous visit rules by state; no guarantee of prescription.
- **Events:** `path_select{rx|otc}`, `timeline_step_view{step}`.
- **Mobile:** Vertical timeline; collapse FAQ.

### 4.3 Programs hub `/programs` and program page `/programs/{goal}`
- **Goal:** Convert interest into eligibility starts with honest expectation-setting.
- **Outline (program page):** Hero (goal, who it's for, who it's not for) → "What's included" (consult, clinician plan, medication if prescribed, monitoring, support) → Candidate ingredients with FDA-status and evidence-grade badges (never a dosing protocol) → All-in pricing table → Safety & side effects → Labs required → Clinician quote (named) → FAQ → CTA.
- **CTAs:** Primary "Check eligibility"; secondary "Read the science".
- **Trust:** Evidence grade with citations; pharmacy disclosure; state availability chip.
- **Disclosures:** Compounded drugs are not FDA-approved for safety/efficacy; Rx only if clinically appropriate; adverse-event contact; results vary.
- **Media:** Clinician explainer video (60–90s, captioned); ingredient illustrations (no syringes).
- **SEO:** "{goal} peptide therapy", "{ingredient} prescription online" (informational + commercial).
- **Events:** `program_view{program}`, `evidence_badge_click`, `pricing_table_view`, `eligibility_start{program}`.
- **Mobile:** Pricing table as stacked cards; sticky CTA.

### 4.4 Peptide library `/peptides` and detail `/peptides/{slug}`
- **Goal:** Become the most trusted plain-language reference (SEO moat; trust builder). 
- **Detail outline:** Summary card (what it is; FDA status; evidence grade; offered by AminoLord? yes/no/why not) → Mechanism in plain language → What studies show (human vs animal; sample sizes) → Risks & contraindications → Regulatory status with citations (FDA bulks list category, approvals) → "Our position" (offered via clinician / not offered / non-Rx form) → Related programs → References → Medical reviewer + review date.
- **CTAs:** Contextual: "Check eligibility" only for ingredients we offer via clinicians; otherwise "Explore programs".
- **Disclosures:** Educational, not medical advice; reviewer credentials; last-reviewed date.
- **SEO:** Informational head terms ("BPC-157", "sermorelin", "NAD+ injections", "tesamorelin") — highest-volume intent in the category [AI]; structured data (MedicalWebPage, Drug where appropriate).
- **Events:** `library_view{slug}`, `reference_click`, `library_to_program`.
- **Mobile:** Sticky summary card; jump-links.

### 4.5 Science & Standards `/science`
- **Goal:** Make the sourcing and evidence policy a differentiator.
- **Outline:** Evidence grading rubric → Sourcing (503A/503B pharmacies, licensure, testing, COAs on request for non-Rx) → What we will not sell (research-use-only products; unapproved ingredients for injection; unproven "stacks") → Clinical governance (medical director role, protocol review cadence, adverse-event process) → Quality partners (named once contracted) → Change log.
- **CTA:** "Meet the medical team".
- **Disclosures:** Compounded vs approved; pharmacy names/licensure.
- **Events:** `standards_section_view`, `coa_request_click`.

### 4.6 Medical Team `/medical-team`
- **Goal:** Verifiable medical authority.
- **Outline:** Medical director profile (proposed: Dr. Michael Azziz, only if credentials verified and agreement signed) → Clinician cards (name, credential, license states, NPI, bio, photo) → Independence statement (clinicians are employed/contracted by the affiliated medical practice; compensation is not tied to prescriptions) → Advisory board.
- **Disclosures:** Entity relationship (MSO vs. practice); state licensure.
- **Events:** `clinician_profile_view{id}`.

### 4.7 Pricing `/pricing`
- **Goal:** Zero-surprise pricing; reduce support load; pre-qualify.
- **Outline:** Toggle (Programs / Membership / Non-Rx) → All-in program price cards (consult + medication + monitoring; what's excluded, e.g., labs) → Membership card → Labs pricing → Payment methods (HSA/FSA where eligible; financing if compliant) → Cancellation and refund policy summary → FAQ.
- **CTAs:** "Check eligibility"; "Join membership".
- **Disclosures:** Auto-renewal terms; medication price may vary by dose/pharmacy; no insurance billing (if true).
- **Events:** `pricing_toggle{tab}`, `plan_select{plan}`, `cancellation_policy_view`.

### 4.8 Eligibility Quiz `/eligibility`
- **Goal:** Route safely: education / non-Rx / clinical intake; capture consented lead.
- **Flow:** Intro (what we ask, why, privacy) → Consent to process consumer health data (explicit, logged) → Goal → State → Age (21+ for Rx programs; 18+ shop) → Red-flag screen (pregnancy/nursing, active cancer, eating disorder history, MEN2/thyroid cancer history for GLP-1, etc.) → Current medications → Email/phone capture (SMS opt-in separate, TCPA-compliant) → Outcome page (eligible to proceed to intake / not a fit with education / non-Rx suggestions).
- **CTAs:** "Continue to intake" or "Explore learning".
- **Disclosures:** Not a diagnosis; clinician decides; state availability; CHD notice.
- **Events:** `quiz_start`, `quiz_step{n}`, `quiz_disqualify{reason_category}`, `quiz_complete{outcome}`, `lead_captured`.
- **Mobile:** One question per screen; progress bar; autosave.

### 4.9 Labs & Monitoring `/labs`
- **Goal:** Explain which programs require labs, how ordering works (partner lab / at-home kit), turnaround, cost, and what results trigger.
- **Disclosures:** Labs ordered by clinician; results reviewed by clinician; no self-interpretation.
- **Events:** `lab_info_view`, `lab_pricing_view`.

### 4.10 Safety `/safety`
- **Goal:** Demonstrate seriousness; meet duty-of-care expectations.
- **Outline:** How to report a side effect (24/7 contact; FDA MedWatch link) → Contraindications by program → Storage/handling → Emergency guidance → Drug interactions → Counterfeit/RUO warning.
- **Events:** `ae_report_click`, `medwatch_click`.

### 4.11 Results & Evidence `/evidence`
- **Goal:** Honest evidence summaries (no outcome guarantees). Includes "what the evidence does not show".
- **Disclosures:** Individual results vary; compounded products not FDA-evaluated.

### 4.12 Learn `/learn`
- **Goal:** Organic acquisition + retention content; founder-led and clinician-led video.
- **Content pillars:** Peptide 101; Regulation explained; Program deep-dives; Member routines; Myths vs evidence.
- **Events:** `article_view`, `video_play`, `newsletter_signup`.

### 4.13 Shop `/shop`
- **Goal:** Non-Rx commerce (supplements/cosmetics that meet standards) with conventional cart.
- **Disclosures:** DSHEA disclaimer for supplements; cosmetics claims limited to appearance; no drug claims.
- **Events:** standard e-commerce events (`view_item`, `add_to_cart`, `begin_checkout`, `purchase`).

### 4.14 Membership `/membership`
- **Goal:** Recurring revenue not tied to prescription volume: education library, clinician Q&A, lab coordination, member pricing on non-Rx, priority support.
- **Disclosures:** Auto-renewal; what membership does not include (medication).

### 4.15 Account / Member Dashboard `/account`
- **Goal:** Retention and safety: program status, next steps, messages with care team, refills, labs, subscriptions, privacy controls.
- **Cancellation:** "Cancel" visible on subscription page; ≤2 clicks; confirmation email; no retention dark patterns beyond one optional "pause" offer.
- **Events:** `dashboard_view`, `refill_request`, `message_sent`, `subscription_pause`, `subscription_cancel{reason}`.

### 4.16 Legal pages
Privacy; Consumer Health Data policy; Terms; Telehealth consent (state-specific); Shipping & returns; Accessibility; NPP; Disclosures (material connections of principals and paid creators). Each carries version and effective date; consent capture logged with version ID.

## 5. User flows

Notation: box = screen; ◆ = decision; ⟶ = transition. Entities: **Brand/MSO** (AminoLord), **Practice** (affiliated professional entity), **Pharmacy** (licensed 503A/503B), **Lab**.

### 5.1 New visitor → education
Home ⟶ Library teaser ⟶ Ingredient detail ⟶ (newsletter capture) ⟶ Related program ⟶ Eligibility.

### 5.2 New visitor → eligibility screening
Home/Program ⟶ Eligibility intro ⟶ CHD consent ◆ decline → education path ⟶ Q&A steps ⟶ ◆ red flag → "Not a fit" (education, non-Rx suggestions, clinician note) ⟶ ◆ state not served → waitlist ⟶ Outcome: "You can proceed to a clinician review".

### 5.3 Eligibility → clinical intake
Create account (email + password/passkey; MFA optional) ⟶ Identity verification (ID + selfie via vendor) ⟶ Telehealth consent (state-specific) + NPP acknowledgment ⟶ Medical intake (history, meds, allergies, vitals, photos if needed) ⟶ ◆ labs required? → Lab order created (partner lab or at-home kit) ⟶ Payment authorization for consult fee (charged only when clinician review begins) ⟶ Submitted to Practice queue.

### 5.4 Clinical approval → payment and fulfillment
Clinician reviews (async or video by state rule) ⟶ ◆ Prescribe / decline / request info ⟶ If prescribed: plan summary + all-in price ⟶ Member accepts (auto-renewal disclosure, checkbox) ⟶ Payment captured ⟶ e-Rx to Pharmacy ⟶ Pharmacy verification & compounding ⟶ Cold-chain ship (if required) with tracking ⟶ Onboarding sequence (how to use, storage, side effects, who to call) ⟶ Check-in at day 7/30.

### 5.5 Non-prescription product purchase
Shop ⟶ PDP ⟶ Cart (retail only) ⟶ Checkout (Shopify) ⟶ Confirmation ⟶ Fulfillment (3PL).

### 5.6 Membership enrollment
Membership page ⟶ Plan select ⟶ Account ⟶ Auto-renewal consent ⟶ Payment ⟶ Dashboard onboarding.

### 5.7 Lab coordination
Clinician orders ⟶ member chooses site/kit ⟶ results to Practice EHR ⟶ clinician reviews ⟶ member notified in dashboard (results never emailed) ⟶ ◆ abnormal → clinician outreach.

### 5.8 Refill request
Dashboard "Request refill" ⟶ short check-in (side effects, adherence, weight if relevant) ⟶ ◆ clinician approves/adjusts/holds ⟶ pharmacy ⟶ ship.

### 5.9 Subscription management and 5.10 cancellation
Dashboard ⟶ Subscriptions ⟶ Pause/Change/Cancel ⟶ Reason (optional) ⟶ Confirm ⟶ Email confirmation; clinician notified for Rx programs (safety follow-up on discontinuation where relevant).

### 5.11 Adverse-event / urgent-support escalation
Any page banner or dashboard "Report a side effect" ⟶ Triage form (severity) ⟶ ◆ Severe → immediate 911 guidance + clinician on-call page ⟶ Non-severe → clinician response within 24h ⟶ AE logged (pharmacovigilance record; pharmacy notified; MedWatch where appropriate).

### 5.12 Customer support
Support page/chat (business hours) ⟶ ◆ clinical question → routed to Practice care team (HIPAA channel) / non-clinical → brand support ⟶ SLA: first response <4 business hours; AE questions <1 hour.

## 6. Wireframes (desktop and mobile)

ASCII wireframes are intentionally low-fidelity. [SR]

### 6.1 Homepage
```
DESKTOP                                                   MOBILE
┌───────────────────────────────────────────────────────┐  ┌──────────────────┐
│ AminoLord   Programs Library Science Team Pricing  [Check eligibility] (Acct) │  │ ☰ AminoLord  (Acct)│
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│ Serving CA, TX, FL, NY, … | non-Rx ships nationwide    │  │ Serving 12 states│
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│  Peptide health, done properly.        [ambient video]│  │ Peptide health,  │
│  Clinician-led programs, tested products,             │  │ done properly.   │
│  plain-language science.                              │  │ [video]          │
│  [Check eligibility]  [Explore the library]           │  │ [Check eligib.]  │
│  Rx products require a clinician consultation.        │  │ [Explore library]│
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│ ✓ Licensed US pharmacies ✓ Independent clinicians     │  │ ✓ Pharmacies     │
│ ✓ Third-party tested     ✓ Transparent pricing        │  │ ✓ Clinicians     │
├───────────────────────────────────────────────────────┤  │ ✓ Tested ✓ Price │
│ Choose your goal                                       │  ├──────────────────┤
│ [Recovery] [Metabolic] [Vitality] [Performance] [Sex.] │  │ Choose your goal │
│ [Skin]                                                │  │ ◀ [Card][Card] ▶ │
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│ How it works: 1 Learn → 2 Check eligibility → 3 Plan  │  │ 1 Learn          │
├───────────────────────────────────────────────────────┤  │ 2 Check eligib.  │
│ Library: BPC-157 [Restricted] Sermorelin [Compounded] │  │ 3 Clinician plan │
│ Tesamorelin [FDA-approved] NAD+ [Compounded]  → all   │  ├──────────────────┤
├───────────────────────────────────────────────────────┤  │ Library chips    │
│ Medical team: Dr. X, MD (CA, TX) · Dr. Y, DO (FL) ... │  ├──────────────────┤
├───────────────────────────────────────────────────────┤  │ Medical team     │
│ What we won't do: RUO products · unproven claims ·    │  ├──────────────────┤
│ forced subscriptions · hidden fees                    │  │ What we won't do │
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│ Learn: 3 latest articles                              │  │ Learn            │
├───────────────────────────────────────────────────────┤  ├──────────────────┤
│ Footer: Legal · CHD Privacy · Accessibility · Disclos.│  │ Footer           │
└───────────────────────────────────────────────────────┘  │ [Sticky: Check   │
                                                            │  eligibility]    │
                                                            └──────────────────┘
```

### 6.2 Program / health-goal page
```
┌────────────────────────────────────────────────────────┐
│ Breadcrumb: Programs › Recovery                         │
│ H1 Recovery & tissue support        [Evidence: B]       │
│ Who it's for / who it's not for (two columns)           │
│ [Check eligibility]  [Read the science]                 │
├────────────────────────────────────────────────────────┤
│ What's included: consult · clinician plan · Rx if      │
│ appropriate · monitoring · support · pharmacy shipping  │
├────────────────────────────────────────────────────────┤
│ Candidate ingredients                                   │
│ ┌ Tesamorelin  [FDA-approved drug] [Evidence B] ┐       │
│ ┌ Sermorelin   [Compounded]        [Evidence C] ┐       │
│ ┌ BPC-157      [FDA-restricted — not offered]    ┐       │
├────────────────────────────────────────────────────────┤
│ All-in pricing table  (monthly · what's excluded)       │
├────────────────────────────────────────────────────────┤
│ Safety & side effects · Labs required · Clinician quote │
│ FAQ · Adverse-event banner · [Check eligibility]        │
└────────────────────────────────────────────────────────┘
Mobile: same order; pricing as stacked cards; sticky CTA.
```

### 6.3 Ingredient detail page
```
┌──────────────────────────────┬─────────────────────────┐
│ H1 Sermorelin                │ Summary card (sticky)   │
│ Plain-language summary       │ FDA status: Compounded  │
│ Mechanism                    │ Evidence grade: C       │
│ What studies show (human/    │ Offered by AminoLord:   │
│  animal, n, duration)        │  Yes — via clinician    │
│ Risks & contraindications    │ [Check eligibility]     │
│ Regulatory status (cited)    │ Reviewed by Dr. X, MD   │
│ Our position                 │ Last reviewed 2026-09   │
│ References (numbered)        │                         │
└──────────────────────────────┴─────────────────────────┘
Mobile: summary card first, then sections with jump links.
```

### 6.4 Pricing page
```
[Programs] [Membership] [Non-Rx]
┌ Recovery ─────────┐ ┌ Metabolic ────────┐ ┌ Vitality ─────────┐
│ $X/mo all-in      │ │ $Y/mo all-in      │ │ $Z/mo all-in      │
│ ✓ consult ✓ Rx    │ │ ✓ consult ✓ Rx    │ │ ✓ consult ✓ Rx    │
│ ✓ monitoring      │ │ ✓ monitoring      │ │ ✓ monitoring      │
│ ✗ labs ($)        │ │ ✗ labs ($)        │ │ ✗ labs ($)        │
│ [Check eligib.]   │ │ [Check eligib.]   │ │ [Check eligib.]   │
└───────────────────┘ └───────────────────┘ └───────────────────┘
Auto-renewal terms · Cancel anytime in account (2 clicks) · Refund policy · HSA/FSA
```

### 6.5 Eligibility flow
```
[1/8] What's your main goal?     ○ Recovery ○ Metabolic ○ Vitality ○ Performance
      ─────────────────────────── progress bar ───────────────────────────
      Privacy: we ask health questions to route you safely. [CHD notice]
[2/8] State  [3/8] Age  [4/8] Red flags  [5/8] Conditions  [6/8] Medications
[7/8] Contact (email; SMS opt-in separate)  [8/8] Outcome
Outcome A: "You can proceed to a clinician review" [Continue to intake]
Outcome B: "This program isn't a fit right now" — reasons (category), education links, non-Rx options
```

### 6.6 Clinician profile
```
┌ Photo ┐ Dr. Jane Example, MD · Internal Medicine
│       │ Licensed: CA, TX, FL (NPI 1234567890 — verify)
└───────┘ Bio · Training · Approach · "How I decide" · Independence statement
```

### 6.7 Checkout / enrollment (Rx program)
```
Step 1 Plan summary (from clinician)  Step 2 Pricing & auto-renewal consent ☐  Step 3 Payment
Order summary: Program $X/mo · Next charge date · Cancel anytime in account
[Confirm & pay]   Secure · PCI · No insurance billed
```

### 6.8 Member dashboard
```
┌ Program status: Active — Recovery ┐ ┌ Next refill: Oct 3 · [Request now] ┐
┌ Messages (care team) 1 new       ┐ ┌ Labs: results ready · [View]        ┐
┌ Subscriptions: Manage / Pause / Cancel ┐ ┌ Report a side effect (24/7)   ┐
┌ Learn: recommended for you        ┐ ┌ Privacy & data: download / delete   ┐
```

## 7. Draft homepage copy (DRAFT — requires legal and medical review)

- **Headline:** Peptide health, done properly.
- **Subhead:** Independent clinicians decide what's right for you. Licensed US pharmacies fill it. We explain the science in plain language and tell you what we won't sell.
- **CTA 1:** Check eligibility · **CTA 2:** Explore the library
- **Standards strip:** Licensed pharmacies · Independent clinician review · Third-party tested · Transparent, all-in pricing
- **"What we won't do" block:** We do not sell research-use-only peptides. We do not promise results. We do not hide fees or trap you in subscriptions. If a peptide is not appropriate to prescribe, we'll tell you why.
- **Fine print:** Prescription products are available only after a consultation with an independent licensed clinician and only where clinically appropriate. Compounded medications are not FDA-approved. Not available in all states. If you are experiencing a medical emergency, call 911.

## 8. Technology recommendation

### 8.1 Options compared [SR]

| Criterion | A. Shopify-based commerce + external compliant clinical workflow | B. Headless commerce + integrated telehealth/identity/accounts | C. Custom member portal over proven clinical infrastructure (recommended) |
|---|---|---|---|
| Description | Shopify (Plus) runs marketing site and non-Rx shop; Rx path handed off to a white-label telehealth vendor's hosted flow | Next.js storefront; commerce via Shopify Hydrogen/Commerce Layer; telehealth vendor API; own auth | Next.js marketing/education/portal; Shopify for non-Rx commerce only; telehealth/EHR/e-Rx via specialist vendor APIs; Stripe for Rx program billing |
| Time to market | 8–12 weeks | 16–24 weeks | 12–18 weeks |
| Build cost (est.) [FA] | $60–120k | $250–500k | $150–300k |
| Flexibility | Low (vendor UX controls Rx journey; brand break at handoff) | High | High where it matters (portal, education, intake UI) |
| HIPAA / CHD | PHI lives with vendor; Shopify not HIPAA-eligible for PHI, so no health inputs in Shopify | Own infra must be HIPAA-eligible (BAA with cloud, vendors) | PHI in vendor EHR + HIPAA-eligible cloud (BAA); brand site collects only consented, minimal CHD |
| EHR / telehealth | Vendor-hosted | API | API (vendor of record for clinical workflow, e-Rx, ID verification) |
| Pharmacy integration | Via vendor | Direct + vendor | Via vendor e-Rx network + pharmacy API for status |
| Subscriptions | Shopify subscriptions (non-Rx only) | Custom | Shopify (non-Rx); Stripe Billing (Rx programs, membership) |
| Identity | Shopify customer accounts | Own (Auth0/Clerk) | Own (Clerk/Auth0) with passkeys, MFA |
| Analytics | GA4/Shopify (no health data) | Own pipeline | Server-side event pipeline (Segment/RudderStack) with CHD filtering; no PHI to ad platforms |
| Consent logging | Vendor | Own | Own (versioned consents, immutable log) |
| Security | Vendor + Shopify | Own | Own + SOC 2 vendors; pen test pre-launch |
| Accessibility | Theme-dependent | Own | Own (design system) |
| SEO | Good for shop; weak for library depth | Excellent | Excellent (SSR/ISR content) |
| Maintenance | Low | High | Medium |
| Risk | Brand/UX break; limited data; harder to differentiate | Highest cost/complexity; regulatory surface fully owned | Balanced; vendor dependence for clinical core (acceptable; auditable) |

### 8.2 Recommended stack (Option C) [SR]
- **Web:** Next.js (App Router) on Vercel or AWS; Sanity or Contentful CMS with medical-review workflow fields (reviewer, date, version).
- **Non-Rx commerce:** Shopify (Basic/Advanced initially; Plus at scale) via Storefront API; Shopify Payments (confirm supplement acceptability) with backup high-risk-tolerant processor.
- **Rx program & membership billing:** Stripe Billing (verify "telehealth" acceptable use; do not bill medications directly to consumer unless permitted by the model chosen by counsel — the practice/pharmacy may need to be merchant of record).
- **Clinical core (license/integrate, do not build):** Telehealth workflow + EHR + e-prescribing + provider network from a vendor with multi-state coverage (candidates to diligence: OpenLoop, Wheel, SteadyMD, Healthie + DoseSpot/Surescripts; final selection subject to due diligence and counsel).
- **Identity verification:** Persona/Veriff/Stripe Identity.
- **Labs:** Vendor with Quest/Labcorp integration and at-home kits (e.g., Vital, Junction/Spike-type providers; diligence required).
- **Pharmacy:** 503A/503B partners with API status webhooks; cold-chain via pharmacy's carrier program.
- **Comms:** Klaviyo (marketing email; no PHI), Twilio (transactional SMS with TCPA consent), HIPAA-eligible messaging within the portal (e.g., vendor-provided or Spruce/Paubox-type).
- **Analytics & tags:** Server-side GTM; GA4 with health-data filtering; ad-platform conversions limited to non-health events (page_view, quiz_start without answers) per Meta/Google health restrictions; product analytics in a HIPAA-eligible warehouse (BigQuery/Snowflake with BAA).
- **Consent & privacy:** OneTrust/Osano-type CMP configured for WA MHMDA, NV, CT, CA; DSAR workflow.
- **Support:** Zendesk (non-clinical) + clinical inbox in EHR; Aircall/Dialpad phone.
- **Security:** SSO, least privilege, secrets manager, WAF, encrypted PHI at rest/in transit, audit logs, annual pen test, incident-response plan, cyber insurance.

### 8.3 Build / license / integrate matrix
| Component | Build | License | Integrate |
|---|---|---|---|
| Marketing site, library, program pages, quiz UI, member dashboard | ✓ | | |
| CMS with medical-review workflow | | ✓ | ✓ |
| Non-Rx commerce and cart | | ✓ (Shopify) | ✓ |
| Telehealth/EHR/e-Rx/provider network | | ✓ | ✓ |
| Identity verification | | ✓ | ✓ |
| Labs | | ✓ | ✓ |
| Pharmacy | | (partner contracts) | ✓ |
| Billing (Stripe) | | ✓ | ✓ |
| Consent logging service | ✓ | | |
| Analytics pipeline with CHD filtering | ✓ | ✓ | ✓ |
| Support tooling | | ✓ | ✓ |

## 9. SEO and content architecture [SR]
- Library entries target informational head terms; program pages target commercial terms; state pages (`/state-availability/{state}`) target "peptide therapy {state}" only where Rx is actually available.
- E-E-A-T: every medical page shows reviewer name, credentials, date; author bios; citations to primary literature and FDA sources.
- Structured data: Organization, MedicalOrganization (practice), Physician, FAQPage, Article, Product (non-Rx only).
- Avoid: doorway pages, dosing "protocol" content, RUO comparison content, and any content implying prescription is guaranteed.

## 10. Analytics event schema (summary)
Core funnel: `session_start → hero_cta_click → program_view → eligibility_start → quiz_complete{outcome} → account_created → intake_submitted → consult_scheduled → consult_completed → plan_offered → plan_accepted → payment_success → rx_sent → shipped → onboarding_complete → refill_requested → churned{reason}`. All events exclude answer values; health-related properties are stored only in the HIPAA-eligible warehouse, never sent to third-party ad pixels.

## 11. Pre-launch website QA checklist
Legal page versions live; consent logging verified; Rx CTAs never link to cart; state gating tested; accessibility audit passed; Core Web Vitals green on mobile (LCP < 2.5s, INP < 200ms, CLS < 0.1); pen test complete; ad pixels audited for health data leakage; cancellation flow ≤2 clicks; AE reporting path tested end-to-end with the practice; support SLAs staffed.
