# CurriculumGenerator

Pour générer des CV ("Curriculum Vitae") en LaTeX (et les traiter pour obtenir un PDF correspondant) ; utilisation de différents langages de programmation, idéalement des langages de script comme Python ou Perl. 

Cette idée afin de permettre de générer facilement un (ou plusieurs) CV, obtenir un bon exemple à réutiliser et tester sur les plate-formes de recrutement et / ou les processus de recrutement. 

Utile tant professionnellement qu'en "Job Testing" (pour travailler sur les discriminations à l'embauche ?)? 

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

Pour les noms d'entreprises et slogans, secteurs d'acivités : 
* Nanochrome, NanoChrome² et Nanodex (Par John Grümph)
* CyberPunk 2020, CyberPunk Red (Mike Pondsmith et al.) à compléter avec données de la liste présente ici : https://cyberpunk.fandom.com/wiki/Category:Cyberpunk_2020_Corporations
* GURPS CyberPunk, Séries TV *DarkAngel* et *Kyle XY*

Également pour la génération de quelques autres noms : 
* Uplink "Hacker Elite" (Introversion Software) et "mods" associés

## Autres ressources et idées

### "Fake Data Generation"

  * https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker Generating Fake Data for Python Unit Tests with Faker
  * https://faker.readthedocs.io/en/master/ -- Welcome to Faker’s documentation!
  * https://blogs.sap.com/2021/05/26/generate-custom-datasets-using-python-faker/ Generate custom datasets using Python Faker
  * https://pypi.org/project/Faker/ Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.
  * https://dzone.com/articles/generating-arbitrary-data-using-mockneat Generating and Mocking Data With MockNeat (equivalent of MockNeat in Python ?? => Faker)

### Idées complémentaires : fausses entreprises

Génération de fausses identités complètes pour tests (et fausses entreprises associées). 

https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Entreprise_de_fiction Liste d'entreprises de fiction

Idées d'entreprises fictives utilisables, déjà référencées (par exemple sur LinkedIn) : 
  - Aperture Science Enrichment Center : https://www.linkedin.com/company/aperture-science-enrichment-center/about/
  - Arasaka Corporation : https://www.linkedin.com/company/arasaka-corporation/mycompany/
  - Cyberdyne Systems Corporation : https://www.linkedin.com/company/cyberdyne-systems-corporation/
  - Waynes Enterprises : https://www.linkedin.com/company/wayne-enterprises-ltd/
  - Stark Industries : https://www.linkedin.com/company/stark-industries-llc/ ; https://www.linkedin.com/company/be-stark-industries/ ; ... 
  - Umbrella Corporation : https://www.linkedin.com/company/umbrella-corporation-uk/
  - Weyland-Yatani Corporation : https://www.linkedin.com/company/weyland-yutani-corporation/
  - Sirius Cybernetics Corporation : https://www.linkedin.com/company/sirius-cybernetics-corporation/
  - ... 
  
Entreprises de fiction : https://www.forbes.com/sites/michaelnoer/2011/03/11/the-25-largest-fictional-companies/?sh=3f15b6925d81
12 famous fictional branding from television and film : https://en.99designs.ch/blog/creative-inspiration/famous-fictional-branding-from-television-and-film/
Science fiction: How not to build a future society : https://www.bbc.com/future/article/20141127-nine-future-societies-to-avoid

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

### Un peu de "Web Scrapping" / "Web Scrapping"

 * https://zenscrape.com/web-scraping-with-python/
 * https://devopscube.com/python-web-scrapping/
 * https://oxylabs.io/blog/python-web-scraping

