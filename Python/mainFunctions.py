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

def readFileToList( filePath ) : 
	listToReturn = []
	with open(filePath, 'r') as file : 
		data = file.read()
		listToReturn = data.split( "\n" )
		# print( data )
	print("End of file ", filePath)
	return listToReturn

import sys, getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print('Input file is "', inputfile)
	print('Output file is "', outputfile)

if __name__ == "__main__":
	pass
	# main(sys.argv[1:])
	