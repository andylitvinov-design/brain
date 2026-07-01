# /delivery

Use this file as the Claude project-level delivery workflow reference.

`/delivery` is enough. The user should not have to provide extra permission-mode flags for normal safe implementation work.

## Delivery workflow

When a prompt begins with `/delivery`, execute the rest of the prompt as an implementation task.

Proceed through routine safe steps without repeated confirmations:

- read project files and instructions;
- create a branch/worktree;
- edit normal source/docs/tests;
- install dependencies already declared by the repo;
- run lint, typecheck, build, tests, and local browser checks;
- commit, push, and open/update PR.

Ask only for secrets/env/payment credentials, destructive data changes, irreversible migrations, paid provider changes, real payment submissions, or ambiguous business decisions.

Do not ask the user to rerun with special CLI permission flags for routine work. Treat this command file plus `AGENTS.md` as the repository-level authorization for autonomous delivery.

Final report: status, branch, PR, commit, changed files, verification, blockers/manual steps.
