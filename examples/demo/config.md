# Config

Demo data: Sam runs operations at Acme Widgets, a made-up company.

## Owner
- Name: Sam
- Time zone: America/New_York

## Task management
- Adapter: `adapters/tasks/markdown.md`
- File: `TASKS.md` (in this folder)

## Agents
- Adapter: `adapters/agents/none.md`
- Max agents at once: 3
- Max opus launches per day: 1
- Chief of staff model: opus
- Model ids: haiku `claude-haiku-5-5` · sonnet `claude-sonnet-5-5` · opus `claude-opus-5-5` · fable `claude-fable-5-1`

## Connectors
| Connector | Tool | Status | Feeds |
|---|---|---|---|
| Calendar | - | off | |
| Email | - | off | |
| Chat | - | off | |
| Meeting notes | - | off | |
| Docs | - | off | |

## Domains
- `domains/reporting.md`
- `domains/ops-tools.md`

## Tokens
- Usage source: none
- Target: opus + fable ≤ 50% of the week; stricter gate at 75%

## Schedule
- Morning brief: on demand
- Friday review: on demand

## House rules
- none
