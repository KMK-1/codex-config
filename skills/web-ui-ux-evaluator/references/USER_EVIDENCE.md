# User Evidence Guide

## Why this is separate

Expert inspection can identify likely usability problems, but it cannot tell you with certainty how satisfied users are, how fast they complete tasks, or whether they retain/adopt the product.

## SUS

Use the standard 10-item System Usability Scale only with actual participant responses.

For each respondent:

- odd-numbered items: contribution = response - 1
- even-numbered items: contribution = 5 - response
- sum contributions and multiply by 2.5

Result range: 0–100.

Do not interpret 70 as “70% usable.” SUS is a standardized scale, not a percentage.

Always report sample size and study context.

## HEART

HEART dimensions:

- Happiness
- Engagement
- Adoption
- Retention
- Task Success

Convert each relevant dimension into:

### Goal
What user/product outcome matters?

### Signal
What observable behavior or attitude indicates progress?

### Metric
What measurable number represents the signal?

Example:

- Goal: Users can register a quality issue quickly and correctly.
- Signal: Users finish without assistance or repeated correction.
- Metrics: completion rate, median completion time, validation-error rate, assistance rate.

## Suggested usability-test dataset

For each task capture:

- task ID;
- participant ID;
- success: success / partial / fail;
- completion time;
- errors;
- assists/prompts;
- abandonment step;
- post-task ease rating;
- qualitative notes.

## Combining expert and user evidence

Do not silently merge them into one opaque score.

Preferred reporting:

- Inspection Score: 0–100
- SUS: 0–100 (if available)
- Task completion: %
- Median time-on-task
- Key HEART metrics

Then explain whether the sources agree or conflict.
