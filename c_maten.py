# -*- coding: utf-8 -*-
from base import page, milez, maeya

HUB = page(
    "/maten/", "Maten", "Sieradenmaten: pols, ring, ketting en piercing - Loes Sieraden",
    "Maattabellen en meetinstructies voor armbanden, ringen, kettinglengtes en piercingstaafjes.",
    "Maten",
    "De helft van de sieraden die niet gedragen worden, zit simpelweg niet goed. Vier korte meetinstructies met tabellen.",
    [
        ("p", "Meten kost een minuut en voorkomt een retourzending. Voor elk type sieraad geldt een eigen methode; een polsomtrek is bijvoorbeeld niet hetzelfde als een armbandmaat."),
        ("rows", [
            ("/maten/polsmaat-meten/", "Polsmaat meten", "Meten met meetlint of touwtje, plus de maattabel van XS tot XL."),
            ("/maten/ringmaat-meten/", "Ringmaat meten", "Omtrek en diameter per maat, en het beste moment van de dag om te meten."),
            ("/maten/kettinglengtes/", "Kettinglengtes", "Welke lengte waar op het lichaam uitkomt, van choker tot lange hanger."),
            ("/maten/piercingmaten/", "Piercingmaten", "Staafdikte en lengte bij oor-, neus- en navelpiercings."),
        ]),
    ],
    rail=False,
)

P1 = page(
    "/maten/polsmaat-meten/", "Polsmaat meten",
    "Polsmaat meten voor een armband - Loes Sieraden",
    "De polsomtrek opmeten met een meetlint of een touwtje, en de vertaling naar armbandmaten van XS tot XL.",
    "Polsmaat meten",
    "Een armband hoort te kunnen schuiven zonder van de hand te vallen. Dat begint bij een strak opgemeten polsomtrek.",
    [
        ("h2", "Meten met meetlint"),
        ("p", "Het meetlint gaat strak om de pols, ter hoogte van het polsbotje. Geen extra ruimte inrekenen: die zit al in de maatvoering van de armband verwerkt. Een meetlint dat los om de pols hangt, geeft al snel een centimeter te veel."),
        ("h2", "Meten zonder meetlint"),
        ("p", "Een touwtje of een reep papier om de pols leggen, het punt markeren waar het rondje sluit, en dat daarna langs een liniaal leggen. Deze methode werkt net zo nauwkeurig, mits het touwtje echt strak zit."),
        ("h2", "Van polsomtrek naar armbandmaat"),
        ("table", ["Polsomtrek", "Maat", "Type pols"], [
            ["16,5 tot 17 cm", "XS", "Smalle polsomtrek"],
            ["17,5 tot 18 cm", "S", "Smalle polsomtrek"],
            ["18,5 tot 19 cm", "M", "Gemiddelde polsomtrek"],
            ["19,5 tot 20 cm", "L", "Brede polsomtrek"],
            ["20,5 tot 21 cm", "XL", "Brede polsomtrek"],
        ]),
        ("note", "De tabel hierboven volgt de maatvoering van %s. Andere merken hanteren soms een andere indeling, dus de maat van een bestaande armband is geen garantie bij een ander merk." % milez("/pages/polsomtrek-man", "Milez Bracelets")),
        ("h2", "Strak of ruim dragen"),
        ("p", "Kralenarmbanden op elastiek zitten het prettigst wanneer ze net iets kunnen bewegen. Leren armbanden met een sluiting mogen strakker, omdat ze niet over de hand hoeven. Wie meerdere banden stapelt, telt de dikte van de andere banden mee: een stapel voelt strakker dan een enkele armband van dezelfde maat."),
        ("h2", "Meten voor een cadeau"),
        ("p", "Zonder de pols te kunnen meten, is een bestaande armband van de ontvanger het beste referentiepunt: plat neerleggen en de binnenkant meten. Lukt dat niet, dan zijn maten met een instelbare of elastische sluiting de veiligste keuze. Meer daarover staat op %s." % '<a href="/cadeau/">de cadeaupagina</a>'),
    ],
    parent="/maten/",
    shops=[
        "Handgemaakte armbanden op maat, van smalle tot brede polsen, staan bij %s: %s en %s." % (milez(), milez("/collections/heren-armband-smalle-pols", "smalle polsmaten bij Milez Bracelets"), milez("/collections/heren-armband-brede-pols", "brede polsmaten bij Milez Bracelets")),
    ],
)

P2 = page(
    "/maten/ringmaat-meten/", "Ringmaat meten",
    "Ringmaat meten: tabel met omtrek en diameter - Loes Sieraden",
    "De juiste ringmaat bepalen met een bestaande ring of een strookje papier, inclusief tabel met omtrek en diameter in millimeters.",
    "Ringmaat meten",
    "Ringmaten lopen in kleine stappen. Een halve maat verschil is het verschil tussen dagelijks dragen en in de la laten liggen.",
    [
        ("h2", "Twee manieren"),
        ("p", "Met een bestaande ring: de binnendiameter meten met een liniaal, van rand tot rand door het midden. Zonder ring: een strookje papier strak om de vinger leggen, het snijpunt markeren en de lengte meten. Die lengte is de omtrek."),
        ("h2", "Tabel"),
        ("table", ["Ringmaat (EU)", "Omtrek (mm)", "Diameter (mm)"], [
            ["15", "49", "16"],
            ["16", "52", "16,5"],
            ["17", "54", "17"],
            ["18", "57", "18"],
            ["19", "59", "19"],
        ]),
        ("note", "Deze waarden komen uit de ringmaattabel van %s." % maeya("/pages/ringmaat", "Maeya Jewelry")),
        ("h2", "Moment van meten"),
        ("p", "Vingers zijn 's ochtends het smalst en aan het eind van de dag het breedst. Warmte, zout eten en inspanning laten ze uitzetten. Meten aan het eind van de middag geeft daarom de bruikbaarste maat."),
        ("h2", "Knokkel groter dan de vinger"),
        ("p", "Als de knokkel duidelijk breder is dan de basis van de vinger, telt de knokkel: de ring moet daar overheen kunnen. Een bredere ring vraagt bovendien een fractie meer ruimte dan een smal bandje in dezelfde maat."),
        ("h2", "Stapelen"),
        ("p", "Twee of drie ringen boven elkaar drukken samen meer op de vinger dan een enkele ring. Wie stapelt, kiest de bovenste ringen soms een halve maat ruimer. Combinaties staan op %s." % '<a href="/stijl/ringen-combineren/">de pagina over ringen combineren</a>'),
    ],
    parent="/maten/",
    shops=[
        "Ringen van roestvrij staal staan bij %s: %s." % (maeya(), maeya("/collections/ringen", "de ringencollectie van Maeya Jewelry")),
    ],
)

P3 = page(
    "/maten/kettinglengtes/", "Kettinglengtes",
    "Kettinglengtes: welke lengte valt waar - Loes Sieraden",
    "Overzicht van kettinglengtes in centimeters en waar ze op het lichaam uitkomen, met tips voor laagjes en halslijnen.",
    "Kettinglengtes",
    "Dezelfde ketting valt bij iedereen net iets anders. De lengtes hieronder zijn een vertrekpunt, geen wet.",
    [
        ("h2", "Lengtes en waar ze uitkomen"),
        ("table", ["Lengte", "Valt ongeveer", "Past bij"], [
            ["36 tot 40 cm", "Strak om de hals, choker", "Open halslijnen, zomerse kleding"],
            ["40 tot 45 cm", "Net onder de halskuil", "De meest gedragen lengte, past onder een kraag"],
            ["45 tot 50 cm", "Op het sleutelbeen tot iets daaronder", "Hangers, laagje onder een korte ketting"],
            ["50 tot 60 cm", "Op de borst", "Over een trui of blouse, met een grotere hanger"],
            ["70 cm en langer", "Ter hoogte van het middenrif", "Lange lijn, ook dubbel te dragen"],
        ]),
        ("h2", "Laagjes uitrekenen"),
        ("p", "Vier tot vijf centimeter verschil per laag houdt de kettingen uit elkaar. Drie kettingen van 40, 45 en 50 centimeter vormen daarmee een klassieke set. De opbouw staat verder uitgewerkt op %s." % '<a href="/stijl/kettingen-laagjes/">de pagina over kettingen in laagjes</a>'),
        ("h2", "Halsomtrek meebrekenen"),
        ("p", "Bij een bredere halsomtrek valt elke ketting hoger dan de tabel aangeeft. Een centimeter of drie extra lengte herstelt dat verschil. Wie twijfelt, meet met een touwtje op de plek waar de ketting moet vallen."),
        ("h2", "Verstelbare sluitingen"),
        ("p", "Een verlengketting van enkele centimeters maakt een ketting geschikt voor meerdere halslijnen en is bij een cadeau de veiligste keuze."),
    ],
    parent="/maten/",
    shops=[
        "Kettingen in verschillende lengtes staan bij %s: %s." % (maeya(), maeya("/collections/kettingen", "de kettingcollectie van Maeya Jewelry")),
    ],
)

P4 = page(
    "/maten/piercingmaten/", "Piercingmaten",
    "Piercingmaten: staafdikte en lengte per piercing - Loes Sieraden",
    "Gangbare maten voor piercingsieraden: staafdikte van 1,2 mm en lengtes van 6 tot 12 mm, per plek op het lichaam.",
    "Piercingmaten",
    "Een piercingsieraad heeft twee maten die tellen: de dikte van het staafje en de lengte ervan.",
    [
        ("h2", "Staafdikte"),
        ("p", "1,2 mm is de gangbare dikte voor de meeste oorpiercings, neuspiercings en navelpiercings. Een dunner staafje past niet strak in een bestaand kanaal en kan het gaatje laten inscheuren; een dikker staafje past er simpelweg niet in zonder oprekken."),
        ("h2", "Lengte"),
        ("table", ["Lengte", "Gebruik"], [
            ["6 mm", "Standaard voor een genezen oorpiercing"],
            ["8 mm", "Dikker weefsel of lichte zwelling"],
            ["10 mm", "Kraakbeen en piercings die net gezet zijn"],
            ["12 mm", "Navelpiercings en dikkere doorgangen"],
        ]),
        ("note", "Bij een verse piercing wordt bewust een langer staafje geplaatst, zodat er ruimte is voor zwelling. Zodra de zwelling weg is, gaat het sieraad meestal terug naar een kortere lengte."),
        ("h2", "Materiaal bij een nieuwe piercing"),
        ("p", "Implant grade titanium, aangeduid als G23 of ASTM F-136, is de standaard voor verse piercings vanwege de biocompatibiliteit. Achtergrond staat op %s." % '<a href="/materialen/titanium/">de pagina over titanium</a>'),
        ("h2", "Zelf wisselen of laten doen"),
        ("p", "Een genezen piercing is eenvoudig zelf te wisselen met schone handen. Bij een piercing die net gezet is, gebeurt dat in de studio waar hij gezet is. Genezing verloopt per plek anders: een oorlel gaat sneller dan kraakbeen."),
    ],
    parent="/maten/",
    shops=[
        "Titanium piercings in de maten hierboven staan bij %s: %s en %s." % (maeya(), maeya("/collections/navelpiercings", "navelpiercings bij Maeya Jewelry"), maeya("/collections/neuspiercings", "neuspiercings bij Maeya Jewelry")),
    ],
)

PAGES = [HUB, P1, P2, P3, P4]
