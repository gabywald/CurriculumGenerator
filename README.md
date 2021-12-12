# CurriculumGenerator

Pour générer des CV ("Curriculum Vitae") en LaTeX (et les traiter pour obtenir un PDF correspondant) ; utilisation de différents langages de programmation, idéalement des langages de script comme Python ou Perl. Cette idée afin de permettre de générer facilement un (ou plusieurs) CV, obtenir un bon exemple à réutiliser et tester sur les plate-formes de recrutement et / ou les processus de recrutement. 

Utile tant professionnellement qu'en "Job Testing" (pour travailler sur les discriminations à l'embauche ?) ou construction de "légende" (un peu de StoryTelling ?) avec un historique contextualisé sous forme de biographie éventuelle. En d'autres termes : un outil qui permet de revoir le CV sous sa forme classique, mais généré à outrance via des outils informatiques dédiés. 

L'idée de base étant de réfléchir à ce qui fait un "bon CV" : 
  * Intitulé(s) ; 
  * Compétences ; 
  * Expériences / Parcours ; 
  * Contexte de mission ou de projet ; 
  * La 'véritable' personne derrière : Motivation, Localisation, Histoire...
  
__Si d'autres développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

Licence : GPLv3

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
  * https://faker.readthedocs.io/en/master/ -- Welcome to Faker’s documentation!
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

Questionnement sur les faux comptes (notamment sur LinkedIn), utilisés par des escrocs : https://blogbuster.fr/social/linkedin-faux-profil.htm (déjà constaté personnellement : faux recruteurs, collecte de données personnelles, usurpation d'ientité...) dont ce n'est pas l'objectif ici !

En réponse également aux recruteurs qui font des bases de données de candidats potentiels, notamment les sociétés de services (SSII / SS2I / ESN en France) ; et qui, notamment, proposent souvent des CV plus avantageux à leurs propsects et clients potentiels, souvent au-delà de la réalité et du possible !

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
