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


