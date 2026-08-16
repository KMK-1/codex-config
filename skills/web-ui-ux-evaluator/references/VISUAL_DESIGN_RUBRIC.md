# Visual Design Audit Rubric

Use this rubric when the user asks for a **visual-only**, **design-only**, **aesthetic/UI craft**, or **visual polish** review. It is a specialist mode inside `web-ui-ux-evaluator`, not a replacement for the core UX audit.

## Scope boundary

Score only what can be judged from rendered visual evidence or implementation styling.

Do score:
- visual hierarchy and composition;
- layout and grid discipline;
- spacing and whitespace rhythm;
- typography;
- color and visual contrast;
- component visual consistency;
- visual density and scanability;
- polish and detail quality;
- responsive visual quality.

Do not include in the Visual Score:
- business logic;
- API/data correctness;
- task success that requires interaction;
- navigation behavior not visible in the evidence;
- actual performance;
- product analytics;
- SUS/HEART;
- backend architecture.

Accessibility findings may be mentioned when visually observable, but a visual-only audit must not claim full WCAG conformance.

---

# Visual score — 100 points

| Dimension | Weight |
|---|---:|
| Visual hierarchy & composition | 20 |
| Layout & grid | 15 |
| Spacing & whitespace | 15 |
| Typography | 15 |
| Color & visual contrast | 10 |
| Component consistency | 10 |
| Visual density & scanability | 5 |
| Polish & micro-detail | 5 |
| Responsive visual quality | 5 |
| **Total** | **100** |

Score each dimension from 1–5, then calculate:

`dimension_points = (dimension_score / 5) × dimension_weight`

`visual_score = sum(dimension_points)`

## Score anchors

| Score | Meaning |
|---|---|
| 5 | Excellent — intentional, coherent, refined, no meaningful visual defect |
| 4 | Good — strong overall with minor inconsistencies or polish gaps |
| 3 | Acceptable — usable and understandable but visibly uneven or generic |
| 2 | Weak — hierarchy, spacing, typography, consistency, or composition repeatedly harms clarity |
| 1 | Poor — visual structure is fundamentally confusing, inconsistent, or broken |

Never assign a score from taste alone. Every score below 5 needs concrete observable evidence.

---

## 1. Visual hierarchy & composition — 20

Inspect:
- whether the eye is led to the primary information/action first;
- clear primary, secondary, tertiary emphasis;
- size/weight/color/position used intentionally;
- focal points and competing emphasis;
- grouping by proximity and enclosure;
- balance of major regions;
- page composition and visual flow;
- excessive cardification or containers without hierarchy value;
- whether decorative elements compete with content.

Ask: **Can a user understand what matters first, second, and third at a glance?**

## 2. Layout & grid — 15

Inspect:
- alignment consistency;
- shared edges and baselines;
- column logic;
- container widths;
- grid regularity where appropriate;
- intentional asymmetry where used;
- relationship between sidebar/header/content regions;
- awkward orphaned elements;
- accidental misalignment;
- balance across the viewport.

Do not penalize asymmetry merely for being asymmetrical. Penalize it when relationships appear accidental or reduce comprehension.

## 3. Spacing & whitespace — 15

Inspect:
- padding consistency;
- gaps between related/unrelated elements;
- vertical rhythm;
- section separation;
- whitespace around headings and CTAs;
- cramped controls;
- excessive dead space;
- inconsistent spacing tokens;
- nested containers with compounding padding;
- whether proximity accurately communicates grouping.

Prefer a small coherent spacing scale over many arbitrary values.

## 4. Typography — 15

Inspect:
- heading hierarchy;
- body readability;
- font size relationships;
- font weight discipline;
- line height;
- line length;
- letter spacing where relevant;
- label/value distinction;
- numeric/table typography;
- unnecessary variety of font sizes/weights;
- truncation/wrapping that harms presentation.

Typography should establish hierarchy before borders, shadows, and color are used to compensate.

## 5. Color & visual contrast — 10

Inspect:
- palette coherence;
- semantic use of color;
- primary/accent color discipline;
- foreground/background separation;
- muted text legibility risk;
- excessive accent colors;
- status colors used consistently;
- dark/light surface relationships;
- borders/dividers that are too strong or too weak;
- information communicated by color alone.

When contrast is not measured, describe it as a **contrast risk**, not a verified WCAG failure.

## 6. Component consistency — 10

Inspect:
- buttons;
- inputs;
- cards;
- tables;
- badges/chips;
- tabs;
- navigation items;
- modals/drawers;
- icons;
- border radius;
- borders;
- shadows;
- selected/active/disabled/error/success visual states.

Repeated components should share a visual grammar unless the difference communicates meaning.

## 7. Visual density & scanability — 5

Inspect:
- information per viewport;
- ability to scan sections quickly;
- excessive separators, labels, metadata, or chrome;
- dashboard density relative to task context;
- repeated visual noise;
- whether dense information is structured rather than merely spaced out.

Do not assume low density is better. Enterprise tools and dashboards may legitimately be dense.

## 8. Polish & micro-detail — 5

Inspect:
- icon sizing/alignment;
- border consistency;
- shadow quality;
- radius consistency;
- divider placement;
- baseline alignment;
- text clipping;
- awkward wrapping;
- tiny spacing defects;
- inconsistent control heights;
- decorative restraint.

Polish findings should not outrank structural hierarchy/layout problems.

## 9. Responsive visual quality — 5

When evidence exists at multiple widths, inspect:
- preservation of hierarchy;
- reflow quality;
- cramped or stretched layouts;
- card/table/chart adaptation;
- navigation composition;
- fixed/sticky collisions;
- typography scaling;
- spacing changes;
- horizontal overflow;
- priority of content across breakpoints.

If only one viewport is supplied, mark this dimension `Not verified` and renormalize the score across applicable dimensions rather than guessing.

---

# Visual finding impact

Use the core S0–S4 severity model when the visual issue materially affects usability or accessibility. For design-specific prioritization, also tag one of:

- **High** — strongly harms hierarchy, comprehension, brand coherence, or visual usability;
- **Medium** — noticeable inconsistency or quality issue;
- **Polish** — small craft/detail improvement.

Do not label a purely cosmetic preference as Critical.

---

# Required Visual Audit output

## Visual summary
- Evidence mode
- Viewports/screens reviewed
- Visual Score / 100
- Strongest 3 visual qualities
- Highest-impact 3 visual issues

## Visual scorecard

| Dimension | Weight | Score (1–5) | Points | Evidence |
|---|---:|---:|---:|---|
| Visual hierarchy & composition | 20 | | | |
| Layout & grid | 15 | | | |
| Spacing & whitespace | 15 | | | |
| Typography | 15 | | | |
| Color & visual contrast | 10 | | | |
| Component consistency | 10 | | | |
| Visual density & scanability | 5 | | | |
| Polish & micro-detail | 5 | | | |
| Responsive visual quality | 5 | | | |
| **Total** | **100** | | **/100** | |

## Findings
For every meaningful finding provide:
- ID
- Dimension
- Impact: High / Medium / Polish
- Location
- Observable evidence
- Why it weakens the design
- Concrete recommendation
- Preserve: what should remain unchanged, if relevant
- Confidence
- Effort: XS / S / M / L / XL

Avoid vague recommendations such as `make it modern`, `improve spacing`, or `use better colors`. Prefer specific relational guidance such as `reduce the visual weight of secondary cards so the primary KPI remains the dominant focal point`.

## Priority plan
- P0 — visually broken or blocks comprehension/action
- P1 — structural hierarchy/layout/typography issues
- P2 — consistency and refinement
- P3 — polish

## Re-review
After changes, use the same rubric, screens, and viewports where possible. Report:
- before score;
- after score;
- dimension deltas;
- fixed findings;
- remaining findings;
- regressions.

---

# Visual Audit guardrails

1. Evidence over taste.
2. Do not redesign merely to follow trends.
3. Preserve established product identity unless it causes a measurable visual problem.
4. Fix hierarchy and layout before decorative polish.
5. Prefer systematic token/component fixes over one-off CSS patches.
6. Do not invent interactions from screenshots.
7. Do not confuse visual minimalism with usability.
8. Do not reward whitespace that lowers useful information density without purpose.
9. Do not punish dense professional tools when density supports expert work.
10. Always identify visual strengths worth preserving.
