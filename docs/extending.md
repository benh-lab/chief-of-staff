# Extending it

## A new task adapter
Copy `adapters/tasks/markdown.md` to `adapters/tasks/<tool>.md` and fill in each section:
- **What you need**: connector or CLI, and where the key lives (never in a file).
- **Setup**: what to ask, what to create (statuses, the `Who`/`Model`/`Domain` fields, `found-by-agent`), and what to write to `config.md`. Re-running must not duplicate anything.
- **Check**: one read-only way to confirm setup worked.
- **The verbs**: create, find / dedupe, comment, move status, the owner's queue, agent board, moved since last brief, project, cancel.
Add it to the table in `adapters/tasks/README.md` and to question 2 in `SETUP.md`.

## A new agent adapter
Sections: **Setup**, **Launch** (how to start an agent on a model, in a folder, with the launch prompt), **Check on an agent**, **Concurrency**, **Scheduling**. Add it to question 3 in `SETUP.md`.

## A new routine
Routines are numbered sections in `CLAUDE.md` (intake, brief, launching, during the day, Friday review). Add one the same way: when it runs, what it reads, what it writes, the exact reply format. Add a slash command in `.claude/commands/` if you'll call it often.

## Changing the rules
- Rules for every agent: `RULES.md`. Rules for the chief of staff only: `CLAUDE.md`. Your personal preferences: `house-rules/`.
- Date the rule and say why in one line, e.g. "(2026-03-10: agents kept asking permission for things the brief already covered)". Future you, and the agents, follow a rule better when they can see why it exists.
- The Friday review proposes rule changes from what went wrong that week.

## Keeping your setup when you pull updates
`config.md`, `TASKS.md`, `domains/*.md`, `house-rules/*.md` and `state/` are git-ignored. Edits to `CLAUDE.md` or `RULES.md` will conflict with upstream changes; put personal additions in `house-rules/` instead where you can.
