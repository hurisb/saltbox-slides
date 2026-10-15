# Converting a PowerPoint or Google Slides deck

## 1. Get a .pptx
- PowerPoint: use the attached file.
- Google Slides: read it with a Google Slides connector if available. Otherwise ask the user for
  **File → Download → Microsoft PowerPoint (.pptx)**.
- Keynote: **File → Export To → PowerPoint**.

## 2. Extract
```bash
pip install python-pptx            # once
python3 scripts/extract-pptx.py deck.pptx extracted/
```
This writes `extracted/outline.md` (titles, text, speaker notes per slide) and `extracted/media/`
(images, named by slide). Read the outline, not the raw XML.

## 3. Show what you found
Reply with a compact outline: slide number, title, a few words of content, and "notes: yes/no".
Flag conflicts (numbers, years, placeholders like "?"), empty slides, and images that look like logos.
Ask Round 2 questions from `questions.md`.

## 4. Map to layouts
Choose a layout per slide from `layouts.md`. Merge thin slides, split dense ones, and move long text
into speaker notes. Keep the user's order unless they agreed to regroup.

## 5. Build
Copy logos and photos from `extracted/media/` into `src/assets/` (trim whitespace, keep originals'
colors), then follow Phases 4–7 in SKILL.md.
