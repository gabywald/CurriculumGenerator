# CurriculumGenerator

Pour générer des CV ("Curriculum Vitae") en LaTeX (et les traiter pour obtenir un PDF correspondant) ; utilisation de différents langages de programmation, idéalement des langages de script comme Python ou Perl. Cette idée afin de permettre de générer facilement un (ou plusieurs) CV, obtenir un bon exemple à réutiliser et tester sur les plate-formes de recrutement et / ou les processus de recrutement. 

Évolutions possibles : voir section dédiée !

## Objectifs et questions

L'idée originelle étant de montrer la preuve de concept de CV de tests utilisables via les plate-formes de recrutement comme LinkedIn et / ou Monster (et beaucoup d'autres) avec des CV normalisés / standardisés. 

Utile tant professionnellement pour réfléchir à bien construire son CV, qu'en "Job Testing" (pour travailler sur les discriminations à l'embauche ?) ou construction de StoryTelling (construction d'une "légende" ?) avec un historique contextualisé sous forme de biographie éventuelle. En d'autres termes : un outil qui permet de revoir le CV sous sa forme classique, mais généré à outrance via des outils informatiques dédiés. 

Également en complément, une idée de tester le comportement des recruteurs, notamment des "cabinets de conseils" et "sociétés de services", qui souvent ne connaissent pas le domaine des profils recherchés et font des recherches de CV et profils uniquement par mots-clefs. 

Questionnement sur les faux comptes (notamment sur LinkedIn), utilisés par des escrocs : https://blogbuster.fr/social/linkedin-faux-profil.htm (déjà constaté personnellement : faux recruteurs, collecte de données personnelles, usurpation d'identité...) dont ce n'est pas l'objectif ici !

En réponse également aux recruteurs qui font des bases de données de candidats potentiels, notamment les sociétés de services (SSII / SS2I / ESN en France) ; et qui, notamment, proposent souvent des CV plus avantageux à leurs propsects et clients potentiels, souvent au-delà de la réalité et du possible !

__L'idée de base étant de réfléchir à ce qui fait un "bon CV"__ : 
  * Intitulé(s) ; 
  * Compétences ; 
  * Expériences / Parcours ; 
  * Contexte de mission ou de projet ; 
  * La 'véritable' personne derrière : Motivation, Localisation, Histoire...
  
__Si d'autres développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

## Licence

Licence : GPLv3

## Biais possibles

### Représentation et connaissances des recruteurs sur les "candidats"

Geek / Nerd / "techniques" ... et autres clichés classqiues et canoniques !

Termes abscons et faciles à confondre :  ...

Que signifient tout ces acronymes et termes abscons ? 
 - RHEL (Red Hat Enterprise Linux), un système d'exploitation (ce qui fait fonctionner un ordinateur en plus de l'électricité) ; 
 - Java / JavaScript : deux langages de programmations bien différents !
 - Shell / PowerShell : deux langages de scripts (un type de programmation), l'un pour linux et l'autre pour windows ; 

...

### Recherches via ces plate-formes

Compétences et métiers plus demandés que d'autres (notamment en informatique), effets de modes. 
Recherches uniquement par mots-clefs. 

Définition d'une typologie de poste recherché en fonction du CV ou de combinaisons de mots-clefs de compétences et d'années d'expériences. 

Arborescence de compétences ?

### Typologie des recruteurs

  * "Client final" (recrutement direct en contrat à terme, CDD, ou à long terme, CDI) ; 
  * "Chasseur de tête" (sous-traitance RH) ; 
  * "Sociétés de services" (intérim, prestation, conseil, forfait / régie, ESN / SSII : sous-traitance RH, encadrement et limitation des coût, "prêt" de main-d'oeuvre...) ; 

Sur le sujet des SSII / ESN en informatique, un peu de lecture (et débat sur l'externalisation / sous-traitance et le fait que de nombreux "profils" partent plutôt en freelance / autoentrepreneurs aux environs de 2020) : 
  * https://fr.wikipedia.org/wiki/Entreprise_de_services_du_numérique
  * https://www.journaldunet.com/solutions/reseau-social-d-entreprise/1486816-esn-la-fin-d-un-modele/
  * https://medium.com/@Vitolae/a-quoi-servent-encore-les-ssii-7514b25bf7f4
  * https://www.reddit.com/r/france/comments/llfno2/une_ssii_pardon_une_esn_parmi_dautres/
  * https://forum.canardpc.com/threads/105700-La-perception-des-ESN-%28SSII%29-%28avec-de-vrai-bouts-de-ressentiment-dedans%29
  * https://forum.compagnons-devops.fr/t/les-esn-ex-ssii/1090
  * https://www.developpez.net/forums/d1793122/emploi-etudes-informatique/emploi/difference-entre-esn-ssii/
  * https://www.developpez.net/forums/d2112046/emploi-etudes-informatique/emploi/ssii/esn-restent-ssii/


## Fichiers sources pour des données de génération aléatoire : "resources/"

Une des idées principales de départ est de générer aléatoirement (ou pas, en orientant) une partie du CV. Des fichiers de ressources sont présents sur les thématiques suivantes : 

* Compétences "métier" (Hard Skills)
* Compétences relationnelles et assimilées (Soft Skills)
* Types de contrats (Contract Types)
* Noms d'entreprises, instituts, associations... (Corporation Names)
* Domaines d'actvités (Corporations Domains)
* Prénoms (First Names)
* Noms (Last Names)
* "Éléments Biographiques"  (Biographic Tables)
* Liste de métiers (à revoir) => Jobs.txt et BiographicJobs.txt
* Liste d'outils (à revoir) => Tools.txt

Le contenu de ces fichiers est à adapter en fonction de l'usage, ils permettent déjà d'obtenir de bons exemples de contenu. 

## Sources pour certains contenus

Pour les noms d'entreprises et slogans, secteurs d'activités : 
* Nanochrome, NanoChrome² et Nanodex (Par John Grümph)
* CyberPunk 2020, CyberPunk Red (Mike Pondsmith et al.) à compléter avec données de la liste présente ici : https://cyberpunk.fandom.com/wiki/Category:Cyberpunk_2020_Corporations
* GURPS CyberPunk, Séries TV *DarkAngel* et *Kyle XY*...

Également pour la génération de quelques autres noms : 
* Uplink "Hacker Elite" (Introversion Software) et "mods" associés

## Autres ressources et idées

### "Fake Data Generation" (Faker, MockNeat...)

  * https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker Generating Fake Data for Python Unit Tests with Faker
  * https://faker.readthedocs.io/en/master/ -- Welcome to Faker's documentation!
  * https://blogs.sap.com/2021/05/26/generate-custom-datasets-using-python-faker/ Generate custom datasets using Python Faker
  * https://pypi.org/project/Faker/ Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.
  * https://dzone.com/articles/generating-arbitrary-data-using-mockneat Generating and Mocking Data With MockNeat (equivalent of MockNeat in Python ?? => Faker)

### Éléments de fausses identités

  * See [arf.json of OSINT-Framework](https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json)
  * [Fake Identity Generator](http://justdelete.me/fake-identity-generator/)
  * [Fake Name Generator](https://www.fakenamegenerator.com/)

```
{First Name}{Middle Name (if apply)}{LastName}
{Address}
	Mother's maiden name
	SSN
	Geo coordinates
Phone
	Phone
	Country code
Birthday
	Birthday
	Age
	Tropical zodiac
Online
	Email Address
	Username
	Password
	Website
	Browser user agent
Finance
	{Card Type}
	Expires
	CVV2
Employment
	Company
	Occupation
Physical characteristics
	Height
	Weight
	Blood type
Tracking numbers
	UPS tracking number
	Western Union MTCN
	MoneyGram MTCN
Other
	Favorite color
	Vehicle
	GUID
	QR Code
```


### Idées complémentaires : fausses entreprises / entreprises de fiction

Génération de fausses identités complètes pour tests (et fausses entreprises associées). 

  * https://fr.wikipedia.org/wiki/Catégorie:Entreprise_de_fiction Liste d'entreprises de fiction
  * https://fr.wikipedia.org/wiki/Liste_de_marques_fictives Liste de marques fictives
  
### Idées d'entreprises fictives utilisables

Entreprises fictives référencées sur LinkedIn (pop-culture, CyberPunk 20XX et autres films, jeux vidéos...) : 
  * [Aperture Science Enrichment Center](https://www.linkedin.com/company/aperture-science-enrichment-center/) -- Portal & Portal 2
  * [Arasaka Corporation](https://www.linkedin.com/company/arasaka-corporation/) -- CyberPunk 20XX
  * [Cyberdyne Systems Corporation](https://www.linkedin.com/company/cyberdyne-systems-corporation/) -- Terminator
  * [Waynes Enterprises](https://www.linkedin.com/company/wayne-enterprises-ltd/) -- Batman / DC Comics
  * [Stark Industries](https://www.linkedin.com/company/stark-industries-llc/ ; https://www.linkedin.com/company/be-stark-industries/) -- Iron Man / Marvel
  * [Umbrella Corporation](https://www.linkedin.com/company/umbrella-corporation-uk/) -- Resident Evil (films et jeux vidéos)
  * [Weyland-Yutani Corporation](https://www.linkedin.com/company/weyland-yutani-corporation/) -- Alien (toute la série de films, incluant Prometheus)
  * [Sirius Cybernetics Corporation](https://www.linkedin.com/company/sirius-cybernetics-corporation/) -- The Hitchhiker's Guide to the Galaxy / Le Guide du Routard Galactique de Douglas Adams
  * [Tessier-Ashpool SA - Bioengineering a better human race. ](https://www.linkedin.com/company/tessier-ashpool-sa/) -- Roman 'Neuromancien' de William Gibson
  * [Wintermute Group -- Services de recherche, Berne](https://www.linkedin.com/company/wintermutegroup/) "Leader In Neural Network Research" -- Roman 'Neuromancien' de William Gibson
  * ... 

Plus d'autres par ici : 
  * [Entreprises de fiction ](https://www.forbes.com/sites/michaelnoer/2011/03/11/the-25-largest-fictional-companies/?sh=3f15b6925d81)
  * [12 famous fictional branding from television and film](https://en.99designs.ch/blog/creative-inspiration/famous-fictional-branding-from-television-and-film/)
  * [Science fiction: How not to build a future society](https://www.bbc.com/future/article/20141127-nine-future-societies-to-avoid)

### Photos, Avatars... 

L'intérêt ici est de recenser de quoi avoir une photo ou un avatar graphique pour portrait dans le CV (donc, suffisemment professionnel). 

  * https://thispersondoesnotexist.com/
  * https://www.avatar-gratuit.com/
  * https://avatarmaker.com/
  * https://face.co/
  * http://www.hexatar.com/
  * ... 

Voir également du côté des générateurs génériques utilisant un GAN (Generative Adversarial Network) : https://thisxdoesnotexist.com/
  * https://github.com/NVlabs/stylegan2
  * https://github.com/lucidrains/stylegan2-pytorch
  * https://github.com/lucidrains/lightweight-gan
  

### Sites de recrutement 

  * www.pole-emploi.fr
  * www.apec.fr
  * fr.linkedin.com
  * www.talent.io
  * www.fiftytalents.com
  * www.cadremploi.fr
  * www.monster.fr

### Lettres de motivation

  * https://www.journaldunet.fr/management/guide-du-management/1200753-lettre-de-motivation-exemple-modele-gratuit-a-telecharger-et-comment-la-faire/
  * www.himp.com ??
  * ...

### Notions de "Web Scrapping" / "Web Scraping"

  * https://zenscrape.com/web-scraping-with-python/
  * https://devopscube.com/python-web-scrapping/
  * https://oxylabs.io/blog/python-web-scraping

### Profils humoristiques et trolls vus sur LinkedIn

  * [Bertrand Chanderlin sur LinkedIn](https://www.linkedin.com/in/bertrand%2Dchanderlin%2D2022/)
  * [Bertrand Chanderlin sur Twitter](https://twitter.com/B_chanderlin)
  * [Clement Berut](https://www.linkedin.com/in/cl%C3%A9ment-%F0%9F%A6%85-berut-%E2%9D%97-4207111b/)
  * ... 
  * ... 

## Usages possibles de cet outil  et évolutions

Voici une liste réaliste et variée d'**usages possibles** pour le projet **CurriculumGenerator** en 2026 et plus, en tenant compte de son état actuel (générateur Python/Perl => LaTeX => PDF, données textuelles dans `resources/`, génération semi-aléatoire ou dirigée, focus multi-langue et ATS).

| N° | Usage principal | Description concrète | Niveau de faisabilité actuel | Difficulté d'adaptation | Public cible principal |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1  | **Génération de CV personnels rapides** | Remplir et modifier les fichiers texte => script => PDF propre en LaTeX | ★★★★☆ (déjà fonctionnel) | Faible | Développeurs, étudiants, LaTeX lovers |
| 2  | **Création de multiples variantes pour candidatures** | Générer 5–10 versions d'un même CV (différents ordres de compétences, accent sur tel outil/projet, longueur différente) | ★★★★☆ | Faible à moyenne | Chercheurs d'emploi intensifs |
| 3  | **Tests de parsing ATS / plateformes de recrutement** | Produire des CV "contrôlés" pour voir comment LinkedIn, Welcome to the Jungle, Indeed, Monster, SAP SuccessFactors, Workday… les interprètent | ★★★★★ (objectif originel du projet) | Faible | Recruteurs tech, consultants SIRH, passionnés RH-tech |
| 4  | **Études / expériences sur les biais en recrutement** | Générer des CV identiques sauf nom/prénom/genre/âge/origine => soumettre et observer les réponses / taux de rappel | ★★★★☆ | Moyenne (script de batch + tracking) | Chercheurs en sociologie du travail, assos anti-discrimination, doctorants RH |
| 5  | **Génération de faux profils pour tests / démos / pentest** | Créer des dizaines/centaines de faux CV plausibles pour tester un parseur interne, un chatbot RH, un outil de matching IA, une base de données anonymisée | ★★★★☆ | Moyenne (ajout Faker-like) | Développeurs d'outils RH, pentesters éthiques, éditeurs de logiciels SIRH |
| 6  | **Création de CV thématiques / fictifs (Cyberpunk, SF, JdR)** | Utiliser les listes de ressources pour intégrer des entreprises fictives (Arasaka, Militech, Night City Corp…), compétences futuristes, outils imaginaires | ★★★☆☆ (très fun) | Faible | MJ / rôlistes, créateurs de lore, convention JdR, humour geek |
| 7  | **Support pédagogique "structure d'un bon CV"** | Montrer aux étudiants / bootcampers comment le même contenu change selon l'ordre, les mots-clés, la mise en page => générer avant/après | ★★★★☆ | Moyenne | Formateurs dev, RH formateurs, écoles informatique |
| 8  | **Génération massive pour A/B testing de design LaTeX** | Produire 50+ PDF avec variations (awesome-cv vs moderncv vs altacv, une colonne vs deux, couleurs vs monochrome…) et demander des retours | ★★★☆☆ | Moyenne | Designers de templates CV, créateurs de contenu "career advice" |
| 9  | **Base pour un mini-projet "CV builder" open-source** | Transformer le script en CLI + YAML/JSON d'entrée + choix de template => fork moderne | ★★☆☆☆ (gros chantier) | Élevée | Contributeurs potentiels ?? |
| 10 | **Critique / satire des pratiques RH** | Générer des CV absurdes mais keyword-stuffed pour montrer les limites du recrutement par mots-clés (ex: "JavaScript Java Python Perl Rust Go C++" partout) | ★★★★☆ | Faible | Posts LinkedIn/X satiriques, conférences "anti-bullshit jobs" |

### Usages les plus immédiats (sans presque rien changer)
- Usages personnels => ton CV perso en PDF LaTeX très propre et mis à jour rapidement
- Tester 3-4 plateformes de recrutement avec la même base de données => voir ce qui passe / ce qui casse
- Générer 20 CV aléatoires plausibles en 2 minutes pour une démo ou un article de blog
- S'amuser à faire un CV "runner" Cyberpunk 2020 / 2077 avec Arasaka, Trauma Team, etc.

### Usages qui demandent un petit coup de pouce (quelques heures / jours)
- Ajouter un générateur Faker-like pour plus de variété et moins de répétition dans les noms/entreprises
- Passer les données d'entrée en YAML => beaucoup plus lisible et maintenable
- Ajouter un flag `--ats-mode` qui force police Arial/Times, enlève colonnes et icônes
- Créer un script batch qui génère 100 CV et les nomme automatiquement (prenom-nom-date-langue-poste.pdf)

Le projet reste petit et "artisanal", mais son orientation **génération contrôlée + test ATS + multi-langue + LaTeX** peut le rendre étonnamment polyvalent pour qui aime bidouiller.  

