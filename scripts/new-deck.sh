#!/usr/bin/env bash
# Start a new deck from the Saltbox template.
#   bash scripts/new-deck.sh my-deck
# Creates my-deck/ with src/index.html (the demo deck, ready to replace) and build.py.
set -euo pipefail
NAME="${1:?Usage: bash scripts/new-deck.sh my-deck}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
[ -e "$NAME" ] && { echo "✗ $NAME already exists"; exit 1; }
mkdir -p "$NAME"
cp -R "$ROOT/template/src" "$NAME/src"
cp "$ROOT/template/build.py" "$NAME/build.py"
echo "✓ Created $NAME/"
echo "  Edit   $NAME/src/index.html"
echo "  Build  python3 $NAME/build.py   →  $NAME/dist/index.html"
