import json
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\threads-queue.json")
data = json.loads(p.read_text(encoding="utf-8"))

for t in data:
    if t.get("id") == 1:
        t["status"] = "posted"
        break

queued = [t for t in data if t.get("status") == "queued"]
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("marked_posted: thread 1")
print("remaining_queued:", len(queued))
