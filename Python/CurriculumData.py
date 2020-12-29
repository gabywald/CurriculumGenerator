#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import configparser
import random

import ModuleHelper

from BiographicDataLoad import BiographicDataLoad

class CVData( object ) :
    """ Singleton class to regroup datas loaded from configuration. """
    _instance = None

    def __init__(self,
                 cvStyle,
                 cvColor,
                 hardList,
                 softList,
                 firstNameList,
                 lastNameList,
                 contractTypesList,
                 corporationNames,
                 corporationDomains,
                 uplinkCompanyPartOne,
                 uplinkCompanyPartTwo,
                 uplinkFornames,
                 uplinkSurnames ):
        self.cvStyle                = cvStyle
        self.cvColor                = cvColor
        self.hardList               = hardList
        self.softList               = softList
        self.firstNameList          = firstNameList
        self.lastNameList           = lastNameList
        self.contractTypesList      = contractTypesList
        self.corporationNames       = corporationNames
        self.corporationDomains     = corporationDomains
        self.uplinkCompanyPartOne   = uplinkCompanyPartOne
        self.uplinkCompanyPartTwo   = uplinkCompanyPartTwo
        self.uplinkFornames         = uplinkFornames
        self.uplinkSurnames         = uplinkSurnames

    @classmethod
    def loadConfig( self ) : 
        if self._instance is None : 
            ## Use a configuration file ! 'sources.ini' !
            parser = configparser.ConfigParser()
            parser.read( "sources.ini" )
            # print( parser.sections() )
            ## CV style and color !
            cvStyle = parser[ "bases" ].get( "cvStyle" ).split(', ')
            cvColor = parser[ "bases" ].get( "cvColor" ).split(', ')
            ## print ( parser[ "paths" ].get( "hardList" ) )
            hardList                = ModuleHelper.readFileToList( parser[ "paths" ].get( "hardList" ) )
            softList                = ModuleHelper.readFileToList( parser[ "paths" ].get( "softList" ) )
            firstNameList           = ModuleHelper.readFileToList( parser[ "paths" ].get( "firstNameList" ) )
            lastNameList            = ModuleHelper.readFileToList( parser[ "paths" ].get( "lastNameList" ) )
            contractTypesList       = ModuleHelper.readFileToList( parser[ "paths" ].get( "contractTypesList" ) )
            corporationNames        = ModuleHelper.readFileToList( parser[ "paths" ].get( "corporationNames" ) )
            corporationDomains      = ModuleHelper.readFileToList( parser[ "paths" ].get( "corporationDomains" ) )
            ## some other sources
            uplinkCompanyPartOne = ModuleHelper.readFileToList( parser[ "paths" ].get( "uplinkCompanyPartOne" ) )
            uplinkCompanyPartTwo = ModuleHelper.readFileToList( parser[ "paths" ].get( "uplinkCompanyPartTwo" ) )
            # uplinkFornames = ModuleHelper.readFileToList( parser[ "paths" ].get( "uplinkFornames" ) )
            # uplinkSurnames = ModuleHelper.readFileToList( parser[ "paths" ].get( "uplinkSurnames" ) )
            ## uplinkCompanyPartOne, uplinkCompanyPartTwo = [], []
            uplinkFornames, uplinkSurnames = [], []
            self._instance = CVData( cvStyle, cvColor, hardList, softList, 
                            firstNameList, lastNameList, contractTypesList, 
                            corporationNames, corporationDomains, 
                            uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames )
        ## print( self._instance.corporationNames )
        return self._instance
    
    @classmethod
    def getRandomCorporationName( self ) : 
        if (random.randint(1, 100) % 2 == 0) : 
            return random.choice( self._instance.corporationNames ).split( "\t" )
        else : 
    	    elt1 = random.choice( self._instance.uplinkCompanyPartOne ) \
    	        + " " + random.choice( self._instance.uplinkCompanyPartTwo )
    	    elt2 = random.choice( self._instance.corporationDomains )
    	    return [ elt1, elt2 ]
    
    @classmethod
    def getRandomContractType( self ) : 
        return random.choice( self._instance.contractTypesList )
    
    @classmethod
    def getRandomJob( self ) : 
        selection = BiographicDataLoad.loadJobsToSkills()
        choiceToMakeInside = list(selection.keys())
        generalTitle = random.choice( choiceToMakeInside )
        title = generalTitle
        speciality = random.choice( selection[ generalTitle ].skills )
        return [ generalTitle, title, speciality ]
