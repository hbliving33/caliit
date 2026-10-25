"""Builds logos.html: 50 Cali IT logo options (not linked from the site, noindex)."""
import pathlib, itertools
ROOT = pathlib.Path(__file__).resolve().parent.parent
NAVY, RED, SLATE, INK, SKY = '#0b2a5b', '#c8102e', '#5b6578', '#111827', '#2f6fd6'
FONTS = [('Inter','inter'),('Montserrat','montserrat'),('IBM Plex Sans','ibm-plex-sans'),('Space Grotesk','space-grotesk'),('Sora','sora'),
         ('Manrope','manrope'),('Outfit','outfit'),('Archivo','archivo'),('Barlow','barlow'),('Oswald','oswald'),('Rajdhani','rajdhani'),
         ('Exo 2','exo-2'),('Lexend','lexend'),('Raleway','raleway'),('Poppins','poppins')]
faces = ''.join(f'@font-face{{font-family:"{n}";src:url(assets/fonts/{s}-latin-{w}-normal.woff2) format("woff2");font-weight:{w};font-display:swap}}\n'
                for n, s in FONTS for w in (400, 600, 700, 800) if (ROOT / f'assets/fonts/{s}-latin-{w}-normal.woff2').exists())

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
PALS = [('Pacific','#1f6feb','#e5484d','#334155','#6ea8fe'),('Harbor','#2563eb','#dc3545','#1e293b','#7aa7ff'),
        ('Coastal','#0f7bd8','#e8505b','#3f4b5e','#5fb3f6'),('Skyline','#3b6fd8','#f05454','#2b3445','#8fb0f5'),
        ('Steel','#2f5fb3','#d9434f','#475569','#86a8e6')]
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
    mi = i % len(MARKS); wi = (i*2 + i//len(MARKS)) % len(WORDS); fi = (i*7) % len(FONTS); pi = (i*3 + i//len(MARKS)) % len(PALETTES)
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

html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Cali IT logo options</title>
<style>{faces}
*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,system-ui,sans-serif;background:#f3f5f9;color:#111827}}
header{{max-width:1240px;margin:0 auto;padding:28px 20px 6px}} h1{{margin:0;font-size:26px}} header p{{margin:6px 0 0;color:#5b6578}}
.grid{{max-width:1240px;margin:0 auto;padding:18px 20px 40px;display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}}
.card{{margin:0;background:#fff;border:1px solid #e3e7ef;border-radius:14px;overflow:hidden}}
.light{{padding:14px 14px 6px}} .dark{{background:#13213a;padding:10px 14px}} svg{{display:block;width:100%;height:auto}}
figcaption{{padding:8px 14px 12px;font-size:13px;color:#5b6578}} figcaption b{{color:#e5484d;margin-right:6px}}
.pals{{max-width:1240px;margin:0 auto;padding:14px 20px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}}
.pal{{background:#fff;border:1px solid #e3e7ef;border-radius:12px;padding:12px 14px}} .chips{{display:flex;gap:6px;margin-bottom:8px}} .chips i{{width:34px;height:34px;border-radius:8px;display:block}}
.pal b{{display:block;font-size:15px}} .pal small{{color:#5b6578;font-size:12px}} h2{{max-width:1240px;margin:22px auto 0;padding:0 20px;font-size:18px}}
</style></head><body><header><h1>Cali IT logo options</h1><p>A lighter, refreshed red, white and blue: brighter blue, a softer coral red, and slate gray for text.  No flag.  Pick a color scheme by name and a logo by number, or mix a mark from one with the type from another.</p></header>
<h2>Refreshed color schemes</h2><section class="pals">{sw}</section><h2>Logo options</h2><main class="grid">{"".join(cards)}</main></body></html>'''
(ROOT / 'logos.html').write_text(html)
print('cards', len(cards))
