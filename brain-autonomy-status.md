# Brain autonomy setup status

Autonomous delivery entrypoints added on 2026-07-01:

- `AGENTS.md`
- `.codex/commands/delivery.md`
- `.claude/commands/delivery.md`
- `CLAUDE.md`

These files instruct Codex/Claude delivery agents to proceed autonomously for safe implementation, verification, branch, commit, push, and PR actions, and to ask only for genuinely risky actions such as secrets, destructive data changes, paid provider changes, real payment submissions, or ambiguous business decisions.

If approvals still appear, they are likely coming from the local CLI/tool runtime rather than repository instructions. Launch Codex with the non-interactive approval mode described in `.codex/commands/delivery.md`.
