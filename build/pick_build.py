"""pick.html: 275 next to 275 in the 278 colors (Midnight & Steel), with a smaller IT, plus matching light versions."""
import pathlib, re
from logos_set4 import _state, _dot
from logos_set6 import redwood
from logos_set9 import logo as c_logo
ROOT = pathlib.Path(__file__).resolve().parent.parent

def lockup(bg, tint, it_col, line_col, it_size, panel=True, gid='p'):
    x, y, h = 122, 0, 96
    tx = '#ffffff' if panel else '#0f1c2d'
    sub = '#c3ccd4' if panel else '#5b6675'
    op_s, op_t = (.2, .3) if panel else (.1, .2)
    tw = 10 * (10.5 * .62 + 5)
    out = ''
    if panel:
        out += f'<defs><clipPath id="{gid}"><rect x="40" y="4" width="250" height="88" rx="10"/></clipPath></defs><rect x="40" y="4" width="250" height="88" rx="10" fill="{bg}"/><g clip-path="url(#{gid})">'
    out += _state(x, y, h, tint, op=op_s) + redwood(x + 10, 44, 44, tint, op_t) + redwood(x + 22, 46, 32, tint, op_t * .8)
    if panel: out += '</g>'
    out += _dot(x, y, h, bg)
    out += (f'<text x="165" y="52" text-anchor="middle"><tspan font-family="Bodoni Moda" font-weight="700" font-size="42" font-style="italic" fill="{tx}">Cali</tspan>'
            f'<tspan dx="10" font-family="Archivo Black" font-weight="400" font-size="{it_size}" fill="{it_col}">IT</tspan></text>')
    out += (f'<rect x="{165 - tw/2 - 44:.0f}" y="68" width="30" height="2" fill="{line_col}"/><rect x="{165 + tw/2 + 8:.0f}" y="68" width="30" height="2" fill="{line_col}"/>'
            f'<text x="165" y="72" text-anchor="middle" font-family="Josefin Sans" font-weight="700" font-size="10.5" letter-spacing="5" fill="{sub}">CONSULTING</text>')
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
    lightpart = f'<div class="light"><svg viewBox="0 0 330 96" role="img" aria-label="{label}">{b}</svg></div>' if b else ''
    cards += (f'<figure class="card"><div class="light" style="background:#f7f8fa"><svg viewBox="0 0 330 96" role="img" aria-label="{label}">{a}</svg></div>{lightpart}'
              f'<figcaption><b>P{i}</b> {label}{" · top: header/dark version, bottom: white-background version" if b else ""}</figcaption></figure>')
html = head + '<body><header><h1>Cali IT: 275 in the 278 colors</h1><p>Bodoni italic "Cali" with Archivo Black "IT", lines on both sides of CONSULTING.  Navy panel with steel blue, and smaller IT options.</p></header><main class="grid" style="grid-template-columns:repeat(auto-fill,minmax(520px,1fr))">' + cards + '</main></body></html>'
(ROOT / 'pick.html').write_text(html); print('ok')
