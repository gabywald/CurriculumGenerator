## naming WITHOUT the extensions [.tex] or [.bib]
LATEXFILE=sampleCurriculum

## the local software...
CCPDFLA=pdflatex
CCPHTML=latex2html
CCP2RTF=latex2rtf

all : pdflatex # html rtf
	@echo 'DONE'

pdflatex : $(LATEXFILE).tex # $(BIBTEFILE).bib
	$(CCPDFLA) $(LATEXFILE).tex
	$(CCPDFLA) $(LATEXFILE).tex
	$(CCPDFLA) $(LATEXFILE).tex
	@echo 'PDFLATEX DONE'

html : $(LATEXFILE).tex # $(BIBTEFILE).bib
	$(CCPHTML) $(LATEXFILE).tex
	@echo 'HTML DONE'
	
rtf : $(LATEXFILE).tex # $(BIBTEFILE).bib
	$(CCP2RTF) -Z9 $(LATEXFILE).tex
	@echo 'RTF DONE' 

clean : mrproper
	rm $(LATEXFILE).log
	# rm $(LATEXFILE).lot
	# rm $(LATEXFILE).lof
	# rm $(LATEXFILE).dvi
	# rm $(LATEXFILE).pdf
	@echo 'CLEAN DONE'

mrproper : $(LATEXFILE).out $(LATEXFILE).aux # $(LATEXFILE).bbl $(LATEXFILE).blg $(LATEXFILE).toc
	rm $(LATEXFILE).out
	rm $(LATEXFILE).aux
	# rm $(LATEXFILE).toc
	# rm $(LATEXFILE).bbl
	# rm $(LATEXFILE).blg
	@echo 'MRPROPER DONE'
