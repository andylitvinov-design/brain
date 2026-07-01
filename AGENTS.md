# Brain repo agent rules

## Delivery autopilot

When the user runs `/delivery`, operate in full delivery mode by default.

Do not repeatedly ask for confirmation for safe implementation steps. Proceed autonomously through:

- reading repo instructions and relevant files;
- creating a branch/worktree when needed;
- editing source files and docs;
- running local tests, lint, typecheck, build, and targeted verification;
- using Playwright/browser checks when they are part of the task;
- committing, pushing, and opening/updating a PR;
- reporting the final PR, commit, checks, and remaining blockers.

Ask the user only when the next action is genuinely risky or impossible to infer:

- secrets, tokens, passwords, cookies, payment credentials, or production env values;
- destructive data changes, irreversible migrations, deletes, or backfills;
- production deploys when deploy target or safety is ambiguous;
- spending money or changing paid plan/provider settings;
- changing business/finance semantics without explicit task instruction;
- legal/compliance decisions;
- missing required external account access.

## Tool approval reduction

Prefer non-interactive commands and explicit flags that minimize approval prompts.

For Codex CLI delivery, use the closest available equivalent of:

```bash
codex --ask-for-approval never exec --sandbox workspace-write -c sandbox_workspace_write.network_access=true
```

For Claude Code delivery, use the closest available equivalent of:

```bash
claude --permission-mode bypassPermissions
```

For browser/Playwright verification, avoid pausing for routine navigation, screenshots, DOM inspection, form filling, and local preview checks. Stop only before submitting real external forms, payment actions, destructive admin actions, or credential entry.

## Reporting

Final delivery report should be short and include:

- branch;
- PR link;
- commit SHA;
- changed files summary;
- verification commands/results;
- blockers or manual steps, if any.

Do not expose secrets or private data in logs, PRs, comments, or final reports.
