#!/usr/bin/env python3
"""Generator voor loessieraden.nl. Geen externe afhankelijkheden."""
import os, re, shutil, html
from datetime import date

from content import PAGES, SITE

OUT = "dist"
DOMAIN = "https://loessieraden.nl"

NAV = [
    ("/stijl/", "Stijl"),
    ("/materialen/", "Materialen"),
    ("/maten/", "Maten"),
    ("/onderhoud/", "Onderhoud"),
    ("/cadeau/", "Cadeau"),
    ("/veelgestelde-vragen/", "Vragen"),
    ("/contact/", "Contact"),
]

CSS = """
:root{
  --paper:#faf7f2; --paper-2:#f2ece3; --ink:#231f1b; --ink-soft:#5c544b;
  --line:#ded4c6; --brass:#95763c; --rose:#a9756c; --white:#fffdfa;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);
  font:16px/1.65 "Helvetica Neue",Helvetica,Arial,sans-serif}
h1,h2,h3,.serif{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:600;letter-spacing:.1px}
h1{font-size:2.1rem;line-height:1.2;margin:0 0 .6rem}
h2{font-size:1.35rem;margin:2.4rem 0 .7rem}
h3{font-size:1.05rem;margin:1.6rem 0 .4rem}
p{margin:0 0 1rem}
a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--brass)}
a:hover{color:var(--brass)}
.wrap{max-width:1060px;margin:0 auto;padding:0 22px}
header.top{border-bottom:1px solid var(--line);background:var(--white)}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:16px 0}
.brand{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-size:1.25rem;border:0;letter-spacing:.5px}
.brand span{color:var(--brass)}
nav.main{display:flex;flex-wrap:wrap;gap:16px}
nav.main a{border:0;font-size:.92rem;color:var(--ink-soft);padding:2px 0;border-bottom:1px solid transparent}
nav.main a:hover,nav.main a[aria-current="page"]{color:var(--ink);border-bottom-color:var(--brass)}
.crumb{font-size:.83rem;color:var(--ink-soft);padding:18px 0 0}
.crumb a{border:0;color:var(--ink-soft)}
.crumb a:hover{color:var(--brass)}
main{padding:6px 0 40px}
.lede{font-size:1.08rem;color:var(--ink-soft);max-width:62ch}
.cols{display:grid;grid-template-columns:minmax(0,1fr) 250px;gap:44px;align-items:start}
article{max-width:70ch}
aside.rail{position:sticky;top:22px;font-size:.9rem}
aside.rail h4{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);margin:0 0 .6rem;font-weight:600}
aside.rail ol{list-style:none;margin:0;padding:0}
aside.rail li{padding:.32rem 0;border-top:1px solid var(--line)}
aside.rail a{border:0;color:var(--ink-soft)}
aside.rail a:hover{color:var(--brass)}
ul.plain{padding-left:1.1rem}
ul.plain li{margin:.3rem 0}
.rows{border-top:1px solid var(--line);margin:1.4rem 0}
.row{display:grid;grid-template-columns:34px minmax(0,1fr);gap:16px;padding:16px 2px;border-bottom:1px solid var(--line);align-items:start}
.row .num{font-family:"Iowan Old Style",Georgia,serif;color:var(--brass);font-size:.95rem;padding-top:2px}
.row h3{margin:0 0 .25rem;font-size:1.02rem}
.row p{margin:0;color:var(--ink-soft);font-size:.95rem}
.row a{border:0}
.row a:hover h3{color:var(--brass)}
table{border-collapse:collapse;width:100%;font-size:.95rem;margin:1rem 0}
th,td{text-align:left;padding:.5rem .6rem;border-bottom:1px solid var(--line)}
th{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);font-weight:600}
.note{background:var(--paper-2);border-left:2px solid var(--brass);padding:.9rem 1.1rem;margin:1.6rem 0;font-size:.96rem}
.note p:last-child{margin:0}
.shops{border-top:1px solid var(--line);margin-top:2.6rem;padding-top:1.2rem}
.shops h2{margin-top:0;font-size:1.05rem}
.shops p{font-size:.96rem}
.hero{padding:46px 0 8px;border-bottom:1px solid var(--line);margin-bottom:26px}
.hero .kicker{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--brass);margin-bottom:.8rem}
.hero h1{font-size:2.6rem;max-width:20ch}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);margin:2rem 0}
.tile{background:var(--white);padding:22px 20px}
.tile a{border:0}
.tile h3{margin:.5rem 0 .3rem}
.tile p{color:var(--ink-soft);font-size:.94rem;margin:0}
.tile svg{display:block}
.faq dt{font-weight:600;margin-top:1.3rem}
.faq dd{margin:.3rem 0 0;color:var(--ink-soft)}
footer.bot{border-top:1px solid var(--line);background:var(--white);margin-top:40px}
.footgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:26px;padding:30px 0}
.footgrid h4{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);margin:0 0 .6rem;font-weight:600}
.footgrid ul{list-style:none;margin:0;padding:0;font-size:.93rem}
.footgrid li{margin:.28rem 0}
.footgrid a{border:0;color:var(--ink-soft)}
.footgrid a:hover{color:var(--brass)}
.legal{border-top:1px solid var(--line);padding:14px 0 26px;font-size:.85rem;color:var(--ink-soft);display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between}
@media(max-width:820px){.cols{grid-template-columns:1fr;gap:24px}aside.rail{position:static}.hero h1{font-size:2rem}}
"""

ICONS = {
    "ring": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><circle cx="15" cy="18" r="8"/><path d="M11.5 8.5 15 4l3.5 4.5"/></svg>',
    "chain": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><path d="M4 20c4-9 18-9 22 0"/><circle cx="15" cy="22.5" r="3"/></svg>',
    "hoop": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><circle cx="15" cy="17" r="7.5"/><path d="M12 9.5a3 3 0 0 1 5 0"/></svg>',
    "band": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><ellipse cx="15" cy="15" rx="10" ry="6.5"/><path d="M11 21.5h8"/></svg>',
    "beads": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><circle cx="7" cy="15" r="2.6"/><circle cx="15" cy="15" r="2.6"/><circle cx="23" cy="15" r="2.6"/></svg>',
    "ruler": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><rect x="4" y="11" width="22" height="8"/><path d="M9 11v3M14 11v4M19 11v3"/></svg>',
    "drop": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><path d="M15 5c4 5.5 6 8.5 6 11.5a6 6 0 0 1-12 0C9 13.5 11 10.5 15 5z"/></svg>',
    "gift": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><rect x="5" y="12" width="20" height="13"/><path d="M15 12v13M5 17h20M15 12c-3.5 0-5-1-5-2.5S12 7 15 12zm0 0c3.5 0 5-1 5-2.5S18 7 15 12z"/></svg>',
    "spark": '<svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="#95763c" stroke-width="1.1"><path d="M15 5v20M5 15h20M8.5 8.5l13 13M21.5 8.5l-13 13"/></svg>',
}


def esc(t):
    return html.escape(t, quote=False)


def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append("<p>%s</p>" % b[1])
        elif kind == "h2":
            out.append("<h2 id=\"%s\">%s</h2>" % (slugify(b[1]), esc(b[1])))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % esc(b[1]))
        elif kind == "ul":
            out.append("<ul class=\"plain\">%s</ul>" % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "table":
            head = "".join("<th>%s</th>" % esc(h) for h in b[1])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % esc(str(c)) for c in r) for r in b[2])
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (head, rows))
        elif kind == "note":
            out.append("<div class=\"note\"><p>%s</p></div>" % b[1])
        elif kind == "rows":
            items = "".join(
                '<div class="row"><div class="num">%02d</div><div><a href="%s"><h3>%s</h3></a><p>%s</p></div></div>'
                % (n + 1, url, esc(t), d) for n, (url, t, d) in enumerate(b[1]))
            out.append('<div class="rows">%s</div>' % items)
        elif kind == "tiles":
            items = "".join(
                '<div class="tile">%s<a href="%s"><h3>%s</h3></a><p>%s</p></div>'
                % (ICONS.get(ic, ""), url, esc(t), d) for ic, url, t, d in b[1])
            out.append('<div class="tiles">%s</div>' % items)
        elif kind == "faq":
            items = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(q), a) for q, a in b[1])
            out.append('<dl class="faq">%s</dl>' % items)
        elif kind == "html":
            out.append(b[1])
    return "\n".join(out)


def slugify(t):
    s = t.lower()
    s = s.replace("ë", "e").replace("é", "e").replace("ï", "i").replace("ó", "o").replace("ö", "o")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def headings(blocks):
    return [b[1] for b in blocks if b[0] == "h2"]


def page_html(p, all_pages):
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if p["url"].startswith(u) and u != "/" else "", t)
        for u, t in NAV)
    crumb = ""
    if p["url"] != "/":
        parts = ['<a href="/">Home</a>']
        if p.get("parent"):
            par = next(x for x in all_pages if x["url"] == p["parent"])
            parts.append('<a href="%s">%s</a>' % (par["url"], par["nav_title"]))
        parts.append(esc(p["nav_title"]))
        crumb = '<div class="crumb">%s</div>' % " / ".join(parts)

    hs = headings(p["blocks"])
    rail = ""
    if len(hs) >= 3 and p.get("rail", True):
        rail = '<aside class="rail"><h4>Op deze pagina</h4><ol>%s</ol></aside>' % "".join(
            '<li><a href="#%s">%s</a></li>' % (slugify(h), esc(h)) for h in hs)

    body = render_blocks(p["blocks"])
    if p.get("shops"):
        body += '<div class="shops"><h2 id="waar-te-vinden">Waar te vinden</h2>%s</div>' % "".join(
            "<p>%s</p>" % s for s in p["shops"])

    inner = "<article><h1>%s</h1><p class=\"lede\">%s</p>%s</article>" % (esc(p["h1"]), p["lede"], body)
    main = '<div class="cols">%s%s</div>' % (inner, rail) if rail else inner
    if p["url"] == "/":
        main = body

    hero = ""
    if p["url"] == "/":
        hero = ('<section class="hero"><div class="wrap"><div class="kicker">%s</div>'
                '<h1>%s</h1><p class="lede">%s</p></div></section>' % (SITE["kicker"], esc(p["h1"]), p["lede"]))

    foot_cols = [
        ("Stijl", [(x["url"], x["nav_title"]) for x in all_pages if x.get("parent") == "/stijl/"]),
        ("Materialen", [(x["url"], x["nav_title"]) for x in all_pages if x.get("parent") == "/materialen/"]),
        ("Maten en onderhoud", [(x["url"], x["nav_title"]) for x in all_pages if x.get("parent") in ("/maten/", "/onderhoud/")]),
        ("Cadeau", [(x["url"], x["nav_title"]) for x in all_pages if x.get("parent") == "/cadeau/"]),
    ]
    fg = "".join(
        "<div><h4>%s</h4><ul>%s</ul></div>" % (t, "".join('<li><a href="%s">%s</a></li>' % (u, esc(n)) for u, n in items))
        for t, items in foot_cols)

    canonical = DOMAIN + p["url"]
    schema = ""
    if p.get("faq_schema"):
        import json
        schema = '<script type="application/ld+json">%s</script>' % json.dumps({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                           for q, a in p["faq_schema"]]}, ensure_ascii=False)

    return """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:url" content="%s">
<meta property="og:site_name" content="Loes Sieraden">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Ccircle cx='16' cy='19' r='9' fill='none' stroke='%%2395763c' stroke-width='2'/%%3E%%3Cpath d='M11 8l5-5 5 5' fill='none' stroke='%%2395763c' stroke-width='2'/%%3E%%3C/svg%%3E">
<style>%s</style>
%s
</head>
<body>
<header class="top"><div class="wrap topbar">
<a class="brand" href="/">Loes <span>Sieraden</span></a>
<nav class="main">%s</nav>
</div></header>
%s
<div class="wrap">%s<main>%s</main></div>
<footer class="bot"><div class="wrap">
<div class="footgrid">%s</div>
<div class="legal"><span>Loes Sieraden, sieradeninspiratie op loessieraden.nl</span>
<span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacybeleid</a> &middot; <a href="/cookiebeleid/">Cookiebeleid</a></span></div>
</div></footer>
</body>
</html>
""" % (esc(p["title"]), esc(p["description"]), canonical, esc(p["title"]), esc(p["description"]),
       canonical, CSS, schema, nav, hero, crumb, main, fg)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    for p in PAGES:
        rel = "index.html" if p["url"] == "/" else p["url"].strip("/") + "/index.html"
        write(os.path.join(OUT, rel), page_html(p, PAGES))

    nf = dict(PAGES[0])
    nf.update({"url": "/404/", "title": "Pagina niet gevonden - Loes Sieraden",
               "description": "Deze pagina bestaat niet op loessieraden.nl. Het overzicht van alle onderwerpen over sieraden staat op de homepage.",
               "h1": "Pagina niet gevonden", "nav_title": "404",
               "lede": "Deze pagina bestaat niet of heeft een ander adres gekregen.",
               "blocks": [("p", 'Het overzicht van alle onderwerpen staat op de <a href="/">homepage</a>. '
                                'Zoeken kan ook via de rubrieken <a href="/stijl/">Stijl</a>, '
                                '<a href="/materialen/">Materialen</a>, <a href="/maten/">Maten</a>, '
                                '<a href="/onderhoud/">Onderhoud</a> en <a href="/cadeau/">Cadeau</a>.')],
               "shops": None, "parent": None, "rail": False, "faq_schema": None})
    write(os.path.join(OUT, "404.html"), page_html(nf, PAGES))

    today = date.today().isoformat()
    urls = "".join("<url><loc>%s%s</loc><lastmod>%s</lastmod></url>" % (DOMAIN, p["url"], today) for p in PAGES)
    write(os.path.join(OUT, "sitemap.xml"),
          '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
    write(os.path.join(OUT, "robots.txt"), "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    print("%d pagina's gebouwd in %s/" % (len(PAGES) + 1, OUT))


if __name__ == "__main__":
    main()
