#!/usr/bin/python3
# -*- coding: utf-8 -*- 

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

def getLaTeXHeaderCVStyle(style = "classic") :
    """Attempted Argument in "[ 'classic', 'casual', 'oldstyle', 'banking' ]" """ 
    return "\\moderncvstyle{" + style + "}\n" 

def getLaTeXHeaderCVStyle(color = "blue") :
    """Attempted Argument in "[ 'blue', 'orange', 'green', 'red', 'purple', 'grey', 'black' ]" """ 
    return "%% \\moderncvcolor{" + color + "}\n" 

def getMinimalVariableDefinitions( general="General Title", title="Titre poste CV", 
                                    speciality="", firstname="Anne", lastname="Onyme", 
                                    cellphone="06~00~00~00~00" ) : 
    str = "%% some variable definitions\n"
    str += "\\def\\titreGeneralNewLine{" + general + "}\n"
    str += "\\def\\titreGeneral{" + title + "}\n"
    str += "\\def\\titreSpecialite{" + speciality + "}\n"
    str += "\\def\\prenom{ " + firstname + " }\n"
    str += "\\def\\nom{ " + lastname + " }\n"
    str += "\\def\\prenomNom{\\prenom ~\\nom }\n"
    str += "\\def\\portable{" + cellphone + "}\n"
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
    str += "\t\t\\includeLogoCC \\today -- \\emph{Curriculum Generator (Python)} \\hfill %% \\copyright\n"
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
    str += "\t\tpdfcreator={PDFLaTeX (production)}\n"
    str += "\t\t%% urlcolor=blue,\n"
    str += "}}\n\n"
    str += "\\usepackage{vmargin}\n"
    str += "\\setmarginsrb{1.0cm}{0.2cm}{1.0cm}{0.50cm}{15pt}{10pt}{15pt}{45pt}\n"
    str += "\\setlength{\hintscolumnwidth}{2.25cm}\n"
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

