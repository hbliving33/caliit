"""Set 6 (191-220): Redwood & Sage, built on 131.  Faint California behind the name, one or two very light redwoods
over the north coast (redwood country), the small red Huntington Beach dot, "Cali" and "IT" in different type styles,
and the tagline simply "CONSULTING" so the logo isn't locked to one kind of work."""
from logos_set4 import _state, _dot, _dots_state

TEXT_DARK, TEXT_LIGHT = '#243028', '#ffffff'
GREENS = [('Forest', '#2f6d4f', '#7fc8a0'), ('Redwood green', '#3a7d44', '#8fd19e'), ('Fresh green', '#2e8b57', '#7fdcaa'), ('Deep pine', '#1f5f45', '#6fbf96')]
SUB_LIGHT, SUB_DARK = '#5f6f66', '#a9b8ae'

def redwood(x, base, h, col, op):
    """A slim redwood: straight trunk, narrow spire with short tiers of branches.  (x, base) = foot of the trunk."""
    w = h * .23
    tiers = 7
    pts = [(0, -h)]
    for i in range(1, tiers + 1):            # right side, tiers stepping out
        y = -h + (h * .82) * i / tiers
        half = w / 2 * (.35 + .65 * i / tiers)
        pts += [(half, y), (half * .55, y - h * .015)]
    left = [(-px, py) for px, py in reversed(pts[1:])]
    poly = ' '.join(f'{x + px:.1f},{base + py:.1f}' for px, py in pts + left)
    trunk = f'<rect x="{x - w * .06:.1f}" y="{base - h * .2:.1f}" width="{w * .12:.1f}" height="{h * .2:.1f}" fill="{col}"/>'
    return f'<g opacity="{op}"><polygon points="{poly}" fill="{col}"/>{trunk}</g>'

def word(x, y, anchor, cali, it, tx, green):
    (cf, cw, cs, cst, cls), (itf, iw, isz, ist, ils) = cali, it
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}"><tspan font-family="{cf}" font-weight="{cw}" font-size="{cs}" font-style="{cst}" letter-spacing="{cls}" fill="{tx}">Cali</tspan>'
            f'<tspan dx="12" font-family="{itf}" font-weight="{iw}" font-size="{isz}" font-style="{ist}" letter-spacing="{ils}" fill="{green}">IT</tspan></text>')

# (label, Cali style, IT style)  style = (font, weight, size, style, letter-spacing)
PAIRS6 = [
    ('Pacifico + Bebas Neue', ('Pacifico', 400, 36, 'normal', 0), ('Bebas Neue', 400, 46, 'normal', 1)),
    ('Playfair italic + Archivo Black', ('Playfair Display', 700, 42, 'italic', 0), ('Archivo Black', 400, 36, 'normal', 0)),
    ('Yellowtail + Montserrat', ('Yellowtail', 400, 46, 'normal', 0), ('Montserrat', 800, 36, 'normal', 1)),
    ('Bodoni italic + Big Shoulders', ('Bodoni Moda', 700, 42, 'italic', 0), ('Big Shoulders Display', 800, 48, 'normal', 1)),
    ('Instrument Serif + Syne', ('Instrument Serif', 400, 50, 'italic', 0), ('Syne', 800, 38, 'normal', 0)),
    ('Kaushan Script + Oswald', ('Kaushan Script', 400, 40, 'normal', 0), ('Oswald', 700, 40, 'normal', 1)),
    ('Fraunces + Unbounded', ('Fraunces', 600, 42, 'normal', 0), ('Unbounded', 700, 32, 'normal', 0)),
    ('DM Serif + Bebas Neue', ('DM Serif Display', 400, 44, 'normal', 0), ('Bebas Neue', 400, 48, 'normal', 2)),
    ('Abril Fatface + Josefin Sans', ('Abril Fatface', 400, 42, 'normal', 0), ('Josefin Sans', 700, 38, 'normal', 3)),
    ('Playfair + Michroma', ('Playfair Display', 700, 42, 'normal', 0), ("Michroma", 400, 34, "normal", 1)),
]

def tag(x, y, anchor, col):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Josefin Sans" font-weight="600" font-size="10.5" letter-spacing="5" fill="{col}">CONSULTING</text>'

def logo(treat, pair, green, dark, gid):
    _, cali, it = PAIRS6[pair]
    gname, g_light, g_dark = GREENS[green]
    gr = g_dark if dark else g_light
    tx = TEXT_LIGHT if dark else TEXT_DARK
    sub = SUB_DARK if dark else SUB_LIGHT
    k = '#1a2230' if dark else '#ffffff'
    fade = .22 if dark else .13
    tree = .34 if dark else .28
    if treat == 'one':          # faint state centered, one redwood on the north coast
        x, y, h = 122, 0, 96
        return (_state(x, y, h, gr, op=fade) + redwood(x + 14, 46, 46, gr, tree) + _dot(x, y, h, k)
                + word(165, 52, 'middle', cali, it, tx, gr) + tag(165, 72, 'middle', sub))
    if treat == 'two':          # two redwoods, one tall, one shorter
        x, y, h = 122, 0, 96
        return (_state(x, y, h, gr, op=fade) + redwood(x + 10, 44, 44, gr, tree) + redwood(x + 22, 46, 32, gr, tree * .8) + _dot(x, y, h, k)
                + word(165, 52, 'middle', cali, it, tx, gr) + tag(165, 72, 'middle', sub))
    if treat == 'left':         # state and trees behind the start of the name
        x, y, h = 20, 0, 96
        return (_state(x, y, h, gr, op=fade) + redwood(x + 12, 44, 44, gr, tree) + redwood(x + 24, 46, 30, gr, tree * .8) + _dot(x, y, h, k)
                + word(42, 52, 'start', cali, it, tx, gr) + tag(46, 72, 'start', sub))
    if treat == 'tall':         # one tall redwood rising above the state, like it's growing out of the north
        x, y, h = 122, 4, 92
        return (_state(x, y, h, gr, op=fade) + redwood(x + 16, 50, 52, gr, tree) + _dot(x, y, h, k)
                + word(165, 54, 'middle', cali, it, tx, gr) + tag(165, 74, 'middle', sub))
    if treat == 'panel':        # green panel; state and trees as lighter shapes inside
        x, y, h = 40, -2, 96
        return (f'<defs><clipPath id="{gid}"><rect x="10" y="6" width="310" height="84" rx="12"/></clipPath></defs><rect x="10" y="6" width="310" height="84" rx="12" fill="{g_light}"/>'
                f'<g clip-path="url(#{gid})">{_state(x, y, h, "#ffffff", op=.15)}{redwood(x + 12, 42, 42, "#ffffff", .22)}{redwood(x + 24, 44, 30, "#ffffff", .18)}</g>'
                + _dot(x, y, h, g_light, 2.6) + word(178, 54, 'middle', cali, it, '#ffffff', '#d9f2e2') + tag(178, 74, 'middle', '#e6f2ea'))
    raise ValueError(treat)

TREATS6 = [('One redwood', 'one'), ('Two redwoods', 'two'), ('Left, two redwoods', 'left'), ('Tall redwood', 'tall'), ('Green panel', 'panel')]
