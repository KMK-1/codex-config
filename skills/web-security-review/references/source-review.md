# Source review

Use this checklist selectively according to the application's attack surface. Inspect centralized controls before reporting per-route omissions.

## Architecture and trust boundaries

- Map internet, browser, service, worker, database, cache, file store, queue, identity provider, administrative, and third-party boundaries.
- Identify privileged operations, sensitive business flows, tenant boundaries, and data classification.
- Compare intended behavior with actual enforcement. Existing code proves current facts, not product policy.

## Access control

- Verify authentication and authorization server-side at the trusted service layer.
- Test object ownership and tenant scoping for every read and mutation path.
- Check horizontal, vertical, function-level, property-level, and administrative access controls.
- Deny by default and fail closed when dependencies or policy checks fail.
- Review alternate routes, batch endpoints, background jobs, exports, webhooks, and direct object references.

## Authentication and sessions

- Review enrollment, login, MFA, recovery, credential change, logout, revocation, and re-authentication.
- Check account enumeration, automation controls, session fixation, token rotation, expiry, cookie flags, CSRF, and redirect validation.
- Validate JWT issuer, audience, algorithm policy, time claims, key rotation, and revocation assumptions.
- Do not design custom cryptography or password hashing.

## Input, output, and unsafe operations

- Trace attacker-controlled input into SQL/NoSQL, OS commands, templates, HTML/JS/CSS, headers, redirects, files, XML, deserialization, and dynamic evaluation.
- Prefer typed parsing, allowlists, parameterized APIs, contextual output encoding, and sandboxing.
- Review URL fetching for SSRF, redirects, DNS rebinding, internal ranges, cloud metadata, protocol restrictions, and response limits.
- Check upload type by content, size/count limits, storage location, generated names, malware controls, and authenticated retrieval.

## API and business logic

- Inventory versions, hosts, methods, schemas, deprecated endpoints, debug interfaces, and undocumented paths.
- Enforce limits on pagination, payload size, concurrency, expensive queries, exports, and LLM/tool consumption.
- Review state transitions, replay, duplicate submission, race conditions, idempotency, pricing, quotas, inventory, approvals, and workflow order.
- Treat third-party API responses as untrusted and constrain outbound data.

## Data, secrets, and cryptography

- Keep secrets out of source, images, URLs, logs, prompts, client bundles, and chart values.
- Review secret retrieval identity, least privilege, rotation, expiry, auditability, and failure behavior.
- Use maintained cryptographic libraries, authenticated encryption, secure random generation, and explicit key lifecycle management.
- Minimize sensitive data collection, retention, exposure, caching, and backup copies.

## Configuration and supply chain

- Review debug modes, default credentials, CORS, CSP, HSTS, cache controls, error detail, directory listing, admin exposure, and environment separation.
- Check pinned dependencies, lockfiles, integrity verification, provenance, build scripts, generated artifacts, and known-vulnerability gates.
- Review CI/CD and deployment identities, branch protections, artifact signing, image privileges, container capabilities, network policy, and Kubernetes RBAC.

## Logging and exceptional conditions

- Log authentication, authorization failures, sensitive actions, and unexpected errors with useful context but no secrets.
- Protect logs from injection and unauthorized modification; define alerting and retention.
- Ensure timeouts, partial failures, fallback paths, and exceptions do not bypass security controls or leave inconsistent state.

## Verification

Prefer focused tests that demonstrate the invariant: another tenant receives denial, revoked sessions stop working, unsafe input remains data, and dependency failure denies access. Supplement review with the repository's existing SAST, dependency, secret, type, build, and test commands; tool output is evidence to investigate, not an automatic confirmed finding.

