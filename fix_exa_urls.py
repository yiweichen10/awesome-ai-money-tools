import json, re
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\tweets-queue.json")
data = json.loads(p.read_text(encoding='utf-8'))
url_re = re.compile(r'https?://\S+|(?<!\w)([\w-]+\.(com|io|ai|co|net|org)(/\S*)?)', re.IGNORECASE)
fixed = 0
for item in data:
    txt = item.get('text', '')
    cleaned = url_re.sub('', txt).strip()
    # also clean trailing arrows/bullets left dangling
    cleaned = re.sub(r'[\r\n]+', '\n', cleaned)
    cleaned = re.sub(r'\n(→|•|-)\s*\n', '\n', cleaned)
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned).strip()
    if cleaned != txt:
        item['text'] = cleaned
        fixed += 1
        print('FIXED:', cleaned[:100])
p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('fixed_count=' + str(fixed))
