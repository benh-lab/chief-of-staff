# Domain: Ops tools

Task manager: `Domain: Ops tools` in `TASKS.md`
Projects: none yet

## Scope
Internal apps the warehouse team opens every day: the order-tracking app and the returns form. Not in scope: reports (Reporting).

## Where the work happens
| Work | Folder or repo | Agent workspace |
|---|---|---|
| Order-tracking app | `~/code/acme-orders` | - |

## Guardrails
- PRs only; never commit to main. Merging deploys.
- Changes that touch customer records: opus, and Sam reviews the PR.

## Who's who
Warehouse lead (main user of the order-tracking app).
