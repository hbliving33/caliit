"""Cali IT Consulting site, "field chart" design.  Content comes from site_build.py; this file owns the layout.
Run from the repo root:  python3 build/site2_build.py"""
from urllib.parse import quote
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
sb.SERVICES.append(dict(slug='ai', name='AI', h='Put AI to work, <em>safely and on purpose</em>.', short='Copilot readiness, AI policies and guardrails, and practical automation that saves real time.',
  intro="AI is only as safe as the data it can reach.  We get your permissions, policies and people ready, then put AI to work where it actually saves time.",
  pains=[('Copilot sees too much', 'Old sharing links and loose permissions mean AI can surface files people were never meant to see.'), ('No rules yet', 'Staff are already pasting company data into free AI tools, and nobody has said what is allowed.'), ('Pilots that go nowhere', 'A few licenses were bought, a few people tried it, and nobody can say what it is worth.')],
  get=['Microsoft 365 Copilot readiness review', 'SharePoint and OneDrive permission cleanup before AI is turned on', 'AI acceptable use policy and guardrails', 'Tool selection and a pilot with clear goals', 'AI-assisted automation in Power Automate and Copilot Studio', 'Staff training on using AI well and safely'],
  plat=['Microsoft 365 Copilot', 'Copilot Studio', 'Power Automate', 'Azure OpenAI', 'SharePoint and OneDrive', 'Entra ID', 'Sensitivity labels'],
  case=('Ready, then useful', 'Every AI engagement starts the same way, so you get value without surprises.', ['Review who can see what across Microsoft 365, and fix the oversharing', 'Write a short, plain-English AI policy your staff will follow', 'Pilot with a small team on two or three real tasks, then measure the time saved'], 'AI turned on with guardrails, and a clear answer on what it is worth.'),
  case_label='How we start', case_note=''))
sb.SERVICES.append(dict(slug='managed-it', name='Managed IT', h='Managed IT, <em>sized to fit</em>.', short='A right-sized MSP plan built around you: monitoring, patching, users and vendors, from a few systems to the whole stack.',
  intro="We're not a big-box managed service provider (MSP) with one plan for everyone.  We sit down with you, choose what we manage and how, and price it to fit.",
  pains=[('One-size contracts', 'The big MSPs sell a package, and you pay for what you never use.'), ('Tickets, not answers', 'Every call goes to a queue and a different person who has never seen your setup.'), ('Too small for in-house IT', 'You need someone watching the systems, but not a full-time hire.')],
  get=['Monitoring and patching for servers, network and devices', 'User onboarding and offboarding', 'Vendor and license management', 'Help when something breaks, from people who know your setup', 'A monthly review of what changed and what is next', 'A scope you can grow or shrink as you go'],
  plat=['Remote monitoring', 'Patch management', 'Microsoft 365', 'Intune', 'Cisco Meraki', 'UniFi', 'Cloud backup', 'Co-managed IT'],
  case=('Built around you', 'Every managed plan starts with a short conversation, not a price sheet.', ['We list what you have and what matters most', 'You choose what we manage, from a few key systems to the whole stack', 'We agree on response times and a monthly price, in writing'], 'MSP-style coverage, without a one-size contract.'),
  case_label='How it works', case_note=''))
sb.SERVICES.append(dict(slug='business-applications', name='Business Applications', h='Every app, <em>with an owner</em>.', short='ERP, HR and payroll, CRM and quality systems: single sign-on, access by role, licenses and renewals, managed.',
  intro="Your business runs on a stack of apps: ERP, HR and payroll, CRM, quality and document systems.  We give every one an owner, put sign-in through one identity, and keep access, licenses and renewals under control.",
  pains=[('Nobody owns the apps', 'Each department bought its own tools, and IT finds out when something breaks or the invoice arrives.'), ('Logins everywhere', 'Every app has its own password, and nobody is sure who still has access after someone leaves.'), ('Renewals on autopilot', 'Contracts renew themselves, seat counts only go up, and no one has compared what you pay to what you use.')],
  get=['Administration for ERP, HR and payroll, CRM and quality systems', 'Single sign-on and automatic user provisioning through Entra ID', 'Roles and permissions set by job, with regular access reviews', 'One onboarding and offboarding checklist across every app', 'An app inventory with owners, costs and renewal dates', 'License and renewal reviews before the contract auto-renews', 'App selection, rollout and vendor management, start to finish'],
  plat=['NetSuite', 'Oracle', 'ADP', 'MasterControl', 'HubSpot', 'Pipedrive', 'Entra ID single sign-on', 'SCIM provisioning'],
  case=('One owner for the whole stack', 'A diagnostics company ran its ERP, payroll, CRM and quality systems with separate logins and no single owner.', ['Took over ERP administration: roles, approvals and license types', 'Connected the HR and payroll platform to Entra ID for single sign-on', 'Earlier led an Oracle ERP rollout alongside acquisition integrations for a large manufacturer'], 'Every app with an owner, access set by role, and renewals on a calendar.'),
  desc='Business application management: ERP, HR and payroll, CRM and quality systems, with single sign-on, access by role and license control.'))
sb.TOPICS.insert(sb.TOPICS.index('Something else'), 'AI'); sb.TOPICS.insert(sb.TOPICS.index('Something else'), 'Managed IT'); sb.TOPICS.insert(sb.TOPICS.index('Microsoft 365') + 1, 'Business Applications')
ORDER = ['network', 'cloud', 'data-center', 'microsoft-365', 'business-applications', 'ai', 'managed-it', 'it-strategy', 'cybersecurity', 'business-automation', 'access-control', 'compliance']
sb.SERVICES.sort(key=lambda x: ORDER.index(x['slug']))
for _x in sb.SERVICES:
    if _x['slug'] == 'cloud': _x['short'] = 'Azure and hybrid servers, storage and virtualization, with backups you have tested.'
    if _x['slug'] == 'microsoft-365': _x['short'] = 'Identity first, then email, SharePoint/OneDrive and Teams, with devices, file permissions and licensing set up right and kept clean.'
    if _x['slug'] == 'cybersecurity': _x['short'] = 'Penetration testing, risk assessments, MFA, email gateway security and a plan for a bad day.'
    if _x['slug'] == 'access-control': _x['short'] = 'Badge access, security cameras and monitoring for every door and every site.'
    if _x['slug'] == 'it-strategy': _x['short'] = 'IT operations leadership, repeatable processes, roadmaps, budgets and vendor management.'
# ---- launch refresh (Oct 2026): current terms, identity first, unique meta descriptions ----
def _upd(slug, **kw):
    for _x in sb.SERVICES:
        if _x['slug'] == slug: _x.update(kw)
_upd('network', desc='Network design and support: firewalls, switching, Wi-Fi, SD-WAN, site-to-site VPN and zero trust remote access, documented and monitored.',
     get=['Network design from core to edge', 'Firewall, switching and Wi-Fi installs', 'Site-to-site VPN and SD-WAN between offices, labs and plants', 'Remote access, from VPN to zero trust (ZTNA)', 'Office moves and new building cutovers', 'Guest Wi-Fi kept separate from your business network', 'Monitoring and documentation you keep'],
     plat=['Cisco Meraki', 'UniFi', 'SD-WAN', 'Site-to-site VPN', 'ZTNA', 'Wi-Fi', 'Phone systems', 'Network monitoring'])
_upd('cloud', desc='Servers, storage, virtualization and backup: Azure and hybrid design, VMware and Hyper-V, immutable offsite backups and tested disaster recovery.',
     get=['Cloud readiness review and migration plan', 'Azure and hybrid server design', 'Virtualization and storage: VMware, Hyper-V and NetApp', 'Immutable, offsite backups with tested restores', 'Disaster recovery with recovery times agreed in writing', 'Cloud cost reviews'],
     plat=['Azure', 'VMware', 'Hyper-V', 'NetApp', 'Dell', 'HP', 'Synology', 'Immutable backups', 'Colocation'])
_upd('data-center', desc='Data center and server room design, colocation selection and moves: power, cooling, racks and cabling, with a cutover and rollback plan.')
_upd('microsoft-365', h='Your workplace, <em>secured from the sign-in up</em>.',
     intro='Microsoft 365 starts with identity: who can sign in, from where, on what device.  Then email, files and meetings.  We set it up right, secure it, and keep licensing under control.',
     get=['Identity first: Entra ID, phishing-resistant MFA, passkeys and conditional access', 'Tenant security review with a ranked fix list, tracked in Secure Score', 'Exchange Online, Teams, SharePoint and OneDrive migrations', 'SharePoint and OneDrive sharing and permissions cleaned up and kept that way', 'Devices enrolled and managed with Intune and Autopilot', 'Licensing review and cleanup', 'Standard onboarding and offboarding for every user'],
     plat=['Entra ID', 'Conditional access', 'Passkeys', 'Exchange Online', 'Teams', 'SharePoint', 'OneDrive', 'Intune', 'Autopilot'],
     desc='Microsoft 365, identity first: Entra ID, phishing-resistant MFA and conditional access, then Exchange Online, SharePoint, OneDrive, Teams, Intune and licensing.')
_upd('ai', get=['Microsoft 365 Copilot readiness review', 'SharePoint and OneDrive oversharing cleanup before AI is turned on', 'Shadow AI check: which AI tools staff already use, and with what data', 'AI acceptable use policy and guardrails', 'Tool selection and a pilot with clear goals', 'Agents and automation in Copilot Studio and Power Automate', 'Staff training on using AI well and safely'],
     desc='AI readiness for Microsoft 365: Copilot readiness, oversharing cleanup, shadow AI checks, AI policies and practical agents in Copilot Studio.')
_upd('managed-it', desc='Managed IT sized to fit: monitoring, patching, users, devices and vendors, fully managed or co-managed alongside your own IT staff.')
_upd('it-strategy', intro='Fractional CIO and IT director support for companies that need a senior IT voice without a full-time hire.  Roadmaps, budgets, vendors, written processes and the hard calls.',
     desc='Fractional CIO and IT leadership: technology roadmaps, IT budgets, written processes, vendor contracts, M&A integration and board reporting.')
_upd('cybersecurity', get=['Penetration testing, including autonomous pentesting, and vulnerability scanning', 'Security assessment with a ranked remediation plan', 'Phishing-resistant MFA and conditional access for every account', 'Endpoint protection (EDR) and managed detection (MDR) chosen and set up with the right partner', 'Email gateway security and phishing defenses', 'Security awareness training for staff', 'Board and audit committee cybersecurity briefings: risks, progress and what is next', 'Incident response plan and tabletop exercise', 'Hands-on help when an incident happens'],
     plat=['Penetration testing', 'EDR and MDR', 'Email gateway', 'Entra ID', 'Conditional access', 'Passkeys', 'Intune', 'Security awareness training'],
     desc='Cybersecurity based on risk: penetration testing, phishing-resistant MFA, EDR and MDR, email security, staff training and an incident response plan.')
_upd('business-automation', desc='Business automation with Power Apps, Power Automate and CRM workflows: approvals, handoffs and data entry done by the system, not by people.')
_upd('access-control', desc='Physical security that works with IT: badge access, security cameras, visitor management and monitoring, shut off the day someone leaves.')
_upd('compliance', get=['IT general controls for SOX', 'IT support for 21 CFR Part 11 and GxP: access, audit trails and change records', 'HIPAA and data protection readiness', 'Written policies and procedures that match reality', 'Evidence collection and audit support', 'Change management and access reviews', 'Support for FDA-regulated and certified lab environments'],
     plat=['SOX', '21 CFR Part 11', 'GxP', 'HIPAA', 'GDPR', 'ISO 9001', 'ISO 14001', 'ISO 27001', 'ITIL', 'CLIA labs'],
     desc='IT compliance for regulated companies: SOX IT general controls, 21 CFR Part 11 and GxP support, HIPAA, ISO audits and evidence that is ready on time.')
S = {s['slug']: s for s in sb.SERVICES}
TOPICS = ['A project or assessment', 'Ongoing IT support', 'Security or compliance', 'IT leadership and strategy', 'Something else']
TOPIC_OF = {'managed-it': 'Ongoing IT support', 'cybersecurity': 'Security or compliance', 'compliance': 'Security or compliance', 'access-control': 'Security or compliance', 'it-strategy': 'IT leadership and strategy'}   # everything else is a project
sb.SVC.update(S)
sb.PAINS.insert(sb.PAINS.index(next(x for x in sb.PAINS if x[1] == 'business-automation')), ('Nobody can say how many apps you pay for, or who still has access to them.', 'business-applications'))
STATS2 = [('30', 'Years in IT leadership'), ('10+', 'Acquisitions integrated'), ('50', 'States we support remotely'), ('$12M', 'Largest IT budget managed')]

def chart(cls='', labels=True, draw=False, vb='-34 -12 276 246'):
    grat = ''.join(f'<path class="grat" d="{p["d"]}"/>' for p in GRID['par'] if p['lat'] % 2 == 0) + ''.join(f'<path class="grat" d="{m["d"]}"/>' for m in GRID['mer'] if m['lon'] % 2 == 0)
    gl = ''
    if labels:
        for p in GRID['par']:
            if p['lat'] % 2 == 0 and 34 <= p['lat'] <= 42:
                y = float(p['d'].split(' L')[0].split()[1])
                gl += f'<text class="grat-t" x="-31" y="{y + 1.5:.1f}">{p["lat"]}°N</text>'
    rings = ''.join(f'<g transform="translate({CX} {CY}) scale({k}) translate({-CX} {-CY})"><path class="ring" d="{CA}" stroke-width="{.55 / k:.2f}" opacity="{op}"/></g>' for k, op in [])
    trees = (redwood(22.8, 74, 22, '#3c5c80', 1, wr=.42) + redwood(37.2, 74, 22, '#3c5c80', 1, wr=.42) + redwood(30, 74, 29, '#46688e', 1, wr=.42)   # three redwoods: equal flanks, taller center, one base line
             + wave(104, 180, 16, '#4a6d94'))
    pins = ''
    for (x, y), name, sub, lx, ly, anchor in [(ARCATA, 'Arcata', 'Remote office', 46, 12, 'start'), (HB, 'Huntington Beach', 'Headquarters', 168, 226, 'start')]:
        pins += f'<circle class="pin-halo" cx="{x}" cy="{y}" r="2.6"/><circle class="pin" cx="{x}" cy="{y}" r="2.6"/>'
        if labels:
            pins += f'<line class="lead-line" x1="{x + 2.5}" y1="{y - 1.5 if y < 100 else y + 1.5}" x2="{lx - 2}" y2="{ly - 2}"/><text class="pin-t" x="{lx}" y="{ly}" text-anchor="{anchor}">{name}</text><text class="pin-s" x="{lx}" y="{ly + 6}">{sub}</text>'
    return (f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="Map of California marking our Arcata remote office and Huntington Beach headquarters">'
            f'<g>{grat}{gl}</g><path class="land" d="{CA}"/>{rings}{trees}{pins}</svg>')


US = json.loads((ROOT / 'build' / 'us_chart.json').read_text())
DE = json.loads((ROOT / 'build' / 'de_inset.json').read_text())
DE_CITY = None   # set to a key in DE['cities'] once confirmed   # Germany inset: we support clients there today
def us_chart(cls=''):
    """Lower 48 in outline, California highlighted with redwoods, wave and board, two marks, and live-looking links:
    arcs from Huntington Beach to cities across the country with light traveling along them."""
    hx, hy = US['hb']['x'], US['hb']['y']; ax, ay = US['ar']['x'], US['ar']['y']
    grat = ''.join(f'<path class="grat" d="{d}"/>' for d in US['grat'])
    trees = (redwood(10.2, 88, 8.5, '#6f97c4', 1, wr=.42) + redwood(15.8, 88, 8.5, '#6f97c4', 1, wr=.42) + redwood(13, 88, 11, '#8db3dc', 1, wr=.42)   # same three, scaled down; lighter so they read on the bluer map
             + wave(30, 145.5, 6, '#8db3dc'))
    arcs = nodes = packets = ''
    for i, (name, (x, y)) in enumerate(US['cities'].items()):
        mx, my = (hx + x) / 2, (hy + y) / 2
        lift = ((x - hx) ** 2 + (y - hy) ** 2) ** .5 * .28
        d = f'M{hx} {hy} Q{mx:.1f} {my - lift:.1f} {x} {y}'
        arcs += f'<path class="arc" d="{d}"/>'
        nodes += f'<circle class="node" cx="{x}" cy="{y}" r="1.5" style="animation-delay:{(i * .37) % 3:.2f}s"/>'
        dur = 2.4 + (i % 4) * .45
        packets += f'<circle class="packet" r="1.25"><animateMotion dur="{dur:.2f}s" begin="{2.4 + i * .3:.1f}s" repeatCount="indefinite" path="{d}"/></circle>'
    pins = ''
    for (x, y), name, sub, lx, ly in [((ax, ay), 'Arcata', 'Remote office', 20, 52), ((hx, hy), 'Huntington Beach', 'Headquarters', 52, 192), (tuple(US['payson']), 'Payson, Arizona', 'Remote office', 95, 150)]:
        pins += (f'<circle class="pin-halo" cx="{x}" cy="{y}" r="1.8"/><circle class="pin" cx="{x}" cy="{y}" r="1.8"/><line class="lead-line" x1="{x + 1.6}" y1="{y + (-1.2 if y < 100 else 1.2)}" x2="{lx - 1.5}" y2="{ly - 3}"/>'
                 f'<text class="pin-t us" x="{lx}" y="{ly}">{name}</text><text class="pin-s us" x="{lx}" y="{ly + 6.5}">{sub}</text>')
    return (f'<svg class="{cls}" viewBox="-14 -6 428 270" role="img" aria-label="Map of the United States.  California is highlighted with marks at our Huntington Beach headquarters and our Arcata remote office, plus a mark at Payson, Arizona, and an inset for Germany, where we also support clients.  Lines run from Huntington Beach to cities across the country.">'
            f'<defs><clipPath id="usgrat"><rect x="-14" y="-6" width="428" height="270"/></clipPath></defs><g clip-path="url(#usgrat)">{grat}</g><path class="nation" d="{US["nation"]}"/><path class="borders" d="{US["borders"]}"/>'
            f'<path class="land" d="{US["ca"]}" style="stroke-width:.7"/>{trees}<g class="links">{arcs}{nodes}{packets}</g>{pins}{germany(DE_CITY)}</svg>')

def germany(city=None):
    cx, cy = DE['cx'], DE['cy']; r = 24
    dot = ''
    if city:
        x, y = DE['cities'][city]
        dot = f'<circle class="pin-halo" cx="{x}" cy="{y}" r="1.6"/><circle class="pin" cx="{x}" cy="{y}" r="1.6"/>'
    d = f'M360.9 85.4 Q{cx + 6} {cy - 62} {cx} {cy - r - 1}'
    return (f'<g class="de-inset"><path class="arc" d="{d}"/><circle class="packet" r="1.25"><animateMotion dur="3.2s" begin="3s" repeatCount="indefinite" path="{d}"/></circle>'
            f'<circle class="de-ring" cx="{cx}" cy="{cy}" r="{r}"/><path class="land de" d="{DE["d"]}"/>{dot}'
            f'<text class="pin-t us" x="{cx}" y="{cy + r + 8}" text-anchor="middle">Germany</text><text class="pin-s us" x="{cx}" y="{cy + r + 14.5}" text-anchor="middle">Remote support</text></g>')

CHIPS = [('Chicago', ['Microsoft 365', 'Identity', 'Exchange Online', 'SharePoint', 'OneDrive', 'Teams', 'Single sign-on', 'Mail migration']),
         ('NewYork', ['Cybersecurity', 'Entra ID', 'MFA', 'Conditional access', 'Zero trust', 'Intune', 'Penetration testing', 'Email security']),
         ('Miami', ['Cloud backup', 'Azure', 'VMware', 'Hyper-V', 'NetApp', 'Synology', 'Disaster recovery', 'Data center']),
         ('Dallas', ['Cisco Meraki', 'Firewalls', 'Site-to-site VPN', 'UniFi', 'SD-WAN', 'Wi-Fi', 'Dell and HP servers', 'Network monitoring']),
         ('Atlanta', ['Power Automate', 'NetSuite', 'ADP', 'MasterControl', 'HubSpot', 'Pipedrive', 'Patch management', 'Help desk', 'Asset management', 'Onboarding'])]
def us_map_block():
    chips = ''
    for i, (city, words) in enumerate(CHIPS):
        x, y = US['cities'][city]
        chips += f'<span class="chip" data-words="{"|".join(words)}" style="left:{(x + 14) / 428 * 100:.2f}%;top:{(y + 6) / 270 * 100:.2f}%;--i:{i}">{words[0]}</span>'
    return f'<div class="map us">{us_chart(cls="draw")}<div class="chips" aria-hidden="true">{chips}</div><p class="map-cap">Remote support in all 50 states</p></div>'

def palm(x, base, h, col, op=1):
    """A small palm: gently curved trunk, five fronds and a few dates.  (x, base) = foot of the trunk."""
    tx, ty = x + h * .16, base - h          # top of the trunk, leaning slightly seaward-right
    trunk = f'<path d="M{x:.2f} {base:.2f} Q{x + h * .02:.2f} {base - h * .55:.2f} {tx:.2f} {ty:.2f}" fill="none" stroke="{col}" stroke-width="{h * .085:.2f}" stroke-linecap="round"/>'
    fr = ''
    for dx, dy, cx, cy in [(-.55, .22, -.3, -.18), (-.38, -.1, -.22, -.3), (.05, -.28, .0, -.32), (.45, -.08, .25, -.3), (.6, .25, .35, -.15)]:
        ex, ey = tx + dx * h, ty + dy * h; qx, qy = tx + cx * h, ty + cy * h
        fr += f'<path d="M{tx:.2f} {ty:.2f} Q{qx:.2f} {qy:.2f} {ex:.2f} {ey:.2f}" fill="none" stroke="{col}" stroke-width="{h * .075:.2f}" stroke-linecap="round"/>'
    return f'<g opacity="{op}">{trunk}{fr}<circle cx="{tx:.2f}" cy="{ty + h * .05:.2f}" r="{h * .05:.2f}" fill="{col}"/></g>'

def wave(x, base, h, col, op=1):
    """A small curling wave, sized like the trees.  (x, base) = left end of the wave's base line."""
    w = h * 1.5
    crest = (f'<path d="M{x:.2f} {base:.2f} C{x + w * .18:.2f} {base - h * .1:.2f} {x + w * .32:.2f} {base - h * .55:.2f} {x + w * .55:.2f} {base - h * .9:.2f} '
             f'C{x + w * .72:.2f} {base - h * 1.12:.2f} {x + w * .98:.2f} {base - h * .98:.2f} {x + w * .96:.2f} {base - h * .7:.2f} '
             f'C{x + w * .8:.2f} {base - h * .82:.2f} {x + w * .66:.2f} {base - h * .66:.2f} {x + w * .72:.2f} {base - h * .45:.2f} '
             f'C{x + w * .8:.2f} {base - h * .22:.2f} {x + w * .92:.2f} {base - h * .1:.2f} {x + w:.2f} {base:.2f}Z" fill="{col}"/>')
    foam = f'<path d="M{x + w * .58:.2f} {base - h * .78:.2f} C{x + w * .66:.2f} {base - h * .92:.2f} {x + w * .82:.2f} {base - h * .95:.2f} {x + w * .9:.2f} {base - h * .8:.2f}" fill="none" stroke="#8fb3d9" stroke-width="{h * .06:.2f}" stroke-linecap="round" opacity=".6"/>'
    return f'<g opacity="{op}">{crest}{foam}</g>'

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

def phero(serif, heavy, lead, trail=None, mini=False):   # inner pages: centered text, no map (the map lives on the home page)
    tr = f'<div class="trail">{trail}</div>' if trail else ''
    m = f'<div class="mini map us us-mini">{us_chart(cls="draw")}</div>' if mini else ''
    return f'''<section class="chart-sec phero on-dark{" has-map" if mini else ""}"><div class="wrap"><div>{tr}<h1><span class="h-serif">{serif}</span><span class="h-heavy">{heavy}</span></h1><p class="lead">{lead}</p></div>{m}</div></section>'''

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
      <div><a class="brand" href="index.html" aria-label="Cali IT Consulting, home">{sb.logo_dark()}</a><p>IT infrastructure and operations consulting.  Headquartered in Huntington Beach, California, serving clients across the United States.</p></div>
      <div><h4>Services</h4><ul>{svc_links}</ul></div>
      <div><h4>Company</h4><ul><li><a href="industries.html">Industries</a></li><li><a href="engagement.html">How we work</a></li><li><a href="why-us.html">Why us</a></li><li><a href="about.html">About</a></li><li><a href="testimonials.html">Testimonials</a></li><li><a href="news.html">Security news</a></li></ul></div>
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
    h = '<div class="index-head"><h2>Twelve practice areas, one team.</h2><p class="lead" style="margin-top:16px">Bring us a single project or hand us the whole stack.  Point at a service to turn the cube, or open it to read more.</p></div>' if head else ''
    return f'''<section class="index-sec on-dark"><div class="wrap">
  <div>{h}<ul class="svc-list" id="svcList">{rows}</ul></div>
  <div class="cube-col">
    <section class="stage" id="stage" aria-label="Rotating cube with one piece for each service.  Drag to spin it."><div class="glow"></div><div class="cube" id="cube"></div><div class="core"><div class="word" id="coreText" aria-live="polite"></div></div></section>
    <p class="cube-cap">Drag the cube to spin it.</p>
    <div class="picker-hidden" id="picker" aria-hidden="true"></div>
  </div>
</div></section>'''

def ledger_block():
    rows = [('FDA-regulated', 'IT controls, access reviews and change records for medical device, diagnostics and biotech companies, plus certified clinical labs.'),
            ('SOX', 'IT general controls: testing, evidence and reporting for publicly traded companies, every audit cycle.'),
            ('HIPAA and GDPR', 'Data protection readiness, access by role and documented handling of patient and personal data.'),
            ('ISO 9001, 14001, 27001', 'IT support for quality, environmental and information security audits at large manufacturers.'),
            ('Physical security', 'Badge access, cameras and visitor logs, with badges shut off the day someone leaves.')]
    trs = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rows)
    return f'''<section class="ledger-sec"><div class="wrap">
  <div><h2>For businesses that answer to auditors.</h2><p class="lead" style="margin-top:20px">Our team has run IT where a change isn't finished until it is documented, approved and provable.</p></div>
  <table class="ledger"><caption class="hp">Standards and environments we support</caption><tbody>{trs}</tbody></table>
</div></section>'''

def fit_block():
    pts = [('Small and growing companies', 'Our sweet spot is the business without a full IT department, or with one IT person stretched thin.'),
           ('People who know your name', 'You talk to the same small team every time, people who know your setup and your people.'),
           ('Enterprise experience', 'Thirty years of running IT for regulated and growing companies, put to work at your size and your budget.')]
    cards = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in pts)
    return f'''<section class="band white fit-sec"><div class="wrap">
  <p class="fit-tag">Mom-and-pop care.  <span>Enterprise experience.</span></p>
  <p class="lead fit-lead">We're a small team, and we're built for small companies.  We don't chase large accounts; we'd rather be the IT partner a growing business can call by name.</p>
  <div class="promises light-p fit-cards">{cards}</div>
</div></section>'''

def run_block():
    rows = [('Core infrastructure', 'Servers, storage, virtualization, networks, Wi-Fi and the links between sites.  Data centers and colocation, designed, built, moved and kept running.'),
            ('IT operations', 'The day-to-day: users, devices, patching, monitoring, backups, onboarding and offboarding, vendors and documentation.  Run the same way every time, with written processes.'),
            ('Microsoft 365 and cloud', 'Identity first: Entra ID, phishing-resistant MFA and conditional access.  Then email, SharePoint/OneDrive, Teams and devices, plus Azure and hybrid servers, set up right and kept clean.'),
            ('Business applications', 'ERP, HR and payroll, CRM and quality systems, each with an owner.  Single sign-on, access by role, and licenses and renewals kept in check.'),
            ('AI', 'Copilot readiness, oversharing cleanup before AI is switched on, plain-English AI policies, and agents and automation that save real time.'),
            ('Security', 'Penetration testing, phishing-resistant MFA, endpoint protection, email security, staff training, a written plan for a bad day, and cybersecurity updates your board and audit committee can follow.'),
            ('Facilities', 'When the building is part of the job: office moves and build-outs, server room power and cooling, badge access and cameras.'),
            ('Compliance', 'When audits come, the evidence is ready: SOX, HIPAA, ISO and FDA-regulated environments.')]
    trs = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in rows)
    return f'''<section class="ledger-sec"><div class="wrap">
  <div><h2>What we run.</h2><p class="lead" style="margin-top:20px">Our specialty is the core of IT: the infrastructure and the day-to-day operations that keep a business moving.  Facilities and compliance come along when the work calls for it.</p><p><a class="link" href="engagement.html">See how we work</a></p></div>
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
    i = '<h2>Three ways to work with us.</h2><p class="lead" style="margin-top:18px">Start with one and add another later.  Many clients fix the foundation with a project, then keep it that way with a managed IT plan sized for them.</p>' if intro else ''
    return f'<section class="compare-sec"><div class="wrap">{i}<table class="compare"><thead><tr><td></td>{heads}</tr></thead><tbody>{body}</tbody></table></div></section>'

def standard_block():
    ps = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for _, t, d in sb.STANDARD)
    return f'<section class="standard-sec on-dark" id="standard"><div class="wrap"><h2>Our standard, in writing.</h2><p class="lead" style="margin-top:18px">Six commitments we hold ourselves to on every engagement, large or small.</p><div class="promises">{ps}</div></div></section>'

def quote_block(i=0):
    q, c = sb.QUOTES[i]
    return f'<section class="quote-sec"><div class="wrap"><figure style="margin:0"><blockquote>{q}</blockquote><figcaption>{c}.  <a class="link" href="testimonials.html">Read the testimonials</a></figcaption></figure></div></section>'

def form(dark=True):
    opts = ''.join(f'<option>{E(t)}</option>' for t in TOPICS)
    sizes = ''.join(f'<option>{t}</option>' for t in ['1 to 10 people', '11 to 50 people', '51 to 200 people', '200+ people'])
    return f'''<form class="form{'' if dark else ' light'}" id="contactForm" novalidate>
  <div class="row"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required maxlength="120"></div><div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization" maxlength="160"></div></div>
  <div class="row"><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="200"></div><div class="field"><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="40"></div></div>
  <div class="row"><div class="field"><label for="f-topic">What can we help with?</label><select id="f-topic" name="topic" required><option value="">Choose one</option>{opts}</select></div><div class="field"><label for="f-size">Company size (optional)</label><select id="f-size" name="size"><option value="">Choose one</option>{sizes}</select></div></div>
  <div class="field"><label for="f-msg">Tell us what's going on</label><textarea id="f-msg" name="message" required maxlength="5000"></textarea></div>
  <div class="hp" aria-hidden="true"><label for="f-hp">Leave this empty</label><input id="f-hp" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div><button class="btn{'' if dark else ' ink'}" type="submit">Send message</button></div>
  <p class="form-msg" id="formMsg" role="alert" hidden></p>
  <p class="form-note">A senior consultant replies within one business day.  We only use your details to reply.  <a href="privacy.html" style="color:inherit">Privacy policy</a>.</p>
</form>'''

def close_block():
    st = ''   # no background art: keeps the contact section clean
    return f'''<section class="chart-sec close-sec on-dark" id="talk">{st}<div class="wrap">
  <div><h2>Tell us what you're working on.</h2><p class="lead" style="margin-top:20px">An audit on the calendar, an office move, a security worry or an IT person who just gave notice.  Send a few lines and we'll reply within one business day.</p>
  <p style="margin-top:28px;color:#8ea2b8;font-size:15px">Headquarters in Huntington Beach, California.  Remote offices in Arcata, California and Payson, Arizona.<br>On-site across California and Arizona.  Remote support in all 50 states.</p></div>
  {form(True)}
</div></section>'''

# ---------- pages ----------
def home():
    stats = ''.join(f'<div><strong>{n}</strong>{t}</div>' for n, t in STATS2)
    body = f'''
<section class="chart-sec hero on-dark"><div class="wrap">
  <div>
    <p class="kicker">Rooted in California.  Serving businesses nationwide.</p>
    <h1><span class="h-serif">Your IT, run right.</span><span class="h-heavy">Infrastructure and IT operations, handled.</span></h1>
    <p class="lead">We design, build and run the systems your business depends on: servers, networks, data centers, Microsoft 365, business applications and security.  Thirty years of running IT operations, now working for you.</p>
    <div class="acts"><a class="btn" href="#talk">Contact us</a><a class="btn line" href="services.html">See our services</a></div>
    <p class="reach-note">On-site across California and Arizona.  Remote support in all 50 states.</p>
  </div>
  {us_map_block()}
</div></section>

<section class="statement"><div class="wrap">
  <p class="big">Our team has spent <b>thirty years</b> on the hard parts of IT: moving a headquarters, standing up a data center, joining ten acquisitions onto one network, fixing what broke at 2 a.m.  Now we do it for you.</p>
  <div class="margin">{stats}</div>
</div></section>

{fit_block()}
{run_block()}
{index_block()}
{notes_block()}
{news_block()}
{compare_block()}
{standard_block()}
{quote_block(1)}
{close_block()}
<script type="application/ld+json">{ORG_LD}</script>'''
    page('index.html', 'Cali IT Consulting | IT infrastructure and operations, nationwide', "IT infrastructure and operations, handled: servers, networks, Microsoft 365, business applications and security.  California-based, serving clients nationwide.", body, CUBE_JS())

def services():
    body = phero('Twelve practice areas.', 'One team that has run them all.', 'Bring us a single project or hand us the whole stack.') + index_block(head=False) + f'''
<section class="band white"><div class="wrap two">
  <div><h2>Not sure where to start?  Start with an assessment.</h2><p class="lead" style="margin-top:18px">We review your environment, rank the risks and hand you a written plan.  You decide what to fix, and who fixes it.</p><p style="margin-top:26px"><a class="btn ink" href="contact.html?topic=A%20project%20or%20assessment">Ask about an assessment</a></p></div>
  <ul class="ticks"><li>Microsoft 365 and identity security</li><li>Backups and recovery</li><li>Network, firewall and Wi-Fi</li><li>Licensing and vendor spend</li><li>Compliance gaps and evidence</li><li>A ranked, written remediation plan</li></ul>
</div></section>
{close_block()}'''
    page('services.html', 'Services | Cali IT Consulting', 'Twelve IT practice areas, one team: network, cloud, data center, Microsoft 365, business applications, AI, managed IT, security and compliance.', body, CUBE_JS())

def service(i, s):
    m = re.match(r'(.*?)<em>(.*?)</em>(.*)', s['h']); a, b, c = m.groups()
    sym = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in s['pains'])
    ct, cs, cl, co = s['case']
    prev, nxt = sb.SERVICES[i - 1], sb.SERVICES[(i + 1) % len(sb.SERVICES)]
    body = phero(a.strip().rstrip(','), b + c, s['intro'], trail=f'<a href="services.html">Services</a> / {s["name"]}') + f'''
<section class="band white"><div class="wrap"><h2>Sound familiar?</h2><div class="symptoms">{sym}</div></div></section>
<section class="band fog"><div class="wrap two">
  <div><h2>What you get.</h2><ul class="ticks" style="margin-top:30px">{''.join(f'<li>{g}</li>' for g in s['get'])}</ul>
  <p style="margin-top:30px"><a class="btn ink" href="contact.html?topic={quote(TOPIC_OF.get(s['slug'], 'A project or assessment'))}&amp;msg={quote('About ' + s['name'] + ': ')}">Talk to us about {s["name"]}</a></p></div>
  <div><article class="story"><p style="color:#8fb3d9;font-weight:600;margin-bottom:10px">{s.get('case_label', 'From the field')}</p><h3>{ct}</h3><p>{cs}</p><ul class="ticks on-dark" style="border-top-color:#8fb3d9">{''.join(f'<li>{x}</li>' for x in cl)}</ul><div class="out">{co}</div></article>
  {'<p class="fine">' + s.get('case_note', 'Client names are kept confidential.') + '</p>' if s.get('case_note', 'x') else ''}
  <h3 style="margin-top:34px">Platforms and standards</h3><p class="inline-list" style="margin-top:10px">{''.join(f'<span>{p}</span>' for p in s['plat'])}</p></div>
</div></section>
<section class="band white"><div class="wrap"><nav class="next-prev" aria-label="More services"><a href="{prev['slug']}.html"><small>Previous service</small><b>{prev['name']}</b></a><a href="{nxt['slug']}.html" style="text-align:right"><small>Next service</small><b>{nxt['name']}</b></a></nav></div></section>
{close_block()}'''
    page(s['slug'] + '.html', f'{s["name"]} | Cali IT Consulting', s.get('desc') or f'{s["name"]} from Cali IT Consulting.  {s["intro"].split("  ")[0]}', body)

def industries():
    rows = ''.join(f'<article class="ind"><div><h3>{t}</h3><p>{d}</p></div><ul class="ticks">{"".join(f"<li>{x}</li>" for x in l)}</ul></article>' for _, t, d, l in sb.INDUSTRIES)
    body = phero('IT for businesses', 'that answer to someone.', 'Regulators, auditors, clients or a board.  Our team has run IT where downtime and audit findings are not an option.') + f'''
<section class="band white"><div class="wrap">{rows}</div></section>
{ledger_block()}
{close_block()}'''
    page('industries.html', 'Industries | Cali IT Consulting', 'IT consulting for life sciences, FDA-regulated companies, clinical labs, manufacturing, finance and growing companies.', body)


FAQ = [('Do you only work in California?', 'No.  Our headquarters is in Huntington Beach, and we work on-site across California and Arizona.  We support clients remotely in all 50 states and travel on-site as required.'),
       ('How big are the companies you work with?', "Small and growing companies are our sweet spot: usually businesses without a full IT department, or with one IT person who needs backup.  We're a small team on purpose, and we keep our client list small enough to know every one of them."),
       ('Are you an MSP?', "Not a big-box one.  You can hire us for a single project, a managed IT plan built around what you actually need, or part-time IT leadership.  Many clients start with a project and keep going from there."),
       ('Can you work alongside our IT person or current provider?', 'Yes.  Co-managed IT is a common setup for us: your team keeps the day-to-day, and we take the projects, the security work or the parts nobody has time for.'),
       ('Do you work with FDA-regulated companies?', "Yes.  Our team has spent years running IT for medical device, diagnostics and certified lab companies, where access, change records and audit evidence have to hold up."),
       ('What happens if we stop working together?', 'You keep everything: passwords, admin access and documentation.  We hand it over in writing, so the next person can pick it up on day one.'),
       ('How do we get started?', 'Send a few lines through the contact form.  A senior consultant replies within one business day, and you get a written scope and price before any work starts.')]
def faq_block():
    items = ''.join(f'<details class="faq-i"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace('  ', ' ')}} for q, a in FAQ]})
    return f'''<section class="band fog"><div class="wrap"><h2>Common questions.</h2><div class="faq">{items}</div></div></section><script type="application/ld+json">{ld}</script>'''

ORG_LD = json.dumps({"@context": "https://schema.org", "@type": "ProfessionalService", "name": "Cali IT Consulting", "url": "https://caliit.com/", "logo": "https://caliit.com/assets/brand/og.png",
    "description": "IT infrastructure, IT operations, Microsoft 365, business applications, cybersecurity and compliance consulting.",
    "address": {"@type": "PostalAddress", "addressLocality": "Huntington Beach", "addressRegion": "CA", "addressCountry": "US"}, "areaServed": "US"})

def engagement():
    steps = [('Send us a message', "Tell us what's going on through the contact form.  We reply within one business day."), ('Get a written proposal', 'A clear scope, timeline and price, in plain English.'), ('Kick off', 'We get to work, keep you posted and document everything as we go.'), ('Hand-off or ongoing', 'Projects end with documentation you own.  Managed and fractional work continue month to month.')]
    st = ''.join(f'<div><h3><span style="font:400 15px var(--heavy);color:#8fb3d9;display:block;margin-bottom:8px">Step {n}</span>{t}</h3><p>{d}</p></div>' for n, (t, d) in enumerate(steps, 1))
    body = phero('Work with us', 'the way that fits.', 'One job, a managed IT plan built around you, or a senior IT leader part time.  Start with one, add another later.') + compare_block(intro=False) + f'''
<section class="standard-sec on-dark"><div class="wrap"><h2>How an engagement starts.</h2><div class="promises four">{st}</div></div></section>
{standard_block().replace('standard-sec on-dark', 'band white').replace('class="promises"', 'class="promises light-p"')}
{faq_block()}
{close_block()}'''
    page('engagement.html', 'How We Work | Cali IT Consulting', 'Projects, a managed IT plan built around you, or fractional IT leadership.  Written scope and price before work starts.', body)

def why():
    qs = ''.join(f'<li data-q="{i}"><p>{q}</p><div class="yn"><button type="button" data-v="1" aria-pressed="false">Yes</button><button type="button" data-v="0" aria-pressed="false">No</button></div></li>' for i, q in enumerate(sb.QUESTIONS))
    pains = ''.join(f'<li><a href="{s}.html"><span class="nm" style="font:italic 500 clamp(20px,2vw,26px)/1.25 var(--serif)">{t}</span><span class="ds">{sb.SVC[s]["name"]}</span></a></li>' for t, s in sb.PAINS)
    body = phero('Mom-and-pop care.', 'Enterprise experience.', "A small team for small and growing companies.  You get people who know your name and your systems, backed by thirty years of running IT where downtime and audit findings aren't an option.") + f'''
<section class="band white" id="check"><div class="wrap">
  <h2>The 60-second IT health check.</h2><p class="lead" style="margin-top:16px">Six honest questions.  No email required, and your answers stay in your browser.</p>
  <div class="check"><ol class="questions" id="questions">{qs}</ol>
  <div class="score"><div class="n" id="gaugeNum">0<small> of {len(sb.QUESTIONS)}</small></div><h3 id="verdictTitle">Answer the questions</h3><p id="verdictText">Every "No" is a gap worth closing.  Most businesses have at least one.</p><a class="btn" id="checkCta" href="contact.html" hidden>Send us your results</a></div></div>
</div></section>
<section class="index-sec on-dark"><div class="wrap" style="grid-template-columns:1fr"><div><div class="index-head"><h2>If you nodded at any of these, we should talk.</h2></div><ul class="svc-list">{pains}</ul></div></div></section>
{notes_block()}
{standard_block()}
{close_block()}'''
    page('why-us.html', 'Why Us | Cali IT Consulting', 'Mom-and-pop care, enterprise experience: a small IT team for small and growing companies.  Take the free 60-second IT health check.', body)

def about():
    vals = ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in [('Straight answers', "Plain English, no jargon.  If something doesn't need fixing, we'll say so."), ('Senior people', 'The people who scope your project are the ones who do the work.'), ('Documented', "Every change is written down, so you're never locked in to us."), ('Built to last', 'We design for the next five years, not the next invoice.')])
    stats = ''.join(f'<div><strong>{n}</strong>{t}</div>' for n, t in STATS2)
    body = phero('Built by people', 'who ran IT, not just sold it.', "Cali IT Consulting brings 30 years of IT leadership to businesses that can't afford downtime.") + f'''
<section class="statement"><div class="wrap">
  <p class="big">Our team has run technology for FDA-regulated medical device and diagnostics companies, manufacturers and growing firms, from the North Coast to Huntington Beach and across the country.</p>
  <div class="margin">{stats}</div>
</div></section>
<section class="band fog"><div class="wrap two">
  <div><h2>What we do.</h2></div>
  <div class="prose"><p class="lead">We've integrated IT for more than ten acquisitions, moved headquarters and data centers, built certified labs, and passed SOX and ISO audits and HIPAA reviews.</p><p>We handle networks, servers and cloud, data centers, Microsoft 365, business applications, cybersecurity, physical security, compliance and IT strategy.  We work on-site across California and Arizona and support clients remotely in all 50 states, traveling on-site as required.  You get senior-level answers from people who have done the work, not a sales pitch.</p><p>Some of our longest client relationships began at OC TechWorks LLC, the Orange County IT firm our founder co-owned from start to finish.  When it wound down, its clients came with us.</p></div>
</div></section>
<section class="standard-sec on-dark"><div class="wrap"><h2>What we stand for.</h2><div class="promises">{vals}</div></div></section>
{notes_block()}
{quote_block(2)}
{close_block()}'''
    page('about.html', 'About | Cali IT Consulting', 'Thirty years of IT leadership in regulated companies, from data centers to Microsoft 365.  Headquartered in Huntington Beach, serving clients nationwide.', body)

def news_block(limit=6, full=False):
    more = '' if full else '<p style="margin-top:26px"><a class="link" href="news.html">All security news</a></p>'
    return f'''<section class="band white news-sec"><div class="wrap two">
  <div><h2>{'Latest headlines.' if full else 'Security briefing.'}</h2><p class="lead" style="margin-top:18px">The latest from CISA, Microsoft and the security press, refreshed every hour.  Each headline links to the original source.</p>
  <a class="m365" id="m365Status" href="https://status.cloud.microsoft/" target="_blank" rel="noopener"><span class="dot" aria-hidden="true"></span><span><b>Microsoft 365 service status</b><span class="m365-t">Checking Microsoft's public status page.</span></span></a>
  <p class="fine" style="margin-top:12px">From Microsoft's public status page, which covers widespread incidents.  Issues in a single company's tenant show in its own admin center.</p>{more}</div>
  <ol class="news" id="newsList" data-limit="{limit}"><li class="news-empty">Loading the latest headlines.</li></ol>
</div></section>'''

def news_page():
    body = phero('Security news,', 'refreshed every hour.', 'Advisories from CISA and Microsoft, plus the stories security teams are reading.  We collect the headlines; every link goes to the original publisher.') + news_block(30, True) + close_block()
    page('news.html', 'Security News | Cali IT Consulting', 'Cybersecurity headlines from CISA, Microsoft and the security press, plus Microsoft 365 service status, refreshed every hour.', body)

def testimonials():
    rows = ''
    for t in sb.TESTIMONIALS:
        ps = ''.join(f'<p>{E(p)}</p>' for p in t['paras'])
        rows += f'<figure class="tq" style="margin:0"><figcaption class="who">{E(t["cap"][0])}<span>{E(t["cap"][1]) if len(t["cap"]) > 1 else ""}</span></figcaption><blockquote>{ps}</blockquote></figure>'
    body = phero('In their', 'own words.', 'What clients and colleagues have said about the work of our team\'s leader.  Quoted from LinkedIn recommendations, with names left out for privacy.') + f'<section class="band white"><div class="wrap tquotes">{rows}</div></section>{close_block()}'
    page('testimonials.html', 'Testimonials | Cali IT Consulting', 'What clients and colleagues say about working with the Cali IT Consulting team.', body)

def contact():
    body = phero('Tell us what', "you're working on.", 'Fill out the form and a senior consultant will get back to you within one business day.') + f'''
<section class="band white"><div class="wrap two">
  <div><h2>California headquarters.  Nationwide clients.</h2><ul class="ticks" style="margin-top:28px"><li>Headquarters in Huntington Beach, California</li><li>Remote offices in Arcata, California and Payson, Arizona</li><li>On-site across California and Arizona</li><li>Remote support in all 50 states, with on-site travel as required</li><li>A reply from a senior consultant within one business day</li></ul></div>
  {form(False)}
</div></section>'''
    page('contact.html', 'Contact | Cali IT Consulting', 'Contact Cali IT Consulting.  California headquarters, clients nationwide.  A senior consultant will reply within one business day.', body)

def thanks():
    body = phero('Thanks.', 'We got your message.', 'A senior consultant will reply within one business day.') + '<section class="band white"><div class="wrap"><a class="btn ink" href="index.html">Back to the home page</a></div></section>'
    page('thanks.html', 'Thank you | Cali IT Consulting', 'Your message was sent.', body)

def privacy():
    src = (ROOT / 'privacy.html').read_text()
    prose = src[src.index('<div class="wrap prose">') + len('<div class="wrap prose">'):src.index('</div></section>', src.index('<div class="wrap prose">'))] if '<div class="wrap prose">' in src else ''
    body = phero('Privacy', 'policy.', f'Effective October 29, {sb.YEAR}.', mini=False) + f'<section class="band white"><div class="wrap prose">{prose}</div></section>'
    page('privacy.html', 'Privacy | Cali IT Consulting', 'How Cali IT Consulting collects, uses and protects information sent through this website and its contact form.', body)

def notfound():
    body = phero('This page', 'is off the map.', "The page you're looking for isn't here.") + '<section class="band white"><div class="wrap"><a class="btn ink" href="index.html">Home page</a> &nbsp; <a class="link" href="services.html">Services</a></div></section>'
    page('404.html', 'Page not found | Cali IT Consulting', 'Page not found.', body)

def cube_preview():
    S2 = {x['slug']: x for x in sb.SERVICES}
    codes = {'network': 'NET', 'cloud': 'CLD', 'data-center': 'DC', 'microsoft-365': 'M365', 'ai': 'AI', 'cybersecurity': 'SEC',
             'it-strategy': 'STRAT', 'business-automation': 'AUTO', 'access-control': 'ACS', 'compliance': 'CMP'}
    it = lambda slug: {'slug': slug, 'code': codes[slug], 'name': {'ai': 'Artificial intelligence'}.get(slug, S2[slug]['name']), 'short': S2[slug]['short']}
    front = [it(x) for x in ['network', 'cloud', 'data-center', 'microsoft-365', 'ai', 'cybersecurity', 'it-strategy', 'business-automation', 'access-control']]
    techs = ['Cisco Meraki', 'UniFi', 'Site-to-site VPN', 'Wi-Fi', 'Firewalls', 'Switching', 'Remote access', 'Monitoring', 'Phone systems',
             'Azure', 'VMware', 'NetApp', 'Synology', 'Dell servers', 'HP servers', 'Cloud backup', 'Colocation', 'Disaster recovery',
             'Entra ID', 'Exchange Online', 'SharePoint', 'OneDrive', 'Teams', 'Intune', 'Conditional access', 'Copilot', 'Power Apps',
             'Power Automate', 'NetSuite', 'HubSpot', 'Pipedrive', 'Pen testing', 'Email gateway', 'Badge access', 'Cameras', 'UPS and power']
    top = ['SOX', 'HIPAA', 'ISO 27001', 'GDPR', it('compliance'), 'FDA-regulated', 'ITIL', 'CLIA labs', 'Audit evidence']
    data = json.dumps({'front': front, 'top': top, 'techs': techs})
    body = phero('A cube you', 'can click.', 'Preview only.  Each tile on the front is a service.  Point at one to read about it, click it to open it, or drag to spin and see the technologies on the other sides.', mini=False) + f"""
<section class="index-sec on-dark"><div class="wrap c2-wrap">
  <div><h2>Ten practice areas, one team.</h2><p class="lead" style="margin:16px 0 30px">Nine services on the front, compliance on top, and the platforms we support on every other side.</p><div class="c2-panel" id="cube2-panel" aria-live="polite"></div></div>
  <div class="c2-stage"><div class="c2-cube" id="cube2"></div></div>
</div></section>
<script type="application/json" id="cube2-data">{data}</script>"""
    page('cube-preview.html', 'Cube preview | Cali IT Consulting', 'Preview of a clickable service cube.', body, f'<script src="assets/js/cube2.js?v={sb.ver("assets/js/cube2.js")}" defer></script>')
    f = ROOT / 'cube-preview.html'; f.write_text(f.read_text().replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n<meta name="theme-color"', 1))

def map_preview():
    global DE_CITY
    keep = DE_CITY; DE_CITY = 'Tuttlingen'
    blk = us_map_block()
    DE_CITY = keep
    def band(tag, title, note):
        return f'''<section class="chart-sec hero on-dark {tag}" style="min-height:0;padding:60px 0"><div class="wrap" style="display:block;max-width:1200px">
  <h2 style="color:#fff;margin-bottom:6px">{title}</h2><p class="lead" style="margin-bottom:24px">{note}</p>{blk}</div></section>'''
    body = (band('opt-a', 'Option A: current colors', 'The map as it is on the live site today, with a red dot in Germany.').replace('padding:60px 0', 'padding:140px 0 60px')
            + band('opt-b', 'Option B: bluer', 'The same map in a richer blue.  California and Germany stand out in a brighter blue.'))
    page('map-preview.html', 'Map preview | Cali IT Consulting', 'Map color preview.', body)
    f = ROOT / 'map-preview.html'; f.write_text(f.read_text().replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n<meta name="theme-color"', 1))

if __name__ == '__main__':
    privacy()   # reads the current privacy text first
    home(); services(); [service(i, s) for i, s in enumerate(sb.SERVICES)]; industries(); engagement(); why(); about(); testimonials(); contact(); news_page(); thanks(); notfound(); cube_preview(); map_preview()
    for _n in ('thanks.html', '404.html'):   # keep these out of search results
        _f = ROOT / _n; _t = _f.read_text()
        if 'name="robots"' not in _t: _f.write_text(_t.replace('<meta name="theme-color"', '<meta name="robots" content="noindex">\n<meta name="theme-color"', 1))
    print('built field-chart site')
