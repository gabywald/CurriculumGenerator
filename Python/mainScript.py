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

## ## ## ## ## Data From Arguments
if ( (hasattr(args, 'firstname')) and (args.firstname != None) ) :
    personnae.firstname = args.firstname
    
if ( (hasattr(args, 'lastname')) and (args.lastname != None) ) :
    personnae.lastname = args.lastname

if ( (hasattr(args, 'generaltitle')) and (args.generaltitle != None) ) :
    personnae.generaltitle = args.generaltitle

if ( (hasattr(args, 'title')) and (args.title != None) ) :
    personnae.title = args.title

if ( (hasattr(args, 'speciality')) and (args.speciality != None) ) :
    personnae.speciality = args.speciality

if ( (hasattr(args, 'cellphone')) and (args.cellphone != None) ) :
    personnae.cellphone = args.cellphone

if ( (hasattr(args, 'address')) and (args.address != None) ) :
    personnae.address = args.address

if ( (hasattr(args, 'cellphone')) and (args.cellphone != None) ) :
    personnae.cellphone = args.cellphone
    
if ( (hasattr(args, 'webpage')) and (args.webpage != None) ) :
    personnae.webpage = args.webpage

if args.noquote : 
    personnae.quote = "NOQUOTE"
else:
    if ( (hasattr(args, 'quote')) and (args.quote != None) ) :
        personnae.quote = args.quote
        
if args.noextrainfo : 
    personnae.extrainfo = "NOEXTRAINFO"
else:
    if ( (hasattr(args, 'extrainfo')) and (args.extrainfo != None) ) :
        personnae.extrainfo = args.extrainfo

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

if ( (hasattr(args, 'skillelements')) and (args.skillelements != None) ) :
    personnae.skilleltnb = args.skillelements

if (args.randomjobelements) :
    personnae.jobeltsnb = random.randint(1, 20)

if ( (hasattr(args, 'jobelements')) and (args.jobelements != None) ) :
    personnae.jobeltsnb = args.jobelements

if (args.randomtrainingelements) :
    personnae.trainingeltsnb = random.randint(1, 5)

if ( (hasattr(args, 'trainingelements')) and (args.trainingelements != None) ) :
    personnae.trainingeltsnb = args.trainingelements

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
if ( (hasattr(args, 'email')) and (args.email != None) ) :
    if (args.email == 'default'): 
        args.email = personnae.pseudo + "@gmx.com"
    personnae.email = args.email

if (personnae.email == None) : 
    defaultemail = personnae.pseudo + "@gmx.com"
    personnae.email = str(input("e-mail (default=[%s])?" % defaultemail))
    if (personnae.email == "default"):
        personnae.email = defaultemail

## ## ## ## ## Generation Part 2
if (personnae.address == None) : 
    personnae.address = "1337 Grand Boulevard -- 61337 Section 42"

if (personnae.cellphone == None) : 
    personnae.cellphone = "06~12~34~56~78"

if (personnae.webpage == None) : 
    personnae.webpage = personnae.firstname.lower() + "." + personnae.lastname.lower() + ".personnalbranding.com"

print( personnae )

## ## Interact with user to choose Skills (randomly generated)
while ( len( personnae.skills ) < personnae.skilleltnb) : 
    futureskill = BiographicTable.selectRandomSkill()
    ## TODO the negative choice by default ?
    remaining = (personnae.skilleltnb) - len( personnae.skills )
    userchoice = None
    if ( args.allyes ) : 
        userchoice = "Y"
    else : 
        userchoice = str(input("\t (remaining: %d ) [Skill] Keep ? [Y/n]" %(remaining) ));
    if ( (userchoice != "N") and (userchoice != "n") ) :
        personnae.skills.append( futureskill )
    if ( len( personnae.skills ) >= personnae.skilleltnb) : 
        break

## ## Interact with user to choose Jobs (randomly generated)
while ( len( personnae.jobs ) < personnae.jobeltsnb) : 
    futurejob = BiographicTable.selectRandomBiographic()
    ## TODO the negative choice by default ?
    remaining = (personnae.jobeltsnb) - len( personnae.jobs )
    userchoice = None
    if ( args.allyes ) : 
        userchoice = "Y"
    else : 
        userchoice = str(input("\t (remaining: %d ) [Job] Keep ? [Y/n]" %(remaining) ));
    if ( (userchoice != "N") and (userchoice != "n") ) :
        personnae.jobs.append( futurejob )
    if ( len( personnae.jobs ) >= personnae.jobeltsnb) : 
        break

## ## Interact with user to choose Training (randomly generated)
while ( len( personnae.trainings ) < personnae.trainingeltsnb) : 
    futuretrain = BiographicTable.selectRandomTraining()
    ## TODO the negative choice by default ?
    remaining = (personnae.trainingeltsnb) - len( personnae.trainings )
    userchoice = None
    if ( args.allyes ) : 
        userchoice = "Y"
    else : 
        userchoice = str(input("\t (remaining: %d ) [Training] Keep ? [Y/n]" %(remaining) ) )
    if ( (userchoice != "N") and (userchoice != "n") ) :
        personnae.trainings.append( futuretrain )
    if ( len( personnae.trainings ) >= personnae.trainingeltsnb) : 
        break

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
