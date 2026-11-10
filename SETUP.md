# Setup (Claude follows this with the user)

You are setting up a chief of staff for the person you're talking to (the **owner**). Ask the questions below **one at a time**, in order. Offer the default in brackets; if they say "default", "skip" or just press enter, take it. Don't explain the whole system up front; a one-line "this sets up your chief of staff, about 10 questions" is enough.

When all answers are in, write the files listed under "Write the files", run the checks, and finish with the "Done" message.

If `config.md` already exists, ask whether to change one section or start over, and edit only what they choose.

## The questions

1. **Name.** "What should I call you?" Used in briefs and the launch prompt.

2. **Task management.** "Where should tasks live?"
   - `markdown` [default]: a `TASKS.md` file in this folder. No accounts, nothing to install. Best for trying it out.
   - `linear`: Linear team with labels, a Needs Me status and saved views. Most complete adapter.
   - `github`: GitHub Issues (optionally a Project board) in a repo you choose.
   - `notion`: a Notion database.
   - `todoist`: a Todoist project.

   Then ask only what the chosen adapter's **Setup** section in `adapters/tasks/<name>.md` asks for, and run its setup steps.

3. **Agent management.** "How should I launch the agents that do the work?"
   - `claude-code` [default]: Claude Code subagents and background tasks from this session.
   - `t3-code`: T3 Code threads, one per task.
   - `none`: I only plan and brief; you start each agent yourself with the launch prompt I give you.

   Then ask: "How many agents may run at once?" [5] and "Most opus launches per day?" [2].

4. **Connectors.** "Which of these should I read? Each is optional." Show the list from `adapters/connectors/README.md` (calendar, email, chat, meeting notes, docs) with what each feeds. For each one they pick, check that the connector is actually available in this session (try one read-only call, such as listing today's events). If it isn't, say how to add it (one line) and record it as `wanted, not connected`.

5. **Domains.** "What are the 2-5 areas your work falls into? For each: a name, what's in it, and the folder or repo where its work happens." [one domain: `General`, folder: this folder]. Offer examples only if they're stuck: "Data & reporting", "Internal tools", "Automations", "Research", "Writing".

6. **Models and tokens.**
   - "Which model should I, the chief of staff, run on?" [`opus`]
   - Model ids: write the current ids into `config.md` [haiku `claude-haiku-5-5` · sonnet `claude-sonnet-5-5` · opus `claude-opus-5-5` · fable `claude-fable-5-1`]. Claude Code also accepts the aliases `haiku`, `sonnet`, `opus`; T3 Code needs the full ids. Check `claude --help` or the model docs if these look out of date.
   - "Should I track token use and gate opus launches?" [yes, with `scripts/usage.py`, target opus+fable ≤ 50%]. If they use a team or enterprise plan with its own dashboard, they can say no.

7. **Schedule.** "When should the morning brief run, and on which days?" [weekdays 8:45, their local time zone] and "When should the Friday review run?" [Fridays 15:00]. Ask for their time zone if you can't tell it from the system clock.

8. **House rules.** "Any standing preferences for every agent? For example: no filler copy, numbers on bar charts, ask before deleting anything." Offer the examples in `house-rules/examples/`. Write each one they pick, or one they dictate, to `house-rules/<short-name>.md`. [none]

## Write the files

1. `config.md` from `templates/config.md`, filled in with the answers.
2. One charter per domain: `domains/<kebab-name>.md` from `templates/domain.md`. Put `[placeholder for …]` where you don't have the answer yet; don't invent scope.
3. The task adapter's setup output (for `markdown`: `TASKS.md` from `templates/TASKS.md`; for others: ids written to `config/<adapter>-ids.json`).
4. `state/last-brief.txt` with the current date and time (`YYYY-MM-DD HH:MM`), and `state/days/<today>.md` with the five headings and one Decisions line: `- <owner>: set up the chief of staff (<task adapter>, <agent adapter>).`
5. If they picked a schedule and the agent adapter can schedule (see the adapter), set up the morning brief and Friday review jobs. Otherwise tell them to say "brief me" each morning, or how to schedule it with `cron`/`launchd` calling `claude -p "brief me"` from this folder.

## Checks (run them, don't just describe them)

- `config.md` names files that exist (adapters, domains, house rules).
- Each domain's work folder exists. If one doesn't, say so and offer to create it (an empty folder).
- The task adapter's **Check** section passes (for `markdown`: `TASKS.md` parses; for `linear`: the status and labels exist).
- `python3 scripts/usage.py 1` runs, if they chose usage tracking. Zero tokens is fine on a fresh machine.
- Create one sample task through the adapter, titled `Try the chief of staff: send me a morning brief`, `Who: me`, Todo, so the first brief has something in it.

## Done

Before the summary, tell them once: "Open this folder in Claude Code interactively one time and accept the trust prompt. Until then, `.claude/settings.json` is ignored, and scheduled or headless runs (`claude -p`) can't use its permissions."


Tell them, in at most 6 lines:
- what was set up (task manager, agents, connectors that work),
- three things to try: paste a list of asks ("intake"), "brief me", "go 1",
- where the rules live (`CLAUDE.md`, `RULES.md`, `config.md`) and that they can edit them any time.
