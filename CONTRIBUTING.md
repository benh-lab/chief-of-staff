# Contributing

Issues and pull requests are welcome, especially new adapters.

- **Adapters:** follow `docs/extending.md`. Include the Setup, Check and verbs sections, and test the setup on a fresh account or workspace.
- **Rules and routines** (`CLAUDE.md`, `RULES.md`): open an issue first with the problem it solves. Keep them tool-neutral; tool-specific steps go in an adapter.
- **Style:** short sentences, plain words, tables over prose. No filler. Dates as YYYY-MM-DD.
- **Examples:** invented data only. No real names, companies, emails, ids or URLs.
- **Never commit secrets.** Run `gitleaks detect` before opening a PR.
