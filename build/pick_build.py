"""pick.html: 275 next to 275 in the 278 colors (Midnight & Steel), with a smaller IT, plus matching light versions."""
import pathlib, re
from logos_set4 import _state, _dot
from logos_set6 import redwood
from logos_set9 import logo as c_logo
ROOT = pathlib.Path(__file__).resolve().parent.parent

import json
SHIFT = json.loads((ROOT / 'build' / 'pick_shift.json').read_text()) if (ROOT / 'build' / 'pick_shift.json').exists() else {}

def lockup(bg, tint, it_col, line_col, it_size, panel=True, gid='p'):
    """Panel: 250 x 100 at (40, 0), center (165, 50).  The state and trees are scaled so the whole state sits inside the
    panel with an even 6-unit margin top and bottom, centered left to right.  The text block is centered by measurement
    (pick_shift.json holds the measured nudge for each version)."""
    x, y, h = 122, 0, 96
    tx = '#ffffff' if panel else '#0f1c2d'
    sub = '#c3ccd4' if panel else '#5b6675'
    op_s, op_t = (.2, .3) if panel else (.1, .2)
    tw = 10 * (10.5 * .62 + 5)
    k = 86 / 96                                   # state height 86 inside a 100-high panel, 7 above and 7 below
    sc = h / 220                                  # state drawn in a 200 x 220 box
    r = round(1.6 / k, 2)                         # small dot: about 1.6 units across the finished logo, well under letter size
    dots = ''.join(f'<circle cx="{x + px * sc:.2f}" cy="{y + py * sc:.2f}" r="{r}" fill="#d93636"/>'
                   for px, py in ((124.5, 191.2),   # Huntington Beach, nearest spot where the whole dot is on land
                                  (14.1, 27.9)))    # Arcata, same rule
    art = (_state(x, y, h, tint, op=op_s) + redwood(x + 15, 38, 30, tint, op_t, wr=.42) + redwood(x + 22, 41, 23, tint, op_t * .8, wr=.42) + dots)
    art = f'<g class="art" transform="translate(165 50) scale({k:.4f}) translate(-165.6 -48)">{art}</g>'
    out = ''
    if panel:
        out += f'<defs><clipPath id="{gid}"><rect x="40" y="0" width="250" height="100" rx="10"/></clipPath></defs><rect x="40" y="0" width="250" height="100" rx="10" fill="{bg}"/>'
    out += art
    m = SHIFT.get(gid, {'name_dx': 0, 'tag_dx': 0, 'half': tw / 2, 'dy': 0})
    nx, tx_, half, dy = 165 + m['name_dx'], 165 + m['tag_dx'], m['half'], m['dy'] + 2   # center the text block on y=50
    gap = 12
    out += f'<g class="txt" data-id="{gid}" transform="translate(0 {dy})">'
    out += (f'<text x="{nx:.2f}" y="52" text-anchor="middle"><tspan font-family="Bodoni Moda" font-weight="700" font-size="42" font-style="italic" fill="{tx}">Cali</tspan>'
            f'<tspan dx="10" font-family="Archivo Black" font-weight="400" font-size="{it_size}" fill="{it_col}">IT</tspan></text>')
    out += (f'<rect x="{165 - half - gap - 30:.2f}" y="67.6" width="30" height="2" fill="{line_col}"/><rect x="{165 + half + gap:.2f}" y="67.6" width="30" height="2" fill="{line_col}"/>'
            f'<text x="{tx_:.2f}" y="72" text-anchor="middle" font-family="Josefin Sans" font-weight="700" font-size="10.5" letter-spacing="5" fill="{sub}">CONSULTING</text>')
    out += '</g>'
    return out

NAVY, STEEL_L, STEEL_D, TINT_D = '#0f1c2d', '#3d6a96', '#8fb3d9', '#8fb3d9'
items = [
    ('275 as it is now (Slate &amp; Silver)', c_logo('panel', 3, 4, 0, False, 'o1'), None),
    ('275 in the 278 colors, IT same size', lockup(NAVY, TINT_D, STEEL_D, STEEL_D, 36, gid='a'), None),
    ('275 in the 278 colors, IT smaller', lockup(NAVY, TINT_D, STEEL_D, STEEL_D, 31, gid='b'), lockup('#ffffff', STEEL_L, STEEL_L, STEEL_L, 31, panel=False, gid='bl')),
    ('275 in the 278 colors, IT smallest', lockup(NAVY, TINT_D, STEEL_D, STEEL_D, 27, gid='c'), lockup('#ffffff', STEEL_L, STEEL_L, STEEL_L, 27, panel=False, gid='cl')),
    ('Smaller IT, white IT with steel lines', lockup(NAVY, TINT_D, '#ffffff', STEEL_D, 31, gid='d'), lockup('#ffffff', STEEL_L, NAVY, STEEL_L, 31, panel=False, gid='dl')),
]
src = (ROOT / 'focus.html').read_text()
head = src[:src.index('<body>')].replace('<title>Cali IT logo focus</title>', '<title>Cali IT pick</title>')
cards = ''
for i, (label, a, b) in enumerate(items, 1):
    lightpart = f'<div class="light"><svg viewBox="0 0 330 100" role="img" aria-label="{label}">{b}</svg></div>' if b else ''
    cards += (f'<figure class="card"><div class="light" style="background:#f7f8fa"><svg viewBox="0 0 330 100" role="img" aria-label="{label}">{a}</svg></div>{lightpart}'
              f'<figcaption><b>P{i}</b> {label}{" · top: header/dark version, bottom: white-background version" if b else ""}</figcaption></figure>')
html = head + '<body><header><h1>Cali IT: 275 in the 278 colors</h1><p>Bodoni italic "Cali" with Archivo Black "IT", lines on both sides of CONSULTING.  Navy panel with steel blue, and smaller IT options.</p></header><main class="grid" style="grid-template-columns:repeat(auto-fill,minmax(520px,1fr))">' + cards + '</main></body></html>'
(ROOT / 'pick.html').write_text(html); print('ok')
