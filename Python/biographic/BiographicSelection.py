#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import random

from BiographicDataLoad import BiographicDataLoad
from BiographicElement import BiographicElement

def selectRandomBiographic( tables ) : 
    """Choose randomly an element from a randomly choosen BiographicTable. """
    orientation = tables[ "d'Orientation" ]
    ## print( orientation )
    bioELT = None
    while (orientation != None) : 
        contents = orientation.contents
        links = orientation.linksTo
        addins = orientation.addins
        index = random.randint(0, len(contents) - 1 )
        ## print( "%d (%d, %d, %d)" %( index, len(contents), len(links), len(addins) ) )
        content = contents[index]
        link = links[index]
        addin = addins[index]
        ## ## ## Generate / complete a BiographicElement 
        if (bioELT == None) : 
            bioELT = BiographicElement( content )
        else : 
            bioELT.contents.append( content )
        if (addin != None) : 
            bioELT.addins = addin.split( ";" )
        if (link != None) : 
            if (link == "Cicatrices") : 
                orientation = tables[ "Cicatrices-localisation" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = tables[ "Cicatrices-gravité" ]
                bioELT.contents.append( "Cicatrice : %s" %( random.choice( orientation.contents ) ) )
                orientation = None;
            else:
                orientation = tables[ link ];
        else : 
            orientation = None
    ## print( bioELT )
    return bioELT

def selectBiographicElements( number ) : 
    results = []
    tables = BiographicDataLoad.loadBiographicsTables()
    for i in range(0, number) : 
        results.append( selectRandomBiographic( tables ) )
    return results

##### ##### ##### ##### ##### 

def addskill( skill, personnae ) : 
    if (skill not in personnae.skills) : 
        if (skill.possibilities == None) : 
            personnae.skills.append( [ skill.name, "---" ] )
        else:
            personnae.skills.append( [ skill.name, ", ".join( skill.possibilities ) ] )

def reworking( personnae ) : 
    genericKey = "Divers"
    skillsAsDict = { genericKey : [] }
    reboot = True
    while (reboot) : 
        reboot = False
        for skill in personnae.skills : 
            if ( (skill[1] is "---") and (skill[0] not in skillsAsDict[ genericKey ] ) ) : 
                skillsAsDict[ genericKey ].append( skill[0] )
            if (skill[1] is "---") : 
                personnae.skills.remove( skill )
                reboot = True
    print( personnae.skills )
    print( skillsAsDict )
    personnae.skills.append( [ genericKey, ", ".join( skillsAsDict[ genericKey ] ) ] )

