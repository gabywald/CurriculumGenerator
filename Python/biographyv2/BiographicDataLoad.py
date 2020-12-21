#!/usr/bin/python3
# -*- coding: utf-8 -*-

import ModuleHelper
import re
import random

from BiographicTable import BiographicTable
from BiographicJob import BiographicJob
from BiographicSkill import BiographicSkill

class BiographicDataLoad( object ) : 
    """ Data Loader for Biographic Data ! """
    _tables = None
    _equipments = None
    _jobsToSkills = None
    _skills = None
   
    def __init__(self, name = None, filepath = None ):
        """BiographicTable Constructor. """
        self.name = name
        self.filepath = filepath
        self.datalist = []
        
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


