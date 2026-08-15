# Example UI/UX Evaluation Report

> Demonstration only. Scores below are fictional and are not evidence about a real product.

## 1. Executive summary

- Evaluation mode: Live interaction
- Scope: Sign-in → dashboard → create issue → submit → history
- Inspection score: 71.5 / 100
- Rating: Fair
- Critical findings: S4 0 / S3 3

### Top strengths
1. Main dashboard hierarchy is clear.
2. Form sections are logically grouped.
3. Success confirmation is persistent.

### Top risks
1. Validation appears only after submit.
2. Mobile table overflows and hides primary actions.
3. Keyboard focus is not visible on several controls.

## 2. Scorecard

| Dimension | Weight | Score | Points | Evidence summary |
|---|---:|---:|---:|---|
| Usability & interaction | 25 | 4.0 | 20.0 | Flow is understandable; late validation adds friction |
| Visual hierarchy & consistency | 15 | 4.0 | 12.0 | Strong hierarchy, minor component inconsistency |
| Task effectiveness & IA | 15 | 4.0 | 12.0 | Main task is easy to locate |
| Accessibility | 20 | 2.5 | 10.0 | Focus and contrast issues observed |
| Responsive behavior | 10 | 2.5 | 5.0 | Mobile data table blocks actions |
| Content clarity & trust | 10 | 4.0 | 8.0 | Mostly clear labels |
| Feedback & robustness | 5 | 4.5 | 4.5 | Good success state, some loading ambiguity |
| **Total** | **100** | | **71.5** | |

## 3. Critical findings

### [UX-001] Primary table action becomes unreachable on narrow screens
- Severity: S3 Major
- Area: responsive
- Location/state: Issue list, 360 px viewport
- Evidence: Horizontal overflow places the row action outside the initial viewport with no affordance indicating additional content.
- Why it matters: Mobile users may not discover how to open/edit an issue.
- Principle/reference: Responsive reflow; discoverability
- Recommendation: Replace the wide table with a mobile row/card pattern or pin the primary action within the visible region.
- Confidence: High
- Effort: M

## 7. User-evidence section

No real-user/analytics evidence was supplied. SUS and HEART outcome metrics were not scored.
