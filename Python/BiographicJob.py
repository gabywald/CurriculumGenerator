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


