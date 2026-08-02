# Standards baseline

Use local, version-matched requirements when a project provides them. Otherwise use these official baselines and record the version in findings.

## Primary references

- [OWASP Top 10:2025](https://owasp.org/Top10/) — awareness and risk-category baseline; not a complete verification standard.
- [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) — testable application security requirements. Cite IDs as `v5.0.0-x.y.z`.
- [OWASP WSTG 4.2](https://owasp.org/www-project-web-security-testing-guide/v42/) — stable web testing scenarios. Use versioned links rather than mutable `latest` links.
- [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) — API-specific awareness baseline; supplements rather than replaces ASVS and WSTG.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — implementation guidance; verify applicability to the project's pinned stack.

## Coverage model

Prioritize broken access control, security misconfiguration, supply-chain failures, cryptographic failures, injection, insecure design, authentication failures, integrity failures, security logging and alerting, and exceptional-condition handling.

For APIs, explicitly cover object-level and function-level authorization, property-level authorization, resource consumption, sensitive business-flow abuse, SSRF, inventory, misconfiguration, and unsafe consumption of third-party APIs.

Top Ten lists prioritize awareness; they do not prove complete coverage. Use ASVS requirements to define assurance and WSTG scenarios to design authorized runtime checks. Do not claim ASVS compliance unless the selected level, every applicable requirement, evidence, exceptions, and review boundary are documented.

