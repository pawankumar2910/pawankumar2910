import sys
from PIL import Image, ImageFilter, ImageOps
src, cols = sys.argv[1], int(sys.argv[2])
im = Image.open(src).convert('RGB')
# crop: drop empty red margins a bit
im = im.crop((60, 40, 400, 380))
W, H = im.size
rows = int(cols * H / W / 2.25)
small = im.resize((cols, rows), Image.LANCZOS)
gray = ImageOps.autocontrast(small.convert('L'), cutoff=2)
edges = im.convert('L').filter(ImageFilter.FIND_EDGES).resize((cols, rows), Image.LANCZOS)
ramp = sys.argv[3] if len(sys.argv)>3 else " .,:;i1tfLCG08@"
out = []
for y in range(rows):
    line = ''
    for x in range(cols):
        r, g, b = small.getpixel((x, y))
        if r > 150 and g < 110 and b < 110:   # red background
            line += ' '; continue
        v = gray.getpixel((x, y)) / 255.0
        e = edges.getpixel((x, y)) / 255.0
        v = min(1.0, 0.18 + 0.82 * v + 0.6 * e)   # floor so the black shirt still shows
        line += ramp[min(len(ramp)-1, int(v * (len(ramp)-1)))]
    out.append(line.rstrip())
while out and not out[0].strip(): out.pop(0)
print('\n'.join(out))
