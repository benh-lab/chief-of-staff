# Task adapter: Notion

Tasks are pages in one Notion database. Fields are properties; the brief is the page body; comments are page comments.

## What you need
- The Notion MCP connector in Claude Code, with access to the page that holds the database.

## Setup
Ask for the parent page (link or name). Create a database `Tasks` with these properties (or check an existing one has them):

| Property | Type | Options |
|---|---|---|
| Title | title | |
| Status | status or select | Backlog, Todo, In Progress, Needs Me, Done, Canceled |
| Who | select | me, agent |
| Model | select | haiku, sonnet, opus, fable |
| Domain | select | one per domain |
| Project | relation to a `Projects` database, or select | |
| Labels | multi-select | found-by-agent |
| Due | date | |
| Source | text | |

Create two views in the Notion UI (the API can't make views): **My Queue** (Status is Needs Me, or Who is me, and not Done/Canceled) and **Agent Board** (Who is agent, board by Status).

In `config.md` under Task management, write `Database: <name and URL>`.

## Check
Fetch the database and confirm every property and option above exists.

## The verbs
| Verb | How |
|---|---|
| Create a task | Create a page in the database with the properties; the brief goes in the body. |
| Find / dedupe | Search the database by title words, Status not Done/Canceled. |
| Comment | Add a page comment. Long handoffs: a comment plus a `Handoff <date>` toggle block in the body. |
| Move status | Update the Status property and comment why. |
| The owner's queue / agent board | Query the database with the view filters above. |
| Moved since last brief | Query by "Last edited time" after the last-brief time. |
| Cancel | Status Canceled. Never delete or archive the page. |
