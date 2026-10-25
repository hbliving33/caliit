"""Focus page: 221 (centered, two redwoods, Charcoal & Forest) with the thin line beside CONSULTING, in more font pairings."""
from logos_set4 import _state, _dot
from logos_set6 import redwood, word

TX, GL, GD, SUB, BRASS = '#1f2a2e', '#2f6d4f', '#7fc8a0', '#5d6a66', '#9a7a35'
PAIRS8 = [
    ('Playfair italic + Bebas Neue', ('Playfair Display', 700, 42, 'italic', 0), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Playfair italic + Oswald', ('Playfair Display', 700, 42, 'italic', 0), ('Oswald', 700, 40, 'normal', 1)),
    ('Bodoni italic + Bebas Neue', ('Bodoni Moda', 700, 42, 'italic', 0), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Bodoni italic + Archivo Black', ('Bodoni Moda', 700, 42, 'italic', 0), ('Archivo Black', 400, 36, 'normal', 0)),
    ('DM Serif + Oswald', ('DM Serif Display', 400, 44, 'normal', 0), ('Oswald', 700, 40, 'normal', 1)),
    ('Fraunces italic + Big Shoulders', ('Fraunces', 700, 42, 'italic', 0), ('Big Shoulders Display', 800, 50, 'normal', 1)),
    ('Instrument Serif + Archivo Black', ('Instrument Serif', 400, 50, 'italic', 0), ('Archivo Black', 400, 36, 'normal', 0)),
    ('Kaushan Script + Big Shoulders', ('Kaushan Script', 400, 40, 'normal', 0), ('Big Shoulders Display', 800, 50, 'normal', 1)),
    ('Cinzel + Bebas Neue', ('Cinzel', 700, 36, 'normal', 2), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Playfair + Montserrat', ('Playfair Display', 700, 42, 'normal', 0), ('Montserrat', 800, 38, 'normal', 1)),
]
TAGF = [('Josefin Sans', 700, 10.5, 5), ('Montserrat', 600, 9.5, 5), ('Oswald', 500, 11, 5)]

def logo(pair, rule, tagf, rule_col, dark):
    _, cali, it = PAIRS8[pair]
    gr = GD if dark else GL; tx = '#ffffff' if dark else TX; sb = '#aab4ad' if dark else SUB
    rc = {'green': gr, 'brass': BRASS if not dark else '#c9a75c', 'gray': sb}[rule_col]
    f, w, s, ls = TAGF[tagf]
    fade = .22 if dark else .12; tree = .34 if dark else .26
    x, y, h = 122, 0, 96
    base = _state(x, y, h, gr, op=fade) + redwood(x + 10, 44, 44, gr, tree) + redwood(x + 22, 46, 32, gr, tree * .8) + _dot(x, y, h, '#1a2230')
    t = lambda tx_, anchor='middle': f'<text x="{tx_}" y="72" text-anchor="{anchor}" font-family="{f}" font-weight="{w}" font-size="{s}" letter-spacing="{ls}" fill="{sb}">CONSULTING</text>'
    tw = 10 * (s * .62 + ls)                       # rough tagline width
    if rule == 'both':        # line — CONSULTING — line
        l0, l1 = 165 - tw / 2 - 10, 165 + tw / 2 + 6
        return base + word(165, 52, 'middle', cali, it, tx, gr) + f'<rect x="{l0 - 34:.0f}" y="68" width="34" height="2" fill="{rc}"/><rect x="{l1:.0f}" y="68" width="34" height="2" fill="{rc}"/>' + t(165)
    if rule == 'lead':        # short line, then CONSULTING, centered as one group (like 224)
        start = 165 - (40 + tw) / 2
        return base + word(165, 52, 'middle', cali, it, tx, gr) + f'<rect x="{start:.0f}" y="68" width="30" height="2.5" fill="{rc}"/>' + t(start + 40, 'start')
    if rule == 'long':        # long line under the whole name, CONSULTING beneath it
        return base + word(165, 50, 'middle', cali, it, tx, gr) + f'<rect x="95" y="58" width="140" height="2" fill="{rc}"/>' + f'<text x="165" y="76" text-anchor="middle" font-family="{f}" font-weight="{w}" font-size="{s}" letter-spacing="{ls}" fill="{sb}">CONSULTING</text>'
    raise ValueError(rule)
RULES = [('Line on both sides', 'both'), ('Line before', 'lead'), ('Long line under the name', 'long')]
