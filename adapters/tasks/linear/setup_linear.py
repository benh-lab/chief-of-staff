"""Set up a Linear team for the chief of staff: Needs Me status, Who/Model/Domain labels, saved views.

Usage:
  LINEAR_API_KEY=... python3 setup_linear.py --team OPS --domains "Data,Ops tools"           # dry run
  LINEAR_API_KEY=... python3 setup_linear.py --team OPS --domains "Data,Ops tools" --live    # create
  LINEAR_API_KEY=... python3 setup_linear.py --team OPS --check                              # report

Safe to re-run: existing statuses, labels and views (matched by name) are reused, never duplicated.
Writes config/linear-ids.json (ids only, no secrets). Reads the key from the environment only.
"""
import argparse, json, os, sys, urllib.error, urllib.request

NEEDS = "Needs Me"
GROUPS = {
    "Who": [("me", "#eb5757", "Only the owner can do it: a conversation, decision, review or send."),
            ("agent", "#4cb782", "An agent can carry it out from the brief.")],
    "Model": [("haiku", "#bec2c8", "Lookups, extraction, small mechanical changes."),
              ("sonnet", "#4ea7fc", "Default: carrying out a clear brief."),
              ("opus", "#9b51e0", "Planning, cross-system design, live customer-data changes, review."),
              ("fable", "#f2994a", "Only with a reason written in the brief.")],
}
FOUND = ("found-by-agent", "#f2c94c", "Follow-up an agent discovered mid-task. Lands in Backlog.")


def gql(query, variables=None):
    key = os.environ.get("LINEAR_API_KEY")
    if not key:
        sys.exit("Set LINEAR_API_KEY for this command (read it from your keychain; see adapters/tasks/linear.md).")
    req = urllib.request.Request("https://api.linear.app/graphql",
                                 data=json.dumps({"query": query, "variables": variables or {}}).encode(),
                                 headers={"Authorization": key, "Content-Type": "application/json"})
    try:
        d = json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        d = json.loads(e.read())
    if "errors" in d:
        sys.exit(json.dumps(d["errors"], indent=1))
    return d["data"]


def load(team_key):
    teams = gql('{teams(first:250){nodes{id key name}}}')["teams"]["nodes"]
    team = next((t for t in teams if t["key"].lower() == team_key.lower()), None)
    if not team:
        sys.exit(f"No team with key {team_key}. Teams you can see: {', '.join(t['key'] for t in teams)}")
    t = gql('query($id:String!){team(id:$id){states{nodes{id name type position}} '
            'labels(first:250){nodes{id name isGroup parent{id}}}}}', {"id": team["id"]})["team"]
    views = gql('{customViews(first:250){nodes{id name slugId team{id}}}}')["customViews"]["nodes"]
    views = [v for v in views if (v.get("team") or {}).get("id") == team["id"]]
    return team, t["states"]["nodes"], t["labels"]["nodes"], views


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--team", required=True, help="Linear team key, e.g. OPS")
    ap.add_argument("--domains", default="", help="Comma-separated domain names")
    ap.add_argument("--live", action="store_true", help="Create what's missing (default: dry run)")
    ap.add_argument("--check", action="store_true", help="Only report ok / missing")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "linear-ids.json"))
    a = ap.parse_args()
    domains = [d.strip() for d in a.domains.split(",") if d.strip()]
    team, states, labels, views = load(a.team)
    ids = {"team": {"id": team["id"], "key": team["key"]}, "states": {}, "labels": {}, "views": {}}
    plan = []

    def act(desc, fn):
        if a.check:
            print(f"missing  {desc}")
        elif a.live:
            print(f"create   {desc}")
            return fn()
        else:
            plan.append(desc)
            print(f"would create  {desc}")

    # Status
    for s in states:
        ids["states"][s["name"]] = s["id"]
    if NEEDS in ids["states"]:
        print(f"ok       status {NEEDS}")
    else:
        started = [s for s in states if s["type"] == "started"]
        pos = max((s["position"] for s in started), default=0) + 0.5
        r = act(f"status {NEEDS}", lambda: gql(
            'mutation($i:WorkflowStateCreateInput!){workflowStateCreate(input:$i){workflowState{id}}}',
            {"i": {"teamId": team["id"], "name": NEEDS, "type": "started", "color": "#eb5757", "position": pos,
                   "description": "An agent stopped and needs the owner's decision, review or input."}}))
        if r:
            ids["states"][NEEDS] = r["workflowStateCreate"]["workflowState"]["id"]

    # Labels
    by_name = {}
    for l in labels:
        by_name[(l["name"], (l.get("parent") or {}).get("id"))] = l["id"]

    def label(name, color, desc=None, parent=None, group=False):
        found = by_name.get((name, parent))
        if found:
            print(f"ok       label {name}")
            ids["labels"][name] = found
            return found
        i = {"teamId": team["id"], "name": name, "color": color}
        if desc: i["description"] = desc
        if parent: i["parentId"] = parent
        if group: i["isGroup"] = True
        r = act(f"label {name}" + (" (group)" if group else ""), lambda: gql(
            'mutation($i:IssueLabelCreateInput!){issueLabelCreate(input:$i){issueLabel{id}}}', {"i": i}))
        if r:
            ids["labels"][name] = r["issueLabelCreate"]["issueLabel"]["id"]
            return ids["labels"][name]
        return f"<{name}>"

    groups = dict(GROUPS)
    groups["Domain"] = [(d, "#26b5ce", None) for d in domains]
    for g, children in groups.items():
        gid = label(g, "#5e6ad2", f"{g}. Single select.", group=True)
        for name, color, desc in children:
            label(name, color, desc, parent=None if gid.startswith("<") else gid)
    label(*FOUND)

    # Views
    open_ = {"state": {"type": {"nin": ["completed", "canceled", "duplicate"]}}}
    lab = lambda n: {"labels": {"id": {"eq": ids["labels"].get(n, f"<{n}>")}}}
    wanted = [
        ("My Queue", "Inbox", {"and": [open_, {"or": [{"state": {"name": {"eq": NEEDS}}}, lab("me")]}]}),
        ("Agent Board", "Robot", {"and": [open_, lab("agent")]}),
        (NEEDS, "Flag", {"state": {"name": {"eq": NEEDS}}}),
    ]
    have = {v["name"]: v for v in views}
    for name, icon, f in wanted:
        if name in have:
            print(f"ok       view {name}")
            ids["views"][name] = {"id": have[name]["id"], "slugId": have[name]["slugId"]}
            continue
        r = act(f"view {name}", lambda: gql(
            'mutation($i:CustomViewCreateInput!){customViewCreate(input:$i){customView{id slugId}}}',
            {"i": {"name": name, "icon": icon, "teamId": team["id"], "shared": True, "filterData": f}}))
        if r:
            ids["views"][name] = r["customViewCreate"]["customView"]

    if a.check:
        return
    if not a.live:
        print(f"\nDry run: {len(plan)} thing(s) to create. Re-run with --live to create them.")
        return
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump(ids, open(a.out, "w"), indent=1)
    print(f"\nWrote {os.path.abspath(a.out)}")


if __name__ == "__main__":
    main()
