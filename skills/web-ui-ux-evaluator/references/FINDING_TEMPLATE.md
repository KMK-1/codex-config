# Finding Template

## [UX-001] Short issue title

- **Severity:** S3 Major
- **Area:** usability
- **Location/state:** Checkout > payment > submit
- **Evidence:** The primary submit action remains enabled during processing and there is no visible in-progress state.
- **Why it matters:** Users may submit repeatedly because they cannot tell whether the request is processing.
- **Principle/reference:** System status visibility; error prevention
- **Recommendation:** Disable repeat submission while processing, show an inline progress state, and confirm successful completion with a persistent result state.
- **Confidence:** High
- **Effort:** S
- **Reach:** Broad

## Strong recommendation rules

Recommendations should say:

- what component/state to change;
- what behavior/content to introduce;
- what user problem it resolves;
- what to verify after implementation.

Avoid vague wording such as:

- “make it more intuitive”;
- “improve design”;
- “make the UX better”;
- “use better colors.”
