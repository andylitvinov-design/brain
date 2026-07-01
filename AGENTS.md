# Brain repo agent rules

## Delivery workflow

The user may write `/delivery` in prompts. Treat `/delivery` as the complete project workflow marker, not as a shell command that needs extra flags from the user.

When a prompt begins with `/delivery`, execute the rest of the prompt as an implementation task in autonomous delivery mode.

Delivery rules:

1. Inspect repository state before editing:
   - `pwd`
   - `git status`
   - `git branch --show-current`
   - `git remote -v`
   - relevant files/docs.
2. Work on a safe branch/worktree when code changes are needed.
3. Make the smallest correct implementation.
4. Run available verification: lint, typecheck, build, tests, and targeted browser checks when relevant.
5. Commit, push, and create/update a PR when code changes are complete.
6. Final report must include status, branch, PR, commit, verification, and blockers/manual steps.

## Confirmation policy

Do **not** repeatedly ask the user to confirm routine safe delivery steps.

Proceed autonomously through:

- reading repository instructions and relevant files;
- creating a branch/worktree;
- editing normal source/docs/tests;
- installing dependencies already declared by the repo;
- running lint/typecheck/build/tests;
- local browser/Playwright verification;
- committing, pushing, and opening/updating a PR.

Ask only when the next action is genuinely risky or impossible to infer:

- secrets, tokens, passwords, cookies, payment credentials, or production env values;
- destructive data changes, irreversible migrations, deletes, or backfills;
- production deploys when deploy target or safety is ambiguous;
- spending money or changing paid plan/provider settings;
- changing business/finance semantics without explicit task instruction;
- real payment submissions;
- legal/compliance decisions;
- missing required external account access.

## Important

Do not tell the user to rerun Codex/Claude with special approval flags as part of normal delivery. The repository-level `/delivery` rules above are the intended source of truth, as in the user's other repositories.

Do not expose secrets or private data in logs, PRs, comments, or final reports.
