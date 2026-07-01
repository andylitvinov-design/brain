# Brain autonomy setup status

Autonomous delivery entrypoints are configured:

- `AGENTS.md`
- `.codex/commands/delivery.md`
- `.claude/commands/delivery.md`
- `CLAUDE.md`

Expected behavior:

- the user writes `/delivery`;
- the agent treats it as enough authorization for normal safe implementation;
- the agent does not repeatedly ask for confirmation for reading files, editing, tests, browser checks, branches, commits, pushes, or PRs;
- the agent asks only for secrets, destructive data changes, paid/provider actions, real payment submissions, or ambiguous business decisions.

This matches the workflow used in the user's other repositories: `/delivery` is the command; extra CLI approval flags should not be required in the prompt.
