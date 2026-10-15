# Essential questions

Ask these before building. Use a multiple-choice question tool when available: put the
recommended option first and keep each question to 2–4 options (the user can always type their own).
Two rounds maximum. Skip anything the user already told you.

## Round 1 — always

| # | Question | Typical options |
|---|---|---|
| 1 | **Who will see this, and how?** | Presented live (presenter clicks, notes help) · Shared link, read alone (slides must stand alone) · Both |
| 2 | **What should people do after the last slide?** | Free text. Push for one sentence: "book a follow-up", "pick an account", "approve the budget" |
| 3 | **How should I treat your content?** | Tighten and restructure (keep every idea, rewrite for clarity, move detail to notes) · Keep the text as-is, only redesign |
| 4 | **How long?** | ~5 min / 6–8 slides · ~15 min / 10–14 slides · ~30 min / 15–20 slides · Match the source deck |

## Round 2 — only when it applies

| When | Question |
|---|---|
| Sources disagree | "This deck says **250+** certifications and the proposal template says **350+**. Which is correct?" Quote both. |
| Dates look stale | "The slide says **2025** in a FY2027 deck. Should it be 2027?" |
| A placeholder or "?" appears | "'Superior? MFG Cloud' — is Superior a confirmed client I can show?" |
| Logos or people appear | "Can these client logos and this contact (name, photo, email) be shown to this audience?" |
| A link is wanted | "Local file only, or a Vercel link? Vercel links are public to anyone who has them." |
| Converting | "Keep your slide order, or may I regroup slides into a stronger story?" |

## Defaults when nobody can answer
Presented live · tighten and restructure · match the source length · local file only, no deploy.
State the defaults you used at the top of your reply.

## Example requests and how to read them

| The user says | Mode | What to ask |
|---|---|---|
| "Use saltbox-slides to make a 10-slide deck about our Q3 delivery wins." | New deck | Round 1, plus "Do you have numbers or client names I can use?" |
| "Use saltbox-slides to convert this .pptx." (file attached) | Convert | Round 1 (3 and 4), then show the extracted outline |
| "Redesign this Google Slides deck in our 2027 theme: <link>" | Convert | Round 1; ask for a .pptx export if you can't read the link |
| "Make the light on slide 1 subtler." | Edit | Nothing. Lower `--cursor-light-opacity` and confirm the new value |
| "I need slides for tomorrow's kickoff." (nothing else) | New deck | Round 1 in full; offer to start from an outline you draft |
