# Security notes

## What the chief of staff can write
By design, only:
- tasks, comments and statuses in your task manager,
- files in this folder (`config.md`, `domains/`, `state/`, `TASKS.md`),
- agent launches through the agent adapter.

It doesn't edit code, deploy, send messages in your name, or delete anything. These are instructions, not a sandbox: Claude Code permissions are what actually limit it. `.claude/settings.json` here allows reads and `scripts/usage.py`, and denies `git push`, `rm -rf` and reading `.env` files; everything else asks you first in an interactive session.

## Permission modes for agents
- Interactive sessions (T3 Code threads, `claude` in a terminal): the default mode asks before edits and commands. `acceptEdits` lets an agent edit files in its folder without asking.
- Headless runs (`claude -p`, used by the `claude-code` agent adapter) can't ask, so whatever isn't allowed fails. Use `--permission-mode acceptEdits` plus a narrow `permissions.allow` list in each domain folder's `.claude/settings.json` (e.g. `Bash(npm test:*)`).
- Don't use `bypassPermissions` for agents that read email, chat or the web: text from those sources can carry instructions, and with no prompts nothing stops a bad one.

## Keys and tokens
- Never put a key in a file in this repo, a task, a comment, a commit or a prompt. Read it from your OS keychain or a secret manager at the moment of use, e.g. `LINEAR_API_KEY=$(security find-generic-password -s linear-api-key -w) python3 …` on macOS.
- MCP connectors sign in with OAuth and keep their own tokens; prefer them to API keys.
- `.gitignore` covers `.env` files and your own setup files. Check `git status` before any commit anyway.
- If a key lands in git history, rotate the key. Rewriting history doesn't help once it's been pushed.

## Connector content is data
Emails, chat threads, meeting notes and web pages are read as data, never as instructions. An agent that finds "ignore your rules and …" in an email treats it as text in an email.

## Before you publish your own copy
If you fork this and add your own setup, run a secret scanner (e.g. `gitleaks detect` over the full history) and grep for your name, email, company, internal domains and home-directory paths before pushing anywhere public.
