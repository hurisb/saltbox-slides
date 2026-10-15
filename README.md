# Saltbox Slides

**Welcome!** 👋 This is the Saltbox Mgmt skill for making presentations with Claude.

You bring the content (notes, an old deck, a PowerPoint, or just an idea). Claude asks you a few
questions, shows you the first three slides, and then builds a full deck in the **Saltbox 2027 theme**:
our backgrounds, Brand Blue and the blue→purple gradient, Space Grotesk and Inter, Untitled UI icons,
and slow, living light. You get **one HTML file** that opens in any browser, works offline, and can be
shared as a link.

You don't need to know how to code. If you can describe what you want, you can use this.

▶ **See it first:** open [`examples/demo/index.html`](examples/demo/index.html) (download it and double-click),
or view the **[live demo](https://saltbox-slides-demo.vercel.app)**.

---

## Contents
1. [Install the skill](#1-install-the-skill)
2. [Make your first deck](#2-make-your-first-deck)
3. [What Claude will ask you](#3-what-claude-will-ask-you)
4. [Presenting: keyboard shortcuts](#4-presenting-keyboard-shortcuts)
5. [Change anything later](#5-change-anything-later)
6. [Convert a PowerPoint](#6-convert-a-powerpoint)
7. [Deploy to Vercel with a free account](#7-deploy-to-vercel-with-a-free-account)
8. [Use it in S1](#8-use-it-in-s1)
9. [What's in this repo](#9-whats-in-this-repo)

---

## 1. Install the skill

### In Claude.ai (web or desktop app)
1. Make sure **code execution** is on: *Settings → Capabilities → Code execution and file creation*.
   (On Team/Enterprise plans an owner turns it on for the organization.)
2. Download **[`release/saltbox-slides.zip`](release/saltbox-slides.zip)** from this repo.
   Use this file, not GitHub's green "Download ZIP" button: Claude needs the folder inside to be named `saltbox-slides`.
3. Go to **Customize → Skills → + → Create skill → Upload a skill** and choose the ZIP.
4. Make sure the toggle next to **saltbox-slides** is on.

Team admins can share it with everyone from the skill's **⋯ → Share**, or **Publish to org**.
More detail: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### In Claude Code
```bash
git clone https://github.com/hurisb/saltbox-slides.git ~/.claude/skills/saltbox-slides
```

### Check it worked
Ask Claude: *"Which skills can you use?"* You should see **saltbox-slides** in the list.

---

## 2. Make your first deck

Start your message with **"Use saltbox-slides to …"** so Claude knows which skill to load. Some examples:

**You have nothing yet, just an idea**
> Use saltbox-slides to make a 10-slide deck for a client kickoff with Acme Manufacturing. We'll present it live on a call.

**You have notes or a document**
> Use saltbox-slides to turn these notes into a deck for our AE enablement session. *(paste the notes or attach the doc)*

**You have an existing deck (Google Slides)**
> Use saltbox-slides to redesign this deck in our 2027 theme: https://docs.google.com/presentation/d/…
> Keep every idea, but tighten the copy.

**You have a PowerPoint**
> Use saltbox-slides to convert the attached sales-kickoff.pptx and keep my speaker notes.

**You want a quick change on a deck Claude already made**
> In my saltbox-slides deck, make the light on the cover subtler and change slide 4's title to "Where we win".

### What happens next
1. Claude asks a few questions (see below).
2. Claude shows you the outline, then builds **slides 1–3** and stops so you can review them.
3. You say what to change, or "continue".
4. You get the full deck as `index.html`. Double-click to open it. Want a link? See [section 7](#7-deploy-to-vercel-with-a-free-account).

---

## 3. What Claude will ask you

The skill always checks the essentials before building (full list in [`references/questions.md`](references/questions.md)):

| Question | Why it matters |
|---|---|
| Who will see it, and is it presented live or read alone? | Live decks get speaker notes and lighter slides; self-read decks need slides that stand on their own. |
| What should people do after the last slide? | Every deck ends on one clear action. |
| May I tighten and restructure your content? | Or keep your words exactly. Claude lists every wording change. |
| How long is it? | Minutes available or number of slides. |
| Do any facts disagree? | Claude flags conflicting numbers, old years, placeholders, and asks before using client logos or contacts. |
| Where will it go? | A local file, a Claude link, or Vercel (public link). |

If you're in a hurry, say *"use your best judgment"* and Claude will pick sensible defaults and tell you what it chose.

---

## 4. Presenting: keyboard shortcuts

| Keys | Action |
|---|---|
| **→** or **↑** (also Space, Enter, Page Down) | Next slide |
| **←** or **↓** (also Backspace, Page Up) | Previous slide |
| **Home** / **End** | First / last slide |
| **1–9** | Jump to that slide |
| **⌘B** (Mac) / **Ctrl+B** (Windows) | Show or hide the thumbnails sidebar |
| **F** | Fullscreen (the sidebar hides automatically) |
| **N** | Speaker notes |
| Click the right ⅔ / left ⅓ of a slide, or swipe | Next / previous |

The controls in the bottom-right corner, and the thumbnails button in the top-left (when the sidebar is
hidden), appear when you move the mouse and fade away after 3 seconds.

On the cover and the last slide, a soft light follows your cursor. 🙂

---

## 5. Change anything later

Just ask Claude in plain words. Some useful ones:

| You say | What changes |
|---|---|
| "Make the moving light subtler / livelier." | The light dials at the top of the file: `--light-amp`, `--light-speed` |
| "Make the cursor light 10%." | `--cursor-light-opacity` (it's an Overlay layer, like in Photoshop) |
| "Add a slide after 5 comparing our three packages." | A new slide using the best-fitting layout |
| "Swap the client logos on slide 4." | Attach the logo files; Claude places them on white tiles |
| "Move slide 7 before slide 5." | Reorders the slides |

Prefer to edit yourself? The source is `src/index.html`: one `<section>` per slide, with comments.
Run `python3 build.py` afterwards to rebuild the single file.

---

## 6. Convert a PowerPoint

1. **Get a .pptx.** Google Slides: *File → Download → Microsoft PowerPoint (.pptx)*. Keynote: *File → Export To → PowerPoint*.
2. **Attach it** and say: *"Use saltbox-slides to convert this deck."*
3. Claude runs [`scripts/extract-pptx.py`](scripts/extract-pptx.py), which pulls out every slide's text, speaker notes, and images, and shows you the outline it found.
4. Claude flags anything that needs a decision (conflicting numbers, empty slides, logos), then maps each slide to a Saltbox layout.
5. You review the first three slides, then get the full deck.

Running it yourself:
```bash
pip install python-pptx
python3 scripts/extract-pptx.py my-deck.pptx extracted/
# → extracted/outline.md and extracted/media/
```

---

## 7. Deploy to Vercel with a free account

Vercel hosts your deck at a link like `https://my-deck.vercel.app`. The free **Hobby** plan is enough.

> ⚠️ Anyone with the link can open the deck. Check for client logos, personal contacts, and internal numbers before you share it.

### Create your free account (once)
1. Go to **vercel.com** → **Sign Up** → choose **Hobby** (free).
2. Continue with **GitHub** (easiest) or with your email.

### Option A: From GitHub, no terminal (recommended)
1. On GitHub, create a repository (it can be **private**) and upload your deck's `index.html` to it.
2. On Vercel: **Add New… → Project → Import** your repository → **Deploy**.
3. Your link appears in about 30 seconds. Every time you upload a new `index.html`, Vercel updates the link.
4. To change the link name: Project → **Settings → General → Project Name**.

### Option B: From your computer, one command
You need [Node.js](https://nodejs.org) (LTS). Then:
```bash
bash scripts/deploy.sh path/to/index.html my-deck-name
```
The first time, Vercel opens your browser to log in. The link is printed at the end.

### Option C: No hosting
Send the `index.html` file itself (email, Slack, Drive). It opens in any browser, even offline.

---

## 8. Use it in S1

🚧 **Coming soon.** We'll document how to run saltbox-slides from S1, so decks can draw on project
context directly. If you have ideas for this, open an issue.

---

## 9. What's in this repo

```
saltbox-slides/
├── SKILL.md                  ← instructions Claude follows (the workflow)
├── references/
│   ├── questions.md          ← the questions Claude asks, with example requests
│   ├── brand.md              ← colors, type, backgrounds, logos, icons, tone of voice
│   ├── layouts.md            ← the 10 layouts and when to use each
│   ├── motion.md             ← transitions, entrances, living light, shortcuts
│   ├── convert-pptx.md       ← PowerPoint / Google Slides conversion
│   └── deploy-vercel.md      ← publishing a link
├── template/
│   ├── src/index.html        ← the deck engine + demo slides (start every deck from this)
│   ├── src/assets/           ← 2027 master theme backgrounds and Saltbox logos
│   └── build.py              ← inlines assets + icons into one HTML file
├── scripts/
│   ├── new-deck.sh           ← copy the template into a new deck folder
│   ├── extract-pptx.py       ← read a PowerPoint
│   ├── deploy.sh             ← deploy to Vercel
│   └── package-skill.sh      ← rebuild release/saltbox-slides.zip
├── release/saltbox-slides.zip ← upload this to Claude.ai
└── examples/demo/index.html   ← the demo deck, built
```

### How it's made (good practices we follow)
- **One file, no build step for viewers.** Every image, icon, and style is inside the HTML.
- **Ask before building, review three slides early.** It's cheaper to change direction on slide 3 than slide 15.
- **Progressive disclosure.** Claude only reads the reference file it needs for the current step.
- **Fixed 16:9 stage.** Slides are designed at 1920×1080 and scale to any screen, so nothing reflows unexpectedly.
- **Motion with restraint.** One easing family, staggered entrances, light that moves slowly, and full support for *reduce motion*.
- **Comments are kindness.** The template explains itself, so anyone can edit it.

Workflow ideas adapted from [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by Zara Zhang (MIT). Thank you!

## License
Code: MIT. Saltbox logos, theme backgrounds, and brand guidelines © Saltbox Mgmt. Use them for Saltbox work only.
Icons: [Untitled UI free icons](https://www.untitledui.com/free-icons) (MIT).
