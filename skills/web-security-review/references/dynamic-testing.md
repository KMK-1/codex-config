# Authorized dynamic testing

Perform dynamic checks only against a target the user owns or is explicitly authorized to test. Establish the environment, hostnames, accounts, time window, source IP restrictions, prohibited techniques, rate limits, data handling, and emergency contact before active testing.

## Safe default sequence

1. Inspect documented routes, roles, APIs, authentication flows, and deployment configuration.
2. Perform passive TLS, certificate, header, cookie, cache, CORS, content, and error-response inspection.
3. Use synthetic low-privilege accounts to exercise ordinary flows.
4. Test authorization with controlled cross-account and cross-role requests that cannot modify real data.
5. Validate input handling with harmless markers and minimal requests. Do not use destructive payloads.
6. Check logout, expiry, revocation, recovery, redirects, CSRF defenses, upload constraints, and rate-limit behavior within the approved limits.
7. Capture minimal reproducible evidence, redact sensitive values, and clean up only test artifacts whose ownership is certain.

## Coverage areas

- Information exposure: public files, source maps, verbose errors, metadata, debug routes, client-side secrets, old assets.
- Transport and browser controls: TLS, certificate validity, HSTS, CSP, framing, MIME sniffing, referrer policy, cookie attributes.
- Identity: enumeration, recovery, MFA, session lifecycle, token handling, account state changes.
- Authorization: object, tenant, property, function, role, and administrative boundaries.
- Input handling: injection classes, redirects, path handling, SSRF, upload validation, parser and serialization boundaries.
- APIs: inventory, schemas, methods, BOLA/BFLA, mass assignment, resource consumption, unsafe third-party consumption.
- Business logic: workflow order, replay, concurrency, quotas, approvals, pricing, inventory, and abuse-resistant sensitive flows.

## Prohibited by default

Do not perform denial-of-service, credential stuffing, broad crawling, high-volume fuzzing, destructive SQL or command execution, malware upload, persistence, privilege retention, lateral movement, real-data extraction, social engineering, or testing outside the named hosts. These require a separate written scope and specialist controls; some should not be performed by this skill at all.

## Evidence quality

A scanner alert is not a confirmed vulnerability. Reproduce safely, identify the affected request and response, account for intermediaries, and demonstrate the boundary crossed without accessing unrelated data. If a test is unsafe or inconclusive, stop and record the exact evidence still required.

