import json



x=[{
		"Date": "23.07",
		"pays": "Abkhazie",
		"evenement": "Indépendance autoproclamée vis-à-vis de la République de Géorgie (1992)"
	},
	{
		"Date": "19.08",
		"pays": "Afghanistan",
		"evenement": "Jour de l'indépendance (1919)."
	},
	{
		"Date": "27.04",
		"pays": "Afrique du Sud",
		"evenement": "Première élection démocratique en 1994."
	},
	{
		"Date": "28.11",
		"pays": "Albanie",
		"evenement": "Indépendance face à l'Empire ottoman en 1912."
	},
	{
	    "pays": "Algérie",
		"Date": "01.11",
		"evenement": "Début de la guerre d’indépendance en 1954"
	},
	{
		"Date": "05.07",
		"pays": "Algérie",
		"evenement": "Indépendance du pays en 1962."
	},
	{
		"Date": "03.10",
		"pays": "Allemagne",
		"evenement": "Anniversaire de la Réunification (Wiedervereinigung) de l'Allemagne en 1990."
	},

	{
		"Date": "08.09",
		"pays": "Andorre",
		"evenement": "Fête de Notre Dame de Meritxell"
	},
	{
		"Date": "11.11",
		"pays": "Angola",
		"evenement": "Jour de l'indépendance vis-à-vis du Portugal (1975)."
	},
	{
		"Date": "01.11",
		"pays": "Antigua-et-Barbuda",
		"evenement": "Indépendance (1981)."
	},
	{
		"Date": "23.09",
		"pays": "Arabie saoudite",
		"evenement": "Unification du royaume (1932)."
	},
	{
		"Date": "09.07",
		"pays": "Argentine",
		"evenement": "Indépendance de l'Espagne en (1816)."
	},
	{
		"Date": "21.09",
		"pays": "Arménie",
		"evenement": "Jour de l'indépendance (1991)"
	},
	{
		"Date": "18.03",
		"pays": "Aruba",
		"evenement": "« Jour du drapeau » : accord pour l'auto-détermination avec les pays-Bas en 1948."
	},
	{
		"Date": "26.01",
		"pays": "Australie",
		"evenement": "Australia Day : Débarquement des premiers colons britanniques en 1788."
	},
	{
		"Date": "26.10",
		"pays": "Autriche",
		"evenement": "Nationalfeiertag : Adoption de la loi constitutionnelle pour la Neutralité autrichienne en 1955."
	},
	{
		"Date": "28.05",
		"pays": "Azerbaïdjan",
		"evenement": "Proclamation de l'indépendance vis-à-vis de la République démocratique fédérative de Transcaucasie en 1918."
	},
	{
		"Date": "10.07",
		"pays": "Bahamas",
		"evenement": "Indépendance du Royaume-Uni en 1973."
	},
	{
		"Date": "16.12",
		"pays": "Bahreïn",
		"evenement": "Intronisation de l'émir Issa ben Salmane Al Khalifa en 1961."
	},
	{
		"Date": "26.03",
		"pays": "Bangladesh",
		"evenement": "Proclamation de l'indépendance du Pakistan en 1971."
	},
	{
		"Date": "30.11",
		"pays": "Barbade",
		"evenement": "Indépendance du Royaume-Uni en 1966."
	},
	{
		"Date": "21.07",
		"pays": "Belgique",
		"evenement": "Fête nationale : Prestation de serment du roi Léopold Ier en 1831."
	},
	{
		"Date": "21.09",
		"pays": "Belize",
		"evenement": "Indépendance déclarée du Royaume-Uni en 1981."
	},
	{
		"Date": "01.08",
		"pays": "Bénin",
		"evenement": "Anniversaire de l'indépendance en 1960 (anciennement français)."
	},
	{
		"Date": "24.05",
		"pays": "Bermudes",
		"evenement": "Initialement Anniversaire de la Reine Victoria ; aujourd'hui « Fête des Bermudes » pour célébrer la culture et le patrimoine des îles."
	},
	{
		"Date": "17.12",
		"pays": "Bhoutan",
		"evenement": "Prise du pouvoir par Ugyen Wangchuk premier roi héréditaire en 1907."
	},
	{
		"Date": "03.07",
		"pays": "Biélorussie",
		"evenement": "Date de la libération de Minsk par l'Armée rouge en 1944."
	},
	{
		"Date": "04.01",
		"pays": "Birmanie",
		"evenement": "Anniversaire de l'indépendance en 1948."
	},
	{
		"Date": "06.08",
		"pays": "Bolivie",
		"evenement": "Indépendance de l'Espagne en 1825."
	},
	{
		"Date": "21.11",
		"pays": "Bosnie-Herzégovine",
		"evenement": ""
	},
	{
		"Date": "30.09",
		"pays": "Botswana",
		"evenement": ""
	},
	{
		"Date": "07.09",
		"pays": "Brésil",
		"evenement": "Indépendance proclamée du Portugal en 1822"
	},
	{
		"Date": "23.02",
		"pays": "Brunei",
		"evenement": ""
	},
	{
		"Date": "03.03",
		"pays": "Bulgarie",
		"evenement": "Libération de la domination ottomane."
	},
	{
		"Date": "11.12",
		"pays": "Burkina Faso",
		"evenement": ""
	},
	{
		"Date": "01.07",
		"pays": "Burundi",
		"evenement": "Indépendance de la Belgique (1962)."
	},
	{
		"Date": "09.11",
		"pays": "Cambodge",
		"evenement": "Fête de l'indépendance vis-à-vis de la France (9 novembre 1953)"
	},
	{
		"Date": "20.05",
		"pays": "Cameroun",
		"evenement": "Référendum sur la fin du système fédéral le 20 mai 1972. Mais le pays a eu son indépendance le 1 janvier 1960. Sa devise: « Paix-Travail-Patrie »."
	},
	{
		"Date": "01.07",
		"pays": "Canada",
		"evenement": "Canada Day : Anniversaire de la confédération en 1867."
	},
	{
		"Date": "1 lundi de juillet",
		"pays": "Îles Caïmans",
		"evenement": ""
	},
	{
		"Date": "05.07",
		"pays": "Cap-Vert",
		"evenement": "Anniversaire de l'indépendance en 1975 (anciennement portugais)."
	},
	{
		"Date": "01.12",
		"pays": "République centrafricaine",
		"evenement": ""
	},
	{
		"Date": "18.09",
		"pays": "Chili",
		"evenement": "Indépendance de l'Espagne en 1818"
	},
	{
		"Date": "01.10",
		"pays": "Chine",
		"evenement": "Proclamation de la République populaire de Chine"
	},
    {
		"Date": "02.10",
		"pays": "Chine",
		"evenement": "Proclamation de la République populaire de Chine"
	},
	{
		"Date": "01.10",
		"pays": "Chypre",
		"evenement": ""
	},
	{
		"Date": "20.07",
		"pays": "Colombie",
		"evenement": "Anniversaire de l'indépendance de l'Espagne en 1810"
	},
	{
		"Date": "06.07",
		"pays": "Comores",
		"evenement": "Anniversaire de l'indépendance en 1975 (anciennement français)."
	},
	{
		"Date": "30.06",
		"pays": "République démocratique du Congo",
		"evenement": "Accession à l'indépendance de la Belgique en 1960."
	},
	{
		"Date": "15.08",
		"pays": "République du Congo",
		"evenement": "Accession à l'indépendance de la France en 1960."
	},
	{
		"Date": "04.08",
		"pays": "Îles Cook",
		"evenement": "Fête de la Constitution de 1965."
	},
	{
		"Date": "09.09",
		"pays": "Corée du Nord",
		"evenement": "Proclamation de la République Populaire Démocratique de Corée en 1948."
	},
	{
		"Date": "15.08",
		"pays": "Corée du Sud",
		"evenement": "Annonce de la capitulation du Japon en 1945 qui signifie pour la Corée la fin des 35 années de colonisation par le Japon. Le 15 août 1948 marque également l'établissement de la République de Corée."
	},
	{
		"Date": "15.09",
		"pays": "Costa Rica",
		"evenement": "Déclaration d'indépendance de l'Espagne en 1821."
	},
	{
		"Date": "07.08",
		"pays": "Côte d'Ivoire",
		"evenement": "Fête de l'indépendance"
	},
	{
		"Date": "25.06",
		"pays": "Croatie",
		"evenement": ""
	},
	{
		"Date": "10.12",
		"pays": "Cuba",
		"evenement": "Indépendance de l'Espagne en 1898."
	},
	{
		"Date": "05.06",
        "pays": "Danemark",
		"evenement": "Constitution de 1849"
	},
	{
		"Date": "16.04",
		"pays": "Danemark",
		"evenement": "Anniversaire de la Reine Margrethe II."
	},
	{
		"Date": "27.06",
		"pays": "Djibouti",
		"evenement": "Anniversaire de l'indépendance vis à vis de la France en 1977."
	},
	{
		"Date": "27.02",
		"pays": "République dominicaine",
		"evenement": "Indépendance de l'Espagne en 1865 suite à la guerre de restauration dominicaine"
	},
	{
		"Date": "03.11",
		"pays": "Dominique",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "23.07",
		"pays": "Égypte",
		"evenement": "Révolution de 1952."
	},
	{
		"Date": "02.12",
		"pays": "Émirats arabes unis",
		"evenement": ""
	},
	{
		"Date": "10.08",
		"pays": "Équateur",
		"evenement": "Indépendance de l'Espagne en 1825"
	},
	{
		"Date": "24.05",
		"pays": "Érythrée",
		"evenement": ""
	},
	{
		"Date": "12.10",
		"pays": "Espagne",
		"evenement": "Jour de l'hispanité ; célèbre la redécouverte de l'Amérique en 1492 pour les Espagnols."
	},
	{
		"Date": "24.02",
		"pays": "Estonie",
		"evenement": "Jour de l'Indépendance (1918)"
	},
	{
		"Date": "04.07",
		"pays": "États-Unis",
		"evenement": "Déclaration d'indépendance de 1776 ; célébrée sous le nom d'Independence Day (Fête de l'Indépendance)."
	},
	{
		"Date": "21.07",
		"pays": "Guam",
		"evenement": "« Liberation Day » (Fête de la libération), commémore le début de la Bataille de Guam."
	},
	{
		"Date": "28.05",
		"pays": "Éthiopie",
		"evenement": "Jour de la chute du Derg en 1991."
	},
	{
		"Date": "10.10",
		"pays": "Fidji",
		"evenement": "Fête de l’Indépendance"
	},
	{
		"Date": "06.12",
		"pays": "Finlande",
		"evenement": "Déclaration d'indépendance finlandaise de 1917."
	},
	{
		"Date": "14.07",
		"pays": "France",
		"evenement": "Fête nationale : Prise de la Bastille (1789) et Fête de la Fédération (1790). Le Sénat vota cette date comme fête nationale par une loi du 6 juillet 1880"
	},
	{
		"Date": "17.08",
		"pays": "Gabon",
		"evenement": "Anniversaire de l'indépendance vis-à-vis de la France en 1960."
	},
	{
		"Date": "18.02",
		"pays": "Gambie",
		"evenement": "Fête de l'indépendance."
	},
	{
		"Date": "26.05",
		"pays": "Géorgie",
		"evenement": "Restauration de l'indépendance vis-à-vis de la République démocratique fédérative de Transcaucasie et proclamation de la République démocratique de Géorgie en 1918."
	},
	{
		"Date": "06.03",
		"pays": "Ghana",
		"evenement": "Déclaration d'indépendance en 1957."
	},
	{
		"Date": "10.09",
		"pays": "Gibraltar",
		"evenement": "Référendum sur l'autodétermination en 1967."
	},
	{
		"Date": "25.03",
		"pays": "Grèce",
		"evenement": "Insurrection de 1821 contre la domination ottomane"
	},
	{
		"Date": "28.10",
		"pays": "Grèce",
		"evenement": "Jour du Non."
	},
	{
		"Date": "07.02",
		"pays": "Grenade",
		"evenement": ""
	},
	{
		"Date": "15.09",
		"pays": "Guatemala",
		"evenement": "Indépendance de l'Espagne en 1821."
	},
	{
		"Date": "02.10",
		"pays": "Guinée",
		"evenement": ""
	},
	{
		"Date": "24.09",
		"pays": "Guinée-Bissau",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "12.10",
		"pays": "Guinée équatoriale",
		"evenement": "Indépendance de l'Espagne en 1968."
	},
	{
		"Date": "23.02",
		"pays": "Guyana",
		"evenement": ""
	},
	{
		"Date": "18.05",
		"pays": "Haïti",
		"evenement": "Création du drapeau nationale par Catherine Flon en 1803"
	},
	{
		"Date": "15.09",
		"pays": "Honduras",
		"evenement": "Déclaration d'indépendance vis-à-vis de l'Espagne en 1821."
	},
	{
		"Date": "15.03",
		"pays": "Hongrie",
		"evenement": "Commémoration de la révolution hongrois de 1848 contre la domination des Habsbourg."
	},
	{
		"Date": "20.08",
		"pays": "Hongrie",
		"evenement": "Commémoration de la révolution hongrois de 1848 contre la domination des Habsbourg."
	},
	{
		"Date": "23.10",
		"pays": "Hongrie",
		"evenement": "Fête de saint Étienne, ce jour célèbre la fondation de l'État hongrois en 1000."
	},
	{
	    "Date": "23.10",
		"pays": "Hongrie",
		"evenement": "Anniversaire de la révolution de 1956 contre le régime communiste."
	},
	{
		"Date": "26.01",
		"pays": "Inde",
		"evenement": "Jour de l'Indépendance en 1947."
	},
	{
		"Date": "15.08",
		"pays": "Inde",
		"evenement": "Proclamation de la république en 1950."
	},
	{
		"Date": "17.08",
		"pays": "Indonésie",
		"evenement": "Proclamation de l'indépendance vis-à-vis des pays-Bas en 1945"
	},

	{
		"Date": "11.02",
		"pays": "Iran",
		"evenement": "Proclamation de la république islamique d'Iran"
	},
	{
		"Date": "17.03",
		"pays": "Irlande",
		"evenement": "Fête de la Saint-Patrick"
	},
	{
		"Date": "17.06",
		"pays": "Islande",
		"evenement": "Proclamation de la république en 1944."
	},
	{
		"Date": "02.06",
		"pays": "Italie",
		"evenement": "Abolition de la Monarchie et proclamation de la République en 1946"
	},
	{
		"Date": "25.04",
		"pays": "Italie",
		"evenement":  "Fête de la libération."
	},

	{
		"Date": "06.08",
		"pays": "Jamaïque",
		"evenement": "Jour de l'indépendance."
	},
	{
		"Date": "23.02",
	    "pays": "Japon",
		"evenement": "Tenno Tanjobi ou Anniversaire de l'Empereur en place"
	},
	{
		"Date": "11.02",
		"pays": "Japon",
		"evenement": "Fête de la Fondation (660 av. J.-C.)."
	},
	{
		"Date": "25.05",
		"pays": "Jordanie",
		"evenement": "date de l'indépendance en 1946"
	},
	{
		"Date": "16.12",
		"pays": "Kazakhstan",
		"evenement": "Date de l'indépendance"
	},
	{
		"Date": "12.12",
		"pays": "Kenya",
		"evenement": "Jamhuri Day : Jour de l'indépendance en 1963."
	},
	{
		"Date": "31.08",
		"pays": "Kirghizistan",
		"evenement": ""
	},
	{
		"Date": "12.07",
		"pays": "Kiribati",
		"evenement": "Anniversaire de l'indépendance vis-à-vis du Royaume-Uni en 1979."
	},
	{
		"Date": "17.02",
		"pays": "Kosovo",
		"evenement": "l'indépendance"
	},
	{
		"Date": "02.12",
		"pays": "Laos",
		"evenement": "Proclamation de la République populaire."
	},
	{
		"Date": "04.10",
		"pays": "Lesotho",
		"evenement": "Jour de l'indépendance."
	},
	{
		"Date": "18.11",
		"pays": "Lettonie",
		"evenement": "Jour de l'Indépendance (1918)"
	},
	{
		"Date": "22.11",
		"pays": "Liban",
		"evenement": "Indépendance en 1943."
	},
	{
		"Date": "26.07",
		"pays": "Liberia",
		"evenement": "Proclamation de la République en 1847."
	},
	{
		"Date": "17.02",
		"pays": "Libye",
		"evenement": "la révolution libyen en 2011"
	},
	{
		"Date": "15.08",
		"pays": "Liechtenstein",
		"evenement": ""
	},
	{
		"Date": "16.02",
		"pays": "Lituanie",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "23.06",
		"pays": "Luxembourg",
		"evenement": "Célébration publique de l'anniversaire du Souverain."
	},
	{
		"Date": "02.08",
		"pays": "Macédoine du Nord",
		"evenement": "Jour Uprising (1903)"
	},
	{
		"Date": "08.09",
		"pays": "Macédoine du Nord",
		"evenement": "Indépendance."
	},
	{
		"Date": "26.06",
		"pays": "Madagascar",
		"evenement": "Déclaration d'indépendance de la France en 1960."
	},
	{
		"Date": "31.08",
		"pays": "Malaisie",
		"evenement": ""
	},
	{
		"Date": "06.07",
		"pays": "Malawi",
		"evenement": "Jour de l'Indépendance (Jour de République) en 1964."
	},
	{
		"Date": "26.07",
		"pays": "Maldives",
		"evenement": ""
	},
	{
		"Date": "22.09",
		"pays": "Mali",
		"evenement": "Proclamation de la République."
	},
	{
		"Date": "21.09",
		"pays": "Malte",
		"evenement": ""
	},
	{
		"Date": "05.07",
		"pays": " Île de Man",
		"evenement": "Solstice d'été dans le calendrier julien"
	},
	{
		"Date": "18.11",
		"pays": "Maroc",
		"evenement": "Anniversaire de l'indépendance"
	},
	{
		"Date": "30.07",
		"pays": "Maroc",
		"evenement": "Fête du Trône."
	},
	{
		"Date": "01.05",
		"pays": "Îles Marshall",
		"evenement": "Fête de la Constitution de 1979."
	},
	{
		"Date": "12.03",
		"pays": "Maurice",
		"evenement": "Accession à l'indépendance en 1968."
	},
	{
		"Date": "28.11",
		"pays": "Mauritanie",
		"evenement": "Proclamation de l'indépendance en 1960."
	},
	{
		"Date": "16.09",
		"pays": "Mexique",
		"evenement": "Grito de Dolores (Appel à la sédition en faveur de Ferdinand VII contre les autorités de la Nouvelle-Espagne (1810) favorables à Joseph Bonaparte"
	},
	{
		"Date": "03.11",
		"pays": "États fédérés de Micronésie",
		"evenement": "Fête de l'indépendance vis-à-vis de la tutelle US en 1979."
	},
	{
		"Date": "27.08",
		"pays": "Moldavie",
		"evenement": "Anniversaire de l'indépendance (1991)"
	},
	{
		"Date": "19.11",
		"pays": "Monaco",
		"evenement": "Fête du Prince."
	},
	{
		"Date": "11.07",
		"pays": "Mongolie",
		"evenement": "Naadam : Fête de la révolution et de l'indépendance-1921"
	},
	{
		"Date": "13.07",
		"pays": "Monténégro",
		"evenement": ""
	},
	{
		"Date": "25.06",
		"pays": "Mozambique",
		"evenement": ""
	},
	{
		"Date": "21.03",
		"pays": "Namibie",
		"evenement": ""
	},
	{
		"Date": "31.01",
		"pays": "Nauru",
		"evenement": "Jour de l'indépendance (1968)."
	},
	{
		"Date": "07.07",
		"pays": "Népal",
		"evenement": "Anniversaire de la naissance de Sa Majesté le Roi"
	},
	{
		"Date": "15.09",
		"pays": "Nicaragua",
		"evenement": "Déclaration d'indépendance de l'Espagne en 1821."
	},
	{
		"Date": "18.12",
		"pays": "Niger",
		"evenement": "Proclamation de la République"
	},
	{
		"Date": "01.10",
		"pays": "Nigeria",
		"evenement": ""
	},
	{
		"Date": "19.10",
		"pays": "Niue",
		"evenement": "Indépendance vis-à-vis de la Nouvelle-Zélande en 1974"
	},
	{
		"Date": "17.05",
		"pays": "Norvège",
		"evenement": "Fête de la Constitution (1814)."
	},
	{
		"Date": "06.02",
		"pays": "Nouvelle-Zélande",
		"evenement": "Waitangi Day : commémoration du traité de Waitangi en 1840 entre les Maori et la Couronne britannique."
	},
	{
		"Date": "18.11",
		"pays": "Oman",
		"evenement": ""
	},
	{
		"Date": "20.09",
		"pays": " Ossétie du Sud",
		"evenement": "Indépendance autoproclamée vis-à-vis de la République de Géorgie (1990)"
	},
	{
		"Date": "09.10",
		"pays": "Ouganda",
		"evenement": ""
	},
	{
		"Date": "01.09",
		"pays": "Ouzbékistan",
		"evenement": "Date de l'indépendance (1991)"
	},
	{
		"Date": "23.03",
		"pays": "Pakistan",
		"evenement": "Proclamation de la République islamique en 1956"
	},
	{
		"Date": "15.11",
		"pays": "Palestine",
		"evenement": "Proclamation d'indépendance de 1988."
	},
	{
		"Date": "09.07",
		"pays": "Palaos",
		"evenement": "Fête de la constitution (1969)"
	},
	{
		"Date": "28.11",
		"pays": "Panama",
		"evenement": "Indépendance de l'Empire espagnol en 1821"
	},
	{
		"Date": "16.09",
		"pays": "Papouasie-Nouvelle-Guinée",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "15.05",
		"pays": "Paraguay",
		"evenement": "Indépendance de l'Espagne en (1811)."
	},
	{
		"Date": "27.04",
		"pays": "pays-Bas",
		"evenement": "Fête du Roi (si la fête tombe un dimanche"
	},
	{
		"Date": "28.07",
		"pays": "Pérou",
		"evenement": "Déclaration d'indépendance vis-à-vis de l'Espagne en 1821."
	},
	{
		"Date": "12.06",
		"pays": "Philippines",
		"evenement": "Déclaration d'indépendance de l'Espagne en 1898."
	},
	{
		"Date": "03.05",
		"pays": "Pologne",
		"evenement": "Proclamation de la Constitution polonaise du 3 mai 1791"
	},
	{
		"Date": "11.11",
		"pays": "Pologne",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "10.06",
		"pays": "Portugal",
		"evenement": "Célébration de la mort du poète Luis de Camões (1580)."
	},
	{
		"Date": "01.12",
		"pays": "Portugal",
		"evenement": "Restauration de l'indépendance nationale vis-à-vis de l'Espagne en 1640."
	},
	{
		"Date": "25.07",
		"pays": "Porto Rico",
		"evenement": "Célébration de la Constitution de 1952."
	},
	{
		"Date": "18.12",
		"pays": "Qatar",
		"evenement": "Accession au trône de la famille Al Thani"
	},
	{
		"Date": "01.12",
		"pays": "Roumanie",
		"evenement": "Célébration de la Grande Union de 1918."
	},
	{
		"Date": "12.06",
		"pays": "Russie",
		"evenement": "Anniversaire de l'indépendance vis-à-vis de l'Union soviétique (1991)"
	},
	{
		"Date": "01.07",
		"pays": "Rwanda",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "19.09",
		"pays": "Saint-Christophe-et-Niévès",
		"evenement": "Anniversaire de l'indépendance 1963."
	},
	{
		"Date": "03.09",
		"pays": "Saint-Marin",
		"evenement": ""
	},
	{
		"Date": "22.02",
		"pays": "Sainte-Lucie",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "27.10",
		"pays": " Saint-Vincent-et-les-Grenadines",
		"evenement": "Anniversaire de l'indépendance 1979."
	},
	{
		"Date": "07.07",
		"pays": "Salomon",
		"evenement": ""
	},
	{
		"Date": "15.09",
		"pays": "Salvador",
		"evenement": "Déclaration d'indépendance de l'Espagne en 1821."
	},
	{
		"Date": "01.06",
		"pays": "Samoa",
		"evenement": "Célébration de l'indépendance."
	},
	{
		"Date": "12.07",
		"pays": "Sao Tomé-et-Principe",
		"evenement": ""
	},
	{
		"Date": "04.04",
		"pays": "Sénégal",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "15.02",
		"pays": "Serbie",
		"evenement": "commémoration du premier soulèvement serbe."
	},
	{
		"Date": "18.06",
		"pays": "Seychelles",
		"evenement": ""
	},
	{
		"Date": "27.04",
		"pays": "Sierra Leone",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "09.08",
		"pays": "Singapour",
		"evenement": ""
	},
	{
		"Date": "01.09",
		"pays": "Slovaquie",
		"evenement": "Jour de la constitution."
	},
	{
		"Date": "25.06",
		"pays": "Slovénie",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "01.07",
		"pays": "Somalie",
		"evenement": ""
	},
	{
		"Date": "01.01",
		"pays": "Soudan",
		"evenement": ""
	},
	{
		"Date": "09.07",
		"pays": "Soudan du Sud",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "04.02",
		"pays": "Sri Lanka",
		"evenement": "Anniversaire de l'indépendance en 1948."
	},
	{
		"Date": "06.06",
		"pays": "Suède",
		"evenement": "Sacre de Gustav Vasa en 1523. Constitution de 1809."
	},
	{
		"Date": "01.08",
		"pays": "Suisse",
		"evenement": "Signature du Pacte fédéral au début aout 1291"
	},
	{
		"Date": "25.11",
		"pays": "Suriname",
		"evenement": "Accession à l'indépendance des pays-Bas en 1975."
	},
	{
		"Date": "06.09",
		"pays": "Eswatini",
		"evenement": ""
	},
	{
		"Date": "17.04",
		"pays": "Syrie",
		"evenement": ""
	},
	{
		"Date": "09.09",
		"pays": "Tadjikistan",
		"evenement": "Fête de l'indépendance vis-à-vis de l'URSS en 1991"
	},
	{
		"Date": "10.10",
		"pays": " Taïwan",
		"evenement": "Anniversaire du renversement de l'Empire 10 octobre 1911."
	},
	{
		"Date": "26.04",
		"pays": "Tanzanie",
		"evenement": ""
	},
	{
		"Date": "11.08",
		"pays": "Tchad",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "28.10",
		"pays": "République tchèque",
		"evenement": "Indépendance vis-à-vis de l'Autriche-Hongrie en 1918."
	},
	{
		"Date": "28.07",
		"pays": "Thaïlande",
		"evenement": "Anniversaire du roi Rama X."
	},
	{
		"Date": "20.05",
		"pays": "Timor oriental",
		"evenement": "Indépendance vis-à-vis de l'Indonésie en 2002."
	},
	{
		"Date": "27.04",
		"pays": "Togo",
		"evenement": "Déclaration d'indépendance en 1957."
	},
	{
		"Date": "04.06",
		"pays": "Tonga",
		"evenement": "Fête de l'émancipation"
	},
	{
		"Date": "31.08",
		"pays": "Trinité-et-Tobago",
		"evenement": ""
	},
	{
		"Date": "25.07",
		"pays": "Tunisie",
		"evenement": "Fête de la République."
	},
	{
		"Date": "20.03",
		"pays": "Tunisie",
		"evenement": "Jour de l'indépendance (1956)."
	},
	{
		"Date": "27.10",
		"pays": "Turkménistan",
		"evenement": "Fête de l'indépendance vis-à-vis de l'URSS en 1991"
	},
	{
		"Date": "29.10",
		"pays": "Turquie",
		"evenement": "Fondation de la république en 1923."
	},
	{
		"Date": "01.10",
		"pays": "Tuvalu",
		"evenement": "Fête de l'indépendance vis-à-vis des Kiribati (îles Gilbert) en 1975 et du Royaume-Uni en 1978."
	},
	{
		"Date": "24.08",
		"pays": "Ukraine",
		"evenement": "Jour de la déclaration d'indépendance en 1991"
	},
	{
		"Date": "25.08",
		"pays": "Uruguay",
		"evenement": "Proclamation d'indépendance de l'Espagne en 1823"
	},
	{
		"Date": "30.07",
		"pays": "Vanuatu",
		"evenement": "Anniversaire de l'indépendance."
	},
	{
		"Date": "19.03",
		"pays": " Vatican",
		"evenement": "Anniversaire de la messe d'inauguration du pape : sous François"
	},
	{
		"Date": "05.07",
		"pays": "Venezuela",
		"evenement": "Déclaration d'indépendance de l'Espagne en 1811."
	},
	{
		"Date": "02.09",
		"pays": "Viêt Nam",
		"evenement": "Indépendance de la France en 1945"
	},
	{
		"Date": "22.05",
		"pays": "Yémen",
		"evenement": ""
	},
	{
		"Date": "24.10",
		"pays": "Zambie",
		"evenement": "Indépendance vis-à-vis du Royaume-Uni en 1964."
	},
	{
		"Date": "18.04",
		"pays": "Zimbabwe",
		"evenement": "Anniversaire de l'indépendance."
	}

]

dico={}
for data in x:
    if data["Date"] in dico:
        dico[data["Date"]]["fetes_nationales"].append([data["pays"],data["evenement"],data["pays"]])
    else:
        dico[data["Date"]]={"fetes_nationales":[[data["pays"],data["evenement"],data["pays"]]]}
with open("liste_pays.json", "w") as f:
    json.dump(dico,f,indent=2)
