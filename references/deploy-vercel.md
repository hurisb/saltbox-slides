# Deploy a deck to Vercel (free Hobby plan)

A deck is one `index.html`, so it deploys as a static site with no build step.
**Vercel links are public to anyone who has them.** Confirm the content may be shared before deploying.

## Option A — From GitHub (recommended for teams)
1. Put the built deck in a repo as `index.html` (private repos work on the free plan).
2. Sign in at vercel.com with GitHub → **Add New… → Project** → pick the repo → **Deploy**.
3. Every push redeploys automatically. Rename the project in **Settings** to change the URL.

## Option B — From your computer (CLI)
```bash
bash scripts/deploy.sh path/to/dist/index.html my-deck-name
```
The script installs nothing globally; it runs `npx vercel` and walks you through the first login
(email or GitHub). The link appears at the end, like `https://my-deck-name.vercel.app`.

## Option C — No account needed to view
Send the HTML file itself. It opens in any browser, offline.
