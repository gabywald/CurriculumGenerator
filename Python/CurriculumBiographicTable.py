#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import re
import random

import CurriculumData
from CurriculumData import CVData

from BiographicDataLoad import BiographicDataLoad

class JobBiographicTable( object ) : 
    """This class defines Tables Definitions for 'biographic' elements for Curriculum generation. """
    
    def __init__(self, name = None, comments = None ):
        """JobBiographicTable Constructor. """
        self.name = name
        self.comments = comments
        self.contents = []
        self.linksTo  = []
        self.addins   = []
    
    def __str__(self) : 
        """JobBiographicTable to str. """
        str = "JobBiographicTable ( % s , % s ) \n"  % (self.name, self.comments)
        str += "\t contents: %s \n" % (self.contents)
        return str

# A dictionnary of JobBiographicTable
localDictionnary = {}

def loadTables() : 
    """Load JobBiographicTables from the configuration. """
    curriculumDataObj = CVData.loadConfig();
    tables     =  BiographicDataLoad.loadBiographicsTables()
    nextTable  = None
    for line in tables:
        resultTableHead       = re.match( "^Table (.*?)(\t(.*?))?$", line)
        resultTableContent    = re.match( "^\t(Table )?(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
        if (resultTableHead != None) : 
            if (nextTable != None) : 
                localDictionnary[ nextTable.name ] = nextTable
            ## print( resultTableHead.groups() )
            ## print( resultTableHead.groups()[0] )
            nextTable = JobBiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[1] )
        elif (resultTableContent != None) : 
            nextTable.contents.append( resultTableContent.groups()[1] )
            if ( resultTableContent.groups()[3] != None ) : 
                nextTable.linksTo.append( resultTableContent.groups()[3] )
            else :
                nextTable.linksTo.append( "" )
            if ( resultTableContent.groups()[5] != None ) : 
                nextTable.linksTo.append( resultTableContent.groups()[5] )
            else:
                nextTable.linksTo.append( "" )
    # Last Table insertion
    if (nextTable != None) : 
        localDictionnary[ nextTable.name ] = nextTable 
    ## print( localDictionnary )
    ## print( "Available Tables: " )
    ## for key in localDictionnary : 
    ##     print ( "\t % s" % key )
    return localDictionnary

def selectRandomBiographic() : 
    """Choose randomly an element from a randomly choosen JobBiographicTable. """
    tables          = BiographicDataLoad.loadBiographicsTables()
    for key in tables.keys() : 
        localDictionnary[ key ] = tables[ key ]
    location     = random.choice( localDictionnary.get("Localisation").contents )
    baseTable    = localDictionnary.get("d'Orientation")
    selected     = random.choice( baseTable.linksTo )
    choice       = localDictionnary.get( selected )
    moreselect   = random.choice( choice.contents )
    ## domain       = random.choice( localDictionnary.get("Domaine").contents )
    corporation  = CVData.getRandomCorporationName()
    contractType = CVData.getRandomContractType()
    ## print( selected + "::" + moreselect + " // " + corporation[1] + " ( " + corporation[0] + ", " + contractType + " )" )
    return [selected + " (" + location + ")", moreselect, corporation[1], corporation[0], contractType]

def selectRandomTraining() : 
    """Choose randomly an elements from the Training table. """
    baseTable   = localDictionnary.get("Formation")
    selected    = random.choice( baseTable.contents )
    trainingTAG = "[Formation]"
    if (selected.startswith( trainingTAG ) ) : 
        selected     = selected[len(trainingTAG):]
    domain      = random.choice( localDictionnary.get("Domaine").contents )
    location    = random.choice( localDictionnary.get("Localisation").contents )
    ## print( selected + " // " + domain + " // " + location )
    return [ domain, selected, location ]

def selectRandomSkill() : 
    """Choose randomly an elements from the Skill table. """
    curriculumDataObj = CVData.loadConfig();
    baseTable1 = CVData._instance.hardList
    baseTable2 = CVData._instance.softList 
    selected = random.choice( baseTable1 + baseTable2 )
    ## print( selected )
    return selected.split( "\t" )
