#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import random

from BiographicDataLoad import BiographicDataLoad
from BiographicElement import BiographicElement

from CurriculumData import CVData
curriculumDataObj = CVData.loadConfig()

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

def preparingBiographicElements( res, personnae ) : 
    tables = BiographicDataLoad.loadBiographicsTables()
    biotables = BiographicDataLoad.loadBiographicsTables()
    jobs = BiographicDataLoad.loadJobsToSkills()
    skills = BiographicDataLoad.loadSkills()
    locations = tables[ "Localisation" ]
    for elt in res : 
        jobOrTrains = elt.contents[1]
        moreselect = elt.contents[0][len("Table "):]
        trainingTAG = "[Formation]"
        print( "%s " %( jobOrTrains ) )
        corporation  = CVData.getRandomCorporationName()
        contractType = CVData.getRandomContractType()
        location     = random.choice( locations.contents )
        ## Training or Job
        if (jobOrTrains.startswith( trainingTAG ) ) : 
            selected     = jobOrTrains[len(trainingTAG):]
            personnae.trainings.append( [corporation[0], selected, corporation[1], location, contractType] )
        else : 
            personnae.jobs.append( [jobOrTrains, moreselect + " (" + location + ")", corporation[1], corporation[0], contractType] )
        for item in elt.addins : 
            if (item.startswith( "talent:" ) ) : 
                if (item == "talent:*"):
                     skill = random.choice(list(skills.values()))
                     addskill( skill, personnae )
                else : 
                    job = item[item.index(":")+1:item.index("=")]
                    val = item[item.index("=")+1:]
                    skill = None
                    if (val == "all") : 
                        for elt in jobs[ job ].skills : 
                            skill = skills[ elt ]
                            print( "\t%s\t%s\t%s" %( skill.name, skill.level, skill.possibilities ) )
                            addskill( skill, personnae )
                    elif (val != "*") : 
                        skill = skills[ job ]
                    else : 
                        jobSkill = jobs[ job ]
                        skill = skills[ random.choice( jobSkill.skills ) ]
                        addskill( skill, personnae )
                print( "\t%s\t%s\t%s" %( skill.name, skill.level, skill.possibilities ) )
            else :
                print( "\t%s +++++" %( item ) )
    return personnae

def addskill( skill, personnae ) : 
    if (skill not in personnae.skills) : 
        if (skill.possibilities == None) : 
            personnae.skills.append( [ skill.name, "---" ] )
        else:
            personnae.skills.append( [ skill.name, ", ".join( skill.possibilities ) ] )

def reworking( personnae ) : 
    """Regroup the skills that are alone. """
    genericKey = "Divers"
    skillsAsDict = { genericKey : [] }
    reboot = True
    while (reboot) : 
        reboot = False
        for skill in personnae.skills : 
            if ( (skill[1] == "---") and (skill[0] not in skillsAsDict[ genericKey ] ) ) : 
                skillsAsDict[ genericKey ].append( skill[0] )
            if (skill[1] == "---") : 
                personnae.skills.remove( skill )
                reboot = True
    print( personnae.skills )
    print( skillsAsDict )
    personnae.skills.append( [ genericKey, ", ".join( skillsAsDict[ genericKey ] ) ] )

