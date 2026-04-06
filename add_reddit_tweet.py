import json
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\tweets-queue.json")
data = json.loads(p.read_text(encoding="utf-8"))

new_tweet = {
    "slot": "morning",
    "source": "reddit",
    "text": "Saw this Reddit question: \"Is anyone actually making money from AI apps?\"\n\nHonest answer: yes, but not from the $5K/month promise posts.\n\nReal income = picking one method + building quietly + iterating.\n\nNo hacks. Just reps. #AI #BuildInPublic"
}

data.append(new_tweet)
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added, total_queue:", len(data))
print("char_count:", len(new_tweet["text"]))
