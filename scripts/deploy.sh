#!/usr/bin/env bash
# Deploy a built Saltbox deck to Vercel (free Hobby plan).
#   bash scripts/deploy.sh path/to/dist/index.html [project-name]
# First run: Vercel asks you to log in (email or GitHub) in your browser.
set -euo pipefail

FILE="${1:?Usage: bash scripts/deploy.sh path/to/index.html [project-name]}"
NAME="${2:-saltbox-deck}"
[ -f "$FILE" ] || { echo "✗ File not found: $FILE"; exit 1; }
command -v npx >/dev/null || { echo "✗ Node.js is required: https://nodejs.org (LTS)"; exit 1; }

TMP="$(mktemp -d)"
cp "$FILE" "$TMP/index.html"
echo "→ Deploying $FILE as '$NAME'…"
cd "$TMP"
npx --yes vercel@latest deploy --prod --yes --name "$NAME"
echo "✓ Done. Vercel links are public to anyone who has them."
