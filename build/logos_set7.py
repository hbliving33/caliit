"""Set 7 (221-250): masculine, professional colorways on the redwood idea.  Charcoal, pine, slate and gunmetal with forest
greens and a muted brass, strong type pairings, "CONSULTING" tagline, faint state, light redwoods, red dot on the state."""
from logos_set4 import _state, _dot
from logos_set6 import redwood, word

# name, Cali text, IT green (light bg), IT green (dark bg), tagline, panel color
WAYS = [('Charcoal & Forest', '#1f2a2e', '#2f6d4f', '#7fc8a0', '#5d6a66', '#1f2a2e'),
        ('Pine & Brass', '#1c2b24', '#1f5f45', '#6fbf96', '#9a7a35', '#1f3a2e'),
        ('Slate & Moss', '#2b3338', '#4b7a3f', '#9fcf8a', '#5f6b70', '#2b3338'),
        ('Gunmetal & Green', '#2a2f33', '#2e7d50', '#7fdcaa', '#646c70', '#2a2f33'),
        ('Black & Forest', '#141917', '#2f6d4f', '#8fd19e', '#55605b', '#141917')]
PAIRS7 = [
    ('Playfair italic + Bebas Neue', ('Playfair Display', 700, 42, 'italic', 0), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Bodoni italic + Archivo Black', ('Bodoni Moda', 700, 42, 'italic', 0), ('Archivo Black', 400, 36, 'normal', 0)),
    ('DM Serif + Oswald', ('DM Serif Display', 400, 44, 'normal', 0), ('Oswald', 700, 40, 'normal', 1)),
    ('Fraunces + Big Shoulders', ('Fraunces', 700, 42, 'normal', 0), ('Big Shoulders Display', 800, 50, 'normal', 1)),
    ('Kaushan Script + Bebas Neue', ('Kaushan Script', 400, 40, 'normal', 0), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Cinzel + Archivo Black', ('Cinzel', 700, 36, 'normal', 2), ('Archivo Black', 400, 34, 'normal', 0)),
]
def tag(x, y, anchor, col):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Josefin Sans" font-weight="700" font-size="10.5" letter-spacing="5" fill="{col}">CONSULTING</text>'
def logo(treat, pair, way, dark, gid):
    _, cali, it = PAIRS7[pair]
    nm, txc, gl, gd, sub, panel = WAYS[way]
    gr = gd if dark else gl; tx = '#ffffff' if dark else txc; sb = '#aab4ad' if dark else sub
    k = '#1a2230'; fade = .22 if dark else .12; tree = .34 if dark else .26
    sh = gr if not dark else gd
    if treat == 'center':
        x, y, h = 122, 0, 96
        return _state(x, y, h, sh, op=fade) + redwood(x + 10, 44, 44, sh, tree) + redwood(x + 22, 46, 32, sh, tree * .8) + _dot(x, y, h, k) + word(165, 52, 'middle', cali, it, tx, gr) + tag(165, 72, 'middle', sb)
    if treat == 'left':
        x, y, h = 20, 0, 96
        return _state(x, y, h, sh, op=fade) + redwood(x + 12, 44, 44, sh, tree) + _dot(x, y, h, k) + word(42, 52, 'start', cali, it, tx, gr) + tag(46, 72, 'start', sb)
    if treat == 'panel':      # charcoal / pine panel, green IT
        x, y, h = 40, -2, 96
        return (f'<defs><clipPath id="{gid}"><rect x="10" y="6" width="310" height="84" rx="10"/></clipPath></defs><rect x="10" y="6" width="310" height="84" rx="10" fill="{panel}"/>'
                f'<g clip-path="url(#{gid})">{_state(x, y, h, gd, op=.18)}{redwood(x + 12, 42, 42, gd, .3)}{redwood(x + 24, 44, 30, gd, .24)}</g>'
                + _dot(x, y, h, panel) + word(178, 54, 'middle', cali, it, '#ffffff', gd) + tag(178, 74, 'middle', '#b9c4bd'))
    if treat == 'rule':       # left-aligned with a thin green rule between name and tagline
        x, y, h = 20, 0, 96
        return (_state(x, y, h, sh, op=fade) + redwood(x + 12, 44, 44, sh, tree) + redwood(x + 24, 46, 30, sh, tree * .8) + _dot(x, y, h, k)
                + word(42, 50, 'start', cali, it, tx, gr) + f'<rect x="44" y="59" width="60" height="2.5" fill="{gr}"/>' + tag(112, 64, 'start', sb))
    if treat == 'bar':        # name with a solid green bar under the whole lockup
        x, y, h = 122, 0, 96
        return (_state(x, y, h, sh, op=fade) + redwood(x + 14, 46, 46, sh, tree) + _dot(x, y, h, k) + word(165, 50, 'middle', cali, it, tx, gr)
                + f'<rect x="90" y="60" width="150" height="16" fill="{gr}"/><text x="165" y="72" text-anchor="middle" font-family="Josefin Sans" font-weight="700" font-size="10" letter-spacing="5" fill="{"#1a2230" if dark else "#ffffff"}">CONSULTING</text>')
    raise ValueError(treat)
TREATS7 = [('Centered, two redwoods', 'center'), ('Left, one redwood', 'left'), ('Dark panel', 'panel'), ('Left with rule', 'rule'), ('Green bar', 'bar')]
