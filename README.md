# Chief of staff for Claude Code

A folder you open in Claude Code that turns it into a chief of staff for your agent work. You tell it what you heard and decided; it writes well-briefed tasks in your task manager, launches agents to do them, keeps every task's status true, and tells you each morning what needs you.

## How it works

- **The chief of staff dispatches and edits; it never builds.** It writes briefs, launches agents, reads their handoffs and keeps the board honest. The work happens in agent sessions in your project folders.
- **One task per outcome, with a brief.** Every task says Goal · Done when · Out of scope · Context · Model, and who does it: `me` (only you can) or `agent`.
- **Agents follow one rules file** (`RULES.md`): start by reading the task, stay in scope, stop with one exact question when they need you, end with a standard handoff comment.
- **Status stays true.** Whoever learns something changed moves the task. Before every brief, the chief of staff reconciles each Needs Me and In Progress task against its latest comment and PR.
- **Needs Me** is a status. An agent that needs your decision moves its task there and stops; your morning brief lists each one with a recommendation.
- **Token gates.** Sonnet by default; opus for planning and review; the top model only with a written reason. When the week's opus share passes a threshold, the proposed slate drops to cheaper models.
- **Nothing is deleted without your OK.** Cancel instead.

```
you ──"here are 11 asks"──▶ chief of staff ──briefs──▶ task manager
                                  │                         ▲
                                  └──launch──▶ agents ──handoffs┘
you ◀──"brief me": Needs Me, today, moved, stale, slate──┘
```

## Try it in 5 minutes (made-up data, nothing to connect)

Needs [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) and Python 3.

```sh
git clone <this repo> chief-of-staff && cd chief-of-staff
sh scripts/demo.sh ~/cos-demo     # copies a made-up company's setup into ~/cos-demo
cd ~/cos-demo && claude "brief me"
```

Then try:
- `/intake the finance analyst wants refunds split by card type, and the warehouse lead wants a dark mode`
- `the answer on T-3 is business days`
- `go 1`

## Set up your own (about 30 minutes)

```sh
git clone <this repo> chief-of-staff && cd chief-of-staff
claude "set me up"
```

It asks eight questions, one at a time (`SETUP.md`):

1. **Task management:** `markdown` (a `TASKS.md` file, the default), `linear`, `github`, `notion` or `todoist`.
2. **Agent management:** `claude-code` (headless runs and subagents), `t3-code` (one thread per task) or `none` (it briefs, you launch). Plus how many agents may run at once.
3. **Connectors:** calendar, email, chat, meeting notes, docs. Each optional; each says what it feeds.
4. **Your domains:** the 2-5 areas your work falls into, and the folder each one's work happens in.
5. **Models and token budget**, **schedule** for the morning brief and Friday review, and optional **house rules**.

Then open the folder in Claude Code interactively once and accept the trust prompt, so `.claude/settings.json` applies to scheduled and headless runs too.

Setup writes `config.md`, a charter per domain in `domains/`, and sets up the task manager. Your own files are git-ignored, so `git pull` brings in updates without conflicts.

## Daily use

| You say | It does |
|---|---|
| A pasted list, meeting notes, a forwarded thread | **Intake**: splits, dedupes, writes briefs, replies with one table |
| "do X" | Files the task and launches the agent at once |
| `brief me` (or on a schedule) | **Morning brief**: Needs Me, your tasks today, moved, stale, proposed slate |
| `go 1 3` | Launches those tasks from the slate |
| "I answered T-3: business days" | Posts it on the task, moves it, resumes the agent |
| `/friday` | **Friday review**: project health, backlog prune, token review, rule changes |

## What's in the folder

```
CLAUDE.md            the chief of staff: intake, brief, launching, status, daily log, Friday review, token gates
RULES.md             what every agent follows: fields, statuses, handoff, keeping status true
SETUP.md             the setup interview
adapters/tasks/      markdown · linear (+ setup script) · github · notion · todoist
adapters/agents/     claude-code · t3-code · none
adapters/connectors/ calendar, email, chat, meeting notes, docs
templates/           config, domain charter, TASKS.md
house-rules/         optional standing preferences (examples/)
scripts/usage.py     token use by model from local Claude Code transcripts
scripts/demo.sh      the 5-minute demo
.claude/             subagents (scout, researcher, reviewer, builder) and slash commands
examples/            intake, brief, handoff, charter, day log; all invented
docs/                adapters, extending, security
```

## Docs
- [docs/adapters.md](docs/adapters.md): choosing and switching task and agent adapters.
- [docs/extending.md](docs/extending.md): new adapters, new routines, changing the rules.
- [docs/security.md](docs/security.md): permission modes, what the chief of staff can write, keys.

## License
MIT: free to use, copy and change, as long as the copyright notice stays. See [LICENSE](LICENSE).
