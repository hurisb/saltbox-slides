---
name: saltbox-slides
description: Build animated, on-brand Saltbox Mgmt presentations as one self-contained HTML file using the Saltbox 2027 master theme (light/dark/gradient backgrounds, moving light, thumbnails sidebar, speaker notes). Use whenever someone asks for a Saltbox deck, slides or presentation, wants to convert a PowerPoint (.pptx) or Google Slides deck into the Saltbox theme, redesign an existing deck, or names saltbox-slides.
---

# Saltbox Slides

You make presentations that look and move like Saltbox: the 2027 master theme backgrounds,
Brand Blue `#1F4796` + the blue→purple gradient, Space Grotesk headlines, Inter body text,
Untitled UI line icons, and slow living light. The output is **one HTML file** with every
asset inlined, so it opens offline, deploys anywhere, and can be edited later by chat.

## Non-negotiables

1. **Ask before you build.** Run Phase 1. A wrong guess on audience or source costs a rebuild.
2. **Three slides first.** Build slides 1–3, show them, and stop until the user approves. Then build the rest.
3. **Start from `template/`.** Never write a deck from scratch. The engine (stage scaling, transitions,
   thumbnails, notes, cursor light, shortcuts) lives in `template/src/index.html`. Copy it, keep the engine,
   replace the slides.
4. **Brand rules from `references/brand.md`.** Purple never appears alone, only inside the gradient.
   Logos are never redrawn or recolored. Icons are Untitled UI only.
5. **Never invent facts.** If sources disagree (a number, a year, a client name), ask. Don't put a figure on a
   claim the source doesn't quantify.
6. **Flag what you changed.** When you tighten copy, list the wording changes in your reply.
7. **Public content check.** Before anything is deployed or published, ask whether the deck holds client logos,
   personal contacts, or internal numbers, and whether the link may be public.

## Files and when to load them (progressive disclosure)

| File | Load when |
|---|---|
| `references/questions.md` | Phase 1, always |
| `references/brand.md` | Phase 3, before writing any slide |
| `references/layouts.md` | Phase 3, to pick a layout per slide |
| `references/motion.md` | Phase 4, when adding or tuning animation and light |
| `references/convert-pptx.md` + `scripts/extract-pptx.py` | Phase 2, only for .pptx / Google Slides input |
| `references/deploy-vercel.md` + `scripts/deploy.sh` | Phase 7, only if the user wants a link |
| `template/src/index.html` | Phase 3, copy it as the starting point |

## Workflow

### Phase 0 · Detect the mode
- **New deck** from notes, a doc, or a topic.
- **Convert** a .pptx or a Google Slides deck.
- **Redesign** an existing HTML deck made with this skill (edit in place, keep the engine).
- **Edit** a deck already built in this conversation (skip to the change; rebuild; re-deliver).

### Phase 1 · Essential questions
Load `references/questions.md`. Ask in at most two rounds of up to four questions each, using a
multiple-choice question tool when available (recommended option first). Always cover:
1. **Audience and setting.** Who sees it, and is it presented live or read alone?
2. **Goal.** What should people do after the last slide?
3. **Source and copy.** What material exists, and may you tighten and restructure it?
4. **Length.** Minutes available or number of slides.
5. **Facts to confirm.** Any conflicting numbers, outdated years, unconfirmed client names or logos.
6. **Sharing.** Local file only, a Claude artifact link, or Vercel. Public or internal?
Skip any question the user already answered. If the user is not around to answer, take the most
reasonable reading, state it at the top of your reply, and continue.

### Phase 2 · Content intake
- Notes / doc / topic: outline directly.
- PowerPoint: follow `references/convert-pptx.md` (run `scripts/extract-pptx.py`, show what was found).
- Google Slides: read it with a Google Slides connector if one is available; otherwise ask the user for
  File → Download → .pptx (or PDF) and treat it as a PowerPoint.
- Images and logos: reuse the originals. Never recreate a logo.

### Phase 3 · Outline and setup
1. Propose a slide-by-slide outline: number, layout (from `references/layouts.md`), scene
   (`light`, `dark`, `gradient`), and the headline. Openers, dividers, and the close use dark/gradient;
   content uses light. Group same-scene slides so the background carries across them.
2. Copy `template/` into a new deck folder (`scripts/new-deck.sh my-deck`).
3. Replace the demo slides in `src/index.html` with yours. Keep everything outside the slides.
4. Update `<title>` and the sidebar title (`.rail-head strong`).

### Phase 4 · Build slides 1–3 and stop
Build, run `python3 build.py`, and check them (screenshots if you can render; see Phase 6).
Deliver the file and ask for feedback. Do not continue until the user approves.

### Phase 5 · Build the rest
Same rules. Give every slide `data-title` and `<aside class="notes">` speaker notes.

### Phase 6 · Quality check
- Nothing overflows the 1920×1080 stage; no text under 18px; headlines wrap where intended.
- Each slide's animated elements carry `data-anim`; the first frame after entrance is complete.
- Light layers use `mix-blend-mode: overlay` on colored grounds only (it has no effect on white).
- Thumbnails render every slide; ⌘B / Ctrl+B toggles them; F hides them in fullscreen.
- Copy follows the tone in `references/brand.md` (Reliable, Magnetic, Grounded).
- If a browser renderer is available (e.g. Playwright), screenshot each slide and look at it.

### Phase 7 · Deliver
- Always: the built `dist/index.html` as a file the user can open locally.
- Optional link: Vercel via `references/deploy-vercel.md`, after the public-content check.
- Tell the user how to edit later: "Ask Claude: in saltbox-slides deck X, change slide 4's title to …".

## Editing a finished deck
Edit `src/index.html` (never the built file), rebuild, re-deliver. Common asks map to:
- Copy → the slide's HTML. Light intensity → `--light-amp`, `--light-speed`, `--cursor-light-opacity` at the top of the styles.
- Wheel labels/icons → the `SERVICES` array in the script. Reorder slides → move `<section>` blocks.
