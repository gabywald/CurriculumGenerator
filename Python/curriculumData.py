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

import configparser

import argparse
## from argparse import ArgumentParser

def readFileToList( filePath ) : 
	listToReturn = []
	with open(filePath, 'r') as file : 
		data = file.read()
		listToReturn = data.split( "\n" )
		# print( data )
	print("End of file ", filePath)
	return listToReturn

class CVData() :
	def __init__(self,
				 cvStyle,
				 cvColor,
				 hardList,
				 softList,
				 jobsList,
				 toolList,
				 firstNameList,
				 lastNameList,
				 contractTypesList,
				 corporationNames,
				 uplinkCompanyPartOne,
				 uplinkCompanyPartTwo,
				 uplinkFornames,
				 uplinkSurnames ):
		self.cvStyle				= cvStyle
		self.cvColor				= cvColor
		self.hardList				= hardList
		self.softList				= softList
		self.jobsList				= jobsList
		self.toolList				= toolList
		self.firstNameList			= firstNameList
		self.lastNameList			= lastNameList
		self.contractTypesList		= contractTypesList
		self.corporationNames		= corporationNames
		self.uplinkCompanyPartOne	= uplinkCompanyPartOne
		self.uplinkCompanyPartTwo	= uplinkCompanyPartTwo
		self.uplinkFornames			= uplinkFornames
		self.uplinkSurnames			= uplinkSurnames

	def _get_kwargs(self):
		names = [
			'cvStyle',
			'cvColor',
			'hardList',
			'softList',
			'jobsList',
			'toolList',
			'firstNameList',
			'lastNameList',
			'contractTypesList'
			'corporationNames',
			'uplinkCompanyPartOne',
			'uplinkCompanyPartTwo',
			'uplinkFornames',
			'uplinkSurnames'
		]
		return [(name, getattr(self, name)) for name in names]

def loadConfig() : 
	## Use a configuration file ! 'sources.ini' !
	parser = configparser.ConfigParser()
	parser.read( "sources.ini" )
	print( parser.sections() )
	## CV style and color !
	cvStyle = parser[ "bases" ].get( "cvStyle" ).split(', ')
	cvColor = parser[ "bases" ].get( "cvColor" ).split(', ')
	## print ( parser[ "paths" ].get( "hardList" ) )
	hardList				= readFileToList( parser[ "paths" ].get( "hardList" ) )
	softList				= readFileToList( parser[ "paths" ].get( "softList" ) )
	jobsList				= readFileToList( parser[ "paths" ].get( "jobsList" ) )
	toolList				= readFileToList( parser[ "paths" ].get( "toolList" ) )
	firstNameList		= readFileToList( parser[ "paths" ].get( "firstNameList" ) )
	lastNameList		= readFileToList( parser[ "paths" ].get( "lastNameList" ) )
	contractTypesList	= readFileToList( parser[ "paths" ].get( "contractTypesList" ) )
	corporationNames	= readFileToList( parser[ "paths" ].get( "corporationNames" ) )
	## some other sources
	# uplinkCompanyPartOne	= readFileToList( parser[ "paths" ].get( "uplinkCompanyPartOne" ) )
	# uplinkCompanyPartTwo	= readFileToList( parser[ "paths" ].get( "uplinkCompanyPartTwo" ) )
	# uplinkFornames		= readFileToList( parser[ "paths" ].get( "uplinkFornames" ) )
	# uplinkSurnames		= readFileToList( parser[ "paths" ].get( "uplinkSurnames" ) )
	uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames = [], [], [], []
	return CVData( cvStyle, cvColor, hardList, softList, jobsList, toolList, 
					firstNameList, lastNameList, contractTypesList, corporationNames, 
					uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames )

parser = argparse.ArgumentParser(
	prog = 'Curriculum Generator', 
	description = """BEGINNING of help""", 
	epilog = """END of help""" )

# Some arguments ... 
parser.add_argument("-s", "--style", 
	help = "ModernCV Style", 
	choices = [ 'classic', 'casual', 'oldstyle', 'banking' ], 
	default = "classic", 
	type=str )
parser.add_argument("-c", "--color", 
	help = "ModernCV Color", 
	choices = [ 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black' ], 
	default = "blue", 
	type=str )

parser.add_argument("-rs", "--randomstyle", 
	help = "Random ModernCV Color", 
	action = "store_true" )
parser.add_argument("-rc", "--randomcolor", 
	help = "Random ModernCV Color", 
	action = "store_true" )
	
parser.add_argument("-rfn", "--randomfirstname", 
	help = "Random First Name", 
	action = "store_true" )
parser.add_argument("-rln", "--randomlastname", 
	help = "Random Last Name", 
	action = "store_true" )
	
parser.add_argument("-fn", "--firstname", 
	help = "First Name", 
	type=str )
parser.add_argument("-ln", "--lastname", 
	help = "Last Name", 
	type=str )

parser.add_argument("-m", "--make", 
	help = "Launch Making of PDF from TeX file", 
	action = "store_true" )

def parsingArgs() :
	args = parser.parse_args()
	print( args )
	return args

## TODO random generation according to arguments !!

