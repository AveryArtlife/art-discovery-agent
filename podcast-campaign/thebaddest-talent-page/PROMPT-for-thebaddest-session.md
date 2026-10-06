Paste this into a Claude Code session opened in `~/Documents/thebaddest` (the TheBaddest agency website project):

---

I need two things in this project (the Astro site for thebaddest.com).

**1. Put this project on GitHub so my cloud Claude sessions can work on it.**
- If this folder isn't a git repo yet, run `git init` and make a first commit. Check `.gitignore` covers `node_modules`, `dist`, `.astro` and any `.env` files, and never commit secrets or API keys.
- Create a **private** GitHub repo named `AveryArtlife/thebaddest` (use `gh repo create AveryArtlife/thebaddest --private --source . --push` if `gh` is installed and logged in; otherwise tell me the exact steps to create it on github.com and push).
- Push the `main` branch and confirm the repo URL.
- Tell me if the site is deployed from this repo (Vercel, Netlify or similar). If it's connected to a host, tell me which branch deploys to production.

**2. Add Avery Andon's talent page.**
- The finished files are on the `claude/zen-sagan-h15cyi` branch of `https://github.com/AveryArtlife/art-discovery-agent`, in `podcast-campaign/thebaddest-talent-page/`. Clone that branch into a temp folder and copy:
  - `src/pages/talent/avery-andon.astro` → `src/pages/talent/avery-andon.astro`
  - `public/talent/avery-andon/` (headshot.jpg, avery-andon-one-sheet.pdf) → `public/talent/avery-andon/`
- The page is self-contained (its own `<head>` and styles). If this site has a shared layout with the header and nav, adapt the page to use it, keeping the page's design, and make sure the header matches the rest of the site.
- Add a link to `/talent/avery-andon` from wherever the site lists talent or clients (create a simple "Talent" link in the nav if there's nothing yet).
- Run the dev server and check `/talent/avery-andon` at desktop and phone widths: no horizontal scroll, the headshot loads, and the one-sheet PDF downloads.
- Run the production build (`npm run build`) and fix any errors.
- Commit on a new branch `talent/avery-andon`, push it, and open a pull request. Don't deploy to production until I've looked at the preview.

When you're done, give me the GitHub repo URL, the PR link and a preview URL if the host makes one.
