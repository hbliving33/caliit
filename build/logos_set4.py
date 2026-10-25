"""Set 4 (131-160): variations on 108, the state of California sitting quietly behind the name.
Rules from Eric: no "California" in the words (Cali already says it), a small red dot on Huntington Beach that is not too strong,
and the dot's red is never used in any letter.  Taglines are broader than "IT consulting", since the work also covers
security, cloud, Microsoft 365, networks, data centers, access control, compliance and automation."""
from logos_set3 import CA, DOTS, HB

DOT_RED = '#d93636'
TAGS = ['IT CONSULTING', 'IT CONSULTING', 'IT CONSULTING & SECURITY', 'IT CONSULTING', 'IT · SECURITY · CLOUD', 'IT CONSULTING', 'IT STRATEGY & SECURITY']

def _state(x, y, h, fill='none', stroke='none', sw=0, op=1):
    s = h / 220
    return f'<g transform="translate({x} {y}) scale({s:.4f})" opacity="{op}"><path d="{CA}" fill="{fill}" stroke="{stroke}" stroke-width="{sw / s:.1f}" stroke-linejoin="round"/></g>'

def _dot(x, y, h, k, r=2.8):
    s = h / 220
    cx, cy = x + HB[0] * s, y + HB[1] * s
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r + 1.4}" fill="{k}"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{DOT_RED}"/>'

def _dots_state(x, y, h, col, op):
    s = h / 220
    return f'<g transform="translate({x} {y}) scale({s:.4f})" opacity="{op}">' + ''.join(f'<circle cx="{a}" cy="{b}" r="4.2" fill="{col}"/>' for a, b in DOTS['12']) + '</g>'

TYPES = {   # name: (font, weight, size, letter-spacing, text)
    'bold':    ('Montserrat', 800, 40, 1, 'Cali IT'),
    'caps':    ('Sora', 700, 34, 6, 'CALI IT'),
    'serif':   ('Fraunces', 600, 42, 0, 'Cali IT'),
    'clean':   ('Inter', 700, 42, -1, 'Cali IT'),
    'light':   ('Manrope', 500, 40, 2, 'Cali IT'),
}

def _word(x, y, anchor, typ, tx, c1, it_brand):
    f, w, size, ls, text = TYPES[typ]
    a, b = text.split(' ')
    it = f'<tspan fill="{c1}">{b}</tspan>' if it_brand else b
    wt = f' font-weight="{w}"'
    if typ == 'light':   # light "Cali", heavy "IT"
        it = f'<tspan font-weight="800"{" fill=" + chr(34) + c1 + chr(34) if it_brand else ""}>{b}</tspan>'
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{f}"{wt} font-size="{size}" letter-spacing="{ls}" fill="{tx}">{a} {it}</text>'

def _tag(x, y, anchor, tag, col, f='Inter'):
    size = 9.5 if len(tag) < 24 else 8.2
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{f}" font-weight="600" font-size="{size}" letter-spacing="2.4" fill="{col}">{tag}</text>'

def logo(treat, typ, tag, tx, sub, c1, k, it_brand, dark):
    """treat = how the state sits behind; typ = word style; tx = main text color; sub = tagline color; k = page color."""
    fade = .22 if dark else .13
    if treat == 'center':      # 108 style: faint state centered behind the name
        x, y, h = 122, 0, 96
        return _state(x, y, h, c1, op=fade) + _dot(x, y, h, k) + _word(165, 50, 'middle', typ, tx, c1, it_brand) + _tag(165, 70, 'middle', tag, sub)
    if treat == 'left':        # state behind the start of the name, everything left-aligned
        x, y, h = 20, 0, 96
        return _state(x, y, h, c1, op=fade) + _dot(x, y, h, k) + _word(44, 50, 'start', typ, tx, c1, it_brand) + _tag(46, 70, 'start', tag, sub)
    if treat == 'outline':     # thin outline instead of a fill
        x, y, h = 122, 0, 96
        return _state(x, y, h, 'none', c1, 1.6, op=.45 if dark else .35) + _dot(x, y, h, k) + _word(165, 50, 'middle', typ, tx, c1, it_brand) + _tag(165, 70, 'middle', tag, sub)
    if treat == 'dots':        # faint dot-grid state
        x, y, h = 122, 0, 96
        return _dots_state(x, y, h, c1, .3 if dark else .22) + _dot(x, y, h, k) + _word(165, 50, 'middle', typ, tx, c1, it_brand) + _tag(165, 70, 'middle', tag, sub)
    if treat == 'panel':       # name on a solid panel, state as a lighter shape inside it
        x, y, h = 40, 4, 96
        return (f'<defs><clipPath id="pc{typ}{treat}{int(dark)}{tag[:3]}"><rect x="10" y="6" width="310" height="84" rx="12"/></clipPath></defs>'
                f'<rect x="10" y="6" width="310" height="84" rx="12" fill="{c1}"/>'
                f'<g clip-path="url(#pc{typ}{treat}{int(dark)}{tag[:3]})">{_state(x, y - 6, h, "#ffffff", op=.16)}</g>' + _dot(x, y - 6, h, c1, 2.6)
                + _word(178, 52, 'middle', typ, '#ffffff', '#ffffff', False) + _tag(178, 72, 'middle', tag, '#ffffff'))
    if treat == 'big':         # oversized state drifting off the right edge, name on the left
        x, y, h = 222, -22, 110
        return (f'<defs><clipPath id="bc{typ}{int(dark)}{tag[:3]}"><rect width="330" height="96"/></clipPath></defs>'
                f'<g clip-path="url(#bc{typ}{int(dark)}{tag[:3]})">{_state(x, y, h, c1, op=fade)}{_dot(x, y, h, k, 3)}</g>'
                + _word(20, 54, 'start', typ, tx, c1, it_brand) + _tag(22, 76, 'start', tag, sub))
    raise ValueError(treat)

TREATS = [('Faint state, centered', 'center'), ('Faint state, left', 'left'), ('Outline state', 'outline'),
          ('Dot-grid state', 'dots'), ('Panel', 'panel'), ('Oversized state', 'big')]
