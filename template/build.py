#!/usr/bin/env python3
"""
Saltbox Slides — build a deck into ONE self-contained HTML file.

    python3 build.py                      # src/index.html  ->  dist/index.html
    python3 build.py my-deck/src/index.html my-deck/dist/index.html

What it does
  1. Inlines every  src="assets/…"  and  url(assets/…)  as a base64 data URI,
     so the output is a single file you can email, open offline, or deploy.
  2. Replaces  <i data-icon="Name"></i>  with the Untitled UI line icon of that name
     (the official S1/Saltbox icon set). Icons used from JS (icon:"Name") are inlined too.

Icons come from the free @untitledui/icons npm package (MIT). The first build
downloads it into ./node_modules automatically (needs Node.js / npm).
Find icon names at https://www.untitledui.com/free-icons
"""
import base64, mimetypes, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE / "src" / "index.html"
OUT = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else HERE / "dist" / "index.html"
SRC_DIR = SRC.parent

def icons_dir():
    for base in (SRC_DIR, SRC_DIR.parent, HERE):
        d = base / "node_modules" / "@untitledui" / "icons" / "dist"
        if d.exists():
            return d
    print("Downloading Untitled UI icons (one time)…")
    subprocess.run(["npm", "install", "--no-save", "--silent", "@untitledui/icons@0.0.23"], cwd=HERE, check=True)
    return HERE / "node_modules" / "@untitledui" / "icons" / "dist"

ICONS = None
def icon_svg(name, cls=""):
    global ICONS
    ICONS = ICONS or icons_dir()
    f = ICONS / f"{name}.mjs"
    if not f.exists():
        sys.exit(f"✗ Unknown icon '{name}'. Check the name at https://www.untitledui.com/free-icons")
    paths = re.findall(r'"path",\{d:"([^"]+)"', f.read_text())
    inner = "".join(f'<path d="{d}"/>' for d in paths)
    return (f'<svg class="ic {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>')

def data_uri(rel):
    p = SRC_DIR / rel
    if not p.exists():
        sys.exit(f"✗ Missing asset: {rel}")
    mime = mimetypes.guess_type(p.name)[0] or ("image/webp" if p.suffix == ".webp" else "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

html = SRC.read_text()
html = re.sub(r'(src=")(assets/[^"]+)(")', lambda m: m.group(1) + data_uri(m.group(2)) + m.group(3), html)
html = re.sub(r'url\((["\']?)(assets/[^)"\']+)\1\)', lambda m: f'url("{data_uri(m.group(2))}")', html)
html = re.sub(r'<i data-icon="(\w+)"(?: class="([^"]*)")?></i>', lambda m: icon_svg(m.group(1), m.group(2) or ""), html)
names = sorted(set(re.findall(r'icon:\s*"(\w+)"', html)))
table = "{" + ",".join(f'"{n}":' + repr(icon_svg(n)) for n in names) + "}"
html = html.replace("/*__ICON_TABLE__*/{}", table)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
print(f"✓ Built {OUT}  ({OUT.stat().st_size / 1024:.0f} KB)")
