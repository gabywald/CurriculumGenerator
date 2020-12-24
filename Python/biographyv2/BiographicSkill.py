#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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


