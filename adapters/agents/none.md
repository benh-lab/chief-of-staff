# Agent adapter: none

The chief of staff plans, briefs and keeps status; the owner starts every agent by hand. Good for a first week, or where launching agents automatically isn't allowed.

## Launch
Instead of launching, reply with the launch prompt from `CLAUDE.md` section 3, filled in with absolute paths, in a code block, plus the command to start it:

```sh
cd "<domain folder>" && claude --model <model id> --add-dir "<abs path to this folder>"
```

`--add-dir` lets the agent read `RULES.md` and the charters, and update `TASKS.md` if you use the markdown adapter. Then comment on the task in the adapter's usual format, e.g. for markdown `- <YYYY-MM-DD HH:MM> · chief of staff: Ready to launch · <model>`. Leave the status at Todo; the agent moves it to In Progress when it starts.

## Check on an agent
Only through the task: handoff comments and status.

## Concurrency
Not enforced. Mention in the brief if more than the cap in `config.md` are In Progress.

## Scheduling the brief and Friday review
The owner says "brief me" each morning, or schedules it with the OS as in `claude-code.md`.
