#!/usr/bin/python3
# -*- coding: utf-8 -*- ## useless in python 3 ? ; default is unicode ?

__author__        = "Gabriel Chandesris"
__copyright__    = "CC Gabriel Chandesris (2020)"
__credits__        = ""
__licence__        = "GNU GENERAL PUBLIC LICENSE v3"
__version__        = "0.1.0"
__maintainer__    = "Gabriel Chandesris"
__email__        = "gabywald[at]laposte.net"
__contact__        = "gabywald[at]laposte.net"
__status__        = "Development"

import sys

print('(debugging pourposes) Number of arguments:', len(sys.argv), 'arguments.' )
print('(debugging pourposes) Argument List:', str(sys.argv) )

from pathlib import Path
from datetime import datetime

import shutil

import random

import curriculumMainFunctions
import curriculumGeneration

from Person import Person
from curriculumData import CVData

import BiographicTable
BiographicTable.loadTables()

args = curriculumMainFunctions.parsingArgs()

curriculumDataObj = CVData.loadConfig();

# print( curriculumDataObj.hardList )
# print( curriculumDataObj.softList )
# print( curriculumDataObj.jobsList )
# print( curriculumDataObj.toolList )
# print( curriculumDataObj.cvStyle )
# print( curriculumDataObj.cvColor )

## TODO passing these in arguments ?!
cvStyle = random.choice( curriculumDataObj.cvStyle ) if args.randomstyle else args.style
cvColor = random.choice( curriculumDataObj.cvColor ) if args.randomcolor else args.color

print( "CV STYLE : " + cvStyle )
print( "CV COLOR : " + cvColor )

personnae = Person()

if ( (hasattr(args, 'firstname')) and (args.firstname != None) ) :
    personnae.firstname    = args.firstname
    
if ( (hasattr(args, 'lastname')) and (args.lastname != None) ) :
    personnae.lastname    = args.lastname

## print ( curriculumDataObj.firstNameList )
if (args.randomfirstname) :
    personnae.firstname = random.choice( curriculumDataObj.firstNameList )

## print ( curriculumDataObj.lastNameList )
if (args.randomlastname) :
    personnae.lastname = random.choice( curriculumDataObj.lastNameList )

if (personnae.firstname == None) : 
    personnae.firstname = str(input("First Name? "))

if (personnae.lastname == None) : 
    personnae.lastname = str(input("Last Name? "))

print( "CV firstname: " + personnae.firstname )
print( "CV lastname : " + personnae.lastname )

if ( (hasattr(args, 'address')) and (args.address != None) ) :
    personnae.address = args.address
    
if ( (hasattr(args, 'webpage')) and (args.webpage != None) ) :
    personnae.webpage = args.webpage

if ( (hasattr(args, 'pseudo')) and (args.pseudo != None) ) :
    personnae.pseudo = args.pseudo
else:
    personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()

if ( (hasattr(args, 'email')) and (args.email != None) ) :
    if (args.email == 'default'): 
        args.email = personnae.pseudo + "@gmx.com"
    personnae.email = args.email

if args.noquote : 
    personnae.quote = "NOQUOTE"
else:
    if ( (hasattr(args, 'quote')) and (args.quote != None) ) :
        personnae.quote = args.quote

if (args.randomjobelements) :
    personnae.jobeltsnb = random.randint(1, 20)

if ( (hasattr(args, 'jobelements')) and (args.jobelements != None) ) :
    personnae.jobeltsnb = args.jobelements

if (args.randomtrainingelements) :
    personnae.trainingeltsnb = random.randint(1, 5)

if ( (hasattr(args, 'trainingelements')) and (args.trainingelements != None) ) :
    personnae.trainingeltsnb = args.trainingelements

if (personnae.email == None) : 
    defaultemail = personnae.firstname.lower() + "." + personnae.lastname.lower() + "@gmx.com"
    personnae.email = str(input("e-mail (default=[%s])?" % defaultemail))
    if (personnae.email == "default"):
        personnae.email = defaultemail

if (personnae.quote == None) : 
    personnae.quote = str(input("quote / citation ?"))

if (personnae.jobeltsnb == None) : 
    personnae.jobeltsnb = int(input("Number of Jobs elements ?"))

if (personnae.trainingeltsnb == None) : 
    personnae.trainingeltsnb = int(input("number of Training elements ?"))

if (personnae.address == None) : 
    personnae.address = "1337 Grand Boulevard -- 61337 Section 42"

if (personnae.webpage == None) : 
    personnae.webpage = "http://" + personnae.firstname.lower() + "." + personnae.lastname.lower() + ".personnalbranding.com"

print( personnae )

localListOfSkills = []

## ## Interact with user to choose Jobs (randmoly generated)
while True : 
    futurejob = BiographicTable.selectRandomBiographic()
    ## TODO the negative choice by default ?
    remaining = (personnae.jobeltsnb) - len( personnae.jobs )
    userchoice = str(input("\t (remaining: %d ) [Job] Keep ? [Y/n]" %(remaining) ));
    if ( (userchoice != "N") and (userchoice != "n") ) :
        personnae.jobs.append( futurejob )
    if ( len( personnae.jobs ) >= personnae.jobeltsnb) : 
        break

## ## Interact with user to choose Training (randmoly generated)
while True : 
    futuretrain = BiographicTable.selectRandomTraining()
    ## TODO the negative choice by default ?
    remaining = (personnae.trainingeltsnb) - len( personnae.trainings )
    userchoice = str(input("\t (remaining: %d ) [Training] Keep ? [Y/n]" %(remaining) ) )
    if ( (userchoice != "N") and (userchoice != "n") ) :
        personnae.trainings.append( futuretrain )
    if ( len( personnae.trainings ) >= personnae.trainingeltsnb) : 
        break

## Date_time generation
now = datetime.now()
print("now =", now)
dt_string = now.strftime("%Y%m%d_%H%M%S")
print("date and time =", dt_string)    

## prefix for directory / filename
texSpecific = personnae.lastname + "." + personnae.firstname ## + "_" + dt_string

## texcurriculumDirectory = "generate/"
## texcurriculumFileName = "curriculumGenerationtest"
texcurriculumDirectory = texSpecific + "_" + "generate/"
texcurriculumFileName = texSpecific

## Copy images files directory !!
path = Path( texcurriculumDirectory )
if ( path.exists() ) :
    print("Removing some resources...")
    shutil.rmtree( texcurriculumDirectory )
print( "Copying some resources..." )
shutil.copytree( "../resources/latexSamples/img/", texcurriculumDirectory + "img/" )

## Generate Makefile
print( "Creating Makefile..." )
with open( texcurriculumDirectory + "Makefile", 'w') as makefile:
    makefile.write( curriculumGeneration.getMakefileContent( texcurriculumFileName ) )

## Generate the TeX file
print( "Creating TeX file..." )
with open( texcurriculumDirectory + texcurriculumFileName + ".tex", 'w') as curriculumGenerationtest:
    curriculumGenerationtest.write( curriculumGeneration.getLaTeXHeaderPart1(cvColor, cvStyle) )
    curriculumGenerationtest.write( "\n\n" )
    ## Personnal Data
    curriculumGenerationtest.write( curriculumGeneration.getMinimalVariableDefinitions( 
        firstname = personnae.firstname, lastname = personnae.lastname
    ) + "\n" )
    curriculumGenerationtest.write( curriculumGeneration.getAddressDefinition(address = personnae.address) + "\n" )
    curriculumGenerationtest.write( curriculumGeneration.getEMailDefinition(email = personnae.email) + "\n" )
    curriculumGenerationtest.write( curriculumGeneration.getWebSiteDefinition(webpage = personnae.webpage) + "\n" )
    curriculumGenerationtest.write( curriculumGeneration.getQuoteDefinition(quote = personnae.quote) + "\n" )
    curriculumGenerationtest.write( "\n\n" )
    ## more header
    curriculumGenerationtest.write( curriculumGeneration.getFancyStyle() + "\n\n" )
    curriculumGenerationtest.write( "\\def\\motsClefs{LaTeX;PDF;Python;Python3...}\n\n" )
    curriculumGenerationtest.write( curriculumGeneration.getHyperSetup() + "\n\n" )
    curriculumGenerationtest.write( curriculumGeneration.getDefVariables() + "\n\n" )
    ## Starting document here !
    curriculumGenerationtest.write( "\\begin{document}\n\n\\maketitle\n\n" )
    ## Compétences
    curriculumGenerationtest.write( "\\section{Comp{\\'e}tences}\n")
    curriculumGenerationtest.write( "\t Introduction Text !!\n\n" )
    ## TODO add some skills (hard and soft) to put in description !
    curriculumGenerationtest.write( "\t \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
    curriculumGenerationtest.write( "\t \\cvcomputer{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
    ## Professionnal Experiences
    curriculumGenerationtest.write( "\\section{Exp{\\'e}rience professionnelle}\n" )
    for eltJOB in personnae.jobs : 
        corporationName = random.choice( curriculumDataObj.corporationNames )
        contractType    = random.choice( curriculumDataObj.contractTypesList )
        curriculumGenerationtest.write( "\t \\cventry{years}{" + corporationName + " (" + eltJOB[1] + ")}{" + eltJOB[0] + "}{" + contractType + "}{\n %% grade \n}{\n %% description \n}\n\n" )
    curriculumGenerationtest.write( "\t %% \\cventry{years}{degree/job title}{institution/employer}{localization}{grade}{description}\n\n" )
    curriculumGenerationtest.write( "\t \\cventry{DATUM}{TITRE}{ENTREPRISE}{CONTRAT}%\n" )
    curriculumGenerationtest.write( "\t     {\\newline INTITULE++}{%\n" )
    curriculumGenerationtest.write( "\t \\begin{itemize}\n" )
    curriculumGenerationtest.write( "\t     \\item[$\\rightarrow$] ELEMENTUN\n" )
    curriculumGenerationtest.write( "\t     \\item[$\\bullet$] ELEMENTDEUXETPLUS\n" )
    curriculumGenerationtest.write( "\t \\end{itemize}}\n\n" )
    ## Training ...
    curriculumGenerationtest.write( "\\section{Formation}\n" )
    for eltTraining in personnae.trainings : 
        curriculumGenerationtest.write( "\t \\cventry{years}{ " + eltTraining[1] + " }{" + eltTraining[0] + "}{ LOCALISATION }{\n %% grade \n}{\n %% description \n}\n\n" )
    curriculumGenerationtest.write( "\t %% \\cventry{Year}{Diploma}{\\newline School}{Location}    {}{}{}\n\n" )
    ## Certifications ...
    curriculumGenerationtest.write( "\\section{Licences et Certifications}\n" )
    curriculumGenerationtest.write( "\t \\cventry{Year}{Diploma}{\newline School}{Location}    {}{}{}\n\n" )
    ## Bénévolat ...
    curriculumGenerationtest.write( "\\section{Expériences de bénévolat}\n" )
    curriculumGenerationtest.write( "\t \\cventry{years}{degree/job title}{institution/employer}{localization}{grade}{description}\n\n" )
    ## Compétences ...
    curriculumGenerationtest.write( "\\section{Compétences}\n" )
    curriculumGenerationtest.write( "\t \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
    ## Recommandations ...
    curriculumGenerationtest.write( "\\section{Recommandations}\n" )
    curriculumGenerationtest.write( "\t \\cvcomputer{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
    ## Réalisations :  ...
    curriculumGenerationtest.write( "\\section{Réalisations}\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Projets}{ Sur GitHub (par exemple) }\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Langues}{ Anglais... }\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Organisations}{ associations... }\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Publications}{ citations, references... }\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Lectures}{ READINGS }\n\n" )
    ## Out of Work / Centres d'intérêts
    curriculumGenerationtest.write( "\\section{Centres d'int{\\'e}r{\\^e}ts}\n\n" )
    curriculumGenerationtest.write( "\t \\cvitem{Lectures}{ READINGS }\n" )
    curriculumGenerationtest.write( "\t \\cvitem{SocialGames}{ SOCIALGAMES }\n" )
    curriculumGenerationtest.write( "\t \\cventry{Year}{WHAT}{CONTENT}{Location}    {MORE1}{MORE2}{MORE3}\n\n" )
    ## END of document 
    curriculumGenerationtest.write( "\\end{document}\n\n" )
    
## TODO continuing / finishing generation of features in document ... 

## Compiling TeX file to obtain PDF !
if args.make : 
    curriculumMainFunctions.launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

print("End of script")
