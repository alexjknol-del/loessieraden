# -*- coding: utf-8 -*-
"""Hulpfuncties en vaste waarden voor de contentmodules."""

MILEZ = "https://milezbracelets.nl"
MAEYA = "https://www.maeyajewelry.nl"


def milez(path="/", label="Milez Bracelets"):
    return '<a href="%s%s">%s</a>' % (MILEZ, path, label)


def maeya(path="/", label="Maeya Jewelry"):
    return '<a href="%s%s">%s</a>' % (MAEYA, path, label)


def url_milez(path="/"):
    return '<a href="%s%s">%s%s</a>' % (MILEZ, path, MILEZ, path)


def url_maeya(path="/"):
    return '<a href="%s%s">%s%s</a>' % (MAEYA, path, MAEYA, path)


def page(url, nav_title, title, description, h1, lede, blocks,
         parent=None, shops=None, rail=True, faq_schema=None):
    return {
        "url": url,
        "nav_title": nav_title,
        "title": title,
        "description": description,
        "h1": h1,
        "lede": lede,
        "blocks": blocks,
        "parent": parent,
        "shops": shops,
        "rail": rail,
        "faq_schema": faq_schema,
    }
