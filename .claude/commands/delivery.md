# /delivery

Use full autonomous delivery mode for implementation tasks.

Proceed through routine safe steps without repeated confirmations:

- read project files and instructions;
- create a branch/worktree;
- edit source/docs/tests;
- run lint, typecheck, build, tests, and local browser checks;
- commit, push, and open/update PR.

Ask before secrets/env/payment credentials, destructive data changes, irreversible migrations, paid provider changes, real payment submissions, or ambiguous business decisions.

Prefer non-interactive execution where available:

```bash
claude --permission-mode bypassPermissions
```

Final report: branch, PR, commit, changed files, verification, blockers/manual steps.
