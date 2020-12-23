#!/usr/bin/python3
# -*- coding: utf-8 -*- 

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

import CurriculumGeneration

def testAndGetInList(index, list, alternatevalue) : 
    item = [ None, None ]
    if ( index < len( list ) ) : 
        item = list[ index ]
    else: 
        item = [ alternatevalue, alternatevalue ]
    return item

def generateLaTeX( personnae, cvColor = "blue", cvStyle = "classic" ):
    ## Date_time generation
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%Y%m%d_%H%M%S")
    print("date and time =", dt_string)    
    
    ## prefix for directory / filename
    texSpecific = personnae.lastname + "." + personnae.firstname ## + "_" + dt_string
    
    ## texcurriculumDirectory = "generate/"
    ## texcurriculumFileName = "curriculumGenerationtest"
    texcurriculumDirectory = texSpecific + "_" + "generate/"
    texcurriculumFileName = texSpecific
    
    ## Working on Output Directory (for one curriculum)
    path = Path( texcurriculumDirectory )
    if ( path.exists() ) :
        print("Removing some resources...")
        shutil.rmtree( texcurriculumDirectory )
    ## print( "Copying some resources..." )
    ## shutil.copytree( "../resources/latexSamples/img/", texcurriculumDirectory + "img/" )
    os.mkdir( texcurriculumDirectory )
    
    ## Generate Makefile
    print( "Creating Makefile..." )
    with open( texcurriculumDirectory + "Makefile", 'w') as makefile:
        makefile.write( CurriculumGeneration.getMakefileContent( texcurriculumFileName ) )
    
    ## Generate the TeX file
    print( "Creating TeX file..." )
    with open( texcurriculumDirectory + texcurriculumFileName + ".tex", 'w') as curriculumGenerationtest:
        curriculumGenerationtest.write( CurriculumGeneration.getLaTeXHeaderPart1(cvColor, cvStyle) )
        curriculumGenerationtest.write( "\n\n" )
        ## Personnal Data
        curriculumGenerationtest.write( CurriculumGeneration.getMinimalVariableDefinitions( 
            firstname = personnae.firstname, lastname = personnae.lastname, 
            cellphone = personnae.cellphone, general = personnae.generaltitle, 
            title = personnae.title, speciality = personnae.speciality
        ) + "\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getAddressDefinition(address = personnae.address) + "\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getEMailDefinition(email = personnae.email) + "\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getWebSiteDefinition(webpage = personnae.webpage) + "\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getQuoteDefinition(quote = personnae.quote) + "\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getExtraInformation(extrainfo = personnae.extrainfo) + "\n" )
        curriculumGenerationtest.write( "\n\n" )
        ## More header
        curriculumGenerationtest.write( CurriculumGeneration.getFancyStyle() + "\n\n" )
        ## ## Get first items of sublits, to put in in keywords
        lstSkills0 = list(list(zip(*personnae.skills))[0])
        lstSkills1 = list(list(zip(*personnae.skills))[1])
        curriculumGenerationtest.write( "\\def\\motsClefs{LaTeX;PDF;Python;Python3;" + ";".join( lstSkills0 ) + ";" + ";".join( lstSkills1 ) + "}\n\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getHyperSetup() + "\n\n" )
        curriculumGenerationtest.write( CurriculumGeneration.getDefVariables() + "\n\n" )
        ## Starting document here !
        curriculumGenerationtest.write( "\\begin{document}\n\n\\maketitle\n\n" )
        ## Introduction
        ## ## ## TODO "Introduction Text" generation ??
        curriculumGenerationtest.write( "%% \\section{Introduction}\n")
        curriculumGenerationtest.write( "\t IntroductionText~\\\\ \n\n" )
        ## Compétences ...
        curriculumGenerationtest.write( "\\section{Comp{\\'e}tences}\n" )
        curriculumGenerationtest.write( "\t%% \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
        for i in range(0, len(personnae.skills), 2) : 
            item1 = personnae.skills[ i + 0 ]
            item2 = testAndGetInList( i+1, personnae.skills, "---" )
            curriculumGenerationtest.write( "\t \\cvcomputer{ %s }{ %s }{ %s }{ %s }\n" %( item1[0], item1[1], item2[0], item2[1], ) )
        curriculumGenerationtest.write( "\t \\cvitem{Langues}{ Anglais, Arabe, Chinois... }\n" )
        # curriculumGenerationtest.write( "\t \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
        # curriculumGenerationtest.write( "\t \\cvcomputer{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
        curriculumGenerationtest.write( "\n" )
        ## Professionnal Experiences
        curriculumGenerationtest.write( "\\section{Exp{\\'e}rience professionnelle}\n" )
        for eltJob in personnae.jobs : 
            curriculumGenerationtest.write( "\t \\cventry{years}{%s (%s)}{%s}{%s}{%s}{\n JobDescription \n}\n\n" %( eltJob[3], eltJob[2], eltJob[0], eltJob[4], eltJob[1] ) ) 
        curriculumGenerationtest.write( "\t %% \\cventry{years}{degree/job title}{institution/employer}{localization}{grade}{description}\n\n" )
        curriculumGenerationtest.write( "\t %% \\cventry{DATUM}{TITRE}{ENTREPRISE}{CONTRAT}%\n" )
        curriculumGenerationtest.write( "\t %% \t{\\newline INTITULE++}{%\n" )
        curriculumGenerationtest.write( "\t %% \\begin{itemize}\n" )
        curriculumGenerationtest.write( "\t %% \t\\item[$\\rightarrow$] ELEMENTUN\n" )
        curriculumGenerationtest.write( "\t %% \t\\item[$\\bullet$] ELEMENTDEUXETPLUS\n" )
        curriculumGenerationtest.write( "\t %% \\end{itemize}}\n\n" )
        ## Training ...
        curriculumGenerationtest.write( "\\section{Formation}\n" )
        for eltTraining in personnae.trainings : 
            curriculumGenerationtest.write( "\t \\cventry{years}{%s}{%s}{%s}{\n %% grade \n}{\n %% description \n}\n\n" %(  eltTraining[1], eltTraining[0], eltTraining[2]  ) )
        curriculumGenerationtest.write( "\t %% \\cventry{Year}{Diploma}{School}{Location}    {}{}{}\n\n" )
        ## Certifications ...
        curriculumGenerationtest.write( "\\section{Licences et Certifications}\n" )
        curriculumGenerationtest.write( "\t \\cventry{Year}{Diploma}{\\newline School}{Location}    {}{}{}\n\n" )
        ## Bénévolat ...
        ## ## ## TODO "Bénévolat" generation ??
        curriculumGenerationtest.write( "\\section{Expériences de bénévolat}\n" )
        curriculumGenerationtest.write( "\t \\cventry{years}{jobtitle}{institution}{localization}{status}{description}\n\n" )
        ## Recommandations ...
        ## ## ## TODO "Recommandations" generation ??
        curriculumGenerationtest.write( "%% \\section{Recommandations}\n" )
        curriculumGenerationtest.write( "%% \t \\cvitem{ Item }{ Content }\n\n" )
        ## Réalisations ...
        ## ## ## TODO "Réalisations" generation ??
        curriculumGenerationtest.write( "\\section{Réalisations}\n" )
        curriculumGenerationtest.write( "\t \\cvitem{Projets}{ GitHub }\n" )
        curriculumGenerationtest.write( "\t \\cvitem{Organisations}{ associations }\n" )
        curriculumGenerationtest.write( "\t \\cvitem{Publications}{ citations }\n\n" )
        ## Out of Work / Centres d'intérêts
        ## ## ## TODO "Interests out of the work" generation ??
        curriculumGenerationtest.write( "\\section{Centres d'int{\\'e}r{\\^e}ts}\n" )
        curriculumGenerationtest.write( "\t \\cvitem{Lectures}{ Science-Fiction, Policier, Fantasy... }\n" )
        curriculumGenerationtest.write( "\t \\cvitem{Jeux Sociaux}{ Jeux de Rôle, Jeux de plateau, e-sport }\n" )
        ## END of document 
        curriculumGenerationtest.write( "\\end{document}\n\n" )
    return texcurriculumDirectory

def launcheMakePDFfromLaTeX( directory ) : 
    print( "Changing dir to {" + directory + "}..." )
    os.chdir( directory )
    print( "Compiling TeX file to PDF..." )
    retcode = subprocess.call( "make", stdin=None, stdout=subprocess.DEVNULL, stderr=None, shell=True )
    print( retcode )
    print( "Cleaning..." )
    retcode2 = subprocess.call( "make clean", stdin=None, stdout=subprocess.DEVNULL, stderr=None, shell=True)
    print( retcode2 )
    print( "Changing dir BACK..." )
    os.chdir( ".." )


