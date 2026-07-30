# Instagram Page Engagement Ranking

Ranking of the 15 available pages by expected engagement strength (views,
comments, and overall interactions).

**Important caveat on data:** live per-post metrics for these accounts could
not be pulled from this environment (Instagram and third-party analytics
sites are blocked by the network policy, and Instagram blocks anonymous
scraping generally). This ranking is therefore an *estimate* built from
follower size combined with well-established niche engagement benchmarks —
how viral each content category typically is on Reels/Explore and how
comment/share-heavy its audience behaves. To turn this into an exact,
data-backed ranking, export per-post metrics and run
`scripts/rank_engagement.py` (see README section below).

## Estimated ranking (strongest first)

| # | Handle | Followers | Niche | Why it ranks here |
|---|--------|-----------|-------|-------------------|
| 1 | @idiotsdriving | 170k | car | Car-fail/dashcam clips are among the most viral Reels formats — view counts routinely run several times follower count, with heavy tag-a-friend commenting. Large following × top-tier viral niche. |
| 2 | @r.a.p | 178k | rap/music | Largest audience on the list, and rap/music-news content reliably generates the most comment debate of any niche (opinions, rankings, beefs). |
| 3 | @weebypods | 170k | meme | Big audience in the highest-share niche; memes propagate through DM shares and tags, which the algorithm rewards with reach. |
| 4 | @thatcatsabode | 137k | cat | Pet content has the highest baseline engagement rate on Instagram; large following amplifies it into strong absolute numbers. |
| 5 | @hithub12 | 70k | fight | Smallest of the top tier by followers, but fight/altercation clips pull disproportionate views and comments relative to audience size — likely the best view-to-follower ratio on the list. |
| 6 | @crimeworld81 | 108k | law/crime | True-crime/law content holds watch time well and draws opinionated comment sections; solid mid-large following. |
| 7 | @catsoftys | 91k | cat | Same high-engagement pet niche as #4 at roughly two-thirds the audience. |
| 8 | @irresistibletexting | 92k | texting | Text-conversation screenshots are save/share machines and comment bait, though views skew lower than clip-based niches. |
| 9 | @hiphoptide | 75k | music meme | Combines meme shareability with music-debate comments; mid-sized audience. |
| 10 | @nyanyathegoddess | 125k | babe | Large following but the niche is likes-heavy with comparatively low commenting and sharing, and reach is often algorithmically throttled. |
| 11 | @rxpfu | 96k | quote | Quote pages earn strong saves but weak comments and modest views; interactions are quieter than the follower count suggests. |
| 12 | @funny.dog.tv | 68k | dog | High-engagement pet niche, but the smallest audience among the animal pages caps absolute numbers. |
| 13 | @love_sonicpov | 40k | food | POV/food content performs well on Reels, but 40k followers limits total interaction volume. |
| 14 | @thieveslosingit | 34k | meme | Good shareable niche (theft-fail clips), small audience. |
| 15 | @girlyyglitter | 32k | girly | Smallest audience in a moderate-engagement aesthetic niche. |

## How the estimate was built

Score ≈ followers × niche multiplier, where multipliers reflect typical
2025–2026 Instagram behavior:

- **Very high** (views + comments): car fails, fight clips, rap/music news
- **High** (engagement rate / shares): cats, dogs, memes, food POV
- **Medium-high** (saves/shares): texting screenshots, music memes, crime
- **Medium** (likes-heavy or save-heavy, low comments): babe, quote, girly

Comments and shares are weighted above raw views because they are the
strongest signals of an engaged (and monetizable) audience.

## Getting the exact ranking

1. Collect per-post metrics for each page's last 10–20 posts into a CSV
   with columns `handle,views,likes,comments,shares,saves` (from Instagram
   professional-dashboard insights, the Meta Graph API, or a logged-in
   scraper run on your own machine).
2. Run:

   ```
   python scripts/rank_engagement.py data/posts.csv --accounts data/accounts.csv
   ```

   The script prints the numeric ranking by weighted engagement score per
   post, plus each page's engagement rate per follower.
