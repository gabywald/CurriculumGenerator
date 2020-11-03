#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import sys, getopt, os, subprocess

import argparse
## from argparse import ArgumentParser

import BiographicTable
BiographicTable.loadTables()

def launcheMakePDFfromLaTeX( directory ) : 
    print( "Changing dir to {" + directory + "}..." )
    os.chdir( directory )
    print( "Compiling TeX file to PDF..." )
    retcode = subprocess.call( "make", stdin=None, stdout=subprocess.DEVNULL, stderr=None, shell=True )
    print( retcode )
    print( "Cleaning..." )
    retcode2 = subprocess.call( "make clean", stdin=None, stdout=subprocess.DEVNULL, stderr=None, shell=True)
    print( retcode2 )
    print( "Changing dir BACK..." )
    os.chdir( ".." )

def testAndGetInList(index, list, alternatevalue) : 
    item = None
    if ( index < len( list ) ) : 
        item = list[ index ]
    else: 
        item = alternatevalue
    return item

def checkArgsAndReturn( args, name, argsValue ) : 
    if ( (hasattr(args, name)) and (argsValue != None) ) : 
        return argsValue
    return None

def interactionSelection( elementsList, nbElements, allyes, strDom) : 
    while ( len( elementsList ) < nbElements) : 
        futurevalue = None
        if (strDom == "Skills") : 
            futurevalue = BiographicTable.selectRandomSkill()
        elif (strDom == "Job") : 
            futurevalue = BiographicTable.selectRandomBiographic()
        elif (strDom == "Training") : 
            futurevalue = BiographicTable.selectRandomTraining()
        else : 
        	break
        ## TODO the negative choice by default ?
        remaining = (nbElements) - len( elementsList )
        userchoice = None
        if ( allyes ) : 
            userchoice = "Y"
        else : 
            userchoice = str(input("\t (remaining: %d ) [%s] Keep ? [Y/n]" %(remaining, strDom) ));
        if ( (userchoice != "N") and (userchoice != "n") ) :
            elementsList.append( futurevalue )
        if ( len( elementsList ) >= nbElements) : 
            break

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
    help = "NO quote / Citation", 
    action = "store_true" )

parser.add_argument("-m", "--make", 
    help = "Launch Making of PDF from TeX file", 
    action = "store_true" )

parser.add_argument("-ya", "--allyes", 
    help = "Automatically yes for generated elements / questions", 
    action = "store_true" )

def parsingArgs() :
    args = parser.parse_args()
    ## print( args )
    return args
    