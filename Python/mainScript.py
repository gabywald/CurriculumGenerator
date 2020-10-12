#!/usr/bin/python3
# -*- coding: utf-8 -*- ## useless in python 3 ? ; default is unicode ?

import sys

print('Number of arguments:', len(sys.argv), 'arguments.' )
print('Argument List:', str(sys.argv) )

import mainFunctions

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

with open("generation/curriculumGenerationtest.tex", 'w') as curriculumGenerationtest:
	curriculumGenerationtest.write( "\\documentclass[11pt,a4paper]{moderncv}\n" )
	curriculumGenerationtest.write( "\\usepackage[french]{babel}\n" )
	curriculumGenerationtest.write( "\\moderncvtheme[black]{classic}\n" )
	curriculumGenerationtest.write( "%% \\moderncvstyle{...}\n" )
	curriculumGenerationtest.write( "%% \moderncvcolor{...}\n" )

## TODO continuing ... 

print("End of script")

