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

## ## ## ## ## Main script to generate file passed in parameter in dedicated script

import sys
import random

import CurriculumArgumentsParsing

from Person import Person
from CurriculumData import CVData

numberOfPersonnae = None

if (len(sys.argv) < 2) : 
    numberOfPersonnae = random.randint(1, 100)
else : 
    try : 
        numberOfPersonnae = int(sys.argv[1])
    except ValueError:
        numberOfPersonnae = curriculumMainFunctions.askForInt( "Number of Person to generate ? " )
    
print ( "## numberOfPersonnae: %d" %( numberOfPersonnae ) )

for i in range(0, numberOfPersonnae) : 
    personnae = Person()
    curriculumDataObj = CVData.loadConfig()
    ## First Name and Last Name
    personnae.firstname = random.choice( curriculumDataObj.firstNameList )
    personnae.lastname = random.choice( curriculumDataObj.lastNameList )
    ## Pseudo and associated values (email, website) and address and cellphone
    personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()
    personnae.email = personnae.pseudo + "@gmx.com"
    personnae.webpage = personnae.pseudo + ".personnalbranding.com"
    personnae.address = "PostalBox%d" %i
    personnae.cellphone = "06~78~34~12~56"
    ## Others
    personnae.quote = "NOQUOTE"
    numberOfYears = random.randint(20, 70)
    personnae.extrainfo = "%d ans" %( numberOfYears )
    ## {Skills;Jobs;Trainings} elements
    personnae.skilleltnb = random.randint(1, int(numberOfYears / 5) )
    personnae.jobeltsnb = random.randint(1, int(numberOfYears / 5) )
    personnae.trainingeltsnb = random.randint(1, int(numberOfYears / 5) )
    CurriculumArgumentsParsing.interactionSelection( personnae.skills, personnae.skilleltnb, True, "Skills" )
    CurriculumArgumentsParsing.interactionSelection( personnae.jobs, personnae.jobeltsnb, True, "Job" )
    CurriculumArgumentsParsing.interactionSelection( personnae.trainings, personnae.trainingeltsnb, True, "Training" )
    ## General Title, Title and Speciality
    threePieces = curriculumDataObj.getRandomJob()
    personnae.generaltitle = "%s (%s)" %( threePieces[0], threePieces[2] )
    personnae.title = threePieces[1]
    personnae.speciality = threePieces[2]
    str = random.choice( curriculumDataObj.cvStyle ) + "\t"
    str += random.choice( curriculumDataObj.cvColor ) + "\t"
    str += personnae.export()
    numberOfYears = None
    print( str )
    personnae = None

