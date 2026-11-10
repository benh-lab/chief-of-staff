# Task adapters

The chief of staff talks about tasks with a few verbs. Each adapter says how to do those verbs in one tool. `config.md` names exactly one.

| Adapter | Needs | Best for |
|---|---|---|
| [markdown](markdown.md) | nothing | trying it out; one person; offline |
| [linear](linear.md) | Linear MCP + a personal API key for setup | the most complete setup; the reference adapter |
| [github](github.md) | `gh` CLI | people who live in GitHub |
| [notion](notion.md) | Notion MCP | people who live in Notion |
| [todoist](todoist.md) | Todoist MCP or API token | a personal task app |

Every adapter must cover: **Setup**, **Check**, and these verbs: create a task, find / dedupe, comment, move status, the owner's queue, agent board, moved since last brief, project, cancel. To write a new one, see `docs/extending.md`.
