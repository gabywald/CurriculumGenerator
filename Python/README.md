# CurriculumGenerator/Python

*Travaux en cours*

__Si des développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

L'objectif ici étant principalement de réviser le Python, et plus spécifiquement le Python 3 : le code présent n'est pas significatif de travaux connexes. L'objectif est tout de mee qu'il puisse être repris facilement en Python ou dans un autre langage de programmation. 

## Outils, technologies et autres éléments utilisés

Ici, certains éléments sont précisés en détail, même si ils semble,net insignifiant à un développeur expérimenté ; de façon à ce qu'un débutant puisse s'y retrouver tout de même sans aucun à priori. 

* Python 3.8.5
* __script principal__ : 'generateCurriculum.py'
* Autre script d'entrée : 'generateFromParameterFile.py' (appelle le précédent à partir d'un fichier)
* Autre script d'entrée : 'mainFileGenertor.py' (génère fichier pour le précédent)
* Eclipse / PyCharm
* Shell Bash
* UTF-8 (les sources pythons et les fichiers de configuration)
* pdflatex ("texlive-*") ; package "texlive-fonts-extra" in Ubuntu (for 'fontawesome' / "fonts-font-awesome" needed in case of 'casual' résumé style, https://www.ctan.org/pkg/fontawesome "Web-Related Icons")

Testé sous Linux Ubuntu 20.04

## Paramètres d'entrée

### Script principal 'generateCurriculum.py'

```
./generateCurriculum.py --help
usage: Curriculum Generator [-h] [-s {classic,casual,oldstyle,banking}]
                            [-c {blue,orange,green,red,purple,grey,black}] [-rs] [-rc] [-rfn]
                            [-rln] [-gt GENERALTITLE] [-ti TITLE] [-sp SPECIALITY] [-fn FIRSTNAME]
                            [-ln LASTNAME] [-em EMAIL] [-ps PSEUDO] [-wp WEBPAGE] [-ad ADDRESS]
                            [-cp CELLPHONE] [-qc QUOTE] [-ei EXTRAINFO] [-se SKILLELEMENTS]
                            [-je JOBELEMENTS] [-te TRAININGELEMENTS] [-rse] [-rje] [-rte]
                            [-lse LISTSKILLELEMENTS] [-lje LISTJOBELEMENTS]
                            [-lte LISTTRAININGELEMENTS] [-nqc] [-nei] [-m] [-ya]

BEGINNING of help

optional arguments:
  -h, --help            show this help message and exit
  -s {classic,casual,oldstyle,banking}, --style {classic,casual,oldstyle,banking}
                        ModernCV Style
  -c {blue,orange,green,red,purple,grey,black}, --color {blue,orange,green,red,purple,grey,black}
                        ModernCV Color
  -rs, --randomstyle    Random ModernCV Color
  -rc, --randomcolor    Random ModernCV Color
  -rfn, --randomfirstname
                        Random First Name
  -rln, --randomlastname
                        Random Last Name
  -gt GENERALTITLE, --generaltitle GENERALTITLE
                        General Title
  -ti TITLE, --title TITLE
                        Title
  -sp SPECIALITY, --speciality SPECIALITY
                        Speciality
  -fn FIRSTNAME, --firstname FIRSTNAME
                        First Name
  -ln LASTNAME, --lastname LASTNAME
                        Last Name
  -em EMAIL, --email EMAIL
                        E-Mail
  -ps PSEUDO, --pseudo PSEUDO
                        Pseudonym
  -wp WEBPAGE, --webpage WEBPAGE
                        Web Page / URL
  -ad ADDRESS, --address ADDRESS
                        Address (IRL)
  -cp CELLPHONE, --cellphone CELLPHONE
                        Cell Phone
  -qc QUOTE, --quote QUOTE
                        Quote / Citation
  -ei EXTRAINFO, --extrainfo EXTRAINFO
                        Extra Info (i.e. age, for exemple)
  -se SKILLELEMENTS, --skillelements SKILLELEMENTS
                        Number of SKILL Elements
  -je JOBELEMENTS, --jobelements JOBELEMENTS
                        Number of JOB Elements
  -te TRAININGELEMENTS, --trainingelements TRAININGELEMENTS
                        Number of TRAINING Elements
  -rse, --randomskillelements
                        Random number of SKILL elements
  -rje, --randomjobelements
                        Random number of JOB elements
  -rte, --randomtrainingelements
                        Random number of TRAINING elements
  -lse LISTSKILLELEMENTS, --listskillelements LISTSKILLELEMENTS
                        List of SKILL elements
  -lje LISTJOBELEMENTS, --listjobelements LISTJOBELEMENTS
                        List of JOB elements
  -lte LISTTRAININGELEMENTS, --listtrainingelements LISTTRAININGELEMENTS
                        List of TRAINING elements
  -nqc, --noquote       NO quote / Citation
  -nei, --noextrainfo   NO quote / Citation
  -m, --make            Launch Making of PDF from TeX file
  -ya, --allyes         Automatically yes for generated elements / questions
  -bio, --biographic    Curriculum Generation in a Biographic way

END of help
```

NOTES : 
* pour les éléments *se, *je et *te (Compétence, Travails, Formations // Skills / Jobs / Trainings), les listes fournies sont prioritaires sur les nombres et la sélection aléatoire ; 
* fonctionenent en binôme : {qc;nqc}, {ei;nei}, les négatifs sont prioritaires ; 
* 'allyes' (ya) permet une sélection automatiques des éléments générés aléatoirement ; 
* email et pseudo acceptent une valeur 'default' (généré à partir nom et prénom). 
* ... 

Les informations non fournies par les arguments sont demandés de façon 'interactive' (attente saisie utilisateur), excepté : adresse, e-mail et numéro de téléphone portable. 

### Script principal 'generateFromParameterFile.py'

Ce script attend un argument : le chemin d'aaccès au fichier d'entrée. 

Voir le fichier exemple :  _argumentParameterFileExample.txt_ . 

Le format attendu est le suivant, chaque contenu de colonne est séparé par une tabulation ('\t') : 


----------------------------
CVstyle|CVcolor|FirstName|LastName|Age|PhysicalAddress|Pseudo|WebSite|email|quote|skills|jobs|trainings|General Title|Title|Speciality
:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---
Note 1 |Note 2 |	|	|	|	|	|	|	|	|	|	|	|	|	|	|	       

----------------------------

NOTE 1 : Style de CV parmi les suivants {classic,casual,oldstyle,banking}

NOTE 2 : Couleur de CV parmi les suivantes {blue,orange,green,red,purple,grey,black}

**Formats particuliers : skills, jobs, trainings** : si plusieurs fois pour un même élément, séparer par des ';' (point-virgules)
* 'skills' : groupe de compétences::compétences associées
* 'jobs' : base::thématique::domaine d'activité::nom entreprise::type de contrat
* 'trainings' : Type de Formation::Thématique::Localisation

### Script principal 'generateParameterFile.py'

Un argument optionnel pour ce script : le nombre de profils à générer. 

Ce script génère le fichier d'entrée pour 'generateFromParameterFile.py'. 

## Cas d'utilisation / Cas d'usage

Environnement Python 3.8 doit être installé. 

Les scripts doivent être executables. 

```
./generateParameterFile.py 5 > exportPersonnae.txt

./generateFromParameterFile.py exportPersonnae.txt

```

On obtient ainsi 5 Curriculum / CV générés en LaTeX et compilés en PDF. 
* Un répertoire "<prénom>.<nom>_generated" pour chacun des profils 
* Un répertoire "generated" contenant les PDF produits

Le fichier 'exportPersonnae.txt' est modifiable, ainsi que les fichiers '.tex', afin de compléter et modifier les contenus (commande 'make' dans le répertoire dédié pour générer à nouveau le PDF). 

	
## "En l'état" (octobre -> décembre 2020)

L'objectif premier étant (de mon côté, initiateur du projet) de réviser le Python et surtout Python 3 pour les éléments suivants : 
 * lecture de fichiers
 * écriture de fichier
 * passage de paramètres
 * utilisation de listes
 * utilisation de dictionnaire
 * utiliser la génération aléatoire (random)
 * Programmation Orientée Objet
 * ...
 
La première partie étant faite (révisions Python 3, donc) ; ce qui reste à faire est d'affiner la génération des CV, plus sur le contenu : 
* dates des étapes professionnelles ; 
* gestion fine des formations (autodidactes acceptés !) ; 
* gestion des centres d'intérêts ; 

Plusieurs scripts pour aider à générer les CV, ainsi que plusieurs scripts d'entrée pour faciliter l'usage. 

__Si d'autres développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

Revue en décembre 2020 : 
 * Renommage des scripts ( => "generate*") ; 
 * Ajout documentation (dans ce fichier README.md) ; 
 * ...

## Exemples de lancement

### generateCurriculum

Une liste des arguments est obtenue avec "./generateCurriculum.py --help". 

* ./generateCurriculum.py -rfn -rln -em default -qc NOQUOTE --make

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-qc NOQUOTE')
	- compilation du CV ('--make')
	
* ./generateCurriculum.py -rfn -rln -em toto@domain.org --noquote

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail "toto@domain.org"
	- NOQUOTE (peut être obtenu avec -nq / --noquote)
	- compilation du CV (--make)
	
* ./generateCurriculum.py -rfn -rln -em toto@domain.org -qc "There is no try" -je 5 -te 3

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail "toto@domain.org"
	- quote "There is no try" ('-qc "There is no try"')
	- compilation du CV ('--make')
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')

* ./generateCurriculum.py -rfn -rln -em default -qc NOQUOTE -je 4 -te 3 -se 10 -ya -nei

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélectyion aléatoire ('-ya')
	- Pas d'information complémentaire ('-nei')

* ./generateCurriculum.py -rfn -rln -em default -nqc -je 4 -te 3 -se 10 -ya -ei "42 ans"

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-nqc')
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélection aléatoire ('-ya')
	- Inforrmation en plus "42 ans" ('-ei "42 ans"')

* ./generateCurriculum.py -lse "Domain::A, B, C;Other::---" -rfn -rln -ti title -gt "general title" -sp speciality -nq -nei -se 1 -je 5 -te 3 --email default -ya -lje "International::Recrutement::Publication::Panopticon::Stage" -lte "Autodidacte::Programmation;Autoformation::Création d'Entreprise"


	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-nqc')
	- NOEXTRAINFO ('-nei')
	- compilation du CV ('-make')
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélection aléatoire ('-ya')
	- liste prédéfinie des compétences ('-lse "Domain::A, B, C;Other::---"')
	- liste prédéfinie des expériences professionnelles ('-lje "International::Recrutement::Publication::Panopticon::Stage"')
	- liste prédéfinie des formations ('-lte "Autodidacte::Programmation::Bali;Autoformation::Création d'Entreprise::Night City"')
	- Titre général du CV ('-gt "general title"')
	- Titre ('-ti title')
	- Spécialité ('-sp speciality')
	
* ./generateCurriculum.py -fn first -ln last -gt TITLE --title title -sp speciality -nq -ne --make --email default --allyes -se 0 -je 5 -te 5 -bio

	- GÉNÉRATION BIOGRAPHIQUE ('-BIO') : __les nombres de jobs et trainings seront aditionnés et considérés globalement__ 
	- prénom 'first' ('-fn first')
	- nom 'last' ('-ln last')
	- adresse e-mail par défault (à partir nom et prénom, '--email default') 
	- NOQUOTE ('-nq')
	- NOEXTRAINFO ('-ne')
	- compilation du CV ('-make')
	- 5 expériences professionnelles ('-je 5')
	- 5 formations ('-te 5')
	- 0 compétences ('-se 0')
	- acceptation automatique de la sélection aléatoire ('--allyes')
	- Titre général du CV ('-gt TITLE')
	- Titre ('-ti title')
	- Spécialité ('-sp speciality')

* ./generateCurriculum.py -rfn -rln -gt TITLE --title title -sp speciality -nq -ne --make --email default --allyes -se 0 -je 5 -te 5 -bio

	- GÉNÉRATION BIOGRAPHIQUE ('-BIO') : __les nombres de jobs et trainings seront aditionnés et considérés globalement__ 
	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '--email default') 
	- NOQUOTE ('-nq')
	- NOEXTRAINFO ('-ne')
	- compilation du CV ('-make')
	- 5 expériences professionnelles ('-je 5')
	- 5 formations ('-te 5')
	- 0 compétences ('-se 0')
	- acceptation automatique de la sélection aléatoire ('--allyes')
	- Titre général du CV ('-gt TITLE')
	- Titre ('-ti title')
	- Spécialité ('-sp speciality')



### generateFromParameterFile.py et generateParameterFile.py

* _generateFromParameterFile.py_   Ce script est conçu pour générer une série de CV / Curriculum à partir d'un fichier d'entrée fournit en paramètre. 

 * _generateParameterFile.py_   Ce script est conçu pour générer le fichier d'entrée du script 'generateFromParameterFile.py'
 
 * Voir les Cas d'utilisation / Cas d'usage pour le lancement de ces scripts. 

## "Biograph[y|ic] Generation"

Voir les éléments développés dans les répertoires suivants : biographyv1, biographyv2, biographic ; ressources propres : biography (contemporain : '2020' ; original ; 'cyberage'). 

Intégration faite dans le générateur général (racine Python) avec argument '-bio' / '--biographic', comme alternative pour générer le contenu. Les exemples de lancement avec arguments ont été complétés avec cet argument, exemples également dans le fichier d'entrée pour la génération en chaine avec un fichier. 

**NOTE** : dans le cas de l'utilisation cet argument, les nombres de 'jobs' et 'trainings' sont additionnés pour une génération globale du profil. Quand cet argument est passé via un fichier (valeur 'BIO'), c'est le nombre de 'skills' qui est pris en compte !

Reste à développer, plus facile avec cette façon de faire (biographique), complétion des parties suivantes : 
 * Certification
 * BenevolentTasks
 * Realisations
 * CentresDInteret
 * ... 

Le contenu est présent (et toujours remplaçable et / ou peut être complété). 

## Tutoriels et formations Python : 
* https://docs.python.org/fr/3.8/tutorial/
* https://docs.python.org/fr/3.8/howto/regex.html
* https://fr.wikibooks.org/wiki/Programmation_Python/Exemples_de_scripts
* https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants
* https://www.tutorialspoint.com/python/python_command_line_arguments.htm
* https://python.sdv.univ-paris-diderot.fr/07_fichiers/
* https://python.doctor/page-apprendre-programmation-orientee-objet-poo-classes-python-cours-debutants
* https://www.w3schools.com/python/python_dictionaries.asp
* https://www.geeksforgeeks.org/python-dictionary/
* https://www.w3schools.com/python/python_regex.asp
* PEP 8 : https://www.python.org/dev/peps/pep-0008/
* PEP 20 : https://www.python.org/dev/peps/pep-0020/ => Zen Of Python and Easter Egg !
* "Conventions de syntaxe en python" : http://all4dev.libre-entreprise.org/index.php/Conventions_de_syntaxe_en_python

NOTE : approffondir la python DOC !

NOTE : voir utilisation Python Linter (vérifier la validité du code)

NOTE : utiliser str.format() instead of print with '%' ! https://www.w3schools.com/python/ref_string_format.asp
