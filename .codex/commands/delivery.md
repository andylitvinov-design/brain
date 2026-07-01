# /delivery

Use this file as the Codex project-level delivery workflow reference.

`/delivery` is enough. The user should not have to provide extra approval-mode flags for normal safe implementation work.

## Delivery workflow

When a prompt begins with `/delivery`, execute the rest of the prompt as an implementation task.

Delivery rules:

1. Inspect repository state before editing:
   - `pwd`
   - `git status`
   - `git branch --show-current`
   - `git remote -v`
   - relevant files/docs.
2. Use the linked issue/spec or user prompt as source of truth.
3. Work on a safe branch/worktree when code changes are needed.
4. Make the smallest correct implementation.
5. Run relevant verification.
6. Commit, push, and create/update a PR.
7. Return a concise final report.

## Confirmation policy

Do **not** ask for routine confirmations during delivery.

Proceed without asking for:

- reading files;
- editing normal source/docs/tests;
- installing dependencies already declared by the repo;
- running lint/typecheck/build/tests;
- local browser/Playwright verification;
- creating branches, commits, pushes, and PRs.

Stop and ask only for:

- secrets/env/payment credentials/cookies/passwords;
- destructive data actions or irreversible migrations;
- spending money or changing paid plans;
- production data rewrites/backfills;
- real payment submissions;
- unclear task scope where multiple business outcomes are possible.

Do not ask the user to rerun with special CLI approval flags for routine work. Treat this command file plus `AGENTS.md` as the repository-level authorization for autonomous delivery.
