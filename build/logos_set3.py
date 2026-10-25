"""Set 3 of the Cali IT logo options (101-130): California-shaped marks, so people see what "Cali" means.
The outline comes from the public US Census state boundaries (us-atlas), mainland only, drawn in a 200 x 220 box."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
CA = (HERE / 'ca_path.txt').read_text().strip()
DOTS = json.loads((HERE / 'ca_dots.json').read_text())
HB = DOTS['hb']   # Huntington Beach, in the same 200 x 220 box

def ca(fill='none', stroke='none', sw=0, extra=''):
    return f'<path d="{CA}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" {extra}/>'

def place(inner, x, y, h):
    """Draw something made in the 200 x 220 box at (x, y), h units tall."""
    s = h / 220
    return f'<g transform="translate({x} {y}) scale({s:.4f})">{inner}</g>'

def logo(kind, f, tx, c1, c2, k, gid):
    W = 330
    if kind == 'through':      # name runs across a large state; letters turn white where they cross it
        word = lambda col: f'<text x="165" y="62" text-anchor="middle" font-family="{f}" font-weight="800" font-size="38" letter-spacing="3" fill="{col}">CALI IT</text>'
        return (f'<defs><clipPath id="{gid}"><g transform="translate(121 2) scale({92/220:.4f})"><path d="{CA}"/></g></clipPath></defs>'
                + place(ca(c1), 121, 2, 92) + word(tx) + f'<g clip-path="url(#{gid})">{word(k)}</g>'
                + f'<circle cx="{121 + HB[0]*92/220:.1f}" cy="{2 + HB[1]*92/220:.1f}" r="3.5" fill="{c2}"/>')
    if kind == 'through_serif':
        word = lambda col: f'<text x="165" y="62" text-anchor="middle" font-family="Fraunces" font-weight="700" font-size="40" fill="{col}">Cali IT</text>'
        return (f'<defs><clipPath id="{gid}"><g transform="translate(121 2) scale({92/220:.4f})"><path d="{CA}"/></g></clipPath></defs>'
                + place(ca(c1), 121, 2, 92) + word(tx) + f'<g clip-path="url(#{gid})">{word(k)}</g>')
    if kind == 'watermark':    # faint state behind the name
        return (place(ca(c1, extra='opacity=".14"'), 126, 2, 92)
                + f'<text x="165" y="56" text-anchor="middle" font-family="{f}" font-weight="700" font-size="36" fill="{tx}">Cali <tspan fill="{c1}">IT</tspan></text>'
                + f'<text x="165" y="76" text-anchor="middle" font-family="{f}" font-weight="600" font-size="9.5" letter-spacing="3" fill="{c2}">CALIFORNIA IT CONSULTING</text>')
    if kind == 'state_as_i':   # the state stands in for the I in CALI
        return (f'<text x="40" y="66" font-family="{f}" font-weight="800" font-size="44" letter-spacing="2" fill="{tx}">CAL</text>'
                + place(ca(c1), 142, 18, 54)
                + f'<circle cx="{142 + HB[0]*54/220:.1f}" cy="{18 + HB[1]*54/220:.1f}" r="2.6" fill="{c2}"/>'
                + f'<text x="200" y="66" font-family="{f}" font-weight="800" font-size="44" letter-spacing="2" fill="{c1}">IT</text>')
    if kind == 'it_inside':    # outline state with IT inside, Cali beside
        return (place(ca('none', c1, 9), 14, 4, 88)
                + f'<text x="35" y="36" text-anchor="middle" font-family="{f}" font-weight="800" font-size="16" fill="{c2}">IT</text>'
                + f'<text x="104" y="62" font-family="{f}" font-weight="700" font-size="40" fill="{tx}">Cali IT</text>')
    if kind == 'cutout':       # solid state with IT cut out of it
        return (f'<defs><mask id="{gid}"><rect width="330" height="96" fill="#fff"/><text x="36" y="36" text-anchor="middle" font-family="{f}" font-weight="800" font-size="17" fill="#000">IT</text></mask></defs>'
                + f'<g mask="url(#{gid})">{place(ca(c1), 14, 4, 88)}</g>'
                + f'<text x="106" y="56" font-family="{f}" font-weight="700" font-size="34" fill="{tx}">Cali IT</text>'
                + f'<text x="107" y="74" font-family="{f}" font-weight="500" font-size="11" letter-spacing="2" fill="{c2}">TECHNOLOGY CONSULTING</text>')
    if kind == 'dots':         # state built from a dot grid (tech feel)
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c2 if abs(x - HB[0]) < 9 and abs(y - HB[1]) < 9 else c1}"/>' for x, y in DOTS['12'])
        return place(dots, 14, 4, 88) + f'<text x="106" y="62" font-family="{f}" font-weight="700" font-size="38" fill="{tx}">Cali <tspan fill="{c1}">IT</tspan></text>'
    if kind == 'pixels':       # state built from square pixels
        px = ''.join(f'<rect x="{x - 6.5}" y="{y - 6.5}" width="13" height="13" rx="2" fill="{c2 if abs(x - HB[0]) < 10 and abs(y - HB[1]) < 10 else c1}"/>' for x, y in DOTS['16'])
        return place(px, 14, 4, 88) + f'<text x="106" y="62" font-family="JetBrains Mono" font-weight="700" font-size="34" fill="{tx}">cali<tspan fill="{c2}">/</tspan><tspan fill="{c1}">it</tspan></text>'
    if kind == 'pin':          # state with a location pin on the home coast
        hx, hy = HB
        pin = f'<g transform="translate({hx} {hy})"><path d="M0 0 C-14 -22 -26 -34 -26 -50 A26 26 0 0 1 26 -50 C26 -34 14 -22 0 0Z" fill="{c2}"/><circle cx="0" cy="-50" r="10" fill="{k}"/></g>'
        return place(ca(c1) + pin, 14, 4, 88) + f'<text x="106" y="56" font-family="{f}" font-weight="700" font-size="34" fill="{tx}">Cali IT</text><text x="107" y="74" font-family="{f}" font-weight="500" font-size="11" letter-spacing="2" fill="{c1}">HUNTINGTON BEACH · CA</text>'
    if kind == 'circuit':      # state outline filled with circuit traces
        traces = (f'<g clip-path="url(#{gid})" stroke="{c1}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".9">'
                  f'<path d="M20 20 H70 V70 H120"/><path d="M40 60 V110 H100 V150 H150"/><path d="M60 140 V180 H110"/><path d="M90 40 V90 H140 V120"/></g>'
                  + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c2}"/>' for x, y in [(120, 70), (150, 150), (110, 180), (140, 120)]))
        return (f'<defs><clipPath id="{gid}"><path d="{CA}"/></clipPath></defs>'
                + place(ca('none', c1, 8) + traces, 14, 4, 88)
                + f'<text x="106" y="62" font-family="{f}" font-weight="700" font-size="38" fill="{tx}">Cali <tspan fill="{c1}">IT</tspan></text>')
    if kind == 'badge':        # state inside a circle badge
        return (f'<circle cx="52" cy="48" r="42" fill="{c1}"/>' + place(ca(k), 33, 12, 72)
                + f'<circle cx="{33 + HB[0]*72/220:.1f}" cy="{12 + HB[1]*72/220:.1f}" r="3.6" fill="{c2}"/>'
                + f'<text x="108" y="58" font-family="{f}" font-weight="800" font-size="34" letter-spacing="3" fill="{tx}">CALI <tspan fill="{c1}">IT</tspan></text>')
    if kind == 'tile':         # state cut out of a rounded tile
        return (f'<rect x="10" y="6" width="84" height="84" rx="18" fill="{c1}"/>' + place(ca(k), 26, 12, 72)
                + f'<rect x="{26 + HB[0]*72/220 - 3:.1f}" y="{12 + HB[1]*72/220 - 3:.1f}" width="6" height="6" fill="{c2}"/>'
                + f'<text x="110" y="62" font-family="{f}" font-weight="700" font-size="38" fill="{tx}">Cali IT</text>')
    if kind == 'shield':       # state inside a shield (security)
        sh = f'<path d="M52 4 L90 16 V44 C90 68 74 84 52 92 C30 84 14 68 14 44 V16Z" fill="{c1}"/>'
        return sh + place(ca(k), 36, 16, 64) + f'<text x="106" y="56" font-family="{f}" font-weight="700" font-size="34" fill="{tx}">Cali IT</text><text x="107" y="74" font-family="{f}" font-weight="600" font-size="11" letter-spacing="2" fill="{c2}">IT AND SECURITY</text>'
    if kind == 'stacked':      # state above the name
        return place(ca(c1), 146, 2, 52) + f'<circle cx="{146 + HB[0]*52/220:.1f}" cy="{2 + HB[1]*52/220:.1f}" r="2.4" fill="{c2}"/><text x="165" y="86" text-anchor="middle" font-family="{f}" font-weight="700" font-size="22" letter-spacing="5" fill="{tx}">CALI <tspan fill="{c1}">IT</tspan></text>'
    if kind == 'outline_slash':  # thin outline with a bold slash through it
        return (place(ca('none', c1, 6), 14, 4, 88) + f'<path d="M36 82 L70 14" stroke="{c2}" stroke-width="7" stroke-linecap="round"/>'
                + f'<text x="106" y="62" font-family="{f}" font-weight="300" font-size="38" letter-spacing="1" fill="{tx}">cali<tspan font-weight="800" fill="{c1}">it</tspan></text>')
    if kind == 'sun':          # state with a setting sun on the coast
        sun = f'<clipPath id="{gid}"><rect x="-40" y="0" width="140" height="220"/></clipPath>'
        return (place(f'<defs>{sun}</defs><circle cx="20" cy="150" r="46" fill="{c2}" clip-path="url(#{gid})"/>' + ca(c1), 18, 4, 88)
                + f'<text x="106" y="62" font-family="{f}" font-weight="700" font-size="38" fill="{tx}">Cali <tspan fill="{c2}">IT</tspan></text>')
    if kind == 'gradient':     # gradient-filled state
        return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
                + place(ca(f'url(#{gid})'), 14, 4, 88) + f'<text x="106" y="62" font-family="{f}" font-weight="800" font-size="38" letter-spacing="-.5" fill="{tx}">Cali IT</text>')
    if kind == 'split':        # state split north / south in two colors
        return (f'<defs><clipPath id="{gid}"><rect x="0" y="0" width="200" height="118"/></clipPath></defs>'
                + place(ca(c2) + f'<g clip-path="url(#{gid})">{ca(c1)}</g>', 14, 4, 88)
                + f'<text x="106" y="56" font-family="{f}" font-weight="700" font-size="34" fill="{tx}">Cali IT</text><text x="107" y="74" font-family="{f}" font-weight="500" font-size="11" letter-spacing="2" fill="{c1}">NORTH TO SOUTH</text>')
    raise ValueError(kind)

KINDS = [('Name through the state', 'through'), ('State as the I', 'state_as_i'), ('Dot state', 'dots'), ('Home pin', 'pin'),
         ('IT cut out', 'cutout'), ('Serif through the state', 'through_serif'), ('Circle badge', 'badge'),
         ('Watermark', 'watermark'), ('Pixel state', 'pixels'), ('IT inside', 'it_inside'), ('Shield', 'shield'), ('Tile', 'tile'),
         ('Stacked', 'stacked'), ('Outline and slash', 'outline_slash'), ('Gradient', 'gradient'), ('North and south', 'split')]
