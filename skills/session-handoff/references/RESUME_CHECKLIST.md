# Resume Checklist

Use this before continuing implementation from a handoff.

- [ ] Read the newest relevant handoff completely.
- [ ] Confirm project/repository root.
- [ ] Confirm current branch and HEAD.
- [ ] Inspect `git status`; do not overwrite unrelated user changes.
- [ ] Compare changed/critical files with the handoff.
- [ ] Check commits made after the handoff.
- [ ] Verify referenced files still exist.
- [ ] Re-check assumptions that may have become stale.
- [ ] Check whether listed blockers were resolved elsewhere.
- [ ] Review tests/checks that were last run and whether they need rerunning.
- [ ] Read predecessor handoffs only if the latest handoff lacks necessary context.
- [ ] Follow repository-native instructions such as `AGENTS.md` or `CLAUDE.md`.
- [ ] Start with Immediate Next Steps #1 unless current evidence invalidates it.

## Conflict rule

When the handoff conflicts with the current repository, the current repository and explicit current user instruction win. Record the discrepancy instead of silently following stale context.

## Security rule

If a handoff contains a credential or secret, stop using that value, redact it from future handoffs, and tell the user that credential handling needs attention without reproducing the secret.
