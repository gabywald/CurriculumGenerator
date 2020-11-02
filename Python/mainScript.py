#!/usr/bin/python3
# -*- coding: utf-8 -*- default is unicode in python3 ?

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "0.1.0"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Main Script to generate a Curriculum, according to parameters indicated !

import sys

print('(debugging purposes) Number of arguments:', len(sys.argv), 'arguments.' )
print('(debugging purposes) Argument List:', str(sys.argv) )

from pathlib import Path
from datetime import datetime

import shutil
import os
import random

import curriculumMainFunctions
import curriculumGeneration

from Person import Person
from curriculumData import CVData

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

## ## ## ## ## Data From Arguments
personnae.firstname = curriculumMainFunctions.checkArgsAndReturn( args, 'firstname', args.firstname )
personnae.lastname = curriculumMainFunctions.checkArgsAndReturn( args, 'lastname', args.lastname )
personnae.generaltitle = curriculumMainFunctions.checkArgsAndReturn( args, 'generaltitle', args.generaltitle )
personnae.title = curriculumMainFunctions.checkArgsAndReturn( args, 'title', args.title )
personnae.speciality = curriculumMainFunctions.checkArgsAndReturn( args, 'speciality', args.speciality )
personnae.cellphone = curriculumMainFunctions.checkArgsAndReturn( args, 'cellphone', args.cellphone )
personnae.address = curriculumMainFunctions.checkArgsAndReturn( args, 'address', args.address )
personnae.webpage = curriculumMainFunctions.checkArgsAndReturn( args, 'webpage', args.webpage )
personnae.cellphone = curriculumMainFunctions.checkArgsAndReturn( args, 'cellphone', args.cellphone )
    
if args.noquote : 
    personnae.quote = "NOQUOTE"
else:
    if ( (hasattr(args, 'quote')) and (args.quote != None) ) :
        personnae.quote = args.quote
        
if args.noextrainfo : 
    personnae.extrainfo = "NOEXTRAINFO"
else:
    personnae.extrainfo = curriculumMainFunctions.checkArgsAndReturn( args, 'extrainfo', args.extrainfo )

personnae.skilleltnb = curriculumMainFunctions.checkArgsAndReturn( args, 'skillelements', args.skillelements )
personnae.jobeltsnb = curriculumMainFunctions.checkArgsAndReturn( args, 'jobelements', args.jobelements )
personnae.trainingeltsnb = curriculumMainFunctions.checkArgsAndReturn( args, 'trainingelements', args.trainingelements )

if ( (hasattr(args, 'listskillelements')) and (args.listskillelements != None) ) :
    personnae.skilleltnb = 0
    print ( args.listskillelements )
    personnae.skills = args.listskillelements.split(";")

if ( (hasattr(args, 'listjobelements')) and (args.listjobelements != None) ) :
    personnae.jobeltsnb = 0
    personnae.jobs = args.listjobelements.split(";")

if ( (hasattr(args, 'listtrainingelements')) and (args.listtrainingelements != None) ) :
    personnae.trainingeltsnb = 0
    personnae.trainings = args.listtrainingelements.split(";")

## ## ## Random numbers for {Skills;Jobs;Trainings} number of elements
if (args.randomjobelements) :
    personnae.skilleltnb = random.randint(1, 20)

if (args.randomjobelements) :
    personnae.jobeltsnb = random.randint(1, 20)

if (args.randomtrainingelements) :
    personnae.trainingeltsnb = random.randint(1, 5)

print (personnae.skilleltnb )
print (personnae.jobeltsnb )
print (personnae.trainingeltsnb )

## ## ## ## ## Random Generation Part 1
## Random Generation of First Name
if (args.randomfirstname) :
    personnae.firstname = random.choice( curriculumDataObj.firstNameList )

## Random Generation of Last Name
if (args.randomlastname) :
    personnae.lastname = random.choice( curriculumDataObj.lastNameList )

## ## ## ## ## Interaction with user Part 1
if (personnae.firstname == None) : 
	personnae.firstname = curriculumMainFunctions.askForStrNotEmpty( "First Name? " )

if (personnae.lastname == None) : 
    personnae.lastname = curriculumMainFunctions.askForStrNotEmpty( "Last Name? " )

if (personnae.generaltitle == None) : 
    personnae.generaltitle = curriculumMainFunctions.askForStrNotEmpty( "General Title? " )

if (personnae.title == None) : 
    personnae.title = curriculumMainFunctions.askForStrNotEmpty( "Title? " )

if (personnae.speciality == None) : 
    personnae.speciality = curriculumMainFunctions.askForStrNotEmpty( "Speciality? " )

if (personnae.quote == None) : 
    personnae.quote = curriculumMainFunctions.askForStrNotEmpty( "quote / citation ?" )

if (personnae.extrainfo == None) : 
    personnae.extrainfo = curriculumMainFunctions.askForStrNotEmpty( "extra info ?" )

if (personnae.skilleltnb == None) : 
    personnae.skilleltnb = curriculumMainFunctions.askForInt( "Number of Skills elements ?" )

if (personnae.jobeltsnb == None) : 
    personnae.jobeltsnb = curriculumMainFunctions.askForInt( "Number of Jobs elements ?" )

if (personnae.trainingeltsnb == None) : 
    personnae.trainingeltsnb = curriculumMainFunctions.askForInt( "Number of Training elements ?" )

## Pseudo From Arguments OR generated from {First Name + Last Name}
if ( (hasattr(args, 'pseudo')) and (args.pseudo != None) ) :
    personnae.pseudo = args.pseudo
else:
    personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()

## EMail Generation (from pseudo) of from Arguments
defaultemail = personnae.pseudo + "@gmx.com"

if ( (hasattr(args, 'email')) and (args.email != None) ) :
    personnae.email = args.email

if (personnae.email == None) : 
    personnae.email = curriculumMainFunctions.askForStrNotEmpty( "e-mail (default=[%s])?" % defaultemail )

if (personnae.email == "default"):
    personnae.email = defaultemail

## ## ## ## ## Generation Part 2
if (personnae.address == None) : 
    personnae.address = "1337 Grand Boulevard -- 61337 Section 42"

if (personnae.cellphone == None) : 
    personnae.cellphone = "06~12~34~56~78"

if (personnae.webpage == None) : 
    personnae.webpage = personnae.firstname.lower() + "." + personnae.lastname.lower() + ".personnalbranding.com"

## ## Interact with user to choose Skills / Jobs / Trainings (randomly generated)
curriculumMainFunctions.interactionSelection( personnae.skills, personnae.skilleltnb, args.allyes, "Skills" )
curriculumMainFunctions.interactionSelection( personnae.jobs, personnae.jobeltsnb, args.allyes, "Job" )
curriculumMainFunctions.interactionSelection( personnae.trainings, personnae.trainingeltsnb, args.allyes, "Training" )

print( personnae )

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
## print( "Copying some resources..." )
## shutil.copytree( "../resources/latexSamples/img/", texcurriculumDirectory + "img/" )
os.mkdir( texcurriculumDirectory )

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
    curriculumGenerationtest.write( curriculumGeneration.getExtraInformation(extrainfo = personnae.extrainfo) + "\n" )
    curriculumGenerationtest.write( "\n\n" )
    ## More header
    curriculumGenerationtest.write( curriculumGeneration.getFancyStyle() + "\n\n" )
    curriculumGenerationtest.write( "\\def\\motsClefs{LaTeX;PDF;Python;Python3;" + ";".join(personnae.skills) + "}\n\n" )
    curriculumGenerationtest.write( curriculumGeneration.getHyperSetup() + "\n\n" )
    curriculumGenerationtest.write( curriculumGeneration.getDefVariables() + "\n\n" )
    ## Starting document here !
    curriculumGenerationtest.write( "\\begin{document}\n\n\\maketitle\n\n" )
    ## Compétences
    curriculumGenerationtest.write( "\\section{Comp{\\'e}tences}\n")
    curriculumGenerationtest.write( "\t Introduction Text !!~\\\\ \n\n" )
    for i in range(0, len(personnae.skills), 4) : 
    	item1 = personnae.skills[ i + 0 ]
    	item2 = curriculumMainFunctions.testAndGetInList( i+1, personnae.skills, "--" )
    	item3 = curriculumMainFunctions.testAndGetInList( i+2, personnae.skills, "--" )
    	item4 = curriculumMainFunctions.testAndGetInList( i+3, personnae.skills, "--" )
    	curriculumGenerationtest.write( "\t \\cvcomputer{ %s }{ %s }{ %s }{ %s }\n" %( item1, item2, item3, item4) )
    # curriculumGenerationtest.write( "\t \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
    # curriculumGenerationtest.write( "\t \\cvcomputer{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
    curriculumGenerationtest.write( "\n" )
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
    curriculumGenerationtest.write( "\t \\cventry{Year}{Diploma}{\\newline School}{Location}    {}{}{}\n\n" )
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
