# -*- coding: utf-8 -*-
from base import page, milez, maeya

HUB = page(
    "/stijl/", "Stijl", "Sieraden combineren: stijlgidsen - Loes Sieraden",
    "Stijlgidsen over armbanden stapelen, kettingen in laagjes dragen, oorbellen combineren en sieraden afstemmen op een outfit.",
    "Stijl en combineren",
    "Zeven gidsen over het combineren van sieraden: van een stapel armbanden tot een set oorbellen die als geheel klopt.",
    [
        ("p", "Combineren draait om drie dingen: verhouding, herhaling en rust. Verhouding gaat over de breedte en het gewicht van de stukken naast elkaar. Herhaling zorgt dat een combinatie samenhangt, bijvoorbeeld door een metaalkleur of een steensoort terug te laten komen. Rust betekent dat er ergens ruimte overblijft, zodat het oog een startpunt heeft."),
        ("rows", [
            ("/stijl/armbanden-stapelen/", "Armbanden stapelen", "Breedtes, materialen en aantallen die naast elkaar werken op een pols."),
            ("/stijl/kettingen-laagjes/", "Kettingen in laagjes", "Lengteverschil, hangers en het voorkomen van verstrengelde schakels."),
            ("/stijl/oorbellen-combineren/", "Oorbellen combineren", "Een oorset opbouwen met studs, hoops en ear cuffs."),
            ("/stijl/ringen-combineren/", "Ringen combineren", "Stapelringen, zegelringen en de verdeling over beide handen."),
            ("/stijl/goud-en-zilverkleur-mixen/", "Goud- en zilverkleur mixen", "Hoe twee metaalkleuren samen rustig blijven ogen."),
            ("/stijl/minimalistisch-of-statement/", "Minimalistisch of statement", "Wanneer een fijn sieraad werkt en wanneer een opvallend stuk."),
            ("/stijl/sieraden-bij-outfit/", "Sieraden bij een outfit", "Halslijn, mouwlengte en kleur als vertrekpunt."),
        ]),
    ],
    rail=False,
)

P1 = page(
    "/stijl/armbanden-stapelen/", "Armbanden stapelen",
    "Armbanden stapelen: breedtes en materialen - Loes Sieraden",
    "Hoe een stapel armbanden opgebouwd wordt: breedtes van 8 tot 15 mm, leer met kralen combineren, aantal banden en de volgorde op de pols.",
    "Armbanden stapelen",
    "Een stapel armbanden valt of staat bij verschil. Verschil in breedte, in materiaal of in structuur, met een lijn die alles verbindt.",
    [
        ("h2", "Begin met een ankerband"),
        ("p", "De ankerband is het breedste of zwaarste stuk in de stapel. Meestal is dat een brede leren band of een armband met grotere kralen. Alle andere banden worden daaromheen gekozen. Zonder anker wordt een stapel snel een verzameling losse dingen zonder middelpunt."),
        ("p", "Een tweede band mag daar dicht tegenaan liggen, een derde geeft de stapel breedte. Vier of meer banden werken vooral bij smalle modellen, anders wordt de pols visueel korter."),
        ("h2", "Breedtes die naast elkaar werken"),
        ("p", "Leren armbanden zijn er grofweg in drie breedtes en die verhouden zich goed tot elkaar."),
        ("table", ["Breedte", "Karakter", "Combineert met"], [
            ["8 mm", "Fijn en onopvallend", "Twee of drie stuks samen, of naast een kralenarmband"],
            ["10 mm", "Middenmaat, dagelijks", "Een tweede band in dezelfde kleur of een kralenband"],
            ["15 mm", "Nadrukkelijk aanwezig", "Hooguit een fijne band ernaast, verder ruimte laten"],
        ]),
        ("p", "Twee banden van precies dezelfde breedte naast elkaar geven een strak, bijna uniform beeld. Een verschil van een paar millimeter oogt losser en minder bedacht."),
        ("h2", "Leer en kralen mengen"),
        ("p", "Leer is glad en strak, kralen zijn rond en onregelmatig. Die twee texturen naast elkaar geven diepte zonder dat er een kleur bij hoeft. Er bestaan ook armbanden waarin beide materialen in een stuk zitten, wat de overgang tussen de banden vanzelf maakt."),
        ("ul", [
            "Leer met leer: rustig, vraagt om verschil in breedte of kleur.",
            "Leer met natuursteen: het meest gebruikte contrast, werkt in vrijwel elke kleurcombinatie.",
            "Kralen met kralen: alleen boeiend bij verschil in steensoort of kraalgrootte.",
        ]),
        ("h2", "Kleur en metaal in de stapel"),
        ("p", "Een stapel wordt rustig zodra een kleur twee keer terugkomt. Een zwarte leren band naast zwarte onyxkralen bijvoorbeeld, of cognac leer met een bruin gevlamde steen. De metaalkleur van de sluitingen telt daarin mee: zilverkleurige sluitingen naast een zwarte sluiting vallen op zodra de mouw omhoog gaat."),
        ("h2", "Volgorde op de pols"),
        ("p", "Het zwaarste stuk ligt het prettigst het dichtst bij de hand, de fijnste band het hoogst op de pols. Een horloge telt als een breed element; wie een horloge draagt, houdt de stapel meestal aan de andere pols of beperkt zich tot twee smalle banden ernaast."),
        ("h2", "Wat een stapel meestal verstoort"),
        ("ul", [
            "Vier of meer brede banden op een smalle pols.",
            "Drie verschillende metaalkleuren in een stapel.",
            "Banden die allemaal even lang zijn maar verschillend zitten, waardoor de sluitingen boven op elkaar komen.",
            "Een stapel die zo strak zit dat er geen beweging in zit; een armband hoort een klein stukje te kunnen schuiven.",
        ]),
    ],
    parent="/stijl/",
    shops=[
        "Handgemaakte leren armbanden en kralenarmbanden voor heren staan bij %s, waaronder de %s met leer en kralen in een stuk." % (milez(), milez("/collections/fusion-combinatie-armbanden-van-leer-en-kralen", "Fusion-serie van Milez Bracelets")),
        "Voor de basis van een stapel is er de %s." % milez("/collections/essentials", "Essentials-lijn van Milez Bracelets"),
    ],
)

P2 = page(
    "/stijl/kettingen-laagjes/", "Kettingen in laagjes",
    "Kettingen in laagjes dragen: lengtes en hangers - Loes Sieraden",
    "Kettingen combineren met verschil in lengte, keuze van hangers en schakels, en het voorkomen van verstrengeling.",
    "Kettingen in laagjes",
    "Twee of drie kettingen samen werken pas als de lengtes ver genoeg uit elkaar liggen en de schakels elkaar met rust laten.",
    [
        ("h2", "Verschil in lengte"),
        ("p", "Vier tot vijf centimeter verschil is het minimum om twee kettingen als aparte laagjes te laten lezen. Bij minder verschil kruisen ze elkaar en ontstaat er een rommelig midden. Een korte ketting rond de hals, een middenlaag op sleutelbeenhoogte en een langere hanger daaronder is de klassieke opbouw."),
        ("h2", "Een hanger per laag"),
        ("p", "Twee hangers naast elkaar vechten om aandacht en tikken hoorbaar tegen elkaar. De rustigste combinatie is een gladde schakel zonder hanger, met daaronder een ketting met een klein bedeltje of steentje."),
        ("h2", "Schakels die niet in elkaar haken"),
        ("ul", [
            "Fijne slangenketting met een grovere schakel: haakt vrijwel nooit.",
            "Twee fijne kettingen van gelijke dikte: de kans op verstrengeling is het grootst.",
            "Parelketting of kralenketting naast een gladde schakel: blijft goed uit elkaar.",
        ]),
        ("h2", "Halslijn als vertrekpunt"),
        ("table", ["Halslijn", "Werkt goed met"], [
            ["Ronde hals", "Korte ketting boven de rand, plus een langere hanger op het textiel"],
            ["V-hals", "Een hanger die eindigt boven het diepste punt van de V"],
            ["Coltrui", "Een lange ketting over de stof, of juist alleen oorbellen"],
            ["Blouse met kraag", "Korte ketting binnen de kraag, verder niets"],
        ]),
        ("h2", "Slijtage voorkomen"),
        ("p", "Kettingen die tegen elkaar schuren, slijten sneller bij de sluiting. Twee stukken die veel samen gedragen worden, kunnen het beste ook samen bewaard worden, ieder in een eigen vakje of zakje. Meer daarover staat op de pagina over %s." % '<a href="/onderhoud/sieraden-bewaren/">sieraden bewaren</a>'),
    ],
    parent="/stijl/",
    shops=[
        "Waterproof kettingen van roestvrij staal staan bij %s, te vinden via %s." % (maeya(), maeya("/collections/kettingen", "de kettingcollectie van Maeya Jewelry")),
    ],
)

P3 = page(
    "/stijl/oorbellen-combineren/", "Oorbellen combineren",
    "Oorbellen combineren tot een oorset - Loes Sieraden",
    "Een oorset opbouwen met studs, hoops, ear cuffs en piercings: aantal, hoogte, metaalkleur en symmetrie tussen beide oren.",
    "Oorbellen combineren",
    "Een oorset is een compositie van meerdere kleine stukken. Niet elk gaatje hoeft gevuld, en beide oren hoeven niet gelijk te zijn.",
    [
        ("h2", "Een ankerpunt kiezen"),
        ("p", "In de meeste oorsets is er een stuk dat het zwaarst weegt: een grotere hoop of een opvallende stud in de oorlel. Wat daarboven zit, blijft kleiner. Hoe hoger in de oorschelp, hoe fijner het sieraad meestal is."),
        ("h2", "Zonder extra gaatjes"),
        ("p", "Ear cuffs klemmen om de rand van de oorschelp en vragen geen piercing. Daarmee is de hoogte van een oorset uit te breiden zonder dat er iets gezet hoeft te worden. Een cuff hoog op de rand, een stud in de lel en een kleine hoop ertussenin geeft al een volledig ogende set."),
        ("h2", "Symmetrie of juist niet"),
        ("ul", [
            "Volledig symmetrisch: rustig en formeel, past bij een strakke outfit.",
            "Een druk oor en een rustig oor: levendiger, en de kant met de meeste stukken valt op.",
            "Gespiegeld in gewicht maar niet in vorm: twee verschillende hoops van gelijke grootte bijvoorbeeld.",
        ]),
        ("h2", "Metaalkleur binnen een oor"),
        ("p", "In een klein vlak vallen twee metaalkleuren sterk op. Binnen een oor is een kleur het rustigst; verschil in vorm doet dan het werk. Wie toch mengt, houdt de kleuren gescheiden per hoogte, bijvoorbeeld alles in de lel in een kleur."),
        ("h2", "Dagelijks dragen"),
        ("p", "Oorsieraden die dag en nacht in blijven, hebben baat bij materiaal dat niet verkleurt en tegen water kan. Roestvrij staal en titanium zijn daarin de gebruikelijke keuzes; wat het verschil is, staat op %s." % '<a href="/materialen/stainless-steel/">de pagina over stainless steel</a>'),
    ],
    parent="/stijl/",
    shops=[
        "Oorbellen, hoops en ear cuffs van roestvrij staal staan bij %s: %s en %s." % (maeya(), maeya("/collections/oorbellen", "de oorbellencollectie van Maeya Jewelry"), maeya("/collections/ear-cuffs", "de ear cuffs van Maeya Jewelry")),
    ],
)

P4 = page(
    "/stijl/ringen-combineren/", "Ringen combineren",
    "Ringen combineren en stapelen - Loes Sieraden",
    "Stapelringen, zegelringen en bandjes verdelen over vingers en handen, met aandacht voor breedte, maat en metaalkleur.",
    "Ringen combineren",
    "Ringen zitten dicht bij elkaar en worden van korte afstand bekeken. Kleine verschillen in breedte en afwerking tellen daardoor zwaar.",
    [
        ("h2", "Verdelen over de hand"),
        ("p", "Een rustige verdeling houdt aan: een opvallende ring per hand, aangevuld met fijne bandjes. Twee brede ringen naast elkaar op dezelfde vinger beperken de beweging van het gewricht en ogen massief."),
        ("h2", "Stapelen op een vinger"),
        ("p", "Twee of drie smalle bandjes boven elkaar vormen samen ongeveer de breedte van een brede ring, maar blijven soepeler. De onderste ring mag de breedste zijn; die draagt het beeld. Wie stapelt, kiest de maat vaak een fractie ruimer, omdat meerdere bandjes samen strakker aanvoelen dan een enkele ring."),
        ("h2", "Zegelring als middelpunt"),
        ("p", "Een zegelring vraagt ruimte. Naast de pink of ringvinger waarop hij zit, blijven de andere vingers meestal leeg of krijgen hooguit een fijn bandje op de andere hand."),
        ("h2", "Maat blijft leidend"),
        ("p", "Vingers zetten uit in warmte en na inspanning. Een ring die 's ochtends perfect zit, kan later op de dag knellen. Het opmeten van de juiste maat en de tabel met omtrek en diameter staan op %s." % '<a href="/maten/ringmaat-meten/">de pagina over ringmaat meten</a>'),
        ("h2", "Afwerking combineren"),
        ("ul", [
            "Glad naast glad: strak en formeel.",
            "Glad naast gedraaid of gehamerd: meer beweging, minder streng.",
            "Ringen met steentjes: een per hand volstaat meestal.",
        ]),
    ],
    parent="/stijl/",
    shops=[
        "Ringen van roestvrij staal en de bijbehorende maattabel staan bij %s: %s en %s." % (maeya(), maeya("/collections/ringen", "de ringencollectie van Maeya Jewelry"), maeya("/pages/ringmaat", "de ringmaattabel van Maeya Jewelry")),
    ],
)

P5 = page(
    "/stijl/goud-en-zilverkleur-mixen/", "Goud- en zilverkleur mixen",
    "Goudkleur en zilverkleur mixen in sieraden - Loes Sieraden",
    "Twee metaalkleuren samen dragen zonder dat het onrustig wordt: verhouding, verbindende stukken en de rol van huidtint.",
    "Goud- en zilverkleur mixen",
    "Twee metaalkleuren door elkaar dragen kan prima, mits een van beide duidelijk de hoofdrol heeft.",
    [
        ("h2", "Kies een hoofdkleur"),
        ("p", "De rustigste verhouding is ongeveer drie staat tot een: drie stukken in de hoofdkleur, een in de tweede kleur. Zodra de verhouding richting fiftyfifty gaat, gaat het oog twijfelen en oogt de combinatie eerder onbedoeld dan gekozen."),
        ("h2", "Een verbindend stuk"),
        ("p", "Een sieraad waarin beide kleuren voorkomen, maakt de rest vanzelf logisch. Denk aan een ketting met een hanger in een andere kleur, of een leren armband met een zilverkleurige sluiting naast een goudkleurige ring."),
        ("h2", "Per zone werken"),
        ("p", "Een andere aanpak houdt de kleuren uit elkaar: alles rond de hals in een kleur, alles aan de handen in de andere. Aan de oren blijft dan de kleur die het dichtst bij het gezicht rustig oogt."),
        ("h2", "Huidtint en kleding"),
        ("p", "Warme huidtinten dragen goudkleur vaak makkelijker, koelere tinten zilverkleur. Dat is geen regel maar een vertrekpunt; kledingkleur weegt in de praktijk zwaarder. Bij marineblauw en grijs valt zilverkleur op, bij camel, olijf en roest komt goudkleur beter uit."),
        ("h2", "Materiaal en kleurechtheid"),
        ("p", "Verkleuring maakt een mix onbedoeld zichtbaar: een verguld laagje dat slijt, laat een andere ondertoon zien naast een stuk dat wel kleurvast is. Materialen die niet verkleuren zijn beschreven op %s." % '<a href="/materialen/">de materialenpagina</a>'),
    ],
    parent="/stijl/",
    shops=[
        "Sieraden in zilver- en goudkleur die niet verkleuren staan bij %s." % maeya("/collections/waterproof-sieraden", "Maeya Jewelry"),
    ],
)

P6 = page(
    "/stijl/minimalistisch-of-statement/", "Minimalistisch of statement",
    "Minimalistische of opvallende sieraden kiezen - Loes Sieraden",
    "Wanneer een fijn sieraad het beste werkt en wanneer een opvallend stuk, met aandacht voor gelegenheid, kleding en verhouding.",
    "Minimalistisch of statement",
    "Fijne sieraden dragen zichzelf, opvallende stukken vragen ruimte. Het verschil zit vooral in wat eromheen gebeurt.",
    [
        ("h2", "Wat een sieraad opvallend maakt"),
        ("p", "Niet alleen formaat telt. Glans, contrast met de huid, beweging en geluid maken een stuk nadrukkelijk. Een matte brede band valt minder op dan een smalle glanzende ketting die licht vangt."),
        ("h2", "Een opvallend stuk per outfit"),
        ("p", "Zodra er twee stukken om aandacht vragen, verliezen beide. De gebruikelijke oplossing: een opvallend sieraad, de rest fijn en in dezelfde metaalkleur."),
        ("h2", "Wanneer minimalistisch beter uitkomt"),
        ("ul", [
            "Bij drukke prints of veel textuur in de kleding.",
            "Op kantoor en bij formele gelegenheden.",
            "Bij werk waarbij sieraden ergens achter kunnen blijven haken.",
            "Als er al een horloge en een bril in beeld zijn.",
        ]),
        ("h2", "Wanneer een statement werkt"),
        ("ul", [
            "Bij effen kleding in een rustige kleur.",
            "Bij een hoge of gesloten hals, waar een lange hanger over de stof valt.",
            "Als de rest van de outfit bewust sober is gehouden.",
        ]),
        ("h2", "Opbouwen in de tijd"),
        ("p", "Een collectie die groeit, begint bij stukken die dagelijks passen en breidt uit met een enkel opvallend stuk. Andersom werkt zelden: opvallende stukken zonder rustige basis blijven vaak in het doosje liggen."),
    ],
    parent="/stijl/",
    shops=[
        "Fijne dagelijkse sieraden staan bij %s, stoere leren armbanden bij %s." % (maeya(), milez("/collections/stoere-heren-armband", "Milez Bracelets")),
    ],
)

P7 = page(
    "/stijl/sieraden-bij-outfit/", "Sieraden bij een outfit",
    "Sieraden afstemmen op een outfit - Loes Sieraden",
    "Sieraden kiezen op basis van halslijn, mouwlengte, kleur en gelegenheid, met voorbeelden voor dagelijkse en formele kleding.",
    "Sieraden bij een outfit",
    "De kleding bepaalt waar ruimte is. Halslijn, mouw en kleur wijzen meestal vanzelf aan welk sieraad past.",
    [
        ("h2", "Beginnen bij de halslijn"),
        ("p", "Een gesloten hals laat weinig ruimte voor een korte ketting en vraagt om lengte of om oorsieraden. Een open hals maakt juist een korte ketting mogelijk. Wie twijfelt, houdt de regel aan dat de ketting eindigt op huid en niet half op stof."),
        ("h2", "Mouwlengte en polssieraden"),
        ("p", "Bij lange mouwen komt een armband alleen in beeld als de mouw omhoog schuift; smalle banden hebben daar het minste last van. Korte mouwen laten een hele stapel zien, waardoor breedte en volgorde belangrijker worden."),
        ("h2", "Kleur van de kleding"),
        ("table", ["Kleding", "Sieraden die opvallen"], [
            ["Zwart", "Zilverkleur en heldere stenen, zoals turquoise"],
            ["Wit en ecru", "Goudkleur, cognac leer, warme natuursteen"],
            ["Denim", "Zowel zilver- als goudkleur, zwart leer met zilverkleurige sluiting"],
            ["Olijf en camel", "Goudkleur, bruin leer, tijgeroog"],
        ]),
        ("h2", "Gelegenheid"),
        ("ul", [
            "Werk: een of twee stukken, geen geluid, niets dat blijft haken.",
            "Feest: een opvallend stuk, de rest fijn en in dezelfde kleur.",
            "Sport en water: alleen materiaal dat tegen zweet en chloor kan.",
            "Reizen: stukken die dag en nacht in kunnen blijven, zodat er weinig los raakt.",
        ]),
        ("h2", "Test voor de spiegel"),
        ("p", "Alles omdoen en daarna een stuk weglaten levert vaker een beter resultaat op dan andersom. Het weggelaten stuk is meestal het element dat dubbelop deed."),
    ],
    parent="/stijl/",
    shops=[
        "Dagelijkse sieraden van roestvrij staal staan bij %s, leren en kralenarmbanden bij %s." % (maeya(), milez()),
    ],
)

PAGES = [HUB, P1, P2, P3, P4, P5, P6, P7]
