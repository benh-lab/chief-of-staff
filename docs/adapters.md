# Adapters

The chief of staff's routines (`CLAUDE.md`) and the agents' rules (`RULES.md`) are written in tool-neutral verbs: "create a task", "move it to Needs Me", "launch an agent". Adapters translate those verbs for one tool. `config.md` names one task adapter, one agent adapter, and any connectors.

## Choosing a task adapter
| If you… | Use |
|---|---|
| want to try it today with nothing to set up | `markdown` |
| already use Linear, or want saved views and a mobile app | `linear` |
| live in GitHub and want tasks next to code | `github` |
| run your life in Notion | `notion` |
| want a personal to-do app | `todoist` |

`linear` is the reference adapter: this template comes from a setup that ran on it, and it's the only one with a setup script (`adapters/tasks/linear/setup_linear.py`, dry run by default).

## Choosing an agent adapter
| If you… | Use |
|---|---|
| use Claude Code in a terminal | `claude-code` (headless `claude -p` runs in the background) |
| use T3 Code | `t3-code` (one thread per task, visible in the sidebar) |
| want to launch every agent yourself, or aren't allowed to automate it | `none` |

## Switching later
1. Run setup again (`/setup`) and pick the section to change; it re-runs only that adapter's setup.
2. Move open tasks across by hand or ask the chief of staff to ("copy every open task from TASKS.md into Linear, keeping ids in the title"). Closed tasks can stay where they are.
3. Update `config.md`. The routines don't change.

## Linear: steps that are easy to miss
- The personal API key is only for the one-time setup script. Day to day, the chief of staff and agents use the Linear MCP connector, which signs in as you.
- Labels are created in your team, not the workspace. If your workspace already has workspace-level labels named `Who` or `Model`, rename one side first, or Linear will show two.
- Linear's "Needs Me" status is a "started" type, so Linear counts those issues as in progress in cycle and project stats.
- Saved views are created as shared in the team. Make them personal in the Linear UI if the team is shared with others.
- Create an **Agent brief** issue template by hand if you want one in the Linear UI (Settings → Team → Templates) with the five brief headings. The chief of staff writes the brief itself, so it's optional.
- Projects: the chief of staff proposes them and creates one only after your yes. Put the acceptance criteria as a checklist in the project description.
