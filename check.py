#!/usr/bin/env python3
"""Controle op de gebouwde site in dist/."""
import os, re, sys, html
from collections import Counter

ROOT = "dist"
problems = []

files = []
for base, _, names in os.walk(ROOT):
    for n in names:
        if n.endswith(".html"):
            files.append(os.path.join(base, n))

titles, descs = Counter(), Counter()
internal_targets = set()
for f in files:
    rel = "/" + os.path.relpath(f, ROOT).replace("index.html", "").replace("\\", "/")
    internal_targets.add(rel if rel.endswith("/") else rel)
internal_targets.add("/404.html")

BAD_WORDS = [
    (r"\b(je|jij|jou|jouw|jullie|uw)\b", "tweede persoon"),
    (r"\b(wij|we|ons|onze)\b", "wij-vorm"),
    (r"\b(goedkoop|goedkope|goedkoper|duur|dure|duurder|gratis|korting|prijs|prijzen|prijskaartje|prijskaartjes|euro)\b", "prijstaal"),
    (r"lorem ipsum", "dummytekst"),
    (r"\bTODO\b", "dummytekst"),
    (r"—|–", "em- of en-dash"),
]

for f in sorted(files):
    src = open(f, encoding="utf-8").read()
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", src, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    text = re.sub(r"\s+", " ", text)

    t = re.search(r"<title>(.*?)</title>", src, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', src, re.S)
    if not t or not d:
        problems.append("%s: title of description ontbreekt" % f)
        continue
    titles[t.group(1)] += 1
    descs[d.group(1)] += 1
    if len(t.group(1)) > 65:
        problems.append("%s: title %d tekens" % (f, len(t.group(1))))
    if not (80 <= len(d.group(1)) <= 165):
        problems.append("%s: description %d tekens" % (f, len(d.group(1))))
    if len(re.findall(r"<h1", src)) != 1:
        problems.append("%s: aantal h1 is %d" % (f, len(re.findall(r"<h1", src))))

    for pat, label in BAD_WORDS:
        for m in set(x.lower() if isinstance(x, str) else x for x in re.findall(pat, text, re.I)):
            problems.append("%s: %s (%s)" % (f, label, m))

    for href, anchor in re.findall(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', body, re.S):
        anchor_txt = re.sub(r"<[^>]+>", "", anchor).strip()
        if href.startswith("http"):
            ok = ("Milez" in anchor_txt or "Maeya" in anchor_txt
                  or anchor_txt in ("Consumentenbond", "Milieu Centraal")
                  or anchor_txt.startswith("https://") or anchor_txt.startswith("http://"))
            if not ok:
                problems.append("%s: ankertekst uitgaande link niet toegestaan: %r -> %s" % (f, anchor_txt, href))
        elif href.startswith("/") and not href.startswith("//"):
            target = href.split("#")[0]
            if target and target not in internal_targets:
                problems.append("%s: interne link zonder pagina: %s" % (f, target))

for t, c in titles.items():
    if c > 1:
        problems.append("dubbele title (%dx): %s" % (c, t))
for d, c in descs.items():
    if c > 1:
        problems.append("dubbele description (%dx): %s" % (c, d))

print("%d html-bestanden gecontroleerd" % len(files))
if problems:
    print("%d punten:" % len(problems))
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("geen problemen gevonden")
