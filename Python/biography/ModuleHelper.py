#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Notes : https://docs.python.org/3/library/configparser.html
import configparser

def readFileToList( filePath ) : 
    """Read file from path indicated in parameter and return it as a list of lines. """
    listToReturn = []
    with open(filePath, 'r') as file : 
        data         = file.read()
        listToReturn = data.split( "\n" )
    return listToReturn

def loadConfig( nameOfRSC ) : 
    ## Use a configuration file ! 'sources.ini' !
    parser = configparser.ConfigParser()
    parser.read( "sources.ini" )
    if parser.has_option('paths', nameOfRSC):
        return readFileToList( parser[ "paths" ].get( nameOfRSC ) )
    else:
        return []
