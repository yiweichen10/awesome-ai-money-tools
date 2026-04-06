import json
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\tweets-queue.json")
data = json.loads(p.read_text(encoding='utf-8'))

# find first afternoon tweet (the one we published)
target_idx = next((i for i, x in enumerate(data) if x.get('slot') == 'afternoon'), None)
removed = data.pop(target_idx)

# count remaining afternoon tweets
afternoon_count = sum(1 for x in data if x.get('slot') == 'afternoon')

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('removed:', removed['text'][:60].replace('\n', ' '))
print('remaining_afternoon:', afternoon_count)
print('total_queue:', len(data))
