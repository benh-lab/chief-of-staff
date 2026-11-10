# Task adapter: markdown (`TASKS.md`)

Zero dependencies: tasks live in `TASKS.md` in this folder. Good for trying the system and for one person. No web view and no notifications; agents in other folders edit the file by its absolute path.

## Setup
1. Copy `templates/TASKS.md` to `TASKS.md` and fill in the placeholders.
2. In `config.md` under Task management, write `File: TASKS.md`. The chief of staff gives agents the absolute path in their launch prompt, since they run in other folders.

## Check
`TASKS.md` exists, starts with `# Tasks`, has the `Next id` comment, and every `## T-<n> · <title>` block has the six field lines.

## Format

```markdown
## T-12 · Weekly report shows refunds by region
- Status: Todo                    # Backlog | Todo | In Progress | Needs Me | Done | Canceled
- Who: agent                      # me | agent
- Domain: Data
- Model: sonnet                   # haiku | sonnet | opus | fable | -
- Project: Q3 reporting           # or -
- Source: Sam, 2026-03-02, standup
- Labels: found-by-agent          # optional line
- Blocked by: T-9                 # optional line
- Due: 2026-03-10                 # optional line

**Goal:** …
**Done when:** …
**Out of scope:** …
**Context:** …
**Model:** sonnet

### Comments
- 2026-03-02 14:10 · chief of staff: Agent launched · sonnet · <session id>
```

Projects live in `PROJECTS.md` with the same idea: `## <name>`, then `Status`, `Target date`, an acceptance-criteria checklist (`- [ ]`), and `Out of scope`.

## The verbs
| Verb | How |
|---|---|
| Create a task | Read the `Next id` comment, append a block with that id, bump `Next id`. Keep blocks in id order. |
| Find / dedupe | Search titles and Goal lines for the key words; ignore Done and Canceled. |
| Comment | Append `- <YYYY-MM-DD HH:MM> · <who>: <text>` under `### Comments`. Multi-line handoffs: indent the continuation lines by two spaces. |
| Move status | Edit the `Status:` line and add a comment saying why. |
| The owner's queue | Blocks with `Status: Needs Me`, or `Who: me` and not Done/Canceled. |
| Agent board | `Who: agent`, not Done/Canceled, grouped by status. |
| Moved since last brief | Comments dated after `state/last-brief.txt`. |
| Stale | `In Progress` + `Who: agent` whose last comment is 2+ working days old. |
| Cancel | `Status: Canceled` with a comment. Never delete a block. |

## Limits
- Two agents editing `TASKS.md` at the same second can clash. Agents re-read the file right before each edit and change only their own block. If clashes happen often, move to a real task manager.
