#!/usr/bin/env python3
"""Generates the static ABI hub MOCK pages. Output is plain HTML (no build step needed to view).
Edit content here and re-run:  python3 build.py"""
import os, html
OUT=os.path.dirname(os.path.abspath(__file__))
CAL="https://calendly.com/callum-ambarorlando/30min"
def P(t): return f'<span class="placeholder">[{t}]</span>'

# page registry (purpose / components / data / phase from the Build-Out Plan page specs)
PAGES=[
 ("index.html","Home",1,"Explain ABI, route visitors","Hero, proof strip, featured development, Isla prompt, area tiles","Maintained"),
 ("developments.html","Developments",1,"List every project","Project cards with stage tags, summary of live availability","Maintained, live summary for AMBAR"),
 ("development-ambar.html","AMBAR",1,"Sell one project (development template, AMBAR first)","Template sections, 3D availability, floor plans, currency toggle, disclaimers","Live and maintained"),
 ("buy.html","Buy",1,"Help buyers choose a route","Route chooser, new versus resale, Isla prompt","Maintained"),
 ("buying-from-the-uk.html","Buying from the UK",1,"Walk through the journey","Six-step journey, cost and tax explainers, currency toggle, call booking","Maintained, rates from a feed"),
 ("about.html","About & team",1,"Build credibility","History, team profiles, offices","Maintained"),
 ("contact.html","Contact & book a call",1,"Capture enquiries","Form, calendar booking, UK and US numbers","CRM"),
 ("areas.html","Areas",2,"Compare locations","Area index, area guide, drive-time map","Maintained, external"),
 ("services.html","Services",2,"Explain the partner network","Service cards, partner introductions","Maintained"),
 ("sell.html","Sell",2,"Win listings","Process steps, valuation request form","Maintained, CRM"),
 ("insights.html","Insights",2,"Publish updates and guides","Article list, guide downloads, email sign-up","Automated"),
 ("insights-article.html","Article template",2,"Article template for Insights","Source and as-of date, related items, sign-up","Automated (drafted, approved by a person)"),
 ("brokers.html","Brokers",2,"Serve brokers","Registration, project packs, availability summary","Live and maintained"),
 ("investor-hub.html","Investor hub",2,"Explain ownership economics","Cost explainers, branded versus unbranded, rental programme basics","Maintained, external"),
 ("developer-partners.html","Developer partners",2,"Attract developers","Partner list, how ABI represents projects, enquiry form","Maintained, CRM"),
 ("compare.html","Compare",3,"Shortlist options","Side-by-side table of projects, plans, areas","Maintained"),
 ("events.html","Events",3,"Run launches and webinars","Event list, registration, recordings","Maintained, CRM"),
 ("client-area.html","Client area",3,"Support buyers in progress","Saved homes, documents, journey status, messaging","Account data"),
 ("press-careers.html","Press & careers",3,"Credibility and recruiting","Coverage list, roles list","Maintained"),
 ("development-continuum-miami.html","Continuum Miami",1,"Second development on the template (coming soon, no live availability)","Template sections; Availability replaced by 'Register interest'","Maintained only"),
]
META={p[0]:p for p in PAGES}
PRIMARY=[("developments.html","Developments"),("buy.html","Buy"),("buying-from-the-uk.html","Buying from the UK"),("areas.html","Areas"),("services.html","Services"),("insights.html","Insights"),("about.html","About")]
MORE=[("sell.html","Sell",2),("investor-hub.html","Investor hub",2),("brokers.html","Brokers",2),("developer-partners.html","Developer partners",2),("compare.html","Compare",3),("events.html","Events",3),("client-area.html","Client area",3),("press-careers.html","Press & careers",3),("contact.html","Contact",1)]

ICON={
 'user':'<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
 'menu':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
 'arrow':'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}
LI={'key':'<circle cx="8" cy="14" r="4"/><path d="M11 11l9-9M17 5l3 3M15 7l2 2"/>','doc':'<path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6M9 13h8M9 17h8"/>','bank':'<path d="M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 20h18"/>','fx':'<path d="M4 8h13l-3-3M20 16H7l3 3"/>','scale':'<path d="M12 3v18M5 7h14M5 7l-3 7h6zM19 7l-3 7h6zM8 21h8"/>','home':'<path d="M3 11l9-7 9 7v10H3z"/><path d="M9 21v-6h6v6"/>','chat':'<path d="M4 5h16v11H9l-5 4z"/>','chart':'<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>','people':'<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20c1-4 4-6 7-6s6 2 7 6M15 14c3 0 5 2 6 5"/>','cal':'<rect x="3" y="5" width="18" height="16"/><path d="M3 10h18M8 3v4M16 3v4"/>'}
def line_icon(k): return f'<svg class="icon-line" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2">{LI[k]}</svg>'

def photo(cls,cap="Photography placeholder",extra="",eager=False):
    if cls.startswith("img:"):
        name=cls[4:]; amb=name.startswith("ambar-")
        if cap in ("Photography placeholder",): cap="AMBAR · rendering" if amb else ""
        load='fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return f'<div class="photo has-img{" is-render" if amb else ""}" {extra}><img src="assets/img/photos/{name}.webp" alt="" {load}>{f"<span class=cap>{cap}</span>" if cap else ""}</div>'
    lines='<svg class="lines" viewBox="0 0 400 300" preserveAspectRatio="none"><g stroke="#F2E8DC" stroke-width=".6" fill="none"><path d="M60 300V120l80-40 80 40v180M220 300V60l70-30 70 30v240"/><path d="M60 160h160M60 200h160M60 240h160M220 100h140M220 140h140M220 180h140M220 220h140M220 260h140"/></g></svg>'
    return f'<div class="photo {cls}" {extra}>{lines}<span class="cap">{cap}</span></div>'

def head(title,desc):
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{html.escape(title)} | ABI Group (mock)</title><meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="icon" href="assets/img/favicon-32.png" sizes="32x32"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css"></head>'''

def is_active(h,fn): return h==fn or (h=="developments.html" and fn.startswith("development")) or (h=="insights.html" and fn.startswith("insights"))
def header(fn):
    nav=''.join(f'<a href="{h}"{" class=active" if is_active(h,fn) else ""}>{l}</a>' for h,l in PRIMARY)
    more=''.join(f'<a href="{h}"><span>{l}</span></a>' for h,l,ph in MORE)
    drawer=''.join(f'<a href="{h}">{l}{ICON["arrow"]}</a>' for h,l in [("index.html","Home")]+PRIMARY)+'<span class="label">More</span>'+''.join(f'<a href="{h}">{l}{ICON["arrow"]}</a>' for h,l,ph in MORE)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="mockbar"><b>Mock site</b> &middot; working draft for review &middot; items in [brackets] need confirming &middot; nothing here is live</div>
<header class="header"><div class="wrap">
<a class="brand" href="index.html" aria-label="ABI Group home"><img src="assets/img/logo-navy.svg" alt=""><span>ABI&nbsp;GROUP</span></a>
<nav class="nav" aria-label="Primary">{nav}<div class="more"><button aria-haspopup="true">More ▾</button><div class="menu">{more}</div></div></nav>
<div class="tools"><div class="ccy" role="group" aria-label="Currency"><button data-c="USD" aria-pressed="true">USD</button><button data-c="GBP">GBP</button><button data-c="CAD">CAD</button></div>
<button class="iconbtn" data-open-account aria-label="Buyer account">{ICON["user"]}</button>
<a class="btn small" href="contact.html">Book a call</a>
<button class="iconbtn burger" aria-label="Menu" aria-expanded="false">{ICON["menu"]}</button></div>
</div></header><nav class="drawer" aria-label="Mobile">{drawer}<div style="margin-top:24px"><a class="btn" href="contact.html" style="justify-content:center;color:var(--stone)">Book a call</a></div></nav>'''

def footer(fn):
    m=META[fn]
    cols=[("Developments",[("developments.html","All developments"),("development-ambar.html","AMBAR"),("development-continuum-miami.html","Continuum Miami"),("compare.html","Compare")]),
          ("Buying",[("buy.html","Buy"),("buying-from-the-uk.html","Buying from the UK"),("areas.html","Areas"),("services.html","Services"),("investor-hub.html","Investor hub"),("sell.html","Sell")]),
          ("Partners",[("brokers.html","Brokers"),("developer-partners.html","Developer partners"),("events.html","Events"),("insights.html","Insights")]),
          ("ABI Group",[("about.html","About & team"),("press-careers.html","Press & careers"),("client-area.html","Client area"),("contact.html","Contact & book a call")])]
    c=''.join(f'<div><h4>{t}</h4><ul>'+''.join(f'<li><a href="{h}">{html.escape(l)}</a></li>' for h,l in ls)+'</ul></div>' for t,ls in cols)
    return f'''<footer class="footer"><div class="wrap"><div class="top"><div><div class="mark"><img src="assets/img/logo-reversed.svg" alt="ABI Group"><span>ABI&nbsp;GROUP</span></div>
<p style="max-width:32ch">Florida property for UK and international buyers. {P("Short company line — to confirm")}</p>
<p style="font-size:14px">UK {P("UK number")}<br>US {P("US number")}<br>{P("Office addresses")}</p></div>{c}</div>
<div class="base"><span>&copy; ABI Group {P("legal entity & licence statement")}</span><span>Mock for internal review &middot; not indexed &middot; Phase {m[2]} page &middot; Images: placeholder</span></div></div></footer>'''

def shared(fn):
    m=META[fn]
    return f'''
<button class="isla-launch" aria-label="Ask Isla"><span class="isla-av"><img src="assets/img/logo-reversed.svg" alt=""></span><span class="t">Ask Isla</span></button>
<aside class="isla" aria-label="Isla, ABI's AI concierge"><header><span class="isla-av"><img src="assets/img/logo-reversed.svg" alt=""></span><div><b>ISLA</b><small>ABI&rsquo;s AI concierge &middot; scripted preview</small></div><button class="x" aria-label="Close">×</button></header>
<div class="ctx">Page context remembered: {html.escape(m[1])}</div><div class="log"></div><div class="quick"></div>
<form class="composer"><button type="button" class="mic" aria-label="Voice (Phase 2)">🎙</button><input placeholder="Ask about buying, areas, AMBAR…" aria-label="Message Isla"><button aria-label="Send">→</button></form></aside>
<div class="modal" id="account" role="dialog" aria-label="Buyer account"><div class="box"><button class="x" aria-label="Close">×</button>
<span class="eyebrow">Buyer account</span><h2 style="font-size:22px">Save residences, compare, message an advisor</h2>
<div><div class="tabs"><button data-t="in" aria-selected="true">Sign in</button><button data-t="up" aria-selected="false">Create account</button></div>
<form class="form" data-mock data-source="buyer account" data-tab="in"><label>Email<input type="email" placeholder="you@example.com"></label><label>Password<input type="password" placeholder="••••••••"></label><button class="btn">Sign in</button><a class="textlink" href="client-area.html" style="justify-self:start">Preview the client area →</a></form>
<form class="form" data-mock data-source="buyer account" data-tab="up" hidden><label>Full name<input></label><label>Email<input type="email"></label><label>Country<select><option>United Kingdom</option><option>Canada</option><option>United States</option><option>Other</option></select></label><button class="btn">Create account</button></form></div>
<p class="rate-note" style="margin-top:16px">Mock only. No account is created and nothing is stored.</p></div></div>
<button class="phase-badge" aria-label="Show mock notes">Phase <b>{m[2]}</b> &middot; notes</button>
<div class="mocknotes" role="note"><h4>Mock notes &middot; {html.escape(m[1])}</h4><dl><dt>Phase</dt><dd>Phase {m[2]}{" (core)" if m[2]==1 else " (engine)" if m[2]==2 else " (extras)"}</dd><dt>Purpose</dt><dd>{html.escape(m[3])}</dd><dt>Key components</dt><dd>{html.escape(m[4])}</dd><dt>Data</dt><dd>{html.escape(m[5])}</dd></dl>
<p style="margin-top:10px">From the ABI Hub Build-Out Plan page specs. Gold-outlined brackets mark content to confirm. Shortcut: Alt+N.</p></div>
<script src="assets/js/site.js" defer></script>'''

def page(fn,body,desc="",context=None):
    m=META[fn]
    bodycls=' class="theme-ambar"' if fn=="development-ambar.html" else ''
    doc=head(m[1],desc or m[3])+f'<body data-context="{html.escape(context or m[1])}"{bodycls}>'+header(fn)+f'<main id="main">{body}</main>'+footer(fn)+shared(fn)+'</body></html>'
    open(os.path.join(OUT,fn),'w').write(doc)

# ---------------- components
def hero(eyebrow,h1,lede,cls="ph-dusk",btns="",short=False,crumbs="",home=False):
    return f'''<section class="hero{" short" if short else ""}{" hero-home" if home else ""}">{photo(cls,eager=True)}<div class="wrap">{crumbs}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{lede}</p>{f'<div class="btn-row hero-cta">{btns}</div>' if btns else ""}</div></section>'''
def crumbs(*items): return '<div class="breadcrumbs">'+' / '.join(f'<a href="{h}">{l}</a>' if h else l for h,l in items)+'</div>'
def proof(items,note=""):
    s=''.join(f'<div class="item"><div class="fig">{f}</div><div class="lbl">{l}</div><div class="src">{src}</div></div>' for f,l,src in items)
    n=f'<div class="wrap" style="padding-bottom:18px"><p class="proof-note" style="color:#9da6b8;margin:0;font-family:Inter,sans-serif;font-size:12px">{note}</p></div>' if note else ""
    return f'<section class="proof" aria-label="Proof strip"><div class="wrap" style="--cols:{len(items)}">{s}</div>{n}</section>'
def card(href,name,tag,tagcls,desc,price_html,cls="ph-facade"):
    return f'''<a class="card" href="{href}"><div style="position:relative">{photo(cls)}<span class="tag {tagcls}">{tag}</span></div><div class="body"><h3>{name}</h3><p>{desc}</p><div class="meta"><span class="label">Price from</span><span class="num">{price_html}</span></div></div></a>'''
def CARD_AMBAR(): return card_ambar("development-ambar.html","AMBAR","Selling","","Orlando. Building 1: 132 residences, 9 floor plans from studio to three bedrooms.",P("to confirm"),"img:ambar-pool-aerial")
def card_ambar(*a):
    return card(*a).replace('<a class="card"','<a class="card card-ambar"',1)
def CARD_TWO(): return card("development-continuum-miami.html","Continuum Miami","Coming soon","soon","North Bay Village, Miami. Details to follow; register interest to hear first.",P("to confirm"),"img:miami-dusk")
def isla_prompt(t="Not sure where to start? Ask Isla."):
    return f'<div class="isla-prompt"><span class="isla-av" style="width:52px;height:52px"><img src="assets/img/logo-navy.svg" alt="" style="width:52px;height:52px"></span><div style="flex:1"><h3 style="margin:0 0 4px">{t}</h3><p style="margin:0;font-size:16px">Isla is ABI&rsquo;s AI concierge. She answers from the same knowledge as this site on every page and every development, recommends a development, area or guide, and hands you to a named ABI advisor.</p></div><a href="#" class="btn" data-open-isla>Ask Isla</a></div>'
JOURNEY_STEPS=[
 ("Introductory call","A conversation with an ABI advisor about your goals, budget, currency and timeline. Book at a UK-friendly time."),
 ("Choose a residence","Shortlist homes, compare floor plans and availability, and save favourites to your buyer account."),
 ("Reserve and contract","Reservation, purchase agreement and deposit schedule, explained before you sign."),
 ("Finance, currency and legal","Introductions to finance, FX, legal and tax partners, including FIRPTA and ITIN topics for non-US buyers."),
 ("Build and updates","Progress updates and documents in your client area while the residence is completed."),
 ("Completion and handover","Closing, keys and introductions for management and ongoing support."),
]
def journey():
    s=''.join(f'<details{" open" if i==0 else ""}><summary><span class="n">0{i+1}</span><h3>{t}</h3><span class="pm">+</span></summary><div class="inner"><p>{d}</p><p class="rate-note">Draft step wording. Replace with AMBAR&rsquo;s six-step journey copy plus UK-specific detail.</p></div></details>' for i,(t,d) in enumerate(JOURNEY_STEPS))
    return f'<div class="journey">{s}</div>'
def disclaimer(project="this development"):
    return f'''<div class="disclaimer" role="note"><h4>Important information</h4><ul>
<li><b>Brand licence:</b> {P("Brand licence statement for "+project+" — to be supplied and approved")}</li>
<li><b>Occupancy:</b> {P("Occupancy limits / permitted use statement — to be supplied")}</li>
<li><b>Returns:</b> Nothing on this page is an offer or a promise of rental income, returns or capital growth. {P("Approved return disclaimer wording")}</li>
<li><b>Pricing &amp; availability:</b> Prices, plans and availability can change without notice. Currency conversions are indicative only; contracts are in USD.</li>
<li><b>Licence:</b> {P("Brokerage licence statement")}</li></ul>
<p style="margin:12px 0 0;font-size:12px">The disclaimer block is part of the template and required on publish. Wording needs compliance sign-off.</p></div>'''
def enquiry_form(source="site form",title="Make an enquiry"):
    return f'''<form class="form" data-mock data-source="{source}"><h3>{title}</h3><div class="row"><label>First name<input></label><label>Last name<input></label></div>
<div class="row"><label>Email<input type="email"></label><label>Phone<input type="tel" placeholder="+44"></label></div>
<div class="row"><label>I&rsquo;m interested in<select><option>AMBAR</option><option>Buying a resale home</option><option>Selling</option><option>Services</option><option>Something else</option></select></label><label>Preferred currency<select><option>GBP</option><option>USD</option><option>CAD</option></select></label></div>
<label>Message<textarea rows="4"></textarea></label><label class="check"><input type="checkbox"> Keep me updated with market updates and guides</label>
<div class="captured"></div><div class="btn-row"><button class="btn">Send enquiry</button><a class="textlink" href="{CAL}" target="_blank" rel="noopener">Or book a 30-minute call</a></div></form>'''
def ccy_note(): return '<p class="rate-note ccy-note"></p>'
def sidenav(secs): return '<nav class="sidenav" aria-label="On this page"><span class="label">On this page</span>'+''.join(f'<a href="#{i}">{t}</a>' for i,t in secs)+'</nav>'
def booking_mock():
    days=["Mon","Tue","Wed","Thu","Fri"]
    slots=''.join(f'<button class="chip" type="button">{t}</button>' for t in ["10:00","11:30","14:00","15:30","17:00"])
    dd=''.join(f'<button class="chip" type="button"{" aria-pressed=true" if i==1 else ""}>{d}</button>' for i,d in enumerate(days))
    return f'''<span class="label">Calendar booking (mock)</span><h3 style="margin:10px 0 14px">Choose a time &middot; UK time</h3><div class="chips" data-chipgroup style="margin-bottom:12px">{dd}</div><div class="chips" data-chipgroup>{slots}</div><p class="rate-note" style="margin-top:12px">Illustrative slots. The build reads advisors&rsquo; live calendars; for now the button opens <a href="{CAL}" target="_blank" rel="noopener">Calendly</a>.</p>'''
def floorplans(live):
    types=[("Studio",0),("Studio",0),("One bedroom",1),("One bedroom",1),("One bedroom",1),("Two bedroom",2),("Two bedroom",2),("Two bedroom",2),("Three bedroom",3)]
    if not live: types=types[:3]
    btn=''.join(f'<button data-beds="{b}" data-name="Plan {chr(65+i)} · {t}" data-meta="{t} · {html.escape(P("sq ft"))} · from {html.escape(P("price — to confirm"))}"><span><b>Plan {chr(65+i)}</b>{t}</span><span>{P("sq ft")}</span></button>' for i,(t,b) in enumerate(types))
    return f'<div class="fp"><div class="list" role="listbox">{btn}</div><div class="view"><div class="plan"></div><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px"><div><h3 class="pname" style="margin:0"></h3><p class="pmeta" style="margin:4px 0 0;font-size:15px"></p></div><div class="btn-row"><a class="btn small" href="#" data-save>Save plan</a><a class="textlink" href="#residences">Download PDF</a></div></div></div></div><p class="rate-note" style="margin-top:8px">Plan letters, plan mix, sizes and drawings are schematic placeholders. Real plans come from ABI marketing.</p>'

AMBAR_GALLERY='<div class="gallery">'+''.join(f'<figure>{photo("img:"+f,c,'style="aspect-ratio:4/3"')}</figure>' for f,c in [("ambar-lobby","Lobby · rendering"),("ambar-cafe-outdoor","Café terrace · rendering"),("ambar-event-lawn","Event lawn · rendering"),("ambar-a1-bedroom","Bedroom · rendering")])+'</div>'
RENDERS='<div class="gallery renders">'+''.join(f'<figure>{photo("img:ambar-plan-"+f,"",'style="aspect-ratio:5/4"')}<figcaption>{c}</figcaption></figure>' for f,c in [("s1","Studio"),("a1","One bedroom"),("b1","Two bedroom"),("c1","Three bedroom")])+'</div><p class="rate-note">3D residence renderings from AMBAR marketing; matching each rendering to a plan letter is to confirm.</p>'
# ================= PAGES
PIONEER=[
 ("Isla, ABI’s AI concierge","One concierge across every page and development. She answers from the same knowledge as the site, qualifies gently, recommends a development, area or guide, and hands over to a named advisor with the conversation summarised.","#",'data-open-isla',"Ask Isla"),
 ("Live 3D availability","Where ABI controls inventory, buyers orbit the building, filter by level and see each residence’s status and price, starting with AMBAR Building 1.","development-ambar.html#availability","","See AMBAR availability"),
 ("A UK-to-Florida buying platform","A six-step journey with GBP and CAD pricing, plain-English guidance on FIRPTA, ITIN and currency, UK-hours call booking and a buyer account to follow progress.","buying-from-the-uk.html","","The UK buyer journey"),
 ("An insights engine","Market updates, guides and explainers drafted from defined sources, each carrying its source and as-of date, and approved by a person before it publishes.","insights.html","","Read insights"),
]
def pioneering(compact=False,dark=True):
    rows=''.join(f'<li class="pi reveal"><span class="pi-n">0{k+1}</span><div class="pi-b"><h3>{t}</h3><p>{d}</p><a class="textlink" href="{h}" {attr}>{lab}</a></div></li>' for k,(t,d,h,attr,lab) in enumerate(PIONEER))
    intro='<p class="lede">ABI is building the tools that make buying property from overseas clearer: one source of truth, shown the same way whether you browse the site or ask Isla.</p>'
    if compact:
        return f'<section id="pioneering"><span class="eyebrow">Pioneering</span><h2>New standards, built in-house</h2>{intro}<ol class="pioneer">{rows}</ol></section>'
    return f'<section class="section {"dark" if dark else ""} pioneer-sec"><div class="wrap"><div class="split" style="align-items:end"><div><span class="eyebrow">Pioneering</span><h2>Setting new standards for buying property</h2></div>{intro}</div><ol class="pioneer">{rows}</ol></div></section>'

def home():
    b=hero("ABI Group &middot; United States &amp; United Kingdom","Over $6.5 billion sold. Thirty years of experience, now guiding Florida.","Thirty years of sales history in the US and UK, brought to Florida property for UK and international buyers: considered developments, a trusted partner network, and Isla, our AI concierge.",
      "img:home-hero",f'<a class="btn light" href="developments.html">Explore developments</a><a class="textlink light" href="{CAL}" target="_blank" rel="noopener">Speak to an advisor</a>',home=True)
    b+=proof([("30+","Years of sales history in the US &amp; UK","Source: ABI"),("$6.5+ Billion","Sold","Source: ABI"),("35","Residences available now at AMBAR Building 1","Sample. Live summary from ABI’s sales system")])
    routes=''.join(f'<li class="reveal"><a href="{h}"><span class="r-t">{t}</span><span class="r-d">{d}</span><span class="r-a">&rarr;</span></a></li>' for h,t,d in [("buy.html","Buy","New development, resale, and what’s right for you."),("buying-from-the-uk.html","Buying from the UK","Six steps, costs, FIRPTA, ITIN, currency and timelines."),("sell.html","Sell","How ABI markets and sells a property."),("services.html","Services","Finance, FX, legal, tax and property management partners.")])
    b+=f'''<section class="section intro"><div class="wrap split" style="align-items:start"><div class="reveal"><span class="eyebrow">The ABI hub</span><h2>One source of truth for Florida property</h2><p class="lede">The company, the team, the markets, the buying journey and the services, held in one place. Developments sit around the hub, each on a shared template.</p><a class="textlink" href="about.html">About ABI</a></div><ul class="routes">{routes}</ul></div></section>'''
    b+=f'''<section class="section alt feature"><div class="wrap"><div class="feature-grid reveal"><a class="feature-img card-ambar" href="development-ambar.html">{photo("img:ambar-beach-entry","AMBAR · rendering",'style="aspect-ratio:5/4"')}<span class="tag">Selling</span></a>
<div class="feature-txt"><span class="eyebrow">Featured development</span><h2>AMBAR, Orlando</h2><p class="lede">The first development on ABI’s template. Building 1 holds 132 residences across nine floor plans, from studio to three bedrooms.</p>
<dl class="facts"><div><dt>Residences</dt><dd>132</dd></div><div><dt>Available now</dt><dd>35 <small>sample</small></dd></div><div><dt>Floor plans</dt><dd>9</dd></div></dl>
<div class="btn-row"><a class="btn" href="development-ambar.html">Discover AMBAR</a><a class="textlink" href="development-ambar.html#availability">Live availability</a></div></div></div>
<div class="also reveal"><span class="label">Also on the template</span><a href="development-continuum-miami.html"><span class="r-t">Continuum Miami</span><span class="r-d">North Bay Village, Miami &middot; Coming soon</span><span class="r-a">&rarr;</span></a><a href="developments.html"><span class="r-t">All developments</span><span class="r-d">Selling, coming soon and sold out</span><span class="r-a">&rarr;</span></a></div></div></section>'''
    b+=pioneering()
    st=''.join(f'<li class="reveal"><span class="pi-n">0{k+1}</span><h3>{t}</h3></li>' for k,(t,d) in enumerate(JOURNEY_STEPS))
    b+=f'''<section class="section"><div class="wrap split" style="align-items:start"><div class="reveal"><span class="eyebrow">UK buyers, first-class</span><h2>From the UK to a Florida home, in six steps</h2><p class="lede">GBP pricing, UK-specific guidance and UK-hours call booking, throughout.</p><div class="btn-row"><a class="btn" href="buying-from-the-uk.html">Read the journey</a><a class="textlink" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div></div><ol class="steps-list">{st}</ol></div></section>'''
    areas=[("Orlando","img:orlando"),("Kissimmee","img:kissimmee"),("ChampionsGate","img:championsgate"),("Davenport","img:davenport")]
    at=''.join(f'<a class="tile reveal" href="areas.html#{n.lower()}">{photo(c,"")}<div class="t"><h3>{n}</h3><span>Area guide &rarr;</span></div></a>' for n,c in areas)
    b+=f'''<section class="section alt"><div class="wrap"><div class="split" style="align-items:end;margin-bottom:56px"><div><span class="eyebrow">Areas</span><h2>Where to buy around Orlando</h2></div><p class="lede" style="margin:0">Demand, rental context, and drive times to the parks and the airport, town by town.</p></div>
<div class="grid g4">{at}</div><p class="rate-note" style="margin-top:18px">Placeholder area set for the mock; the final list comes from the current abire.co.uk location pages.</p></div></section>'''
    li=''.join(f'<li><a href="insights-article.html">{t}</a></li>' for t in ["Branded residences explained","Orlando market update "+P("month"),"FIRPTA and ITIN, in plain English"])
    b+=f'''<section class="section"><div class="wrap split" style="align-items:start"><div class="reveal"><span class="eyebrow">Buyer stories</span><p class="quote">&ldquo;{P("Named buyer story, with permission")}&rdquo;</p><p class="rate-note">{P("Buyer name, location")}</p></div><div class="reveal"><span class="eyebrow">Latest insights</span><ul class="routes plain">{li}</ul><a class="textlink" href="insights.html">All insights</a></div></div></section>'''
    page("index.html",b,"ABI Group: over $6.5 billion sold across thirty years in the US and UK. Florida property for UK and international buyers.")

def developments():
    b=hero("Developments","Every project, one template","AMBAR is the first. New developments are added as new entries on the template, not new builds.","img:ambar-aerial",short=True,crumbs=crumbs(("index.html","Home"),(None,"Developments")))
    b+=f'''<section class="section"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;margin-bottom:30px"><div class="chips" data-chipgroup><button class="chip" aria-pressed="true">All</button><button class="chip">Selling</button><button class="chip">Coming soon</button><button class="chip">Sold out</button></div><a class="textlink" href="compare.html">Compare developments</a></div>
<div class="grid g3">{CARD_AMBAR()}{CARD_TWO()}{card("developments.html","[Past project]","Sold out","sold","Shows the sold-out stage tag. Replace with a real past project, or remove.",P("—"),"img:palms-lake")}</div><p class="rate-note" style="margin-top:14px">Filters are visual only in the mock. Stage tags: Selling, Coming soon, Sold out.</p></div></section>'''
    b+=f'''<section class="section alt"><div class="wrap split"><div><span class="eyebrow">Live availability summary</span><h2>AMBAR Building 1</h2><p>ABI sells AMBAR, so it can show live Building 1 availability. Other projects show static information until ABI has the same control.</p></div>
<div class="grid g3"><div class="kpi"><div class="v">132</div><div class="k">Residences</div></div><div class="kpi"><div class="v">35</div><div class="k">Available (sample)</div></div><div class="kpi"><div class="v" style="font-size:20px">{P("live figure")}</div><div class="k">Lowest available</div></div></div></div></section>'''
    b+=f'<section class="section"><div class="wrap">{isla_prompt("Which development fits you? Ask Isla.")}</div></section>'
    page("developments.html",b)

def dev_template(fn,name,A):
    """Development template; sections follow the Content & Sections draft template table."""
    secs=[("overview","Overview"),("opportunity","Opportunity"),("market","Market evidence"),("investment","Investment case"),("development","The development"),("residences","Residences"),("availability","Availability" if A else "Register interest"),("journey","Purchase journey"),("support","ABI support"),("disclaimers","Disclaimers"),("next","Next step")]
    facts=[("132" if A else P("TBC"),"Residences (Building 1)" if A else "Residences"),(P("towers"),"Towers"),(P("acres"),"Acreage"),(P("date"),"Delivery"),(P("to confirm"),"Price from"),(P("brand"),"Brand")]
    kp=''.join(f'<div class="kpi"><div class="v">{v}</div><div class="k">{k}</div></div>' for v,k in facts)
    ok=''.join(f'<div class="kpi"><div class="v" style="font-size:22px">{P("figure")}</div><div class="k">{k}</div></div>' for k in (["Annual visitors","Occupancy","Home price growth","Source / as of"] if A else ["Location fact","Location fact"]))
    sup=''.join(f'<div class="panel">{line_icon(i)}<h3>{t}</h3><p style="font-size:16px;margin:0">{d}</p></div>' for i,t,d in [("people","Advisor","A named ABI advisor from first call to handover."),("bank","Finance","Introductions to lenders who work with overseas buyers."),("scale","Legal","Contract and closing support from partner attorneys."),("doc","Tax","FIRPTA, ITIN and cross-border tax introductions."),("fx","Currency","FX partners for GBP and CAD transfers."),("key","Handover","Keys, furnishing and management introductions.")])
    origin="UK, Brazil, Colombia + "+P("two more") if A else P("per market")
    c=f'''<section id="overview"><span class="eyebrow">Overview</span><h2>Headline facts</h2><div class="grid g3" style="margin-top:20px">{kp}</div></section>
<section id="opportunity"><span class="eyebrow">Opportunity</span><h2>Why this location</h2><div class="split" style="align-items:start"><p>{"Orlando’s visitors, occupancy and home price growth make the case for the location." if A else "Location facts for this market."} {P("Figures with source and as-of date. Confirm before they go on the hub")}</p><div class="grid g2">{ok}</div></div></section>
<section id="market"><span class="eyebrow">Market evidence</span><h2>Demand and source markets</h2><div class="tablewrap"><table class="t"><thead><tr><th>Measure</th><th>Figure</th><th>Source</th><th>As of</th></tr></thead><tbody>
<tr><td>Visitors</td><td>{P("figure")}</td><td>{P("source")}</td><td>{P("2025/26")}</td></tr><tr><td>Hotel inventory</td><td>{P("figure")}</td><td>{P("source")}</td><td>{P("date")}</td></tr>
<tr><td>Top five origin markets</td><td>{origin}</td><td>{P("source")}</td><td>{P("date")}</td></tr></tbody></table></div></section>
<section id="investment"><span class="eyebrow">Investment case</span><h2>The local economy behind the asset</h2><div class="grid g2"><div class="panel linen"><h3>Regional economy</h3><p>{P("Regional economy summary, sourced")}</p></div><div class="panel linen"><h3>Growth ranking</h3><p>{P("Growth ranking, sourced and dated")}</p></div></div><p class="rate-note" style="margin-top:12px">No rental-return or yield figures appear anywhere. Return wording needs sign-off.</p></section>
<section id="development"><span class="eyebrow">The development</span><h2>Design, amenities, imagery</h2><div class="grid g2" style="margin-bottom:24px">{photo("img:ambar-pool" if A else "img:continuum-marina","Pool &amp; cabanas · rendering" if A else "Area imagery · Biscayne Bay, not the development",'style="aspect-ratio:4/3"')}{photo("img:ambar-c1-living" if A else "img:miami-bridge","Residence interior · rendering" if A else "Area imagery · Miami, not the development",'style="aspect-ratio:4/3"')}</div>{AMBAR_GALLERY if A else ""}
<div class="grid g3"><div><h4>Architecture</h4><p>{"OTJ Architects" if A else P("Architect")}</p></div><div><h4>Interiors / design</h4><p>{"Sixteenfifty" if A else P("Designer")}</p></div><div><h4>Amenities</h4><p>{"Pool and cabanas, "+P("full list") if A else P("Amenities")}</p></div></div>{'<p class="rate-note">Design-team roles to confirm.</p>' if A else ''}</section>
<section id="residences"><span class="eyebrow">Residences</span><h2>Floor plans</h2><p>{"Nine floor plans, studio to three bedrooms." if A else "Floor plans with ‘from’ prices."} Select a plan to view it.</p>{floorplans(A)}{RENDERS if A else ""}</section>'''
    if A:
        c+=f'''<section id="availability"><span class="eyebrow">Availability</span><h2>Building 1 &middot; live availability</h2><p>Orbit and zoom the building, filter by level, and select a residence for its details. <b>The mock uses generated sample data.</b> The build connects ABI’s sales system (132 residences, 35 available at the time of review).</p>
<div class="av"><div class="levels"></div><div class="stage"><span class="sample">SAMPLE DATA</span><div class="legend"><span><i class="lg-a"></i>Available</span><span><i class="lg-r"></i>Reserved</span><span><i class="lg-s"></i>Sold</span></div><div class="scene"></div><div class="ctrl"><button data-a="l" aria-label="Orbit left">⟲</button><button data-a="r" aria-label="Orbit right">⟳</button><button data-a="in" aria-label="Zoom in">+</button><button data-a="out" aria-label="Zoom out">−</button><button data-a="reset" aria-label="Reset">◎</button></div></div>
<div class="unitpanel"><span class="label" style="color:#C4A35A">Residence details</span><h3 style="margin-top:10px">Select a residence</h3><p style="font-size:15px;color:#a9b0c0">Gold squares are available. Use the level list to isolate a floor.</p></div></div>{ccy_note()}</section>'''
    else:
        c+=f'''<section id="availability"><span class="eyebrow">Register interest</span><h2>Availability not yet published</h2><p>This project shows static information until ABI controls its availability. Register to hear first.</p><div class="panel cool">{enquiry_form("register interest: "+name,"Register interest")}</div></section>'''
    c+=f'''<section id="journey"><span class="eyebrow">Purchase journey</span><h2>From enquiry to ownership</h2><p class="rate-note">Written once in the hub and pulled into every project page.</p>{journey()}</section>
<section id="support"><span class="eyebrow">ABI support</span><h2>A partner, not just a broker</h2><div class="grid g3">{sup}</div><p class="rate-note" style="margin-top:10px">Shared sitewide section. Partner names {P("to confirm")}.</p></section>
<section id="disclaimers"><span class="eyebrow">Disclaimers</span>{disclaimer(name)}</section>
<section id="next"><span class="eyebrow">Next step</span><h2>Take the next step</h2><div class="grid g3"><div class="panel">{line_icon("home")}<h3>Buyer account</h3><p style="font-size:16px">Save residences and compare.</p><a href="#" class="textlink" data-open-account>Create account</a></div><div class="panel">{line_icon("cal")}<h3>Speak to an advisor</h3><p style="font-size:16px">30 minutes, UK-friendly times.</p><a class="textlink" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div><div class="panel cool">{line_icon("chat")}<h3>Ask Isla</h3><p style="font-size:16px">ABI&rsquo;s AI concierge can answer questions about {name}, any time.</p><a href="#" class="textlink" data-open-isla>Open Isla</a></div></div></section>'''
    lede=("Building 1: 132 residences, nine floor plans from studio to three bedrooms. "+P("One-line positioning — to confirm")) if A else "North Bay Village, Miami. Coming soon. "+P("Project details — to confirm")+" Register interest to hear first."
    btns='<a class="btn light" href="#availability">'+("View availability" if A else "Register interest")+'</a><a class="btn ghost" href="'+CAL+'" target="_blank" rel="noopener">Book a call</a>'
    b=hero("Development &middot; "+("Selling" if A else "Coming soon"),name,lede,"img:ambar-main-entry" if A else "img:continuum-bay",btns,crumbs=crumbs(("index.html","Home"),("developments.html","Developments"),(None,name)))
    if A: b+=proof([("132","Residences, Building 1","Source: ABI"),("35","Available now (sample)","Live feed in the build, sample in the mock"),("9","Floor plans","Source: ABI"),("Studio–3","Bedrooms","Source: ABI")])
    b+=f'<div class="with-side">{sidenav(secs)}<div class="content">{c}</div></div>'
    page(fn,b,context=name)

def buy():
    b=hero("Buy","How ABI helps you buy","New development, resale, and what’s right for you.","img:interior-dusk",short=True,crumbs=crumbs(("index.html","Home"),(None,"Buy")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Route chooser</span><h2>Where would you like to start?</h2><div class="chips" data-chipgroup="route" style="margin:24px 0 30px"><button class="chip" data-v="new" aria-pressed="true">New development</button><button class="chip" data-v="resale">Resale home</button><button class="chip" data-v="unsure">Not sure yet</button></div>
<div data-route="new" class="split"><div><h3>Buying new</h3><p>New residences on ABI’s development template, starting with AMBAR: floor plans, live availability and a six-step purchase journey.</p><a class="btn" href="developments.html">See developments</a></div>{photo("img:ambar-pool-aerial","AMBAR · rendering",'style="aspect-ratio:16/10"')}</div>
<div data-route="resale" class="split" hidden><div><h3>Buying resale</h3><p>Existing homes across Orlando and the surrounding towns, with area guides and a named advisor. {P("Decision: do resale listings stay on the hub?")}</p><a class="btn" href="areas.html">Explore areas</a></div>{photo("img:resale","",'style="aspect-ratio:16/10"')}</div>
<div data-route="unsure" class="split" hidden><div><h3>Not sure yet</h3><p>Tell Isla your budget, purpose and timeline and she’ll suggest a route, or book a call.</p><a class="btn" href="#" data-open-isla>Ask Isla</a></div>{photo("img:palms-lake","",'style="aspect-ratio:16/10"')}</div></div></section>
<section class="section alt"><div class="wrap"><span class="eyebrow">New versus resale</span><h2>Compare the two routes</h2><div class="tablewrap"><table class="t"><thead><tr><th></th><th>New development</th><th>Resale</th></tr></thead><tbody>
<tr><td>Timeline</td><td>{P("Build schedule")}</td><td>{P("Typical closing time")}</td></tr><tr><td>Deposits</td><td>Staged, per the purchase agreement</td><td>{P("to confirm")}</td></tr><tr><td>Choice</td><td>Floor plans and levels</td><td>What’s on the market</td></tr><tr><td>Management</td><td>{P("Programme details")}</td><td>Partner introductions</td></tr><tr><td>Live availability</td><td>AMBAR Building 1</td><td>{P("If listings stay on the hub")}</td></tr></tbody></table></div></div></section>
<section class="section"><div class="wrap">{isla_prompt()}</div></section>'''
    page("buy.html",b)

def uk():
    secs=[("journey","Six-step journey"),("costs","Costs"),("tax","Tax topics"),("currency","Currency"),("timelines","Timelines"),("guide","UK buyer’s guide"),("book","Book a call")]
    chips=''.join(f'<button class="chip" type="button" onclick="document.querySelector(\'.ccy [data-c={c}]\').click()">{c}</button>' for c in ["USD","GBP","CAD"])
    tx=''.join(f'<div class="panel cool"><h3>{t}</h3><p style="font-size:16px">{d}</p></div>' for t,d in [("FIRPTA","What the Foreign Investment in Real Property Tax Act means when a non-US owner sells. "+P("Partner-reviewed explainer")),("ITIN","Why non-US buyers may need an Individual Taxpayer Identification Number. "+P("Partner-reviewed explainer")),("UK tax",P("UK-side considerations. Partner or legal review before publishing")),("Ownership structure",P("Personal vs company ownership. Partner review"))])
    c=f'''<section id="journey"><span class="eyebrow">The journey</span><h2>Six steps from the UK to Florida</h2><p>Click a step to expand it.</p>{journey()}</section>
<section id="costs"><span class="eyebrow">Costs</span><h2>What buying costs</h2><p>A worked example in your chosen currency. Use the USD / GBP / CAD toggle in the header.</p><div class="tablewrap"><table class="t"><thead><tr><th>Item</th><th>Example</th><th>Note</th></tr></thead><tbody>
<tr><td>Illustrative purchase price</td><td class="ccy-price" data-usd="500000"></td><td>Example only, not a real listing</td></tr>
<tr><td>Closing costs</td><td>{P("% / amount")}</td><td>{P("to confirm with partners")}</td></tr>
<tr><td>Deposit schedule</td><td>{P("per contract")}</td><td>Development-specific</td></tr>
<tr><td>Annual ownership costs</td><td>{P("taxes, HOA, insurance")}</td><td>See the <a href="investor-hub.html">Investor hub</a></td></tr></tbody></table></div>{ccy_note()}</section>
<section id="tax"><span class="eyebrow">Tax topics</span><h2>FIRPTA, ITIN and more</h2><div class="grid g2">{tx}</div><p class="rate-note" style="margin-top:12px">Tax and legal content needs human sign-off before it goes live. Not advice.</p></section>
<section id="currency"><span class="eyebrow">Currency</span><h2>GBP, USD and CAD</h2><div class="split" style="align-items:start"><p>Contracts are in USD. Prices across the site can be shown in GBP or CAD using a daily rate feed, with the rate date displayed.</p><div class="panel warm"><span class="label">Converter (example rates)</span><div class="kpi" style="margin-top:12px"><div class="v ccy-price" data-usd="250000"></div><div class="k">US$250,000 in your currency</div></div><div class="chips" style="margin-top:16px">{chips}</div>{ccy_note()}</div></div></section>
<section id="timelines"><span class="eyebrow">Timelines</span><h2>How long it takes</h2><div class="steps-h"><div><h3>Discovery</h3><p style="font-size:16px">{P("weeks")}</p></div><div><h3>Reserve &amp; contract</h3><p style="font-size:16px">{P("weeks")}</p></div><div><h3>Build</h3><p style="font-size:16px">{P("per development")}</p></div><div><h3>Completion</h3><p style="font-size:16px">{P("weeks")}</p></div></div></section>
<section id="guide"><span class="eyebrow">Guide download</span><h2>The UK buyer’s guide</h2><div class="panel linen split"><div><p>Tax, currency and timelines in one PDF. Drafted automatically and reviewed by a partner before each release.</p><p class="rate-note">Version {P("v1")} &middot; updated {P("date")} &middot; change note {P("…")}</p></div><form class="form" data-mock data-source="guide download: UK buyer's guide"><label>Email<input type="email"></label><div class="captured"></div><button class="btn">Email me the guide</button></form></div></section>
<section id="book"><span class="eyebrow">Call booking</span><h2>Speak to an advisor at a UK-friendly time</h2><div class="split" style="align-items:start"><div><p>Thirty minutes with an ABI advisor. Bring your questions on budget, currency and timing.</p><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 30-minute call</a></div><div class="panel">{booking_mock()}</div></div></section>'''
    b=hero("Buying from the UK","Buying in Florida from the UK","The six-step journey, costs, tax topics, currency and timelines, written for UK and international buyers.","img:london-thames",'<a class="btn light" href="#journey">Start with the journey</a><a class="btn ghost" href="'+CAL+'" target="_blank" rel="noopener">Book a call</a>',crumbs=crumbs(("index.html","Home"),(None,"Buying from the UK")))
    b+=f'<div class="with-side">{sidenav(secs)}<div class="content">{c}</div></div>'
    page("buying-from-the-uk.html",b)

def about():
    secs=[("history","History"),("pioneering","Pioneering"),("team","Team"),("offices","Offices")]
    team=''.join(f'<div class="card" style="box-shadow:none">{photo("ph-interior","Portrait placeholder",chr(32)+"style=\"aspect-ratio:4/5\"")}<div class="body"><h3>{P("Team member name")}</h3><span class="label">{P("Role")}</span><p>{P("Specialties")}</p><div class="meta"><a class="textlink" href="{CAL}" target="_blank" rel="noopener">Book a call</a></div></div></div>' for _ in range(4))
    ms='<div class="kpi"><div class="v">30+</div><div class="k">Years of sales history in the US &amp; UK</div></div><div class="kpi"><div class="v">$6.5+ Billion</div><div class="k">Sold</div></div>'+''.join(f'<div class="kpi"><div class="v" style="font-size:22px">{P("year")}</div><div class="k">{P("milestone")}</div></div>' for _ in range(2))
    c=f'''<section id="history"><span class="eyebrow">History</span><h2>Our story</h2><div class="split" style="align-items:start"><p class="lede">{P("Company history, from the current abire.co.uk About page")}</p><div class="grid g2">{ms}</div></div></section>
{pioneering(compact=True)}
<section id="team"><span class="eyebrow">Team</span><h2>The people you’ll work with</h2><p>Profiles rewritten with roles, specialties and a booking link.</p><div class="grid g4">{team}</div></section>
<section id="offices"><span class="eyebrow">Offices</span><h2>UK and US</h2><div class="grid g2"><div class="panel"><h3>United Kingdom</h3><p>{P("UK office address")}<br>{P("UK number")}</p></div><div class="panel"><h3>United States</h3><p>{P("US office address")}<br>{P("US number")}</p></div></div></section>'''
    b=hero("About ABI","About ABI Group",P("One-line positioning — to confirm"),"img:london-dusk",short=True,crumbs=crumbs(("index.html","Home"),(None,"About")))
    b+=f'<div class="with-side">{sidenav(secs)}<div class="content">{c}</div></div>'
    page("about.html",b)

def contact():
    b=hero("Contact","Contact and book a call","Send an enquiry, book a call at a UK-friendly time, or ring our UK or US team.","ph-navy",short=True,crumbs=crumbs(("index.html","Home"),(None,"Contact")))
    b+=f'''<section class="section"><div class="wrap split" style="align-items:start"><div class="panel">{enquiry_form("contact page")}</div><div><div class="panel cool" style="margin-bottom:24px">{booking_mock()}<a class="btn" style="margin-top:16px" href="{CAL}" target="_blank" rel="noopener">Book via Calendly</a></div>
<div class="grid g2"><div class="kpi"><div class="v" style="font-size:20px">{P("UK number")}</div><div class="k">United Kingdom</div></div><div class="kpi"><div class="v" style="font-size:20px">{P("US number")}</div><div class="k">United States</div></div></div><p style="margin-top:20px">{P("Email address")}</p></div></div></section>'''
    page("contact.html",b)

def areas():
    names=[("orlando","Orlando","img:orlando"),("kissimmee","Kissimmee","img:kissimmee"),("championsgate","ChampionsGate","img:championsgate"),("davenport","Davenport","img:davenport"),("lake-nona","Lake Nona","img:lake-nona"),("windermere","Windermere","img:windermere")]
    tiles=''.join(f'<a class="tile" id="{i}" href="#guide">{photo(c,"")}<div class="t"><h3>{n}</h3><span>Guide &rarr;</span></div></a>' for i,n,c in names)
    pts=[(470,150,"ORLANDO","#0F1D35"),(560,210,"AIRPORT (MCO)","#6B5C4E"),(390,260,"THEME PARKS","#6B5C4E"),(430,340,"KISSIMMEE","#0F1D35"),(300,400,"CHAMPIONSGATE","#0F1D35"),(200,440,"DAVENPORT","#0F1D35"),(590,300,"LAKE NONA","#0F1D35"),(320,190,"WINDERMERE","#0F1D35")]
    mapsvg='<svg viewBox="0 0 800 500"><rect width="800" height="500" fill="#E8DFC8"/><g stroke="#C4A35A" stroke-width="2" fill="none" opacity=".7"><path d="M0 330 C200 300 400 360 800 300"/><path d="M420 0 C430 150 380 300 400 500"/><path d="M150 0 L300 500"/></g><g font-family="Montserrat,sans-serif" font-size="11" letter-spacing="2" fill="#0F1D35">'+''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="{f}"/><text x="{x+12}" y="{y+4}">{t}</text>' for x,y,t,f in pts)+'</g><text x="20" y="485" font-family="Inter,sans-serif" font-size="11" fill="#6B5C4E">Schematic map placeholder, not to scale</text></svg>'
    b=hero("Areas","Orlando and the towns around it","Demand, rental context, and drive times to the parks and the airport.","img:palms-dusk",short=True,crumbs=crumbs(("index.html","Home"),(None,"Areas")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Area index</span><h2>Choose an area</h2><div class="grid g3" style="margin-top:24px">{tiles}</div><p class="rate-note" style="margin-top:12px">Placeholder area list. The final set comes from the current abire.co.uk location pages.</p></div></section>
<section class="section alt" id="guide"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Area guide &middot; example</span><h2>Kissimmee</h2><p>{P("What the town is like, rewritten from the abire.co.uk location page")}</p><div class="tablewrap"><table class="t"><thead><tr><th>Drive time to</th><th>Minutes</th></tr></thead><tbody><tr><td>Theme parks</td><td>{P("mins")}</td></tr><tr><td>Orlando International (MCO)</td><td>{P("mins")}</td></tr><tr><td>Downtown Orlando</td><td>{P("mins")}</td></tr></tbody></table></div><p class="rate-note">Refreshed quarterly &middot; source {P("…")} &middot; as of {P("date")}</p></div><div><span class="label">Drive-time map</span><div class="map" style="margin-top:12px">{mapsvg}</div></div></div></section>
<section class="section"><div class="wrap">{isla_prompt("Which area suits you? Ask Isla.")}</div></section>'''
    page("areas.html",b)

def services():
    sv=[("bank","Financing","Lenders who work with overseas buyers."),("fx","Currency (FX)","GBP and CAD transfers."),("scale","Legal","Contract and closing support."),("doc","Tax","FIRPTA, ITIN and cross-border tax."),("home","Property management","Letting, maintenance and owner reporting."),("key","Furnishing &amp; handover","Ready-to-use homes at completion.")]
    cards=''.join(f'<div class="card"><div class="body">{line_icon(i)}<h3>{t}</h3><p>{d}</p><div class="meta"><span class="label">Partner</span><span>{P("partner name")}</span></div><a class="textlink" href="#intro" style="margin-top:12px;align-self:flex-start">Request introduction</a></div></div>' for i,t,d in sv)
    b=hero("Services","A partner, not just a broker","Financing, FX, legal, tax and property management, shown as a partner network.","img:signing-warm",short=True,crumbs=crumbs(("index.html","Home"),(None,"Services")))
    b+=f'''<section class="section"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="section alt" id="intro"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Partner introductions</span><h2>Ask for an introduction</h2><p>Tell us what you need and your advisor will introduce the right partner.</p></div><div class="panel">{enquiry_form("services: partner introduction","Request an introduction")}</div></div></section>'''
    page("services.html",b)

def sell():
    b=hero("Sell","How ABI markets and sells your property","A clear process, marketing to UK and international buyers, and a named advisor.","img:sell-hero",short=True,crumbs=crumbs(("index.html","Home"),(None,"Sell")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Process</span><h2>Four steps to sold</h2><div class="steps-h" style="margin-top:30px"><div><h3>Valuation</h3><p style="font-size:16px">A market appraisal of your home.</p></div><div><h3>Preparation</h3><p style="font-size:16px">Photography, listing and pricing.</p></div><div><h3>Marketing</h3><p style="font-size:16px">UK, US and international reach. {P("channels")}</p></div><div><h3>Sale &amp; closing</h3><p style="font-size:16px">Offers, negotiation and closing support.</p></div></div><p class="rate-note" style="margin-top:12px">Draft steps. Refresh from the current abire.co.uk Sell page.</p></div></section>
<section class="section alt"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Valuation request</span><h2>What’s my home worth?</h2><p>Share a few details and an advisor will come back with a valuation.</p></div><form class="form panel" data-mock data-source="valuation request"><label>Property address<input></label><div class="row"><label>Bedrooms<select><option>1</option><option>2</option><option>3</option><option>4</option><option>5+</option></select></label><label>Property type<select><option>Condo</option><option>Townhouse</option><option>Single family</option><option>Villa</option></select></label></div><div class="row"><label>Name<input></label><label>Email<input type="email"></label></div><div class="captured"></div><button class="btn">Request valuation</button></form></div></section>'''
    page("sell.html",b)

ARTS=[("Market update","Orlando market update "+P("month"),"img:insight-market"),("Explainer","Branded residences explained","img:interior-living"),("Explainer","Leaseback, in plain English","img:resale"),("Guide","FIRPTA and ITIN for UK buyers","img:signing-bw"),("Buyer story",P("Named buyer story"),"img:areas-hero"),("Market update","Currency and buying power "+P("quarter"),"img:about-hero")]
def art_card(k,t,c,body=True):
    extra=f'<p>Source and as-of date shown on the article.</p><div class="meta"><span class="label">{P("date")}</span><span>Read &rarr;</span></div>' if body else ''
    return f'<a class="card" href="insights-article.html"><div style="position:relative">{photo(c,"")}<span class="tag soon">{k}</span></div><div class="body"><h3>{t}</h3>{extra}</div></a>'
def insights():
    b=hero("Insights","Market updates, explainers and guides","Every page shows its source and as-of date. Anything touching tax, legal or returns is approved by a person first.","img:insights-hero",short=True,crumbs=crumbs(("index.html","Home"),(None,"Insights")))
    fl=''.join(f'<button class="chip"{" aria-pressed=true" if i==0 else ""}>{t}</button>' for i,t in enumerate(["All","Market updates","Explainers","Guides","Buyer stories"]))
    gd=''.join(f'<div class="panel">{line_icon("doc")}<h3>{t}</h3><p style="font-size:16px">{d}</p><a class="textlink" href="buying-from-the-uk.html#guide">Download</a></div>' for t,d in [("UK buyer’s guide","Tax, currency and timelines."),("Branded residences explained","Drafted from AMBAR’s branded-residence content."),("Area guide pack","Drive times and town profiles.")])
    b+=f'''<section class="section"><div class="wrap"><div class="chips" data-chipgroup style="margin-bottom:28px">{fl}</div><div class="grid g3">{''.join(art_card(*a) for a in ARTS)}</div><p class="rate-note" style="margin-top:14px">Every card opens the single article template for the mock.</p></div></section>
<section class="section alt"><div class="wrap"><span class="eyebrow">Guide downloads</span><h2>Guides</h2><div class="grid g3">{gd}</div></div></section>
<section class="section"><div class="wrap split"><div><span class="eyebrow">Email sign-up</span><h2>Monthly market update</h2><p>One email a month with the latest update and new guides.</p></div><form class="form" data-mock data-source="insights sign-up"><div class="row"><label>Email<input type="email"></label><label>Country<select><option>United Kingdom</option><option>Canada</option><option>Other</option></select></label></div><div class="captured"></div><button class="btn">Sign up</button></form></div></section>'''
    page("insights.html",b)

def article():
    cr='<div class="breadcrumbs" style="color:var(--stone-dark)"><a href="index.html">Home</a> / <a href="insights.html">Insights</a> / Article</div>'
    b=f'''<section class="section" style="border:0;padding-top:70px;padding-bottom:40px"><div class="wrap" style="max-width:780px">{cr}<span class="eyebrow">Explainer &middot; article template</span><h1 style="font-size:clamp(28px,4vw,44px)">Branded residences explained</h1>
<div class="panel cool" style="display:flex;gap:24px;flex-wrap:wrap;padding:14px 18px;font-family:Inter,sans-serif;font-size:13px"><span><b>Source:</b> {P("source")}</span><span><b>As of:</b> {P("date")}</span><span><b>Approved by:</b> {P("name, role")}</span><span><b>Change log:</b> {P("v1")}</span></div></div></section>
<div class="wrap" style="max-width:1000px">{photo("img:interior-living","",'style="aspect-ratio:21/9"')}</div>
<section class="section" style="border:0;padding-top:50px"><div class="wrap" style="max-width:720px"><p class="lede">{P("Standfirst, drafted from AMBAR’s branded-residence content and generalised beyond one brand")}</p>
<h2>What a branded residence is</h2><p>{P("Body copy")}</p><p class="quote" style="border-left:2px solid var(--gold);padding-left:24px;margin:34px 0">{P("Pull quote in the accent italic")}</p><h2>Branded versus unbranded</h2><p>{P("Body copy")}</p>
<div class="tablewrap"><table class="t"><thead><tr><th></th><th>Branded</th><th>Unbranded</th></tr></thead><tbody><tr><td>Management</td><td>{P("…")}</td><td>{P("…")}</td></tr><tr><td>Standards</td><td>{P("…")}</td><td>{P("…")}</td></tr><tr><td>Owner use</td><td>{P("…")}</td><td>{P("…")}</td></tr></tbody></table></div>
<div style="margin-top:34px">{disclaimer("this article")}</div>
<div class="panel linen" style="margin-top:34px"><h3>Get the monthly update</h3><form class="form" data-mock data-source="article sign-up"><label>Email<input type="email"></label><div class="captured"></div><button class="btn">Sign up</button></form></div></div></section>
<section class="section alt"><div class="wrap"><span class="eyebrow">Related</span><div class="grid g3">{''.join(art_card(*a,body=False) for a in ARTS[2:5])}</div></div></section>'''
    page("insights-article.html",b)

def brokers():
    b=hero("Brokers","For brokers and referral partners","Register for project packs and an availability summary for AMBAR.","img:signing-desk",short=True,crumbs=crumbs(("index.html","Home"),(None,"Brokers")))
    b+=f'''<section class="section"><div class="wrap grid g3"><div class="panel">{line_icon("doc")}<h3>Project packs</h3><p style="font-size:16px">Brochure, fact sheet, floor plans and price list per development.</p><a class="textlink" href="#register">Register to download</a></div><div class="panel">{line_icon("chart")}<h3>Availability summary</h3><p style="font-size:16px">Units available and lowest price for AMBAR Building 1.</p><span class="label">35 of 132 available (sample)</span></div><div class="panel">{line_icon("people")}<h3>Referral terms</h3><p style="font-size:16px">{P("Referral / co-broke terms — to confirm")}</p></div></div></section>
<section class="section alt" id="register"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Registration</span><h2>Register as a broker</h2><p>Builds on the AMBAR broker interest feature.</p></div><form class="form panel" data-mock data-source="broker registration"><div class="row"><label>Name<input></label><label>Brokerage<input></label></div><div class="row"><label>Email<input type="email"></label><label>Licence / country<input></label></div><label>Developments of interest<select><option>AMBAR</option><option>All</option></select></label><div class="captured"></div><button class="btn">Register</button></form></div></section>'''
    page("brokers.html",b)

def investor():
    secs=[("costs","Ownership costs"),("branded","Branded vs unbranded"),("rental","Rental programme basics"),("exit","Exit and resale"),("disclaimers","Disclaimers")]
    rl=''.join(f'<li>{t} {P("…")}</li>' for t in ["Who operates the programme","Owner-use rules","Fees and reporting","Occupancy limits"])
    c=f'''<section id="costs"><span class="eyebrow">Cost explainers</span><h2>What ownership costs</h2><div class="tablewrap"><table class="t"><thead><tr><th>Cost</th><th>Example</th><th>Frequency</th></tr></thead><tbody>
<tr><td>Illustrative purchase price</td><td class="ccy-price" data-usd="400000"></td><td>One-off</td></tr><tr><td>Property tax</td><td>{P("amount / %")}</td><td>Annual</td></tr><tr><td>HOA / service charge</td><td>{P("amount")}</td><td>Monthly</td></tr><tr><td>Insurance</td><td>{P("amount")}</td><td>Annual</td></tr><tr><td>Management</td><td>{P("%")}</td><td>Ongoing</td></tr></tbody></table></div>{ccy_note()}</section>
<section id="branded"><span class="eyebrow">Branded versus unbranded</span><h2>Two kinds of ownership</h2><div class="grid g2"><div class="panel linen"><h3>Branded</h3><p style="font-size:16px">{P("Generalised from AMBAR’s branded-residence and tier explainer")}</p></div><div class="panel linen"><h3>Unbranded</h3><p style="font-size:16px">{P("…")}</p></div></div><a class="textlink" href="insights-article.html" style="display:inline-block;margin-top:16px">Read: Branded residences explained</a></section>
<section id="rental"><span class="eyebrow">Rental programme basics</span><h2>How rental programmes work</h2><p>How a programme is run, who manages bookings, and what owners should ask. This section describes structure only. It does not state income or returns.</p><ul class="list-check">{rl}</ul></section>
<section id="exit"><span class="eyebrow">Exit and resale</span><h2>Selling later</h2><p>{P("Resale process and FIRPTA withholding note")} <a href="sell.html">How ABI sells</a></p></section>
<section id="disclaimers"><span class="eyebrow">Disclaimers</span>{disclaimer("the Investor hub")}</section>'''
    b=hero("Investor hub","Ownership economics, explained plainly","Costs, branded versus unbranded, rental programme basics, and exit. No return promises.","img:interior-library",short=True,crumbs=crumbs(("index.html","Home"),(None,"Investor hub")))
    b+=f'<div class="with-side">{sidenav(secs)}<div class="content">{c}</div></div>'
    page("investor-hub.html",b)

def devpartners():
    pl=''.join(f'<div class="panel linen" style="text-align:center;padding:40px 12px">{P("Developer partner")}</div>' for _ in range(4))
    hw=''.join(f'<div class="panel">{line_icon(i)}<h3>{t}</h3><p style="font-size:16px">{d}</p></div>' for i,t,d in [("home","Development template","Each project gets its own page set on a shared template, with disclaimers built in."),("chat","Isla","ABI&rsquo;s AI concierge answers buyer questions across every project and hands warm leads to a named ABI advisor."),("chart","Live availability","Where ABI controls inventory, buyers see live availability and pricing.")])
    b=hero("Developer partners","Bring your project to ABI","How ABI represents developments, and how to enquire. Also the entry point for new projects.","img:ambar-aerial",short=True,crumbs=crumbs(("index.html","Home"),(None,"Developer partners")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Partners</span><h2>Developers we work with</h2><div class="grid g4">{pl}</div></div></section>
<section class="section alt"><div class="wrap"><span class="eyebrow">How ABI represents projects</span><h2>A template, a concierge and a UK audience</h2><div class="grid g3">{hw}</div></div></section>
<section class="section"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Enquiry</span><h2>Talk to us about your project</h2></div><form class="form panel" data-mock data-source="developer enquiry"><div class="row"><label>Name<input></label><label>Company<input></label></div><div class="row"><label>Email<input type="email"></label><label>Project location<input></label></div><label>About the project<textarea rows="4"></textarea></label><div class="captured"></div><button class="btn">Send enquiry</button></form></div></section>'''
    page("developer-partners.html",b)

def compare():
    rows=[("Stage","Selling","Coming soon"),("Location","Orlando","North Bay Village, Miami"),("Residences","132 (Building 1)",P("TBC")),("Floor plans","9, studio to 3 bed",P("TBC")),("Price from",P("to confirm"),P("TBC")),("Live availability","Yes (sample: 35 available)","No, register interest"),("Brand",P("to confirm"),P("TBC"))]
    tbl=''.join(f'<tr><td>{a}</td><td data-col="1">{b}</td><td data-col="2">{c}</td><td data-col="3" style="opacity:.35">{P("—")}</td></tr>' for a,b,c in rows)
    b=hero("Compare","Compare up to three","Side-by-side developments, floor plans and areas, in plain attributes.","img:interior-modern",short=True,crumbs=crumbs(("index.html","Home"),(None,"Compare")))
    b+=f'''<section class="section"><div class="wrap"><div class="chips" data-chipgroup style="margin-bottom:24px"><button class="chip" aria-pressed="true">Developments</button><button class="chip">Floor plans</button><button class="chip">Areas</button></div>
<div class="tablewrap"><table class="t compare"><thead><tr><th>Attribute</th><th><a href="development-ambar.html">AMBAR</a></th><th><a href="development-continuum-miami.html">Continuum Miami</a></th><th><select data-compare="3" class="chip"><option value="">+ Add item</option><option value="x">[Third item]</option></select></th></tr></thead><tbody>{tbl}</tbody></table></div><p class="rate-note" style="margin-top:12px">Most useful once there are two or more projects. Values come from the development template.</p></div></section>'''
    page("compare.html",b)

def events():
    ev=[("UK roadshow",P("City, date")),("AMBAR launch webinar",P("Date, UK time")),("Buying from the UK: Q&amp;A",P("Date, UK time"))]
    rows=''.join(f'<tr><td><b style="color:var(--navy)">{e}</b></td><td>{w}</td><td style="text-align:right"><a class="btn small" href="#register">Register</a></td></tr>' for e,w in ev)
    rec=''.join(f'<div class="card">{photo(c,"Video placeholder")}<div class="body"><h3>{t}</h3><span class="label">{P("duration")}</span></div></div>' for t,c in [("Site walkthrough","img:ambar-cafe-outdoor"),("Area tour","img:orlando"),("Developer interview","img:events-talk")])
    b=hero("Events","Roadshows, launches and webinars","Meet the team in the UK, or join online. Recordings for anything you miss.","img:events-hero",short=True,crumbs=crumbs(("index.html","Home"),(None,"Events")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Upcoming</span><h2>Event list</h2><div class="tablewrap"><table class="t"><thead><tr><th>Event</th><th>When &amp; where</th><th></th></tr></thead><tbody>{rows}</tbody></table></div><p class="rate-note" style="margin-top:10px">Example event types only. No dates are set.</p></div></section>
<section class="section alt" id="register"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Registration</span><h2>Save your place</h2><p>Registration feeds the email sequence.</p></div><form class="form panel" data-mock data-source="event registration"><label>Event<select>{''.join(f'<option>{e}</option>' for e,_ in ev)}</select></label><div class="row"><label>Name<input></label><label>Email<input type="email"></label></div><div class="captured"></div><button class="btn">Register</button></form></div></section>
<section class="section"><div class="wrap"><span class="eyebrow">Recordings</span><h2>Watch again</h2><div class="grid g3">{rec}</div></div></section>'''
    page("events.html",b)

def client():
    st=["Call","Residence","Contract","Finance &amp; legal","Build","Handover"]
    sb=''.join(f'<div class="{"done" if i<2 else "now" if i==2 else ""}">{s}</div>' for i,s in enumerate(st))
    sv=''.join(f'<div class="panel" style="margin-bottom:12px;display:flex;justify-content:space-between;gap:10px"><span><b style="color:var(--navy)">AMBAR &middot; {r}</b><br><span style="font-size:15px">{p} &middot; sample</span></span><a class="textlink" href="development-ambar.html#availability">View</a></div>' for r,p in [("Residence 705","1 bed"),("Residence 912","2 bed")])
    dc=''.join(f'<li>{d} <span class="label" style="float:right">{s}</span></li>' for d,s in [("Reservation form","Signed"),("Purchase agreement","To sign"),("ID &amp; proof of address","Uploaded"),("Deposit schedule","View")])
    b=hero("Client area","Welcome back, "+P("Buyer name"),"Saved homes, documents, journey status and messages with your advisor. (Mock account view.)","ph-navy",short=True,crumbs=crumbs(("index.html","Home"),(None,"Client area")))
    b+=f'''<section class="section"><div class="wrap"><span class="eyebrow">Journey status</span><h2>Where you are</h2><div class="status">{sb}</div><p class="rate-note">Sample status: step 3 of 6, Reserve and contract.</p></div></section>
<section class="section alt"><div class="wrap grid g3"><div><h3>Saved homes</h3>{sv}<a class="textlink" href="compare.html">Compare saved</a></div>
<div><h3>Documents</h3><ul class="list-check">{dc}</ul><p class="rate-note">Example document list.</p></div>
<div><h3>Messages</h3><div class="panel cool" style="display:grid;gap:10px;grid-template-columns:minmax(0,1fr)"><div class="msg bot">Hi, the purchase agreement is ready for review. Any questions before Thursday? {P("Advisor")}</div><div class="msg me" style="justify-self:end">Thanks, I’ll read it tonight.</div><form class="form" data-mock data-source="client message" style="grid-template-columns:1fr auto;display:grid;gap:8px"><input placeholder="Write a message" aria-label="Message"><button class="btn small">Send</button></form></div></div></div></section>'''
    page("client-area.html",b)

def press():
    cov=''.join(f'<li>{P("Publication")}: {P("headline")} <span class="label" style="float:right">{P("date")}</span></li>' for _ in range(4))
    aw=''.join(f'<div class="panel linen" style="text-align:center;padding:30px 10px">{P("Award")}</div>' for _ in range(4))
    roles=''.join(f'<tr><td>{P("Role title")}</td><td>{P("UK / US")}</td><td>{P("Full time")}</td><td style="text-align:right"><a class="textlink" href="contact.html">Apply</a></td></tr>' for _ in range(3))
    b=hero("Press &amp; careers","Press and careers","Coverage and awards, plus open roles and referral partner sign-up.","img:press-hero",short=True,crumbs=crumbs(("index.html","Home"),(None,"Press &amp; careers")))
    b+=f'''<section class="section"><div class="wrap split" style="align-items:start"><div><span class="eyebrow">Press</span><h2>Coverage</h2><ul class="list-check">{cov}</ul><p style="margin-top:16px">Press enquiries: {P("press email")}</p></div>
<div><span class="eyebrow">Awards</span><h2>Recognition</h2><div class="grid g2">{aw}</div></div></div></section>
<section class="section alt"><div class="wrap"><span class="eyebrow">Careers</span><h2>Open roles</h2><div class="tablewrap"><table class="t"><thead><tr><th>Role</th><th>Location</th><th>Type</th><th></th></tr></thead><tbody>{roles}</tbody></table></div><p class="rate-note" style="margin-top:10px">Only if ABI wants a careers section (open decision).</p>
<div class="panel" style="margin-top:30px"><h3>Referral partners</h3><p style="font-size:16px">Introduce buyers to ABI. <a href="brokers.html">Register as a referral partner</a></p></div></div></section>'''
    page("press-careers.html",b)

def notfound():
    META["404.html"]=("404.html","Not found",1,"—","—","—")
    page("404.html",'<section class="section" style="min-height:50vh"><div class="wrap"><span class="eyebrow">404</span><h1>Page not found</h1><p><a href="index.html">Return home</a></p></div></section>')

if __name__=="__main__":
    home(); developments(); dev_template("development-ambar.html","AMBAR",True); dev_template("development-continuum-miami.html","Continuum Miami",False)
    buy(); uk(); about(); contact(); areas(); services(); sell(); insights(); article(); brokers(); investor(); devpartners(); compare(); events(); client(); press(); notfound()
    open(os.path.join(OUT,"robots.txt"),"w").write("User-agent: *\nDisallow: /\n")
    print("built",len(PAGES)+1,"html files")
