#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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


