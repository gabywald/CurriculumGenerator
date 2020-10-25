#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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

class CVData( object ) :
	_instance = None

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
				 BiographicTables, 
				 BiographicJobs, 
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
		self.BiographicTables		= BiographicTables
		self.BiographicJobs			= BiographicJobs
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
			'contractTypesList', 
			'corporationNames',
			'BiographicTables',
			'BiographicJobs',
			'uplinkCompanyPartOne',
			'uplinkCompanyPartTwo',
			'uplinkFornames',
			'uplinkSurnames'
		]
		return [(name, getattr(self, name)) for name in names]

	@classmethod
	def loadConfig( self ) : 
		if self._instance is None : 
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
			firstNameList			= readFileToList( parser[ "paths" ].get( "firstNameList" ) )
			lastNameList			= readFileToList( parser[ "paths" ].get( "lastNameList" ) )
			contractTypesList		= readFileToList( parser[ "paths" ].get( "contractTypesList" ) )
			corporationNames		= readFileToList( parser[ "paths" ].get( "corporationNames" ) )
			BiographicTables		= readFileToList( parser[ "paths" ].get( "BiographicTablesTXT" ) )
			BiographicJobs			= readFileToList( parser[ "paths" ].get( "BiographicJobsTXT" ) )
			## some other sources
			# uplinkCompanyPartOne	= readFileToList( parser[ "paths" ].get( "uplinkCompanyPartOne" ) )
			# uplinkCompanyPartTwo	= readFileToList( parser[ "paths" ].get( "uplinkCompanyPartTwo" ) )
			# uplinkFornames		= readFileToList( parser[ "paths" ].get( "uplinkFornames" ) )
			# uplinkSurnames		= readFileToList( parser[ "paths" ].get( "uplinkSurnames" ) )
			uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames = [], [], [], []
			self._instance = CVData( cvStyle, cvColor, hardList, softList, jobsList, toolList, 
							firstNameList, lastNameList, contractTypesList, corporationNames, 
							BiographicTables, BiographicJobs, 
							uplinkCompanyPartOne, uplinkCompanyPartTwo, uplinkFornames, uplinkSurnames )
		## print( self._instance.corporationNames )
		return self._instance

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
parser.add_argument("-em", "--email", 
	help = "E-Mail", 
	type=str )
parser.add_argument("-ps", "--pseudo", 
	help = "Pseudonym", 
	type=str )
parser.add_argument("-wp", "--webpage", 
	help = "Web Page / URL", 
	type=str )
parser.add_argument("-ad", "--address", 
	help = "Address (IRL)", 
	type=str )
parser.add_argument("-qc", "--quote", 
	help = "Quote / Citation", 
	type=str )
	
parser.add_argument("-je", "--jobelements", 
	help = "Number of JOBS Elements", 
	type=int )
	
parser.add_argument("-te", "--trainingelements", 
	help = "Number of TRAINING Elements", 
	type=int )

parser.add_argument("-rje", "--randomjobelements", 
	help = "Random number of JOB elements", 
	action = "store_true" )

parser.add_argument("-rte", "--randomtrainingelements", 
	help = "Random number of TRAINING elements", 
	action = "store_true" )

parser.add_argument("-nq", "--noquote", 
	help = "NO quote / Citation", 
	action = "store_true" )

parser.add_argument("-m", "--make", 
	help = "Launch Making of PDF from TeX file", 
	action = "store_true" )

def parsingArgs() :
	args = parser.parse_args()
	print( args )
	return args
