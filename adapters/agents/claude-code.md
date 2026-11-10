# Agent adapter: Claude Code

Agents are Claude Code sessions. Two ways to launch, pick per task:

| Way | When | Lives after this session ends? |
|---|---|---|
| **Headless run** (`claude -p` in the domain's folder, in the background) | Default. Real work in another folder or repo. | Yes |
| **Subagent** (the Agent tool, `run_in_background: true`) | Quick lookups and checks inside this folder (`scout`, `researcher`, `reviewer`). | No |

## Setup
Ask: "Should headless agents be allowed to edit files without asking?" [yes, `acceptEdits`]. Write the answer to `config.md` under Agents as `Permission mode: <mode>`. Never suggest `bypassPermissions` by default; see `docs/security.md`.

Create `state/runs/` for logs.

## Launch (headless)
From the chief-of-staff folder, for task `<ID>` in domain folder `<folder>`:
```sh
mkdir -p state/runs
(cd "<folder>" && nohup claude -p "<launch prompt>" \
   --model <model id from config.md> \
   --permission-mode <mode from config.md> \
   --add-dir "<abs path to this folder>" \
   > "<abs path>/state/runs/<ID>.log" 2>&1 &) ; echo started
```
`--add-dir` lets the agent read `RULES.md` and the charters here, and edit `TASKS.md` if you use the markdown adapter.

Then comment `Agent launched · <model> · state/runs/<ID>.log` on the task.

The launch prompt is in `CLAUDE.md` section 3. Use absolute paths in it, because the agent runs in another folder.

Headless runs can't ask for permission mid-run. Anything that needs a tool the mode doesn't allow fails; the agent should say so in its handoff. To allow specific commands, add them to the domain folder's `.claude/settings.json` (`permissions.allow`), not a broader mode.

## Check on an agent
- Running? `pgrep -fl "claude -p" | grep <ID>` or look at the log's last lines: `tail -n 20 state/runs/<ID>.log`.
- Done? The handoff comment is on the task. If the process ended with no handoff, read the log's end and post a short handoff yourself, marked `(written by chief of staff from the log)`.

## Concurrency
Count running headless agents with `pgrep -f "claude -p" | wc -l` before launching. Stay under the cap in `config.md`.

## Scheduling the brief and Friday review
Claude Code has no scheduler of its own; use the OS. Open this folder interactively once first and accept the trust prompt, or headless runs ignore `.claude/settings.json`.
- macOS/Linux `cron`: `45 8 * * 1-5 cd <abs path to this folder> && mkdir -p state/briefs && claude -p "brief me" --model <id> > state/briefs/$(date +\%F).md 2>&1`
- macOS `launchd` works the same way and survives sleep better.
- Or a cloud routine, if your plan has them.

A scheduled brief writes to `state/briefs/`. If a chat connector is on, the brief ends by posting itself to the owner there.
