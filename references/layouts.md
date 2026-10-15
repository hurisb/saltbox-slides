# Layout catalog

Every layout below exists in `template/src/index.html` (the demo deck). Copy the `<section>` and change
the content. All sizes are stage pixels on a 1920×1080 canvas.

| Layout | Demo slide | Scene | Best for | Capacity |
|---|---|---|---|---|
| **Cover** (`.cover`) | 1 | dark | Opening: eyebrow, 1–2 line title, one-line lead, meta row (e.g. "Prepared for", "Fiscal year"), optional partner badge. Photo panel on the right with Ken Burns motion. Cursor light on. | Title ≤ 2 lines |
| **Agenda** (`.agenda`) | 2 | light | Numbered sections (a real sequence). Giant outline word behind. | 3–6 rows |
| **Statement and wheel** (`.meet`) | 3 | light | Who we are: statement card in the gradient, 3 proof stats with count-up, services orbit built from the `SERVICES` array. | 6–10 services |
| **Tile grid** (`.ind-grid`) | 4 | light | Segments, industries, features. Each tile: icon, title, small subtitle, optional client logos. | 4–8 tiles |
| **Signal cards** (`.sig-grid`) | 5 | light | Checklists in six titled groups; `.tag` pills cross-reference other slides. | 6 cards × 2–4 bullets |
| **Section divider** (`.divider`) | 6 | dark | Introduces a section; three glass cards preview what's coming. | 3 cards |
| **Panel and columns** (`.play`) | 7 | light | A play, case, or offer: gradient story panel (label, title, use case, customer logos) + two columns (bullets, item cards). Panel wipes in. | 4–6 bullets + 4–5 items |
| **Resource cards** (`.res-grid`) | 8 | light | Three offers plus a contact card in the gradient. | 3 + 1 |
| **Two-step CTA** (`.cta-grid`) | 9 | light | Next steps: a list card and a gradient action card with a flow of pills. | 4 list rows |
| **Thank you** (`.thanks`) | 10 | gradient | Close with a contact pill. Cursor light on. | — |

## Rules
- One idea per slide. If a slide needs more than the capacity above, split it.
- Headlines say the point ("Three plays to win manufacturers"), not the topic ("Overview").
- Numbers like 01/02 only when the content is truly a sequence.
- Content slides end with the footer logo (`<img class="foot">`) and `<span class="folio"></span>` (auto-numbered).
- Every slide gets `data-scene`, `data-title`, and speaker notes in `<aside class="notes">`.
