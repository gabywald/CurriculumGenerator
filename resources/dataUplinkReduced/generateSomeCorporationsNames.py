#!/usr/bin/python3
# -*- coding: utf-8 -*- ## useless in python 3 ? ; default is unicode ?

__author__		= "Gabriel Chandesris (2020)"
__copyright__	= "CC Gabriel Chandesris (2020)"
__credits__		= ""
__licence__		= "GNU GENERAL PUBLIC LICENSE v3"
__version__		= "0.1.0"
__maintainer__	= "Gabriel Chandesris"
__email__		= "gabywald[at]laposte.net"
__contact__		= "gabywald[at]laposte.net"
__status__		= "Development"

import random

def readFileToList( filePath ) : 
	listToReturn = []
	with open(filePath, 'r') as file : 
		data = file.read()
		listToReturn = data.split( "\n" )
	return listToReturn

uplinkCompanyPartOne	= readFileToList( "companyPart1.txt" )
uplinkCompanyPartTwo	= readFileToList( "companyPart2.txt" )

for i in range( 10 ):
	print( random.choice( uplinkCompanyPartOne ) + " " + random.choice( uplinkCompanyPartTwo ) )

