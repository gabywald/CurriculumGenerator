#!/usr/bin/python3
# -*- coding: utf-8 -*- default is unicode in python3 ?

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0a"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Main Script to generate a Curriculum, according to parameters indicated !

import sys
import shutil
import random

import CurriculumMainFunctions
import CurriculumGeneration

from Person import Person
from CurriculumData import CVData
from CurriculumLaTeXGenerator import generateLaTeX

## print('(debugging purposes) Number of arguments:', len(sys.argv), 'arguments.' )
## print('(debugging purposes) Argument List:', str(sys.argv) )

args = CurriculumMainFunctions.parsingArgs()

curriculumDataObj = CVData.loadConfig()

# print( curriculumDataObj.hardList )
# print( curriculumDataObj.softList )
# print( curriculumDataObj.jobsList )
# print( curriculumDataObj.toolList )
# print( curriculumDataObj.cvStyle )
# print( curriculumDataObj.cvColor )

## cvStyle and cvColor are random if argument indicates it, otherwise as selected
cvStyle = random.choice( curriculumDataObj.cvStyle ) if args.randomstyle else args.style
cvColor = random.choice( curriculumDataObj.cvColor ) if args.randomcolor else args.color

print( "CV STYLE : " + cvStyle )
print( "CV COLOR : " + cvColor )

personnae = Person()

## ## ## ## ## Data From Arguments
personnae.firstname = CurriculumMainFunctions.checkArgsAndReturn( args, 'firstname', args.firstname )
personnae.lastname = CurriculumMainFunctions.checkArgsAndReturn( args, 'lastname', args.lastname )
personnae.generaltitle = CurriculumMainFunctions.checkArgsAndReturn( args, 'generaltitle', args.generaltitle )
personnae.title = CurriculumMainFunctions.checkArgsAndReturn( args, 'title', args.title )
personnae.speciality = CurriculumMainFunctions.checkArgsAndReturn( args, 'speciality', args.speciality )
personnae.email = CurriculumMainFunctions.checkArgsAndReturn( args, 'email', args.email )
personnae.address = CurriculumMainFunctions.checkArgsAndReturn( args, 'address', args.address )
personnae.webpage = CurriculumMainFunctions.checkArgsAndReturn( args, 'webpage', args.webpage )
personnae.cellphone = CurriculumMainFunctions.checkArgsAndReturn( args, 'cellphone', args.cellphone )
    
if args.noquote : 
    personnae.quote = "NOQUOTE"
else:
    if ( (hasattr(args, 'quote')) and (args.quote != None) ) :
        personnae.quote = args.quote
        
if args.noextrainfo : 
    personnae.extrainfo = "NOEXTRAINFO"
else:
    personnae.extrainfo = CurriculumMainFunctions.checkArgsAndReturn( args, 'extrainfo', args.extrainfo )

personnae.skilleltnb = CurriculumMainFunctions.checkArgsAndReturn( args, 'skillelements', args.skillelements )
personnae.jobeltsnb = CurriculumMainFunctions.checkArgsAndReturn( args, 'jobelements', args.jobelements )
personnae.trainingeltsnb = CurriculumMainFunctions.checkArgsAndReturn( args, 'trainingelements', args.trainingelements )

if ( (hasattr(args, 'listskillelements')) and (args.listskillelements != None) ) :
    personnae.skilleltnb = 0
    print ( args.listskillelements )
    for elt in args.listskillelements.split(";") : 
        personnae.skills.append( elt.split("::") )

if ( (hasattr(args, 'listjobelements')) and (args.listjobelements != None) ) :
    personnae.jobeltsnb = 0
    for elt in args.listjobelements.split(";") : 
        personnae.jobs.append( elt.split("::") )

if ( (hasattr(args, 'listtrainingelements')) and (args.listtrainingelements != None) ) :
    personnae.trainingeltsnb = 0
    for elt in args.listtrainingelements.split(";") : 
        personnae.trainings.append( elt.split("::") )

## ## ## Random numbers for {Skills;Jobs;Trainings} number of elements
if (args.randomjobelements) :
    personnae.skilleltnb = random.randint(1, 20)

if (args.randomjobelements) :
    personnae.jobeltsnb = random.randint(1, 20)

if (args.randomtrainingelements) :
    personnae.trainingeltsnb = random.randint(1, 5)

print ( personnae.skilleltnb )
print ( personnae.jobeltsnb )
print ( personnae.trainingeltsnb )

## ## ## ## ## Random Generation Part 1
## Random Generation of First Name
if (args.randomfirstname) :
    personnae.firstname = random.choice( curriculumDataObj.firstNameList )

## Random Generation of Last Name
if (args.randomlastname) :
    personnae.lastname = random.choice( curriculumDataObj.lastNameList )

## ## ## ## ## Interaction with user Part 1
if (personnae.firstname == None) : 
	personnae.firstname = CurriculumMainFunctions.askForStrNotEmpty( "First Name? " )

if (personnae.lastname == None) : 
    personnae.lastname = CurriculumMainFunctions.askForStrNotEmpty( "Last Name? " )

if (personnae.generaltitle == None) : 
    personnae.generaltitle = CurriculumMainFunctions.askForStrNotEmpty( "General Title? " )

if (personnae.title == None) : 
    personnae.title = CurriculumMainFunctions.askForStrNotEmpty( "Title? " )

if (personnae.speciality == None) : 
    personnae.speciality = CurriculumMainFunctions.askForStrNotEmpty( "Speciality? " )

if (personnae.quote == None) : 
    personnae.quote = CurriculumMainFunctions.askForStrNotEmpty( "quote / citation ? ('NOQUOTE' for nothing) " )

if (personnae.extrainfo == None) : 
    personnae.extrainfo = CurriculumMainFunctions.askForStrNotEmpty( "extra info ? ('NOEXTRAINFO' for nothing) " )

if (personnae.skilleltnb == None) : 
    personnae.skilleltnb = CurriculumMainFunctions.askForInt( "Number of Skills elements ?" )

if (personnae.jobeltsnb == None) : 
    personnae.jobeltsnb = CurriculumMainFunctions.askForInt( "Number of Jobs elements ?" )

if (personnae.trainingeltsnb == None) : 
    personnae.trainingeltsnb = CurriculumMainFunctions.askForInt( "Number of Training elements ?" )

## Pseudo From Arguments OR generated from {First Name + Last Name}
if ( (hasattr(args, 'pseudo')) and (args.pseudo != None) ) :
    personnae.pseudo = args.pseudo
else:
    personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()

## EMail Generation (from pseudo) of from Arguments
defaultemail = personnae.pseudo + "@gmx.com"

if (personnae.email == None) : 
    personnae.email = CurriculumMainFunctions.askForStrNotEmpty( "e-mail (default=[%s])?" % defaultemail )

if (personnae.email == "default"):
    personnae.email = defaultemail

## ## ## ## ## Generation Part 2
if (personnae.address == None) : 
    personnae.address = "1337 Grand Boulevard -- 61337 Section 42"

if (personnae.cellphone == None) : 
    personnae.cellphone = "06~12~34~56~78"

if (personnae.webpage == None) : 
    personnae.webpage = personnae.pseudo + ".personnalbranding.com"

## ## Interact with user to choose Skills / Jobs / Trainings (randomly generated)
CurriculumMainFunctions.interactionSelection( personnae.skills, personnae.skilleltnb, args.allyes, "Skills" )
CurriculumMainFunctions.interactionSelection( personnae.jobs, personnae.jobeltsnb, args.allyes, "Job" )
CurriculumMainFunctions.interactionSelection( personnae.trainings, personnae.trainingeltsnb, args.allyes, "Training" )

print( personnae )

generateLaTeX( personnae )
    
## Compiling TeX file to obtain PDF !
if args.make : 
    CurriculumMainFunctions.launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

print("End of script")
