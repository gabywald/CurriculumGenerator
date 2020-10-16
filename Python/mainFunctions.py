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

import sys, getopt, os, subprocess

def launcheMakePDFfromLaTeX( directory ) : 
	print( "Changing dir to {" + directory + "}..." )
	os.chdir( directory )
	print( "Compiling TeX file to PDF..." )
	retcode = subprocess.call( "make", shell=True )
	print( retcode )
	print( "Cleaning..." )
	retcode2 = subprocess.call( "make clean", shell=True )
	print( retcode2 )
	print( "Changing dir BACK..." )
	os.chdir( ".." )	