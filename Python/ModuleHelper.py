#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020, 2022)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0a"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## Notes : https://docs.python.org/3/library/configparser.html
import configparser

def readFileToList( filePath ) : 
  """Read file from path indicated in parameter and return it as a list of lines. """
  listToReturn = []
  with open(filePath, 'r') as file : 
    data     = file.read()
    listToReturn = data.split( "\n" )
  return listToReturn

def loadFileConfig( nameOfRSC ) : 
  """ To read file resources ! """
  ## Use a configuration file ! 'sources.ini' !
  parser = configparser.ConfigParser()
  parser.read( "sources.ini" )
  if parser.has_option('paths', nameOfRSC):
    return readFileToList( parser[ "paths" ].get( nameOfRSC ) )
  else:
    return []
    
def loadDataConfig( nameOfRSC ) : 
  """ To read data resources ! """
  ## Use a configuration file ! 'sources.ini' !
  parser = configparser.ConfigParser()
  parser.read( "sources.ini" )
  if parser.has_option('data', nameOfRSC):
    return parser[ "data" ].get( nameOfRSC )[2:-2].split( ", " )
  else:
    return []
