# AGENTS.md

## Working Agreements

- Inspect the relevant files before changing code.
- State important assumptions when the request is ambiguous.
- If multiple reasonable interpretations exist, ask before making a broad change.
- Keep changes minimal and directly tied to the user's request.
- Do not refactor unrelated code or reformat untouched areas.
- Match the existing style, naming, architecture, and tooling of the project.
- Prefer simple, local solutions over speculative abstractions.
- Add abstractions only when they remove real duplication or match an existing pattern.
- Do not add new production dependencies without a clear reason.
- Preserve user changes and never revert unrelated work.

## Source of Truth

- Prefer repository evidence over pretrained knowledge.
- Before using framework or library APIs, inspect the project's pinned version and relevant local documentation.
- When local version-matched documentation exists, treat it as authoritative and retrieve only the files relevant to the task.
- If local documentation conflicts with existing code or configuration, identify the conflict instead of silently choosing one.

## Dryforge

- Do not invoke Dryforge automatically for ordinary coding requests.
- Use Dryforge only when the user explicitly requests `ready`, `go`, or `migration`.
- Reserve Dryforge for consequential work such as risky multi-step features, security or data-state changes, project setup, migrations, and existing-project onboarding.
- Handle small, fully specified, mechanical changes through the normal workflow unless the user explicitly asks for Dryforge.

## Verification

- For broad or ambiguous work, define the expected behavior before implementing.
- Prefer executable checks over manual inspection when correctness matters.
- Make verification deterministic: the same inputs should produce the same pass/fail result.
- Treat tests, types, linters, coverage, and other quality gates as contracts that constrain the implementation.
- When a quality gate is unavailable or flaky, call that out instead of treating the result as proven.
- Run the smallest relevant check after making changes.
- For JavaScript or TypeScript changes, prefer the repository's existing package manager and test scripts.
- For Python changes, prefer the repository's existing test, lint, or type-check command.
- If a check cannot be run, explain why and name the next best verification.
- When a command fails, summarize the key failure and continue with the safest useful next step.

## Design

- Let the desired behavior and constraints drive the implementation shape.
- Keep modules deep where practical: expose a small interface over meaningful behavior.
- Prefer reducing complexity through structure over adding comments or tests around confusing code.
- Avoid hiding important decisions in implementation details; surface them in the plan, spec, tests, or docs when they affect future work.
- If a method, function, or component needs many branches, consider whether the design should be split before adding more logic.

## Git

- Prefer non-interactive Git commands.
- Do not run destructive Git commands such as `git reset --hard` or `git checkout --` unless explicitly requested.
- Do not create commits, branches, tags, or pull requests unless asked.
- Before committing or summarizing changes, check the working tree status.

## Communication

- Lead with the result, then give only the details needed to verify it.
- Keep updates concise while working.
- Mention files changed and checks run in the final response.
- If blocked, explain the blocker clearly and suggest the smallest next action.
