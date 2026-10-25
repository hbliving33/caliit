"""Cali IT Consulting site, "field chart" design.  Content comes from site_build.py; this file owns the layout.
Run from the repo root:  python3 build/site2_build.py"""
import json, pathlib, re, html, sys, importlib.util
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'build'))
spec = importlib.util.spec_from_file_location('sb', ROOT / 'build' / 'site_build.py'); sb = importlib.util.module_from_spec(spec); spec.loader.exec_module(sb)
from logos_set3 import CA
from logos_set6 import redwood
E = html.escape
GRID = json.loads((ROOT / 'build' / 'ca_grid.json').read_text())
CX, CY = GRID['centroid']
ARCATA, HB = (14.1, 27.9), (124.5, 191.2)
ORDER = ['network', 'cloud', 'data-center', 'microsoft-365', 'it-strategy', 'cybersecurity', 'business-automation', 'access-control', 'compliance']
sb.SERVICES.sort(key=lambda x: ORDER.index(x['slug']))
for _x in sb.SERVICES:
    if _x['slug'] == 'cloud': _x['short'] = 'Servers, storage, virtualization and cloud, with backups you have tested.'
    if _x['slug'] == 'microsoft-365': _x['short'] = 'Licensing under control, plus tenant security and migrations.'
    if _x['slug'] == 'it-strategy': _x['short'] = 'Day-to-day IT operations leadership, roadmaps, budgets and vendors.'
S = {s['slug']: s for s in sb.SERVICES}
STATS2 = [('30', 'Years in IT leadership'), ('10+', 'Acquisitions integrated'), ('30+', 'Sites networked worldwide'), ('$12M', 'Largest IT budget managed')]

def chart(cls='', labels=True, draw=False, vb='-34 -12 276 246'):
    grat = ''.join(f'<path class="grat" d="{p["d"]}"/>' for p in GRID['par'] if p['lat'] % 2 == 0) + ''.join(f'<path class="grat" d="{m["d"]}"/>' for m in GRID['mer'] if m['lon'] % 2 == 0)
    gl = ''
    if labels:
        for p in GRID['par']:
            if p['lat'] % 2 == 0 and 34 <= p['lat'] <= 42:
                y = float(p['d'].split(' L')[0].split()[1])
                gl += f'<text class="grat-t" x="-31" y="{y + 1.5:.1f}">{p["lat"]}°N</text>'
    rings = ''.join(f'<g transform="translate({CX} {CY}) scale({k}) translate({-CX} {-CY})"><path class="ring" d="{CA}" stroke-width="{.55 / k:.2f}" opacity="{op}"/></g>' for k, op in [])
    trees = (redwood(26, 66, 30, '#3c5c80', 1, wr=.42) + redwood(34, 70, 22, '#3c5c80', .8, wr=.42) + redwood(30.5, 75, 25, '#4a6d94', 1, wr=.42)
             + palm(140, 192, 26, '#3c5c80') + board(152, 193, 18, '#4a6d94'))
    pins = ''
    for (x, y), name, sub, lx, ly, anchor in [(ARCATA, 'Arcata', 'North Coast', 46, 12, 'start'), (HB, 'Huntington Beach', 'Headquarters', 168, 226, 'start')]:
        pins += f'<circle class="pin-halo" cx="{x}" cy="{y}" r="2.6"/><circle class="pin" cx="{x}" cy="{y}" r="2.6"/>'
        if labels:
            pins += f'<line class="lead-line" x1="{x + 2.5}" y1="{y - 1.5 if y < 100 else y + 1.5}" x2="{lx - 2}" y2="{ly - 2}"/><text class="pin-t" x="{lx}" y="{ly}" text-anchor="{anchor}">{name}</text><text class="pin-s" x="{lx}" y="{ly + 6}">{sub}</text>'
    return (f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="Map of California marking Arcata on the North Coast and Huntington Beach, our headquarters">'
            f'<g>{grat}{gl}</g><path class="land" d="{CA}"/>{rings}{trees}{pins}</svg>')


US = json.loads((ROOT / 'build' / 'us_chart.json').read_text())
def us_chart(cls=''):
    """Lower 48 in faint outline, California bright with contours, redwoods, two marks, and rings pulsing out from Huntington Beach."""
    cx, cy = US['cc']; hx, hy = US['hb']['x'], US['hb']['y']; ax, ay = US['ar']['x'], US['ar']['y']
    grat = ''.join(f'<path class="grat" d="{d}"/>' for d in US['grat'])
    rings = ''.join(f'<g transform="translate({cx} {cy}) scale({k}) translate({-cx} {-cy})"><path class="ring" d="{US["ca"]}" stroke-width="{.45 / k:.2f}" opacity="{op}"/></g>' for k, op in [])
    trees = (redwood(11.5, 86, 11, '#3c5c80', 1, wr=.42) + redwood(14.2, 87.5, 8, '#3c5c80', .8, wr=.42) + redwood(12.9, 89.2, 9, '#4a6d94', 1, wr=.42)
             + palm(40.5, 151.5, 10, '#4a6d94') + board(45.3, 151.8, 7, '#5a7ea6'))
    pulses = ''.join(f'<circle class="reach" cx="{hx}" cy="{hy}" r="12" style="animation-delay:{d}s"/>' for d in (0, 1.6, 3.2))
    pins = ''
    for (x, y), name, sub, lx, ly in [((ax, ay), 'Arcata', 'North Coast', 20, 52), ((hx, hy), 'Huntington Beach', 'Headquarters', 52, 186)]:
        pins += (f'<circle class="pin" cx="{x}" cy="{y}" r="1.7"/><line class="lead-line" x1="{x + 1.6}" y1="{y + (-1.2 if y < 100 else 1.2)}" x2="{lx - 1.5}" y2="{ly - 3}"/>'
                 f'<text class="pin-t us" x="{lx}" y="{ly}">{name}</text><text class="pin-s us" x="{lx}" y="{ly + 6.5}">{sub}</text>')
    legend = '<text class="us-leg" x="400" y="258" text-anchor="end">Remote support in all 50 states</text>'
    return (f'<svg class="{cls}" viewBox="-14 -6 428 270" role="img" aria-label="Map of the United States.  California is highlighted with marks at Arcata and at our Huntington Beach headquarters.  Rings spread from Huntington Beach across the country.">'
            f'<defs><clipPath id="usclip"><rect x="-14" y="-6" width="428" height="270"/></clipPath></defs>'
            f'<g>{grat}</g><path class="nation" d="{US["nation"]}"/><path class="borders" d="{US["borders"]}"/>'
            f'<g clip-path="url(#usclip)">{pulses}</g>'
            f'<path class="land" d="{US["ca"]}" style="stroke-width:.7"/>{rings}{trees}{pins}{legend}</svg>')


def palm(x, base, h, col, op=1):
    """A small palm: gently curved trunk, five fronds and a few dates.  (x, base) = foot of the trunk."""
    tx, ty = x + h * .16, base - h          # top of the trunk, leaning slightly seaward-right
    trunk = f'<path d="M{x:.2f} {base:.2f} Q{x + h * .02:.2f} {base - h * .55:.2f} {tx:.2f} {ty:.2f}" fill="none" stroke="{col}" stroke-width="{h * .085:.2f}" stroke-linecap="round"/>'
    fr = ''
    for dx, dy, cx, cy in [(-.55, .22, -.3, -.18), (-.38, -.1, -.22, -.3), (.05, -.28, .0, -.32), (.45, -.08, .25, -.3), (.6, .25, .35, -.15)]:
        ex, ey = tx + dx * h, ty + dy * h; qx, qy = tx + cx * h, ty + cy * h
        fr += f'<path d="M{tx:.2f} {ty:.2f} Q{qx:.2f} {qy:.2f} {ex:.2f} {ey:.2f}" fill="none" stroke="{col}" stroke-width="{h * .075:.2f}" stroke-linecap="round"/>'
    return f'<g opacity="{op}">{trunk}{fr}<circle cx="{tx:.2f}" cy="{ty + h * .05:.2f}" r="{h * .05:.2f}" fill="{col}"/></g>'

def board(x, base, h, col, op=1):
    """An upright surfboard with a center stringer.  (x, base) = tail."""
    w = h * .26
    body = f'<path d="M{x:.2f} {base:.2f} C{x - w:.2f} {base - h * .25:.2f} {x - w * .8:.2f} {base - h * .85:.2f} {x:.2f} {base - h:.2f} C{x + w * .8:.2f} {base - h * .85:.2f} {x + w:.2f} {base - h * .25:.2f} {x:.2f} {base:.2f}Z" fill="{col}"/>'
    stringer = f'<path d="M{x:.2f} {base - h * .06:.2f} L{x:.2f} {base - h * .94:.2f}" stroke="#0a1420" stroke-width="{h * .03:.2f}" opacity=".55"/>'
    return f'<g opacity="{op}">{body}{stringer}</g>'

def two_voice(h):
    """'Find the gaps <em>before someone else does</em>.' -> serif line, heavy line."""
    m = re.match(r'(.*?)<em>(.*?)</em>(.*)', h)
    if not m:
        return f'<span class="h-serif">{h}</span>'
    a, b, c = m.groups()
    return f'<span class="h-serif">{a.strip().rstrip(",")}</span><span class="h-heavy">{b}{c}</span>'

def phero(serif, heavy, lead, trail=None, mini=True):
    tr = f'<div class="trail">{trail}</div>' if trail else ''
    m = f'<div class="mini map">{chart(labels=False)}</div>' if mini else ''
    return f'''<section class="chart-sec phero on-dark"><div class="wrap"><div>{tr}<h1><span class="h-serif">{serif}</span><span class="h-heavy">{heavy}</span></h1><p class="lead">{lead}</p></div>{m}</div></section>'''

def page(fname, title, desc, body, extra_js='', hero_header=True):
    css, js = sb.ver('assets/css/cali.css'), sb.ver('assets/js/site.js')
    cur = lambda f: ' aria-current="page"' if f == fname or (fname in sb.SVC_FILES and f == 'services.html') else ''
    nav = ''.join(f'<a href="{f}"{cur(f)}>{n}</a>' for f, n in sb.NAV) + '<a class="talk" href="contact.html">Contact us</a>'
    svc_links = ''.join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in sb.SERVICES)
    canon = '' if fname == 'index.html' else fname
    full = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0f1c2d">
<link rel="canonical" href="https://caliit.com/{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Cali IT Consulting"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="https://caliit.com/{canon}"><meta property="og:image" content="https://caliit.com/assets/brand/og.png">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/bodoni-moda-latin-500-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/archivo-black-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/cali.css?v={css}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top{'' if hero_header else ' solid'}">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Cali IT Consulting, home">{sb.logo_dark()}</a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div><a class="brand" href="index.html" aria-label="Cali IT Consulting, home">{sb.logo_dark()}</a><p>Senior IT consulting, headquartered in Huntington Beach, California and serving clients across the United States.</p></div>
      <div><h4>Services</h4><ul>{svc_links}</ul></div>
      <div><h4>Company</h4><ul><li><a href="industries.html">Industries</a></li><li><a href="engagement.html">How we work</a></li><li><a href="why-us.html">Why us</a></li><li><a href="about.html">About</a></li><li><a href="testimonials.html">Testimonials</a></li></ul></div>
      <div><h4>Get in touch</h4><ul><li><a href="contact.html">Contact us</a></li><li><a href="why-us.html#check">Free IT health check</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="base"><span>&copy; {sb.YEAR} Cali IT Consulting</span><span>Huntington Beach, California</span></div>
  </div>
</footer>
<script src="assets/js/site.js?v={js}" defer></script>
{extra_js}
</body>
</html>
'''
    (ROOT / fname).write_text(full)

CUBE_JS = lambda: f'<script src="assets/js/cube.js?v={sb.ver("assets/js/cube.js")}" defer></script>'

# ---------- shared blocks ----------
def index_block(head=True):
    rows = ''.join(f'<li data-name="{s["name"]}"><a href="{s["slug"]}.html"><span class="nm">{s["name"]}</span><span class="ds">{s["short"]}</span></a></li>' for s in sb.SERVICES)
    h = '<div class="index-head"><h2>Nine practice areas, one team.</h2><p class="lead" style="margin-top:16px">Bring us a single project or hand us the whole stack.  Point at a service to turn the cube, or open it to read more.</p></div>' if head else ''
    return f'''<section class="index-sec on-dark"><div class="wrap">
  <div>{h}<ul class="svc-list" id="svcList">{rows}</ul></div>
  <div class="cube-col">
    <section class="stage" id="stage" aria-label="Rotating cube with one piece for each service.  Drag to spin it."><div class="glow"></div><div class="cube" id="cube"></div><div class="core"><div class="word" id="coreText" aria-live="polite"></div></div></section>
    <p class="cube-cap">Nine services, one cube.  Drag it to spin.</p>
    <div class="picker-hidden" id="picker" aria-hidden="true"></div>
  </div>
</div></section>'''

def ledger_block():
    rows = [('FDA-regulated', 'IT controls, access reviews and change records for medical device, diagnostics and biotech companies, plus certified clinical labs.'),
            ('SOX', 'IT general controls: testing, evidence and reporting for publicly traded companies, every audit cycle.'),
            ('HIPAA and GDPR', 'Data protection readiness, access by role and documented handling of patient and personal data.'),
            ('ISO 9001, 14001, 27001', 'IT support for quality, environmental and information security audits at global manufacturers.'),
            ('Physical security', 'Badge access, cameras and visitor logs tied to user accounts, so access ends the day someone leaves.')]
    trs = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rows)
    return f'''<section class="ledger-sec"><div class="wrap">
  <div><h2>For businesses that answer to auditors.</h2><p class="lead" style="margin-top:20px">Most IT shops stop at HIPAA.  Our team has run IT where a change isn't finished until it is documented, approved and provable.</p><p><a class="link" href="industries.html">See the industries we serve</a></p></div>
  <table class="ledger"><caption class="hp">Standards and environments we support</caption><tbody>{trs}</tbody></table>
</div></section>'''

def run_block():
    rows = [('Core infrastructure', 'Servers, storage, virtualization, networks, Wi-Fi and the links between sites.  Data centers and colocation, designed, built, moved and kept running.'),
            ('Licensing', 'Microsoft 365 and software licensing reviewed, right-sized and kept that way.  Renewals, true-ups and vendor contracts negotiated so you stop paying for seats nobody uses.'),
            ('IT operations', 'The day-to-day: users, devices, patching, monitoring, backups, onboarding and offboarding, vendors and documentation.  Run the same way every time.'),
            ('Facilities', 'When the building is part of the job: office moves and build-outs, server room power and cooling, badge access and cameras.'),
            ('Compliance', 'When audits come, the evidence is ready: SOX, HIPAA, ISO and FDA-regulated environments.')]
    trs = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rows)
    return f'''<section class="ledger-sec"><div class="wrap">
  <div><h2>What we run.</h2><p class="lead" style="margin-top:20px">Our specialty is the core of IT: the infrastructure, the licenses and the day-to-day operations that keep a business moving.  Facilities and compliance come along when the work calls for it.</p><p><a class="link" href="engagement.html">See how we work</a></p></div>
  <table class="ledger"><caption class="hp">What we run</caption><tbody>{trs}</tbody></table>
</div></section>'''

def notes_block(title='Field notes.', intro='A few of the projects behind the numbers.  Client names are kept confidential.'):
    notes = ''.join(f'<article class="note"><div class="where">{k}</div><div><h3>{t}</h3><p>{d}</p></div><div class="out">{b}</div></article>' for k, t, d, b in sb.RESULTS)
    return f'<section class="notes-sec"><div class="wrap"><h2>{title}</h2><p class="lead" style="margin:18px 0 44px">{intro}</p>{notes}</div></section>'

def compare_block(intro=True):
    heads = ''.join(f'<th scope="col">{t}<span>{s}</span></th>' for t, s, *_ in sb.ENGAGE)
    def row(label, fn):
        return f'<tr><th scope="row">{label}</th>' + ''.join(f'<td data-col="{e[0]}">{fn(e)}</td>' for e in sb.ENGAGE) + '</tr>'
    ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    body = row('How it works', lambda e: e[2]) + row("What's included", lambda e: ul(e[3])) + row('Typical work', lambda e: ul(e[4])) + row('Best for', lambda e: e[5][0].upper() + e[5][1:] + '.')
    i = '<h2>Three ways to work with us.</h2><p class="lead" style="margin-top:18px">Start with one and add another later.  Many clients fix the foundation with a project, then keep it that way with managed support.</p>' if intro else ''
    return f'<section class="compare-sec"><div class="wrap">{i}<table class="compare"><thead><tr><td></td>{heads}</tr></thead><tbody>{body}</tbody></table></div></section>'

def standard_block():
    ps = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for _, t, d in sb.STANDARD)
    return f'<section class="standard-sec on-dark" id="standard"><div class="wrap"><h2>Our standard, in writing.</h2><p class="lead" style="margin-top:18px">Six commitments we hold ourselves to on every engagement, large or small.</p><div class="promises">{ps}</div></div></section>'

def quote_block(i=0):
    q, c = sb.QUOTES[i]
    return f'<section class="quote-sec"><div class="wrap"><figure style="margin:0"><blockquote>{q}</blockquote><figcaption>{c}.  <a class="link" href="testimonials.html">Read the testimonials</a></figcaption></figure></div></section>'

def form(dark=True):
    opts = ''.join(f'<option>{E(t)}</option>' for t in sb.TOPICS)
    sizes = ''.join(f'<option>{t}</option>' for t in ['1 to 10 people', '11 to 50 people', '51 to 200 people', '200+ people'])
    return f'''<form class="form{'' if dark else ' light'}" id="contactForm" novalidate>
  <div class="row"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required maxlength="120"></div><div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization" maxlength="160"></div></div>
  <div class="row"><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="200"></div><div class="field"><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="40"></div></div>
  <div class="row"><div class="field"><label for="f-topic">What can we help with?</label><select id="f-topic" name="topic" required><option value="">Choose one</option>{opts}</select></div><div class="field"><label for="f-size">Company size</label><select id="f-size" name="size"><option value="">Choose one</option>{sizes}</select></div></div>
  <div class="field"><label for="f-msg">Tell us what's going on</label><textarea id="f-msg" name="message" required maxlength="5000"></textarea></div>
  <div class="hp" aria-hidden="true"><label for="f-hp">Leave this empty</label><input id="f-hp" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div><button class="btn{'' if dark else ' ink'}" type="submit">Send message</button></div>
  <p class="form-msg" id="formMsg" role="alert" hidden></p>
  <p class="form-note">A senior consultant replies within one business day.  We only use your details to reply.  <a href="privacy.html" style="color:inherit">Privacy policy</a>.</p>
</form>'''

def close_block():
    st = f'<svg class="close-state" viewBox="0 0 200 220" aria-hidden="true"><path d="{CA}" fill="#8fb3d9"/></svg>'
    return f'''<section class="chart-sec close-sec on-dark" id="talk">{st}<div class="wrap">
  <div><h2>Tell us what you're working on.</h2><p class="lead" style="margin-top:20px">An audit on the calendar, an office move, a security worry or an IT person who just gave notice.  Send a few lines and we'll reply within one business day.</p>
  <p style="margin-top:28px;color:#8ea2b8;font-size:15px">Headquarters in Huntington Beach, California.<br>On-site across California.  Remote support in all 50 states.</p></div>
  {form(True)}
</div></section>'''

# ---------- pages ----------
def home():
    stats = ''.join(f'<div><strong>{n}</strong>{t}</div>' for n, t in STATS2)
    body = f'''
<section class="chart-sec hero on-dark"><div class="wrap">
  <div>
    <p class="kicker">Rooted in California.  Serving businesses nationwide.</p>
    <h1><span class="h-serif">Your IT, run right.</span><span class="h-heavy">Infrastructure, licensing and IT operations.</span></h1>
    <p class="lead">We manage the core of your IT: servers, networks, data centers, Microsoft 365 and the licenses and vendors behind them.  Thirty years of running IT operations, now working for you.</p>
    <div class="acts"><a class="btn" href="#talk">Contact us</a><a class="btn line" href="services.html">See our services</a></div>
    <p class="reach-note">On-site across California.  Remote support in all 50 states.</p>
  </div>
  <div class="map us">{us_chart(cls='draw')}</div>
</div><p class="chart-note">Red marks show our California home base.  We support clients in every state.</p></section>

<section class="statement"><div class="wrap">
  <p class="big">For <b>thirty years</b> we've built and run the infrastructure behind growing companies: the servers, the networks, the data centers, the licenses and the vendors.  Now we run it for you.</p>
  <div class="margin">{stats}</div>
</div></section>

{run_block()}
{index_block()}
{notes_block()}
{compare_block()}
{standard_block()}
{quote_block(1)}
{close_block()}'''
    page('index.html', 'Cali IT Consulting | IT infrastructure, licensing and operations, nationwide', "Cali IT Consulting manages core IT infrastructure, software licensing and day-to-day IT operations: servers, networks, data centers, Microsoft 365 and vendors.  Headquartered in Huntington Beach, California, serving clients nationwide.", body, CUBE_JS())

def services():
    body = phero('Everything your IT needs,', 'under one roof.', 'Nine practice areas, one team.  Bring us a single project or hand us the whole stack.') + index_block(head=False) + f'''
<section class="band white"><div class="wrap two">
  <div><h2>Not sure where to start?  Start with an assessment.</h2><p class="lead" style="margin-top:18px">We review your environment, rank the risks and hand you a written plan.  You decide what to fix, and who fixes it.</p><p style="margin-top:26px"><a class="btn ink" href="contact.html?topic=IT%20and%20security%20assessment">Ask about an assessment</a></p></div>
  <ul class="ticks"><li>Microsoft 365 and identity security</li><li>Backups and recovery</li><li>Network, firewall and Wi-Fi</li><li>Licensing and vendor spend</li><li>Compliance gaps and evidence</li><li>A ranked, written remediation plan</li></ul>
</div></section>
{close_block()}'''
    page('services.html', 'Services | Cali IT Consulting', 'Microsoft 365, cybersecurity, network, cloud, data center, compliance, access control, business automation and IT strategy, for clients nationwide.', body, CUBE_JS())

def service(i, s):
    m = re.match(r'(.*?)<em>(.*?)</em>(.*)', s['h']); a, b, c = m.groups()
    sym = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in s['pains'])
    ct, cs, cl, co = s['case']
    prev, nxt = sb.SERVICES[i - 1], sb.SERVICES[(i + 1) % len(sb.SERVICES)]
    body = phero(a.strip().rstrip(','), b + c, s['intro'], trail=f'<a href="services.html">Services</a> / {s["name"]}') + f'''
<section class="band white"><div class="wrap"><h2>Sound familiar?</h2><div class="symptoms">{sym}</div></div></section>
<section class="band fog"><div class="wrap two">
  <div><h2>What you get.</h2><ul class="ticks" style="margin-top:30px">{''.join(f'<li>{g}</li>' for g in s['get'])}</ul>
  <p style="margin-top:30px"><a class="btn ink" href="contact.html?topic={E(s["name"])}">Talk to us about {s["name"]}</a></p></div>
  <div><article class="story"><p style="color:#8fb3d9;font-weight:600;margin-bottom:10px">From the field</p><h3>{ct}</h3><p>{cs}</p><ul class="ticks on-dark" style="border-top-color:#8fb3d9">{''.join(f'<li>{x}</li>' for x in cl)}</ul><div class="out">{co}</div></article>
  <p class="fine">Client names are kept confidential.</p>
  <h3 style="margin-top:34px">Platforms and standards</h3><p class="inline-list" style="margin-top:10px">{''.join(f'<span>{p}</span>' for p in s['plat'])}</p></div>
</div></section>
<section class="band white"><div class="wrap"><nav class="next-prev" aria-label="More services"><a href="{prev['slug']}.html"><small>Previous service</small><b>{prev['name']}</b></a><a href="{nxt['slug']}.html" style="text-align:right"><small>Next service</small><b>{nxt['name']}</b></a></nav></div></section>
{close_block()}'''
    page(s['slug'] + '.html', f'{s["name"]} | Cali IT Consulting', f'{s["name"]} from Cali IT Consulting, serving clients nationwide.  {s["intro"].split("  ")[0]}', body)

def industries():
    rows = ''.join(f'<article class="ind"><div><h3>{t}</h3><p>{d}</p></div><ul class="ticks">{"".join(f"<li>{x}</li>" for x in l)}</ul></article>' for _, t, d, l in sb.INDUSTRIES)
    body = phero('IT for businesses', 'that answer to someone.', 'Regulators, auditors, clients or a board.  Our team has run IT where downtime and audit findings are not an option.') + f'''
<section class="band white"><div class="wrap">{rows}</div></section>
{ledger_block()}
{close_block()}'''
    page('industries.html', 'Industries | Cali IT Consulting', 'IT consulting for life sciences, FDA-regulated companies, clinical labs, manufacturing, finance and growing companies.', body)

def engagement():
    steps = [('Send us a message', "Tell us what's going on through the contact form.  We reply within one business day."), ('Get a written proposal', 'A clear scope, timeline and price, in plain English.'), ('Kick off', 'We get to work, keep you posted and document everything as we go.'), ('Hand-off or ongoing', 'Projects end with documentation you own.  Managed and fractional work continue month to month.')]
    st = ''.join(f'<div><h3><span style="font:400 15px var(--heavy);color:#8fb3d9;display:block;margin-bottom:8px">Step {n}</span>{t}</h3><p>{d}</p></div>' for n, (t, d) in enumerate(steps, 1))
    body = phero('Work with us', 'the way that fits.', 'One job, ongoing support or a senior IT leader part time.  Start with one, add another later.') + compare_block(intro=False) + f'''
<section class="standard-sec on-dark"><div class="wrap"><h2>How an engagement starts.</h2><div class="promises four">{st}</div></div></section>
{standard_block().replace('standard-sec on-dark', 'band white').replace('class="promises"', 'class="promises light-p"')}
{close_block()}'''
    page('engagement.html', 'How We Work | Cali IT Consulting', 'Projects, managed support or fractional IT leadership.  Written scope and price before work starts.', body)

def why():
    qs = ''.join(f'<li data-q="{i}"><p>{q}</p><div class="yn"><button type="button" data-v="1" aria-pressed="false">Yes</button><button type="button" data-v="0" aria-pressed="false">No</button></div></li>' for i, q in enumerate(sb.QUESTIONS))
    pains = ''.join(f'<li><a href="{s}.html"><span class="nm" style="font:italic 500 clamp(20px,2vw,26px)/1.25 var(--serif)">{t}</span><span class="ds">{sb.SVC[s]["name"]}</span></a></li>' for t, s in sb.PAINS)
    body = phero('Why teams', 'choose Cali IT.', "Thirty years of running IT inside companies where downtime and audit findings aren't an option.") + f'''
<section class="band white" id="check"><div class="wrap">
  <h2>The 60-second IT health check.</h2><p class="lead" style="margin-top:16px">Six honest questions.  No email required, and your answers stay in your browser.</p>
  <div class="check"><ol class="questions" id="questions">{qs}</ol>
  <div class="score"><div class="n" id="gaugeNum">0<small> of {len(sb.QUESTIONS)}</small></div><h3 id="verdictTitle">Answer the questions</h3><p id="verdictText">Every "No" is a gap worth closing.  Most businesses we meet have at least two.</p><a class="btn" id="checkCta" href="contact.html" hidden>Send us your results</a></div></div>
</div></section>
<section class="index-sec on-dark"><div class="wrap" style="grid-template-columns:1fr"><div><div class="index-head"><h2>If you nodded at any of these, we should talk.</h2></div><ul class="svc-list">{pains}</ul></div></div></section>
{notes_block()}
{standard_block()}
{close_block()}'''
    page('why-us.html', 'Why Us | Cali IT Consulting', 'Senior IT consultants with 30 years of experience in regulated companies.  Take the free 60-second IT health check.', body)

def about():
    vals = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in [('Straight answers', "Plain English, no jargon.  If something doesn't need fixing, we'll say so."), ('Senior people', 'The people who scope your project are the ones who do the work.'), ('Documented', "Every change is written down, so you're never locked in to us."), ('Built to last', 'We design for the next five years, not the next invoice.')])
    stats = ''.join(f'<div><strong>{n}</strong>{t}</div>' for n, t in STATS2)
    body = phero('Built by people', 'who ran IT, not just sold it.', "Cali IT Consulting brings 30 years of IT leadership to businesses that can't afford downtime.") + f'''
<section class="statement"><div class="wrap">
  <p class="big">Our team has run technology for FDA-regulated medical device and diagnostics companies, global manufacturers and growing firms, from the North Coast to Huntington Beach and across the country.</p>
  <div class="margin">{stats}</div>
</div></section>
<section class="band fog"><div class="wrap two">
  <div><h2>What we do.</h2></div>
  <div class="prose"><p class="lead">We've led more than ten acquisitions, moved headquarters and data centers, built certified labs, and passed SOX, HIPAA and ISO audits.</p><p>We handle Microsoft 365, cybersecurity, networks, cloud, data centers, physical security, compliance and IT strategy.  We work on-site across California and support clients remotely in all 50 states, traveling on-site when the job needs it.  You get senior-level answers from people who have done the work, not a sales pitch.</p></div>
</div></section>
<section class="standard-sec on-dark"><div class="wrap"><h2>What we stand for.</h2><div class="promises">{vals}</div></div></section>
{notes_block()}
{quote_block(2)}
{close_block()}'''
    page('about.html', 'About | Cali IT Consulting', 'Cali IT Consulting: senior IT consultants with 30 years of leadership in regulated companies.  Headquartered in Huntington Beach, California, serving clients nationwide.', body)

def testimonials():
    rows = ''
    for t in sb.TESTIMONIALS:
        ps = ''.join(f'<p>{E(p)}</p>' for p in t['paras'])
        rows += f'<figure class="tq" style="margin:0"><figcaption class="who">{E(t["cap"][0])}<span>{E(t["cap"][1]) if len(t["cap"]) > 1 else ""}</span></figcaption><blockquote>{ps}</blockquote></figure>'
    body = phero('In their', 'own words.', 'What the people we have worked for, and alongside, have said about the work.  Quoted from LinkedIn recommendations, with names left out for privacy.') + f'<section class="band white"><div class="wrap tquotes">{rows}</div></section>{close_block()}'
    page('testimonials.html', 'Testimonials | Cali IT Consulting', 'What clients and colleagues say about working with the Cali IT Consulting team.', body)

def contact():
    body = phero('Tell us what', "you're working on.", 'Fill out the form and a senior consultant will get back to you within one business day.') + f'''
<section class="band white"><div class="wrap two">
  <div><h2>California headquarters.  Nationwide clients.</h2><ul class="ticks" style="margin-top:28px"><li>Headquarters in Huntington Beach, California</li><li>On-site across California</li><li>Remote support in all 50 states, and on-site travel when the job needs it</li><li>A reply from a senior consultant within one business day</li></ul></div>
  {form(False)}
</div></section>'''
    page('contact.html', 'Contact | Cali IT Consulting', 'Contact Cali IT Consulting.  California headquarters, clients nationwide.  A senior consultant will reply within one business day.', body)

def thanks():
    body = phero('Thanks.', 'We got your message.', 'A senior consultant will reply within one business day.') + '<section class="band white"><div class="wrap"><a class="btn ink" href="index.html">Back to the home page</a></div></section>'
    page('thanks.html', 'Thank you | Cali IT Consulting', 'Your message was sent.', body)

def privacy():
    src = (ROOT / 'privacy.html').read_text()
    prose = src[src.index('<div class="wrap prose">') + len('<div class="wrap prose">'):src.index('</div></section>', src.index('<div class="wrap prose">'))] if '<div class="wrap prose">' in src else ''
    body = phero('Privacy', 'policy.', f'Effective October 25, {sb.YEAR}.', mini=False) + f'<section class="band white"><div class="wrap prose">{prose}</div></section>'
    page('privacy.html', 'Privacy | Cali IT Consulting', 'How Cali IT Consulting handles information sent through this website.', body)

def notfound():
    body = phero('This page', 'is off the map.', "The page you're looking for isn't here.") + '<section class="band white"><div class="wrap"><a class="btn ink" href="index.html">Home page</a> &nbsp; <a class="link" href="services.html">Services</a></div></section>'
    page('404.html', 'Page not found | Cali IT Consulting', 'Page not found.', body)

if __name__ == '__main__':
    privacy()   # reads the current privacy text first
    home(); services(); [service(i, s) for i, s in enumerate(sb.SERVICES)]; industries(); engagement(); why(); about(); testimonials(); contact(); thanks(); notfound()
    print('built field-chart site')
