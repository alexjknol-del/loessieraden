# -*- coding: utf-8 -*-
from base import page, milez, maeya

HUB = page(
    "/materialen/", "Materialen", "Materialen van sieraden: staal, leer en steen - Loes Sieraden",
    "Overzicht van veelgebruikte materialen in sieraden: roestvrij staal, titanium, leer, natuursteen en wat waterproof in de praktijk betekent.",
    "Materialen",
    "Waar een sieraad van gemaakt is, bepaalt hoe het dagelijks draagt: gewicht, huidreactie, kleurvastheid en onderhoud.",
    [
        ("p", "De meeste sieraden die dagelijks gedragen worden, bestaan uit een handvol materialen. Ieder materiaal heeft eigen sterke punten en eigen beperkingen, en die verschillen zijn in de praktijk groter dan ze op een foto lijken."),
        ("rows", [
            ("/materialen/stainless-steel/", "Roestvrij staal", "Het meest gebruikte materiaal voor sieraden die dag en nacht in blijven."),
            ("/materialen/titanium/", "Titanium", "Licht, biocompatibel en de standaard voor piercingsieraden."),
            ("/materialen/leer/", "Leer", "Warm, soepel en het enige materiaal dat zichtbaar meegroeit met de drager."),
            ("/materialen/natuursteen/", "Natuursteen", "Onyx, tijgeroog, turquoise: kleur en tekening per steen verschillend."),
            ("/materialen/waterproof-sieraden/", "Waterproof sieraden", "Wat de term betekent bij douchen, zwemmen en zweten."),
            ("/materialen/nikkelallergie/", "Nikkelallergie", "Waarom sommige sieraden jeuk geven en welke materialen dat voorkomen."),
        ]),
    ],
    rail=False,
)

P1 = page(
    "/materialen/stainless-steel/", "Roestvrij staal",
    "Roestvrij staal in sieraden: eigenschappen - Loes Sieraden",
    "Wat roestvrij staal als sieradenmateriaal doet: kleurvastheid, hypoallergene eigenschappen, gewicht en dagelijks onderhoud.",
    "Roestvrij staal",
    "Roestvrij staal, ook wel RVS of stainless steel, is het werkpaard onder de sieradenmaterialen: kleurvast, sterk en makkelijk in onderhoud.",
    [
        ("h2", "Waarom het zo veel gebruikt wordt"),
        ("p", "Roestvrij staal roest niet, verkleurt niet en geeft niet af op de huid. Daardoor kan een sieraad blijven zitten tijdens douchen, sporten en zwemmen zonder dat de glans achteruitgaat. Ook is het materiaal recyclebaar, wat bij metalen sieraden zelden een probleem oplevert maar wel meetelt."),
        ("h2", "Huid en allergie"),
        ("p", "Sieradenstaal wordt hypoallergeen genoemd omdat het nikkel vastlegt in de legering, waardoor er nauwelijks nikkel vrijkomt aan de huid. Voor de meeste mensen met een lichte nikkelgevoeligheid is dat voldoende. Bij een sterke allergie is titanium de veiligere keuze; het verschil staat op %s." % '<a href="/materialen/nikkelallergie/">de pagina over nikkelallergie</a>',),
        ("h2", "Verguld staal"),
        ("p", "Goudkleurig staal heeft meestal een dun laagje over het staal. Dat laagje bepaalt hoe lang de kleur mooi blijft. Parfum, zonnebrand en schuurmiddelen tasten het sneller aan dan water. Wie goudkleur draagt, doet het sieraad daarom als laatste om en als eerste af."),
        ("h2", "Gewicht en draagcomfort"),
        ("p", "Staal is zwaarder dan titanium en lichter dan massief zilver in dezelfde vorm. Bij grote hoops of brede ringen is dat gewicht merkbaar; bij fijne stukken speelt het nauwelijks een rol."),
        ("h2", "Onderhoud"),
        ("ul", [
            "Lauw water met een druppel milde zeep, daarna goed afdrogen.",
            "Een zachte doek voor de glans, geen schuursponsjes of tandpasta.",
            "Bij goudkleurige afwerking geen ultrasoon bad en geen agressieve reinigers.",
        ]),
        ("p", "Uitgebreider staat dat op %s." % '<a href="/onderhoud/sieraden-schoonmaken/">de pagina over sieraden schoonmaken</a>'),
    ],
    parent="/materialen/",
    shops=[
        "Sieraden van premium roestvrij staal, ontworpen in Nederland, staan bij %s. Meer over het materiaal staat op %s." % (maeya(), maeya("/pages/materiaal", "de materiaalpagina van Maeya Jewelry")),
    ],
)

P2 = page(
    "/materialen/titanium/", "Titanium",
    "Titanium sieraden en piercings: G23 - Loes Sieraden",
    "Titanium in sieraden en piercings: implant grade G23 en ASTM F-136, gewicht, biocompatibiliteit en gangbare maten.",
    "Titanium",
    "Titanium is licht, sterk en biocompatibel. In de piercingwereld is het daarom de standaard, zeker bij verse gaatjes.",
    [
        ("h2", "Implant grade"),
        ("p", "De aanduidingen G23 en ASTM F-136 verwijzen naar titaniumlegeringen die geschikt zijn voor gebruik in het lichaam. Dat is precies wat een piercing doet: een sieraad dat door de huid gaat en daar blijft zitten terwijl het weefsel geneest."),
        ("h2", "Gewicht en gevoel"),
        ("p", "Titanium is ongeveer de helft lichter dan staal bij hetzelfde volume. Bij oorsieraden hoog in de oorschelp scheelt dat merkbaar, omdat gewicht daar aan een dunner stukje weefsel trekt."),
        ("h2", "Gangbare maten"),
        ("p", "De meeste piercingstaafjes hebben een dikte van 1,2 mm. In lengte zijn 6, 8, 10 en 12 mm gebruikelijk, waarbij 6 mm de standaard is voor een genezen oorpiercing en een langere staaf ruimte laat voor zwelling bij een verse piercing."),
        ("table", ["Maat", "Waarvoor"], [
            ["1,2 mm dikte", "Standaard voor de meeste oor- en gezichtspiercings"],
            ["6 mm lengte", "Genezen piercing, strak tegen de huid"],
            ["8 tot 10 mm", "Dikkere weefsels of net gezet, ruimte voor zwelling"],
            ["12 mm", "Navelpiercings en dikker weefsel"],
        ]),
        ("h2", "Titanium of staal"),
        ("p", "Voor genezen gaatjes voldoen beide materialen. Bij een verse piercing, een gevoelige huid of een bekende nikkelallergie heeft titanium de voorkeur. Meer over maten staat op %s." % '<a href="/maten/piercingmaten/">de pagina over piercingmaten</a>'),
    ],
    parent="/materialen/",
    shops=[
        "Titanium piercings in G23 en ASTM F-136 staan bij %s: %s." % (maeya(), maeya("/collections/piercings", "de piercingcollectie van Maeya Jewelry")),
    ],
)

P3 = page(
    "/materialen/leer/", "Leer",
    "Leer in armbanden: soort, kleur en slijtage - Loes Sieraden",
    "Leer als sieradenmateriaal: breedtes, gevlochten en glad leer, kleurverloop door dragen en wat leer niet verdraagt.",
    "Leer",
    "Leer is het enige materiaal in een sieradenla dat zichtbaar verandert door dragen. Dat is precies de aantrekkingskracht.",
    [
        ("h2", "Glad, gevlochten en rond"),
        ("p", "Glad leer heeft een strakke lijn en toont snel gebruikssporen op het oppervlak. Gevlochten leer verbergt sporen beter en heeft meer structuur, waardoor het naast kralen prettig uitkomt. Rond leer, dun en soepel, is de meest onopvallende variant."),
        ("h2", "Kleur en veroudering"),
        ("p", "Zwart leer blijft het langst gelijk. Cognac en bruin worden donkerder op de plekken waar de huid het meest raakt, waardoor een band na een jaar herkenbaar van de drager wordt. Blauw en groen gekleurd leer verbleekt het snelst in fel zonlicht."),
        ("h2", "Wat leer slecht verdraagt"),
        ("ul", [
            "Langdurig contact met water, zeker zeewater en chloor.",
            "Warmte van een radiator of een dashboard, waardoor het uitdroogt.",
            "Parfum en alcoholhoudende reinigers, die vlekken achterlaten.",
        ]),
        ("h2", "Sluitingen"),
        ("p", "Bij leren armbanden zit de zwakke plek meestal niet in het leer maar in de sluiting. Een magneetsluiting is snel om te doen, een klemsluiting houdt beter vast bij intensief bewegen. Veel sluitingen zijn graveerbaar, zie %s." % '<a href="/cadeau/graveren/">de pagina over graveren</a>'),
        ("h2", "Onderhoud"),
        ("p", "Droog afvegen na het dragen en af en toe een klein beetje leervet of kleurloze schoencreme houdt het soepel. De volledige werkwijze staat op %s." % '<a href="/onderhoud/leer-onderhouden/">de pagina over leer onderhouden</a>'),
    ],
    parent="/materialen/",
    shops=[
        "Handgemaakte leren armbanden in dun, medium en breed leer staan bij %s: %s." % (milez(), milez("/collections/leren-heren-armbanden", "de leren armbanden van Milez Bracelets")),
    ],
)

P4 = page(
    "/materialen/natuursteen/", "Natuursteen",
    "Natuursteen: onyx, tijgeroog en turquoise - Loes Sieraden",
    "Veelgebruikte natuursteen in kralenarmbanden, met kleur, tekening, hardheid en het verschil tussen de steensoorten.",
    "Natuursteen",
    "Geen twee kralen van natuursteen zijn gelijk. Die variatie in tekening is het verschil met glas of geverfd materiaal.",
    [
        ("h2", "Veelgebruikte steensoorten"),
        ("table", ["Steen", "Kleur en tekening", "Valt op bij"], [
            ["Onyx", "Diep zwart, mat of gepolijst, egaal", "Zwart leer, zilverkleurige sluitingen"],
            ["Tijgeroog", "Goudbruin met glanzende banen", "Cognac leer, goudkleur, camel kleding"],
            ["Turquoise", "Blauwgroen met donkere adering", "Wit, denim en zomerse kleding"],
            ["Howliet", "Wit met grijze adering", "Lichte outfits, naast zilverkleur"],
            ["Lavasteen", "Mat zwart en poreus", "Combinaties met veel structuur"],
        ]),
        ("h2", "Hardheid en slijtage"),
        ("p", "Gepolijste stenen zoals onyx en tijgeroog houden hun glans lang, maar krassen bij hard contact met beton of gereedschap. Poreuze stenen zoals lavasteen nemen vocht en geur op en drogen daarna weer op."),
        ("h2", "Kraalgrootte"),
        ("p", "Kleinere kralen ogen fijner en dragen dichter tegen de pols. Grotere kralen vullen de pols sneller en werken beter als losstaand stuk dan in een stapel. Twee kralenarmbanden met dezelfde kraalgrootte naast elkaar vragen om verschil in steensoort."),
        ("h2", "Natuursteen en water"),
        ("p", "De steen zelf kan tegen water, maar het elastiek of de draad waarop de kralen zitten meestal minder. Regelmatig zwemmen met een kralenarmband verkort de levensduur van het rijgmateriaal."),
    ],
    parent="/materialen/",
    shops=[
        "Kralenarmbanden van natuursteen staan bij %s, waaronder %s en %s." % (milez("/collections/kralen-armband-heren-natuursteen", "Milez Bracelets"), milez("/collections/onyx-armband-heren", "onyx bij Milez Bracelets"), milez("/collections/tijgeroog-armband-heren", "tijgeroog bij Milez Bracelets")),
    ],
)

P5 = page(
    "/materialen/waterproof-sieraden/", "Waterproof sieraden",
    "Waterproof sieraden: wat de term betekent - Loes Sieraden",
    "Wat waterproof en zweetproof betekenen bij sieraden, welke materialen tegen chloor en zeewater kunnen en wat beter afgaat.",
    "Waterproof sieraden",
    "Waterproof betekent dat het materiaal niet aantast door water. Het zegt niets over de sluiting, de draad of het steentje dat erin zit.",
    [
        ("h2", "Waar de term over gaat"),
        ("p", "Bij roestvrij staal en titanium blijft de kleur gelijk in contact met water en zweet. Dat is de kern van de belofte. Verguld staal ligt genuanceerder: het staal eronder blijft heel, maar de laag erover slijt sneller bij dagelijks douchen met zeep en shampoo."),
        ("h2", "Zwembad, zee en sauna"),
        ("table", ["Situatie", "Aandachtspunt"], [
            ["Douchen", "Zeepresten in schakels en achter steentjes doen de glans doffen"],
            ["Chloorwater", "Belast vooral vergulde lagen en gelijmde onderdelen"],
            ["Zeewater", "Zout kruipt in de sluiting; naspoelen met kraanwater helpt"],
            ["Sauna", "Metaal wordt heet en zet uit; sieraden gaan er meestal af"],
        ]),
        ("h2", "Wat beter niet mee het water in gaat"),
        ("ul", [
            "Leren armbanden, omdat leer hard wordt na herhaald nat worden.",
            "Kralenarmbanden op elastiek, omdat het rijgmateriaal verzwakt.",
            "Sieraden met gelijmde stenen of parels.",
        ]),
        ("h2", "Na het water"),
        ("p", "Afspoelen met kraanwater en droog deppen is genoeg om zout en chloor kwijt te raken. Vocht dat achterblijft in een sluiting is de meest voorkomende oorzaak van stroef openende karabijnhaken."),
    ],
    parent="/materialen/",
    shops=[
        "Waterproof en zweetproof sieraden van roestvrij staal staan bij %s: %s." % (maeya(), maeya("/collections/waterproof-sieraden", "de waterproof collectie van Maeya Jewelry")),
    ],
)

P6 = page(
    "/materialen/nikkelallergie/", "Nikkelallergie",
    "Nikkelallergie en sieraden: geschikte materialen - Loes Sieraden",
    "Waarom sieraden jeuk of roodheid geven, hoe nikkel vrijkomt en welke materialen geschikt zijn bij een nikkelallergie.",
    "Nikkelallergie",
    "Nikkel is de bekendste oorzaak van contactallergie bij sieraden. Niet elk metaal met nikkel erin geeft klachten.",
    [
        ("h2", "Hoe klachten ontstaan"),
        ("p", "Nikkel geeft pas een reactie als het loskomt uit het metaal en in contact komt met de huid. Zweet, warmte en beschadigde huid versnellen dat proces. Roodheid, jeuk en kleine bultjes rond het contactvlak zijn de gebruikelijke signalen."),
        ("h2", "Gebonden nikkel"),
        ("p", "In sieradenstaal zit nikkel vast in de legering, waardoor er onder normale omstandigheden nauwelijks iets vrijkomt. Daarom verdragen veel mensen met een lichte gevoeligheid stalen sieraden goed, terwijl goedkopere legeringen wel klachten geven."),
        ("h2", "Materialen bij een bekende allergie"),
        ("ul", [
            "Titanium, implant grade: de veiligste keuze, ook bij verse piercings.",
            "Roestvrij staal van sieradenkwaliteit: voor de meeste mensen zonder klachten.",
            "Leer met een sluiting die de huid nauwelijks raakt.",
            "Natuursteen op elastiek, waar helemaal geen metaal aan zit.",
        ]),
        ("h2", "Klachten aan een piercing"),
        ("p", "Roodheid bij een nieuwe piercing komt vaker door genezing of door wrijving dan door allergie. Aanhoudende jeuk met vochtblaasjes wijst eerder op een allergische reactie. Bij twijfel is een huisarts of een piercingstudio het aangewezen adres, niet een sieradenwinkel."),
        ("h2", "Praktisch"),
        ("p", "Zweet vergroot de kans op klachten, dus sieraden afdoen bij intensief sporten scheelt. Een dun laagje transparante lak op een sluiting is een noodgreep die slijt en dus telkens opnieuw moet."),
    ],
    parent="/materialen/",
    shops=[
        "Titanium piercings en hypoallergene sieraden van roestvrij staal staan bij %s." % maeya(),
    ],
)

PAGES = [HUB, P1, P2, P3, P4, P5, P6]
