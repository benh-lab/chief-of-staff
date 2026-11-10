# Domain: Reporting

Task manager: `Domain: Reporting` in `TASKS.md`
Projects: Weekly ops report v2

## Scope
Recurring numbers for the leadership team: the weekly ops report, the order-delay chart, ad hoc data pulls. Not in scope: the order-tracking app (Ops tools).

## Where the work happens
| Work | Folder or repo | Agent workspace |
|---|---|---|
| Report scripts and SQL | `~/code/acme-reports` | - |

## Guardrails
- Numbers going to leadership get a `reviewer` check first.
- Read from the reporting database's read-only user; never write to production tables.

## Who's who
Head of ops (asks for the weekly report). Finance analyst (owns the revenue numbers).
