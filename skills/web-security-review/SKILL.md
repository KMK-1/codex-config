---
name: web-security-review
description: Review web applications and APIs for exploitable security vulnerabilities using current OWASP guidance. Use when the user explicitly asks for a security review, OWASP review, authentication or authorization audit, pre-deployment security validation, API security assessment, or an authorized dynamic web security test. Covers source review and non-destructive testing of user-owned or explicitly authorized targets; does not replace specialist penetration testing.
---

# Web Security Review

Review observable attack paths, not isolated suspicious patterns. Keep requirements, current code, runtime behavior, and completion evidence distinct.

## Select the review mode

- For source code, diffs, configuration, or architecture, perform a source review. Read [references/source-review.md](references/source-review.md).
- For a running application, require an explicitly identified user-owned or authorized target. Read [references/dynamic-testing.md](references/dynamic-testing.md).
- For release readiness, combine both modes when artifacts and authorization are available.
- For the standards baseline and coverage map, read [references/standards.md](references/standards.md).

Do not mutate code, configuration, accounts, data, or infrastructure unless the user separately asks for remediation. A request to review authorizes read-only inspection, not fixes.

## Establish scope

1. Identify the application, review boundary, environment, and requested depth.
2. Inspect repository instructions, pinned versions, authentication middleware, trust boundaries, sensitive data, privileged actions, external integrations, and existing security checks.
3. State material coverage limitations. Do not imply full-application assurance from a partial diff or unavailable runtime.
4. For dynamic testing, verify authorization and allowed techniques before sending test traffic. Default to passive and non-destructive checks.

## Validate every finding

Confirm all of the following before reporting an exploitable vulnerability:

1. **Source:** Identify attacker-controlled input or capability.
2. **Path:** Trace how it reaches the relevant operation across validation and middleware.
3. **Sink or control failure:** Identify the unsafe operation, missing control, or violated invariant.
4. **Reachability:** Account for framework protections, centralized authorization, allowlists, encoding, parameterization, and deployment controls.
5. **Impact:** Explain the trust boundary crossed and realistic blast radius.
6. **Evidence:** Cite exact code locations, safe reproduction evidence, or observable behavior.

If reachability or impact cannot be established, label the item `Needs validation` or `Defense in depth`; do not present it as confirmed.

## Prioritize

Assign severity from demonstrated exploitability and impact, not category name alone:

- `Critical`: likely compromise of a major trust boundary with severe organization-wide impact.
- `High`: practical unauthorized access, code execution, sensitive-data exposure, or equivalent material impact.
- `Medium`: exploitable weakness with meaningful constraints or limited impact.
- `Low`: limited security impact or hardening with a concrete abuse case.

Use `Needs validation` when evidence is insufficient. Do not invent CVSS scores without enough metric evidence.

## Report

Lead with confirmed findings ordered by severity. For each finding include:

```text
[Severity] Short title
Location: file:line, endpoint, or component
Path: attacker-controlled source -> missing/failed control -> sink
Impact: realistic result and affected boundary
Evidence: inspected code or safe observation
Remediation: smallest effective control and where to enforce it
Verification: deterministic check that should fail before the fix and pass after it
Standard: versioned OWASP reference when confidently mapped
```

Then list coverage, checks performed, limitations, and residual risk. If no confirmed findings exist, say so without claiming the application is secure.

Before filling the `Standard` field, read [references/standards.md](references/standards.md) and verify the current version and mapping from the referenced official source. Prefer repository-provided version-matched requirements when present. Never cite a category or requirement ID from model memory; omit the field when the mapping is uncertain.

## Preserve testing safety

- Never test third-party or ambiguous targets without explicit authorization.
- Do not perform denial-of-service, brute force, destructive injection, persistence, malware upload, data exfiltration, or lateral movement by default.
- Use synthetic accounts and data. Minimize requests and stop on unexpected state changes.
- Do not expose secrets, tokens, personal data, exploit payloads, or sensitive responses in logs or reports.
- Prefer a staging environment. Treat production testing as a separate, explicitly approved scope.
