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

## ## ## ## ## Generate some Ideas from associated resources !

import random

from BiographicSelection import selectRandomBiographic
from BiographicSelection import selectBiographicElements
from BiographicDataLoad import BiographicDataLoad

from Person import Person

from CurriculumData import CVData
from CurriculumLaTeXGenerator import generateLaTeX

curriculumDataObj = CVData.loadConfig()

## from BiographicTable import BiographicTable
biotables = BiographicDataLoad.loadBiographicsTables()
## from BiographicJob import BiographicJob
jobs = BiographicDataLoad.loadJobsToSkills()
## from BiographicSkill import BiographicSkill
skills = BiographicDataLoad.loadSkills()

## print( biotables )
## print( selectRandomBiographic( biotables ) )

## print( jobs )
## for elt in jobs : 
##     print( jobs[ elt ] )

## print( skills )
## for elt in skills : 
##     print( skills[ elt ] )

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
personnae.generaltitle = "General Title"
personnae.speciality = "Speciality"

numberOfResults = 10

res = selectBiographicElements( numberOfResults )

def addskill( skill ) : 
    if skill not in personnae.skills: 
        if (skill.possibilities == None) : 
            personnae.skills.append( [ skill.name, "---" ] )
        else:
            personnae.skills.append( [ skill.name, ", ".join( skill.possibilities ) ] )

for elt in res : 
    jobOrTraing = elt.contents[1]
    trainingTAG = "[Formation]"
    print( "%s " %( jobOrTraing ) )
    if (jobOrTraing.startswith( trainingTAG ) ) : 
        personnae.trainings.append( jobOrTraing[len(trainingTAG):len(jobOrTraing)] )
    else : 
        personnae.jobs.append( jobOrTraing )
    for item in elt.addins : 
        if (item.startswith( "talent:" ) ) : 
            if (item == "talent:*"):
                 skill = random.choice(list(skills.values()))
                 addskill( skill )
            else : 
                job = item[item.index(":")+1:item.index("=")]
                val = item[item.index("=")+1:]
                skill = None
                if (val == "all") : 
                    for elt in jobs[ job ].skills : 
                        skill = skills[ elt ]
                        print( "\t%s\t%s\t%s" %( skill.name, skill.level, skill.possibilities ) )
                        addskill( skill )
                elif (val != "*") : 
                    skill = skills[ job ]
                else : 
                    jobSkill = jobs[ job ]
                    skill = skills[ random.choice( jobSkill.skills ) ]
                    addskill( skill )
            print( "\t%s\t%s\t%s" %( skill.name, skill.level, skill.possibilities ) )
        else :
            print( "\t%s +++++" %( item ) )

print( personnae );

generateLaTeX( personnae )

## TODO generate curriculum from chat is done here !!
