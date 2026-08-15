---
name: web-ui-ux-evaluator
description: Evaluate web services and web-app UIs using a repeatable evidence-based UX audit combining Nielsen-style heuristic inspection, WCAG 2.2 AA accessibility checks, visual design quality, task success, responsive behavior, and optional SUS/HEART validation. Use for design reviews, UI audits, pre-release checks, redesign prioritization, and before/after comparisons.
---

# Web UI/UX Evaluator

## Purpose

Evaluate a web service systematically rather than by taste. Produce an evidence-backed review that distinguishes:

1. **Observable UI/UX quality** — what can be inspected directly from the interface.
2. **User evidence** — what requires real users, analytics, experiments, or survey data.

Never invent SUS, HEART, conversion, retention, completion-rate, or time-on-task values from appearance alone.

---

## When to use this skill

Use this skill when asked to:

- review or score a website/web app UI/UX;
- compare two interface versions;
- identify usability problems and redesign priorities;
- audit accessibility and responsive behavior;
- create a prioritized UX backlog;
- judge whether a UI is release-ready;
- evaluate a prototype, screenshot set, staging site, or production site.

Do not use it as a substitute for formal legal/accessibility certification or real user research.

---

## Inputs

Accept any of the following:

- URL or running web application;
- screenshots or screen recording;
- Figma/exported mockups;
- HTML/CSS/React implementation;
- product requirements and target-user description;
- analytics, task-success data, SUS responses, or HEART metrics.

If target users or tasks are not supplied, infer only the minimum plausible task context and clearly label it as an assumption.

---

## Evidence modes

Before scoring, declare the evaluation mode.

### Mode A — Live interaction

You can navigate and interact with the product.

May evaluate:
- information architecture;
- navigation;
- forms;
- feedback;
- validation;
- errors;
- keyboard behavior;
- responsive states;
- loading/empty/error states;
- task flow.

### Mode B — Static visual review

You have screenshots/mockups only.

May evaluate:
- visual hierarchy;
- density;
- typography;
- spacing;
- visible affordances;
- visible consistency;
- apparent content clarity;
- some accessibility risks.

Do **not** claim keyboard behavior, focus management, dynamic validation, actual performance, or complete WCAG compliance.

### Mode C — Code-assisted review

You have implementation/code but no full live interaction.

May additionally inspect:
- semantic markup;
- labels;
- ARIA usage;
- responsive CSS;
- component consistency;
- likely focus behavior;
- error handling paths.

### Mode D — User-evidence review

You also have surveys, analytics, or usability-test data.

May calculate or interpret:
- SUS;
- HEART;
- task completion;
- time-on-task;
- error rate;
- conversion/adoption/retention evidence.

---

# Evaluation workflow

## Step 1 — Establish context

Identify:

- target users;
- primary user goal;
- 3–5 critical tasks;
- device context;
- business-critical actions;
- evaluation mode;
- known constraints.

For a general web service, use this default task set only when applicable:

1. Understand what the service does.
2. Find the primary function.
3. Complete the primary action.
4. Recover from a mistake.
5. Find status/history/help or next step.

---

## Step 2 — Test critical task flows first

Do not begin with aesthetics.

For each critical task, inspect:

- discoverability;
- number and clarity of decisions;
- navigation continuity;
- feedback after action;
- error prevention;
- error recovery;
- completion confirmation;
- unnecessary friction.

Record concrete evidence such as page, component, state, label, action, or screenshot location.

---

## Step 3 — Score the observable UI/UX rubric

Score each criterion from **1 to 5**.

### Score anchors

| Score | Meaning | Standard |
|---|---|---|
| 5 | Excellent | Clear, consistent, low-friction, no meaningful issue observed |
| 4 | Good | Minor issue; task remains easy and predictable |
| 3 | Acceptable | Noticeable friction or inconsistency; still usable |
| 2 | Poor | Repeated confusion, effort, or accessibility risk |
| 1 | Critical | Prevents/seriously harms task completion or access |

Do not give a score without at least one concrete observation.

---

# Core rubric — 100 points

## A. Usability & interaction — 25 points

Evaluate using heuristic principles inspired by established usability inspection practice.

1. **System status visibility** — users know what is happening.
2. **Match to user mental model** — language and concepts make sense to users.
3. **User control & freedom** — undo, cancel, back, exit, correction.
4. **Consistency & standards** — patterns behave consistently.
5. **Error prevention** — design prevents predictable mistakes.
6. **Recognition over recall** — required information/actions remain visible.
7. **Flexibility & efficiency** — frequent users are not needlessly slowed.
8. **Minimalism & signal-to-noise** — irrelevant content does not compete with the task.
9. **Error recovery** — errors explain what happened and how to fix it.
10. **Help & guidance** — help appears where needed without becoming a crutch.

Score the section as the weighted average of applicable criteria.

---

## B. Visual hierarchy & UI consistency — 15 points

Evaluate:

- primary CTA prominence;
- information hierarchy;
- grouping/proximity;
- spacing rhythm;
- alignment/grid discipline;
- typography hierarchy;
- component consistency;
- color used with purpose;
- density/readability;
- visual states (selected, disabled, active, warning, success).

Aesthetic preference alone is not evidence of a defect.

---

## C. Task effectiveness & information architecture — 15 points

Evaluate:

- main task discoverability;
- navigation labels;
- page/route structure;
- action sequencing;
- decision complexity;
- form burden;
- completion confirmation;
- next-step clarity;
- findability of important information.

If actual task-test data exists, report it separately under User Evidence rather than replacing the inspection score.

---

## D. Accessibility — 20 points

Use **WCAG 2.2 AA** as the reference target where applicable.

Inspect, as evidence permits:

- text/non-text contrast risks;
- keyboard operability;
- visible focus;
- logical focus order;
- semantic headings/landmarks;
- form labels and instructions;
- error identification;
- accessible names for controls;
- image alternatives;
- link/button purpose;
- content reflow/zoom;
- target size and touch usability;
- information not conveyed by color alone;
- motion/flashing risks;
- status-message accessibility.

When only screenshots are available, label results **visual accessibility review**, not WCAG compliance.

If automated accessibility tools are available, use them as evidence but do not treat automated success as complete WCAG conformance.

---

## E. Responsive & adaptive behavior — 10 points

Where possible test at least:

- mobile: ~360 px width;
- tablet: ~768 px width;
- desktop: ~1440 px width.

Evaluate:

- content reflow;
- clipping/overflow;
- navigation adaptation;
- touch target usability;
- sticky/fixed element collisions;
- table/chart behavior;
- modal/drawer usability;
- keyboard visibility and form layout on mobile;
- preservation of task priority across breakpoints.

---

## F. Content clarity & trust — 10 points

Evaluate:

- labels and microcopy;
- jargon burden;
- CTA specificity;
- error-message clarity;
- destructive-action warnings;
- confirmation clarity;
- important policy/cost/status visibility;
- trust cues proportional to risk;
- absence of deceptive or manipulative patterns.

---

## G. Feedback, states & robustness — 5 points

Evaluate visible/interactive handling of:

- loading;
- empty states;
- success;
- partial failure;
- network/server failure;
- permission/auth failure;
- disabled/unavailable actions;
- retries;
- duplicate submission prevention.

If these states cannot be observed, mark them **Not verified** rather than assuming success.

---

# Score calculation

Each section is scored on a 1–5 scale, converted to its section weight.

Formula:

`section_points = (section_score / 5) × section_weight`

`inspection_score = sum(section_points)`

Round the final score to one decimal place.

### Rating bands

| Score | Rating | Interpretation |
|---|---|---|
| 90–100 | Excellent | Strong release quality; mostly refinement work |
| 80–89.9 | Good | Solid UX with a manageable set of issues |
| 70–79.9 | Fair | Usable but meaningful friction remains |
| 60–69.9 | Weak | Multiple high-impact usability/accessibility issues |
| <60 | Poor | Major redesign/remediation likely required |

A high numeric score never overrides a **Critical** finding.

---

# Finding severity

Assign every issue a severity from 0 to 4.

| Severity | Name | Definition |
|---|---|---|
| S0 | Observation | No usability problem; note/context only |
| S1 | Cosmetic | Polish issue with negligible task impact |
| S2 | Minor | Causes hesitation or extra effort but task remains easy |
| S3 | Major | Frequently causes errors, confusion, abandonment, or access difficulty |
| S4 | Critical | Blocks a critical task, creates severe accessibility exclusion, or risks destructive/unrecoverable action |

Also assign:

- **Confidence:** High / Medium / Low
- **Effort:** XS / S / M / L / XL
- **Area:** usability / visual / IA / accessibility / responsive / content / robustness

Prioritize primarily by severity and user impact, not by implementation effort.

---

# User evidence: SUS, HEART, and task metrics

## SUS — System Usability Scale

Use only when actual responses to the standard 10-item SUS questionnaire are supplied.

Do not infer SUS from screenshots or expert opinion.

Report:

- number of respondents;
- SUS score;
- sample limitations;
- distribution if available;
- comparison between versions only when study conditions are sufficiently comparable.

## HEART

Use HEART as a measurement framework, not an aesthetic checklist:

- Happiness
- Engagement
- Adoption
- Retention
- Task Success

For each relevant dimension define:

`Goal → Signal → Metric`

Example:

`Task Success → users can finish issue registration without assistance → completion rate / median time / error rate`

Never fabricate product analytics.

## Task metrics

When actual usability-test data exists, prefer:

- completion rate;
- failure rate;
- time on task;
- error count/rate;
- abandonment point;
- assistance rate;
- post-task ease rating.

Keep observed expert-inspection scores and real-user metrics clearly separated.

---

# Prioritization model

For each finding calculate an optional priority score:

`Priority = Severity × Reach × Confidence`

Where:

- Severity: 1–4
- Reach: 1–3 (limited / common / broad)
- Confidence: 0.5 / 0.75 / 1.0

Do not let this formula hide S4 findings. S4 issues always appear in the release blockers section.

---

# Required output format

Always produce the following sections unless the user requests a different format.

## 1. Executive summary

- Evaluation mode
- Scope
- Inspection score / 100
- Rating
- Number of S4 / S3 findings
- Top 3 strengths
- Top 3 risks

## 2. Scorecard

| Dimension | Weight | Score (1–5) | Points | Evidence summary |
|---|---:|---:|---:|---|
| Usability & interaction | 25 | | | |
| Visual hierarchy & consistency | 15 | | | |
| Task effectiveness & IA | 15 | | | |
| Accessibility | 20 | | | |
| Responsive behavior | 10 | | | |
| Content clarity & trust | 10 | | | |
| Feedback & robustness | 5 | | | |
| **Total** | **100** | | **/100** | |

## 3. Critical findings

List S4 and S3 first.

For every finding use:

**[ID] Finding title**  
- Severity: S#
- Area:
- Location/state:
- Evidence:
- Why it matters:
- Principle/reference:
- Recommendation:
- Confidence:
- Effort:

## 4. Quick wins

List high-impact S2/S3 items that are XS–S effort.

## 5. Detailed findings

Group remaining findings by dimension.

## 6. Accessibility summary

Separate:

- verified failures;
- likely risks;
- not verified;
- automated-tool findings, if any.

## 7. User-evidence section

If SUS/HEART/task data is supplied, analyze it here.

Otherwise say:

`No real-user/analytics evidence was supplied. SUS and HEART outcome metrics were not scored.`

## 8. Recommended action plan

Prioritize into:

- P0 — release blocker
- P1 — next iteration
- P2 — improvement
- P3 — polish

## 9. Re-test checklist

State exactly what should be verified after changes.

---

# Comparison mode

When comparing A vs B:

1. Use the same task set.
2. Use the same rubric and weights.
3. Evaluate equivalent states/breakpoints.
4. Show score delta by dimension.
5. Identify regressions separately from improvements.
6. Do not claim statistical significance without real study data.

Output:

| Dimension | A | B | Delta | Winner | Reason |
|---|---:|---:|---:|---|---|

Then provide:

- meaningful improvements;
- regressions;
- unchanged critical issues;
- recommendation.

---

# Release gate

Recommend **Do not release** when any of these applies to a critical workflow:

- unresolved S4 issue;
- keyboard-inaccessible critical action;
- destructive action can occur without adequate prevention/recovery;
- primary task cannot be completed reliably;
- severe mobile layout failure blocks primary action;
- authentication/payment/submission state is ambiguous enough to cause duplicate or irreversible action.

Otherwise choose:

- Ready
- Ready with minor fixes
- Conditional release
- Do not release

Explain the gate decision with evidence.

---

# Guardrails

1. **Evidence over taste.** Never downgrade only because a style is unfashionable.
2. **Do not hallucinate interactions.** If a state was not tested, say Not verified.
3. **Do not hallucinate users.** Expert review is not user research.
4. **Do not invent SUS or HEART values.** They require real data.
5. **Accessibility automation is incomplete.** Automated checks supplement manual evaluation.
6. **Context matters.** Internal enterprise tools, consumer apps, dashboards, and public services may need different density and efficiency tradeoffs.
7. **Critical tasks dominate.** A visually attractive interface can still score poorly if its primary task is hard to complete.
8. **Report strengths too.** Preserve working patterns during redesign.
9. **Make recommendations actionable.** Prefer concrete UI changes over vague advice such as “improve UX.”
10. **Separate fact from inference.** Label assumptions and confidence.

---

# Optional tool-assisted checks

If tools are available, use them where appropriate:

- browser automation for task-flow checks;
- axe-core or equivalent for automated accessibility findings;
- Lighthouse for supplemental performance/accessibility signals;
- viewport emulation for responsive review;
- DOM/code inspection for semantics, labels, and states.

Tool output is evidence, not the final judgment.

---

# Reference framework map

| Evaluation need | Primary framework/reference |
|---|---|
| Expert usability inspection | Nielsen-style usability heuristics |
| Accessibility | W3C WCAG 2.2 AA |
| Standardized perceived usability | SUS |
| Product UX outcome measurement | HEART |
| Task effectiveness | Completion/error/time-on-task usability metrics |
| Visual/UI craft | Hierarchy, typography, spacing, consistency, affordance principles |

See `references/RUBRIC.md` for detailed scoring anchors and `references/USER_EVIDENCE.md` for SUS/HEART handling.
