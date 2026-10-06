# Avery Andon: Podcast Guest Campaign

**Goal:** Make Avery Andon a recurring podcast guest across business, culture, luxury and art shows, and build the booking record that leads to **The Joe Rogan Experience**.
**Agency:** The Baddest Agency (David Harris, VP / Talent Coordinator)

**Formal strategy (shareable doc):** [Avery Andon: Podcast Ladder Strategy](https://claude.ai/code/artifact/61c2d8b4-8e56-485b-adb3-0f8b00a4c47f). It covers the climb from entry-level shows to Tier 2, then the gateway shows, then Joe Rogan, with South Florida shows first.

## What's in this folder

| File | What it is |
|---|---|
| `podcast-targets.html` | The tiered target list, readable in a browser: host notes, genre, topics, stances, booking contact, links and proposed angles for every show |
| `podcast-targets.csv` | The same list as a spreadsheet for tracking outreach. Add Status, Date Pitched, Follow-up and Result columns as you work it |
| `feeder-map.html` | Feeder map: where recent guests of Modern Wisdom, Theo Von and Shawn Ryan appeared before they were booked, and the recommended route to each show |
| `data/tier1.json`, `tier2.json`, `tier3.json` | Raw research data behind the list |
| `data/tier2-feeders/*.json` | Which entry-level shows feed each Tier 2 show (47 guests traced, with gaps listed in each file) |
| `data/south_florida.json` | 24 South Florida podcasts and 12 local studios |
| `data/feeders/*.json`, `build_feeders.py` | Feeder research (87 guests traced) and the script that builds the feeder map |
| `pitch-email.md` | Pitch email from David Harris (with confidentiality notice), subject lines, angle blocks and a follow-up |
| `avery-andon-guest-page.html` | Guest profile page for thebaddest.com: bio, talking points, episodes, clip slots, press, socials and booking |
| `build_targets.py` | Rebuilds the CSV and HTML from the JSON. Run `python3 build_targets.py` |

### Research status (October 2026)
The list covers **47 shows**: 17 in Tier 1, 16 in Tier 2 and 14 in Tier 3.

**How it was researched:** Apify and direct page fetches (Spotify, Apple, RSS feeds, show websites) were blocked in the research environment. Everything was compiled from web search results. No email address was guessed, and every booking route records where it came from.

**Before pitching any show:**
- **Booking routes:** confirm each one. Each entry's `booking_contact.type` says how reliable it is (official site / RSS / press report / unverified). Routes marked unverified need someone to open the source link.
- **Audience figures:** many are marked "unverified". Fill them in from Rephonic, Podscan or the show's own media kit.
- **Weak entries:** these are long shots or need more research.
  - **Pivot:** rarely books outside guests.
  - **The David Rubenstein Show / Bloomberg Wealth:** Bloomberg Wealth may have ended in 2025.
  - **The Art Angle:** hosts, topics and booking route are unverified.
- **Paid shows:** Miami's Podcast and Florida Business Forum may charge guests to appear. Ask before committing.
- **Inactive shows:** some Tier 1 shows had no confirmed 2026 episode at research time. Check the latest episode date first.
- **Coverage gap:** the list is light on politics. Candidates for a second pass include Young and Profiting and Honestly with Bari Weiss.

---

## The campaign: a 5-phase ladder

Rogan, Theo Von and Diary of a CEO almost never book from cold pitches. They book people they've already *seen*: guests who are good on other shows, who come up in clips, or who a past guest vouches for. The campaign works up the tiers so each appearance becomes proof for the next pitch.

### Phase 0: Foundation (weeks 1–2)
- **Publish the guest page** on thebaddest.com. Add a professional headshot, links to the six major press articles, and a one-sheet PDF.
- **Media training session:** tighten 5 signature stories to 90 seconds each:
  1. How Alec Monopoly went from street tags to global brand deals
  2. Launching an online blue-chip gallery in 2014 when everyone said it couldn't work
  3. The craziest celebrity art deal
  4. The NFT boom: what he saw from the inside
  5. One contrarian take on the art market, money or business
- **Cut a sizzle reel:** 60–90 seconds of Avery's best moments from *ArtLife with Avery Andon* and the Clean Break interview.
- **Clean up socials:** pin podcast clips on Instagram (@averyandon, @artlifepodcast) and keep LinkedIn current.

### Phase 1: Tier 1, small and niche shows (weeks 2–8)
- **Target:** 8–12 bookings. These shows say yes, give practice reps and generate clips.
- **Cadence:** 5–8 personalized pitches a week, with one follow-up 5–7 business days later.
- Rotate angles on purpose so the clip library covers every pillar: art, entrepreneurship, luxury/HNW, tech and celebrity partnerships.
- **After every episode:** ask the host for the raw video, cut 3–5 vertical clips, post them within 72 hours and tag the show.
- **Use Avery's own show as leverage:** invite Tier 1 and Tier 2 hosts onto *ArtLife with Avery Andon*. Reciprocal bookings are the fastest yes in podcasting.

### Phase 2: Tier 2, mid-size shows (months 2–5)
- **Target:** 4–6 bookings.
- Every pitch leads with **proof**: "Recently on [Show A] and [Show B]," with a link to the strongest clip.
- **Tie pitches to the news:** auction records, art-world scandals, luxury market shifts, AI-generated art, Miami Art Week / Art Basel (December). Basel season is the single best moment to pitch art and luxury angles.
- Pitch non-art angles hardest here (entrepreneur, HNW, brand building). That proves Avery can carry a general-interest conversation.

### Phase 3: Breakout positioning (months 4–8)
- **Create one shareable, distinct idea:** a contrarian thesis Avery can own, such as "Most art sold to celebrities is a bad investment" or "The art world is the last unregulated market."
- **Get one clip to break 1M views.** That clip is the actual pitch to Tier 3.
- **Get introduced:** map past guests of Tier 3 shows who are in Avery's network (artists, athletes, celebrity clients, comedians). A warm intro from a past guest is the main way onto Rogan, Theo Von and Flagrant.
- Pitch Tier 2 hosts with big audiences to have Avery back. Repeat guests signal a strong guest.

### The route to Modern Wisdom, Theo Von and Shawn Ryan (from the feeder map)
We traced 87 recent guests of the three shows (excluding celebrities) back to the podcasts they appeared on beforehand.
- **Jordan Harbinger and PBD Podcast come first.** Each feeds two of the three targets, fits Avery well and has a published guest route. PBD also records in Fort Lauderdale.
- **The Diary of a CEO comes next.** It fed 3 Modern Wisdom guests and 1 Shawn Ryan guest.
- **Single-target feeders:** School of Greatness and The Skinny Confidential lead to Modern Wisdom. Full Send leads to Theo Von. Theo's comedy feeders (Kill Tony, Bad Friends/Whiskey Ginger) are a poor fit for Avery.
- **How each show books:**
  - **Modern Wisdom** books around book-launch interview runs and through Chris Williamson's podcaster friends.
  - **Theo Von** books colorful outsiders, often found through viral clips.
  - **Shawn Ryan** books from its own guests' circles and from news hooks. Lead with the Miami Police work, art crime and conservation.
- **Joe Rogan shows up in all three feeder tallies.** Getting on two of the three targets puts Avery in the guest pool Rogan books from.

### Phase 4: Tier 3, the big shows (months 6–12+)
- Use each show's booking route from the target list. Most Tier 3 shows book through producers and referrals, not inbox pitches.
- **Joe Rogan path:** JRE has no public booking inbox. The realistic route is:
  1. Become a known name to Rogan's circle by appearing on the shows his comedian and fighter friends run (Theo Von, Flagrant, Shawn Ryan and similar shows on the target list).
  2. Get a warm referral from a past JRE guest.
  3. Have a clip that circulates in the same online spaces as JRE (MMA, comedy, hunting/outdoors, entrepreneurship).
- **Rogan-specific angle:** Avery's outdoors and conservation work (WildAid, Amazon Conservation Team), the strangeness of the art market, street art versus the establishment, and the money and characters behind celebrity art. Lead with curiosity and stories, not credentials.

---

## Tracking and KPIs

| Metric | Phase 1 | Phase 2 | Phase 3–4 |
|---|---|---|---|
| Pitches sent / week | 5–8 | 4–6 | 2–3 (personalized, often warm intros) |
| Reply rate target | 20%+ | 10–15% | Relationship-driven |
| Bookings | 8–12 | 4–6 | 1–3 |
| Clips published per episode | 3–5 | 5+ | 5+ |

**Pipeline status** (add as a column in the CSV): `Not contacted → Pitched → Followed up → In conversation → Booked → Recorded → Aired → Clipped`. Add `Do not contact` for any show that declines, and leave it unpitched for at least 6 months.

## Ground rules
- Personalize every pitch with a specific recent episode. Never send a generic blast.
- Use each show's published booking route. If a show asks for a form, use the form.
- Re-verify every contact before sending. Producers change often.
- Keep claims accurate. Every credential in the pitch must match the bio and press list.
