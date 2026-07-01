# /delivery

Run the requested task in autonomous delivery mode.

## Default behavior

- Inspect repository state and instructions first.
- Work on a safe branch/worktree when code changes are needed.
- Make the smallest correct implementation.
- Run relevant verification.
- Commit, push, and create/update a PR.
- Return a concise final report.

## Confirmation policy

Do **not** ask for routine confirmations during delivery.

Proceed without asking for:

- reading files;
- editing normal source/docs/tests;
- installing project dependencies already declared by the repo;
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

## Preferred command mode

Use non-interactive/autopilot execution where available:

```bash
codex --ask-for-approval never exec --sandbox workspace-write -c sandbox_workspace_write.network_access=true
```

If a tool asks for approval for routine safe actions, choose the safe auto-approve/bypass option when available and continue.
