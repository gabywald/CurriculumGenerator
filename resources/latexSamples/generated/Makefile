SUBDIRS=Banking.Orange Casual.Green Classic.Blue OldStyle.Red

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

