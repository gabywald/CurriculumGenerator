#!/usr/bin/python3
# -*- coding: utf-8 -*- 

__author__		= "Gabriel Chandesris (2020)"
__copyright__	= "CC Gabriel Chandesris (2020)"
__credits__		= ""
__licence__		= "GNU GENERAL PUBLIC LICENSE v3"
__version__		= "0.1.0"
__maintainer__	= "Gabriel Chandesris"
__email__		= "gabywald[at]laposte.net"
__contact__		= "gabywald[at]laposte.net"
__status__		= "Development"

import curriculumData
from curriculumData import CVData
import re

class BiographicTable( object ) : 
	def __init__(self, name = None, comments = None ):
		self.name			= name
		self.comments		= comments
		self.contents		= []
		self.linksTo		= []
		self.addins			= []
	
	def _get_kwargs(self):
		names = [
			'name',
			'comments',
			'contents',
			'linksTo',
			'addins'
		]
		return [(name, getattr(self, name)) for name in names]
	
	def __str__(self) : 
		str = "BiographicTable ( % s , % s ) \n"  % (self.name, self.comments)
		str += "\t contents: %s \n" % (self.contents)
		return str

class BiographicElement( object ) : 
	def __init__(self, content, comments ):
		self.content		= content
		self.addins			= []
	
	def _get_kwargs(self):
		names = [
			'content',
			'addins'
		]
		return [(name, getattr(self, name)) for name in names]

biographictablesDict = {}

def loadTables() : 
	curriculumDataObj = CVData.loadConfig();
	tablesAsTXT = curriculumDataObj.BiographicTables
	nextTable	= None
	for line in tablesAsTXT:
		## print( line )
		resultTableHead		= re.match( "^Table (.*?)(\t(.*?))?$", line)
		resultTableContent	= re.match( "^\t(Table )?(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$", line )
		if (resultTableHead != None) : 
			if (nextTable != None) : 
				biographictablesDict[ nextTable.name ] = nextTable
			## print( resultTableHead.groups() )
			## print( resultTableHead.groups()[0] )
			nextTable = BiographicTable( resultTableHead.groups()[0], resultTableHead.groups()[1] )
		elif (resultTableContent != None) : 
			## print( resultTableContent.groups() )
			nextTable.contents.append( resultTableContent.groups()[1] )
			nextTable.linksTo.append( resultTableContent.groups()[3] ) if ( resultTableContent.groups()[3] != None ) else nextTable.linksTo.append( "" )
			nextTable.linksTo.append( resultTableContent.groups()[5] ) if ( resultTableContent.groups()[5] != None ) else nextTable.linksTo.append( "" )
	# Last Table insertion
	if (nextTable != None) : 
		biographictablesDict[ nextTable.name ] = nextTable 
	## print( biographictablesDict )
	print( "Available Tables: " )
	for key in biographictablesDict : 
		print ( "\t % s" % key )

import random

def selectRandomBiographic() : 
	baseTable	= biographictablesDict.get("CurriculumGenerator")
	selected	= random.choice( baseTable.contents )
	choice		= biographictablesDict.get( selected )
	print ( selected + " => ... " )
	moreselect	= random.choice( choice.contents )
	domain		= random.choice( biographictablesDict.get("Domaine").contents )
	print( selected + "::" + moreselect + " // " + domain)
	return [selected, moreselect, domain]

def selectRandomTraining() : 
	baseTable	= biographictablesDict.get("Formation")
	selected	= random.choice( baseTable.contents )
	print ( selected + " => ... " )
	domain		= random.choice( biographictablesDict.get("Domaine").contents )
	print( selected + "// " + domain)
	return [selected, domain]


