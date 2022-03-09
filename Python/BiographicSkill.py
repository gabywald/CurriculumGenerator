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


