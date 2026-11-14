import datetime
art = open('art.txt', encoding='utf-8').read().rstrip('\n').split('\n')
AW = max(map(len, art)) + 3
IW = 52
def kv(k, v):
    k = '. ' + k + ': '
    return k + '.' * (IW - len(k) - len(v) - 1) + ' ' + v
def head(t):
    t = '- ' + t + ' '
    return t + '─' * (IW - len(t))
start = datetime.date(2022, 11, 1); today = datetime.date(2026, 11, 15)
y = today.year - start.year; m = today.month - start.month; d = today.day - start.day
if d < 0: m -= 1; d += 30
if m < 0: y -= 1; m += 12
info = [
 'pawankumar2910@github ' + '─' * (IW - 22),
 kv('OS', 'Windows 11'),
 kv('Uptime', f'{y} years, {m} months, {d} days'),
 kv('Host', 'renderedby.pk'),
 kv('Kernel', 'Video editor + dev'),
 '.',
 kv('Craft', 'Edit, Motion, Colour, 3D'),
 kv('Tools', 'AE, Premiere, Resolve, Blender'),
 kv('Languages', 'Rust, TS, JS, Python, SQL'),
 kv('Web', 'HTML, CSS, three.js, Flask'),
 '.',
 head('Contact'),
 kv('Instagram', 'instagram.com/renderedby.pk'),
 kv('Website', 'renderedbypk.vercel.app'),
 kv('Email', 'pavankch29@gmail.com'),
 '.',
 head('Stats'),
 kv('Years in post', '4'),
 kv('Projects delivered', '15+'),
 kv('Brands', '6'),
 kv('Public repos', '8'),
]
n = max(len(art), len(info))
top = (n - len(info)) // 2
info = [''] * top + info + [''] * (n - len(info) - top)
art += [''] * (n - len(art))
lines = [(a.ljust(AW) + ('│ ' + i if i else '│')).rstrip() for a, i in zip(art, info)]
block1 = '\n'.join(lines)
work = '''~/films  (client work, 2026)
├── Norwood Gulf          Campaign   The Art of Diesel · master + square cut + trend reels
├── Orchid                AI launch  Launch film · 16:9 · 01:09
├── SSV Infra             Founder    Founder reel + raw → edited breakdown series
├── AtCozy                Retail     The New Season · store launch film
├── Fit Secrets           Retail     Store film · 9:16
└── Cardinelle            Fashion    Key art + poster series · 11 pieces'''
code = '''~/code  (pinned, best first)
├── Aethelgard            Rust       Double-entry ledger · exact multi-currency maths · Merkle audit proofs
├── CampaignLens          Next.js    Agency reporting: what changed, budget pacing, branded client reports
├── Portfolio             three.js   Scroll walk through a Kyoto house · renderedbypk.vercel.app
├── Resume-Builder        JS         Local-first resume studio · 60 templates · PDF + DOCX export
├── ELORA                 three.js   Client site · one WebGL camera through an agency's departments
└── HDI-Prediction-App    Python     scikit-learn HDI model behind a Flask form'''
readme = f'''```text
{block1}
```

```text
{work}
```

```text
{code}
```
'''
open('README.txt', 'w', encoding='utf-8').write(readme)
print(readme)
