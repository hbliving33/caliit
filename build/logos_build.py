"""Builds logos.html: 50 Cali IT logo options (not linked from the site, noindex)."""
import pathlib, itertools
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAVY, RED, SLATE, INK, SKY = '#0b2a5b', '#c8102e', '#5b6578', '#111827', '#2f6fd6'
FONTS = [('Inter','inter'),('Montserrat','montserrat'),('IBM Plex Sans','ibm-plex-sans'),('Space Grotesk','space-grotesk'),('Sora','sora'),
         ('Manrope','manrope'),('Outfit','outfit'),('Archivo','archivo'),('Barlow','barlow'),('Oswald','oswald'),('Rajdhani','rajdhani'),
         ('Exo 2','exo-2'),('Lexend','lexend'),('Raleway','raleway'),('Poppins','poppins')]
EXTRA = [('Fraunces','fraunces'),('IBM Plex Serif','ibm-plex-serif'),('DM Serif Display','dm-serif-display'),('IBM Plex Mono','ibm-plex-mono'),('JetBrains Mono','jetbrains-mono')]
faces = ''.join(f'@font-face{{font-family:"{n}";src:url(assets/fonts/{s}-latin-{w}-normal.woff2) format("woff2");font-weight:{w};font-display:swap}}\n'
                for n, s in FONTS + EXTRA for w in (400, 600, 700, 800) if (ROOT / f'assets/fonts/{s}-latin-{w}-normal.woff2').exists())

# ---- marks: each returns SVG drawn in a 64x64 box ----
def m_shield(c1,c2): return f'<path d="M32 4 L56 12 V30 C56 46 45 56 32 60 C19 56 8 46 8 30 V12Z" fill="{c1}"/><path d="M40 22 A11 11 0 1 0 40 42" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="44" cy="32" r="3" fill="{c2}"/>'
def m_hex(c1,c2): return f'<path d="M32 4 L56 18 V46 L32 60 L8 46 V18Z" fill="{c1}"/><text x="32" y="41" text-anchor="middle" font-weight="800" font-size="24" fill="#fff" font-family="inherit">CI</text><rect x="20" y="46" width="24" height="3" fill="{c2}"/>'
def m_rsq(c1,c2): return f'<rect x="6" y="6" width="52" height="52" rx="14" fill="{c1}"/><path d="M40 22 A12 12 0 1 0 40 42" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/><circle cx="46" cy="32" r="4" fill="{c2}"/>'
def m_ring(c1,c2): return f'<circle cx="32" cy="32" r="26" fill="none" stroke="{c1}" stroke-width="5"/><path d="M41 23 A13 13 0 1 0 41 41" fill="none" stroke="{c2}" stroke-width="6" stroke-linecap="round"/>'
def m_bars(c1,c2): return f'<rect x="10" y="38" width="10" height="16" rx="2" fill="{c1}"/><rect x="26" y="26" width="10" height="28" rx="2" fill="{c1}"/><rect x="42" y="12" width="10" height="42" rx="2" fill="{c2}"/>'
def m_chev(c1,c2): return f'<path d="M8 44 L32 20 L56 44" fill="none" stroke="{c1}" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/><path d="M20 54 L32 42 L44 54" fill="none" stroke="{c2}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
def m_nodes(c1,c2): return f'<path d="M14 46 L32 16 L50 46 Z" fill="none" stroke="{c1}" stroke-width="4"/><circle cx="32" cy="16" r="7" fill="{c2}"/><circle cx="14" cy="46" r="7" fill="{c1}"/><circle cx="50" cy="46" r="7" fill="{c1}"/>'
def m_sun(c1,c2): return f'<path d="M10 38 A22 22 0 0 1 54 38Z" fill="{c2}"/><path d="M4 44 Q18 38 32 44 T60 44" fill="none" stroke="{c1}" stroke-width="5" stroke-linecap="round"/><path d="M4 54 Q18 48 32 54 T60 54" fill="none" stroke="{c1}" stroke-width="5" stroke-linecap="round"/>'
def m_lock(c1,c2): return f'<path d="M20 28 V20 A12 12 0 0 1 44 20 V28" fill="none" stroke="{c1}" stroke-width="6"/><rect x="12" y="28" width="40" height="30" rx="6" fill="{c1}"/><circle cx="32" cy="40" r="5" fill="{c2}"/><rect x="30" y="42" width="4" height="9" rx="2" fill="{c2}"/>'
def m_arcs(c1,c2): return f'<path d="M44 12 A24 24 0 1 0 44 52" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round"/><path d="M40 21 A14 14 0 1 0 40 43" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round"/><circle cx="34" cy="32" r="4.5" fill="{c2}"/>'
def m_grid(c1,c2): return f'<rect x="8" y="8" width="22" height="22" rx="4" fill="{c1}"/><rect x="34" y="8" width="22" height="22" rx="4" fill="{c1}"/><rect x="8" y="34" width="22" height="22" rx="4" fill="{c1}"/><rect x="34" y="34" width="22" height="22" rx="4" fill="{c2}"/>'
def m_brkt(c1,c2): return f'<path d="M22 8 H12 V56 H22" fill="none" stroke="{c1}" stroke-width="6"/><path d="M42 8 H52 V56 H42" fill="none" stroke="{c1}" stroke-width="6"/><text x="32" y="42" text-anchor="middle" font-weight="800" font-size="22" fill="{c2}" font-family="inherit">IT</text>'
def m_cloud(c1,c2): return f'<path d="M18 48 A11 11 0 0 1 17 26 A15 15 0 0 1 45 22 A12 12 0 0 1 47 48Z" fill="{c1}"/><path d="M36 30 A7 7 0 1 0 36 40" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><rect x="18" y="52" width="28" height="4" rx="2" fill="{c2}"/>'
def m_split(c1,c2): return f'<path d="M48 14 A24 24 0 0 0 10 32" fill="none" stroke="{c1}" stroke-width="10" stroke-linecap="round"/><path d="M10 32 A24 24 0 0 0 48 50" fill="none" stroke="{c2}" stroke-width="10" stroke-linecap="round"/>'
def m_circuit(c1,c2): return f'<path d="M44 16 A20 20 0 1 0 44 48" fill="none" stroke="{c1}" stroke-width="6" stroke-linecap="round"/><path d="M32 32 H56 M44 32 V20 H56 M44 32 V44 H56" fill="none" stroke="{c2}" stroke-width="3"/><circle cx="56" cy="20" r="3" fill="{c2}"/><circle cx="56" cy="32" r="3" fill="{c2}"/><circle cx="56" cy="44" r="3" fill="{c2}"/>'
MARKS = [('Shield',m_shield),('Hexagon',m_hex),('Tile',m_rsq),('Ring',m_ring),('Signal bars',m_bars),('Peak',m_chev),('Network',m_nodes),
         ('Coastline',m_sun),('Lock',m_lock),('Arcs',m_arcs),('Grid',m_grid),('Brackets',m_brkt),('Cloud',m_cloud),('Split C',m_split),('Circuit C',m_circuit)]
PALS = [('Pacific Teal','#0e7c86','#f08a4b','#1f2d3d','#5fd0d8'),('Redwood & Sage','#2f6d4f','#c99a2e','#243028','#7fc8a0'),
        ('Indigo Sunset','#3d348b','#f18701','#262338','#a59bf0'),('Plum & Peach','#6a3f99','#f27c5f','#2a2438','#c2a6ee'),
        ('Graphite & Lime','#2f3a40','#6bb33e','#1f2629','#cfd8dc'),('Slate & Coral','#36557a','#ef6f6c','#1f2933','#9fb8d6'),
        ('Desert Clay','#b5562b','#23867a','#2d2a26','#eba07a'),('Ocean & Amber','#14619e','#e09a00','#1c2533','#74b3f0')]
PALETTES = [(b,r) for _,b,r,_,_ in PALS]
TINT = {b:t for _,b,_,_,t in PALS}
TEXT = {b:x for _,b,_,x,_ in PALS}
# ---- wordmark styles ----
def w_caps(f,c1,c2): return f'<text x="0" y="0" font-family="{f}" font-weight="700" font-size="30" letter-spacing="2" fill="{c1}">CALI <tspan fill="{c2}">IT</tspan></text>'
def w_title(f,c1,c2): return f'<text x="0" y="0" font-family="{f}" font-weight="700" font-size="32" fill="{c1}">Cali<tspan fill="{c2}" font-weight="800"> IT</tspan></text>'
def w_light(f,c1,c2): return f'<text x="0" y="0" font-family="{f}" font-weight="400" font-size="32" fill="{c1}">cali<tspan font-weight="800" fill="{c2}">it</tspan></text>'
def w_stack(f,c1,c2): return f'<text x="0" y="-12" font-family="{f}" font-weight="800" font-size="28" letter-spacing="3" fill="{c1}">CALI IT</text><text x="1" y="12" font-family="{f}" font-weight="600" font-size="10" textLength="228" lengthAdjust="spacing" fill="{c2}">IT AND SECURITY CONSULTING</text>'
def w_rule(f,c1,c2): return f'<text x="0" y="0" font-family="{f}" font-weight="700" font-size="30" letter-spacing="1" fill="{c1}">Cali IT</text><rect x="0" y="9" width="44" height="4" fill="{c2}"/>'
WORDS = [w_caps, w_title, w_light, w_stack, w_rule]

sw=''.join(f'<div class="pal"><div class="chips"><i style="background:{b}"></i><i style="background:{r}"></i><i style="background:{x}"></i><i style="background:#f5f8fc;border:1px solid #dde3ec"></i></div><b>{nm}</b><small>{b} · {r} · {x}</small></div>' for nm,b,r,x,_ in PALS)
cards=[]; n=0
combos = list(itertools.product(range(len(MARKS)), range(len(WORDS))))
seen=set()
i=0
while len(cards)<50:
    mi = i % len(MARKS); wi = (i*2 + i//len(MARKS)) % len(WORDS); fi = (i*7) % len(FONTS); pi = i % len(PALETTES)
    i += 1
    if (mi,wi) in seen: continue
    seen.add((mi,wi)); n += 1
    mname, mf = MARKS[mi]; fname = FONTS[fi][0]; c1, c2 = PALETTES[pi]
    wc2 = c1 if (n % 2) else c2   # alternate: "IT" in blue or in red
    svg = (f'<svg viewBox="0 0 330 96" role="img" aria-label="Cali IT logo option {n}" style="font-family:\'{fname}\'">'
           f'<g transform="translate(8 16)">{mf(c1,c2)}</g><g transform="translate(88 58)">{WORDS[wi](fname,TEXT[c1],wc2)}</g></svg>')
    dark = (f'<svg viewBox="0 0 330 96" aria-hidden="true" style="font-family:\'{fname}\'"><g transform="translate(8 16)">{mf(TINT[c1],c2)}</g>'
            f'<g transform="translate(88 58)">{WORDS[wi](fname,"#ffffff",TINT[c1] if wc2==c1 else c2)}</g></svg>')
    pal = next(nm for nm,b,*_ in PALS if b==c1)
    cards.append(f'<figure class="card"><div class="light">{svg}</div><div class="dark">{dark}</div><figcaption><b>{n}</b> {mname} · {fname} · {pal}</figcaption></figure>')


# ---------------- Set 2 (51-100): new styles ----------------
import sys; sys.path.insert(0, str(ROOT / 'build'))
from logos_set2 import MARKS2
SANS2 = ['Inter','Manrope','IBM Plex Sans','Sora','Outfit','Archivo','Lexend','Montserrat','Space Grotesk','Barlow']
def wd_side(style, f, tx, c1, c2):
    if style == 'serif':  return f'<text x="0" y="-2" font-family="Fraunces" font-weight="600" font-size="31" fill="{tx}">Cali <tspan fill="{c1}">IT</tspan></text><text x="1" y="16" font-family="{f}" font-weight="600" font-size="9.5" letter-spacing="3" fill="{c2}">TECHNOLOGY CONSULTING</text>'
    if style == 'plexserif': return f'<text x="0" y="0" font-family="IBM Plex Serif" font-weight="600" font-size="30" fill="{tx}">Cali IT</text><rect x="1" y="9" width="30" height="3" fill="{c2}"/>'
    if style == 'slash':  return f'<text x="0" y="0" font-family="JetBrains Mono" font-weight="700" font-size="30" fill="{tx}">cali<tspan fill="{c2}">/</tspan><tspan fill="{c1}">it</tspan></text>'
    if style == 'dot':    return f'<text x="0" y="0" font-family="{f}" font-weight="800" font-size="32" letter-spacing="-1" fill="{tx}">caliit<tspan fill="{c2}">.</tspan></text>'
    if style == 'divider':return f'<text x="0" y="0" font-family="{f}" font-weight="700" font-size="27" letter-spacing="3" fill="{tx}">CALI</text><rect x="86" y="-24" width="2.5" height="28" fill="{c2}"/><text x="98" y="0" font-family="{f}" font-weight="400" font-size="27" letter-spacing="3" fill="{c1}">IT</text>'
    if style == 'spaced': return f'<text x="0" y="0" font-family="{f}" font-weight="400" font-size="24" letter-spacing="7" fill="{tx}">CALI <tspan font-weight="700" fill="{c1}">IT</tspan></text>'
    if style == 'two':    return f'<text x="0" y="-4" font-family="{f}" font-weight="700" font-size="27" fill="{tx}">Cali IT</text><text x="1" y="14" font-family="{f}" font-weight="400" font-size="12" fill="{c1}">IT and security consulting</text>'
    return f'<text x="0" y="0" font-family="{f}" font-weight="600" font-size="31" fill="{tx}">Cali <tspan fill="{c1}">IT</tspan></text>'
SIDE_STYLES = ['serif','slash','dot','divider','spaced','two','plain','plexserif']
def full_logo(kind, f, tx, c1, c2, k, gid):
    if kind == 'seal':
        return (f'<defs><path id="{gid}r" d="M165 48 m-34 0 a34 34 0 1 1 68 0 a34 34 0 1 1 -68 0"/></defs><circle cx="165" cy="48" r="45" fill="none" stroke="{c1}" stroke-width="2"/><circle cx="165" cy="48" r="25" fill="{c1}"/>'
                f'<text font-family="{f}" font-weight="700" font-size="7.6" fill="{tx}"><textPath href="#{gid}r" textLength="208" lengthAdjust="spacing">TECHNOLOGY · SECURITY · CONSULTING · CALI IT ·</textPath></text>'
                f'<text x="165" y="55" text-anchor="middle" font-family="Fraunces" font-weight="700" font-size="19" fill="{k}">CI</text><rect x="156" y="59" width="18" height="2" fill="{c2}"/>')
    if kind == 'box':
        return f'<rect x="60" y="20" width="210" height="56" fill="none" stroke="{tx}" stroke-width="3"/><text x="165" y="58" text-anchor="middle" font-family="{f}" font-weight="700" font-size="28" letter-spacing="6" fill="{tx}">CALI <tspan fill="{c1}">IT</tspan></text><rect x="150" y="16" width="30" height="8" fill="{c2}"/>'
    if kind == 'split':
        return f'<rect x="58" y="22" width="122" height="52" fill="{c1}"/><text x="119" y="58" text-anchor="middle" font-family="{f}" font-weight="800" font-size="28" letter-spacing="2" fill="{k}">CALI</text><rect x="180" y="22" width="92" height="52" fill="none" stroke="{c1}" stroke-width="3"/><text x="226" y="58" text-anchor="middle" font-family="{f}" font-weight="800" font-size="28" letter-spacing="2" fill="{c1}">IT</text><rect x="58" y="74" width="214" height="4" fill="{c2}"/>'
    if kind == 'prompt':
        return f'<text x="62" y="58" font-family="JetBrains Mono" font-weight="700" font-size="30" fill="{c2}">&gt;_</text><text x="116" y="58" font-family="JetBrains Mono" font-weight="700" font-size="30" fill="{tx}">cali<tspan fill="{c1}">.it</tspan></text><rect x="250" y="34" width="14" height="28" fill="{c1}"><animate attributeName="opacity" values="1;1;0;0" dur="1.2s" repeatCount="indefinite"/></rect>'
    if kind == 'classic':
        return f'<text x="165" y="48" text-anchor="middle" font-family="DM Serif Display" font-size="38" fill="{tx}">Cali IT</text><rect x="92" y="63" width="32" height="1.5" fill="{c2}"/><rect x="206" y="63" width="32" height="1.5" fill="{c2}"/><text x="165" y="66" text-anchor="middle" font-family="{f}" font-weight="600" font-size="8.5" letter-spacing="2.6" fill="{c1}">CONSULTING</text>'
    if kind == 'underline':
        return f'<text x="165" y="56" text-anchor="middle" font-family="{f}" font-weight="800" font-size="40" letter-spacing="-1.5" fill="{tx}">caliit</text><rect x="104" y="66" width="80" height="6" rx="3" fill="{c1}"/><rect x="190" y="66" width="36" height="6" rx="3" fill="{c2}"/>'
FULLS = ['seal','box','split','prompt','classic','underline']

cards2 = []; n2 = 50; j = 0
plan = []   # (layout, mark index or full kind)
for t in range(50):
    if t % 5 == 4: plan.append(('full', FULLS[(t // 5) % len(FULLS)]))
    elif t % 5 == 2: plan.append(('stack', (t * 7) % len(MARKS2)))
    else: plan.append(('side', (t * 3) % len(MARKS2)))
for t, (layout, what) in enumerate(plan):
    n2 += 1
    c1, c2 = PALETTES[(t * 3 + 1) % len(PALETTES)]
    f = SANS2[t % len(SANS2)]
    pal = next(nm for nm, b, *_ in PALS if b == c1)
    def draw(dark):
        a = TINT[c1] if dark else c1; tx = '#ffffff' if dark else TEXT[c1]; k = '#1a2230' if dark else '#ffffff'; gid = f'g{n2}{"d" if dark else "l"}'
        if layout == 'full':
            return full_logo(what, f, tx, a, c2, k, gid), what.capitalize()
        name, mf = MARKS2[what]
        mk = mf(a, c2, k, gid=gid) if name == 'Gradient C' else (mf(a, c2, k, f=f) if name == 'ci monogram' else mf(a, c2, k))
        if layout == 'stack':
            word = f'<text x="165" y="88" text-anchor="middle" font-family="{f}" font-weight="700" font-size="20" letter-spacing="4" fill="{tx}">CALI <tspan fill="{a}">IT</tspan></text>'
            return f'<g transform="translate(141 4) scale(.75)">{mk}</g>{word}', name + ' (stacked)'
        style = SIDE_STYLES[t % len(SIDE_STYLES)]
        return f'<g transform="translate(8 16)">{mk}</g><g transform="translate(88 58)">{wd_side(style, f, tx, a, c2)}</g>', name
    light, label = draw(False); dark, _ = draw(True)
    fnt = f
    cards2.append(f'<figure class="card"><div class="light"><svg viewBox="0 0 330 96" role="img" aria-label="Cali IT logo option {n2}" style="font-family:\'{f}\'">{light}</svg></div>'
                  f'<div class="dark"><svg viewBox="0 0 330 96" aria-hidden="true" style="font-family:\'{f}\'">{dark}</svg></div><figcaption><b>{n2}</b> {label} · {fnt} · {pal}</figcaption></figure>')

# ---------------- Set 3 (101-130): California-shaped marks ----------------
from logos_set3 import logo as ca_logo, KINDS as CA_KINDS
cards3 = []; n3 = 100
SANS3 = ['Montserrat','Inter','Sora','Manrope','Archivo','Outfit','Lexend','IBM Plex Sans','Space Grotesk','Barlow']
order = list(range(len(CA_KINDS))) + list(range(14))
for t, ki in enumerate(order):
    n3 += 1
    label, kind = CA_KINDS[ki]
    c1, c2 = PALETTES[(t * 5 + 2) % len(PALETTES)]
    f = SANS3[t % len(SANS3)]
    pal = next(nm for nm, b, *_ in PALS if b == c1)
    lt = ca_logo(kind, f, TEXT[c1], c1, c2, '#ffffff', f'c{n3}l')
    dk = ca_logo(kind, f, '#ffffff', TINT[c1], c2, '#1a2230', f'c{n3}d')
    cards3.append(f'<figure class="card"><div class="light"><svg viewBox="0 0 330 96" role="img" aria-label="Cali IT logo option {n3}" style="font-family:\'{f}\'">{lt}</svg></div>'
                  f'<div class="dark"><svg viewBox="0 0 330 96" aria-hidden="true" style="font-family:\'{f}\'">{dk}</svg></div><figcaption><b>{n3}</b> {label} · {f} · {pal}</figcaption></figure>')

# ---------------- Set 4 (131-160): variations on 108, the state behind the name ----------------
from logos_set4 import logo as bg_logo, TREATS, TYPES as BG_TYPES, TAGS as BG_TAGS
cards4 = []; n4 = 130
PAL4 = [pp for pp in PALS if pp[0] != 'Desert Clay']   # its clay color is too close to the red dot
typs = list(BG_TYPES)
for t in range(30):
    n4 += 1
    tl, treat = TREATS[t % len(TREATS)]
    typ = typs[(t // len(TREATS) + t) % len(typs)]
    nm, c1, _, txc, tint = PAL4[(t * 2 + 1) % len(PAL4)]
    tag = BG_TAGS[t % len(BG_TAGS)]
    it_brand = (t % 3 != 2)
    lt = bg_logo(treat, typ, tag, txc, '#5b6578', c1, '#ffffff', it_brand, False)
    dk = bg_logo(treat, typ, tag, '#ffffff', '#aab4c3', tint, '#1a2230', it_brand, True)
    f = BG_TYPES[typ][0]
    cards4.append(f'<figure class="card"><div class="light"><svg viewBox="0 0 330 96" role="img" aria-label="Cali IT logo option {n4}">{lt}</svg></div>'
                  f'<div class="dark"><svg viewBox="0 0 330 96" aria-hidden="true">{dk}</svg></div><figcaption><b>{n4}</b> {tl} · {f} · {nm}</figcaption></figure>')

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Cali IT logo options</title>
<style>{faces}
*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,system-ui,sans-serif;background:#f3f5f9;color:#111827}}
header{{max-width:1240px;margin:0 auto;padding:28px 20px 6px}} h1{{margin:0;font-size:26px}} header p{{margin:6px 0 0;color:#5b6578}}
.grid{{max-width:1240px;margin:0 auto;padding:18px 20px 40px;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}}
.card{{margin:0;background:#fff;border:1px solid #e3e7ef;border-radius:14px;overflow:hidden}}
.light{{padding:14px 14px 6px}} .dark{{background:#1a2230;padding:10px 14px}} svg{{display:block;width:100%;height:auto}}
figcaption{{padding:8px 14px 12px;font-size:13px;color:#5b6578}} figcaption b{{color:#0e7c86;margin-right:6px}}
.pals{{max-width:1240px;margin:0 auto;padding:14px 20px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}
.pal{{background:#fff;border:1px solid #e3e7ef;border-radius:12px;padding:12px 14px}} .chips{{display:flex;gap:6px;margin-bottom:8px}} .chips i{{width:34px;height:34px;border-radius:8px;display:block}}
.pal b{{display:block;font-size:15px}} .pal small{{color:#5b6578;font-size:12px}} h2{{max-width:1240px;margin:22px auto 0;padding:0 20px;font-size:18px}}
</style></head><body><header><h1>Cali IT logo options</h1><p>Eight new color schemes, no red, white and blue.  Each logo is shown in one scheme, but any logo works in any scheme.  Pick a scheme by name and a logo by number, for example: logo 14 in Pacific Teal.</p></header>
<h2>Refreshed color schemes</h2><section class="pals">{sw}</section><h2 id="set4">Built on 108: the state behind the name, 131 to 160</h2><main class="grid">{"".join(cards4)}</main><h2 id="set3">California, 101 to 130</h2><main class="grid">{"".join(cards3)}</main><h2 id="set2">New styles, 51 to 100</h2><main class="grid">{"".join(cards2)}</main><h2 id="set1">First set, 1 to 50</h2><main class="grid">{"".join(cards)}</main></body></html>'''
(ROOT / 'logos.html').write_text(html)
print('cards', len(cards))
