# Detailed Rubric Anchors

This file makes scoring more repeatable across evaluators.

## A. Usability & interaction — 25

### 5 — Excellent
- Current state and consequences are consistently clear.
- Core actions are easy to discover and predictable.
- Mistakes are prevented where practical and recovery is obvious.
- Users rarely need to remember hidden information between steps.
- Patterns are consistent across equivalent screens.

### 3 — Acceptable
- Core tasks are possible but contain several hesitation points.
- Some labels, states, or flows require interpretation.
- Minor inconsistencies or avoidable steps are present.
- Error recovery exists but may be generic or indirect.

### 1 — Critical
- Primary actions are difficult to locate or understand.
- System state is ambiguous.
- Users can easily make serious mistakes.
- Recovery is absent or unreliable.
- Equivalent components behave inconsistently enough to block learning.

## B. Visual hierarchy & consistency — 15

### 5
- Primary task dominates appropriately.
- Typography, spacing, alignment, grouping, and component states form a coherent system.
- Dense screens remain scannable.

### 3
- Overall hierarchy exists but some areas compete for attention.
- Minor spacing/component inconsistencies reduce scan speed.

### 1
- No reliable visual hierarchy.
- Important and secondary actions look equivalent.
- Alignment, spacing, typography, or state styling makes scanning difficult.

## C. Task effectiveness & IA — 15

### 5
- Users can predict where information/actions live.
- Critical flows are concise and logically ordered.
- Completion and next steps are explicit.

### 3
- Tasks complete successfully but require extra navigation, interpretation, or form effort.

### 1
- Navigation/structure repeatedly misleads users or blocks critical task completion.

## D. Accessibility — 20

### 5
- No meaningful issue observed in the tested scope.
- Critical interactions appear operable by keyboard and assistive technology where verified.
- Visual accessibility checks are strong.

### 3
- Several moderate issues/risks exist but critical tasks remain accessible in tested scope.

### 1
- Critical task is inaccessible or serious WCAG-related barriers are verified.

Never award 5 for full WCAG compliance based on screenshots alone. In static review, 5 means only “strong within visually observable scope.”

## E. Responsive behavior — 10

### 5
- Task priority and readability survive across tested breakpoints.
- No blocking overflow, collision, or target-size issue.

### 3
- Minor reflow/density issues; tasks remain usable.

### 1
- Primary task is blocked or severely degraded on a common viewport.

## F. Content clarity & trust — 10

### 5
- Labels are specific, concise, and user-oriented.
- Risk/cost/destructive consequences are clear before action.
- Errors and confirmations tell users what happened and what to do next.

### 3
- Mostly understandable but includes jargon, generic CTA labels, or weak confirmation language.

### 1
- Wording is misleading, ambiguous, or hides material consequences.

## G. Feedback, states & robustness — 5

### 5
- Loading, success, empty, error, unavailable, and retry states are coherent in tested flows.

### 3
- Main success path is clear but edge states are inconsistent or underdesigned.

### 1
- Users cannot tell whether important actions succeeded, failed, or are still processing.
