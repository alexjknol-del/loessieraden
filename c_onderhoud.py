# -*- coding: utf-8 -*-
from base import page, milez, maeya

HUB = page(
    "/onderhoud/", "Onderhoud", "Sieraden onderhouden: schoonmaken en bewaren - Loes Sieraden",
    "Praktische pagina's over sieraden schoonmaken, leer onderhouden, verkleuring voorkomen en sieraden bewaren zonder krassen.",
    "Onderhoud",
    "Sieraden gaan zelden kapot door slijtage. Ze gaan stuk in een tas, in een la of onder de douche.",
    [
        ("p", "Onderhoud is bij de meeste materialen een kwestie van lauw water, een zachte doek en droog opbergen. De uitzonderingen zitten bij leer, natuursteen en vergulde lagen."),
        ("rows", [
            ("/onderhoud/sieraden-schoonmaken/", "Sieraden schoonmaken", "Per materiaal, met wat wel en niet gebruikt kan worden."),
            ("/onderhoud/leer-onderhouden/", "Leer onderhouden", "Soepel houden, vlekken voorkomen en nat geworden leer redden."),
            ("/onderhoud/verkleuren-voorkomen/", "Verkleuren voorkomen", "Waarom een laagje slijt en welke gewoontes dat vertragen."),
            ("/onderhoud/sieraden-bewaren/", "Sieraden bewaren", "Kettingen zonder knopen, ringen zonder krassen, leer zonder vouwen."),
        ]),
    ],
    rail=False,
)

P1 = page(
    "/onderhoud/sieraden-schoonmaken/", "Sieraden schoonmaken",
    "Sieraden schoonmaken per materiaal - Loes Sieraden",
    "Schoonmaakmethodes voor roestvrij staal, titanium, vergulde sieraden, natuursteen en leer, met middelen die vermeden moeten worden.",
    "Sieraden schoonmaken",
    "Vuil op een sieraad is meestal een mengsel van huidvet, zeep en bodylotion. Lauw water met een milde zeep haalt dat weg.",
    [
        ("h2", "Basismethode"),
        ("p", "Een kom lauw water met een druppel afwasmiddel, het sieraad enkele minuten laten staan, daarna zachtjes borstelen met een zachte tandenborstel. Naspoelen met schoon water en direct droogmaken met een zachte doek. Vocht dat achterblijft in een sluiting is de meest voorkomende oorzaak van stroef sluiten."),
        ("h2", "Per materiaal"),
        ("table", ["Materiaal", "Wel", "Niet"], [
            ["Roestvrij staal", "Lauw water, milde zeep, zachte doek", "Schuurmiddel, staalwol, tandpasta"],
            ["Titanium", "Zelfde als staal", "Agressieve reinigers bij verse piercings"],
            ["Verguld", "Zacht afvegen met droge doek", "Onderdompelen, ultrasoon bad, alcohol"],
            ["Natuursteen", "Vochtige doek, daarna direct drogen", "Weken in water, zeker bij poreuze steen"],
            ["Leer", "Droge of licht vochtige doek", "Zeep, alcohol, water in de week"],
        ]),
        ("h2", "Sluitingen en schakels"),
        ("p", "In een karabijnhaak verzamelt zich zeep. Een tandenborstel komt er meestal niet bij; spoelen onder een dunne straal lauw water werkt beter. Daarna de sluiting een paar keer openen en sluiten terwijl hij nog vochtig is, zodat het vuil eruit komt."),
        ("h2", "Wat glans terugbrengt"),
        ("p", "Een doffe indruk komt vaker door een filmlaagje dan door slijtage. Poetsen met een droge microvezeldoek herstelt dat in de meeste gevallen. Blijft het dof, dan zit er meestal een kras op het oppervlak en helpt poetsen niet meer."),
        ("h2", "Hoe vaak"),
        ("p", "Sieraden die dagelijks in blijven: elke paar weken. Stukken die af en toe gedragen worden: na elke keer dragen, voordat ze weer worden opgeborgen. Zo komt huidvet niet ingedroogd terug uit de la."),
    ],
    parent="/onderhoud/",
    shops=[
        "Sieraden van roestvrij staal die dagelijks water verdragen staan bij %s." % maeya("/collections/waterproof-sieraden", "Maeya Jewelry"),
    ],
)

P2 = page(
    "/onderhoud/leer-onderhouden/", "Leer onderhouden",
    "Leren armband onderhouden - Loes Sieraden",
    "Leer soepel houden, vlekken voorkomen, en wat te doen als een leren armband nat is geworden of stug aanvoelt.",
    "Leer onderhouden",
    "Leer heeft weinig nodig, maar reageert slecht op twee dingen: water en warmte.",
    [
        ("h2", "Dagelijks"),
        ("p", "Na het dragen droog afvegen met een doek haalt zweet en huidvet weg. Dat is genoeg om de kleur gelijkmatig te houden. Leer dat continu gedragen wordt, verdonkert op de contactpunten, wat bij bruin en cognac juist gewaardeerd wordt."),
        ("h2", "Af en toe voeden"),
        ("p", "Een klein beetje kleurloze leervet of schoencreme, uitgesmeerd met een doek en daarna uitgewreven, houdt het leer soepel. Te veel vet maakt het leer donker en plakkerig, dus minder is hier beter. Twee tot drie keer per jaar volstaat voor een armband."),
        ("h2", "Nat geworden"),
        ("ul", [
            "Deppen met een droge doek, niet wrijven.",
            "Op kamertemperatuur laten drogen, uit de buurt van radiator, kachel of foehn.",
            "Pas voeden wanneer het leer weer helemaal droog is.",
        ]),
        ("p", "Snel drogen bij warmte laat leer krimpen en hard worden. Die schade is niet meer terug te draaien."),
        ("h2", "Vlekken"),
        ("p", "Parfum, zonnebrand en desinfecterende gel laten vlekken achter die in het leer trekken. Sieraden als laatste omdoen, na het aanbrengen van verzorgingsproducten, voorkomt het grootste deel daarvan."),
        ("h2", "Sluiting nakijken"),
        ("p", "Bij leren armbanden zit de slijtage meestal in de sluiting of in de overgang van leer naar metaal. Een sluiting die stroef opent of speling vertoont, is het moment om de band niet meer bij sport of zwaar werk te dragen."),
    ],
    parent="/onderhoud/",
    shops=[
        "Leren armbanden in dun, medium en breed leer staan bij %s: %s." % (milez(), milez("/collections/leren-heren-armbanden", "de leren armbanden van Milez Bracelets")),
    ],
)

P3 = page(
    "/onderhoud/verkleuren-voorkomen/", "Verkleuren voorkomen",
    "Verkleuren van sieraden voorkomen - Loes Sieraden",
    "Waarom sieraden verkleuren of dof worden, welke stoffen dat versnellen en welke gewoontes de kleur langer intact houden.",
    "Verkleuren voorkomen",
    "Verkleuring komt zelden door het metaal zelf. Meestal is het een laagje dat slijt of een filmpje dat achterblijft.",
    [
        ("h2", "Drie oorzaken"),
        ("ul", [
            "Slijtage van een dunne toplaag, vooral bij goudkleurige afwerking.",
            "Chemische aanslag door parfum, haarlak, zonnebrand of schoonmaakmiddel.",
            "Aanslag op de huid door zweet in combinatie met zeepresten.",
        ]),
        ("h2", "Volgorde van aankleden"),
        ("p", "Sieraden gaan als laatste om en als eerste af. Parfum en bodylotion krijgen daarmee de tijd om in te trekken, waardoor er niets op het metaal achterblijft."),
        ("h2", "Situaties die het snelst schade geven"),
        ("table", ["Situatie", "Wat er gebeurt"], [
            ["Schoonmaken met chloor", "Tast vergulde lagen en gelijmde delen aan"],
            ["Zwembad", "Chloorwater dringt in schakels en sluitingen"],
            ["Sporten", "Zweet in combinatie met wrijving slijt het oppervlak"],
            ["Slapen met sieraden om", "Wrijving tegen beddengoed, haakschade aan schakels"],
        ]),
        ("h2", "Materiaalkeuze scheelt het meest"),
        ("p", "Massief roestvrij staal en titanium verkleuren niet, ongeacht de gewoontes van de drager. Bij vergulde stukken bepaalt de dikte van de laag de levensduur. Het verschil is uitgewerkt op %s." % '<a href="/materialen/stainless-steel/">de pagina over roestvrij staal</a>'),
    ],
    parent="/onderhoud/",
    shops=[
        "Kleurvaste sieraden van roestvrij staal en titanium staan bij %s." % maeya(),
    ],
)

P4 = page(
    "/onderhoud/sieraden-bewaren/", "Sieraden bewaren",
    "Sieraden bewaren zonder knopen en krassen - Loes Sieraden",
    "Kettingen zonder knopen opbergen, ringen beschermen tegen krassen en leer bewaren zonder vouwen, thuis en onderweg.",
    "Sieraden bewaren",
    "De meeste schade ontstaat buiten het dragen om: in een tasje waarin alles door elkaar ligt.",
    [
        ("h2", "Kettingen"),
        ("p", "Een ketting knoopt zichzelf zodra hij kan bewegen. Dicht doen voor het opbergen en plat neerleggen voorkomt dat. Hangen aan een haakje werkt ook, mits de kettingen elkaar niet raken. Voor onderweg: de ketting door een rietje of door een tissue rollen houdt hem gestrekt."),
        ("h2", "Ringen en armbanden"),
        ("p", "Metaal krast metaal. Ringen die los in een doosje liggen, geven elkaar binnen een paar weken lichte krassen. Aparte vakjes of zachte zakjes lossen dat op. Kralenarmbanden op elastiek liggen het beste plat, niet strak opgerold, omdat elastiek anders onder spanning blijft staan."),
        ("h2", "Leer"),
        ("p", "Leren armbanden bewaren in de vorm waarin ze gedragen worden, dus rond en niet plat gevouwen. Een vouw in leer blijft zichtbaar. Droog bewaren en niet in een afgesloten plastic zakje, omdat leer moet kunnen ademen."),
        ("h2", "Vochtigheid en licht"),
        ("ul", [
            "Badkamer is de slechtste bewaarplek: warm en vochtig.",
            "Direct zonlicht verbleekt gekleurd leer en sommige stenen.",
            "Een lade in een slaapkamer is in de praktijk de beste plek.",
        ]),
        ("h2", "Onderweg"),
        ("p", "Een klein etui met vakjes weegt niets en voorkomt dat oorbellen los in een toilettas belanden. Piercingsieraden die gewisseld worden, gaan het veiligst in een apart doosje, omdat losse staafjes en balletjes klein zijn en makkelijk verdwijnen."),
    ],
    parent="/onderhoud/",
    shops=[
        "Armbanden en sieraden uit dit artikel staan bij %s en %s." % (milez(), maeya()),
    ],
)

PAGES = [HUB, P1, P2, P3, P4]
