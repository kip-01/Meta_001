#!/usr/bin/env python3
"""Generates the Meta_001 static site into /home/claude/Meta_001."""
import html, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
E = lambda s: html.escape(str(s), quote=True)
WA_URL = 'https://wa.me/%s' % WA
TEL = 'tel:%s' % PHONE_TEL
PROJ = {p['id']: p for p in PROJECTS}
FIELD_NAME = dict(FIELDS)

IC = {
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .1-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'email': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/></svg>',
 'medium': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="7" cy="12" r="5"/><ellipse cx="16.5" cy="12" rx="2.6" ry="5"/><ellipse cx="21.2" cy="12" rx="1" ry="4.4"/></svg>',
 'github': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.7c-2.8.6-3.4-1.3-3.4-1.3-.5-1.1-1.1-1.4-1.1-1.4-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.3 1.1 2.9.8.1-.6.3-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.300.1-2.700 0 0 .8-.3 2.800 1a9.600 9.600 0 0 1 5 0c1.900-1.300 2.800-1 2.800-1 .5 1.400.2 2.400.1 2.700.6.700 1 1.600 1 2.700 0 3.900-2.400 4.700-4.600 5 .4.300.7.900.7 1.800v2.700c0 .3.200.6.700.5A10 10 0 0 0 12 2z"/></svg>',
 'youtube': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.100-2.100C19 4.600 12 4.600 12 4.600s-7 0-8.900.5A3 3 0 0 0 1 7.200 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.800a3 3 0 0 0 2.100 2.100c1.900.5 8.900.5 8.900.5s7 0 8.900-.5a3 3 0 0 0 2.100-2.100A31 31 0 0 0 23.500 12 31 31 0 0 0 23 7.200zM9.700 15.200V8.800L15.800 12z"/></svg>',
 'linkedin': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.500 3A2 2 0 1 0 4.500 7 2 2 0 0 0 4.500 3zM3 9h3v12H3zm6 0h2.900v1.700c.5-.9 1.700-2 3.500-2 3.500 0 4.100 2.300 4.100 5.300V21h-3v-6c0-1.400 0-3.200-2-3.200s-2.300 1.500-2.300 3.100V21H9z"/></svg>',
 'instagram': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.500" cy="6.500" r="1" fill="currentColor"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.800 3h3.100l-6.800 7.800L22 21h-6.200l-4.900-6.400L5.300 21H2.200l7.300-8.300L2 3h6.400l4.400 5.800zm-1.100 16.200h1.700L7.400 4.700H5.600z"/></svg>',
 'facebook': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8V6.500c0-.7.200-1 1.200-1H17V2h-2.800C11 2 10 3.700 10 6v2H8v3.500h2V22h4V11.500h2.800L17.300 8z"/></svg>',
 'tiktok': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.500 2h-3.200v13.200a2.800 2.800 0 1 1-2.800-2.800c.3 0 .6 0 .8.100V9.300a6 6 0 1 0 5.200 5.900V8.600a7 7 0 0 0 4 1.300V6.700A4.300 4.300 0 0 1 16.500 2z"/></svg>',
 'play': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4v16l14-8z"/></svg>',
 'pal': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a9 9 0 1 0 0 18c1.100 0 1.800-.8 1.800-1.700 0-.5-.2-.9-.5-1.200-.3-.3-.5-.7-.5-1.200 0-.9.700-1.600 1.600-1.600H17a4 4 0 0 0 4-4C21 6.500 17 3 12 3z"/><circle cx="7.500" cy="11" r="1"/><circle cx="12" cy="7.500" r="1"/><circle cx="16.500" cy="11" r="1"/></svg>',
}
HANDLE_ICON = {'whatsapp': 'wa', 'phone': 'phone', 'email': 'email', 'medium': 'medium', 'github': 'github', 'youtube': 'youtube', 'linkedin': 'linkedin', 'instagram': 'instagram', 'x': 'x', 'facebook': 'facebook', 'tiktok': 'tiktok'}

NAV = [('index.html', 'Dashboard', 'index'), ('work.html', 'Work', 'work'), ('business.html', 'Business', 'business'), ('more.html', 'More', 'more'), ('media.html', 'Media', 'media'), ('medium.html', 'Medium', 'medium'), ('contact.html', 'Contact', 'contact')]
SCHEME_TILES = [('lagoon', 'Lagoon', ['#FBF6EC', '#0E7C86', '#22D3EE', '#FF6B4A', '#0B1B1E']), ('midnight', 'Midnight', ['#070B0C', '#14B8A6', '#5EEAD4', '#FFB020', '#111A1C']), ('savanna', 'Savanna', ['#F4F5F3', '#0A5C63', '#19A7B5', '#F59E0B', '#12201F']), ('reef', 'Reef', ['#EAF7F7', '#0B8F9A', '#00D1E0', '#FF7A59', '#06353B'])]


def sw_buttons(extra=''):
    out = ''
    for k, n, cols in SCHEME_TILES:
        out += '<button class="sw" type="button" data-scheme="%s" aria-pressed="false"><span>%s</span>%s</button>' % (k, ''.join('<b style="background:%s"></b>' % c for c in cols), n)
    return out


def art(seed, kind=''):
    cx, cy = 20 + (seed * 37) % 60, 25 + (seed * 23) % 50
    rot = (seed * 29) % 180
    rings = ''.join('<ellipse cx="%d%%" cy="%d%%" rx="%d" ry="%d" transform="rotate(%d %d %d)" fill="none" stroke="%s" stroke-opacity="%.2f" stroke-width="2"/>' % (cx, cy, 18 + i * 20, 11 + i * 13, rot, 4 * cx, 2.5 * cy, 'var(--brand2)' if i % 3 else 'var(--accent)', max(.15, .75 - i * .06)) for i in range(11))
    return '<svg viewBox="0 0 400 250" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="400" height="250" fill="var(--panel)"/><circle cx="%d%%" cy="%d%%" r="120" fill="var(--brand)" opacity=".35"/>%s</svg>' % (cx, cy, rings)


def head(title, desc, page, base=''):
    t = title if page == 'index' else title + ' · ' + NAME
    ld = ''
    if page == 'index':
        ld = '<script type="application/ld+json">%s</script>' % json.dumps({'@context': 'https://schema.org', '@type': 'Person', 'name': NAME, 'jobTitle': 'Project and resilience practitioner', 'telephone': PHONE_TEL, 'email': EMAIL, 'url': SITE_URL, 'address': {'@type': 'PostalAddress', 'addressLocality': 'Kakamega', 'addressCountry': 'KE'}, 'sameAs': ['https://medium.com/@kiprop', 'https://github.com/kip-01']})
    return '''<!doctype html>
<html lang="en-KE"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><meta name="description" content="%s">
<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website"><meta name="theme-color" content="#0E7C86">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='9' fill='%%230E7C86'/%%3E%%3Ctext x='16' y='22' font-size='16' font-family='sans-serif' font-weight='700' text-anchor='middle' fill='%%2322D3EE'%%3EKH%%3C/text%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap">
%s<link rel="stylesheet" href="%sassets/css/app.css"><script>try{var s=localStorage.getItem('scheme');if(s&&s!=='lagoon')document.documentElement.setAttribute('data-scheme',s)}catch(e){}</script>
%s</head><body>
<a class="skip" href="#main">Skip to content</a><div class="bar-progress" aria-hidden="true"></div>
''' % (E(t), E(desc), E(t), E(desc), '<base href="/Meta_001/">\n' if page == '404' else '', base, ld)


def header(active):
    links = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if k == active else '', n) for h, n, k in NAV)
    return '''<header class="top"><div class="wrap">
<a class="brand" href="index.html"><i>KH</i>%s</a>
<nav class="nav" id="nav" aria-label="Main">%s</nav>
<div class="acts">
<div class="pal"><button class="btn sm pal-btn" type="button" aria-expanded="false" aria-label="Choose a colour scheme">%s<span class="hide-m">Colours</span></button><div class="pal-pop" role="group" aria-label="Colour schemes">%s</div></div>
<a class="btn sm dark hide-m" href="%s">%s Call</a>
<a class="btn sm accent" href="%s" target="_blank" rel="noopener" aria-label="WhatsApp 0716 494 214">%s <span class="hide-m">WhatsApp</span></a>
<button class="btn sm menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
</div></div></header>
''' % (E(NAME), links, IC['pal'], sw_buttons(), TEL, IC['phone'], WA_URL + '?text=' + 'Hello%20Kiprop%2C%20', IC['wa'])


def footer(fab=True):
    hd = ''.join('<li><a href="%s"%s>%s</a></li>' % (E(u), ' target="_blank" rel="noopener"' if u.startswith('http') else '', E(n + ': ' + v)) for _, n, v, u in HANDLES)
    pages = ''.join('<li><a href="%s">%s</a></li>' % (h, n) for h, n, _ in NAV) + '<li><a href="articles.html">All Medium articles</a></li>'
    f = '''<footer><div class="wrap cols"><div><h4>%s</h4><p>Climate resilience, peacebuilding, compliance and community enterprise. Kakamega, Kenya.</p><p><a href="%s">Call %s</a> · <a href="%s" target="_blank" rel="noopener">WhatsApp</a></p><p style="font-size:.85rem;opacity:.8">No cookies, no tracking. Designed in Figma, published on GitHub Pages.</p></div>
<div><h4>Pages</h4><ul>%s</ul></div><div><h4>Reach me</h4><ul>%s</ul></div></div></footer>
<div class="toast" role="status" aria-live="polite"></div>''' % (E(NAME), TEL, PHONE_DISPLAY, WA_URL, pages, hd)
    if fab:
        f += '<div class="fab"><a class="c" href="%s" aria-label="Call 0716 494 214">%s</a><a class="w" href="%s" target="_blank" rel="noopener" aria-label="WhatsApp 0716 494 214">%s</a></div>' % (TEL, IC['phone'], WA_URL, IC['wa'])
    return f + '<script src="assets/js/app.js" defer></script></body></html>\n'


def write(name, content):
    p = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(content)


def page(name, title, desc, active, body, fab=True):
    write(name, head(title, desc, active if name != '404.html' else '404') + header(active) + '<main id="main">' + body + '</main>' + footer(fab))


def chips_fields(extra_all=True):
    c = '<button class="chip" type="button" data-field-chip="all" aria-pressed="true">All</button>'
    return c + ''.join('<button class="chip" type="button" data-field-chip="%s" aria-pressed="false">%s</button>' % (k, E(n)) for k, n in FIELDS)


def wa_for(text):
    import urllib.parse
    return WA_URL + '?text=' + urllib.parse.quote(text)


def proj_href(p, from_work=False):
    if p['id'] == 'terraheal': return 'business.html#terraheal'
    return 'work.html#' + p['id']


def mini(p, n=3):
    return ''.join('<span><b>%s</b> %s</span>' % (E(a), E(b)) for a, b in p['metrics'][:n])


# ================================================================ INDEX
def index():
    # KPI tiles
    K = [('5,000+', 'households supported by K4RC programmes', 'climate peace', 'K4RC, Samburu (CV figure)'), ('45%', 'fewer conflict incidents in target areas', 'peace', 'K4RC, Wamba'),
         ('450+', 'people at 18 dialogue forums', 'peace', 'K4RC cross-border forums'), ('1,200+', 'households reached through Mseto', 'climate wash', 'Mseto, five counties'),
         ('800+', 'smallholders linked to markets', 'climate', 'K4RC input suppliers and buyers'), ('7', 'households relocated and compensated', 'compliance', 'TerraOre, Ikolomani'),
         ('800+', 'product lines tracked at the pharmacy', 'enterprise', 'TerraHeal inventory'), ('17', 'impact stories written', 'climate peace', 'K4RC beneficiary stories')]
    kp = ''.join('<div class="kpi" data-fields="%s" tabindex="0"><b data-count="%s">%s</b><span>%s</span><div class="src">%s</div></div>' % (f, E(n), E(n), E(l), E(s)) for n, l, f, s in K)
    # bars: items per field
    cnt = {k: sum(1 for p in PROJECTS if k in p['fields']) for k, _ in FIELDS}
    mx = max(cnt.values())
    bars = ''.join('<button class="bar" type="button" data-bar="%s" aria-pressed="false" style="--w:%.2f"><span>%s</span><i></i><b>%d</b></button>' % (k, cnt[k] / mx, E(n), cnt[k]) for k, n in FIELDS)
    # gantt
    y0, y1 = 2016, 2027.0
    bars_g = ''
    for r in ROLES:
        a = r['start'][0] + (r['start'][1] - 1) / 12.0
        b = r['end'][0] + (r['end'][1] - 1) / 12.0 if r['end'][1] <= 12 else r['end'][0] + 11.5 / 12
        w = max(8.0, (b - a) / (y1 - y0) * 100); l = min((a - y0) / (y1 - y0) * 100, 100 - w)
        name = {'terraheal': 'TerraHeal', 'terraore': 'TerraOre', 'k4rc': 'K4RC', 'mseto': 'Mseto', 'kmfri': 'KMFRI'}[r['id']]
        bars_g += '<div class="g-row"><button class="g-bar" type="button" data-fields="%s" data-title="%s" data-org="%s" data-when="%s" data-lead="%s" aria-pressed="false" style="left:%.1f%%;width:%.1f%%">%s</button></div>' % (' '.join(r['fields']), E(r['title']), E(r['org']), E(r['when']), E(r['bullets'][0]), l, w, name)
    axis = ''.join('<span>%d</span>' % y for y in range(2016, 2027, 2))
    # stack
    feat = ['k4rc', 'terraheal', 'terraore', 'jeep']
    st = ''
    for i, pid in enumerate(feat):
        p = PROJ[pid]
        st += '''<article class="sc rv" style="--i:%d" data-fields="%s"><div><span class="tag %s">%s</span><h3 style="margin-top:12px">%s</h3><p>%s</p><div class="mini">%s</div><a class="btn accent" href="%s">Open the full story</a></div><div class="art">%s</div></article>''' % (
            i, ' '.join(p['fields']), p['kind'], p['kind'], E(p['name']), E(p['hook'] + ' ' + p['summary'].split('. ')[0] + '.'), mini(p), proj_href(p), art(i * 5 + 3))
    # medium + media strips
    arts = ''.join(story_card(a, 'medium') for a in sorted(ARTICLES, key=lambda a: a['date'], reverse=True)[:3])
    vids = ''.join(video_card(v, compact=True) for v in VIDEOS)
    body = '''
<section class="hero"><div class="wrap">
<div><span class="eyebrow">Project and resilience practitioner · Kakamega, Kenya</span>
<h1>Programmes that hold when <span class="grad">the rains don't.</span></h1>
<p class="lede">I design and run work where climate, livelihoods and conflict overlap, from pastoral Samburu to mining country in Kakamega. I also run TerraHeal, a pharmacy, and I led community and compliance work at TerraOre.</p>
<div class="cta"><a class="btn accent" href="%s" target="_blank" rel="noopener">%s WhatsApp %s</a><a class="btn dark" href="%s">%s Call</a><a class="btn" href="#console">Open the dashboard</a></div></div>
<div class="floaters" aria-label="Current and recent work">
<a class="fl" href="business.html#terraheal"><small>Now</small><b>TerraHeal Pharmaceuticals</b><em>Pharmacy operations, supply and systems</em></a>
<a class="fl" href="business.html#terraore"><small>2024 to 2025</small><b>TerraOre community and CSR</b><em>Relocation, licensing, engagement</em></a>
<a class="fl" href="medium.html"><small>Writing</small><b>Stories from the field</b><em>Eight articles on Medium</em></a></div>
</div></section>

<section id="console" style="padding-top:20px"><div class="wrap"><div class="console" data-filter-scope>
<span class="eyebrow">Impact console</span><h2>Numbers behind the work. Pick a field.</h2>
<div class="chips" role="group" aria-label="Filter by field">%s</div>
<div class="kpis">%s</div>
<div class="console-grid">
<div class="card-in"><h3>Items per field</h3><p style="font-size:.9rem;color:var(--panel-muted)">Click a bar to filter this page. Stories shown below: <span data-visible-count style="color:var(--brand2);font-weight:700"></span></p><div class="bars">%s</div></div>
<div class="card-in"><h3>Ten years on one line</h3><div class="gantt"><div class="g-axis" aria-hidden="true">%s</div>%s<div class="g-info" id="g-info" aria-live="polite">Hover or tap a bar to see the role.</div></div></div>
</div></div></div></section>

<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Selected work</span><h2>Four stories, stacked.</h2></div><p>Scroll and the cards stack. Each opens a full write-up with the numbers and my part in it. <a href="work.html">See all nine items.</a></p></div>
<div class="stack" data-filter-scope>%s</div></div></section>

<section class="band"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">On Medium</span><h2>Notes from the field.</h2></div><a class="btn accent" href="medium.html">Open the Medium landing page</a></div><div class="grid">%s</div></div></section>

<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Media</span><h2>Watch the work.</h2></div><a class="btn" href="media.html">All videos</a></div><div class="vgrid">%s</div></div></section>

<section class="soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Next step</span><h2>Have a project, a bid or a pharmacy question?</h2></div></div>
<div class="cta" style="margin-top:0"><a class="btn accent" href="%s" target="_blank" rel="noopener">%s WhatsApp %s</a><a class="btn dark" href="%s">%s Call %s</a><a class="btn" href="more.html">Everything else, on More</a></div></div></section>
''' % (WA_URL + '?text=Hello%20Kiprop%2C%20', IC['wa'], PHONE_DISPLAY, TEL, IC['phone'], chips_fields(), kp, bars, axis, bars_g, st, arts, vids, WA_URL + '?text=Hello%20Kiprop%2C%20', IC['wa'], PHONE_DISPLAY, TEL, IC['phone'], PHONE_DISPLAY)
    page('index.html', 'Kiprop Haggai: resilience, peace and enterprise', 'Dashboard portfolio of Kiprop Haggai: climate resilience, peacebuilding, environmental compliance, TerraHeal Pharmaceuticals, TerraOre and Medium articles. Call or WhatsApp 0716 494 214.', 'index', body)


# ================================================================ shared cards
def story_card(a, mode='medium'):
    d = datetime.date.fromisoformat(a['date']).strftime('%d %b %Y')
    ph = '<img src="%s" alt="" loading="lazy" referrerpolicy="no-referrer">' % E(a['img']) if a['img'] else '<span class="mono">%s</span>' % E(a['title'][0])
    return '<a class="story" href="%s" target="_blank" rel="noopener" data-topics="%s"><div class="ph">%s</div><div class="b"><span class="eyebrow" style="margin:0">%s · %s%s</span><h3>%s</h3><p>%s</p><span class="read">Read on Medium →</span></div></a>' % (
        E(a['url']), E('|'.join(a['topics'])), ph, E(' · '.join(a['topics'])), d, ' · reprint' if a.get('reprint') else '', E(a['title']), E(a['blurb']))


def video_card(v, compact=False):
    return '''<div class="vid"><button class="thumb" type="button" data-yt="%s" data-title="%s" aria-label="Play video: %s"><img alt="" referrerpolicy="no-referrer"><span class="fallback">%s</span><span class="play">%s</span><span class="dur">%s</span></button><div class="body"><span class="eyebrow" style="margin-bottom:6px">%s · %s</span><h3>%s</h3><p style="color:var(--muted);margin:0 0 10px">%s</p><a class="btn sm" href="https://youtu.be/%s" target="_blank" rel="noopener">%s Watch on YouTube</a></div></div>''' % (
        v['id'], E(v['title']), E(v['title']), E(v['title']), IC['play'], v['dur'], E(v['channel']), v['date'], E(v['title']), E(v['blurb']), v['id'], IC['youtube'])


# ================================================================ WORK
def work():
    cards, tpls = '', ''
    for p in PROJECTS:
        if p['id'] == 'terraheal':
            href = 'href="business.html#terraheal"'; tagname = 'a'; attrs = ''
        else:
            tagname = 'button'; attrs = ' type="button" data-open="%s"' % p['id']; href = ''
        pts = ''.join('<span>%s %s</span>' % (E(a), E(b)) for a, b in p['metrics'][:3])
        img = '<img src="assets/img/%s" alt="" loading="lazy">' % p['photo'] if p.get('photo') else art(PROJECTS.index(p) * 7 + 2)
        cards += '<%s class="card has-pts rv" %s%s data-fields="%s"><div class="art">%s<div class="pts">%s</div></div><div class="body"><span class="tag %s" style="align-self:flex-start">%s</span><h3>%s</h3><p>%s</p><span class="meta">%s · %s</span><span class="more-link">%s →</span></div></%s>' % (
            tagname, href, attrs, ' '.join(p['fields']), img, pts, p['kind'], p['kind'], E(p['name']), E(p['hook']), E(p['place']), E(p['when']), 'Open the business page' if p['id'] == 'terraheal' else 'Open details', tagname)
        if p['id'] == 'terraheal': continue
        m = ''.join('<div><b>%s</b><small>%s</small></div>' % (E(a), E(b)) for a, b in p['metrics'][:4])
        pl = ''.join('<li><b>%s</b>%s</li>' % (E(a), E(b)) for a, b in p['points'])
        mine = ''.join('<li>%s</li>' % E(x) for x in p['mine'])
        facts = ''.join('<p style="margin:0 0 6px"><b>%s:</b> %s</p>' % (E(a), E(b)) for a, b in p['facts'])
        shots = ''
        if p.get('photo'):
            shots = '<div class="shots"><img src="assets/img/%s" alt="A new classroom block at Joytown" loading="lazy"><img src="assets/img/%s" alt="The classroom block under construction" loading="lazy"></div><p style="font-size:.9rem;color:var(--muted)">%s</p>' % (p['photo'], p['photo2'], E(p['caption']))
        tpls += '''<template id="tpl-%s"><div class="in"><span class="tag %s">%s</span><h2 id="sheet-title" style="margin-top:12px">%s</h2><p class="meta">%s · %s · <b>%s</b></p><p class="lede" style="font-size:1.08rem">%s</p><div class="metrics">%s</div>%s<div class="two"><div><h3>How it worked</h3><ul class="pts-list">%s</ul></div><div><h3>My part</h3><ul class="plain">%s</ul>%s</div></div><div class="cta"><a class="btn accent" href="%s" target="_blank" rel="noopener">%s Ask about this</a><a class="btn" href="%s">%s Call</a><button class="btn sheet-x" type="button" style="float:none;margin:0">Close</button></div></div></template>''' % (
            p['id'], p['kind'], p['kind'], E(p['name']), E(p['place']), E(p['when']), E(p['role']), E(p['summary']), m, shots, pl, mine, facts, wa_for('Hello Kiprop, I would like to talk about %s.' % p['short']), IC['wa'], TEL, IC['phone'])
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / Work</p><span class="eyebrow">Work</span><h1>Nine pieces of work, one filter.</h1><p class="lede">Delivered programmes, written proposals and businesses. Hover a card to see its numbers; open it for the whole story.</p></div></div>
<section style="padding-top:20px" data-filter-scope><div class="wrap"><div class="chips" role="group" aria-label="Filter by field" style="margin-bottom:10px">%s</div><p style="color:var(--muted)">Showing <b data-visible-count>%d</b> of %d.</p><div class="grid" style="margin-top:12px">%s</div></div></section>
<dialog class="sheet" id="sheet" aria-labelledby="sheet-title"><button class="btn sm sheet-x x" type="button">Close</button><div class="sheet-body"></div></dialog>%s''' % (chips_fields(), len(PROJECTS), len(PROJECTS), cards, tpls)
    page('work.html', 'Work: projects, proposals and businesses', 'Delivered programmes (K4RC, Mseto, Joytown, TerraOre), proposals (JEEP, Resilient Nursery Schools, Kujenga Amani) and TerraHeal, filterable by field.', 'work', body)


# ================================================================ BUSINESS
def biz_block(key, dark):
    b = BUSINESS[key]
    stats = ''.join('<div><b>%s</b><small>%s</small></div>' % (E(a), E(c)) for a, c in b['stats'])
    steps = ''.join('<li><button type="button" role="tab" aria-selected="%s" data-copy="%s">%s</button></li>' % ('true' if i == 0 else 'false', E(t), E(n)) for i, (n, t) in enumerate(b['flow']))
    svc = ''.join('<div><b>%s</b><p>%s</p></div>' % (E(a), E(c)) for a, c in b['services'])
    built = ''.join('<li>%s</li>' % E(x) for x in b['built'])
    contact = ''
    if b['contact']:
        contact = '<div class="panel dark"><h3>Reach TerraHeal</h3><div class="cta" style="margin-top:12px">' + ''.join('<a class="btn %s" href="%s">%s</a>' % ('accent' if i == 0 else '', E(u), E(v)) for i, (n, v, u) in enumerate(b['contact'])) + '<a class="btn" style="color:var(--panel-ink);border-color:var(--panel-ink)" href="%s" target="_blank" rel="noopener">%s WhatsApp</a></div><p style="margin-top:14px;font-size:.92rem">Open daily, 8am to 1am. Kakamega, Kenya.</p></div>' % (WA_URL, IC['wa'])
    cta = contact or '<div class="panel dark"><h3>Community and compliance work</h3><p>For stakeholder engagement, relocation planning or licensing support, call or message me.</p><div class="cta"><a class="btn accent" href="%s" target="_blank" rel="noopener">%s WhatsApp</a><a class="btn" style="color:var(--panel-ink);border-color:var(--panel-ink)" href="%s">%s Call</a></div></div>' % (wa_for('Hello Kiprop, I have a question about community engagement or compliance work.'), IC['wa'], TEL, IC['phone'])
    return '''<section id="%s" class="%s"><div class="wrap"><div class="biz"><div><span class="eyebrow">%s</span><h2>%s</h2><p class="lede">%s</p><div class="stats">%s</div><h3>The flow, step by step</h3><div><ul class="steps" role="tablist">%s</ul><div class="step-copy" aria-live="polite">%s</div></div></div>
<div><div class="panel"><h3>What it does</h3><div class="svc">%s</div></div><div class="panel" style="margin-top:18px"><h3>What I built and did</h3><ul class="plain">%s</ul></div><div style="margin-top:18px">%s</div></div></div></div></section>''' % (
        key, 'soft' if dark else '', E(b['role']), E(b['name']), E(b['tagline']), stats, steps, E(b['flow'][0][1]), svc, built, cta)


def business():
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / Business</p><span class="eyebrow">Business portfolio</span><h1>TerraHeal and TerraOre.</h1><p class="lede">One is a pharmacy I run from set-up to daily trading. The other is a mining operation where I led community relations and compliance. Between them: supply chains, stakeholders and the paperwork that keeps both honest.</p>
<div class="chips"><a class="chip" href="#terraheal">TerraHeal Pharmaceuticals</a><a class="chip" href="#terraore">TerraOre Mineral Resources</a><a class="chip" href="#skills">Business skills</a></div></div></div>
%s%s
<section id="skills"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Business skills</span><h2>What both roles taught me.</h2></div></div><div class="grid">%s</div></div></section>
<section class="band"><div class="wrap"><div class="follow"><h2>Need a supplier, a partner or a fixer for the paperwork?</h2><div class="cta" style="margin:0"><a class="btn dark" href="%s" target="_blank" rel="noopener">%s WhatsApp</a><a class="btn" href="%s">%s Call %s</a></div></div></div></section>''' % (
        biz_block('terraheal', False), biz_block('terraore', True),
        ''.join('<div class="card rv" tabindex="0" style="cursor:default"><div class="body" style="padding:22px"><h3>%s</h3><p>%s</p></div></div>' % (E(a), E(c)) for a, c in [
            ('Procurement and supplier management', 'Quotations compared, licensed distributors only, batch and expiry checks on arrival.'),
            ('Inventory and records', 'Stock sheets, invoices, purchase orders, cash reconciliation and a management dashboard.'),
            ('Stakeholder and community relations', 'Mapping, meetings, grievance handling and written records at every step.'),
            ('Regulatory compliance', 'EIA licensing, Ministry of Mining registration, KRA documentation and payroll.'),
            ('Institutional supply and bids', 'Prequalification letters, quotations and screening proposals for churches, centres and health facilities.'),
            ('People and payroll', 'Hiring, staff set-up, payroll and banking authorisation for a small team.')]),
        wa_for('Hello Kiprop, I would like to talk about TerraHeal or TerraOre.'), IC['wa'], TEL, IC['phone'], PHONE_DISPLAY)
    page('business.html', 'Business portfolio: TerraHeal and TerraOre', 'TerraHeal Pharmaceuticals (Kakamega) and TerraOre Mineral Resources (Ikolomani): operations, supply, community relations and compliance, with contacts.', 'business', body)


# ================================================================ MORE
def more():
    ex = ''.join('<div class="ex rv" data-tag="%s"><button type="button" aria-expanded="false"><span><b>%s</b><small>%s</small></span></button><div class="more"><div><div class="pad"><b>Evidence</b><ul>%s</ul><p style="margin:0">%s</p></div></div></div></div>' % (
        e['tag'], E(e['name']), E(e['blurb']), ''.join('<li>%s</li>' % E(x) for x in e['proof']), ''.join('<span class="pill">%s</span>' % E(t) for t in e['tools'])) for e in EXPERTISE)
    tl = ''.join('<li data-fields="%s"><span class="when">%s</span><h3>%s</h3><p style="margin:0;color:var(--muted)">%s · %s</p><ul>%s</ul></li>' % (' '.join(r['fields']), E(r['when']), E(r['title']), E(r['org']), E(r['place']), ''.join('<li>%s</li>' % E(b) for b in r['bullets'])) for r in ROLES)
    method = ''.join('<div class="rv"><h3>%s</h3><p style="margin:0;color:var(--muted)">%s</p></div>' % (E(a), E(b)) for a, b in METHOD)
    svc = ''.join('<div><b>%s</b><p>%s</p></div>' % (E(a), E(b)) for a, b in SERVICES)
    edu = ''.join('<li><b>%s</b><br><span style="color:var(--muted)">%s · %s</span></li>' % (E(a), E(b), E(c)) for a, b, c in EDU)
    trn = ''.join('<li><b>%s</b><br><span style="color:var(--muted)">%s</span></li>' % (E(a), E(b)) for a, b in TRAINING)
    faq = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(q), E(a)) for q, a in FAQ)
    hd = ''.join('<a href="%s"%s>%s<span><b>%s</b><small>%s</small></span></a>' % (E(u), ' target="_blank" rel="noopener"' if u.startswith('http') else '', IC[HANDLE_ICON[k]], E(n), E(v)) for k, n, v, u in HANDLES)
    sch = ''.join('<button class="sw" type="button" data-scheme="%s" aria-pressed="false"><span style="height:46px">%s</span>%s</button>' % (k, ''.join('<b style="background:%s"></b>' % c for c in cols), n) for k, n, cols in SCHEME_TILES)
    toc = [('about', 'About'), ('expertise', 'Fields of expertise'), ('method', 'How I work'), ('experience', 'Experience'), ('education', 'Education'), ('help', 'How I can help'), ('beyond', 'Beyond work'), ('faq', 'Questions'), ('reach', 'Handles'), ('colours', 'Colour schemes'), ('site', 'About this site')]
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / More</p><span class="eyebrow">More</span><h1>Everything behind the dashboard.</h1><p class="lede">The long version: what I do, how I work, where I studied, what I can help with, and how to reach me.</p></div></div>
<div class="wrap more-layout"><nav class="toc" aria-label="On this page">%s</nav><div>
<section id="about"><h2>About</h2><div class="two"><div><p class="lede" style="font-size:1.1rem">I am a project and resilience practitioner based in Kakamega. Since 2016 I have worked wherever climate, livelihoods and conflict overlap: fish farms at Sagana, savings groups and special schools in the east, pastoral Samburu, and a mineral plant in Ikolomani.</p><p>My habit is to start with the people who will be affected and the records that already exist, then design the smallest plan that can actually be delivered. Most of what is on this site began that way.</p><p>Today I run operations at TerraHeal Pharmaceuticals and write proposals and articles on the side.</p></div><div><img src="assets/img/fields.jpg" alt="Project staff and smallholder farmers in a bean field" style="border-radius:22px;border:2px solid var(--ink)" loading="lazy"></div></div></section>
<section id="expertise"><h2>Fields of expertise</h2><p style="color:var(--muted)">Thirteen areas, from core programme work to the things I picked up along the way. Open any one for the evidence.</p><div class="chips" style="margin:14px 0 18px"><button class="chip" type="button" data-exp-chip="all" aria-pressed="true">All 13</button><button class="chip" type="button" data-exp-chip="core" aria-pressed="false">Core programme work</button><button class="chip" type="button" data-exp-chip="other" aria-pressed="false">Other fields</button></div><div class="exp">%s</div></section>
<section id="method"><h2>How I work</h2><div class="method">%s</div></section>
<section id="experience"><h2>Experience</h2><div class="chips" style="margin:14px 0 20px"><button class="chip" type="button" data-role-chip="all" aria-pressed="true">All roles</button>%s</div><ol class="tl">%s</ol></section>
<section id="education"><h2>Education and credentials</h2><div class="two"><div class="panel"><h3>Education</h3><ul class="plain">%s</ul></div><div class="panel"><h3>Licence and training</h3><ul class="plain">%s</ul></div></div></section>
<section id="help"><h2>How I can help</h2><div class="svc">%s</div><div class="cta"><a class="btn accent" href="%s" target="_blank" rel="noopener">%s Tell me about your project</a></div></section>
<section id="beyond"><h2>Beyond work</h2><p>Arsenal on match days, a lot of coding for fun, travel, and a soft spot for Watamu and its beaches. Imagine Dragons on most long drives.</p></section>
<section id="faq" class="acc"><h2>Questions</h2>%s</section>
<section id="reach"><h2>Handles</h2><div class="hdl">%s</div></section>
<section id="colours"><h2>Colour schemes</h2><p style="color:var(--muted)">Teal and black carry the brand. Pick the mood; the whole site changes and remembers your choice on this device.</p><div class="big-sw">%s</div></section>
<section id="site"><h2>About this site</h2><p>Plain HTML, CSS and JavaScript with no cookies and no tracking. User flows, the dashboard layout, the colour schemes, hover-card states and the Medium landing page were designed in Figma first. Pages slide into each other using the browser's view-transition support, and fall back to normal navigation elsewhere. The code lives in the Meta_001 repository on GitHub.</p><p><a href="https://www.figma.com/design/pQMq5zq0D9bbvNvQpLfiD8" target="_blank" rel="noopener">Open the Figma design</a> · <a href="https://github.com/kip-01/Meta_001" target="_blank" rel="noopener">Open the repository</a></p></section>
</div></div>''' % (
        ''.join('<a href="#%s">%s</a>' % t for t in toc), ex, method,
        ''.join('<button class="chip" type="button" data-role-chip="%s" aria-pressed="false">%s</button>' % (k, E(n)) for k, n in FIELDS), tl, edu, trn, svc, wa_for('Hello Kiprop, I would like to talk about a project.'), IC['wa'], faq, hd, sch)
    page('more.html', 'More: expertise, experience, credentials and handles', 'Fields of expertise, how I work, experience timeline, education, services, FAQ, social handles and colour schemes for Kiprop Haggai.', 'more', body)


# ================================================================ MEDIA
def media():
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / Media</p><span class="eyebrow">Media</span><h1>Films from the field.</h1><p class="lede">Two Kenya4Resilience films on the consortium work I coordinated in Samburu. Tap a thumbnail to play it here, or open it on YouTube.</p></div></div>
<section style="padding-top:10px"><div class="wrap"><div class="vgrid">%s</div></div></section>
<section class="soft"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Keep going</span><h2>Read the stories behind the films.</h2></div><a class="btn accent" href="medium.html">Medium landing page</a></div><p style="color:var(--muted);max-width:60ch">More on the programme: <a href="https://www.kenya4resilience.org" target="_blank" rel="noopener">kenya4resilience.org</a>. Videos play through youtube-nocookie.com only after you press play.</p></div></section>''' % ''.join(video_card(v) for v in VIDEOS)
    page('media.html', 'Media: YouTube films', 'Kenya4Resilience films with thumbnails: Consortium Project and Community of Practice.', 'media', body)


# ================================================================ MEDIUM
def medium():
    arts = sorted(ARTICLES, key=lambda a: a['date'], reverse=True)
    f = arts[0]
    chips = '<button class="chip" type="button" data-topic-chip="all" aria-pressed="true">All</button>' + ''.join('<button class="chip" type="button" data-topic-chip="%s" aria-pressed="false">%s</button>' % (E(t), E(t)) for t in TOPICS)
    grid = ''.join(story_card(a) for a in arts)
    A = {a['id']: a for a in ARTICLES}
    paths = ''.join('<div><h3 style="color:var(--panel-ink)">%s</h3><p>%s</p><ol>%s</ol></div>' % (E(t), E(s), ''.join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (E(A[i]['url']), E(A[i]['title'])) for i in ids)) for t, s, ids in PATHS)
    body = '''
<section class="m-hero"><div class="wrap"><div><span class="eyebrow">Stories from the field · on Medium</span><h1>Notes on resilience, peace and everyday leadership.</h1><p class="lede">Eight stories, 2019 to 2022, from dryland farms, women's groups and church halls. Short, plain and written close to the ground.</p>
<div class="author"><img src="%s" alt="" referrerpolicy="no-referrer" width="54" height="54"><div><b>%s</b><br><span style="color:var(--panel-muted)">medium.com/@kiprop</span></div></div>
<div class="cta" style="margin:0"><a class="btn accent" href="https://medium.com/@kiprop" target="_blank" rel="noopener">%s Follow on Medium</a><a class="btn" style="color:var(--panel-ink);border-color:var(--panel-ink)" href="%s" target="_blank" rel="noopener">Read the latest</a></div></div>
<a class="feat" href="%s" target="_blank" rel="noopener"><div class="ph"><img src="%s" alt="" referrerpolicy="no-referrer"></div><div class="b"><span class="eyebrow" style="margin-bottom:6px">Latest · %s</span><h3>%s</h3><p style="color:var(--muted);margin:0">%s</p></div></a></div></section>
<div class="m-stats"><div class="wrap"><div><b data-count="8">8</b><span>stories</span></div><div><b>2019 to 2022</b><span>published</span></div><div><b data-count="7">7</b><span>topics</span></div><div><b>Wamba to Embakasi</b><span>where they were set</span></div></div></div>
<section id="stories"><div class="wrap" data-topic-scope data-topic="all"><div class="sec-head"><div><span class="eyebrow">Latest stories</span><h2>Pick a topic.</h2></div><p><b data-n>%d</b> stories shown. <a href="articles.html">Prefer a list? Open the archive.</a></p></div><div class="chips" style="margin-bottom:24px" role="group" aria-label="Filter stories by topic">%s</div><div class="grid">%s</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Reading paths</span><h2>Three ways in.</h2></div></div><div class="path">%s</div></div></section>
<section><div class="wrap"><div class="follow"><h2>Follow the stories, or tell me what to write next.</h2><div class="cta" style="margin:0"><a class="btn dark" href="https://medium.com/@kiprop" target="_blank" rel="noopener">Follow on Medium</a><a class="btn" href="%s" target="_blank" rel="noopener">%s WhatsApp</a></div></div></div></section>''' % (
        MEDIUM_AVATAR, NAME, IC['medium'], E(f['url']), E(f['url']), E(f['img']), datetime.date.fromisoformat(f['date']).strftime('%d %b %Y'), E(f['title']), E(f['blurb']), len(arts), chips, grid, paths, wa_for('Hello Kiprop, I read your stories on Medium. '), IC['wa'])
    page('medium.html', 'Stories on Medium', 'Landing page for Kiprop Haggai\'s Medium stories: resilience, climate, peace, women and leadership, youth and family, with reading paths.', 'medium', body)


def articles():
    arts = sorted(ARTICLES, key=lambda a: a['date'], reverse=True)
    rows = ''.join('<a class="arow" href="%s" target="_blank" rel="noopener" data-topics="%s"><time datetime="%s">%s</time><span><b>%s</b><br><span style="color:var(--muted);font-size:.93rem">%s</span></span><span class="tag">%s</span></a>' % (
        E(a['url']), E('|'.join(a['topics'])), a['date'], datetime.date.fromisoformat(a['date']).strftime('%b %Y'), E(a['title']), E(a['blurb']), E(a['topics'][0])) for a in arts)
    chips = '<button class="chip" type="button" data-topic-chip="all" aria-pressed="true">All</button>' + ''.join('<button class="chip" type="button" data-topic-chip="%s" aria-pressed="false">%s</button>' % (E(t), E(t)) for t in TOPICS)
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / <a href="medium.html">Medium</a> / Archive</p><span class="eyebrow">Articles</span><h1>The full reading list.</h1><p class="lede">Every story on Medium, newest first. Search, or narrow by topic.</p></div></div>
<section style="padding-top:10px"><div class="wrap" data-topic-scope data-topic="all"><div style="display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-bottom:18px"><input class="search" type="search" placeholder="Search stories" aria-label="Search stories"><span><b data-n>%d</b> shown</span></div><div class="chips" style="margin-bottom:24px">%s</div><div class="alist">%s</div><p style="margin-top:28px"><a class="btn accent" href="https://medium.com/@kiprop" target="_blank" rel="noopener">%s Follow on Medium</a></p></div></section>''' % (len(arts), chips, rows, IC['medium'])
    page('articles.html', 'Medium articles archive', 'Searchable list of all Kiprop Haggai Medium articles with topics and dates.', 'medium', body)


# ================================================================ CONTACT
def contact():
    hd = ''.join('<a href="%s"%s>%s<span><b>%s</b><small>%s</small></span></a>' % (E(u), ' target="_blank" rel="noopener"' if u.startswith('http') else '', IC[HANDLE_ICON[k]], E(n), E(v)) for k, n, v, u in HANDLES)
    picks = ''.join('<button class="chip" type="button" data-topic-pick="%s" aria-pressed="false">%s</button>' % (E(t), E(t)) for t in ['a project proposal', 'resilience programme design', 'community engagement or CSR', 'environmental compliance', 'TerraHeal pharmacy supply', 'TerraOre', 'writing or an article'])
    body = '''<div class="page-head"><div class="wrap"><p class="crumbs"><a href="index.html">Dashboard</a> / Contact</p><span class="eyebrow">Contact</span><h1>Call or WhatsApp: 0716 494 214.</h1><p class="lede">The fastest way to reach me. Based in Kakamega, Kenya; working across the country.</p></div></div>
<section style="padding-top:10px"><div class="wrap"><div class="reach"><a class="big wa" href="%s" target="_blank" rel="noopener">%s<b>WhatsApp<br>0716 494 214</b><span>Opens a chat with a ready message</span></a><a class="big call" href="%s">%s<b>Call<br>0716 494 214</b><span>Tap to dial on your phone</span></a></div>
<div class="cta"><button class="btn" type="button" data-copy="0716494214">Copy the number</button><a class="btn" href="assets/kiprop-haggai.vcf" download>Save to contacts</a><a class="btn" href="mailto:%s">%s Email</a></div></div></section>
<section class="soft builder"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Message builder</span><h2>Tell me what it is about.</h2></div><p>Pick what applies. The message below is sent to my WhatsApp, and you can edit it first.</p></div><div class="chips" style="margin-bottom:14px">%s</div><textarea id="wa-text" aria-label="Your WhatsApp message"></textarea><p style="margin-top:14px"><a class="btn accent" id="wa-send" href="%s" target="_blank" rel="noopener">%s Send on WhatsApp</a></p></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Handles</span><h2>Find me elsewhere.</h2></div></div><div class="hdl">%s</div></div></section>''' % (
        wa_for('Hello Kiprop, '), IC['wa'], TEL, IC['phone'], EMAIL, IC['email'], picks, wa_for('Hello Kiprop, '), IC['wa'], hd)
    page('contact.html', 'Contact: call or WhatsApp 0716 494 214', 'Call or WhatsApp Kiprop Haggai on 0716 494 214, email, Medium, GitHub and YouTube.', 'contact', body, fab=False)
    vcf = 'BEGIN:VCARD\r\nVERSION:3.0\r\nFN:Kiprop Haggai\r\nN:Haggai;Kiprop;;;\r\nTEL;TYPE=CELL:%s\r\nEMAIL:%s\r\nURL:%s\r\nADR;TYPE=WORK:;;;Kakamega;;;Kenya\r\nTITLE:Project and resilience practitioner\r\nEND:VCARD\r\n' % (PHONE_TEL, EMAIL, SITE_URL)
    write('assets/kiprop-haggai.vcf', vcf)


def notfound():
    body = '<div class="page-head"><div class="wrap"><span class="eyebrow">404</span><h1>That page wandered off.</h1><p class="lede">Try the dashboard, or call 0716 494 214.</p><div class="cta"><a class="btn accent" href="index.html">Back to the dashboard</a><a class="btn" href="work.html">See the work</a></div></div></div>'
    page('404.html', 'Page not found', 'Page not found.', 'index', body)


if __name__ == '__main__':
    index(); work(); business(); more(); media(); medium(); articles(); contact(); notfound()
    write('.nojekyll', '')
    pages = ['index', 'work', 'business', 'more', 'media', 'medium', 'articles', 'contact']
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % ''.join('<url><loc>%s%s.html</loc></url>' % (SITE_URL, p) for p in pages))
    write('robots.txt', 'User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % SITE_URL)
    print('built', len(pages) + 1, 'pages')
