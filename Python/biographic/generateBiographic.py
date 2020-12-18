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

numberOfResults = 10

res = selectBiographicElements( numberOfResults )

for elt in res : 
    print( "%s " %( elt.contents[1] ) )
    for item in elt.addins : 
        if (item.startswith( "talent:" ) ) : 
            if (item == "talent:*"):
                 skill = random.choice(list(skills.values()))
            else : 
                job = item[item.index(":")+1:item.index("=")]
                val = item[item.index("=")+1:]
                skill = None
                if (val == "all") : 
                    for skill in skills : 
                        print( "\t%s\t%s\t%s" %( skill.name, level, skill.possibilities ) )
                elif (val != "*") : 
                    skill = skills[ job ]
                else : 
                    jobSkill = jobs[ job ]
                    skill = skills[ random.choice( jobSkill.skills ) ]
            level = skill.level
            print( "\t%s\t%s\t%s" %( skill.name, level, skill.possibilities ) )
        else :
            print( "\t%s" %( item ) )


