#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import argparse

import CurriculumBiographicTable
CurriculumBiographicTable.loadTables()

##### ##### ##### ##### ##### ##### 
## Below is reading from arguments
##### ##### ##### ##### ##### ##### 

parser = argparse.ArgumentParser(
    prog = 'Curriculum Generator', 
    description = """BEGINNING of help""", 
    epilog = """END of help""" )

# Some arguments ... 
parser.add_argument("-s", "--style", 
    help = "ModernCV Style", 
    choices = [ 'classic', 'casual', 'oldstyle', 'banking' ], 
    default = "classic", 
    type=str )
parser.add_argument("-c", "--color", 
    help = "ModernCV Color", 
    choices = [ 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black' ], 
    default = "blue", 
    type=str )

parser.add_argument("-rs", "--randomstyle", 
    help = "Random ModernCV Color", 
    action = "store_true" )
parser.add_argument("-rc", "--randomcolor", 
    help = "Random ModernCV Color", 
    action = "store_true" )
    
parser.add_argument("-rfn", "--randomfirstname", 
    help = "Random First Name", 
    action = "store_true" )
parser.add_argument("-rln", "--randomlastname", 
    help = "Random Last Name", 
    action = "store_true" )

parser.add_argument("-gt", "--generaltitle", 
    help = "General Title", 
    type=str )
parser.add_argument("-ti", "--title", 
    help = "Title", 
    type=str )
parser.add_argument("-sp", "--speciality", 
    help = "Speciality", 
    type=str )
    
parser.add_argument("-fn", "--firstname", 
    help = "First Name", 
    type=str )
parser.add_argument("-ln", "--lastname", 
    help = "Last Name", 
    type=str )
parser.add_argument("-em", "--email", 
    help = "E-Mail", 
    type=str )
parser.add_argument("-ps", "--pseudo", 
    help = "Pseudonym", 
    type=str )
parser.add_argument("-wp", "--webpage", 
    help = "Web Page / URL", 
    type=str )
parser.add_argument("-ad", "--address", 
    help = "Address (IRL)", 
    type=str )
parser.add_argument("-cp", "--cellphone", 
    help = "Cell Phone", 
    type=str )
parser.add_argument("-qc", "--quote", 
    help = "Quote / Citation", 
    type=str )
parser.add_argument("-ei", "--extrainfo", 
    help = "Extra Info (i.e. age, for exemple)", 
    type=str )

parser.add_argument("-se", "--skillelements", 
    help = "Number of SKILL Elements", 
    type=int )
parser.add_argument("-je", "--jobelements", 
    help = "Number of JOB Elements", 
    type=int )
parser.add_argument("-te", "--trainingelements", 
    help = "Number of TRAINING Elements", 
    type=int )

parser.add_argument("-rse", "--randomskillelements", 
    help = "Random number of SKILL elements", 
    action = "store_true" )
parser.add_argument("-rje", "--randomjobelements", 
    help = "Random number of JOB elements", 
    action = "store_true" )
parser.add_argument("-rte", "--randomtrainingelements", 
    help = "Random number of TRAINING elements", 
    action = "store_true" )

parser.add_argument("-lse", "--listskillelements", 
    help = "List of SKILL elements", 
    type=str )
parser.add_argument("-lje", "--listjobelements", 
    help = "List of JOB elements", 
    type=str )
parser.add_argument("-lte", "--listtrainingelements", 
    help = "List of TRAINING elements", 
    type=str )

parser.add_argument("-nqc", "--noquote", 
    help = "NO quote / Citation", 
    action = "store_true" )

parser.add_argument("-nei", "--noextrainfo", 
    help = "NO extra info", 
    action = "store_true" )

parser.add_argument("-m", "--make", 
    help = "Launch Making of PDF from TeX file", 
    action = "store_true" )

parser.add_argument("-ya", "--allyes", 
    help = "Automatically yes for generated elements / questions", 
    action = "store_true" )

parser.add_argument("-bio", "--biographic", 
    help = "Curriculum Generation in a Biographic way", 
    action = "store_true" )

def parsingArgs() :
    args = parser.parse_args()
    ## print( args )
    return args

##### ##### ##### ##### ##### ##### 
## Interactive User Interaction
##### ##### ##### ##### ##### ##### 

def checkArgsAndReturn( args, name, argsValue ) : 
    if ( (hasattr(args, name)) and (argsValue != None) ) : 
        return argsValue
    return None

def checkList( args, name, argsList, finalnbelts, finalList ) : 
    if ( (hasattr(args, name)) and (argsList != None) ) :
        finalnbelts = 0
        for elt in argsList.split(";") : 
            finalList.append( elt.split("::") )
    return finalList

def interactionSelection( elementsList, nbElements, allyes, strDom) : 
    while ( len( elementsList ) < nbElements) : 
        futurevalue = None
        if (strDom == "Skills") : 
            futurevalue = CurriculumBiographicTable.selectRandomSkill()
        elif (strDom == "Job") : 
            futurevalue = CurriculumBiographicTable.selectRandomBiographic()
        elif (strDom == "Training") : 
            futurevalue = CurriculumBiographicTable.selectRandomTraining()
        else : 
        	break
        ## TODO the negative choice by default ?
        remaining = (nbElements) - len( elementsList )
        userchoice = None
        if ( allyes ) : 
            userchoice = "Y"
        else : 
            print ( futurevalue )
            userchoice = str(input("\t (remaining: %d ) [%s] Keep ? [Y/n]" %(remaining, strDom) ))
        if ( (userchoice != "N") and (userchoice != "n") ) :
            if futurevalue not in elementsList: 
                elementsList.append( futurevalue )

def askForInt( txtmsg ) : 
    data = None
    while ( data == None ):
        try:
            data = int(input( txtmsg ))
        except ValueError:
            print("Please enter digits")
    return data

def askForStrNotEmpty( txtmsg ) : 
    data = None
    while ( ( data == None ) or (data == '') ):
        try:
            data = str(input( txtmsg ))
        except ValueError:
            print("Please enter not empty alphanumerics")
        if ( data == '' ) : 
            print("Please enter not empty alphanumerics")
    return data

def interactiveCompletionSkillsJobsTraining( personnae, args ) : 
    ## ## ## ## ## SKILLS + JOBS + TRAININGS
    personnae.skilleltnb = checkArgsAndReturn( args, 'skillelements', args.skillelements )
    personnae.jobeltsnb = checkArgsAndReturn( args, 'jobelements', args.jobelements )
    personnae.trainingeltsnb = checkArgsAndReturn( args, 'trainingelements', args.trainingelements )
    personnae.skills = checkList(args, 'listskillelements', args.listskillelements, personnae.skilleltnb, personnae.skills)
    personnae.jobs = checkList(args, 'listjobelements', args.listjobelements, personnae.jobeltsnb, personnae.jobs)
    personnae.trainings = checkList(args, 'listtrainingelements', args.listtrainingelements, personnae.trainingeltsnb, personnae.trainings)
    ## ## ## ## ## ask for nbs
    if (personnae.skilleltnb == None) : 
        personnae.skilleltnb = askForInt( "Number of Skills elements ?" )
    if (personnae.jobeltsnb == None) : 
        personnae.jobeltsnb = askForInt( "Number of Jobs elements ?" )
    if (personnae.trainingeltsnb == None) : 
        personnae.trainingeltsnb = askForInt( "Number of Training elements ?" )
    ## ## Interact with user to choose Skills / Jobs / Trainings (randomly generated)
    interactionSelection( personnae.skills, personnae.skilleltnb, args.allyes, "Skills" )
    interactionSelection( personnae.jobs, personnae.jobeltsnb, args.allyes, "Job" )
    interactionSelection( personnae.trainings, personnae.trainingeltsnb, args.allyes, "Training" )

def interactiveCompletionOf( personnae, args ) : 
    ## ## ## ## ## cvStyle and cvColor are random if argument indicates it, otherwise as selected
    cvStyle = random.choice( curriculumDataObj.cvStyle ) if args.randomstyle else args.style
    cvColor = random.choice( curriculumDataObj.cvColor ) if args.randomcolor else args.color
    ## print( "CV STYLE : " + cvStyle )
    ## print( "CV COLOR : " + cvColor )
    ## ## ## ## ## Data From Arguments
    personnae.firstname = checkArgsAndReturn( args, 'firstname', args.firstname )
    personnae.lastname = checkArgsAndReturn( args, 'lastname', args.lastname )
    personnae.generaltitle = checkArgsAndReturn( args, 'generaltitle', args.generaltitle )
    personnae.title = checkArgsAndReturn( args, 'title', args.title )
    personnae.speciality = checkArgsAndReturn( args, 'speciality', args.speciality )
    personnae.email = checkArgsAndReturn( args, 'email', args.email )
    personnae.address = checkArgsAndReturn( args, 'address', args.address )
    personnae.webpage = checkArgsAndReturn( args, 'webpage', args.webpage )
    personnae.cellphone = checkArgsAndReturn( args, 'cellphone', args.cellphone )
    ## QUOTE
    if args.noquote : 
        personnae.quote = "NOQUOTE"
    else:
        if ( (hasattr(args, 'quote')) and (args.quote != None) ) :
            personnae.quote = args.quote
    ## EXTRAINFO
    if args.noextrainfo : 
        personnae.extrainfo = "NOEXTRAINFO"
    else:
        personnae.extrainfo = checkArgsAndReturn( args, 'extrainfo', args.extrainfo )
    ## ## ## ## ## Random numbers for {Skills;Jobs;Trainings} number of elements
    if (args.randomjobelements) :
        personnae.skilleltnb = random.randint(1, 20)
    if (args.randomjobelements) :
        personnae.jobeltsnb = random.randint(1, 20)
    if (args.randomtrainingelements) :
        personnae.trainingeltsnb = random.randint(1, 5)
    ## print ( personnae.skilleltnb )
    ## print ( personnae.jobeltsnb )
    ## print ( personnae.trainingeltsnb )
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
    ## ## ## ## ## Random Generation Part 1
    ## Random Generation of First Name
    if (args.randomfirstname) :
        personnae.firstname = random.choice( curriculumDataObj.firstNameList )
    ## Random Generation of Last Name
    if (args.randomlastname) :
        personnae.lastname = random.choice( curriculumDataObj.lastNameList )
    ## ## ## ## ## Interaction with user Part 1
    if (personnae.firstname == None) : 
        personnae.firstname = askForStrNotEmpty( "First Name? " )
    if (personnae.lastname == None) : 
        personnae.lastname = askForStrNotEmpty( "Last Name? " )
    if (personnae.generaltitle == None) : 
        personnae.generaltitle = askForStrNotEmpty( "General Title? " )
    if (personnae.title == None) : 
        personnae.title = askForStrNotEmpty( "Title? " )
    if (personnae.speciality == None) : 
        personnae.speciality = askForStrNotEmpty( "Speciality? " )
    if (personnae.quote == None) : 
        personnae.quote = askForStrNotEmpty( "quote / citation ? ('NOQUOTE' for nothing) " )
    if (personnae.extrainfo == None) : 
        personnae.extrainfo = askForStrNotEmpty( "extra info ? ('NOEXTRAINFO' for nothing) " )
    ## ## ## ## ## Pseudo From Arguments OR generated from {First Name + Last Name}
    if ( (hasattr(args, 'pseudo')) and (args.pseudo != None) ) :
        personnae.pseudo = args.pseudo
    else:
        personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()
    ## ## ## ## ## EMail Generation (from pseudo) of from Arguments
    defaultemail = personnae.pseudo + "@gmx.com"
    if (personnae.email == None) : 
        personnae.email = askForStrNotEmpty( "e-mail (default=[%s])?" % defaultemail )
    if (personnae.email == "default"):
        personnae.email = defaultemail
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
    ## ## ## ## ## Generation Part 2
    if (personnae.address == None) : 
        personnae.address = "1337 Grand Boulevard -- 61337 Section 42"
    if (personnae.cellphone == None) : 
        personnae.cellphone = "06~12~34~56~78"
    if (personnae.webpage == None) : 
        personnae.webpage = personnae.pseudo + ".personnalbranding.com"
    return personnae


