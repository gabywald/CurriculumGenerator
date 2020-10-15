#!/usr/bin/python3
# -*- coding: utf-8 -*- ## useless in python 3 ? ; default is unicode ?

__author__		= "Gabriel Chandesris (2020)"
__copyright__	= "CC Gabriel Chandesris (2020)"
__credits__		= ""
__licence__		= "GNU GENERAL PUBLIC LICENSE v3"
__version__		= "0.1.0"
__maintainer__	= "Gabriel Chandesris"
__email__		= "gabywald[at]laposte.net"
__contact__		= "gabywald[at]laposte.net"
__status__		= "Development"

import sys

print('Number of arguments:', len(sys.argv), 'arguments.' )
print('Argument List:', str(sys.argv) )

from pathlib import Path

import shutil

import random

import mainFunctions
import curriculumGeneration
import curriculumData

args = curriculumData.parsingArgs()

## mainFunctions.main(sys.argv[1:])

curriculumDataObj = curriculumData.loadConfig();

print( curriculumDataObj.hsList )
print( curriculumDataObj.cvStyle )
print( curriculumDataObj.cvColor )

## TODO passing these in arguments ?!
cvStyle = random.choice( curriculumDataObj.cvStyle ) if args.randomstyle else args.style
cvColor = random.choice( curriculumDataObj.cvColor ) if args.randomcolor else args.color

print( "CV STYLE : " + cvStyle )
print( "CV COLOR : " + cvColor )

firstname	= "Anne"
lastname	= "Onyme"

if ( (hasattr(args, 'firstname')) and (args.firstname != None) ) :
	firstname	= args.firstname
else:
	firstname	= "Anne"
	
if ( (hasattr(args, 'lastname')) and (args.lastname != None) ) :
	lastname	= args.lastname
else:
	lastname	= "Onyme"
	
print ( firstname )
print ( lastname )

## print ( curriculumDataObj.firstNameList )
if (args.randomfirstname) :
	firstname = random.choice( curriculumDataObj.firstNameList )

## print ( curriculumDataObj.lastNameList )
if (args.randomlastname) :
	lastname = random.choice( curriculumDataObj.lastNameList )
	
print( "CV firstname: " + firstname )
print( "CV lastname : " + lastname )

texcurriculumDirectory = "generate/"
texcurriculumFileName = "curriculumGenerationtest"

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
	curriculumGenerationtest.write( curriculumGeneration.getMinimalVariableDefinitions( 
		firstname = firstname, lastname = lastname
	) + "\n" )
	curriculumGenerationtest.write( curriculumGeneration.getAddressDefinition() + "\n" )
	curriculumGenerationtest.write( curriculumGeneration.getEMailDefinition() + "\n" )
	curriculumGenerationtest.write( curriculumGeneration.getWebSiteDefinition() + "\n\n" )
	curriculumGenerationtest.write( curriculumGeneration.getFancyStyle() + "\n\n" )
	curriculumGenerationtest.write( "\\def\\motsClefs{LaTeX;PDF;Python;Python3...}\n\n" )
	curriculumGenerationtest.write( curriculumGeneration.getHyperSetup() + "\n\n" )
	curriculumGenerationtest.write( curriculumGeneration.getDefVariables() + "\n\n" )
	## Starting document here !
	curriculumGenerationtest.write( "\\begin{document}\n\n\\maketitle\n\n" )
	curriculumGenerationtest.write( "\\section{Comp{\\'e}tences}\nIntroduction Text !!\n\n" )
	curriculumGenerationtest.write( "%% \\cvdoubleitem{ Item }{Description }\n\n" )
	curriculumGenerationtest.write( "\\section{Exp{\\'e}rience professionnelle}\n\n" )
	curriculumGenerationtest.write( "\\cventry{years}{degree/job title}{institution/employer}{localization}{grade}{description}\n\n" )
	curriculumGenerationtest.write( "\\cventry{DATUM}{TITRE}{ENTREPRISE}{CONTRAT}%\n" )
	curriculumGenerationtest.write( "	{\\newline INTITULE++}{%\n" )
	curriculumGenerationtest.write( "\\begin{itemize}\n" )
	curriculumGenerationtest.write( "	\\item[$\\rightarrow$] ELEMENTUN\n" )
	curriculumGenerationtest.write( "	\\item[$\\bullet$] ELEMENTDEUXETPLUS\n" )
	curriculumGenerationtest.write( "\\end{itemize}}\n\n" )
	curriculumGenerationtest.write( "\\section{Formation}\n\n" )
	curriculumGenerationtest.write( "\\cventry{Year}{Diploma}{\\newline School}{Location}	{}{}{}\n\n" )
	curriculumGenerationtest.write( "\\section{Centres d'int{\\'e}r{\\^e}ts}\n\n" )
	curriculumGenerationtest.write( "\\cvitem{Lectures}{ READINGS }\n" )
	curriculumGenerationtest.write( "\\cvitem{SocialGames}{ SOCIALGAMES }\n" )
	curriculumGenerationtest.write( "\\cventry{Year}{WHAT}{CONTENT}{Location}	{MORE1}{MORE2}{MORE3}\n\n" )
	curriculumGenerationtest.write( "\\end{document}\n\n" )
	
## TODO continuing / finishing generation of features in document ... 

## Compiling TeX file to obtain PDF !
if args.make : 
	mainFunctions.launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

print("End of script")

