# Research brief: Top 20 podcast targets for Avery Andon (as of 2026-10-06)

## Approved facts about Avery Andon (use ONLY these; never invent credentials)
- Miami-based art dealer, entrepreneur and philanthropist. Instagram @averyandon, 153K followers.
- Developed street artist Alec Monopoly into a global brand: sold-out exhibitions from New York to Morocco, major brand partnerships.
- Launched ArtLife.com in 2015 as one of the first online-only blue-chip art galleries and scaled it into an eight-figure-a-year business. Coined "Click & Mortar" (social-first marketing + curated physical pop-ups), since widely copied.
- Early champion of Hebru Brantley and Jammie Holmes.
- Advises celebrities, athletes and high-net-worth individuals on buying and investing in art (fame, money and outlandish requests).
- Press: Us Weekly (Kris Jenner spent over $100K on a Hap Tivey artwork at Art Basel Miami Beach 2024, placed by Avery; Kris Jenner publicly thanked him on Instagram, Dec 2024); Hypebeast ("Celebrity Art Dealer Avery Andon Launches ArtLife Auctions", 2020); LA Times (Alec Monopoly profile, 2018); Page Six (Scott Disick buys $57K Helmut Newton print, 2021); Forbes (Lionel Smit show at ArtLife Gallery LA, 2018); Vanity Fair (Michael Cohen's prison badge sold as an NFT via ArtGrails, 2021); Rolling Stone (Ozuna drops art for launch of NFT site ArtGrails); also The Wall Street Journal.
- Hosts the podcast "ArtLife with Avery Andon". Guests include Incubus frontman Brandon Boyd; Brian Clarke (artist, executor of the Zaha Hadid and Francis Bacon estates); David Packouz (inspiration for the film War Dogs); actor Said Taghmaoui; art dealer/journalist Kenny Schachter; retired Army Ranger Erick Innis; exotic-car collector PJ (Exotic Car Hacks).
- Philanthropy: Co-Chair for UCLA Mattel Children's Hospital and Goldie Hawn's MindUP; co-founded City Seats with the New York Yankees (Boys & Girls Clubs of America); supports WildAid, the Amazon Conservation Team, the Miami Police Department's Do the Right Thing program and Amigos for Kids.
- Talent page: https://www.thebaddest.com/talent/avery-andon . Agent: David Harris, VP / Talent Coordinator, The Baddest Agency, David@thebaddest.com, (305) 791-9990.

## Task per show
Using web search (page fetches of most sites are blocked; search results are the main source):
1. Confirm the show is active: find its most recent episodes (aim for the last ~90 days, as of Oct 2026). List 4-6 recent episodes with date (or approx), guest, and the topic in one line, plus a source URL each.
2. Pick the ONE best recent episode for a personalized opener ("Your conversation with X about Y...") and say why.
3. Propose 3 specific, show-tailored angles for Avery. Each: a headline, a one-sentence pitch, and which recent episode/theme it builds on. Angles must rest on the approved facts above.
4. Confirm current host(s) and the booking route (guest form URL, booking email, producer name) WITH the source. Never guess or construct an email address. If no route is verifiable, say so and give the best documented route (e.g., contact form, producer on LinkedIn, network PR).
5. Note format details that matter for a pitch (in-person vs remote, studio city, video, episode length, typical guest profile) and any red flags (pay-to-play, inactive, no outside guests, host change).

Write results as JSON to /home/user/art-discovery-agent/podcast-campaign/data/top20/<slug>.json, one file per show, with keys:
name, slug, tier, hosts, active (bool), last_episode_date, recent_episodes [{date, title, guest, topic, url}], opener_episode {title, guest, date, why}, angles [{headline, pitch, builds_on}], booking {route, contact, source, confidence: high|medium|low}, format, red_flags, sources [urls], notes.
Mark anything you could not verify as "unverified". Accuracy beats completeness.
