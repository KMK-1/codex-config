---
name: session-handoff
description: Create and resume structured handoff documents so Codex, Claude Code, and other coding agents can continue work across sessions with minimal ambiguity. Use when the user asks to save state, create a handoff, pause work, transfer work to another agent, resume from a handoff, or continue a previous coding session.
---

# Session Handoff

Cross-agent session continuity for Codex and Claude Code. Inspired by the softaworks session-handoff workflow, adapted to avoid agent-specific storage assumptions.

## Core principle

A handoff is a compact operational state, not a transcript dump. Prefer references to files, commits, issues, PRs, ADRs, and docs over copying information that already exists elsewhere.

## Modes

### CREATE
Use when saving or transferring the current work.

1. Inspect current repository state before writing the handoff:
   - project root
   - current branch
   - `git status`
   - recent relevant commits
   - modified/untracked files
   - tests/checks already run
2. Create a handoff under `.agent-handoffs/` using `references/HANDOFF_TEMPLATE.md`.
3. Capture current state, decisions and rationale, completed work, failed attempts, blockers, critical files, tests, and exact next steps.
4. Never include secrets, tokens, passwords, private keys, cookies, or sensitive `.env` values.
5. Run `scripts/validate_handoff.py <file>` when available.
6. Finalize only when the document is actionable and contains no TODO placeholders.

Recommended filename:
`YYYY-MM-DD-HHMMSS-<task-slug>.md`

For a continuation, add `Continues from:` pointing to the previous handoff.

### RESUME
Use when continuing from an existing handoff.

1. Locate the newest relevant file in `.agent-handoffs/`.
2. Read the newest handoff completely before changing code.
3. If it links to a predecessor, read older handoffs only when the latest document does not contain enough context.
4. Follow `references/RESUME_CHECKLIST.md`.
5. Verify branch, git state, referenced files, assumptions, blockers, and tests against the current repository. The repository is source of truth when it conflicts with the handoff.
6. Start from `Immediate Next Steps` item 1 unless current repository evidence makes it obsolete.
7. Record important new decisions or failed approaches for the next handoff.

## Cross-agent compatibility

This skill is intentionally neutral between Codex and Claude Code.

- Store project handoffs in `.agent-handoffs/`, not an agent-specific directory.
- Use Markdown and repository-relative paths.
- Do not depend on hidden conversation memory.
- Do not assume the next agent has access to the previous transcript.
- State commands and observed results explicitly when they matter.
- If agent-specific instructions exist (`AGENTS.md`, `CLAUDE.md`, etc.), reference them rather than copying them.

## What a good handoff must contain

Prioritize:
1. Goal and current state
2. Important context the next agent cannot safely infer
3. Completed work
4. Decisions made and why
5. Changed/critical files
6. Tests/checks and their results
7. Failed attempts and why they failed
8. Blockers / unresolved questions
9. Immediate next steps with exact first action
10. Handoff chain/reference to predecessor when applicable

## Failed attempts

Record meaningful failed approaches. Include the command/approach, observed failure, likely cause if known, and why it should not be repeated. Do not fill the handoff with trivial mistakes.

## Context compression

Do not paste large code blocks, logs, diffs, or documents if they already exist in the repository. Reference the path/commit/PR and summarize only the implication the next agent needs.

Good:
`src/import/banksalad.ts — ZIP parsing entry point; password is intentionally never persisted.`

Bad:
Copying the entire file into the handoff.

## Git safety

A handoff records state; it does not imply commit, push, merge, reset, stash, or checkout permission. Never mutate git state merely to make a handoff cleaner unless the user separately requested that action.

## Security

Before finalizing:
- remove secrets and credentials;
- do not copy `.env` contents;
- redact sensitive URLs/query parameters;
- prefer variable names such as `SUPABASE_URL` over values;
- mention that a secret exists/configuration is required without recording the secret.

## Validation

Run:
`python scripts/validate_handoff.py <handoff-file>`

The validator checks required headings, unfinished placeholders, likely secrets, and basic handoff quality. Treat secret warnings as blockers. Review false positives manually rather than blindly deleting useful context.

## Output to user

After CREATE, report:
- handoff path;
- validation result;
- one-sentence current-state summary;
- first next action.

After RESUME, report:
- handoff loaded;
- whether current git/repository state matches it;
- stale/conflicting assumptions discovered;
- action being resumed.

## Handoff chaining

For long-running work, create a new handoff instead of endlessly expanding one file. Link it with `Continues from:`. The newest handoff should stand on its own for immediate continuation; older handoffs are historical context, not mandatory reading by default.

## Resources

- `references/HANDOFF_TEMPLATE.md` — handoff document template
- `references/RESUME_CHECKLIST.md` — verification steps before resuming
- `scripts/validate_handoff.py` — lightweight completeness/security validation
