# Config

Written by `SETUP.md`. Edit by hand any time; the chief of staff reads it at the start of every session.

## Owner
- Name: {{name}}
- Time zone: {{tz}}

## Task management
- Adapter: `adapters/tasks/{{task_adapter}}.md`
- {{adapter-specific settings, e.g. "Team: OPS" or "File: TASKS.md"}}

## Agents
- Adapter: `adapters/agents/{{agent_adapter}}.md`
- Max agents at once: {{cap}}
- Max opus launches per day: {{opus_cap}}
- Chief of staff model: {{cos_model}}
- Model ids: haiku `{{haiku_id}}` · sonnet `{{sonnet_id}}` · opus `{{opus_id}}` · fable `{{fable_id}}`

## Connectors
| Connector | Tool | Status | Feeds |
|---|---|---|---|
| Calendar | {{e.g. Google Calendar}} | {{connected / wanted, not connected / off}} | brief: today's meetings |
| Email | | off | |
| Chat | | off | |
| Meeting notes | | off | |
| Docs | | off | |

## Domains
- `domains/{{domain}}.md`

## Tokens
- Usage source: {{`python3 scripts/usage.py 7` / none}}
- Target: opus + fable ≤ {{50}}% of the week; stricter gate at {{75}}%

## Schedule
- Morning brief: {{weekdays 08:45}}
- Friday review: {{Fridays 15:00}}

## House rules
- {{`house-rules/<name>.md`, or "none"}}
