---
name: shortform-visual-polisher
description: Polish the visual effects and motion treatment of an already-finished short-form video while preserving locked content such as captions, narration, story, scene order, and duration. Optimized for 30–120s contest videos, enterprise AI demos, and product promos.
---

# Shortform Visual Polisher

## Purpose
Improve the perceived production quality of an existing short-form video **without rewriting the finished content**. Default direction: `Clean / Minimal / Premium / Modern Enterprise Tech`.

## LOCK contract
Unless explicitly unlocked, preserve:
- total duration and timeline;
- story/message and scene order;
- narration/voiceover and spoken wording;
- caption wording and caption timing;
- factual claims;
- core screenshots/demo content;
- brand identity.

Never silently trim/reorder scenes, rewrite captions, replace narration, or alter claims. If a locked element causes a problem, report it as a constraint.

## Editable visual layer
May improve transitions, fade/slide/wipe/subtle scale, push-in/pull-out, pan/crop/reframing, UI spotlight/focus, cursor emphasis, click ripple, masks/reveals, background blur/dim, overlays, restrained gradients, shadow/depth, subtle glow, KPI emphasis, before/after treatment, motion graphics, callouts, processing visualization, and visual rhythm. SFX are editable only when audio changes are explicitly allowed.

## Non-negotiable rule
**Every effect must Explain, Focus, or Transition. Otherwise remove it.**

Use `Remove before add`: before adding glow, particles, cards, borders, icons, or extra motion, first ask whether visual noise can be removed.

## Visual language
Prefer restrained motion, strong alignment, consistent spacing, one focal point per beat, subtle depth, controlled contrast, meaningful motion, readable product UI, and a consistent transition grammar.

Avoid gratuitous neon, AI brains/robots/circuit clichés, constant glow, lens flares, random particles, aggressive glitches, spin/bounce/shake, excessive zoom, a different transition for every scene, or effects that obscure captions/UI.

# Workflow

## 1. Inspect before editing
Analyze the entire source video first. Record duration, aspect ratio/resolution, frame rate if available, semantic scene boundaries, caption safe zones, narration/BGM/SFX presence, UI/demo regions, established visual style, strongest moments to preserve, and visually weak/static intervals.

## 2. Build a semantic timeline
Divide by meaning, not arbitrary equal intervals. For each beat capture: `time | purpose | current visual | weakness | treatment`.

## 3. Tag each effect
Every proposed treatment must be tagged `EXPLAIN`, `FOCUS`, or `TRANSITION`. Reject effects with no tag.

## 4. Motion hierarchy
Prioritize motion in this order:
1. core message/result;
2. product behavior;
3. supporting evidence;
4. decoration.

Decoration must never compete with 1–3.

## 5. Transition system
Use at most 2–3 transition families by default. Prefer fade/crossfade for continuity, directional slide/wipe for progression, subtle scale/push for emphasis, and hard cuts when pace benefits. A transition is not required between every scene.

## 6. UI/demo treatment
When software UI is visible: enlarge the relevant region, dim/blur nonessential regions rather than covering them, preserve legibility, use cursor/click emphasis sparingly, show cause → Agent action → result, avoid unreadably small full-desktop views, preserve product context when cropping, and never fabricate product behavior.

## 7. Before/After
Use consistent framing where possible. Reduce visual weight for Before, create a clear transformation point, restore emphasis for After, and emphasize existing KPIs/results only when present in the source. Never invent metrics.

## 8. Caption protection
Captions are locked content. Never cover them. Respect safe zones, avoid high-detail motion behind text, preserve contrast, and do not continuously pull the focal point away while reading is required. If caption styling is separately unlocked, styling may change but wording/timing remain locked unless explicitly unlocked too.

## 9. Quality gate
Review at normal speed and muted. For every semantic beat ask:
1. Is the focal point obvious within about one second?
2. Does each effect Explain, Focus, or Transition?
3. Does motion compete with captions/narration?
4. Is the motion language consistent?
5. Is the product/demo easier to understand?
6. Is the scene cleaner after the change?
7. Would removing an effect improve it?

Remove effects that fail.

# Enterprise AI contest mode
For internal AI/work-improvement contest videos, visually prove:
`Work arrives → Agent recognizes it → Agent organizes/acts → Agent tracks state → Human sees the result`.

Useful treatments include distributed sources converging into one work state, task extraction, priority sorting, owner/deadline/status appearing sequentially, unresolved work remaining active over time, follow-up/escalation paths, and before/after reduction in visual complexity.

Avoid generic AI spectacle. The viewer should remember **what work the Agent does**.

# 90-second guidance
Do not change the locked timeline to force this structure; use it only to judge effect density:
- 0–5s: Hook — one strong focal treatment, minimal decoration.
- 5–20s: Problem — controlled complexity and guided attention.
- 20–55s: Agent/demo — highest density of explanatory focus effects.
- 55–75s: Outcome — reduce noise, emphasize result/before-after.
- 75–90s: Closing — simplify and finish with a strong visual identity/message.

# Output contract
Before implementation, unless direct implementation is explicitly requested, return:

## A. Preservation contract
What is locked and what is editable.

## B. Visual diagnosis
Strongest qualities to preserve, top weaknesses, and intervals needing attention.

## C. Timeline treatment plan
| Time | Current issue | Proposed treatment | Tag | Priority |
|---|---|---|---|---|

## D. Global motion system
Specify transition families, zoom limits, highlight behavior, UI-focus behavior, depth/overlay rules, and effect-density ceiling.

## E. Restraint pass
List effects intentionally rejected because they add noise or obscure meaning.

# Implementation guidance
If the project uses Remotion, prefer frame-deterministic animation and reusable motion primitives. Preserve source timing exactly. If using FFmpeg or another renderer, build a non-destructive overlay/effects pipeline where possible. Capture representative frames after changes and compare them with the source before final render.

When a companion visual/UI evaluator exists, use it for static visual hierarchy/readability; use this skill for temporal motion/effect treatment.
