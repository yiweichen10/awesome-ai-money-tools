import json, re
from pathlib import Path

p = Path(r"C:\Users\27040\.accio\accounts\1751848970\agents\DID-F456DA-2B0D4C\project\tweets-queue.json")
data = json.loads(p.read_text(encoding='utf-8'))

fixes = {
    28: "New AI tool alert: Doba Pilot (March 2026)\n\nAn AI dropshipping agent that:\n→ Builds your Shopify store\n→ Picks winning products\n→ Syncs inventory\n→ All via chat\n\nE-commerce on autopilot. Worth watching. #Dropshipping #AI",
    29: "Creators: stop drowning in DMs.\n\nECHO-ME by POP.STORE detects brand deals, engages fans in YOUR voice, and converts followers to revenue 24/7.\n\nYour AI business manager just arrived. #CreatorEconomy #AI",
    30: "MuleRun: your new digital employee.\n\nA self-evolving AI that:\n→ Learns your workflows\n→ Works in its own VM\n→ Buy or sell specialized agents\n\nFreelancers can now hire AI employees. #AIWorkforce #FutureOfWork",
    31: "ASCN No Code: #1 business automation builder in 2026.\n\nMarketplace of ready-made AI agents for:\n→ Lead generation\n→ Sales pipelines\n→ Content creation\n\nNo coding. Just results. #NoCode #AIBusiness"
}

for idx, new_text in fixes.items():
    data[idx]['text'] = new_text

p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# verify
url_re = re.compile(r'https?://|github\.com|systeme\.io|\.com/|\.io/')
bad = [x['text'][:60] for x in data if url_re.search(x.get('text',''))]
print('remaining_with_url:', len(bad))
for b in bad: print(' ', b)
print('done')
