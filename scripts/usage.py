"""Token use by model, from local Claude Code transcripts.

Usage: python3 scripts/usage.py [days=7] [--root DIR] [--target 50]

Counts input + output + cache-write tokens per model. Cache reads are left out: they are cheap and would swamp the totals.
Reads $CLAUDE_CONFIG_DIR/projects, or ~/.claude/projects. Covers every Claude Code session on this machine
(terminal, IDE, T3 Code, subagents, headless runs); not claude.ai chats or cloud routines.
Exit code 0 always; prints "over target" when the opus + fable share is above --target.
"""
import argparse, collections, datetime as dt, glob, json, os

ap = argparse.ArgumentParser()
ap.add_argument("days", nargs="?", type=int, default=7)
ap.add_argument("--root", default=os.path.join(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude"), "projects"))
ap.add_argument("--target", type=float, default=50, help="opus + fable share target, percent")
a = ap.parse_args()

since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=a.days)).isoformat()
cutoff = (dt.datetime.now() - dt.timedelta(days=a.days + 1)).timestamp()
tot, out, seen = collections.Counter(), collections.Counter(), set()
for f in glob.glob(os.path.join(a.root, "**", "*.jsonl"), recursive=True):
    if os.path.getmtime(f) < cutoff:
        continue
    with open(f, errors="ignore") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            m = d.get("message") if isinstance(d, dict) else None
            if not isinstance(m, dict) or not m.get("usage") or (d.get("timestamp") or "") < since:
                continue
            key = (m.get("id"), d.get("requestId"))
            if key in seen or str(m.get("model", "")).startswith("<"):
                continue
            seen.add(key)
            u = m["usage"]
            name = str(m.get("model", "?")).replace("claude-", "")
            tot[name] += u.get("input_tokens", 0) + u.get("output_tokens", 0) + u.get("cache_creation_input_tokens", 0)
            out[name] += u.get("output_tokens", 0)

total = sum(tot.values())
print(f"Last {a.days} days, local transcripts in {a.root} (input + output + cache writes):")
if not total:
    print("  no usage found")
    raise SystemExit(0)
for name, n in tot.most_common():
    print(f"  {name:18} {n/1e6:7.1f}M  {100*n/total:5.1f}%   (output {out[name]/1e6:.1f}M)")
heavy = 100 * sum(n for k, n in tot.items() if k.startswith(("opus", "fable"))) / total
print(f"  Total {total/1e6:.1f}M · opus + fable {heavy:.0f}% (target <= {a.target:.0f}%)" + ("  over target" if heavy > a.target else ""))
