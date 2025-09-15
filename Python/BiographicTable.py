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
    str += "\t linksTo: %s \n" % (self.linksTo)
    str += "\t addins: %s \n" % (self.addins)
    return str
  
  def appendContent( self, content) : 
    self.contents.append( content )
  
  def appendLinks( self, link) : 
    self.linksTo.append( link )
  
  def appendAddin( self, addin) : 
    self.addins.append( addin )
  
