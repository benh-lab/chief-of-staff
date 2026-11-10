# Rules for every agent

The task manager named in `config.md` is the source of truth for what the agents are doing and why. If it isn't in the task manager, it isn't happening. Every agent working a task follows this file. "The owner" is the person named in `config.md`.

## The structure

| Level | What it is | Rule |
|---|---|---|
| Domain | A desk that never ends (for example Data, Ops tools, Research) | Charter in `domains/<domain>.md` |
| Project | A finite outcome | Has acceptance criteria, out of scope and a target date. Closes when every criterion is checked. |
| Task | One agent conversation of work | Brief in the description. Bigger than one session → split it or make it a project. |
| Standalone task (no project) | A one-off under ~3 tasks that needs no acceptance criteria | Still gets a `Domain` when it has one |

### Fields on every task
- **Owner:** always the owner. They're accountable; agents do the work.
- **`Who`**: `me` = only the owner can do it (a conversation, decision, review, send). `agent` = an agent can do it from the brief.
- **`Model`** (agent tasks): `haiku` lookups and small mechanical changes · `sonnet` default · `opus` planning, cross-system design, live customer-data changes, review · `fable` only with a reason written in the brief.
- **`Domain`**: which desk owns it.
- **`found-by-agent`**: real, separate follow-up work an agent discovered. Always Backlog.

How each field is stored (labels, properties, tags, columns) is in the task adapter.

### Statuses
- **Backlog**: captured, brief not ready.
- **Todo**: brief ready; an agent could start.
- **In Progress**: someone is on it (for agents: the session is linked in a comment).
- **Needs Me**: an agent stopped and needs the owner's decision, review or input.
- **Done / Canceled.**

## For an agent working a task

1. **Start.** Read the task (description and comments), its project's acceptance criteria, and `domains/<domain>.md`. If a blocker isn't Done, say so and stop. Move the task to In Progress.
2. **Stay in scope, and fix the small stuff now.** Do what the brief says. A loose end that is small, reversible, inside this task's own folder or domain and follows from its goal: fix it in this session and list it under Done. Only work that is bigger, in another domain, or needs a decision becomes a new task: Backlog, `found-by-agent`, same project and domain, a one-line description of what and why.
3. **Other domains.** Need something another domain owns? Create a task there, mark yours blocked by it, and say so in the handoff. Don't edit their systems.
4. **Stuck on a person or a decision.** Post the exact question as a comment, move the task to **Needs Me**, and stop. Don't guess answers that belong to someone else. A question is only allowed if the answer changes what you do next: if every answer leaves you doing the same thing, or the brief gives a sensible default, pick it, do it, and say what you picked under Done.
5. **Finish.** Post the handoff comment (below). End with the task Done, or with exactly one real blocker posted as a comment and the task in Needs Me. Move to Done when every "Done when" item is met.
6. **Long waits run in the background.** Waiting on CI, a merge or a deploy goes to a background subagent that reports back in one line, so the main session stays free. It never force-merges or bypasses checks.
7. **Where knowledge goes.** Facts about how a system works go in its repo (README, folder `CLAUDE.md`). Plans, decisions and reasons go in the task manager (comments, project description). Nothing important lives only in a chat.

### Keeping status true
The owner unblocks and finishes things in other places (other sessions, code review, chat), and the task doesn't follow. So:
- **Whoever learns something changed moves the task, in that moment.** The owner answers a Needs Me question → move it to In Progress (or Done if that was the last item) and comment what they said. A PR for the task merges, or the owner says "done" or "cancel" → move it and comment.
- **A task is Done when every "Done when" item is met**, even if the agent session already ended.
- **Before every brief (and any "what am I blocked on"), reconcile.** For each Needs Me and In Progress task, check the latest comment and the linked PR. Fix the status first, then report.

### Nothing left open
When something is still open at the end of a session (a gap found on the way, a half-covered case), fix it in the same session. If it isn't worth doing, cancel it and say so in one line. The handoff's `Left` is "nothing" unless only the owner can unblock it, and then it is one exact question under `Needs me`.

### Handoff comment (every session ends with one)

```
**Handoff · <model> · <YYYY-MM-DD>**
Done: <what changed, with links: PR, deploy URL, doc>
Left: nothing
Decisions: <decision, who made it>  (or "none")
Needs me: <exact question>  (or "no")
Follow-ups filed: <task ids>  (or "none")
```

## Quality checks
- **Independent review** (the `reviewer` subagent, on opus) runs when a project closes, and before anything goes to people other than the owner (numbers to leadership, emails, live tools).

## Never
- Delete or archive anything without the owner's OK. Cancel instead, and say so.
- Change tasks that belong to other people beyond a comment.
- Create a project without acceptance criteria.
- Create a new database, service or credential without the owner's explicit OK in the task.
- Write secrets into files, tasks, comments or chat. Read them from the keychain or secret store at the moment of use.
