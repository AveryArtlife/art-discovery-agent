# Instagram Page Engagement Ranking — Real Data

Ranking of the available pages by measured engagement (views, comments,
interactions), built from live Apify scrapes taken **2026-07-30**:

- `apify/instagram-scraper` — last 20 posts per page (220 posts total)
- `apify/instagram-profile-scraper` — current follower counts

Raw converted data: `data/posts.csv`; follower counts refreshed in
`data/accounts.csv`. Reproduce with:

```
python scripts/rank_engagement.py data/posts.csv --accounts data/accounts.csv
```

Averages are per post over the last 20 posts; views average over video
posts only, likes over posts where the count is public. Score weights
comments (×8) above likes (×1) and views (×0.01). Engagement rate =
(avg likes + avg comments) / followers.

## Ranking (strongest engagement first)

| # | Handle | Followers | Niche | Avg views | Avg comments | Score/post | Eng. rate |
|---|--------|-----------|-------|-----------|--------------|------------|-----------|
| 1 | @catsoftys | 90,365 | cat | 12,924,776 | 485 | 492,917 | 398.7% |
| 2 | @thatcatsabode | 137,118 | cat | 344,408 | 67 | 75,401 | 52.1% |
| 3 | @weebypods | 170,362 | meme | 495,630 | 105 | 55,434 | 29.2% |
| 4 | @funny.dog.tv | 67,705 | dog | 41,058 | 38 | 6,725 | 8.9% |
| 5 | @irresistibletexting | 90,717 | texting | 51,070 | 3 | 4,927 | 4.9% |
| 6 | @idiotsdriving | 168,956 | car | 104,703 | 45 | 2,510 | 0.7% |
| 7 | @r.a.p | 172,955 | rap/music | 10,350 | 5 | 685 | 0.3% |
| 8 | @girlyyglitter | 31,922 | girly | 10,266 | 1 | 498 | 1.2% |
| 9 | @crimeworld81 | 107,399 | law | 21,287 | 7 | 386 | 0.1% |
| 10 | @hiphoptide | 74,786 | music meme | 8,172 | 1 | 243 | 0.2% |
| 11 | @thieveslosingit | 35,823 | meme | 9,851 | 3 | 242 | 0.4% |

## Accounts with no data

| Handle | Status |
|--------|--------|
| @love_sonicpov | Not found — deleted, banned, or renamed |
| @rxpfu | Not found — deleted, banned, or renamed |
| @hithub12 | Not found — deleted, banned, or renamed |
| @nyanyathegoddess | Restricted profile — Instagram blocks anonymous viewing; needs a logged-in scrape or insights export |

@crimeworld81 has renamed itself to **@cursedmemerz** (its URL redirects
there); its posts under both names are merged above.

## Reading the numbers

- **@catsoftys is the clear #1 but outlier-driven.** Its mean is inflated
  by one 72M-view reel; the median video still does ~585k views — several
  times anything else on the list. Only 9 of its last 20 posts are videos.
- **@thatcatsabode** engages heavily on image posts (~71k avg likes) but
  had only one recent video (344k views). 10 of 20 posts hide like counts.
- **@weebypods** mixes a 5.9M-view viral hit with a ~17k median — spiky
  but strong likes (~50k avg) and the second-best comment volume.
- **@idiotsdriving is the most *consistent* video performer**: median 55k
  views and median 38 comments per post with no outliers. If you want
  steady, predictable reach rather than viral spikes, it's effectively
  top-3 despite ranking #6 on averages.
- **Follower counts were badly misleading.** @r.a.p (173k), @crimeworld81
  (107k), and @hiphoptide (75k) all engage at 0.1–0.3% — likes in the
  hundreds and single-digit comments — consistent with inflated or dead
  followings. Meanwhile 90k-follower @catsoftys outperforms every page
  with more followers.
- Shares and saves are not publicly exposed by Instagram, so the score
  runs on views, likes, and comments.
