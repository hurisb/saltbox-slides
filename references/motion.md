# Motion and light

Motion should feel like a motion designer made it: one ease family, staggered entrances, nothing bouncy
except small icon pops, and backgrounds that only move slowly.

## Transitions (engine, `go()` in the script)
- **Same scene:** the background stays. Content leaves (0.5s, power3.in, 28px up) and the next slide enters at 0.38s.
- **Scene change:** the outgoing scene fades (1.0s), the incoming one fades in from 106% scale (1.5s, expo.out); content enters at 0.55s.
- **Backwards:** the same, mirrored.
- `prefers-reduced-motion`: no movement, simple swaps.

## Entrances (`data-anim` values)
| Value | Effect |
|---|---|
| `lines` | Headline lines rise from a mask (`<span class="ln"><span>…</span></span>` per line) |
| `rise` | Fade + 36px rise |
| `fade` | Fade only (logos) |
| `rows` | Children stagger in (lists, grids) |
| `grow` | Horizontal rule draws from the left |
| `pop` | Scale-in (hub circles) |
| `draw` | SVG stroke draws |
| `wipe-left` | Cover photo panel wipes in |
| `panel` | Story panel wipes in, then its contents |
| `ghost` | Giant outline word slides in |
| `wheel` | Spokes, nodes, and labels stagger around the orbit |
Elements animate in DOM order 0.09s apart. Add `data-at="0.6"` to pin a start time.
Numbers with `data-count="250" data-suffix="+"` count up.

## Living light
- `.glow` = a blurred shape with `mix-blend-mode: overlay` that morphs (border-radius), wanders, and breathes.
  Place it inside a colored element (gradient cards, panels, dark scenes). Overlay has no effect on white.
  Per-instance variables: `--size --c --o --blur --dx --dy --t1 --t2`.
- **Dials** at the top of the styles (`:root`):
  - `--light-amp` (2.4) — how far lights travel and how much they change shape. 1 = subtle.
  - `--light-speed` (0.5) — multiplies cycle times. Lower = faster.
  - `--cursor-light-opacity` (0.15) — the cursor light layer, in overlay mode, like a Photoshop layer.
- **Cursor light:** add `data-cursor-light` to a slide (cover and thank-you by default). The light trails
  the pointer, stretches along its direction of travel, keeps morphing at rest, and drifts on its own
  after 3.5s without movement.

## Shortcuts (built into the engine)
| Keys | Action |
|---|---|
| → ↑ Space PageDown Enter | Next slide |
| ← ↓ PageUp Backspace | Previous slide |
| Home / End | First / last slide |
| 1–9 | Go to slide |
| ⌘B (Mac) / Ctrl+B (Windows) | Show / hide thumbnails |
| F | Fullscreen (thumbnails hide) |
| N | Speaker notes |
| Click right ⅔ / left ⅓ · swipe | Next / previous |
The controls (bottom right) and the thumbnails button (top left, when the sidebar is hidden) appear on
mouse movement and hide after 3 seconds.
