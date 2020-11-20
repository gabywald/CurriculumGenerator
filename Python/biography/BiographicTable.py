#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import ModuleHelper
import re
import random

class BiographicTable( object ) : 
    """This class defines Tables Definitions for 'biographic' elements for Curriculum generation. """
    _tables = None
    _equipments = None
    _jobsToSkills = None
    _skills = None
    
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
        str += "\t linksTo: %s \n" % (self.linksTo)
        str += "\t addins: %s \n" % (self.addins)
        return str
    
    def appendContent( self, content) : 
        self.contents.append( content )
    
    def appendLinks( self, link) : 
        self.linksTo.append( link )
    
    def appendAddin( self, addin) : 
        self.addins.append( addin )
    
    @classmethod
    def subLoad( self, tables, fileInConfig ) : 
        """Sub Function to load tables !"""
        if (tables != None) : 
            return tables
        tables = {}
        data = ModuleHelper.loadFileConfig( fileInConfig )
        nextTable = None
        nextSubTable = None
        for line in data : 
            resultTableHead = re.match( "^Table (.*?)(\t(.*?))?(\t(.*?))?$", line)
            resultTableContent = re.match( "^\t(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
            if (resultTableHead != None) : 
                if (nextTable != None) : 
                    tables[ nextTable.name ] = nextTable
                nextTable = BiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[2] )
                ## print ( resultTableHead.groups() )
            elif (resultTableContent != None) : 
                nextTable.appendContent( resultTableContent.groups()[0] );
                nextTable.appendLinks( resultTableContent.groups()[2] );
                nextTable.appendAddin( resultTableContent.groups()[4] );
        if (nextTable != None) : 
            tables[ nextTable.name ] = nextTable 
        return tables
    
    @classmethod
    def loadBiographicsTables( self ) : 
        """Load / Return Biographic Tables"""
        return self.subLoad( self._tables, "biographyCyberAge" )
    
    @classmethod
    def loadEquipmentTables( self ) : 
        """Load / Return Equipment Tables"""
        return self.subLoad( self._equipments, "tableEquipementsCyberAge" )
    
    @classmethod
    def loadJobsToSkills( self ) : 
        if (self._jobsToSkills != None) : 
            return self._jobsToSkills
        self._jobsToSkills = {}
        data = ModuleHelper.loadFileConfig( "metiersEtTalentsCyberAge" )
        nextTable = None
        for line in data : 
            resultTableHead = re.match( "^(.*?)\t(.*?)$", line)
            if (resultTableHead != None) : 
                if (nextTable != None) : 
                    self._jobsToSkills[ nextTable.name ] = nextTable
                nextTable = BiographicJob( resultTableHead.groups()[0], \
                                           resultTableHead.groups()[1].split( ";" ) )
        if (nextTable != None) : 
            self._jobsToSkills[ nextTable.name ] = nextTable 
        return self._jobsToSkills
    
    @classmethod
    def loadSkills( self ) : 
        if (self._skills != None) : 
            return self._skills
        self._skills = {}
        data = ModuleHelper.loadFileConfig( "talentsCyberAge" )
        nextTable = None
        for line in data : 
            resultTableHead = re.match( "^(.*?)\t(.*?)(\t\[(.*?)\])?$", line)
            if (resultTableHead != None) : 
                if (nextTable != None) : 
                    self._skills[ nextTable.name ] = nextTable
                values = None 
                if (resultTableHead.groups()[3] != None) : 
                    values = resultTableHead.groups()[3].split( ";" )
                nextTable = BiographicSkill( resultTableHead.groups()[0], \
                                             resultTableHead.groups()[1], \
                                             values )
        if (nextTable != None) : 
            self._skills[ nextTable.name ] = nextTable 
        return self._skills

class BiographicElement( object ) : 
    """This class defines Selected Biographic Elements choosen from BioGraphic Tables """
    def __init__(self, name ):
        self.contents = []
        self.contents.append( name )
        self.addins = []
    
    def __str__(self) : 
        """BiographicElement to str. """
        str = "BiographicElement() \n" 
        str += "\t contents: %s \n" % (self.contents)
        str += "\t addins: %s \n" % (self.addins)
        return str

class BiographicJob( object ) : 
    """This class defines Biographic Jobs and related Skills """
    def __init__(self, name = None, skills = None ):
        """BiographicJob Constructor. """
        self.name = name
        self.skills = skills
    
    def __str__(self) : 
        """BiographicJob to str. """
        str = "BiographicJob() \n" 
        str += "\t name: %s \n" % (self.name)
        str += "\t skills: %s \n" % (self.skills)
        return str

class BiographicSkill( object ) : 
    """This class defines Biographic Skills """
    def __init__(self, name = None, level = None, possibilities = None ):
        """BiographicSkill Constructor. """
        self.name = name
        self.level = level
        self.possibilities = possibilities
    
    def __str__(self) : 
        """BiographicSkill to str. """
        str = "BiographicSkill() \n" 
        str += "\t name: %s \n" % (self.name)
        str += "\t level: %s \n" % (self.level)
        str += "\t possibilities: %s \n" % (self.possibilities)
        return str

def selectRandomBiographic( tables ) : 
    """Choose randomly an element from a randomly choosen BiographicTable. """
    orientation = tables[ "d'Orientation" ]
    ## print( orientation )
    bioELT = None
    while (orientation != None) : 
        contents = orientation.contents
        links = orientation.linksTo
        addins = orientation.addins
        index = random.randint(0, len(contents) - 1 )
        ## print( "%d (%d, %d, %d)" %( index, len(contents), len(links), len(addins) ) )
        content = contents[index]
        link = links[index]
        addin = addins[index]
        ## ## ## Generate / complete a BiographicElement 
        if (bioELT == None) : 
            bioELT = BiographicElement( content )
        else : 
            bioELT.contents.append( content )
        if (addin != None) : 
            bioELT.addins = addin.split( ";" )
        if (link != None) : 
            if (link == "Cicatrices") : 
                orientation = tables[ "Cicatrices-localisation" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = tables[ "Cicatrices-gravité" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = None;
            else:
                orientation = tables[ link ];
        else : 
            orientation = None
    ## print( bioELT )
    return bioELT

def selectBiographicElements( number ) : 
    results = []
    tables = BiographicTable.loadBiographicsTables()
    for i in range(0, number) : 
        results.append( selectRandomBiographic( tables ) )
    return results
