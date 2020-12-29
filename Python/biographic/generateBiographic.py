#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

import random

## ## ## ## ## Generate some Ideas from associated resources !

import BiographicSelection
from BiographicDataLoad import BiographicDataLoad

from Person import Person

from CurriculumLaTeXGenerator import generateLaTeX
from CurriculumLaTeXGenerator import launcheMakePDFfromLaTeX

from CurriculumData import CVData
curriculumDataObj = CVData.loadConfig()

personnae = Person()

personnae.extrainfo	= "NOEXTRAINFO"
personnae.quote		= "NOQUOTE"

personnae.firstname = random.choice( curriculumDataObj.firstNameList )
personnae.lastname = random.choice( curriculumDataObj.lastNameList )
personnae.pseudo = personnae.firstname.lower() + "." + personnae.lastname.lower()
defaultemail = personnae.pseudo + "@gmx.com"
personnae.email = defaultemail
personnae.address = "1337 Grand Boulevard -- 61337 Section 42"
personnae.cellphone = "06~12~34~56~78"
personnae.webpage = personnae.pseudo + ".personnalbranding.com"

personnae.title = "Title"
personnae.generaltitle = "GeneralTitle"
personnae.speciality = "Speciality"

numberOfResults = 10

res = BiographicSelection.selectBiographicElements( numberOfResults )

personnae = BiographicSelection.preparingBiographicElements( res, personnae )

BiographicSelection.reworking( personnae )

personnae.recos.append( ["referent 1", "some text"] )
personnae.certifs.append( BiographicSelection.selectRandomCertification() )
personnae.btasks.append( BiographicSelection.selectRandomBenevolentTasks() )
personnae.projs.append( BiographicSelection.selectRandomRealisations() )
personnae.interests.append( BiographicSelection.selectRandomCentresDInteret() )

print( personnae )

texcurriculumDirectory = generateLaTeX( personnae )
launcheMakePDFfromLaTeX( directory = texcurriculumDirectory )

## => go to directory : "make && make clean" to generate PDF !