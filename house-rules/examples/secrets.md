# Secrets

API keys live in the OS keychain (or a secret manager for hosted apps). Never write a key into a file, task, prompt, commit or chat. Read it inline at the moment of use, e.g. `$(security find-generic-password -s <service> -w)` on macOS.

Keep a list of keychain service names (not values) in a private note so agents know where to look.

Why: agent transcripts and task comments are copied to more places than you think.
