#!/usr/bin/python3
# -*- coding: utf-8 -*- 

__author__ = "Gabriel Chandesris"
__copyright__ = "CC Gabriel Chandesris (2020, 2022)"
__credits__ = ""
__licence__ = "GNU GENERAL PUBLIC LICENSE v3"
__version__ = "1.0.0a"
__maintainer__ = "Gabriel Chandesris"
__email__ = "gabywald[at]laposte.net"
__contact__ = "gabywald[at]laposte.net"
__status__ = "Development"

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

def testAndGetInList(index, list, alternatevalue) : 
    item = [ None, None ]
    if ( index < len( list ) ) : 
        item = list[ index ]
    else: 
        item = [ alternatevalue, alternatevalue ]
    return item

def getLaTeXHeaderCVStyle(style = "classic") :
    """Attempted Argument in "[ 'classic', 'casual', 'oldstyle', 'banking' ]" """ 
    return "\\moderncvstyle{" + style + "}\n" 

def getLaTeXHeaderCVStyle(color = "blue") :
    """Attempted Argument in "[ 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black' ]" """ 
    return "%% \\moderncvcolor{" + color + "}\n" 

def getMakefileContent( texfilename ) : 
    str = "## naming WITHOUT the extensions [.tex] or [.bib]\n"
    str += "LATEXFILE=" + texfilename + "\n\n"
    str += "## the local software...\n"
    str += "CCPDFLA=pdflatex\n"
    str += "CCPHTML=latex2html\n"
    str += "CCP2RTF=latex2rtf\n\n"
    str += "all : pdflatex # html rtf\n"
    str += "\t@echo 'DONE'\n\n"
    str += "pdflatex : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
    str += "\t$(CCPDFLA) $(LATEXFILE).tex\n"
    str += "\t$(CCPDFLA) $(LATEXFILE).tex\n"
    str += "\t$(CCPDFLA) $(LATEXFILE).tex\n"
    str += "\t@echo 'PDFLATEX DONE'\n\n"
    str += "html : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
    str += "\t$(CCPHTML) $(LATEXFILE).tex\n"
    str += "\t@echo 'HTML DONE'\n\n"
    str += "rtf : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
    str += "\t$(CCP2RTF) -Z9 $(LATEXFILE).tex\n"
    str += "\t@echo 'RTF DONE'\n\n"
    str += "clean : mrproper\n"
    str += "\trm $(LATEXFILE).log\n"
    str += "\t# rm $(LATEXFILE).lot\n"
    str += "\t# rm $(LATEXFILE).lof\n"
    str += "\t# rm $(LATEXFILE).dvi\n"
    str += "\t# rm $(LATEXFILE).pdf\n"
    str += "\t@echo 'CLEAN DONE'\n\n"
    str += "mrproper : $(LATEXFILE).out $(LATEXFILE).aux # $(LATEXFILE).bbl $(LATEXFILE).blg $(LATEXFILE).toc\n"
    str += "\trm $(LATEXFILE).out\n"
    str += "\trm $(LATEXFILE).aux\n"
    str += "\t# rm $(LATEXFILE).toc\n"
    str += "\t# rm $(LATEXFILE).bbl\n"
    str += "\t# rm $(LATEXFILE).blg\n"
    str += "\t@echo 'MRPROPER DONE'\n\n"
    return str

def getLaTeXHeaderPart1(color = "blue", style = "classic") : 
    str = "%% HEADER PART 1 of LaTeX Curriculum file\n" 
    str += "\\documentclass[11pt,a4paper]{moderncv}\n" 
    str += "\\usepackage[french]{babel}\n" 
    str += "\\moderncvtheme[" + color + "]{" + style + "}\n" 
    str += "%% \\moderncvstyle{...}\n" 
    str += "%% \\moderncvcolor{...}\n" 
    return str

def getMinimalVariableDefinitions( general = "General Title", title = "Titre poste CV", 
                                    speciality = "", firstname = "Anne", lastname = "Onyme", 
                                    cellphone = "06~00~00~00~00", age = 42, pseudo = "Anne.Onyme" ) : 
    str = "%% some variable definitions\n"
    str += "\\def\\titreGeneralNewLine{" + general + "}\n"
    str += "\\def\\titreGeneral{" + title + "}\n"
    str += "\\def\\titreSpecialite{" + speciality + "}\n"
    str += "\\def\\prenom{ " + firstname + " }\n"
    str += "\\def\\nom{ " + lastname + " }\n"
    str += "\\def\\prenomNom{\\prenom ~\\nom }\n"
    str += "\\def\\portable{" + cellphone + "}\n"
    str += "\\def\\pseudo{" + pseudo + "}\n"
    str += "\\def\\ageing{" + f'{age}' + "}\n"
    return str

def getAddressDefinition(address = "1337 Grand Boulevard -- 61337 Section") : 
    return "\\def\\adressePhysique{ " + address + " }\n"

def getEMailDefinition(email = "firstname.lastname@provider.ext") : 
    return "\\def\\eMail{" + email + "}\n"
    
def getWebSiteDefinition(webpage = "www.siteweb.com") : 
    return "\\def\\pageWeb{" + webpage + "} \n"

def getQuoteDefinition(quote = "NOQUOTE") : 
    if ( (quote != None) and (quote != "NOQUOTE") ): 
        return "\\def\\quotationCitation{ " + quote + " } \n"
    else:
    	return "%% NOQUOTE"
    	
def getExtraInformation(extrainfo = "NOEXTRAINFO") : 
    if ( (extrainfo != None) and (extrainfo != "NOEXTRAINFO") ): 
        return "\\def\\extrainfoDATA{ " + extrainfo + " } \n"
    else:
    	return "%% NOEXTRAINFO"
    
def getFancyStyle() : 
    str = "%% Fancy Style Defintion (and collateral elements)\n"
    str += "\\usepackage{lastpage}\n"
    str += "\n"
    str += "\\def\\logoGliderNorma{../../resources/latexSamples/img/logo_glider.png}\n"
    str += "\\def\\logoGliderRight{../../resources/latexSamples/img/logo-glider-right.png}\n"
    str += "\\def\\logoGliderLeftt{../../resources/latexSamples/img/logo-glider-left.png}\n"
    str += "\\def\\logoCreativeCommon{../../resources/latexSamples/img/CreativeCommonLogo.jpeg}\n"
    str += "\\def\\includeLogoGN{\\includegraphics[width=0.50cm]{\\logoGliderNorma }}\n"
    str += "\\def\\includeLogoGR{\\includegraphics[width=0.50cm]{\\logoGliderRight }}\n"
    str += "\\def\\includeLogoGL{\\includegraphics[width=0.50cm]{\\logoGliderLeftt }}\n"
    str += "\\def\\includeLogoCC{\\includegraphics[width=0.25cm]{\\logoCreativeCommon }}\n"
    str += "\n"
    str += "\\pagestyle{fancy}\n"
    str += "\\def\\makestylefancyContent{%\n"
    str += "\t\\fancyhf{}\n"
    str += "\t\\fancyhead[LE]{\n"
    str += "\t\t\\includegraphics[width=0.5cm]{\\logoGliderLeftt }\n"
    str += "\t\t\\hfill\n"
    str += "\t\t\\prenomNom \n"
    str += "\t\t\\hfill\n"
    str += "\t\t\\titreGeneral  -- \\titreSpecialite\n"
    str += "\t}\n"
    str += "\t\\fancyfoot[LE]{\n"
    str += "\t\\includegraphics[width=0.5cm]{\\logoGliderLeftt } \\hfill\n"
    str += "\t\t\\includeLogoCC \\today -- \\emph{Curriculum Generator (Python)} \\hfill %% \\copyright\n"
    str += "\t\t\\thepage /\\pageref{LastPage}\n"
    str += "\t}\n"
    str += "\n"
    str += "\t\\fancyhead[RO]{\n"
    str += "\t\t\\titreGeneral  -- \\titreSpecialite\n"
    str += "\t\t\\hfill\n"
    str += "\t\t\\prenomNom \n"
    str += "\t\t\\hfill\n"
    str += "\t\t\\includegraphics[width=0.5cm]{\\logoGliderRight }\n"
    str += "\t}\n"
    str += "\t\\fancyfoot[RO]{\n"
    str += "\t\t\\thepage /\\pageref{LastPage} \\hfill\n"
    str += "\t\t\\includeLogoCC \\today -- \\emph{\href{https://github.com/gabywald/CurriculumGenerator}{Curriculum Generator (Python)} par \href{https://www.linkedin.com/in/gabriel-chandesris/}{GabyWald} } \\hfill %% \\copyright\n"
    str += "\t\t\\includegraphics[width=0.5cm]{\\logoGliderRight }\n"
    str += "\t}\n"
    str += "\t\\renewcommand{\\headrulewidth}{0.25pt}\n"
    str += "\t\\renewcommand{\\footrulewidth}{0.5pt}\n"
    str += "}%\n"
    str += "\\makestylefancyContent\n"
    return str

def getHyperSetup() : 
    str = "%% Some SetUp\n"
    str += "\AfterPreamble{\hypersetup{\n"
    str += "\t\tpdfauthor={\\prenomNom},\n"
    str += "\t\tpdftitle={\\titreGeneral ~-- \\titreSpecialite },\n"
    str += "\t\tpdfsubject={\\titreGeneral ~-- \\titreSpecialite },\n"
    str += "\t\tpdfkeywords={\\motsClefs },\n"
    str += "\t\tpdfproducer={PDFLaTeX (creation)},\n"
    str += "\t\tpdfcreator={Curriculum Generator by Gaby Wald https://github.com/gabywald/CurriculumGenerator}\n"
    str += "\t\t%% urlcolor=blue,\n"
    str += "}}\n\n"
    str += "\\usepackage{vmargin}\n"
    str += "\\setmarginsrb{1.0cm}{0.2cm}{1.0cm}{0.50cm}{15pt}{10pt}{15pt}{45pt}\n"
    str += "%% \\setlength{\hintscolumnwidth}{2.25cm}\n"
    return str

def getDefVariables() : 
    str = "%% Defines Some attempted Values\n"
    str += "\\firstname{\\prenom }\n"
    str += "\\familyname{\\nom }\n"
    str += "\\title{\\titreGeneral }\n"
    str += "%% \\title{\\titreGeneral \\newline \\titreSpecialite}\n"
    str += "\\address{\\adressePhysique }\n"
    str += "\\email{\\eMail }\n"
    str += "\\homepage{\\pageWeb }\n"
    str += "\\mobile{\\portable }\n"
    ## str += "\\quote{ \\quotationCitation }\n"
    str += "\\ifdefined\\quotationCitation\n\\quote{ \\quotationCitation }\\fi\n"
    str += "\\ifdefined\\extrainfoDATA\n\\extrainfo{ \\extrainfoDATA }\\fi\n"
    str += "%% \\phone{00 00 00 00 00}\n"
    str += "%% \\fax{00 00 00 00 00}\n"
    str += "%% \\photo[64pt][0.4pt]{img/logo_glider.png}\n"
    str += "%% \\phone[mobile]{\\portable } %% \\phone[mobile]{06~12~34~56~78}\n"
    str += "%% \\phone[fixed]{01~01~01~01~01}\n"
    str += "%% \\phone[fax]{01~01~01~01~01}\n"
    str += "%% \\social[linkedin]{LinkedInProfile}    %% https://www.linkedin.com/in/.../\n"
    str += "%% \\social[github]{GitHubProfile}        %% https://github.com/...\n"
    str += "%% \\social[facebook]{FaceBookProfile}    %% https://www.facebook.com/...\n"
    str += "%% \\social[twitter]{TwitterPage}         %% https://twitter.com/...\n"
    return str

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
        makefile.write( getMakefileContent( texcurriculumFileName ) )
    
    ## Generate the TeX file
    print( "Creating TeX file..." )
    with open( texcurriculumDirectory + texcurriculumFileName + ".tex", 'w') as curriculumGenerationtest:
        curriculumGenerationtest.write( getLaTeXHeaderPart1(cvColor, cvStyle) )
        curriculumGenerationtest.write( "\n\n" )
        ## Personnal Data
        curriculumGenerationtest.write( getMinimalVariableDefinitions( 
            firstname = personnae.firstname, lastname = personnae.lastname, 
            cellphone = personnae.cellphone, general = personnae.generaltitle, 
            title = personnae.title, speciality = personnae.speciality, 
            age = personnae.age, pseudo = personnae.pseudo
        ) + "\n" )
        curriculumGenerationtest.write( getAddressDefinition(address = personnae.address) + "\n" )
        curriculumGenerationtest.write( getEMailDefinition(email = personnae.email) + "\n" )
        curriculumGenerationtest.write( getWebSiteDefinition(webpage = personnae.webpage) + "\n" )
        curriculumGenerationtest.write( getQuoteDefinition(quote = personnae.quote) + "\n" )
        curriculumGenerationtest.write( getExtraInformation(extrainfo = personnae.extrainfo) + "\n" )
        curriculumGenerationtest.write( "\n\n" )
        ## More header
        curriculumGenerationtest.write( getFancyStyle() + "\n\n" )
        ## ## Get first items of sublists, to put in in keywords
        lstSkills0 = []
        if (len(personnae.skills) > 0) :
        	lstSkills0 = list(list(zip(*personnae.skills))[0])
        lstSkills1 = []
        if (len(personnae.skills) > 1) :
        	lstSkills1 = list(list(zip(*personnae.skills))[1])
        curriculumGenerationtest.write( "\\def\\motsClefs{LaTeX;PDF;Python;Python3;" + ";".join( lstSkills0 ) + ";" + ";".join( lstSkills1 ) + "}\n\n" )
        curriculumGenerationtest.write( getHyperSetup() + "\n\n" )
        curriculumGenerationtest.write( getDefVariables() + "\n\n" )
        ## Starting document here !
        curriculumGenerationtest.write( "\\begin{document}\n\n\\maketitle\n\n" )
        ## Introduction
        ## ## ## TODO "Introduction Text" generation ??
        curriculumGenerationtest.write( "%% \\section{Introduction}\n")
        curriculumGenerationtest.write( "\t IntroductionText~\\\\ \n\n" )
        ## Skills / Compétences ...
        curriculumGenerationtest.write( "\\section{Comp{\\'e}tences}\n" )
        curriculumGenerationtest.write( "\t%% \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n\n" )
        for i in range(0, len(personnae.skills), 2) : 
            item1 = personnae.skills[ i + 0 ]
            item2 = testAndGetInList( i+1, personnae.skills, "---" )
            # print( "SKILL", item1, item2 )
            curriculumGenerationtest.write( "\t \\cvcomputer{ %s }{ %s }{ %s }{ %s }\n" %( item1[0], item1[1], item2[0], item2[1], ) )
        curriculumGenerationtest.write( "\t \\cvitem{Langues}{ Anglais, Arabe, Chinois... }\n" )
        # curriculumGenerationtest.write( "\t \\cvdoubleitem{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
        # curriculumGenerationtest.write( "\t \\cvcomputer{ Item1 }{ Description1 }{ Item2 }{ Description2 }\n" )
        curriculumGenerationtest.write( "\n" )
        ## Professionnal Experiences
        ## TODO compute years for jobs !
        curriculumGenerationtest.write( "\\section{Exp{\\'e}rience professionnelle}\n" )
        for eltJob in personnae.jobs : 
            # print( "eltJOB", eltJob )
            curriculumGenerationtest.write( "\t \\cventry{years}{%s (%s)}{%s}{%s}{%s}{\n JobDescription \n}\n\n" %( eltJob[3], eltJob[2], eltJob[0], eltJob[4], eltJob[1] ) )
        curriculumGenerationtest.write( "\t %% \\cventry{years}{degree/job title}{institution/employer}{localization}{grade}{description}\n\n" )
        curriculumGenerationtest.write( "\t %% \\cventry{DATUM}{TITRE}{ENTREPRISE}{CONTRAT}%\n" )
        curriculumGenerationtest.write( "\t %% \t{\\newline INTITULE++}{%\n" )
        curriculumGenerationtest.write( "\t %% \\begin{itemize}\n" )
        curriculumGenerationtest.write( "\t %% \t\\item[$\\rightarrow$] ELEMENTUN\n" )
        curriculumGenerationtest.write( "\t %% \t\\item[$\\bullet$] ELEMENTDEUXETPLUS\n" )
        curriculumGenerationtest.write( "\t %% \\end{itemize}}\n\n" )
        ## Training ...
        ## TODO compute years for trainings !
        curriculumGenerationtest.write( "\\section{Formation}\n" )
        for eltTraining in personnae.trainings : 
            # print( "eltTraining", eltTraining )
            curriculumGenerationtest.write( "\t \\cventry{years}{%s}{%s}{%s}{\n %% grade \n}{\n %% description \n}\n\n" %(  eltTraining[1], eltTraining[0], eltTraining[2]  ) )
        curriculumGenerationtest.write( "\t %% \\cventry{Year}{Diploma}{School}{Location}    {}{}{}\n\n" )
        ## Recommandations ...
        if (len(personnae.recos) > 0) : 
            curriculumGenerationtest.write( "\\section{Recommandations}\n" )
            curriculumGenerationtest.write( "%% \t \\cvitem{ Recommendation }{ Content }\n\n" )
            for elt in personnae.recos : 
                curriculumGenerationtest.write( "\t \\cvitem{%s}{%s}\n" %(  elt[0], elt[1]  ) )
        ## Certifications ...
        if (len(personnae.certifs) > 0) : 
            curriculumGenerationtest.write( "\\section{Licences et Certifications}\n" )
            for elt in personnae.certifs : 
                curriculumGenerationtest.write( "\t \\cvitem{%s}{%s}\n" %(  elt[0], elt[1]  ) )
        ## Bénévolat ...
        if (len(personnae.btasks) > 0) : 
            curriculumGenerationtest.write( "\\section{Exp{\\'e}riences de b{\\'e}n{\\'e}volat}\n" )
            for elt in personnae.btasks : 
                curriculumGenerationtest.write( "\t \\cvitem{%s}{%s}\n" %(  elt[0], elt[1]  ) )
        ## Réalisations ...
        if (len(personnae.projs) > 0) : 
            curriculumGenerationtest.write( "\\section{R{\\'e}alisations}\n" )
            for elt in personnae.projs : 
                curriculumGenerationtest.write( "\t \\cvitem{%s}{%s}\n" %(  elt[0], elt[1]  ) )
        ## Out of Work / Centres d'intérêts
        if (len(personnae.interests) > 0) : 
            curriculumGenerationtest.write( "\\section{Centres d'int{\\'e}r{\\^e}ts}\n" )
            for elt in personnae.interests : 
                curriculumGenerationtest.write( "\t \\cvitem{%s}{%s}\n" %(  elt[0], elt[1]  ) )
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


