# -*- coding: utf-8 -*-
from base import page, milez, maeya

HUB = page(
    "/cadeau/", "Cadeau", "Sieraden cadeau geven: gidsen per ontvanger - Loes Sieraden",
    "Cadeaugidsen voor sieraden: keuzes voor hem en voor haar, graveren als persoonlijke toevoeging en passende stukken per gelegenheid.",
    "Sieraden cadeau geven",
    "Een sieraad als cadeau valt of staat bij twee dingen: het past, en het sluit aan bij wat de ontvanger al draagt.",
    [
        ("p", "Kijken naar wat iemand dagelijks draagt, levert meer op dan raden naar smaak. Metaalkleur, breedte en het aantal stukken zeggen genoeg om een veilige keuze te maken."),
        ("rows", [
            ("/cadeau/cadeau-voor-hem/", "Cadeau voor hem", "Armbanden, materialen en maten die bij mannen het meest gedragen worden."),
            ("/cadeau/cadeau-voor-haar/", "Cadeau voor haar", "Kettingen, oorbellen en ringen kiezen zonder de maat te kennen."),
            ("/cadeau/graveren/", "Graveren", "Wat er graveerbaar is en welke teksten in de praktijk passen."),
            ("/cadeau/gelegenheden/", "Per gelegenheid", "Verjaardag, jubileum, geslaagd, vaderdag en een blijvende herinnering."),
        ]),
    ],
    rail=False,
)

P1 = page(
    "/cadeau/cadeau-voor-hem/", "Cadeau voor hem",
    "Sieraad cadeau voor hem: armbanden en materialen - Loes Sieraden",
    "Een sieraad uitkiezen voor een man: welke breedte leer, welke steensoort, hoe de maat te achterhalen en welke stukken veilig zijn.",
    "Cadeau voor hem",
    "Bij herensieraden is de keuze overzichtelijk: leer, kralen of een combinatie, in drie breedtes en een handvol kleuren.",
    [
        ("h2", "Kijken naar wat er al gedragen wordt"),
        ("p", "Iemand die niets draagt, begint zelden bij een brede band. Iemand met een horloge en een armband draagt er makkelijk een derde bij. De bestaande metaalkleur van horloge of trouwring is het beste vertrekpunt voor de sluiting."),
        ("h2", "Veilige keuzes"),
        ("ul", [
            "Zwart leer met een zilverkleurige of zwarte sluiting: past bij vrijwel alles.",
            "Onyx in een kleinere kraalmaat: rustig en donker, valt niet op als sieraad.",
            "Cognac of bruin leer bij wie warme kleuren draagt.",
            "Een set van twee armbanden, waardoor het combineren al gedaan is.",
        ]),
        ("h2", "Maat achterhalen"),
        ("p", "Een bestaande armband platleggen en de binnenkant meten geeft de maat zonder vragen te stellen. Lukt dat niet, dan is de gemiddelde polsmaat een redelijke gok, met de kanttekening dat ruilen makkelijker is dan gokken. De maattabel staat op %s." % '<a href="/maten/polsmaat-meten/">de pagina over polsmaat meten</a>'),
        ("h2", "Wat vaak misgaat"),
        ("ul", [
            "Een te brede band voor iemand die nog nooit een armband droeg.",
            "Felle kleuren die niet bij de garderobe passen.",
            "Een gravure met een tekst die alleen leuk is voor de gever.",
        ]),
        ("h2", "Voor jongens"),
        ("p", "Voor kinderen en tieners bestaan smallere maten met dezelfde materialen. Een korte lengte en een lichte sluiting dragen prettiger bij een dunne pols."),
    ],
    parent="/cadeau/",
    shops=[
        "Handgemaakte herenarmbanden staan bij %s, inclusief %s en %s." % (milez(), milez("/collections/armbanden-set-heren", "sets bij Milez Bracelets"), milez("/collections/jongens-armband", "jongensarmbanden bij Milez Bracelets")),
    ],
)

P2 = page(
    "/cadeau/cadeau-voor-haar/", "Cadeau voor haar",
    "Cadeau voor haar: kettingen, oorbellen en ringen - Loes Sieraden",
    "Een sieraad kiezen voor haar zonder de maat te kennen: kettinglengtes, oorbellen die altijd passen en het risico van ringmaten.",
    "Cadeau voor haar",
    "Kettingen en oorbellen zijn maatvrij, ringen niet. Dat verschil bepaalt in de praktijk de veiligste keuze.",
    [
        ("h2", "Maatvrij en maatgevoelig"),
        ("table", ["Sieraad", "Risico op de verkeerde maat"], [
            ["Oorbellen en oorstekers", "Geen"],
            ["Ear cuffs", "Geen, ze klemmen om de rand"],
            ["Ketting", "Klein, zeker met verlengketting"],
            ["Armband", "Middelmatig, elastiek of verstelbaar helpt"],
            ["Ring", "Groot, meten is nodig"],
        ]),
        ("h2", "Metaalkleur eerst"),
        ("p", "Wie altijd zilverkleur draagt, draagt goudkleur zelden. Een blik op wat er dagelijks in blijft, geeft die informatie zonder te vragen. Bij twijfel is een stuk waarin beide kleuren voorkomen de tussenweg."),
        ("h2", "Aansluiten bij een bestaande set"),
        ("p", "Iemand met een opgebouwde oorset heeft eerder behoefte aan een aanvulling dan aan iets nieuws in een andere stijl. Een fijne hoop of een kleine stud past in vrijwel elke set. De opbouw van een oorset staat op %s." % '<a href="/stijl/oorbellen-combineren/">de pagina over oorbellen combineren</a>'),
        ("h2", "Materiaal bij gevoelige oren"),
        ("p", "Voor oren die snel reageren, is titanium of roestvrij staal de aangewezen keuze. Achtergrond staat op %s." % '<a href="/materialen/nikkelallergie/">de pagina over nikkelallergie</a>'),
        ("h2", "Praktisch bij een cadeau"),
        ("p", "Een sieraad dat tegen water kan, wordt vaker gedragen dan een stuk dat telkens af moet. Voor wie sport, zwemt of in de zorg werkt, is dat het belangrijkste criterium."),
    ],
    parent="/cadeau/",
    shops=[
        "Kettingen, oorbellen en ringen staan bij %s, met een apart overzicht op %s." % (maeya(), maeya("/collections/gift-shop", "de cadeaupagina van Maeya Jewelry")),
    ],
)

P3 = page(
    "/cadeau/graveren/", "Graveren",
    "Sieraden graveren: wat kan en welke tekst past - Loes Sieraden",
    "Graveren van armbandsluitingen en hangers: binnen- of buitenkant, aantal tekens, en teksten die na jaren nog kloppen.",
    "Graveren",
    "Een gravure maakt een sieraad persoonlijk zonder dat het aan de buitenkant hoeft op te vallen.",
    [
        ("h2", "Wat er graveerbaar is"),
        ("p", "Bij leren armbanden is het metalen slot de plek waar gegraveerd wordt. Dat kan aan de buitenkant, zichtbaar voor iedereen, of aan de binnenkant, alleen zichtbaar voor de drager. Bij medium en brede leren armbanden is daar ruimte voor; bij heel smalle banden is het slot vaak te klein."),
        ("h2", "Binnen of buiten"),
        ("ul", [
            "Binnenkant: persoonlijk, blijft privé, slijt langzamer omdat het beschermd ligt.",
            "Buitenkant: zichtbaar, geschikt voor initialen of een datum.",
        ]),
        ("h2", "Tekst kiezen"),
        ("p", "Ruimte is beperkt, meestal een enkele regel. Wat na jaren nog klopt: initialen, een datum, een naam, coordinaten van een plek. Wat sneller gedateerd raakt: een grap of een verwijzing naar een moment dat vervaagt."),
        ("h2", "Leesbaarheid"),
        ("p", "Kleine letters op een gebogen sluiting worden ondieper gegraveerd dan op een vlak plaatje. Korte teksten blijven daardoor langer leesbaar dan een volle regel in een klein lettertype."),
        ("h2", "Bij een cadeau"),
        ("p", "Een gravure maakt ruilen onmogelijk. Wie twijfelt over maat of model, kiest eerst het juiste sieraad en laat de gravure eventueel later doen."),
    ],
    parent="/cadeau/",
    shops=[
        "Graveerbare sluitingen op leren armbanden en sets staan bij %s: %s." % (milez(), milez("/pages/heren-armband-leer-graveren", "de graveerpagina van Milez Bracelets")),
    ],
)

P4 = page(
    "/cadeau/gelegenheden/", "Per gelegenheid",
    "Sieraden per gelegenheid kiezen - Loes Sieraden",
    "Welk sieraad past bij welke gelegenheid: verjaardag, geslaagd, jubileum, vaderdag en een blijvende herinnering aan een dierbare.",
    "Per gelegenheid",
    "De gelegenheid bepaalt vooral hoe persoonlijk een sieraad mag zijn, en of een gravure op zijn plaats is.",
    [
        ("h2", "Verjaardag"),
        ("p", "Ruimte voor smaak en kleur. Een stuk dat aansluit bij wat iemand al draagt, wordt het vaakst gedragen. Een set met twee armbanden geeft direct een combinatie."),
        ("h2", "Geslaagd of nieuwe baan"),
        ("p", "Een rustig, dagelijks draagbaar stuk past hier beter dan iets opvallends: het gaat mee naar werk of studie. Materiaal dat tegen water en zweet kan, verlengt de levensduur."),
        ("h2", "Jubileum of relatie"),
        ("p", "Hier komt een gravure het meest tot zijn recht: een datum aan de binnenkant van een sluiting. Twee stukken in dezelfde stijl, ieder met een eigen tekst, is een variant die vaak gekozen wordt. Zie %s." % '<a href="/cadeau/graveren/">de pagina over graveren</a>'),
        ("h2", "Vaderdag"),
        ("p", "Leer en natuursteen zijn de meest gedragen materialen bij mannen die verder weinig sieraden dragen. Een smalle band valt het minst op en wordt daardoor het vaakst dagelijks omgedaan."),
        ("h2", "Herinnering aan een dierbare"),
        ("p", "Er bestaan armbanden waarin een kleine hoeveelheid as of een lok haar bewaard kan worden, afgesloten in een metalen element. Voor wie iets tastbaars wil houden, is dat een blijvende vorm."),
        ("h2", "Naamsieraden"),
        ("p", "Een naam op een sieraad maakt het onmiskenbaar persoonlijk, maar beperkt het draagmoment. Als de ontvanger normaal alleen rustige stukken draagt, valt een naamsieraad vaak buiten die routine."),
    ],
    parent="/cadeau/",
    shops=[
        "Persoonlijke armbanden staan bij %s: %s en %s." % (milez(), milez("/collections/mannen-armband-met-naam", "naamarmbanden bij Milez Bracelets"), milez("/collections/asarmbanden-voor-een-dierbare-herinnering", "asarmbanden bij Milez Bracelets")),
        "Sieraden als cadeau staan ook bij %s." % maeya("/collections/gift-shop", "Maeya Jewelry"),
    ],
)

PAGES = [HUB, P1, P2, P3, P4]
