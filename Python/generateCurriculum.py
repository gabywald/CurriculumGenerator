#!/usr/bin/python3
# -*- coding: utf-8 -*- default is unicode in python3 ?

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0a"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

## ## ## ## ## Main Script to generate a Curriculum, according to parameters indicated !

import sys
import shutil
import random

import CurriculumArgumentsParsing
import CurriculumLaTeXGenerator

from Person import Person

from BiographicSelection import selectRandomBiographic
from BiographicSelection import selectBiographicElements
from BiographicSelection import preparingBiographicElements
from BiographicSelection import addskill
from BiographicSelection import reworking
from BiographicDataLoad import BiographicDataLoad

## print('(debugging purposes) Number of arguments:', len(sys.argv), 'arguments.' )
## print('(debugging purposes) Argument List:', str(sys.argv) )

args = CurriculumArgumentsParsing.parsingArgs()

personnae = Person()

CurriculumArgumentsParsing.interactiveCompletionOf( personnae, args )
if (args.biographic) :
    print( "Biographic Curriculum Generation" )
    numberOfResults = 0
    if (personnae.skilleltnb != None) : 
        numberOfResults += personnae.skilleltnb
    if (personnae.trainingeltsnb != None) : 
        numberOfResults += personnae.trainingeltsnb
    if (personnae.trainingeltsnb != None) : 
        numberOfResults += personnae.jobeltsnb
    res = selectBiographicElements( numberOfResults )
    personnae = preparingBiographicElements( res, personnae )
    reworking( personnae )
else : 
    print( "NON-biographic Curriculum Generation !!" )
    CurriculumArgumentsParsing.interactiveCompletionSkillsJobsTraining( personnae, args )

## final show !!
print( personnae )
texcurriculumDirectory = CurriculumLaTeXGenerator.generateLaTeX( personnae, args.color, args.style )
## Compiling TeX file to obtain PDF !
if args.make : 
    CurriculumLaTeXGenerator.launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

print("End of script")
