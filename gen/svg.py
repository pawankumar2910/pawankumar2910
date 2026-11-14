# Turns the three text blocks of README.txt into red SVG cards (GitHub can't colour plain code blocks).
import re, sys
from xml.sax.saxutils import escape
RED, DIM, VAL, BG, BORDER = '#ff2b3a', '#7a2a31', '#e6edf3', '#0d1117', '#30363d'
FS, LH, CW, PAD = 14, 19, 8.43, 22
FONT = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
src = open(sys.argv[1], encoding='utf-8').read()
blocks = re.findall(r'```text\n(.*?)\n```', src, re.S)

def segs_info(rest):
    # rest = text right of the art, starting at the │
    out = []
    m = re.match(r'(│ ?)(.*)$', rest)
    if not m: return [(rest, DIM)]
    out.append((m.group(1), DIM)); body = m.group(2)
    kv = re.match(r'(\. )([^:]+)(: )(\.+)( )(.*)$', body)
    hd = re.match(r'(- )(\S.*?)( ─+)$', body)
    tt = re.match(r'(\S+@github)( ─+)$', body)
    if kv: out += [(kv[1], DIM), (kv[2], RED), (kv[3], DIM), (kv[4], DIM), (kv[5], DIM), (kv[6], VAL)]
    elif hd: out += [(hd[1], DIM), (hd[2], RED), (hd[3], DIM)]
    elif tt: out += [(tt[1], RED), (tt[2], DIM)]
    else: out.append((body, DIM))
    return out

def segs_tree(line):
    m = re.match(r'([├└]── )(\S+)(\s+)(\S+)(\s+)(.*)$', line)
    if m: return [(m[1], DIM), (m[2], RED), (m[3], DIM), (m[4], DIM), (m[5], DIM), (m[6], VAL)]
    return [(line, RED)]

def card(lines, segfn, name):
    w = int(max(len(l) for l in lines) * CW + PAD * 2)
    h = len(lines) * LH + PAD * 2 - 4
    rows = []
    for i, l in enumerate(lines):
        spans = ''.join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in segfn(l) if t)
        rows.append(f'<text x="{PAD}" y="{PAD + 13 + i * LH}" xml:space="preserve">{spans}</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
           f'font-family="{FONT}" font-size="{FS}">\n'
           f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8" fill="{BG}" stroke="{BORDER}"/>\n'
           + '\n'.join(rows) + '\n</svg>\n')
    open(name, 'w', encoding='utf-8').write(svg)

art_block = blocks[0].split('\n')
cut = min(l.index('│') for l in art_block if '│' in l)
card(art_block, lambda l: [(l[:cut], RED)] + (segs_info(l[cut:]) if len(l) > cut else []), 'card.svg')
card(blocks[1].split('\n'), segs_tree, 'films.svg')
card(blocks[2].split('\n'), segs_tree, 'code.svg')
print('ok', cut)
