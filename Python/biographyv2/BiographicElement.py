#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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


