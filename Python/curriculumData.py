#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import configparser

def readFileToList( filePath ) : 
    """Read file from path indicated in parameter and return it as a list of lines. """
    listToReturn = []
    with open(filePath, 'r') as file : 
        data         = file.read()
        listToReturn = data.split( "\n" )
        # print( data )
    # print("End of file ", filePath)
    return listToReturn

class CVData( object ) :
    """ Singleton class to regroup datas loaded from configuration. """
    _instance = None

    def __init__(self,
                 cvStyle,
                 cvColor,
                 hardList,
                 softList,
                 jobsList,
                 toolList,
                 firstNameList,
                 lastNameList,
                 contractTypesList,
                 corporationNames,
                 BiographicTables, 
                 BiographicJobs, 
                 uplinkCompanyPartOne,
                 uplinkCompanyPartTwo,
                 uplinkFornames,
                 uplinkSurnames ):
        self.cvStyle                = cvStyle
        self.cvColor                = cvColor
        self.hardList               = hardList
        self.softList               = softList
        self.jobsList               = jobsList
        self.toolList               = toolList
        self.firstNameList          = firstNameList
        self.lastNameList           = lastNameList
        self.contractTypesList      = contractTypesList
        self.corporationNames       = corporationNames
        self.BiographicTables       = BiographicTables
        self.BiographicJobs         = BiographicJobs
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
            print( parser.sections() )
            ## CV style and color !
            cvStyle = parser[ "bases" ].get( "cvStyle" ).split(', ')
            cvColor = parser[ "bases" ].get( "cvColor" ).split(', ')
            ## print ( parser[ "paths" ].get( "hardList" ) )
            hardList                = readFileToList( parser[ "paths" ].get( "hardList" ) )
            softList                = readFileToList( parser[ "paths" ].get( "softList" ) )
            jobsList                = readFileToList( parser[ "paths" ].get( "jobsList" ) )
            toolList                = readFileToList( parser[ "paths" ].get( "toolList" ) )
            firstNameList           = readFileToList( parser[ "paths" ].get( "firstNameList" ) )
            lastNameList            = readFileToList( parser[ "paths" ].get( "lastNameList" ) )
            contractTypesList       = readFileToList( parser[ "paths" ].get( "contractTypesList" ) )
            corporationNames        = readFileToList( parser[ "paths" ].get( "corporationNames" ) )
            BiographicTables        = readFileToList( parser[ "paths" ].get( "BiographicTablesTXT" ) )
            BiographicJobs          = readFileToList( parser[ "paths" ].get( "BiographicJobsTXT" ) )
            ## some other sources
            # uplinkCompanyPartOne  = readFileToList( parser[ "paths" ].get( "uplinkCompanyPartOne" ) )
            # uplinkCompanyPartTwo  = readFileToList( parser[ "paths" ].get( "uplinkCompanyPartTwo" ) )
            # uplinkFornames        = readFileToList( parser[ "paths" ].get( "uplinkFornames" ) )
            # uplinkSurnames        = readFileToList( parser[ "paths" ].get( "uplinkSurnames" ) )
            uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames = [], [], [], []
            self._instance = CVData( cvStyle, cvColor, hardList, softList, jobsList, toolList, 
                            firstNameList, lastNameList, contractTypesList, corporationNames, 
                            BiographicTables, BiographicJobs, 
                            uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames )
        ## print( self._instance.corporationNames )
        return self._instance

