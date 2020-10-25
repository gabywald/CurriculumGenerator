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
	str += "	@echo 'DONE'\n\n"
	str += "pdflatex : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
	str += "	$(CCPDFLA) $(LATEXFILE).tex\n"
	str += "	$(CCPDFLA) $(LATEXFILE).tex\n"
	str += "	$(CCPDFLA) $(LATEXFILE).tex\n"
	str += "	@echo 'PDFLATEX DONE'\n\n"
	str += "html : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
	str += "	$(CCPHTML) $(LATEXFILE).tex\n"
	str += "	@echo 'HTML DONE'\n\n"
	str += "rtf : $(LATEXFILE).tex # $(BIBTEFILE).bib\n"
	str += "	$(CCP2RTF) -Z9 $(LATEXFILE).tex\n"
	str += "	@echo 'RTF DONE'\n\n"
	str += "clean : mrproper\n"
	str += "	rm $(LATEXFILE).log\n"
	str += "	# rm $(LATEXFILE).lot\n"
	str += "	# rm $(LATEXFILE).lof\n"
	str += "	# rm $(LATEXFILE).dvi\n"
	str += "	# rm $(LATEXFILE).pdf\n"
	str += "	@echo 'CLEAN DONE'\n\n"
	str += "mrproper : $(LATEXFILE).out $(LATEXFILE).aux # $(LATEXFILE).bbl $(LATEXFILE).blg $(LATEXFILE).toc\n"
	str += "	rm $(LATEXFILE).out\n"
	str += "	rm $(LATEXFILE).aux\n"
	str += "	# rm $(LATEXFILE).toc\n"
	str += "	# rm $(LATEXFILE).bbl\n"
	str += "	# rm $(LATEXFILE).blg\n"
	str += "	@echo 'MRPROPER DONE'\n\n"
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
	return "\\def\\eMail{ " + email + " }\n"
	
def getWebSiteDefinition(webpage = "http://www.siteweb.com") : 
	return "\\def\\pageWeb{ " + webpage + " } \n"

def getQuoteDefinition(quote = "Quotation Citation") : 
	return "\\def\\quotationCitation{ " + quote + " } \n"
	
def getFancyStyle() : 
	str = "%% Fancy Style Defintion (and collateral elements)\n"
	str += "\\usepackage{lastpage}\n"
	str += "\n"
	str += "\\def\\logoGliderNorma{img/logo_glider.png}\n"
	str += "\\def\\logoGliderRight{img/logo-glider-right.png}\n"
	str += "\\def\\logoGliderLeftt{img/logo-glider-left.png}\n"
	str += "\\def\\logoCreativeCommon{img/CreativeCommonLogo.jpeg}\n"
	str += "\\def\\includeLogoGN{\\includegraphics[width=0.50cm]{\\logoGliderNorma }}\n"
	str += "\\def\\includeLogoGR{\\includegraphics[width=0.50cm]{\\logoGliderRight }}\n"
	str += "\\def\\includeLogoGL{\\includegraphics[width=0.50cm]{\\logoGliderLeftt }}\n"
	str += "\\def\\includeLogoCC{\\includegraphics[width=0.25cm]{\\logoCreativeCommon }}\n"
	str += "\n"
	str += "\\pagestyle{fancy}\n"
	str += "\\def\\makestylefancyContent{%\n"
	str += "	\\fancyhf{}\n"
	str += "	\\fancyhead[LE]{\n"
	str += "		\\includegraphics[width=0.5cm]{\\logoGliderLeftt }\n"
	str += "		\\hfill\n"
	str += "		\\prenomNom \n"
	str += "		\\hfill\n"
	str += "		\\titreGeneral  -- \\titreSpecialite\n"
	str += "	}\n"
	str += "	\\fancyfoot[LE]{\n"
	str += "		\\includegraphics[width=0.5cm]{\\logoGliderLeftt } \\hfill\n"
	str += "		\\includeLogoCC  \\prenomNom  -- \\today -- \\emph{Curriculum Generator (Python)} \\hfill %% \\copyright\n"
	str += "		\\thepage /\\pageref{LastPage}\n"
	str += "	}\n"
	str += "\n"
	str += "	\\fancyhead[RO]{\n"
	str += "		\\titreGeneral  -- \\titreSpecialite\n"
	str += "		\\hfill\n"
	str += "		\\prenomNom \n"
	str += "		\\hfill\n"
	str += "		\\includegraphics[width=0.5cm]{\\logoGliderRight }\n"
	str += "	}\n"
	str += "	\\fancyfoot[RO]{\n"
	str += "		\\thepage /\\pageref{LastPage} \\hfill\n"
	str += "		\\includeLogoCC  \\prenomNom  -- \\today -- \\emph{Curriculum Generator (Python)} \\hfill %% \\copyright\n"
	str += "		\\includegraphics[width=0.5cm]{\\logoGliderRight }\n"
	str += "	}\n"
	str += "	\\renewcommand{\\headrulewidth}{0.25pt}\n"
	str += "	\\renewcommand{\\footrulewidth}{0.5pt}\n"
	str += "}%\n"
	str += "\\makestylefancyContent\n"
	return str

def getHyperSetup() : 
	str = "%% Some SetUp\n"
	str += "\AfterPreamble{\hypersetup{\n"
	str += "		pdfauthor={\\prenomNom},\n"
	str += "		pdftitle={\\titreGeneral ~-- \\titreSpecialite },\n"
	str += "		pdfsubject={\\titreGeneral ~-- \\titreSpecialite },\n"
	str += "		pdfkeywords={\\motsClefs },\n"
	str += "		pdfproducer={PDFLaTeX (creation)},\n"
	str += "		pdfcreator={PDFLaTeX (production)}\n"
	str += "		%% urlcolor=blue,\n"
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
	str += "\\quote{ \\quotationCitation }\n"
	str += "%% \\phone{00 00 00 00 00}\n"
	str += "%% \\fax{00 00 00 00 00}\n"
	str += "%% \\photo[64pt][0.4pt]{img/logo_glider.png}\n"
	str += "%% \\phone[mobile]{\\portable } %% \\phone[mobile]{06~12~34~56~78}\n"
	str += "%% \\phone[fixed]{01~01~01~01~01}\n"
	str += "%% \\phone[fax]{01~01~01~01~01}\n"
	str += "\\social[linkedin]{ LinkedInProfile }		%% https://www.linkedin.com/in/.../\n"
	str += "\\social[github]{ GitHubProfile }			%% https://github.com/...\n"
	str += "%% \\social[facebook]{ FaceBookProfile }	%% https://www.facebook.com/...\n"
	str += "\\social[twitter]{ TwitterPage }			%% https://twitter.com/...\n"
	str += "%% \\extrainfo{ More Informations (Age...}\n"
	return str

