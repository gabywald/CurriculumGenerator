
SUBDIRS=Anna-Carlsen_RH Angela-Bennett_DevJavaJ2EE Antoine-Adelont_DevJunior Anne-Legendre_DevPython Emmanuel-Colin_DevPython

all : $(SUBDIRS)
	for d in $(SUBDIRS);	\
	do	\
		$(MAKE) --directory=$$d;	\
	done
	
clean : $(SUBDIRS)
	for d in $(SUBDIRS);	\
	do	\
		$(MAKE) clean --directory=$$d;	\
	done

cleanpdf : $(SUBDIRS)
	for d in $(SUBDIRS);	\
	do	\
		$(MAKE) cleanpdf --directory=$$d;	\
	done

