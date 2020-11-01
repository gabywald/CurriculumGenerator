#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import curriculumData
from curriculumData import CVData
import re
import random

class BiographicTable( object ) : 
    """This class defines Tables Definitions for 'biographic' elements for Curriculum generation. """
    
    def __init__(self, name = None, comments = None ):
        """BiographicTable Constructor. """
        self.name = name
        self.comments = comments
        self.contents = []
        self.linksTo  = []
        self.addins   = []
    
    def __str__(self) : 
        """BiographicTable to str. """
        str = "BiographicTable ( % s , % s ) \n"  % (self.name, self.comments)
        str += "\t contents: %s \n" % (self.contents)
        return str

class BiographicElement( object ) : 
    def __init__(self, content, comments ):
        self.content    = content
        self.addins     = []

# A dictionnary of BiographicTable
biographictablesDict = {}

def loadTables() : 
    """Load BiographicTables from the configuration. """
    curriculumDataObj = CVData.loadConfig();
    tablesAsTXT  = curriculumDataObj.BiographicTables
    nextTable    = None
    for line in tablesAsTXT:
        resultTableHead       = re.match( "^Table (.*?)(\t(.*?))?$", line)
        resultTableContent    = re.match( "^\t(Table )?(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
        if (resultTableHead != None) : 
            if (nextTable != None) : 
                biographictablesDict[ nextTable.name ] = nextTable
            ## print( resultTableHead.groups() )
            ## print( resultTableHead.groups()[0] )
            nextTable = BiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[1] )
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
        biographictablesDict[ nextTable.name ] = nextTable 
    ## print( biographictablesDict )
    print( "Available Tables: " )
    for key in biographictablesDict : 
        print ( "\t % s" % key )

def selectRandomBiographic() : 
    """Choose randomly an element from a randomly choosen BiographicTable. """
    baseTable    = biographictablesDict.get("CurriculumGenerator")
    selected     = random.choice( baseTable.contents )
    choice       = biographictablesDict.get( selected )
    moreselect   = random.choice( choice.contents )
    domain       = random.choice( biographictablesDict.get("Domaine").contents )
    print( selected + "::" + moreselect + " // " + domain)
    return [selected, moreselect, domain]

def selectRandomTraining() : 
    """Choose randomly an elements from the Training table. """
    baseTable   = biographictablesDict.get("Formation")
    selected    = random.choice( baseTable.contents )
    domain      = random.choice( biographictablesDict.get("Domaine").contents )
    print( selected + "// " + domain)
    return [selected, domain]

def selectRandomSkill() : 
    """Choose randomly an elements from the Skill table. """
    curriculumDataObj = CVData.loadConfig();
    baseTable1 = CVData._instance.hardList
    baseTable2 = CVData._instance.softList 
    selected = random.choice( baseTable1 + baseTable2 )
    print( selected )
    return selected
