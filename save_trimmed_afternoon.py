import json
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\tweets-queue.json")
data = json.loads(p.read_text(encoding="utf-8"))

# find first afternoon tweet, replace with trimmed version (do NOT remove — keep for tomorrow)
idx = next((i for i, x in enumerate(data) if x.get("slot") == "afternoon"), None)
old = data[idx]["text"]
data[idx]["text"] = "ChatGPT found me 5 profitable micro-niches:\n\n1. AI headshots for LinkedIn ($20-50)\n2. Pet portrait illustrations ($30-80)\n3. Resume optimization ($40-100)\n4. Social media content packs ($100-500/mo)\n5. AI email sequences ($200-1000/client)\n\nAll doable from your laptop. #AI #SideHustle"

afternoon_count = sum(1 for x in data if x.get("slot") == "afternoon")
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("trimmed tweet saved at index:", idx)
print("remaining_afternoon:", afternoon_count)
print("total_queue:", len(data))
