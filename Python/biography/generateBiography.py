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

from BiographicTable import BiographicTable
from BiographicTable import selectRandomBiographic
from BiographicTable import selectBiographicElements

biotables = BiographicTable.loadBiographicsTables()
jobs = BiographicTable.loadJobsToSkills()
skills = BiographicTable.loadSkills()

## print( biotables )
## print( selectRandomBiographic( biotables ) )
## print( jobs )
## for elt in jobs : 
##     print( jobs[ elt ] )
## print( talents )
## for elt in talents : 
##     print( talents[ elt ] )

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
                if (val != '*'):
                    level = val
                    ## NOTE value here !!
                print( "\t%s\t%s\t%s" %( skill.name, level, skill.possibilities ) )
        else :
            print( "\t%s" %( item ) )

## TODO avoid double results
## TODO better treatment of jobs ('metiers')
## TODO better treatment of equipments, software ('logiciels')
## TODO better treatment of GodFather's ('Parrain')
## TODO better treatment of debts (debtTo & debtFrom)
## TODO better treatment of some elements ('credit', ...)

