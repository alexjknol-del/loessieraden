# -*- coding: utf-8 -*-
import c_stijl, c_materialen, c_maten, c_onderhoud, c_cadeau, c_overig

SITE = {"kicker": "Sieradeninspiratie"}

PAGES = ([c_overig.HOME] + c_stijl.PAGES + c_materialen.PAGES + c_maten.PAGES
         + c_onderhoud.PAGES + c_cadeau.PAGES + c_overig.PAGES)
