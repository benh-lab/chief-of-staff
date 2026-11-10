# Task adapter: Linear

The reference adapter: the setup this template was generalized from runs on it. Tasks are Linear issues in one team; the fields are label groups; Needs Me is a workflow status; three saved views give the owner's queue.

## What you need
- A Linear team for this work (a personal team works well; the owner is the assignee of every issue).
- The Linear MCP connector in Claude Code (for the chief of staff and agents), **and** a personal API key for the one-time setup script. Create the key in Linear → Settings → Security & access → Personal API keys.
- Store the key in your OS keychain or a secret manager, never in a file in this repo. The script reads it from `LINEAR_API_KEY` at run time, so you can pass it inline:
  - macOS: `security add-generic-password -s linear-api-key -a "$USER" -w` (prompts for the key), then `LINEAR_API_KEY=$(security find-generic-password -s linear-api-key -w) python3 …`
  - Linux with `pass`: `LINEAR_API_KEY=$(pass show linear-api-key) python3 …`

## Setup
Ask the owner for: the team key (e.g. `OPS`), their domain names (from setup question 5).

1. Dry run, which prints what it would create and changes nothing:
   `python3 adapters/tasks/linear/setup_linear.py --team OPS --domains "Data,Ops tools"`
2. Show the owner the plan. On their OK, run it again with `--live`. It is safe to re-run: anything that already exists (matched by name) is reused, not duplicated.
3. It writes `config/linear-ids.json` (team, status, label, view and template ids; no secrets).
4. In `config.md` under Task management, write `Team: <key>` and `Ids: config/linear-ids.json`.
5. Connect the Linear MCP in Claude Code if it isn't already (`claude mcp add` or your connector settings), and check that `list_issues` for the team works.

What it creates in the team:

| Thing | Name | Notes |
|---|---|---|
| Workflow status | `Needs Me` | type "started", placed after In Progress |
| Label group `Who` | `me`, `agent` | single-select |
| Label group `Model` | `haiku`, `sonnet`, `opus`, `fable` | single-select |
| Label group `Domain` | one per domain | single-select |
| Label | `found-by-agent` | |
| Saved views | `My Queue` (Needs Me or `Who: me`, open), `Agent Board` (`Who: agent`, open), `Needs Me` | shared in the team |

**Already have open issues in the team?** After the script, ask the chief of staff to triage them: it lists every open issue with a proposed `Who`, `Model`, `Domain`, project and status in one table, and applies them only after your OK (with `addLabels`, so existing labels stay). Issues it can't brief go to Backlog with the question at the top.

**Optional: an initiative per domain.** Linear initiatives make a good home for each domain's projects (`<you> · <domain>`). Create them in the UI, then put the initiative name at the top of each charter in `domains/`.

The team's own statuses (Backlog, Todo, In Progress, Done, Canceled) are used as they are. The script doesn't touch them. If your team renamed them, list the names in `config.md` under Task management so the chief of staff uses yours.

## Check
`python3 adapters/tasks/linear/setup_linear.py --team OPS --check` (with `LINEAR_API_KEY` set) lists each expected status, label and view as `ok` or `missing`.

## The verbs (Linear MCP tools)
| Verb | How |
|---|---|
| Create a task | `save_issue` with `team`, `title`, `description` (the brief), `assignee: "me"`, `labels` (Who, Model, Domain), `state`, optional `project`. |
| Find / dedupe | `list_issues` with `team` and `query`. |
| Comment | `save_comment` with `issueId`. |
| Move status | `save_issue` with `id` and `state` (e.g. `Needs Me`). |
| Change a label | `save_issue` with `addLabels` / `removeLabels` (not `labels`, which replaces the whole set). |
| The owner's queue | `list_issues` with `customView: "My Queue"`. |
| Agent board | `list_issues` with `customView: "Agent Board"`. |
| Moved since last brief | `list_issues` with `team` and `updatedAt` set to the last-brief time; then `list_comments` on each for handoffs. |
| Project | `save_project` with acceptance criteria in the description (only after the owner's yes). |
| Cancel | `save_issue` with `state: "Canceled"`. Never archive or delete. |

## Notes
- The template's description sections match the brief in `CLAUDE.md`. If you change one, change the other.
- Linear rate-limits personal keys; the setup script makes about 20 calls.
- `config/linear-ids.json` holds ids only and is fine to commit in a private copy; it is git-ignored here so a fork doesn't publish them.
