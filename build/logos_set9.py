"""Set 9 (251-280): centered layouts (like 221, 231, 235) in new colors drawn from the research: deep navy, charcoal,
graphite and slate with brass, bronze or steel accents.  No green.  Trees and state take a quiet tint of the main color."""
from logos_set4 import _state, _dot
from logos_set6 import redwood, word
from logos_set8 import PAIRS8, TAGF

# name, Cali text, IT (light bg), IT (dark bg), state/tree tint (light), tint (dark), tagline, accent line/bar (light), (dark)
WAYS9 = [('Navy & Brass', '#0f1c2d', '#a8844c', '#d1b07a', '#0f1c2d', '#8fa3bf', '#5b6675', '#a8844c', '#d1b07a'),
         ('Charcoal & Brass', '#1e2226', '#97773a', '#c9a75c', '#4a5561', '#9aa5b1', '#5f666d', '#97773a', '#c9a75c'),
         ('Midnight & Steel', '#0f1c2d', '#3d6a96', '#8fb3d9', '#3d6a96', '#8fb3d9', '#5b6675', '#3d6a96', '#8fb3d9'),
         ('Graphite & Bronze', '#23272b', '#8a6038', '#c08d5c', '#3b4147', '#a3a9b0', '#61676d', '#8a6038', '#c08d5c'),
         ('Slate & Silver', '#2b3338', '#5f6e7a', '#c3ccd4', '#4a5561', '#aab4bd', '#66717a', '#5f6e7a', '#c3ccd4'),
         ('Navy & Steel Gray', '#0f1c2d', '#4a5561', '#b7c1cb', '#0f1c2d', '#8fa3bf', '#5b6675', '#a8844c', '#d1b07a')]

def logo(layout, pair, way, tagf, dark, gid):
    _, cali, it = PAIRS8[pair]
    nm, txc, itl, itd, shl, shd, sub, acl, acd = WAYS9[way]
    tx = '#ffffff' if dark else txc; itc = itd if dark else itl; sh = shd if dark else shl
    sb = '#aab4bd' if dark else sub; ac = acd if dark else acl
    f, w, s, ls = TAGF[tagf]
    fade = .2 if dark else .1; tree = .3 if dark else .2
    x, y, h = 122, 0, 96
    base = _state(x, y, h, sh, op=fade) + redwood(x + 10, 44, 44, sh, tree) + redwood(x + 22, 46, 32, sh, tree * .8) + _dot(x, y, h, '#1a2230')
    tag = lambda yy=72, col=sb: f'<text x="165" y="{yy}" text-anchor="middle" font-family="{f}" font-weight="{w}" font-size="{s}" letter-spacing="{ls}" fill="{col}">CONSULTING</text>'
    tw = 10 * (s * .62 + ls)
    nm_ = word(165, 52, 'middle', cali, it, tx, itc)
    if layout == 'plain':
        return base + nm_ + tag()
    if layout == 'both':
        l0, l1 = 165 - tw / 2 - 10, 165 + tw / 2 + 6
        return base + nm_ + f'<rect x="{l0 - 34:.0f}" y="68" width="34" height="2" fill="{ac}"/><rect x="{l1:.0f}" y="68" width="34" height="2" fill="{ac}"/>' + tag()
    if layout == 'long':
        return base + word(165, 50, 'middle', cali, it, tx, itc) + f'<rect x="95" y="58" width="140" height="2" fill="{ac}"/>' + tag(76)
    if layout == 'bar':
        return (base + word(165, 50, 'middle', cali, it, tx, itc) + f'<rect x="90" y="60" width="150" height="16" fill="{ac}"/>'
                + f'<text x="165" y="72" text-anchor="middle" font-family="{f}" font-weight="{w}" font-size="{s}" letter-spacing="{ls}" fill="{"#0f1c2d" if dark else "#ffffff"}">CONSULTING</text>')
    if layout == 'panel':     # centered lockup on a dark panel
        bg = '#0f1c2d' if way in (0, 2, 5) else '#1e2226'
        return (f'<defs><clipPath id="{gid}"><rect x="40" y="4" width="250" height="88" rx="10"/></clipPath></defs><rect x="40" y="4" width="250" height="88" rx="10" fill="{bg}"/>'
                f'<g clip-path="url(#{gid})">{_state(x, y, h, shd, op=.2)}{redwood(x + 10, 44, 44, shd, .3)}{redwood(x + 22, 46, 32, shd, .24)}</g>' + _dot(x, y, h, bg)
                + word(165, 52, 'middle', cali, it, '#ffffff', itd) + f'<rect x="{165 - tw/2 - 44:.0f}" y="68" width="30" height="2" fill="{acd}"/><rect x="{165 + tw/2 + 8:.0f}" y="68" width="30" height="2" fill="{acd}"/>'
                + f'<text x="165" y="72" text-anchor="middle" font-family="{f}" font-weight="{w}" font-size="{s}" letter-spacing="{ls}" fill="#c3ccd4">CONSULTING</text>')
    raise ValueError(layout)
LAYOUTS9 = [('Centered', 'plain'), ('Lines both sides', 'both'), ('Long line under', 'long'), ('Accent bar', 'bar'), ('Dark panel', 'panel')]
