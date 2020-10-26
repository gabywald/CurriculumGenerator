#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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