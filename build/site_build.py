"""Builds the Cali IT website (all public pages) from the content below.
Run from the repo root:  python3 build/site_build.py
Design: navy / steel, logo P3, Archivo + Inter + Bodoni italic + Josefin labels.  No personal names; contact form only."""
import json, pathlib, sys, html, hashlib, importlib.util
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'build'))
spec = importlib.util.spec_from_file_location('pb', ROOT / 'build' / 'pick_build.py'); pb = importlib.util.module_from_spec(spec); spec.loader.exec_module(pb)
from logos_set3 import CA

YEAR = 2026
E = html.escape

def ver(rel):
    return hashlib.md5((ROOT / rel).read_bytes()).hexdigest()[:8]

# ---------- logo pieces ----------
def logo_dark(cls='brand-svg'):
    svg = pb.lockup('#0f1c2d', '#8fb3d9', '#8fb3d9', '#8fb3d9', 31, panel=False, gid='bl', on_dark=True)
    return f'<svg class="{cls}" viewBox="62 4 206 92" role="img" aria-label="Cali IT Consulting">{svg}</svg>'
STATE = f'<svg class="state-bg" viewBox="0 0 200 220" aria-hidden="true"><path d="{CA}" fill="#8fb3d9"/></svg>'
HERO_STATE = f'<svg class="hero-state" viewBox="0 0 200 220" aria-hidden="true"><path d="{CA}" fill="#8fb3d9"/></svg>'

# ---------- icons (simple line icons) ----------
def icon(name):
    p = {
      'microsoft-365': '<rect x="3" y="3" width="8" height="8"/><rect x="13" y="3" width="8" height="8"/><rect x="3" y="13" width="8" height="8"/><rect x="13" y="13" width="8" height="8"/>',
      'cybersecurity': '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
      'network': '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M12 7.5v4M12 11.5L6.5 17M12 11.5l5.5 5.5"/>',
      'cloud': '<path d="M7 18a4.5 4.5 0 01-.6-9A6 6 0 0118 8.5a4.5 4.5 0 01-.5 9.5z"/>',
      'data-center': '<rect x="4" y="3" width="16" height="5" rx="1"/><rect x="4" y="10" width="16" height="5" rx="1"/><rect x="4" y="17" width="16" height="4" rx="1"/><path d="M8 5.5h.01M8 12.5h.01"/>',
      'compliance': '<path d="M7 3h8l4 4v14H7z"/><path d="M15 3v4h4M10 13l2 2 4-4"/>',
      'access-control': '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 018 0v3"/><circle cx="12" cy="15.5" r="1.5"/>',
      'business-automation': '<path d="M4 7h11M11 3l4 4-4 4M20 17H9M13 13l-4 4 4 4"/>',
      'it-strategy': '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
      'flask': '<path d="M9 3h6M10 3v6l-5 9a2 2 0 002 3h10a2 2 0 002-3l-5-9V3"/><path d="M7.5 15h9"/>',
      'factory': '<path d="M3 21V10l6 4V10l6 4V6l6 3v12z"/><path d="M7 18h2M12 18h2M17 18h2"/>',
      'briefcase': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 12h18"/>',
      'growth': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
      'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
      'doc': '<path d="M7 3h8l4 4v14H7z"/><path d="M10 12h6M10 16h6M10 8h2"/>',
      'person': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/>',
      'talk': '<path d="M4 5h16v11H9l-5 4z"/>',
      'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/>',
    }[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

# ---------- content ----------
SERVICES = [
 dict(slug='microsoft-365', name='Microsoft 365', h='Your workplace, <em>locked down</em> and running clean.', short='Tenant security, migrations and licensing that works for you.',
  intro='Microsoft 365 runs your email, files, meetings and identity.  We set it up right, secure it, and keep licensing under control so it works for you instead of against you.',
  pains=[('Nobody owns the tenant', 'Settings were clicked through years ago, admins come and go, and nobody is sure what is configured.'), ('Licenses keep creeping up', 'You pay for seats and add-ons nobody uses, and every renewal costs more.'), ('Files live everywhere', 'Shared drives, personal OneDrives and old file servers, with no clear owner or permissions.')],
  get=['Tenant security review with a prioritized fix list', 'Exchange, Teams, SharePoint and OneDrive migrations', 'Licensing review and cleanup', 'Standard onboarding and offboarding for every user', 'SharePoint sites and intranets your staff will actually use', 'Power Apps and Power Automate to replace manual steps'],
  plat=['Microsoft 365', 'Exchange', 'Teams', 'SharePoint', 'OneDrive', 'Entra ID', 'Intune', 'Power Apps', 'Power Automate'],
  case=('A full move to the cloud', 'A medical device company was running its own email, chat and document servers.', ['Migrated Exchange 2010, Lync 2013 and SharePoint 2013 to Office 365', "Built the company's first corporate intranet, with project and team sites", 'Retired the on-premises servers once users were moved'], 'Email, chat and documents moved to the cloud, and the company launched its first intranet.')),
 dict(slug='cybersecurity', name='Cybersecurity', h='Find the gaps <em>before someone else does</em>.', short='Assessments, MFA, email protection and a plan for a bad day.',
  intro='Security based on risk, not fear.  We find the doors an attacker would use, close the important ones first, and get your team ready for the day something gets through.',
  pains=[('MFA is "mostly" on', 'A few accounts, often admins or shared mailboxes, were left out, and those are the ones attackers find.'), ('No plan for a bad day', 'If ransomware hit tomorrow, nobody knows who calls whom, or what gets shut off first.'), ('Staff are the target', 'Phishing and phone scams now impersonate your help desk and your vendors.')],
  get=['Security assessment with a ranked remediation plan', 'MFA and conditional access everywhere', 'Email protection and phishing defenses', 'Security awareness training for staff', 'Incident response plan and tabletop exercise', 'Hands-on help when an incident happens'],
  plat=['Entra ID', 'Conditional access', 'Intune', 'Cisco Meraki', 'Remote access VPN', 'Security awareness training'],
  case=('Security leadership for a regulated company', 'A global medical device company needed someone to own security across the US and Europe.', ['Served as acting chief security officer for incident response and risk management', 'Led HIPAA and GDPR compliance work', 'Ran secure remote access for thousands of users at a global manufacturer'], 'Security had an owner, a plan and a response process that held up across two continents.')),
 dict(slug='network', name='Network', h='Fast, stable and <em>built to grow</em>.', short='Firewalls, switching, Wi-Fi and the links between your sites.',
  intro='Firewalls, switches, Wi-Fi and the links between your sites.  We design it, install it, document it and watch it, so the network is the last thing anyone thinks about.',
  pains=[('The Wi-Fi drops', 'Everyone has learned which conference room to avoid.'), ("Sites don't talk", 'Branch offices or labs connect through workarounds nobody wants to touch.'), ('The office is moving', "A new building means cabling, firewalls, phones and a cutover that can't go wrong.")],
  get=['Network design from core to edge', 'Firewall, switching and Wi-Fi installs', 'Site-to-site and remote access VPN', 'Office moves and new building cutovers', 'Guest Wi-Fi that stays separate from your business network', 'Monitoring and documentation you keep'],
  plat=['Cisco Meraki', 'UniFi', 'Site-to-site VPN', 'Wi-Fi', 'Phone systems', 'Network monitoring'],
  case=('One network, many countries', 'A global manufacturer had offices and plants on multiple continents running on separate networks.', ['Built private networks linking 30+ facilities in more than 10 countries', 'Rolled out 2,000+ internet phones across 10 sites', 'Later designed and deployed a Cisco Meraki network with site-to-site VPN for a multi-site lab company'], 'Every site on one managed network, with phones and security handled centrally.')),
 dict(slug='cloud', name='Cloud', h="Move what makes sense.  <em>Keep what doesn't.</em>", short='Migration plans, servers, storage and backups you have tested.',
  intro="Not everything belongs in the cloud, and not everything belongs in your closet.  We help you decide, then move it, back it up and keep the bill in check.",
  pains=[('The server closet is aging', 'The hardware is out of warranty and the one person who understood it has left.'), ('Backups are a hope', 'Backups run, but nobody has tested a real restore in years.'), ('The cloud bill keeps climbing', 'Resources were spun up for a project and never turned off.')],
  get=['Cloud readiness review and migration plan', 'Azure and hybrid server design', 'Virtualization and storage', 'Cloud backup with tested restores', 'Disaster recovery you have actually practiced', 'Cloud cost reviews'],
  plat=['Azure', 'VMware', 'NetApp', 'Dell', 'HP', 'Synology', 'Cloud backup', 'Colocation'],
  case=('Out of the server room', 'A medical device company ran its systems in an on-site data center with local backups.', ['Moved the corporate data center to a colocation facility', 'Replaced local backup appliances with an offsite cloud backup partner', 'Set up disaster recovery on cloud-based virtual servers'], 'Systems in a professional facility, backups offsite and a working recovery plan.')),
 dict(slug='data-center', name='Data Center', h='Data centers and colocation, <em>built right the first time</em>.', short='Server rooms, colocation and moves without the surprises.',
  intro='We have designed, built and moved data centers and server rooms for companies across the country.  From picking a colocation provider to the last cable in the rack, we plan it, build it and move you in without the surprises.',
  pains=[('The server room is out of room', 'Power, cooling or rack space has run out, and adding one more server is a risk.'), ('A colocation contract is up', 'The renewal is coming, the price went up, and nobody has compared providers in years.'), ('A move is on the calendar', 'A new office, a closing facility or a lease ending, and the servers have to go somewhere without downtime.')],
  get=['Data center and server room design and build-outs', 'Colocation provider selection and contract negotiation', 'Server and data center moves, between facilities or to the cloud', 'Power, cooling and backup generator planning', 'Rack layout, structured cabling and labeling', 'Move plans with cutover steps and a rollback plan'],
  plat=['Colocation', 'Server rooms', 'Rack and cabling', 'UPS and power', 'Cooling', 'Generators', 'Data center moves'],
  case=('Into a professional facility', 'A global manufacturer was running its data center on-site, with servers spread across regional hubs.', ['Virtualized 80% of servers across six regional hubs', 'Moved the data center to a colocation facility with failover', 'Restructured outside partners as part of the same program'], '$4.5 million in operating costs cut over two years, with failover built in.')),
 dict(slug='compliance', name='Compliance', h='Ready when the <em>auditors show up</em>.', short='SOX, HIPAA, ISO and FDA-regulated IT controls and evidence.',
  intro="We've sat on the IT side of SOX, HIPAA, ISO and FDA-regulated audits.  We help you build the controls, keep the evidence and walk into the audit calm.",
  pains=[('Evidence is scattered', 'Screenshots in email, spreadsheets on desktops, and a scramble every audit season.'), ('Policies are out of date', 'Written years ago, never followed, and now they contradict what you really do.'), ('New rules apply to you', 'Growth, a new customer or going public just put you in scope.')],
  get=['IT general controls for SOX', 'HIPAA and data protection readiness', 'Written policies and procedures that match reality', 'Evidence collection and audit support', 'Change management and access reviews', 'Support for FDA-regulated and certified lab environments'],
  plat=['SOX', 'HIPAA', 'GDPR', 'ISO 9001', 'ISO 14001', 'ISO 27001', 'ITIL', 'CLIA labs'],
  case=('Audits without the scramble', 'A publicly traded diagnostics company needed IT controls tested every year.', ['Served as business lead for SOX IT general controls testing and reporting', 'Supported certified clinical labs in multiple states and countries', 'Earlier ran ISO 9001, 14001 and 27001 audits for a global manufacturer'], 'Controls documented, tested on schedule and ready for every audit cycle.')),
 dict(slug='access-control', name='Access Control', h='Badge doors, cameras and alarms that <em>work with your IT</em>.', short='Badge access, cameras and monitoring tied to your accounts.',
  intro='Physical security is part of security.  We design badge access, cameras and monitoring that tie into your user accounts, so access ends the day someone leaves.',
  pains=[('Old badges still work', 'People who left months ago can still open the front door.'), ('Cameras nobody can use', 'The system records, but nobody knows how to find or export footage.'), ('A new building is coming', 'Doors, readers, cameras and network all need to be planned before the walls close.')],
  get=['Access control system design and installs', 'Security cameras and video surveillance', 'Badge design and visitor management', 'Remote guard and alarm monitoring coordination', 'Access tied to your hiring and offboarding process', 'Plans for new buildings and build-outs'],
  plat=['Badge access control', 'Video surveillance', 'Visitor management', 'Remote guard services', 'Alarm monitoring'],
  case=('A secure campus from day one', 'A medical device company was moving into a new four-building campus.', ['Designed the access control and video surveillance system for all four buildings', 'Created the employee badge design', 'Later built a full physical security program, with access control, cameras and remote guards, for three sites including certified labs'], 'Every door, camera and badge planned before move-in, and managed from one place.')),
 dict(slug='business-automation', name='Business Automation', h='Stop re-typing.  <em>Let the systems do it.</em>', short='Power Apps, Power Automate and CRM workflows that end busywork.',
  intro='Approvals stuck in email, the same data typed into three systems, spreadsheets passed around for sign-off.  We automate the busywork with Power Apps, Power Automate and the tools you already pay for.',
  pains=[('Approvals live in email', 'Purchase requests, time off and sign-offs bounce between inboxes, and nobody knows where things stand.'), ('Double data entry', 'The same customer or order gets typed into the CRM, the accounting system and a spreadsheet.'), ('Spreadsheets run the business', 'A critical process depends on one workbook and the one person who understands it.')],
  get=['Process review to find what is worth automating', 'Power Apps that replace paper forms and spreadsheets', 'Power Automate flows for approvals, alerts and handoffs', 'CRM setup and automation in Pipedrive or HubSpot', 'Connections between Microsoft 365, your CRM and accounting', 'Documentation and training so your team owns it'],
  plat=['Power Apps', 'Power Automate', 'SharePoint lists', 'Microsoft Forms', 'Teams approvals', 'Pipedrive', 'HubSpot', 'NetSuite'],
  case=('Business apps that keep up', 'A global medical device company needed its business systems to work together.', ['Supported the business application stack, data integrations and data warehousing', 'Delivered reporting, business intelligence and Power Apps for the business', 'Later managed the business application stack and change management for a diagnostics company'], 'Systems connected, data flowing, and fewer manual steps between teams.')),
 dict(slug='it-strategy', name='IT Strategy', h='A plan that matches the business, and <em>a budget to back it</em>.', short='Roadmaps, budgets, vendors and part-time IT leadership.',
  intro='Fractional IT leadership for companies that need a senior IT voice without a full-time hire.  Roadmaps, budgets, vendors and the hard calls.',
  pains=[('IT is a pile of vendors', 'Contracts renew on their own, and nobody knows what you are paying for.'), ('Growth is coming', 'An acquisition, a new site or a funding round, and IT has to keep up.'), ('No one to ask', 'Leadership needs someone who can explain the risks and the costs in plain English.')],
  get=['Technology roadmap with a 3 to 5 year view', 'IT budget and annual operating plan', 'Vendor contract review and negotiation', 'Merger and acquisition IT integration', 'Managed service provider selection, or replacement', 'Board and leadership reporting'],
  plat=['IT roadmaps', 'Budgets', 'Vendor contracts', 'M&A integration', 'NetSuite', 'Service desk'],
  case=('A roadmap and a budget that held', 'Growing companies needed IT that kept pace with acquisitions, new sites and new budgets.', ['Built a technology roadmap by business function, with a 3 to 5 year view', 'Managed IT budgets up to $12 million and negotiated 50+ IT contracts', 'Replaced an outside managed service provider with an in-house service desk'], 'A clear plan, predictable spending and support that answered to the business.')),
]
SVC = {s['slug']: s for s in SERVICES}
TOPICS = ['IT and security assessment'] + [s['name'] for s in SERVICES] + ['Regulated industry support', 'Something else']

STATS = [('30', 'Years in IT leadership'), ('10+', 'Acquisitions integrated'), ('30+', 'Sites networked worldwide'), ('$12M', 'Largest IT budget managed')]
STEPS = [('Assess', 'We look at what you have, what it costs and where the risks are, then hand you a ranked, written plan.'),
         ('Deploy', 'We build it right the first time, on a written scope and price, with every change documented.'),
         ('Manage', 'We keep it running: users, devices, updates, vendors and a real person when something breaks.'),
         ('Protect', 'We keep watch, test the backups, train your people and keep the evidence ready for audits.')]
RESULTS = [('Facilities', 'Headquarters and lab, rebuilt and moved', 'Moved a diagnostics company into a new 26,800 sq ft headquarters, including network design, building systems input and lab layout, then relocated a production lab and biobank.', 'New certified and R&D labs built out'),
           ('Mergers and acquisitions', 'More than ten companies, joined into one', 'Integrated systems, networks and applications for more than ten acquisitions, including companies in the US and Europe.', '10+ acquisitions integrated'),
           ('Cost', '$4.5 million out of the IT budget', 'For a global manufacturer: virtualized 80% of servers across six regional hubs, moved the data center to a colocation facility with failover, and restructured outside partners.', '$4.5M cut over two years')]
STANDARD = [('clock', 'A reply within one business day', 'Every message through our contact form gets a real answer from a senior consultant, not an autoresponder.'),
            ('doc', 'Written scope and price first', 'You see the scope, timeline and price in plain English before any work starts.  No surprise invoices.'),
            ('person', 'Senior people do the work', 'The people who scope your project are the people who deliver it.'),
            ('key', 'You own everything', 'Passwords, documentation and admin access stay with you.  We never lock you in.'),
            ('talk', 'Straight answers', "If something doesn't need fixing, we'll say so.  If it's urgent, we'll say that too."),
            ('it-strategy', 'Built for the next five years', 'We design for where the business is going, not for the next invoice.')]
INDUSTRIES = [
 ('flask', 'Life sciences and FDA-regulated companies', 'Medical device, diagnostics and biotech teams where systems, records and audits are under a regulator\'s eye.',
  ['IT controls, access reviews and change management that hold up in audits', 'Experience supporting FDA-regulated and certified clinical lab environments', 'Lab build-outs, biobank moves and validated-system support', 'Account and role management for lab and quality systems']),
 ('compliance', 'Clinical and diagnostics labs', 'Certified labs that cannot stop for an IT problem, from a single site to multiple states and countries.',
  ['Lab network and Wi-Fi design that stays up', 'Physical security for labs: badges, cameras and visitor logs', 'Backups and recovery you have actually tested', 'Support across sites in multiple states and countries']),
 ('factory', 'Manufacturing and distribution', 'Plants, warehouses and offices that need one network, one standard and costs under control.',
  ['Multi-site networks and phone systems', 'Data center and colocation moves', 'ISO 9001, 14001 and 27001 audit support', 'Vendor consolidation and cost reduction']),
 ('briefcase', 'Finance and professional services', 'Firms that live on email, documents and client trust, and answer to auditors and clients.',
  ['SOX IT general controls', 'Microsoft 365 security and licensing', 'Phishing and impersonation defenses', 'Client data protection and access reviews']),
 ('growth', 'Growing and acquiring companies', 'Companies adding sites, people or acquisitions faster than IT can keep up.',
  ['Acquisition IT integration, from first day to full merge', 'Office moves and new building cutovers', 'Roadmaps and budgets for the next three to five years', 'Fractional IT leadership until a full-time hire makes sense']),
]
ENGAGE = [('Projects', 'A defined job with a clear finish line.', 'A fixed scope and a price agreed before work starts.  When it is done, it is documented and handed back to you.',
           ['Written scope, timeline and fixed price', 'One senior lead from start to finish', 'Documentation and handoff when the job is done'], ['Office or headquarters moves', 'Microsoft 365 migrations', 'Network or Wi-Fi refreshes', 'Security assessments', 'Access control installs'], 'one-time needs with a clear goal'),
          ('Managed support', 'We keep it running, every month.', 'A monthly agreement that covers the day-to-day: users, devices, updates, vendors and a real person when something breaks.',
           ['Monitoring and patching', 'User onboarding and offboarding', 'Vendor and license management', 'Help when something breaks', 'A regular review of what changed and what is next'], ['Companies without in-house IT', 'Teams whose IT person left', 'Offices that need backup for a small IT staff'], 'teams without in-house IT'),
          ('Fractional IT leadership', 'A senior IT leader, part time.', 'The judgment of an IT director for a set number of days a month, without a full-time salary.',
           ['Technology roadmap and budget', 'Vendor contract review and negotiation', 'Audit, compliance and risk ownership', 'Leadership and board reporting', 'Hiring and managing outside providers'], ['Growing companies', 'Businesses facing an audit or acquisition', 'Leadership teams that need an IT voice at the table'], 'companies not ready for a full-time IT director')]
QUOTES = [('“[His] commitment to providing his clients with the highest level of service … is unsurpassed!”', 'President, equipment financing firm'),
          ('“Always assured of [his] passion to do what is right, what is technically sound, and what is cost effective.”', 'Former manager'),
          ('“A strong leader (often leading by example) and a great communicator!”', 'President and Chief Operating Officer'),
          ('“[He] is the kind of guy all successful organizations need.”', 'Project manager')]
QUESTIONS = ['Is multi-factor sign-in turned on for every account, including admins?', 'Have you actually restored something from backup in the last six months?',
             'Do people who leave lose access to everything the same day?', 'Are your firewall, servers and laptops patched every month?',
             'Do you know exactly which licenses you pay for, and who uses them?', 'Is there a written plan for what happens if ransomware hits tomorrow?']
PAINS = [('Your IT person left, and nobody knows the passwords.', 'it-strategy'), ("You're not sure you'd survive a ransomware attack.", 'cybersecurity'),
         ("You're paying for Microsoft licenses nobody uses.", 'microsoft-365'), ('The Wi-Fi drops every afternoon, and everyone just lives with it.', 'network'),
         ('An audit is coming and the evidence is scattered everywhere.', 'compliance'), ('Your server closet is one bad day away from a very bad week.', 'cloud'),
         ('Your colocation contract renews next month, and nobody has compared prices in years.', 'data-center'), ('Someone who left months ago still has a badge that opens the front door.', 'access-control'),
         ('Your team types the same order into three different systems.', 'business-automation')]
TESTIMONIALS = json.loads((ROOT / 'build' / 'testimonials.json').read_text())

NAV = [('index.html', 'Home'), ('services.html', 'Services'), ('industries.html', 'Industries'), ('engagement.html', 'How We Work'), ('why-us.html', 'Why Us'), ('about.html', 'About')]

# ---------- page shell ----------
def page(fname, title, desc, body, extra_js=''):
    css, js = ver('assets/css/cali.css'), ver('assets/js/site.js')
    cur = lambda f: ' aria-current="page"' if f == fname or (fname in SVC_FILES and f == 'services.html') else ''
    nav = ''.join(f'<a href="{f}"{cur(f)}>{n}</a>' for f, n in NAV) + f'<a class="nav-cta" href="contact.html"{cur("contact.html")}>Contact us</a>'
    svc_links = ''.join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    full = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0f1c2d">
<link rel="canonical" href="https://caliit.com/{'' if fname == 'index.html' else fname}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Cali IT Consulting"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="https://caliit.com/{'' if fname == 'index.html' else fname}"><meta property="og:image" content="https://caliit.com/assets/brand/og.png">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/archivo-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/cali.css?v={css}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Cali IT Consulting, home">{logo_dark()}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" aria-label="Menu"><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot">
      <div><a class="brand" href="index.html" aria-label="Cali IT Consulting, home">{logo_dark()}</a><p>Senior IT consulting for businesses that can't afford to get it wrong.  Based in Huntington Beach, California.  Serving Southern California on-site and the United States remotely.</p></div>
      <div><h4>Services</h4><ul>{svc_links}</ul></div>
      <div><h4>Company</h4><ul><li><a href="industries.html">Industries</a></li><li><a href="engagement.html">How we work</a></li><li><a href="why-us.html">Why us</a></li><li><a href="about.html">About</a></li><li><a href="testimonials.html">Testimonials</a></li></ul></div>
      <div><h4>Get in touch</h4><ul><li><a href="contact.html">Contact us</a></li><li><a href="why-us.html#check">Free IT health check</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="foot-base"><span>&copy; {YEAR} Cali IT Consulting.  All rights reserved.</span><span>Huntington Beach, California</span></div>
  </div>
</footer>
<script src="assets/js/site.js?v={js}" defer></script>
{extra_js}
</body>
</html>
'''
    (ROOT / fname).write_text(full)

SVC_FILES = {s['slug'] + '.html' for s in SERVICES}

def cta(h='Tell us what you\'re working on.', p='Fill out a short form and a senior consultant will reply within one business day.'):
    return f'''<section class="cta-band section tight">{STATE}<div class="wrap"><div><h2>{h}</h2><p>{p}</p></div><a class="btn btn-primary" href="contact.html" style="background:#8fb3d9;color:#0f1c2d">Contact us</a></div></section>'''

def page_hero(label, h1, lede, crumbs=None):
    cr = f'<div class="crumbs">{crumbs}</div>' if crumbs else f'<div class="label">{label}</div>'
    return f'<section class="page-hero dark">{STATE}<div class="wrap">{cr}<h1>{h1}</h1><p class="lede">{lede}</p></div></section>'

def svc_cards(cls='g3'):
    return f'<div class="grid {cls}">' + ''.join(f'<a class="card reveal" href="{s["slug"]}.html"><div class="ico">{icon(s["slug"])}</div><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="arrow">Learn more</span></a>' for s in SERVICES) + '</div>'

def results_block(dark=False):
    cards = ''.join(f'<div class="card result reveal"><div class="num">{k.upper()}</div><h3 style="margin-top:10px">{t}</h3><p>{d}</p><div class="big">{b}</div></div>' for k, t, d, b in RESULTS)
    return f'<div class="grid g3">{cards}</div><p class="fine">Client names are kept confidential.</p>'

def quotes_block():
    figs = ''.join(f'<figure class="{"on" if i == 0 else ""}"><blockquote>{q}</blockquote><figcaption>{c}</figcaption></figure>' for i, (q, c) in enumerate(QUOTES))
    return f'<section class="section dark"><div class="wrap"><div class="center" style="margin-bottom:26px"><div class="label">In their own words</div></div><div class="quote" id="quoteRot" aria-live="polite">{figs}</div><p class="center" style="margin-top:28px"><a class="arrow" href="testimonials.html">Read the full testimonials</a></p></div></section>'

def standard_block(alt=True):
    cards = ''.join(f'<div class="card reveal"><div class="ico">{icon(i)}</div><h3>{t}</h3><p style="margin:0">{d}</p></div>' for i, t, d in STANDARD)
    return f'''<section class="section{' alt' if alt else ''}" id="standard"><div class="wrap"><div class="section-head"><div class="label">Our standard</div><h2>What you can <em>count on</em>, in writing.</h2><p class="lede">Six commitments we hold ourselves to on every engagement, large or small.</p></div><div class="grid g3">{cards}</div></div></section>'''

# ---------- pages ----------
def home():
    hs = ''.join(f'''<div class="hs-item hs-svc" data-slug="{s['slug']}" aria-hidden="true"><div class="hs-top"><div class="hs-name" data-text="{s['name']}">{s['name']}</div><button type="button" class="hs-x" aria-label="Back to overview">&times;</button></div><h2 class="hs-h">{s['h']}</h2><ul class="hs-list">{''.join(f'<li>{x}</li>' for x in s['get'][:3])}</ul></div>''' for s in SERVICES)
    stats = ''.join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n, t in STATS)
    steps = ''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in STEPS)
    inds = ''.join(f'<li>{t}</li>' for _, t, _, _ in INDUSTRIES)
    eng = ''.join(f'<div class="card reveal"><div class="num">OPTION 0{i + 1}</div><h3 style="margin-top:10px">{t}</h3><p>{s}</p><span class="muted" style="font-size:15px">Best for: {b}.</span></div>' for i, (t, s, _, _, _, b) in enumerate(ENGAGE))
    body = f'''
<section class="hero dark">{HERO_STATE}
  <div class="wrap">
    <div class="copy">
      <div class="hs" id="heroSwap">
        <div class="hs-item hs-default on">
          <div class="label">IT consulting · Huntington Beach, California</div>
          <h1>Senior IT for businesses that <em>can't afford</em> to get it wrong.</h1>
          <p class="lede">Thirty years of running IT inside regulated companies, from FDA-regulated labs to global manufacturers.  We find the gaps, build it right the first time, and keep it running.</p>
          <div class="hero-actions"><a class="btn btn-primary" href="contact.html">Contact us</a><a class="btn btn-ghost" href="services.html">See our services</a></div>
        </div>
        {hs}
      </div>
      <div class="picker" id="picker" aria-label="Pick a service"></div>
      <a class="svc-more" id="svcMore" href="services.html">Explore all services <span aria-hidden="true">→</span></a>
    </div>
    <div>
      <section class="stage" id="stage" aria-label="Interactive cube of our nine services.  Drag to spin, or pick a service.">
        <div class="glow"></div><div class="cube" id="cube"></div><div class="core"><div class="word" id="coreText" aria-live="polite"></div></div>
      </section>
      <p class="stage-hint">Drag the cube or pick a service</p>
    </div>
  </div>
</section>
<section class="proof" aria-label="Experience"><div class="wrap">{stats}</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div class="label">What we do</div><h2>Nine practice areas.  <em>One team.</em></h2><p class="lede">Bring us a single project or hand us the whole stack.  Every engagement is led by senior consultants who have run IT themselves.</p></div>
  {svc_cards()}
</div></section>

<section class="section dark"><div class="wrap">
  <div class="section-head"><div class="label">How we work</div><h2>Assess.  Deploy.  Manage.  <em>Protect.</em></h2><p class="lede">One method for every engagement, so you always know what happens next.</p></div>
  <ol class="steps">{steps}</ol>
</div></section>

<section class="section"><div class="wrap split">
  <div class="reveal">
    <div class="label">Regulated industries</div>
    <h2>Built for businesses that <em>answer to auditors</em>.</h2>
    <p class="lede">Most IT shops stop at HIPAA.  Our team has run IT for FDA-regulated medical device and diagnostics companies, certified clinical labs and publicly traded firms.</p>
    <ul class="checks">{inds}</ul>
    <a class="arrow" href="industries.html">See the industries we serve</a>
  </div>
  <div class="panel reveal">{STATE}
    <div class="label">Audit-ready IT</div>
    <h3 style="font-size:26px">SOX, HIPAA, ISO and FDA-regulated environments.</h3>
    <p style="color:#c3ccd4">IT general controls, access reviews, change management and evidence that is ready before the auditors ask.</p>
    <div class="tags">{''.join(f'<span>{t}</span>' for t in ['SOX', 'HIPAA', 'GDPR', 'ISO 9001', 'ISO 27001', 'CLIA labs', 'FDA-regulated'])}</div>
  </div>
</div></section>

<section class="section alt"><div class="wrap">
  <div class="section-head"><div class="label">Selected results</div><h2>Work we've <em>actually done</em>.</h2></div>
  {results_block()}
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div class="label">Ways to work with us</div><h2>Start with one.  <em>Add another later.</em></h2></div>
  <div class="grid g3">{eng}</div>
  <p style="margin-top:26px"><a class="arrow" href="engagement.html">Compare the options</a></p>
</div></section>

{standard_block()}
{quotes_block()}
{cta()}'''
    js = f'<script src="assets/js/cube.js?v={ver("assets/js/cube.js")}" defer></script>\n<script src="assets/js/heroswap.js?v={ver("assets/js/heroswap.js")}" defer></script>'
    page('index.html', 'Cali IT Consulting | Senior IT for regulated businesses', "Cali IT Consulting: senior IT for businesses that can't afford to get it wrong.  Microsoft 365, cybersecurity, networks, cloud, data centers, compliance and IT strategy.  Huntington Beach, California.", body, js)

def services():
    body = page_hero('Services', 'Everything your IT needs, <em>under one roof</em>.', 'Nine practice areas, one team.  Bring us a single project or hand us the whole stack.') + f'''
<section class="section"><div class="wrap">{svc_cards()}</div></section>
<section class="section alt"><div class="wrap split">
  <div><div class="label">Not sure where to start?</div><h2>Start with an <em>assessment</em>.</h2><p class="lede">We review your environment, rank the risks and hand you a written plan.  You decide what to fix, and who fixes it.</p><a class="btn btn-primary" href="contact.html?topic=IT%20and%20security%20assessment">Ask about an assessment</a></div>
  <div class="card"><h3>What an assessment covers</h3><ul><li>Microsoft 365 and identity security</li><li>Backups and recovery</li><li>Network, firewall and Wi-Fi</li><li>Licensing and vendor spend</li><li>Compliance gaps and evidence</li><li>A ranked, written remediation plan</li></ul></div>
</div></section>
{cta()}'''
    page('services.html', 'Services | Cali IT Consulting', 'Microsoft 365, cybersecurity, network, cloud, data center, compliance, access control, business automation and IT strategy.', body)

def service(s):
    pains = ''.join(f'<div class="card reveal"><h3>{t}</h3><p style="margin:0">{d}</p></div>' for t, d in s['pains'])
    gets = ''.join(f'<li>{g}</li>' for g in s['get'])
    plat = ''.join(f'<span>{p}</span>' for p in s['plat'])
    ct, cs, cl, co = s['case']
    others = ''.join(f'<a class="card reveal" href="{o["slug"]}.html"><div class="ico">{icon(o["slug"])}</div><h3 style="font-size:17px;margin:0">{o["name"]}</h3></a>' for o in SERVICES if o is not s)
    body = page_hero('', s['h'], s['intro'], crumbs=f'<a href="services.html">Services</a> &nbsp;/&nbsp; <span>{s["name"]}</span>') + f'''
<section class="section"><div class="wrap">
  <div class="section-head"><div class="label">Sound familiar?</div><h2>The problems we <em>usually hear</em>.</h2></div>
  <div class="grid g3">{pains}</div>
</div></section>
<section class="section alt"><div class="wrap split" style="align-items:start">
  <div><div class="label">What you get</div><h2>{s["name"]}, <em>done right</em>.</h2><ul class="checks">{gets}</ul><a class="btn btn-primary" href="contact.html?topic={E(s["name"])}">Talk to us about {s["name"]}</a></div>
  <div><div class="panel">{STATE}<div class="label">From the field</div><h3 style="font-size:24px">{ct}</h3><p style="color:#c3ccd4">{cs}</p><ul class="checks">{''.join(f'<li>{x}</li>' for x in cl)}</ul><p style="color:#fff;font-weight:600;margin:0">{co}</p></div><p class="fine">Client names are kept confidential.</p>
  <div style="margin-top:22px"><div class="label">Platforms and standards</div><div class="tags">{plat}</div></div></div>
</div></section>
<section class="section"><div class="wrap"><div class="section-head"><div class="label">Other services</div><h2>One team for the <em>whole stack</em>.</h2></div><div class="grid g4">{others}</div></div></section>
{cta(f"Let's talk about {s['name']}.")}'''
    page(s['slug'] + '.html', f'{s["name"]} | Cali IT Consulting', f'{s["name"]} from Cali IT Consulting.  {s["intro"].split("  ")[0]}', body)

def industries():
    blocks = ''.join(f'''<div class="card reveal"><div class="ico">{icon(i)}</div><h3>{t}</h3><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in l)}</ul></div>''' for i, t, d, l in INDUSTRIES)
    body = page_hero('Industries', 'IT for businesses that <em>answer to someone</em>.', 'Regulators, auditors, clients or a board.  Our team has run IT where downtime and audit findings are not an option.') + f'''
<section class="section"><div class="wrap"><div class="grid g2">{blocks}</div></div></section>
<section class="section dark"><div class="wrap split">
  <div><div class="label">Why it matters</div><h2>Regulated IT is <em>different</em>.</h2><p class="lede">In a regulated company, a change isn't finished until it is documented, approved and provable.  We work that way by default, whatever your industry.</p></div>
  <ul class="checks"><li>Every change written down and traceable</li><li>Access granted by role, reviewed on a schedule, removed the day someone leaves</li><li>Backups tested, with the results on file</li><li>Policies that match what you actually do</li><li>Evidence ready before the auditors ask</li></ul>
</div></section>
{cta("Tell us about your environment.")}'''
    page('industries.html', 'Industries | Cali IT Consulting', 'IT consulting for life sciences, FDA-regulated companies, clinical labs, manufacturing, finance and growing companies.', body)

def engagement():
    cards = ''.join(f'''<div class="card reveal"><div class="num">OPTION 0{n + 1}</div><h3 style="margin-top:10px;font-size:24px">{t}</h3><p style="font-weight:600;color:#0f1c2d">{s}</p><p>{d}</p><h4>What's included</h4><ul>{''.join(f'<li>{x}</li>' for x in inc)}</ul><h4>Typical examples</h4><ul>{''.join(f'<li>{x}</li>' for x in ex)}</ul><div class="best"><b>Best for:</b> {b}.</div></div>''' for n, (t, s, d, inc, ex, b) in enumerate(ENGAGE))
    start = ''.join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in [('Send us a message', "Tell us what's going on through the contact form.  We reply within one business day."), ('Get a written proposal', 'A clear scope, timeline and price, in plain English.  No surprises later.'), ('Kick off', 'We get to work, keep you posted and document everything as we go.'), ('Hand-off or ongoing', 'Projects end with documentation you own.  Managed and fractional work continue month to month.')])
    body = page_hero('How we work', 'Work with us <em>the way that fits</em>.', 'One job, ongoing support or a senior IT leader part time.  Start with one, add another later.') + f'''
<section class="section"><div class="wrap engage"><div class="grid g3">{cards}</div><p class="fine">Many clients combine them: a project to fix the foundation, then managed support to keep it that way.</p></div></section>
<section class="section dark"><div class="wrap"><div class="section-head"><div class="label">Getting started</div><h2>How an engagement <em>starts</em>.</h2></div><ol class="steps">{start}</ol></div></section>
{standard_block()}
{cta("Let's find the right fit.")}'''
    page('engagement.html', 'How We Work | Cali IT Consulting', 'Projects, managed support or fractional IT leadership.  Written scope and price before work starts.', body)

def why():
    qs = ''.join(f'<li data-q="{i}"><p>{q}</p><div class="yn"><button type="button" data-v="1" aria-pressed="false">Yes</button><button type="button" data-v="0" aria-pressed="false">No</button></div></li>' for i, q in enumerate(QUESTIONS))
    pains = ''.join(f'<a class="card reveal" href="{s}.html"><p style="color:#0f1c2d;font-weight:600;font-size:17px">{t}</p><span class="arrow">{SVC[s]["name"]}</span></a>' for t, s in PAINS)
    body = page_hero('Why Cali IT', 'Why teams choose <em>Cali IT</em>.', "Thirty years of running IT inside companies where downtime and audit findings aren't an option.  Here's what that means for you.") + f'''
<section class="section" id="check"><div class="wrap">
  <div class="section-head"><div class="label">Free 60-second IT health check</div><h2>Where do you <em>stand</em>?</h2><p class="lede">Six honest questions.  No email required, and your answers stay in your browser.</p></div>
  <div class="check">
    <div class="gauge"><div class="gauge-num" id="gaugeNum">0<small> of {len(QUESTIONS)}</small></div><h3 id="verdictTitle">Answer the questions</h3><p id="verdictText">Every "No" is a gap worth closing.  Most businesses we meet have at least two.</p><a class="btn btn-primary" id="checkCta" href="contact.html" hidden style="background:#8fb3d9;color:#0f1c2d">Send us your results</a></div>
    <ol class="questions" id="questions">{qs}</ol>
  </div>
</div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div class="label">Sound familiar?</div><h2>If you nodded at any of these, <em>we should talk</em>.</h2></div><div class="grid g3">{pains}</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div class="label">Selected results</div><h2>Work we've <em>actually done</em>.</h2></div>{results_block()}</div></section>
{standard_block()}
{cta()}'''
    page('why-us.html', 'Why Us | Cali IT Consulting', 'Senior IT consultants with 30 years of experience in regulated companies.  Take the free 60-second IT health check.', body)

def about():
    stats = ''.join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n, t in STATS)
    vals = ''.join(f'<div class="card reveal"><h3>{t}</h3><p style="margin:0">{d}</p></div>' for t, d in [('Straight answers', "Plain English, no jargon.  If something doesn't need fixing, we'll say so."), ('Senior people', 'The people who scope your project are the ones who do the work.'), ('Documented', "Every change is written down, so you're never locked in to us."), ('Built to last', 'We design for the next five years, not the next invoice.')])
    body = page_hero('About us', 'Built by people who <em>ran IT</em>, not just sold it.', "Cali IT Consulting brings 30 years of IT leadership to businesses that can't afford downtime.") + f'''
<section class="section"><div class="wrap split" style="align-items:start">
  <div><div class="label">Who we are</div><h2>Senior consultants.  <em>Real experience.</em></h2></div>
  <div class="prose"><p class="lede">Our team has run technology for FDA-regulated medical device and diagnostics companies, global manufacturers and growing firms.</p>
  <p>We've led more than ten acquisitions, moved headquarters and data centers, built certified labs, and passed SOX, HIPAA and ISO audits.  We handle Microsoft 365, cybersecurity, networks, cloud, data centers, physical security, compliance and IT strategy.</p>
  <p>We're based in Huntington Beach, California.  We work on-site across Southern California and remotely anywhere in the United States.  You get senior-level answers from people who have done the work, not a sales pitch.</p></div>
</div></section>
<section class="proof" aria-label="Experience"><div class="wrap">{stats}</div></section>
<section class="section alt"><div class="wrap"><div class="section-head"><div class="label">How we work</div><h2>What we <em>stand for</em>.</h2></div><div class="grid g4">{vals}</div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div class="label">Selected results</div><h2>Work we've <em>actually done</em>.</h2></div>{results_block()}</div></section>
{quotes_block()}
{cta("Let's talk about your environment.")}'''
    page('about.html', 'About | Cali IT Consulting', 'Cali IT Consulting: senior IT consultants with 30 years of leadership in regulated companies.  Huntington Beach, California.', body)

def testimonials():
    cards = ''
    for t in TESTIMONIALS:
        paras = ''.join(f'<p style="color:#2b3644;font-size:16.5px">{E(p)}</p>' for p in t['paras'])
        cap = t['cap'][0]; sub = t['cap'][1] if len(t['cap']) > 1 else ''
        cards += f'<figure class="card reveal" style="margin:0"><div style="font:700 54px/0.6 var(--accent);color:#8fb3d9;margin-bottom:10px">&ldquo;</div>{paras}<figcaption style="border-top:1px solid #e2e7ee;padding-top:14px"><b style="font-family:var(--head)">{E(cap)}</b><br><span class="muted" style="font-size:14px">{E(sub)}</span></figcaption></figure>'
    body = page_hero('Testimonials', 'In their <em>own words</em>.', 'What the people we have worked for, and alongside, have said about the work.  Quoted from LinkedIn recommendations, with names left out for privacy.') + f'''
<section class="section"><div class="wrap"><div class="grid g2">{cards}</div></div></section>
{cta()}'''
    page('testimonials.html', 'Testimonials | Cali IT Consulting', 'What clients and colleagues say about working with the Cali IT Consulting team.', body)

def contact():
    opts = ''.join(f'<option>{E(t)}</option>' for t in TOPICS)
    sizes = ''.join(f'<option>{t}</option>' for t in ['1 to 10 people', '11 to 50 people', '51 to 200 people', '200+ people'])
    body = page_hero('Contact', 'Contact <em>us</em>.', "Have a question or a project in mind?  Fill out the form and a senior consultant will get back to you within one business day.") + f'''
<section class="section"><div class="wrap contact-grid">
  <form class="form" id="contactForm" novalidate>
    <h2 style="font-size:28px">Send us a message</h2>
    <div class="row"><div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required maxlength="120"></div>
    <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization" maxlength="160"></div></div>
    <div class="row"><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="200"></div>
    <div class="field"><label for="f-phone">Phone <small>(optional)</small></label><input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="40"></div></div>
    <div class="row"><div class="field"><label for="f-topic">What can we help with?</label><select id="f-topic" name="topic" required><option value="">Choose one</option>{opts}</select></div>
    <div class="field"><label for="f-size">Company size</label><select id="f-size" name="size"><option value="">Choose one</option>{sizes}</select></div></div>
    <div class="field"><label for="f-msg">Tell us about it</label><textarea id="f-msg" name="message" required maxlength="5000"></textarea></div>
    <div class="hp" aria-hidden="true"><label for="f-hp">Leave this empty</label><input id="f-hp" name="_honey" tabindex="-1" autocomplete="off"></div>
    <button class="btn btn-primary" type="submit">Send message</button>
    <p class="form-msg" id="formMsg" role="alert" hidden></p>
    <p class="form-note">We only use your details to reply to you.  See our <a href="privacy.html">privacy policy</a>.</p>
  </form>
  <aside class="side">
    <div class="block"><b>Headquarters</b><p>Huntington Beach, California</p></div>
    <div class="block"><b>Southern California</b><p>On-site and remote support</p></div>
    <div class="block"><b>Nationwide</b><p>Remote support anywhere in the United States</p></div>
    <div class="block"><b>Response time</b><p>A reply from a senior consultant within one business day</p></div>
  </aside>
</div></section>'''
    page('contact.html', 'Contact | Cali IT Consulting', 'Contact Cali IT Consulting.  A senior consultant will reply within one business day.', body)

def thanks():
    body = page_hero('Message sent', 'Thanks.  <em>We got it.</em>', 'A senior consultant will reply within one business day.') + '<section class="section"><div class="wrap center"><a class="btn btn-primary" href="index.html">Back to the home page</a></div></section>'
    page('thanks.html', 'Thank you | Cali IT Consulting', 'Your message was sent.', body.replace('<section class="page-hero', '<section class="page-hero', 1))

def privacy():
    body = page_hero('Privacy', 'Privacy <em>policy</em>.', f'Effective October 25, {YEAR}.') + '''
<section class="section"><div class="wrap prose">
<h2>Who we are</h2><p>This website is operated by Cali IT Consulting.  This policy explains what information we collect through the site, how we use it and who we share it with.</p>
<h2>Information we collect</h2><p>When you send us a message through the contact form, we collect what you enter: your name, company, email address, phone number (optional), what you need help with, your company size and your message.</p>
<p>The IT health check on our Why Us page runs entirely in your browser.  Your answers are not sent to us unless you choose to include them in a message.</p>
<p>We count page visits without cookies.  The count records only which page was viewed and the date.  It does not record your IP address, your device or who you are.</p>
<p>Like any website, the services that host and deliver this site may receive standard technical information when a page loads, such as your IP address and browser type.</p>
<p>We do not use cookies, advertising trackers or third-party analytics on this site.</p>
<h2>How we use it</h2><p>We use the information you send us to reply to you and to provide the services you ask about.  We do not sell or rent your information, and we do not use it for advertising.</p>
<h2>Who we share it with</h2><p>We share information only with the service providers that run this site and deliver your message:</p>
<ul><li><b>Supabase</b> stores contact form messages and the anonymous page counts.</li><li><b>FormSubmit</b> delivers a copy of each contact form message to our email.</li><li><b>GitHub Pages</b> hosts this website.</li><li><b>Cloudflare</b> provides the domain name service for this website.</li><li>Our <b>email provider</b> receives and stores the messages you send us.</li></ul>
<p>The fonts on this site are served from this website itself, not from an outside font service.  We may also disclose information if required by law.</p>
<h2>Do Not Track</h2><p>We do not track visitors over time or across other websites, so the site does not change its behavior in response to browser Do Not Track signals.</p>
<h2>Reviewing or changing your information</h2><p>To review, correct or delete information you've sent us, send a request through our <a href="contact.html">contact form</a>.</p>
<h2>Changes to this policy</h2><p>If we change this policy, we'll post the new version here and update the effective date at the top.</p>
</div></section>'''
    page('privacy.html', 'Privacy | Cali IT Consulting', 'How Cali IT Consulting handles information sent through this website.', body)

def notfound():
    body = page_hero('Page not found', 'This page <em>broke out of the cube</em>.', "The page you're looking for isn't here.  Try the home page or our services.") + '<section class="section"><div class="wrap center"><a class="btn btn-primary" href="index.html">Home page</a> &nbsp; <a class="btn btn-ghost" href="services.html">Services</a></div></section>'
    page('404.html', 'Page not found | Cali IT Consulting', 'Page not found.', body)

if __name__ == '__main__':
    home(); services(); [service(s) for s in SERVICES]; industries(); engagement(); why(); about(); testimonials(); contact(); thanks(); privacy(); notfound()
    print('built', 2 + len(SERVICES) + 9, 'pages')
