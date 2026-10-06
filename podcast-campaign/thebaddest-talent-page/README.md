# Avery Andon talent page for thebaddest.com

A drop-in talent profile page for the Astro site at `~/Documents/thebaddest`, plus a one-page PDF one-sheet.

| File | Goes to (in the site project) | What it is |
|---|---|---|
| `src/pages/talent/avery-andon.astro` | `src/pages/talent/avery-andon.astro` | The talent page, served at `/talent/avery-andon` |
| `public/talent/avery-andon/headshot.jpg` | `public/talent/avery-andon/headshot.jpg` | Press photo |
| `public/talent/avery-andon/avery-andon-one-sheet.pdf` | `public/talent/avery-andon/avery-andon-one-sheet.pdf` | One-sheet that the page's download buttons link to |
| `build_one_sheet.py` | (stays here) | Rebuilds the PDF: `python3 build_one_sheet.py` |
| `preview-desktop.png` | (stays here) | Screenshot of the built page |

## Install

From a terminal on the Mac, with this repo checked out next to the site:

```bash
git clone -b claude/zen-sagan-h15cyi https://github.com/AveryArtlife/art-discovery-agent.git /tmp/ada
cp -R /tmp/ada/podcast-campaign/thebaddest-talent-page/src/pages/talent ~/Documents/thebaddest/src/pages/
cp -R /tmp/ada/podcast-campaign/thebaddest-talent-page/public/talent ~/Documents/thebaddest/public/
cd ~/Documents/thebaddest && npm run dev   # then open http://localhost:4321/talent/avery-andon
```

Then deploy the site the usual way. Or open a Claude Code session in `~/Documents/thebaddest` and ask it to do the copy and add a link to the page from the site's talent/roster section.

## Notes

- The page is self-contained (its own `<head>` and scoped styles matching the live site: Anton, JetBrains Mono, the agency blue), so it doesn't depend on the site's layout component. If the site has a shared layout, it can be wrapped in it later.
- Spotify and YouTube embeds only render on the live site.
- Before publishing, check the agency phone number (`1305-791-990` looks one digit short) and confirm the philanthropy roles are ones you're happy to list publicly.
