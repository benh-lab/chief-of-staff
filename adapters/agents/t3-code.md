# Agent adapter: T3 Code

Agents are T3 Code threads, one per task. The chief of staff itself runs in a T3 thread in this folder, and launches each agent as a new thread in the domain's T3 project, so the owner can watch, reply to or stop any agent from the T3 sidebar.

## What you need
- T3 Code, with this folder and each domain folder added as T3 projects.
- The T3 tools available in the chief-of-staff thread (`t3_project_list`, `t3_thread_launch`, `t3_thread_list`, `t3_thread_read`, `schedule_task`).

## Setup
1. `t3_project_list` and match each domain's folder to its T3 project id. Write the id into the charter's "Where the work happens" table (`Agent workspace` column).
2. Write `Agent adapter: t3-code` in `config.md`.

## Launch
`t3_thread_launch` with:
- `title`: `<ID> · <short title>`
- `projectId`: from the domain charter
- `modelSelection`: `{"provider": "claudeAgent", "model": "<model id from config.md>"}`
- `interactionMode`: `plan` for opus/fable tasks that change live systems; otherwise default
- `delegatedFrom`: this thread
- `message`: the launch prompt from `CLAUDE.md` section 3

Comment `Agent launched · <model> · <thread link>` on the task.

**Worktrees.** Launching into a git worktree only works when the T3 project's root is the git repo root. If a project points at a subfolder, launch plainly and have the agent make its own branch.

## Check on an agent
Prefer the task's handoff comment. If it's missing, `t3_thread_list` to see whether the thread is still running, then a short `t3_thread_read` of its last messages.

## Concurrency
Count threads launched from this one that are still running (`t3_thread_list`). Stay under the cap in `config.md`.

## Scheduling the brief and Friday review
`schedule_task` from the chief-of-staff thread, with the cron and time zone from `config.md` and the prompt `brief me` (or `run the Friday review`).
