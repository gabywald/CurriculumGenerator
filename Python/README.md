# CurriculumGenerator/Python

*Travaux en cours*

__Si d'autres développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

L'objectif ici étant principalement de réviser le Python, et plus spécifiquement le Python 3 : le code présent n'est pas significatif de travaux connexes. L'objectif est tout de mee qu'il puisse être repris facilement en Python ou dans un autre langage de programmation. 

## Outils, technologies et autres éléments utilisés

Ici, certains éléments sont précisés en détail, même si ils semble,net insignifiant à un développeur expérimenté ; de façon à ce qu'un débutant puisse s'y retrouver tout de même sans aucun à priori. 

* Python 3.8.5
* __script principal__ : 'mainScript.py'
* Autre script d'entrée : 'mainWithFile.py' (appelle le précédent à partir d'un fichier)
* Eclipse / PyCharm
* Shell Bash
* UTF-8 (les sources pythons et les fichiers de configuration)
* pdflatex ("texlive-*") ; package "texlive-fonts-extra" in Ubuntu (for 'fontawesome' / "fonts-font-awesome" needed in case of 'casual' résumé style, https://www.ctan.org/pkg/fontawesome "Web-Related Icons")

Testé sous Linux Ubuntu 20.04

## Idées

* Paramètres d'entrée (à préciser)

	- nom
	- prénom
	- poste 
	- citation / quote
	- liste de compétences
	- un fichier (CSV de préférence ; JSON ?) regroupant les éléments précédents et également expériences professionnelles, formations... (format interne à définir)
	- fichiers plats avec noms d'entreprises ("corporations"), générées ou non à la volée
	- ...
	
## "En l'état" (23/10/2020)

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

__Si d'autres développeurs veulent participer au projet, n'hésitez pas à vous signaler !__

## Exemples de lancement

Une liste des arguments est obtenue avec "./mainScript.py --help". 

* ./mainScript.py -rfn -rln -em default -qc NOQUOTE --make

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-qc NOQUOTE')
	- compilation du CV ('--make')
	
* ./mainScript.py -rfn -rln -em toto@domain.org --noquote

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail "toto@domain.org"
	- NOQUOTE (peut être obtenu avec -nq / --noquote)
	- compilation du CV (--make)
	
* ./mainScript.py -rfn -rln -em toto@domain.org -qc "There is no try" -je 5 -te 3

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail "toto@domain.org"
	- quote "There is no try" ('-qc "There is no try"')
	- compilation du CV ('--make')
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')

* ./mainScript.py -rfn -rln -em default -qc NOQUOTE -je 4 -te 3 -se 10 -ya -nei

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélectyion aléatoire ('-ya')
	- Pas d'information complémentaire ('-nei')

* ./mainScript.py -rfn -rln -em default -nqc -je 4 -te 3 -se 10 -ya -ei "42 ans"

	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-nqc')
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélection aléatoire ('-ya')
	- Inforrmation en plus "42 ans" ('-ei "42 ans"')

* ./mainScript.py -lse "A;B;C" -rfn -rln -ti title -gt "general title" -sp speciality -nq -nei -se 1 -je 5 -te 3 --email default -ya -lje "International::Recrutement::Publication" -lte "Autodidacte::Programmation;Autoformation::Création d'Entreprise"


	- prénom aléatoire ('-rfn')
	- nom aléatoire ('-rln')
	- adresse e-mail par défault (à partir nom et prénom, '-em default') 
	- NOQUOTE ('-nqc')
	- NOEXTRAINFO ('-nei')
	- compilation du CV
	- 5 expériences professionnelles ('-je 5')
	- 3 formations ('-te 3')
	- 10 compétences ('-se 10')
	- acceptation automatique de la sélectyion aléatoire ('-ya')
	- liste prédéfinie des compétences ('-lse "A;B;C"')
	- liste prédéfinie des expériences professionnelles ('-lje "International::Recrutement::Publication"')
	- liste prédéfinie des formations ('-lte "Autodidacte::Programmation;Autoformation::Création d'Entreprise"')
	- Titre général du CV ('-gt "general title"')
	- Titre ('-ti title')
	- Spécialité ('-sp speciality')

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

NOTE : approffondir la python DOC !

NOTE : voir utilisation Python Linter (vérifier la validité du code)

NOTE : utiliser str.format() instead of print with '%' ! https://www.w3schools.com/python/ref_string_format.asp
