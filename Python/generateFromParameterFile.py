#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020, 2022)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0a"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Main script to generate several Curriculum according to file passed in parameter

import os
import sys
import shutil
import glob
import subprocess

from pathlib import Path

import ModuleHelper

from Person import Person

def is_integer( n ):
  try:
    res = int( n )
    return True
  except ValueError:
    ## print ("not int: " + n )
    return False

print('(debugging purposes) Number of arguments:', len(sys.argv), 'arguments.' )
print('(debugging purposes) Argument List:', str(sys.argv) )

if (len(sys.argv) < 2):
  print("Please gives one argument: path to the file !")
  exit(1)

path2file = sys.argv[1]

fileContent = ModuleHelper.readFileToList( path2file );

## print( fileContent )

for line in fileContent : 
  if ( ( not line.startswith( "#" ) ) and (line != "") ) :
    lineSplitter = line.split( "\t" )
    cvStyle = lineSplitter[ 0 ]
    cvColor = lineSplitter[ 1 ]
    ## skills = lineSplitter[10], 
    ## jobs = lineSplitter[11], 
    ## trainings = lineSplitter[12]
    nbskills = 0
    nbjobs = 0
    nbtrainings = 0
    lstskills = []
    lstjobs = []
    lsttrainings = []
    isbiographic = False
    ## Parsing ListS {Skillms;Jobs;Trainings} !
    if (is_integer( lineSplitter[14] ) ) : 
      nbskills = int( lineSplitter[14] )
    else : 
      lstskills = lineSplitter[14].split( ";" )
      ## print( lstskills )
    if (is_integer( lineSplitter[15] ) ) : 
      nbjobs = int( lineSplitter[15] )
    elif (lineSplitter[11] == "BIO" ) : 
      isbiographic = True
    else : 
      lstjobs = lineSplitter[15].split( ";" )
      ## print( lstjobs )
    if (is_integer( lineSplitter[16] ) ) : 
      nbtrainings = int( lineSplitter[16] )
    elif (lineSplitter[12] == "BIO" ) : 
      isbiographic = True
    else : 
      lsttrainings = lineSplitter[16].split( ";" )
      ## print( lsttrainings )
    ## Instanciate Person !
    personnae = Person( 
      firstname = lineSplitter[2], 
      lastname = lineSplitter[3], 
      extrainfo = lineSplitter[4], 
      address = lineSplitter[5], 
      pseudo = lineSplitter[6], 
      webpage = lineSplitter[7], 
      email = lineSplitter[8], 
      quote = lineSplitter[9], 
      generaltitle = lineSplitter[10], 
      title = lineSplitter[11], 
      speciality = lineSplitter[12], 
      cellphone = lineSplitter[13], 
      jobeltsnb = nbjobs, 
      trainingeltsnb = nbtrainings, 
      skilleltnb = nbskills, 
      skills = lstskills, 
      jobs = lstjobs, 
      trainings = lsttrainings )
    print( personnae )
    ## Build Command to call build of Curriculum !
    cmd = "./generateCurriculum.py "
    cmd += "--style %s --color %s " %(cvStyle, cvColor)
    cmd += "-fn %s -ln %s " %(personnae.firstname, personnae.lastname)
    cmd += "--email %s --pseudo %s " %(personnae.email, personnae.pseudo)
    cmd += "--webpage %s --address \"%s\" " %(personnae.webpage, personnae.address)
    cmd += "--quote \"%s\" --extrainfo \"%s\" " %(personnae.quote, personnae.extrainfo)
    cmd += "--generaltitle \"%s\" " %( personnae.generaltitle )
    cmd += "--title \"%s\" " %( personnae.title )
    cmd += "--speciality \"%s\" " %( personnae.speciality )
    cmd += "--cellphone \"%s\" " %( personnae.cellphone )
    if ( len( personnae.skills ) != 0) : 
      cmd += "-lse \"%s\" " %( ";".join(personnae.skills) )
    if ( len( personnae.jobs ) != 0) :
      cmd += "-lje \"%s\" " %( ";".join(personnae.jobs) )
    if ( len( personnae.trainings ) != 0) :
      cmd += "-lte \"%s\" " %( ";".join(personnae.trainings) )
    if (isbiographic) : 
      cmd += "--skillelements %d " %( personnae.skilleltnb )
      cmd += "--biographic "
    elif ( (personnae.jobeltsnb != 0) 
        and (personnae.trainingeltsnb != 0) 
        and (personnae.skilleltnb != 0) ) : 
      cmd += "--jobelements %d " %( personnae.jobeltsnb )
      cmd += "--trainingelements %d " %( personnae.trainingeltsnb )
      cmd += "--skillelements %d " %( personnae.skilleltnb )
      cmd += "--allyes "
    else:
      cmd += ""
    cmd += "--make "
    print ( cmd + "\n" )
    retcode = subprocess.call( cmd, shell=True )
    personnae = None

directory4outputs = "generated/"
path = Path( directory4outputs )
if ( path.exists() ) :
  shutil.rmtree( directory4outputs )
os.mkdir( directory4outputs )

listing = glob.glob( "*_generate/*.pdf" )
print( listing )
for pdffile in listing:
  shutil.copy(pdffile, directory4outputs)

listing2remove = glob.glob( "*_generate/" )
for dir2rm in listing2remove : 
  subprocess.call( dir2rm, shell=True )

