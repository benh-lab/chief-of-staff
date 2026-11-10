#!/bin/sh
# Make a throwaway chief of staff with made-up data, to try "brief me" in 5 minutes.
# Usage: sh scripts/demo.sh [target dir]   (default: a new temp dir)
set -eu
src=$(cd "$(dirname "$0")/.." && pwd)
dst=${1:-$(mktemp -d "${TMPDIR:-/tmp}/cos-demo.XXXXXX")}
if [ -e "$dst/config.md" ]; then echo "$dst already has a config.md; pick an empty folder." >&2; exit 1; fi
mkdir -p "$dst"
for f in CLAUDE.md RULES.md SETUP.md adapters templates scripts house-rules .claude; do cp -R "$src/$f" "$dst/"; done
cp -R "$src/examples/demo/." "$dst/"
echo "Demo ready in $dst"
echo "Next: cd \"$dst\" && claude \"brief me\""
