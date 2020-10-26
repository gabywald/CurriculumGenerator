#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import sys, getopt, os, subprocess

import argparse
## from argparse import ArgumentParser

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

## Below is reading from arguments

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
    ## print( args )
    return args
    