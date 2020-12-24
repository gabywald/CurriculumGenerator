#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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
    
