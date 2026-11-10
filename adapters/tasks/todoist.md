# Task adapter: Todoist

Tasks are Todoist tasks in one project. Status is a section; Who, Model and Domain are labels. Todoist has no long-form body, so the brief goes in the task description (it supports markdown) and handoffs are comments.

## What you need
- A Todoist MCP connector, or the REST API with a token read from your keychain at the moment of use (`Authorization: Bearer $(security find-generic-password -s todoist-api-token -w)` on macOS). Never write the token to a file.

## Setup
Ask for the project name. Create (or check) in that project:
- Sections: `Backlog`, `Todo`, `In Progress`, `Needs Me`. Done is a completed task; Canceled is a completed task with the label `canceled`.
- Labels (personal, shared by all projects): `who-me`, `who-agent`, `haiku`, `sonnet`, `opus`, `fable`, `found-by-agent`, `canceled`, and `domain-<name>` per domain.
- A filter **My Queue**: `#<project> & (/Needs Me | @who-me)`.

In `config.md` under Task management, write `Project: <name>`.

## Check
List the project's sections and the labels; every name above exists.

## The verbs
| Verb | How |
|---|---|
| Create a task | Add a task in the right section, with labels and the brief as description. Projects (outcomes) are parent tasks with the acceptance criteria as sub-tasks. |
| Find / dedupe | Search active tasks in the project by words. |
| Comment | Add a comment on the task. |
| Move status | Move the task to the section, and comment why. |
| The owner's queue | The My Queue filter. |
| Moved since last brief | Comments and completed tasks after the last-brief time. |
| Cancel | Add label `canceled`, comment, complete. Never delete. |
