# Task adapter: GitHub Issues

Tasks are issues in one repo (a private repo just for this works well). Fields are labels; Needs Me is a label because issues only have open/closed. Optional: a GitHub Project board for a view by status.

## What you need
- The `gh` CLI, logged in (`gh auth status`). No key in files: `gh` keeps its own token in the OS keychain.
- A repo, e.g. `you/tasks`.

## Setup
Ask for the repo (`owner/name`) and whether they want a Project board.

Create the labels (re-running is safe; `--force` updates existing ones):
```sh
R=owner/name
for l in "status: backlog" "status: todo" "status: in progress" "status: needs me" \
         "who: me" "who: agent" "model: haiku" "model: sonnet" "model: opus" "model: fable" "found-by-agent"; do
  gh label create "$l" -R $R --force
done
# one per domain
gh label create "domain: data" -R $R --force
```
Done and Canceled are closed issues (`gh issue close --reason completed` / `--reason "not planned"`).

In `config.md` under Task management, write `Repo: owner/name`.

## Check
`gh label list -R owner/name` shows every label above.

## The verbs
| Verb | How |
|---|---|
| Create a task | `gh issue create -R $R -t "<title>" -F brief.md -a @me -l "who: agent,model: sonnet,domain: data,status: todo"` |
| Find / dedupe | `gh issue list -R $R --search "<words> in:title,body" --state open` |
| Comment | `gh issue comment <n> -R $R -F handoff.md` |
| Move status | `gh issue edit <n> -R $R --remove-label "status: todo" --add-label "status: needs me"` |
| The owner's queue | `gh issue list -R $R --label "status: needs me"` plus `--label "who: me"` |
| Agent board | `gh issue list -R $R --label "who: agent" --json number,title,labels,updatedAt` |
| Moved since last brief | `gh issue list -R $R --state all --search "updated:>=<date>"` |
| Project (outcome) | A milestone (`gh api repos/$R/milestones -f title=… -f description=…`) with the acceptance criteria as a checklist in the description. |
| Cancel | `gh issue close <n> -R $R --reason "not planned"` with a comment. |

Write briefs and handoffs to a temp file and pass `-F`, so quoting doesn't break markdown.
