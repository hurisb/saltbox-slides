#!/usr/bin/env bash
# Package the skill for Claude.ai upload (Customize → Skills → Upload a skill).
# Claude.ai needs a ZIP whose folder name matches the skill name: saltbox-slides/SKILL.md
#   bash scripts/package-skill.sh   →  release/saltbox-slides.zip
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
DEST="$TMP/saltbox-slides"
mkdir -p "$DEST/template"
cp "$ROOT/SKILL.md" "$DEST/"
cp -R "$ROOT/references" "$ROOT/scripts" "$DEST/"
cp -R "$ROOT/template/src" "$DEST/template/src"
cp "$ROOT/template/build.py" "$DEST/template/"
mkdir -p "$ROOT/release"
rm -f "$ROOT/release/saltbox-slides.zip"
(cd "$TMP" && zip -qr "$ROOT/release/saltbox-slides.zip" saltbox-slides -x '*.DS_Store')
echo "✓ release/saltbox-slides.zip"
