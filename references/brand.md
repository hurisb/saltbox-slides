# Saltbox brand rules for slides

Source of truth: the Saltbox brand guideline (sb-brandguideline) and the Saltbox Mgmt 2027 master theme.

## Color
| Token | Value | Use |
|---|---|---|
| `--sb-blue` | `#1F4796` | Titles, key UI, icons on light |
| `--sb-purple` | `#7F3F98` | **Only inside the gradient.** Never alone |
| `--sb-gradient` | `linear-gradient(45deg, #1F4796, #7F3F98)` | Highlight cards, numbers (as text fill), CTAs, story panels |
| Grays | `#181D27` text · `#414651` body · `#535862` secondary · `#E9EAEB` borders | Light slides |
| On dark | `#FFFFFF` · `rgba(255,255,255,.74)` secondary | Dark and gradient slides |
Approved pairings: white on brand blue, brand blue on white, dark text on light brand-blue tint.

## Type
- **Space Grotesk** (headlines, numbers, labels on cards): 600 weight, tight tracking (-0.02 to -0.035em).
- **Inter** (body, notes, captions): 400/500. Uppercase eyebrows at 600 with +0.16em tracking.
- Scale on the 1920×1080 stage: hero 128–176 · H1 104 · H2 72 · card titles 26–36 · body 21–25 · minimum 18.

## Backgrounds (scenes)
| Scene | Image | Use for |
|---|---|---|
| `light` | white + blue/violet light bottom-right + hex top-left | Content slides |
| `dark` | deep purple + light rising from the bottom + hex | Cover, section dividers |
| `gradient` | blue → magenta | Logo screens, thank you |
Consecutive slides on the same scene share one background, so only content moves.

## Logos
- White Saltbox logo on dark/gradient, blue on light. Never redraw, recolor, stretch, or add effects.
- Client logos: use the client's own file on a white tile. Confirm they may be shown.

## Icons
Untitled UI line icons only (`<i data-icon="Name"></i>`; names at untitledui.com/free-icons).
Same style across a deck. 20–30px inside 44–56px tinted chips.

## Tone of voice
- **Reliable:** say exactly what happens and what the client gets. No vague promises.
- **Magnetic:** short sentences, get to the point, make it interesting.
- **Grounded:** practitioner words, not consultant words.
Write in active voice. Avoid em-dash asides, "not X but Y" framing, and filler like "leverage", "unlock", "holistic".
