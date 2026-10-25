"""Set 5 (161-190): the 108 idea (state behind the name, red dot on Huntington Beach) with livelier type.
All fonts are standard, free Google Fonts (Open Font License), served from the site itself."""
from logos_set4 import _state, _dot, _dots_state, DOT_RED

FONTS5 = [('Pacifico', 'pacifico'), ('Bebas Neue', 'bebas-neue'), ('Playfair Display', 'playfair-display'), ('Bricolage Grotesque', 'bricolage-grotesque'),
          ('Syne', 'syne'), ('Unbounded', 'unbounded'), ('Cinzel', 'cinzel'), ('Josefin Sans', 'josefin-sans'), ('Abril Fatface', 'abril-fatface'),
          ('Yellowtail', 'yellowtail'), ('Archivo Black', 'archivo-black'), ('Bodoni Moda', 'bodoni-moda'), ('Instrument Serif', 'instrument-serif'),
          ('Michroma', 'michroma'), ('Righteous', 'righteous'), ('Big Shoulders Display', 'big-shoulders-display'), ('Kaushan Script', 'kaushan-script')]

def T(x, y, anchor, parts, size_tag=None):
    """parts = list of (text, font, weight, size, style, color, letter-spacing)."""
    sp = ''.join(f'<tspan{" dx=" + chr(34) + "5" + chr(34) if i and parts[0][1] != f else ""} font-family="{f}" font-weight="{w}" font-size="{s}" font-style="{st}" fill="{c}" letter-spacing="{ls}">{t}</tspan>' for i, (t, f, w, s, st, c, ls) in enumerate(parts))
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}">{sp}</text>'

# Each pairing returns (name, parts-builder(tx, ac), tagline font, tagline weight).  tx = main text color, ac = brand color.
PAIRS = [
    ('Surf script + bold caps', lambda tx, ac: [('Cali', 'Pacifico', 400, 38, 'normal', tx, 0), (' IT', 'Bebas Neue', 400, 46, 'normal', ac, 1)], 'Josefin Sans', 600),
    ('Italic serif + heavy sans', lambda tx, ac: [('Cali', 'Playfair Display', 700, 42, 'italic', tx, 0), (' IT', 'Archivo Black', 400, 38, 'normal', ac, 0)], 'Josefin Sans', 600),
    ('Characterful grotesque', lambda tx, ac: [('Cali', 'Bricolage Grotesque', 800, 44, 'normal', tx, -1.5), (' IT', 'Bricolage Grotesque', 800, 44, 'normal', ac, -1.5)], 'Bricolage Grotesque', 600),
    ('Bold geometric', lambda tx, ac: [('Cali', 'Syne', 800, 42, 'normal', tx, -1), (' IT', 'Syne', 800, 42, 'normal', ac, -1)], 'Syne', 600),
    ('Wide modern caps', lambda tx, ac: [('CALI', 'Unbounded', 700, 30, 'normal', tx, 1), (' IT', 'Unbounded', 400, 30, 'normal', ac, 1)], 'Unbounded', 500),
    ('Classical caps', lambda tx, ac: [('CALI', 'Cinzel', 700, 36, 'normal', tx, 3), (' IT', 'Cinzel', 700, 36, 'normal', ac, 3)], 'Cinzel', 600),
    ('Vintage geometric', lambda tx, ac: [('CALI', 'Josefin Sans', 700, 38, 'normal', tx, 5), (' IT', 'Josefin Sans', 300 if False else 400, 38, 'normal', ac, 5)], 'Josefin Sans', 600),
    ('Fashion serif', lambda tx, ac: [('Cali', 'Abril Fatface', 400, 44, 'normal', tx, 0), (' IT', 'Abril Fatface', 400, 44, 'normal', ac, 1)], 'Josefin Sans', 600),
    ('Retro script + block', lambda tx, ac: [('Cali', 'Yellowtail', 400, 44, 'normal', tx, 0), (' IT', 'Archivo Black', 400, 36, 'normal', ac, 1)], 'Archivo Black', 400),
    ('Editorial italic', lambda tx, ac: [('Cali', 'Bodoni Moda', 700, 44, 'italic', tx, 0), (' IT', 'Bodoni Moda', 800, 44, 'normal', ac, 0)], 'Bodoni Moda', 600),
    ('Soft serif', lambda tx, ac: [('Cali', 'Instrument Serif', 400, 50, 'italic', tx, 0), (' IT', 'Instrument Serif', 400, 50, 'normal', ac, 0)], 'Josefin Sans', 600),
    ('Tech wide', lambda tx, ac: [('CALI', 'Michroma', 400, 28, 'normal', tx, 3), (' IT', 'Michroma', 400, 28, 'normal', ac, 3)], 'Michroma', 400),
    ('Rounded retro', lambda tx, ac: [('Cali', 'Righteous', 400, 44, 'normal', tx, 0), (' IT', 'Righteous', 400, 44, 'normal', ac, 0)], 'Righteous', 400),
    ('Tall condensed', lambda tx, ac: [('CALI', 'Big Shoulders Display', 800, 50, 'normal', tx, 2), (' IT', 'Big Shoulders Display', 800, 50, 'normal', ac, 2)], 'Big Shoulders Display', 700),
    ('Brush script + condensed', lambda tx, ac: [('Cali', 'Kaushan Script', 400, 42, 'normal', tx, 0), (' IT', 'Bebas Neue', 400, 46, 'normal', ac, 2)], 'Josefin Sans', 600),
]

def tag(x, y, anchor, text, col, f, w):
    size = 10 if f in ('Josefin Sans', 'Cinzel', 'Bodoni Moda', 'Big Shoulders Display') else 8.6
    if f == 'Big Shoulders Display': size = 12
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{f}" font-weight="{w}" font-size="{size}" letter-spacing="2.6" fill="{col}">{text}</text>'

def logo(pair, treat, tagtext, tx, sub, ac, k, dark, gid):
    name, parts, tf, tw = PAIRS[pair]
    fade = .22 if dark else .13
    if treat == 'center':
        x, y, h = 122, 0, 96
        return _state(x, y, h, ac, op=fade) + _dot(x, y, h, k) + T(165, 52, 'middle', parts(tx, ac)) + tag(165, 72, 'middle', tagtext, sub, tf, tw)
    if treat == 'left':
        x, y, h = 20, 0, 96
        return _state(x, y, h, ac, op=fade) + _dot(x, y, h, k) + T(44, 52, 'start', parts(tx, ac)) + tag(46, 72, 'start', tagtext, sub, tf, tw)
    if treat == 'big':
        x, y, h = 222, -22, 110
        return (f'<defs><clipPath id="{gid}"><rect width="330" height="96"/></clipPath></defs><g clip-path="url(#{gid})">{_state(x, y, h, ac, op=fade)}{_dot(x, y, h, k, 3)}</g>'
                + T(20, 52, 'start', parts(tx, ac)) + tag(22, 72, 'start', tagtext, sub, tf, tw))
    if treat == 'panel':
        x, y, h = 40, -2, 96
        return (f'<defs><clipPath id="{gid}"><rect x="10" y="6" width="310" height="84" rx="12"/></clipPath></defs><rect x="10" y="6" width="310" height="84" rx="12" fill="{ac}"/>'
                f'<g clip-path="url(#{gid})">{_state(x, y, h, "#ffffff", op=.16)}</g>' + _dot(x, y, h, ac, 2.6)
                + T(178, 52, 'middle', parts('#ffffff', '#ffffff')) + tag(178, 72, 'middle', tagtext, '#ffffff', tf, tw))
    if treat == 'dots':
        x, y, h = 122, 0, 96
        return _dots_state(x, y, h, ac, .3 if dark else .22) + _dot(x, y, h, k) + T(165, 52, 'middle', parts(tx, ac)) + tag(165, 72, 'middle', tagtext, sub, tf, tw)
    raise ValueError(treat)

TREATS5 = ['center', 'left', 'big', 'center', 'panel', 'dots']
