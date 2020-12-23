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
from CurriculumData import CVData

## print('(debugging purposes) Number of arguments:', len(sys.argv), 'arguments.' )
## print('(debugging purposes) Argument List:', str(sys.argv) )

args = CurriculumArgumentsParsing.parsingArgs()

curriculumDataObj = CVData.loadConfig()

personnae = Person()

CurriculumArgumentsParsing.interactiveCompletionOf( personnae, args )
CurriculumArgumentsParsing.interactiveCompletionSkillsJobsTraining( personnae, args )

print( personnae )

texcurriculumDirectory = CurriculumLaTeXGenerator.generateLaTeX( personnae )
    
## Compiling TeX file to obtain PDF !
if args.make : 
    CurriculumLaTeXGenerator.launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

print("End of script")
