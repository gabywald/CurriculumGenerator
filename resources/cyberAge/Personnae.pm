package Personnae;

use strict;

## idées : générer variables d'en-tête fichiers [.tex] 
## include [TEX] du reste du fichier à générer en PDF
## ## ++ Makefile associés et compilé

sub new {
	my $class	= shift;
	$class		= ref($class) || $class;

	my $self	= {};

	$self->{NAME}	= undef;
	$self->{IMAGE}	= "img/personnageAnonymous.jpg"; ## undef;
	$self->{TITLE}	= undef;
	$self->{PV}		= undef;
	$self->{IMPACT}	= undef;
	$self->{SAN}	= undef;
	$self->{APP}	= undef;
	$self->{CON}	= undef;
	$self->{DEX}	= undef;
	$self->{FOR}	= undef;
	$self->{TAI}	= undef;
	$self->{EDU}	= undef;
	$self->{INT}	= undef;
	$self->{POU}	= undef;
	$self->{CYBEREQUI}	= ();
	$self->{CAILLOUX}	= ();
	$self->{PROGRAMS}	= ();
	$self->{TALENTS}	= ();
	$self->{LIGHTBIO}	= ();
	$self->{AGE}		= undef;
	$self->{SEXE}		= undef;
	$self->{PARRAIN}	= undef;
	$self->{ARGENT}		= undef;
	$self->{METIER}		= undef;
	$self->{DIVERS}		= undef;
	$self->{BIOGRAPHY}	= (); ## undef
	
	$self->{CONCEPT}	= undef;

	bless($self, $class);
	return $self;
}

sub setConcept {
	my $self			= shift;
	$self->{CONCEPT}	= shift;
}

sub getConcept {
	my $self			= shift;
	return $self->{CONCEPT};
}

sub toString {
	my $self = shift;
	my $toReturn = "";
	
	$toReturn .= $self->getName()." : ";
	$toReturn .= $self->getSexe().", ".$self->getAge()." ans. ";
	$toReturn .= "\n";
	$toReturn .= $self->getTitle()." (".$self->getMetier()."). ";
	$toReturn .= "\n";
	
	my @biography = $self->getLightBiography();
	foreach my $item (@biography) 
		{ $toReturn .= "\t".$item."\n"; }
	
	return $toReturn."\n\n\n";
}

sub toStringPersonnae {
	my $self = shift;
	my $toReturn = "";
	
	$toReturn .= "BEGIN personnae\n";
	$toReturn .= "CONCEPT ".$self->getConcept()."\n";
	$toReturn .= "NAME ".$self->getName()."\n";
	$toReturn .= "IMAGE ".$self->getImage()."\n";
	$toReturn .= "TITLE ".$self->getTitle()."\n";
	$toReturn .= "PV ".$self->getPV()."\n";
	$toReturn .= "IMPACT ".$self->getImpact()."\n";
	$toReturn .= "SAN ".$self->getSAN()."\n";
	$toReturn .= "APP ".$self->getAPP()."\n";
	$toReturn .= "CON ".$self->getCON()."\n";
	$toReturn .= "DEX ".$self->getDEX()."\n";
	$toReturn .= "FOR ".$self->getFOR()."\n";
	$toReturn .= "TAI ".$self->getTAI()."\n";
	$toReturn .= "EDU ".$self->getEDU()."\n";
	$toReturn .= "INT ".$self->getINT()."\n";
	$toReturn .= "POU ".$self->getPOU()."\n";
	$toReturn .= "BEGIN cyberequipement"."\n";
	my @cyberEqus = $self->getCyberEquipments();
	my $CEcount = @cyberEqus;
	foreach my $item (@cyberEqus) 
		{ $toReturn .= "".$item."\n"; }
	$toReturn .= "END cyberequipement"."\n";
	$toReturn .= "BEGIN cailloux"."\n";
	my @cailloux = $self->getCailloux();
	foreach my $item (@cailloux) 
		{ $toReturn .= "".$item."\n"; }
	$toReturn .= "END cailloux"."\n";
	$toReturn .= "AGE ".$self->getAge()."\n";
	$toReturn .= "SEXE ".$self->getSexe()."\n";
	$toReturn .= "PARRAIN ".$self->getParrain()."\n";
	$toReturn .= "ARGENT ".$self->getArgent()."\n";
	$toReturn .= "DIVERS ".$self->getDivers()."\n";
	$toReturn .= "METIER ".$self->getMetier()."\n";
	$toReturn .= "BEGIN talents"."\n";
	my @talents = $self->getTalents();
	foreach my $item (@talents) 
		{ $toReturn .= "".$item."\n"; }
	$toReturn .= "END talents"."\n";
	$toReturn .= "BEGIN lightbio"."\n";
	my @lightBiography = $self->getLightBiography();
	foreach my $item (@lightBiography) 
		{ $toReturn .= "".$item."\n"; }
	$toReturn .= "END lightbio "."\n";
	$toReturn .= "BEGIN biography"."\n";
	my @biography = $self->getBiography();
	foreach my $item (@biography) 
		{ $toReturn .= "".$item."\n"; }
	$toReturn .= "END biography"."\n";
	$toReturn .= "END personnae"."\n";
	
	return $toReturn."\n\n";
}

sub toLaTeX {
	my $self = shift;
	my $toReturn = "";
	$toReturn .= "\\input{personnaeHeader.tex}\n\n"; 

	$toReturn .= "\\def\\PersonnaeName{ ".$self->getName()." }\n\n"; 

	$toReturn .= "\\def\\FRdefCharacterSheetHeaderTitle{Feuille de Personnage Cyber Age -- \\emph{\\PersonnaeName } }\n\n"; 

	$toReturn .= "\\def\\CApersoName{ {\\footnotesize \\PersonnaeName } }\n";
	$toReturn .= "\\def\\CApersoImage{".$self->getImage()."}\n";
	$toReturn .= "\\def\\CApersoTitle{ {\\footnotesize ".$self->getTitle()."} }\n";
	$toReturn .= "\\def\\CApersoPV{".$self->getPV()."}\n";
	$toReturn .= "\\def\\CApersoIMPACT{".$self->getImpact()."}\n";
	$toReturn .= "\\def\\CApersoSAN{".$self->getSAN()."}\n\n";

	$toReturn .= "\\def\\CApersoAPP{".$self->getAPP()."}\n";
	$toReturn .= "\\def\\CApersoCON{".$self->getCON()."}\n";
	$toReturn .= "\\def\\CApersoDEX{".$self->getDEX()."}\n";
	$toReturn .= "\\def\\CApersoFOR{".$self->getFOR()."}\n";
	$toReturn .= "\\def\\CApersoTAI{".$self->getTAI()."}\n";
	$toReturn .= "\\def\\CApersoEDU{".$self->getEDU()."}\n";
	$toReturn .= "\\def\\CApersoINT{".$self->getINT()."}\n";
	$toReturn .= "\\def\\CApersoPOU{".$self->getPOU()."}\n\n";

	$toReturn .= "\\def\\CApersoPES{".(int($self->getAPP())*5)."}\n";
	$toReturn .= "\\def\\CApersoSTA{".(int($self->getCON())*5)."}\n";
	$toReturn .= "\\def\\CApersoAGI{".(int($self->getDEX())*5)."}\n";
	$toReturn .= "\\def\\CApersoPUI{".(int($self->getFOR())*5)."}\n";
	$toReturn .= "\\def\\CApersoCOR{".(int($self->getTAI())*5)."}\n";
	$toReturn .= "\\def\\CApersoKNO{".(int($self->getEDU())*5)."}\n";
	$toReturn .= "\\def\\CApersoIUI{".(int($self->getINT())*5)."}\n";
	$toReturn .= "\\def\\CApersoVOL{".(int($self->getPOU())*5)."}\n\n";

	$toReturn .= "\\def\\CApersoAGE{".$self->getAge()."}\n";
	$toReturn .= "\\def\\CApersoSEXE{".$self->getSexe()."}\n";
	$toReturn .= "\\def\\CApersoPARRAIN{".$self->getParrain()."}\n";
	$toReturn .= "\\def\\CApersoARGENT{".$self->getArgent()."}\n";
	$toReturn .= "\\def\\CApersoDIVERS{".$self->getDivers()."}\n";
	$toReturn .= "\\def\\CApersoMETIER{".$self->getMetier()."}\n\n";

	$toReturn .= "\\def\\CApersoTALENT{%\n";
	$toReturn .= "\t\\begin{itemize}\n";
	my @talents = $self->getTalents();
	my $TAcount = @talents;
	foreach my $item (@talents) 
		{ $toReturn .= "\t\t\\item ".$item." \%\n"; }
	for (my $i = $TAcount ; $i < 5 ; $i++)
		{ $toReturn .= "\t\t\\item \\dotfill\n"; }
	$toReturn .= "\t\\end{itemize}\n";
	$toReturn .= "}%\n\n";

	$toReturn .= "\\def\\CApersoCYBEQU{%\n";
	$toReturn .= "\t\\begin{itemize}\n";
	my @cyberEqus = $self->getCyberEquipments();
	my $CEcount = @cyberEqus;
	foreach my $item (@cyberEqus) 
		{ $toReturn .= "\t\t\\item ".$item."\n"; }
	for (my $i = $CEcount ; $i < ((@talents < 5)?5:(@talents-@cyberEqus+1)) ; $i++)
		{ $toReturn .= "\t\t\\item \\dotfill\n"; }
	$toReturn .= "\t\\end{itemize}\n";
	$toReturn .= "}%\n\n";
	
	$toReturn .= "\\def\\CApersoCAILLO{%\n";
	$toReturn .= "\t\\begin{itemize}\n";
	my @cailloux = $self->getCailloux();
	my $CAcount = @cailloux;
	foreach my $item (@cailloux) 
		{ $toReturn .= "\t\t\\item ".$item."\n"; }
	for (my $i = $CAcount ; $i < 5 ; $i++)
		{ $toReturn .= "\t\t\\item \\dotfill\n"; }
	$toReturn .= "\t\\end{itemize}\n";
	$toReturn .= "}%\n\n";
	
	$toReturn .= "\\def\\CApersoPROGRA{%\n";
	$toReturn .= "\t\\begin{itemize}\n";
	my @programmes = $self->getProgrammes();
	my $PRcount = @programmes;
	foreach my $item (@programmes) 
		{ $toReturn .= "\t\t\\item ".$item."\n"; }
	for (my $i = $PRcount ; $i < 5 ; $i++)
		{ $toReturn .= "\t\t\\item \\dotfill\n"; }
	$toReturn .= "\t\\end{itemize}\n";
	$toReturn .= "}%\n\n";
	
	$toReturn .= "\\def\\CApersoBIOLIG{%\n";
	$toReturn .= "\t\\begin{itemize}\n";
	my @lightBiography = $self->getLightBiography();
	foreach my $item (@lightBiography) 
		{ $toReturn .= "\t\t\\item ".$item."\n"; }
	$toReturn .= "\t\\end{itemize}\n";
	$toReturn .= "}%\n\n";
	
	$toReturn .= "\\def\\CApersoBIOBIO{%\n";
	my @biography = $self->getBiography();
	foreach my $item (@biography) 
		{ $toReturn .= "\t\t".$item."\n"; }
	$toReturn .= "}%\n\n";

	$toReturn .= "\\input{personnaeBottom.tex}\n";
	return $toReturn;
}

sub setName {
	my $self		= shift;
	$self->{NAME}	= shift;
}

sub getName {
	my $self		= shift;
	return $self->{NAME};
}

sub setImage {
	my $self		= shift;
	$self->{IMAGE}	= shift;
}

sub getImage {
	my $self		= shift;
	return $self->{IMAGE};
}

sub setTitle {
	my $self		= shift;
	$self->{TITLE}	= shift;
}

sub getTitle {
	my $self		= shift;
	return $self->{TITLE};
}

sub setPV {
	my $self		= shift;
	$self->{PV}		= shift;
}

sub getPV {
	my $self		= shift;
	return $self->{PV};
}

sub setSAN {
	my $self		= shift;
	$self->{SAN}	= shift;
}

sub getSAN {
	my $self		= shift;
	return $self->{SAN};
}

sub setImpact {
	my $self		= shift;
	$self->{IMPACT}	= shift;
}

sub getImpact {
	my $self		= shift;
	return $self->{IMPACT};
}

sub setAPP {
	my $self		= shift;
	$self->{APP}	= shift;
}

sub getAPP {
	my $self		= shift;
	return $self->{APP};
}

sub setCON {
	my $self		= shift;
	$self->{CON}	= shift;
}

sub getCON {
	my $self		= shift;
	return $self->{CON};
}

sub setDEX {
	my $self		= shift;
	$self->{DEX}	= shift;
}

sub getDEX {
	my $self		= shift;
	return $self->{DEX};
}

sub setFOR {
	my $self		= shift;
	$self->{FOR}	= shift;
}

sub getFOR {
	my $self		= shift;
	return $self->{FOR};
}

sub setTAI {
	my $self		= shift;
	$self->{TAI}	= shift;
}

sub getTAI {
	my $self		= shift;
	return $self->{TAI};
}

sub setEDU {
	my $self		= shift;
	$self->{EDU}	= shift;
}

sub getEDU {
	my $self		= shift;
	return $self->{EDU};
}

sub setINT {
	my $self		= shift;
	$self->{INT}	= shift;
}

sub getINT {
	my $self		= shift;
	return $self->{INT};
}

sub setPOU {
	my $self		= shift;
	$self->{POU}	= shift;
}

sub getPOU {
	my $self		= shift;
	return $self->{POU};
}

sub addCyberEquipments {
	my $self			= shift;
	while(@_) { push (@{$self->{CYBEREQUI}},shift); }
}

sub getCyberEquipments {
	my $self = shift;
	return ($self->{CYBEREQUI})?@{$self->{CYBEREQUI}}:();
}

sub addCailloux {
	my $self			= shift;
	while(@_) { push (@{$self->{CAILLOUX}},shift); }
}

sub getCailloux {
	my $self = shift;
	return ($self->{CAILLOUX})?@{$self->{CAILLOUX}}:();
}

sub addProgrammes {
	my $self			= shift;
	while(@_) { push (@{$self->{PROGRAMS}},shift); }
}

sub getProgrammes {
	my $self = shift;
	return ($self->{PROGRAMS})?@{$self->{PROGRAMS}}:();
}

sub addTalents {
	my $self			= shift;
	while(@_) { push (@{$self->{TALENTS}},shift); }
}

sub getTalents {
	my $self = shift;
	return ($self->{TALENTS})?@{$self->{TALENTS}}:();
}

sub addLightBiography {
	my $self			= shift;
	while(@_) { push (@{$self->{LIGHTBIO}},shift); }
}

sub getLightBiography {
	my $self = shift;
	return ($self->{LIGHTBIO})?@{$self->{LIGHTBIO}}:();
}

sub setAge {
	my $self		= shift;
	$self->{AGE}	= shift;
}

sub getAge {
	my $self		= shift;
	return $self->{AGE};
}

sub setSexe {
	my $self		= shift;
	$self->{SEXE}	= shift;
}

sub getSexe {
	my $self		= shift;
	return $self->{SEXE};
}

sub setParrain {
	my $self		= shift;
	$self->{PARRAIN}	= shift;
}

sub getParrain {
	my $self		= shift;
	return $self->{PARRAIN};
}

sub setArgent {
	my $self			= shift;
	$self->{ARGENT}	= shift;
}

sub getArgent {
	my $self		= shift;
	return $self->{ARGENT};
}

sub setMetier {
	my $self		= shift;
	$self->{METIER}	= shift;
}

sub getMetier {
	my $self		= shift;
	return $self->{METIER};
}

sub setDivers {
	my $self		= shift;
	$self->{DIVERS}	= shift;
}

sub getDivers {
	my $self		= shift;
	return $self->{DIVERS};
}

## sub setBiography {
## 	my $self			= shift;
## 	$self->{BIOGRAPHY}	= shift;
## }

## sub getBiography {
## 	my $self		= shift;
## 	return $self->{BIOGRAPHY};
## }

sub addBiography {
	my $self			= shift;
	while(@_) { push (@{$self->{BIOGRAPHY}},shift); }
}

sub getBiography {
	my $self = shift;
	return ($self->{BIOGRAPHY})?@{$self->{BIOGRAPHY}}:();
}

1;
