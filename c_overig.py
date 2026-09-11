# -*- coding: utf-8 -*-
from base import page, milez, maeya, url_milez, url_maeya, url

HOME = page(
    "/", "Home", "Loes Sieraden: sieraden combineren, maten en onderhoud",
    "Sieradeninspiratie: stijlgidsen voor stapelen en combineren, materialen van staal tot leer, maattabellen en onderhoud per materiaal.",
    "Sieraden die dagelijks gedragen worden",
    "Stijlgidsen, materialen, maattabellen en onderhoud. Geen trends, wel de dingen die bepalen of een sieraad in de la belandt of elke dag om gaat.",
    [
        ("tiles", [
            ("band", "/stijl/", "Stijl en combineren", "Armbanden stapelen, kettingen in laagjes, oorsets en ringen."),
            ("beads", "/materialen/", "Materialen", "Roestvrij staal, titanium, leer, natuursteen en waterproof."),
            ("ruler", "/maten/", "Maten", "Polsmaat, ringmaat, kettinglengtes en piercingmaten."),
            ("drop", "/onderhoud/", "Onderhoud", "Schoonmaken, bewaren, leer voeden en verkleuring voorkomen."),
            ("gift", "/cadeau/", "Cadeau", "Kiezen voor hem of haar, graveren en per gelegenheid."),
        ]),
        ("h2", "Veelgelezen"),
        ("rows", [
            ("/maten/polsmaat-meten/", "Polsmaat meten", "Meten met een touwtje en de maattabel van XS tot XL."),
            ("/stijl/armbanden-stapelen/", "Armbanden stapelen", "Breedtes van 8, 10 en 15 mm naast elkaar."),
            ("/maten/ringmaat-meten/", "Ringmaat meten", "Omtrek en diameter, en het beste moment om te meten."),
            ("/materialen/waterproof-sieraden/", "Waterproof sieraden", "Wat de term wel en niet belooft."),
            ("/onderhoud/sieraden-bewaren/", "Sieraden bewaren", "Kettingen zonder knopen en ringen zonder krassen."),
            ("/cadeau/graveren/", "Graveren", "Binnen- of buitenkant van de sluiting, en welke tekst blijft kloppen."),
        ]),
        ("h2", "Webshops die hier terugkomen"),
        ("p", "Zes Nederlandse webshops komen op deze site langs, geordend naar het zwaartepunt van het assortiment en niet naar voorkeur."),
        ("h3", "Handgemaakte armbanden"),
        ("p", "Milez Bracelets maakt herenarmbanden van leer, natuursteen en combinaties daarvan, in maten voor smalle tot brede polsen, met graveerbare sluitingen. Te vinden op " + url_milez("/") + "."),
        ("h3", "Waterproof staal en piercings"),
        ("p", "Maeya Jewelry voert sieraden van roestvrij staal en titanium piercings, met boutiques in Eindhoven en Tilburg. Te vinden op " + url_maeya("/") + "."),
        ("h3", "Breed assortiment met winkels door het land"),
        ("p", "Lucardi is een juweliersketen met ruim honderd winkels en voert sieraden, horloges, piercings en graveerbare stukken. Te vinden op " + url("https://www.lucardi.nl/") + "."),
        ("h3", "Zilver, goud en graveerwerk"),
        ("p", "Zilver.nl verkoopt sinds 1991 zilveren en gouden sieraden, horloges en zilverwerk vanuit Broek in Waterland, met graveren als aparte dienst. Te vinden op " + url("https://www.zilver.nl/") + "."),
        ("h3", "Eigen ontwerp uit Amsterdam"),
        ("p", "ANNA + NINA ontwerpt sieraden in 14 karaats goud en in zilver, en heeft naast de webshop eigen winkels in Amsterdam en Utrecht. Te vinden op " + url("https://www.anna-nina.nl/") + "."),
        ("h3", "Sieraden en horloges van bekende merken"),
        ("p", "Brandfield voert sieraden en horloges van merken als Pandora, Fossil en Swarovski, naast tassen en accessoires. Te vinden op " + url("https://www.brandfield.nl/") + "."),
        ("h2", "Waar deze site over gaat"),
        ("p", "Loes Sieraden verzamelt praktische informatie over sieraden: hoe stukken zich tot elkaar verhouden, waar materialen wel en niet tegen kunnen, en welke maat waar op uitkomt. De pagina's staan los van elkaar en zijn te lezen zonder voorkennis."),
    ],
    rail=False,
)

FAQ = page(
    "/veelgestelde-vragen/", "Vragen", "Veelgestelde vragen over sieraden - Loes Sieraden",
    "Antwoorden op veelgestelde vragen over sieraden: douchen met sieraden, maten bepalen, verkleuring, allergie en het combineren van metaalkleuren.",
    "Veelgestelde vragen",
    "De vragen die op de andere pagina's uitgebreider aan bod komen, hier kort beantwoord.",
    [
        ("faq", [
            ("Kunnen sieraden mee onder de douche?",
             "Roestvrij staal en titanium kunnen tegen water. Zeepresten blijven wel achter in schakels en sluitingen, waardoor de glans afneemt. Vergulde sieraden, leer en kralen op elastiek gaan er beter af. Meer staat op <a href=\"/materialen/waterproof-sieraden/\">de pagina over waterproof sieraden</a>."),
            ("Hoe wordt de polsmaat bepaald?",
             "Met een meetlint of een touwtje strak om de pols, ter hoogte van het polsbotje, zonder extra ruimte. De vertaling naar maten van XS tot XL staat in de tabel op <a href=\"/maten/polsmaat-meten/\">de pagina over polsmaat meten</a>."),
            ("Waarom verkleurt een goudkleurig sieraad?",
             "Bij goudkleurig staal ligt een dunne laag over het metaal. Die laag slijt door wrijving en door contact met parfum, zonnebrand en schoonmaakmiddelen. Massief staal en titanium verkleuren niet."),
            ("Welk materiaal past bij gevoelige huid?",
             "Implant grade titanium, aangeduid als G23 of ASTM F-136, geeft de minste kans op reactie en is ook bij verse piercings gebruikelijk. Roestvrij staal van sieradenkwaliteit volstaat voor de meeste mensen met een lichte nikkelgevoeligheid."),
            ("Mogen goudkleur en zilverkleur door elkaar?",
             "Ja, mits een van beide duidelijk de hoofdkleur is. Een verhouding van ongeveer drie op een oogt rustig, fiftyfifty oogt onbedoeld. Zie <a href=\"/stijl/goud-en-zilverkleur-mixen/\">goud- en zilverkleur mixen</a>."),
            ("Hoeveel armbanden passen er in een stapel?",
             "Twee tot drie banden werken op vrijwel elke pols. Meer dan drie lukt alleen met smalle modellen, anders oogt de pols korter."),
            ("Welke kettinglengte is het meest gedragen?",
             "40 tot 45 centimeter valt net onder de halskuil en past onder een kraag. Voor laagjes ligt er vier tot vijf centimeter verschil tussen de lengtes."),
            ("Welke staafdikte hebben piercings meestal?",
             "1,2 mm is gangbaar, met lengtes van 6, 8, 10 en 12 mm. Een verse piercing krijgt een langer staafje vanwege zwelling."),
            ("Hoe wordt een leren armband schoongemaakt?",
             "Droog afvegen na het dragen, en twee tot drie keer per jaar een klein beetje kleurloze leervet. Water, zeep en warmte maken leer hard."),
            ("Hoe blijft een ketting zonder knopen?",
             "Gesloten en plat opbergen, of hangend zonder dat kettingen elkaar raken. Onderweg helpt het om de ketting gestrekt te houden, bijvoorbeeld in een rietje of opgerold in een tissue."),
        ]),
    ],
    rail=False,
    faq_schema=[
        ("Kunnen sieraden mee onder de douche?", "Roestvrij staal en titanium kunnen tegen water. Zeepresten blijven wel achter in schakels en sluitingen. Vergulde sieraden, leer en kralen op elastiek gaan er beter af."),
        ("Hoe wordt de polsmaat bepaald?", "Met een meetlint of een touwtje strak om de pols, ter hoogte van het polsbotje, zonder extra ruimte in te rekenen."),
        ("Waarom verkleurt een goudkleurig sieraad?", "Bij goudkleurig staal ligt een dunne laag over het metaal die slijt door wrijving en door contact met parfum, zonnebrand en schoonmaakmiddelen."),
        ("Welk materiaal past bij gevoelige huid?", "Implant grade titanium, aangeduid als G23 of ASTM F-136, geeft de minste kans op reactie. Roestvrij staal van sieradenkwaliteit volstaat voor de meeste mensen met een lichte nikkelgevoeligheid."),
        ("Mogen goudkleur en zilverkleur door elkaar?", "Ja, mits een van beide duidelijk de hoofdkleur is. Een verhouding van ongeveer drie op een oogt rustig."),
        ("Welke staafdikte hebben piercings meestal?", "1,2 mm is gangbaar, met lengtes van 6, 8, 10 en 12 mm."),
    ],
)

CONTACT = page(
    "/contact/", "Contact", "Contact - Loes Sieraden",
    "Contactgegevens van Loes Sieraden: bereikbaar via e-mail op info@loessieraden.nl.",
    "Contact",
    "Vragen, correcties of een aanvulling op een van de artikelen zijn welkom per e-mail.",
    [
        ("p", "E-mail: <a href=\"mailto:info@loessieraden.nl\">info@loessieraden.nl</a>"),
        ("p", "Loes Sieraden is een informatieve site over sieraden. Er worden geen sieraden verkocht en er is geen klantenservice voor bestellingen. Vragen over een bestelling horen thuis bij de webshop waar die bestelling is geplaatst."),
        ("h2", "Correcties"),
        ("p", "Maattabellen en materiaalgegevens worden overgenomen van de bron waar ze vandaan komen. Klopt er iets niet meer, dan is een bericht met de betreffende pagina voldoende om het aan te passen."),
    ],
    rail=False,
)

PRIVACY = page(
    "/privacybeleid/", "Privacybeleid", "Privacybeleid - Loes Sieraden",
    "Privacybeleid van loessieraden.nl: welke gegevens verwerkt worden en welke niet.",
    "Privacybeleid",
    "Loessieraden.nl is een statische informatiesite zonder account, bestelproces of contactformulier.",
    [
        ("h2", "Gegevens die worden verwerkt"),
        ("p", "De site vraagt geen gegevens en slaat niets op in de browser. Er is geen inlog, geen nieuwsbrief en geen formulier."),
        ("h2", "E-mail"),
        ("p", "Wie een bericht stuurt naar info@loessieraden.nl, deelt daarmee een e-mailadres en de inhoud van dat bericht. Die gegevens worden alleen gebruikt om te antwoorden en verder niet bewaard dan nodig."),
        ("h2", "Serverlogs"),
        ("p", "De hostingpartij houdt technische logbestanden bij, zoals opgevraagde adressen en tijdstippen. Die gegevens dienen om de site beschikbaar te houden en worden niet gebruikt om bezoekers te volgen."),
        ("h2", "Links naar andere sites"),
        ("p", "Vanuit de artikelen wordt verwezen naar webshops van derden. Op die sites geldt het privacybeleid van de betreffende partij."),
        ("h2", "Inzage en verwijdering"),
        ("p", "Een verzoek om inzage of verwijdering van e-mailcorrespondentie kan gestuurd worden naar info@loessieraden.nl."),
    ],
    rail=False,
)

COOKIES = page(
    "/cookiebeleid/", "Cookiebeleid", "Cookiebeleid - Loes Sieraden",
    "Cookiebeleid van loessieraden.nl: de site plaatst geen cookies en gebruikt geen trackingscripts.",
    "Cookiebeleid",
    "Loessieraden.nl plaatst zelf geen cookies en laadt geen trackingscripts.",
    [
        ("h2", "Geen cookies"),
        ("p", "De pagina's bestaan uit tekst en opmaak. Er wordt geen analysesoftware geladen, geen advertentienetwerk aangeroepen en geen socialmediaknop ingebouwd. Daardoor is er geen toestemmingsvenster nodig."),
        ("h2", "Technische opslag"),
        ("p", "De hostingpartij kan technische gegevens verwerken die nodig zijn om de site te tonen, zoals het IP-adres in een serverlog. Dat is geen cookie en wordt niet gebruikt voor profilering."),
        ("h2", "Externe links"),
        ("p", "Zodra een link naar een webshop gevolgd wordt, gelden daar de cookies en instellingen van die site. Dat staat los van loessieraden.nl."),
    ],
    rail=False,
)

PAGES = [FAQ, CONTACT, PRIVACY, COOKIES]
