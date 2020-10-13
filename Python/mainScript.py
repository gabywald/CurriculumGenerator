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
import subprocess
import os

import mainFunctions
import curriculumGeneration
import curriculumData

## mainFunctions.main(sys.argv[1:])

cvStyle = [ 'classic', 'casual', 'oldstyle', 'banking' ]
cvColor = [ 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black' ]

hsList = mainFunctions.readFileToList( '../resources/HardSkills.txt' )
sfList = mainFunctions.readFileToList( '../resources/SoftSkills.txt' )
firstNameList = mainFunctions.readFileToList( '../resources/NameFirstListing.txt' )
lastNameList = mainFunctions.readFileToList( '../resources/NameLastListing.txt' )
contractTypesList = mainFunctions.readFileToList( '../resources/ContractTypes.txt' )
corporationNames = mainFunctions.readFileToList( '../resources/CorporationsNames.txt' )

uplinkCompanyPartOne = mainFunctions.readFileToList( '../resources/dataUplinkReduced/companyPart1.txt' )
uplinkCompanyPartTwo = mainFunctions.readFileToList( '../resources/dataUplinkReduced/companyPart2.txt' )
uplinkFornames = mainFunctions.readFileToList( '../resources/dataUplinkReduced/fornamesComplete.txt' )
uplinkSurnames = mainFunctions.readFileToList( '../resources/dataUplinkReduced/surnames.txt' )

## print( hsList )

## TODO passing these in arguments ?!
cvStyle = "classic"
cvColor = "black"

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
	curriculumGenerationtest.write( curriculumGeneration.getMinimalVariableDefinitions() + "\n" )
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
print( "Changing dir to {" + texcurriculumDirectory + "}..." )
os.chdir( texcurriculumDirectory )
print( "Compiling TeX file to PDF..." )
retcode = subprocess.call( "make", shell=True )
print( retcode )
print( "Cleaning..." )
retcode2 = subprocess.call( "make clean", shell=True )
print( retcode2 )
print( "Changing dir BACK..." )
os.chdir( ".." )

print("End of script")

