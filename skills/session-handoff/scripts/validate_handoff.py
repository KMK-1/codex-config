#!/usr/bin/env python3
import re
import sys
from pathlib import Path

REQUIRED = [
    "## Goal",
    "## Current State Summary",
    "## Completed Work",
    "## Important Context",
    "## Decisions Made",
    "## Changed / Critical Files",
    "## Tests / Verification",
    "## Failed Attempts",
    "## Blockers / Unresolved Questions",
    "## Pending Work",
    "## Immediate Next Steps",
]

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*[\"']?[^\s\"']{8,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_handoff.py <handoff-file>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: file not found: {path}")
        return 2
    text = path.read_text(encoding="utf-8", errors="replace")
    errors = []
    warnings = []
    for heading in REQUIRED:
        if heading not in text:
            errors.append(f"missing required section: {heading}")
    if re.search(r"<[^>]+>|\[TODO(?::[^\]]*)?\]", text, re.I):
        warnings.append("template/TODO placeholders may remain")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append("possible secret or credential detected; review and redact")
            break
    filled = sum(1 for h in REQUIRED if h in text)
    score = round(100 * filled / len(REQUIRED))
    if "1. " not in text.split("## Immediate Next Steps", 1)[-1]:
        warnings.append("Immediate Next Steps may not contain an ordered first action")
        score = max(0, score - 10)
    print(f"Validation score: {score}/100")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    if errors or score < 70:
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
