# Banksy Junior Partner Search — Research Notes

**Research dates:** 17 September 2026 (single session)
**Analyst:** Automated research agent, Claude Code
**All claims last verified:** 17 September 2026

---

## 1. Research limitations — read before anything else

These are not minor caveats. They materially affect how much weight the outputs can carry.

### 1.1 Direct page retrieval was blocked entirely

The session's network egress policy blocked **every** attempt to fetch a source page directly. Tested and confirmed blocked:

| Domain | Method | Result |
|---|---|---|
| `www.myartbroker.com` | WebFetch | `EGRESS_BLOCKED` |
| `hanguppictures.com` | WebFetch | `EGRESS_BLOCKED` |
| `en.wikipedia.org` | WebFetch | `EGRESS_BLOCKED` |
| `www.theartnewspaper.com` | WebFetch | `EGRESS_BLOCKED` |
| `news.artnet.com` | WebFetch | `EGRESS_BLOCKED` |
| `www.tateward.com` | curl | HTTP 000 (blocked) |
| `andipagallery.com` | curl | HTTP 000 (blocked) |
| `api.apify.com` | curl | HTTP 403, `connect_rejected` (organisation policy) |

**Consequence:** Quality-control step 1 of the brief — *"Open every important source link and confirm it supports the stated claim"* — **could not be performed.** Not one source page was opened and read in full. Every claim rests on search-result titles, URLs and indexed snippets.

**Mitigations applied:**
- **Domain-scoped searching** as a substitute for fetching. Restricting a search to a single domain surfaces that site's individual page URLs and titles — enough to confirm, for instance, that `hanguppictures.com/team/madeleine-white-2` exists and is titled "Madeleine White | Senior Sales and Acquisitions". This confirms role and employment but not page body content.
- **Multi-source corroboration required** before any claim was scored.
- **Confidence caps.** No claim is rated High on a single search-derived source. "High" was used only where three or more independent reputable sources agreed, or where the source type is itself dispositive (a formal corporate appointment press release).
- **Every URL is recorded** in `banksy_candidate_evidence.csv` so a human can perform the verification pass that I could not.

### 1.2 Search-summary hallucination risk — one confirmed instance

Search results arrive with a model-generated summary, which can misstate what the underlying pages say. **One concrete error was caught and corrected:**

> A summary described **Shane Xu** as "Head of the Modern & Contemporary Prints & Multiples department at Roseberys." A follow-up domain-scoped query surfaced `roseberys.co.uk/staff/ed-plackett`, titled **"Ed Plackett - Head of Department | Prints & Multiples"**. Resolved in favour of the employer's own staff page; Shane Xu's title is recorded as **unconfirmed**.

Others may have survived undetected. This is the strongest single argument for the human verification pass.

### 1.3 Geographic search bias

The search tool is documented as US-region. Given that the Banksy dealer population is concentrated in the UK, **UK and European candidates are likely under-represented relative to their true share of the market.** Several UK-specific avenues could not be pursued: Companies House filings, UK trade-press archives (Antiques Trade Gazette), and paywalled coverage in the FT and The Art Newspaper.

### 1.4 Structural evidence asymmetries

- **Self-published dominance.** Most biographical detail about dealers comes from their own firms' websites. Galleries market; they do not file. Independent corroboration exists for only a minority of candidates.
- **Private sales are private.** The Banksy private-treaty market is deliberately confidential. Absence of published transactions is *expected* and is not evidence of weak performance — but it means "proven sales skill" cannot be established from public sources for most candidates and must come from references.
- **Auction professionals are over-evidenced relative to dealers**, because auction houses publish results, press releases and staff pages. This may bias the shortlist toward auction candidates on evidence availability rather than actual suitability.
- **Sales figures are almost all employer-level.** Phillips' £4.4m Editions result and Maddox's £7.6m Banksy figure are departmental/firm totals and are flagged as such throughout.

### 1.5 What was not attempted

No paywall, login, robots control, CAPTCHA or platform access limit was bypassed. LinkedIn was used only as it appears in public search results — no profile was logged into or scraped. No individual was contacted. No private contact details, addresses, family information or protected characteristics were collected.

---

## 2. Apify workflow

**Step 1 — Credential check.** Performed first, as instructed. Checked `APIFY_TOKEN` and equivalents in the environment, `~/.apify/auth.json`, the `apify` CLI binary, and local `.env` files. **No Apify credential of any kind exists in this environment.** (Environment variables were listed with values redacted; no token was ever displayed.)

**Step 2 — Store access check.** Attempted the public Apify Store API (`api.apify.com/v2/store?search=google+search+scraper&limit=3`). The egress proxy returned **HTTP 403 `connect_rejected`** — an organisation policy denial. Per the proxy's own guidance, policy denials are reported, not retried or routed around.

**Step 3 — Conclusion.** **Apify was unavailable for both credentialed and anonymous use.** No actor was searched, evaluated or run. **Actual Apify spend: $0.00**, against the $25 ceiling. No approval for additional spend is needed or requested.

**What the Apify workflow would have covered, had it been available** — recorded so the gap is legible and the work is repeatable:

| Purpose | Actor category to evaluate | What it would have added |
|---|---|---|
| Search-engine results at depth | Google/SERP scrapers | Systematic pagination beyond first-page results; the single biggest coverage gap here |
| Public LinkedIn profile/company discovery | LinkedIn public profile scrapers | Structured career history, tenure dates, employer transitions — directly addressing the "career trajectory" and "career stage" fields that are currently thin |
| Public Instagram professional accounts | Instagram profile/post scrapers | Dealer activity signals, exhibition participation, public client engagement |
| Website crawling | Generic site crawlers | Full team pages, exhibition archives and "about" histories for every gallery — which would have substantially resolved the self-published-vs-verified problem |
| News and article discovery | News aggregator actors | Systematic press archive coverage rather than incidental search hits |

Per the brief's instruction 3, actor ID, maintainer, update date, rating and estimated cost would have been recorded before use, with a small test run inspected before scaling. None of this was reachable.

---

## 3. Exact search queries executed

74 queries, all via web search, all on 17 September 2026. Queries marked **[domain]** were scoped to a single site.

**Ecosystem discovery (1–12)**
1. `Banksy specialist auction house head of urban art department`
2. `"Banksy" art advisor private sales dealer specialist London`
3. `MyArtBroker Banksy specialist team founder`
4. `Steve Lazarides Lazinc Banksy former dealer gallery`
5. `Andipa Gallery Banksy Acoris Andipa dealer`
6. `Hang-Up Gallery London founder director Banksy team`
7. `Sotheby's Phillips Christie's contemporary art specialist Banksy sale led by`
8. `"Art of Banksy" exhibition curator organiser Banksy collection touring`
9. `Tate Ward Auctions urban contemporary art founder director specialist`
10. `former auction house specialist founded own art advisory contemporary street art`
11. `Woodbury House gallery Banksy founder director`
12. `Grove Gallery London Banksy director founder urban art`

**Team-page mining (13–15, 19) [domain-scoped]**
13. `our people team specialist Banksy` **[myartbroker.com]**
14. `team director specialist about us` **[hanguppictures.com]**
15. `meet the team specialist urban art` **[tateward.com]**
19. `staff Harry Brian Parkinson Elise Ballard Danny Herbert head of department` **[tateward.com]**

**Institutional expansion (16–18, 20–29)**
16. `Bonhams urban art specialist Gareth Williams Banksy sale`
17. `Maddox Gallery director partner Banksy sales team`
18. `Lougher Contemporary Bristol Banksy dealer founder`
20. `Madeleine White senior sales acquisitions Charlotte Bain art consultant Hang-Up Gallery`
21. `Andipa Gallery team director sales specialist Banksy Alex Andipa`
22. `Guy Hepner gallery New York Banksy director founder`
23. `Taglialatella Galleries director Banksy street art New York Paris`
24. `Julien's Auctions street art Banksy specialist head of department`
25. `Artcurial urban art Arnaud Oliveux Banksy specialist Paris auction`
26. `Phillips editions specialist Banksy prints head of department London`
27. `Chiswick Auctions urban art department head specialist Banksy`
28. `Enter Gallery Brighton artrepublic Banksy founder director`
29. `Heritage Auctions urban art director Banksy consignment specialist`

**Broadening and adjacency (30–35, 42–50)**
30. `CULTURED Young Dealers List 2025 gallerists named emerging`
31. `Banksy Pest Control authentication provenance expert specialist advisor named`
32. `Banksy dealer Dubai Hong Kong Asia gallery urban art director sells Banksy`
33. `Florence Whittaker Maddox Gallery head of secondary market background career`
34. `MyArtBroker specialists team Charlotte Stewart Erin Argun Banksy KAWS specialist`
35. `street art gallery founder sold Banksy original interview entrepreneur built business`
42. `Miami street art gallery director contemporary secondary market dealer KAWS Banksy`
43. `New York street art dealer advisor private sales KAWS Invader Banksy founded gallery`
44. `"Banksy" specialist left joined appointed new role gallery 2024 2025 art market moves`
45. `GraffitiStreet Rosh Boroumand co-founder Banksy specialist Chichester gallery`
46. `Forum Auctions Roseberys prints multiples head of department Banksy urban art specialist London`
47. `Silverback Gallery street art Banksy founder director`
48. `Bonhams current urban contemporary art specialist London Banksy sale 2024 2025`
49. `Stik Invader Shepard Fairey gallery dealer director sold works private sales specialist`
50. `Banksy market commentator analyst quoted "head of" OR "director of" print market report`

**ArtLife company research (36–41)**
36. `about us company Banksy sell art` **[artlife.com]**
37. `ArtLife artlife.com Banksy art gallery company who are they`
38. `team founder leadership contact` **[artlife.com]**
39. `Avery Andon ArtLife Gallery founder art advisor Miami career background`
40. `ArtLife Gallery Miami exhibitions artists represented online gallery`
41. `sell consignment Banksy verified supply secondary market inventory` **[artlife.com]**

**Candidate depth and reputational diligence (51–74)**
51. `Jasper Tordoff MyArtBroker Banksy specialist background career`
52. `Grove Gallery London investment art complaints Jacob Barnes criticism`
53. `Maddox Gallery criticism investment claims FCA complaints art investment scrutiny`
54. `Danny Herbert Tate Ward urban art Chiswick Auctions built department interview`
55. `Huw Lougher Lougher Contemporary interview art market ten years founder growth`
56. `Taylor Curry Heritage Auctions director modern contemporary urban art career background`
57. `Joseph Bannan Woodbury House gallery director street art interview career`
58. `Rebecca Tooby-Desmond Phillips editions specialist head of sale background`
59. `Acoris Andipa interview Banksy market gallery director curator museum exhibitions`
60. `US based street art dealer advisor Banksy Los Angeles Miami sold private collectors gallery founder`
61. `Ben Cotton Hang-Up Gallery interview founder Banksy market built gallery`
62. `Shane Xu Roseberys head of prints multiples urban contemporary career`
63. `Roseberys Ed Plackett Shane Xu head of department prints multiples who is current`
64. `Madeleine White Hang-Up Gallery senior sales acquisitions Roseberys Chiswick career Banksy`
65. `Steven Sulley Woodbury House founder career street art Richard Hambleton dealer`
66. `art advisor United States contemporary street art private sales founded firm ex-Phillips ex-Sotheby's KAWS Banksy collectors`
67. `Banksy print market dealer Instagram public specialist advisor rising young`
68. `"Banksy" gallery director "joined" OR "appointed" specialist urban art 2023 2024 London new hire`
69. `Tim Luke Julien's Auctions street art contemporary career background specialist`
70. `Alec Monopoly gallery dealer represented sold works director US collectors`
71. `Rosh Boroumand GraffitiStreet Banksy sourcing six figure prints collectors institutions`
72. `Bonhams Los Angeles urban art sale specialist United States street art department head`
73. `Joe Syer MyArtBroker co-founder career background Banksy specialist years experience`
74. `Robin Barton Bankrobber Banksy dealer controversy removed street works sold`

### Query families from the brief that returned no usable new candidates

Several suggested query families were run in substance and produced no names beyond those already captured: `"Banksy" sold by`, `"Banksy" sourced`, `"Banksy" provenance advisor`, `emerging contemporary art dealer private sales`, `independent contemporary art advisor collectors`. The reason is structural — Banksy private sales are confidential, so transaction-led searching returns market commentary rather than named intermediaries. Searching **backwards from institutions to individuals** proved far more productive and became the primary method.

---

## 4. Sources searched

**Primary / authoritative:** artlife.com · myartbroker.com · hanguppictures.com · andipagallery.com / andipa.com / andipaeditions.com · tateward.com · graffitistreet.com · loughercontemporary.com · woodburyhouseart.com · grovegallery.com · maddoxgallery.com · entergallery.com · dellasposa.com · guyhepner.com · taglialatellagalleries.com · silverbackgallery.com · mocomuseum.com · museumbanksy.com · bonhams.com · phillips.com · sothebys.com · roseberys.co.uk · fineart.ha.com (Heritage) · juliensauctions.com · artcurial.com · stevensulley.co.uk

**Reputable press and art-market publications:** The Art Newspaper · Artnet News · ARTnews · Artforum · Artsy Editorial · NBC News · NPR · PBS · CNN · Forbes · The Local (France) · Hackney Gazette · Sussex Express · Brighton Journal · Scene Magazine · FAD Magazine · Art Plugged · The London Magazine · Made in Shoreditch · Hypebeast · Broadway World · Monaco Life · East Hampton Star · Miami New Times · Grazia · Cultured Magazine

**Art-market platforms:** Artsy · Artnet · MutualArt · Invaluable · the-saleroom · 1stDibs · Ocula

**Public professional profiles:** LinkedIn public pages (as surfaced in search results only) · The Org · Forbes Business Council

**Explicitly treated as discovery leads only, never as evidence:** RocketReach · ZoomInfo · Wiza · HolaConnect · Trustpilot · Traders Union · Grokipedia · Pinterest · Quora · promotional listicles. Contact-aggregator sites (RocketReach, ZoomInfo and similar) appeared in results but **no contact data from them was recorded** — they surface personal emails and phone numbers, which the brief excludes.

**Could not be searched:** Apify Store · Companies House · Artprice · ArtRabbit · Art Basel / Frieze / TEFAF exhibitor archives · paywalled FT, NYT, WSJ, Bloomberg content. Companies House in particular is a real loss — it would have established directorships, shareholdings and company health for every UK candidate.

---

## 5. Inclusion and exclusion decisions

### Inclusion criteria applied
A person was added to the longlist if they met **all** of: (a) named in at least one identifiable public source; (b) holding a commercial, curatorial or leadership role at an organisation with demonstrable Banksy, street-art or blue-chip secondary-market activity; (c) evidence of a *professional* function, not merely a collector or enthusiast.

### Exclusions and reasoning

| Excluded | Category | Reasoning |
|---|---|---|
| **Pearl Lam** | Risk | [Litigation alleging a Banksy painting was paid for but never delivered](https://www.artnews.com/art-news/news/hong-kong-heiress-sues-art-dealer-banksy-painting-1234662087/), reported by ARTnews and The Art Newspaper. Unresolved. Excluded on risk, not merit. |
| **John Marquez** | Not a professional | Miami collector, real-estate developer and ICA Miami trustee who founded a non-profit gallery. Early KAWS collector with genuine relevance — but a collector, not a dealer. **Better as a Miami collector relationship for ArtLife than as a candidate.** |
| **Wissam Al Mana** | Wrong profile | Lazinc co-founder, but a Qatari business magnate and investor rather than an operating art professional. |
| **Emma Fernberger, Adora Mba, Margot Samel, Alex Fleming, Anya Komar** (Cultured Young Dealers List) | No Banksy/street nexus | Correct career stage and genuinely entrepreneurial, but primary-market galleries representing living emerging artists — a different business from Banksy secondary-market dealing. |
| **Rebecca Wei, Patti Wong, Amy Cappellazzo** | Too senior; wrong market | Former auction-house chairs who founded advisories. Far beyond "junior partner" and focused on Impressionist/Modern/Asian markets, not street art. |
| **Albert Scaglione** (Park West) | Wrong model | Park West's cruise-ship auction model is reputationally distinct from ArtLife's positioning; also a long-established principal. |
| **Silverback Gallery principals** | Unidentifiable | Gallery sells Banksy but no named founder or director could be established from public sources. Dead end. |
| **Chiswick Auctions current urban art staff** | Unidentifiable | Repeated searching returned department pages but no current named specialists. The department's historic significance is captured via Danny Herbert's founding of it. |
| **Kirsteen Davidson** | Stale, thin | Retained on the longlist at rank 27 but not shortlisted: the only evidence is a single 2019 reference to Sotheby's "Banksy/Online" sale. Current role and employer entirely unverified. |
| **Erin-Atlanta Argun, Sheena Carrington, Paul Wells** | Function mismatch | Editorial, market-research and marketing roles at Banksy-active firms. Retained on the longlist for completeness but cannot meet the brief's sales-ability requirement. |
| **Elise Ballard** | Career stage | Graduated 2021; genuinely early career, well below junior-partner level. Retained on the longlist as pipeline. |
| **Hazis Vardar, Corey Ross, Alexander Nachkebiya** | Wrong discipline | Exhibition and venue operators, not dealers. Touring Banksy exhibitions are also explicitly unauthorised by the artist. |
| **Robin Barton** | **Risk — see below** | Retained on the longlist at rank 22 with an explicit do-not-approach flag. |

### The Robin Barton decision, stated explicitly

Robin Barton has among the deepest documented Banksy transaction records of anyone identified — a 2007 street-piece sale at around £250,000, *Slave Labour* at roughly £1m, *Art Buff*. On raw Banksy transaction evidence he would rank highly. **He was excluded from recommendation because his business model is structurally incompatible with ArtLife's positioning.** Bankrobber specialises in removing, restoring and selling Banksy street works. Pest Control has stated it will not authenticate works removed from their original site and has warned dealers of the implications of selling unauthenticated works; [Banksy publicly called one such exhibition "disgusting"](https://www.nbcnews.com/news/world/street-artist-banksy-calls-exhibition-london-disgusting-n89196). ArtLife's entire Banksy proposition is anchored on Pest Control verification. Hiring from the opposite side of that line would compromise the proposition ArtLife is trying to strengthen.

### The Maddox Gallery decision

Four Maddox individuals are on the longlist; one (Florence Whittaker) is shortlisted, all flagged. Maddox is defending [a US civil complaint alleging knowingly false valuations and involvement in a "pump and dump" scheme](https://www.artnews.com/art-news/market/maddox-gallery-lac-art-lender-lawsuit-1234786102/); the gallery calls the claim "bizarre and irrational." **These allegations are unproven and are not directed at any individual named in this research.** They are recorded because valuation integrity is the exact competence ArtLife would be hiring for, making the employer context directly relevant to professional risk. This is a diligence flag, not a disqualification, and the distinction is maintained throughout.

---

## 6. Duplicate and conflicting identities resolved

| Issue | Resolution |
|---|---|
| **Shane Xu vs Ed Plackett, Roseberys** | A search summary called Shane Xu "Head of the Modern & Contemporary Prints & Multiples department." Roseberys' own staff page titles **Ed Plackett** "Head of Department \| Prints & Multiples." **Resolved in favour of the employer's staff page.** Shane Xu's title recorded as unconfirmed; both individuals listed separately (ranks 11 and 36). |
| **Danny Herbert / Daniel Herbert** | Same person. Tate Ward's staff page uses "Danny Herbert"; his public professional profile uses "Daniel Herbert - Co-Owner, Tate Ward Ltd." Merged into one record; both forms noted. |
| **Grove Gallery / Grove Collective / Square Gallery** | Jacob Barnes is associated with Grove Gallery, and separately with "Grove Collective"; Morgane Wagner is separately linked to Square Gallery. **Not resolved** — flagged as an open entity question requiring clarification before any approach. |
| **Madeleine White** | Search results conflated her with Madeleine Ponsonby, Countess of Bessborough (an unrelated historical figure) and with an unrelated "Erica White." Disambiguated via the employer team page URL and matching employment history on her public professional profile. |
| **Tim Luke** | Named as Julien's Executive Director (2017) *and* as head of Hindman's Independent Appraisals division in a later source. **Current role unresolved** — flagged as verify-first. Also disambiguated from an unrelated academic of the same name. |
| **Charlotte Stewart vs Charlotte Bain** | Two different people at two different firms (MyArtBroker MD; Hang-Up art consultant). Kept separate. |
| **Rebecca Tooby-Desmond** | Third-party aggregators give three different titles (Head of Sale; Associate Director; Researcher). Employer team page used as the authority; title flagged for confirmation. |
| **Gareth Williams** | Described both as "Urban Art Specialist" and as "Head of Contemporary Art and Modern Design" — consistent with a 1995 joiner promoted over time, not two people. Single record; both titles noted. |
| **ArtLife vs Andon Gallery** | `andongallery.com` surfaced alongside Avery Andon searches. Treated as a **separate, unconfirmed entity**; not conflated with ArtLife. |
| **Two "Art of Banksy" exhibitions** | At least two distinct unauthorised touring shows exist — one associated with Steve Lazarides and producer Corey Ross, another curated by Alexander Nachkebiya via Exhibition Hub. Recorded as separate ventures. |

---

## 7. Candidates who initially looked promising but were set aside

| Name | Initial promise | Why set aside |
|---|---|---|
| **Joe Syer** | Highest score in the entire research (88/100); the definitive Banksy market specialist | Co-owner of ArtLife's most direct competitor. Availability effectively zero. Retained at rank 1 as a benchmark and competitive-intelligence entry, priority Monitor. |
| **Gareth Williams** | Genuine Banksy record-setter; pioneered the urban art auction format; took it to Los Angeles | Joined Bonhams in **1995** — approximately three decades in, far outside "rising." Excellent potential **referee**, and the best single source on how Banksy auction records were historically built. |
| **Steve Lazarides** | Unmatched Banksy access as the artist's former agent and dealer | [Publicly quit the commercial gallery world in 2019](https://www.theartnewspaper.com/2019/09/09/banksys-former-agent-quits-gallery-world-citing-snobbery-and-the-death-of-subculture) citing art-world snobbery — a stated exit from exactly the work ArtLife needs. Also sold his Banksy archive at Julien's. Relationship or referee, not a hire. |
| **Acoris Andipa** | Arguably the deepest continuous Banksy dealing record identified | Principal of a family gallery trading since 1967. Prohibitively established; unavailable. |
| **Ben Cotton** | Outstanding founder narrative closely paralleling ArtLife's own | Owner-operator of a direct competitor. **His team, however, proved the most productive hunting ground identified** — Madeleine White came from this thread. |
| **Lawrence Alkin** | Founded the gallery claiming to be the first to sell Banksy prints (6,000+) | Established founder, and [reports indicate Enter Gallery is closing](https://www.scenemag.co.uk/enter-gallery-brightons-oldest-independent-art-gallery-to-close-its-doors/) — which could mean availability or commercial difficulty. **Worth monitoring precisely because of the dislocation.** |
| **Jay Rutland** | A promotional article stated he "works closely with Pest Control" | **The Pest Control claim appears only in promotional coverage and is not independently established.** Per the brief it was excluded from scoring and must not be repeated. Creative/brand role rather than specialist dealing. |
| **Guy Hepner** | US gallery and advisory with genuine Banksy and graffiti-art depth; publishes Pest Control education | Founded 2000 — an established owner, directly competitive with ArtLife in the same US segment. Very little independent third-party coverage found. |
| **Brian Swarts / Paolo Galli-Zugaro / Nadège Buffe** (Taglialatella) | US and Paris based, Pop and Street Art specialists who have exhibited Banksy | Evidence never rose above gallery staff-listing level. The 2015 Banksy show is the only concrete Banksy activity found; it appears episodic. Retained on the longlist, not shortlisted. |
| **Kim and Lionel Logchies** (Moco) | Built a three-city private museum around Banksy from a commercial gallery base | Museum principals, not transacting dealers, and not available. **Genuinely valuable as an institutional loan and exhibition relationship** for ArtLife. |
| **Cultured "Young Dealers" cohort** | Exactly the right career stage and entrepreneurial energy | Primary-market galleries representing living emerging artists — a fundamentally different business from Banksy secondary-market dealing. |

---

## 8. Stale information register

Claims resting on sources that are materially dated. **Each must be re-verified before use.**

| Candidate | Stale element | Age / status |
|---|---|---|
| **Tim Luke** | Julien's appointment | July 2017; a later source indicates a move to Hindman. **Current role genuinely unknown.** |
| **Arnaud Oliveux** | Banksy sale responsibility | October 2018 (post-shredding sale). Current role unverified. |
| **Kirsteen Davidson** | Sotheby's Banksy/Online sale | 2019. Role and employer unverified. |
| **Gareth Williams** | Urban Art sale results | Bonhams press releases undated on the record collected; some appear to date to 2008–2011. |
| **Danny Herbert** | "£13m across 8 auctions last year" | **Undated page — "last year" is relative to an unknown publication date.** Could be several years old. |
| **Lawrence Alkin** | Enter Gallery operating status | Reported closing; status unconfirmed. |
| **Steve Lazarides** | Gallery-world exit | 2019; current activity beyond Laz Emporium unverified. |
| **All staff listings** | Employment currency | Team pages can lag departures by months. **Every candidate's current employment should be confirmed before contact.** |

---

## 9. Quality-control checklist against the brief

| # | Requirement | Status |
|---|---|---|
| 1 | Open every important source link and confirm it supports the claim | ❌ **NOT DONE — technically impossible.** All fetching blocked. This is the primary handover task. |
| 2 | Two credible sources for every top-five candidate, one primary/authoritative | ✅ Met. Tordoff (employer page + LinkedIn + Sky News); Herbert (staff page + LinkedIn + Artsy); Curry (**formal press release** + consignment listing + LinkedIn); Boroumand (own site + two independent Sussex Express pieces); Lougher (**two independent Artnet features** + own site). |
| 3 | Check similar names have not been merged | ✅ Done — nine conflicts resolved in §6; one (Grove entities) left open and flagged. |
| 4 | Separate employer from individual accomplishments | ✅ Done — Phillips £4.4m, Maddox £7.6m, Julien's Banksy archive sale and Heritage/Tate Ward department figures all explicitly flagged as employer-level. |
| 5 | Mark stale information and record verification date | ✅ Done — §8 register; all records dated 17 Sep 2026. |
| 6 | Remove unsupported statements and promotional language | ✅ Done — marketing claims ("largest private dealer," "worldwide Banksy specialists," "six-figure sums") retained but explicitly labelled as promotional and unverified. |
| 7 | Identify significant uncertainty openly | ✅ Done — §1 limitation notice, per-candidate "Gaps requiring verification," and the shortlist's opening warning. |
| 8 | Confirm no recommendation rests on a protected characteristic | ✅ Confirmed. No age was estimated or inferred anywhere. Career stage is derived only from founding dates, promotion trails, graduation-to-role intervals and stated years of experience. No gender, race, nationality, religion, disability or family status informed any score. *(Where family relationships appear incidentally in public business records — co-founders who are spouses or brothers — they are noted only as facts about business ownership structure affecting availability, and carry no scoring weight.)* |
| 9 | Ranking based on professional evidence and ArtLife fit | ✅ Done. Note the deliberate design choice: rank follows total score, while **outreach priority carries the availability judgement.** Several top-ranked individuals are marked Monitor because they own competing businesses. |
| 10 | End with five candidates for immediate diligence and the single strongest reason for each | ✅ Done — final section of `banksy_partner_shortlist.md`. |

---

## 10. Recommended next steps for a human researcher

1. **Perform the verification pass I could not.** Open every URL in `banksy_candidate_evidence.csv`, starting with the immediate-priority five. Downgrade or remove anything unsupported.
2. **Pull Companies House records** for all UK candidates — directorships, shareholdings, filing history and accounts. This would resolve the ownership and availability questions that are currently the least evidenced dimension.
3. **Confirm current employment** for every candidate before contact; staff pages lag reality.
4. **Resolve the three open identity questions**: Shane Xu's title, Tim Luke's current employer, and the Grove Gallery/Grove Collective entity structure.
5. **Check the Maddox v. Luxury Asset Capital docket** for current status before any Maddox approach.
6. **Re-run this research with Apify or unrestricted fetching enabled.** LinkedIn career-history data alone would substantially strengthen the career-trajectory and career-stage assessments, which are currently the thinnest fields in the dataset.
7. **Treat references as the primary evidence source for sales ability.** Public sources cannot establish it in a confidential private-sale market; only people who have seen the numbers can.
