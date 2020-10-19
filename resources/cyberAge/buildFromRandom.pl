#!/usr/bin/perl -w

use strict;

## use Switch;

use lib '.';
use Personnae;

my $toShowAllParse = ( (@ARGV >= 1) && ($ARGV[0] eq "show") );

## ## conf/dataRPG/biographyCyberAge.txt et autres docs du meme répertoire...
my $dirToRSCfiles	= "./";
my $fileTalentsCA	= $dirToRSCfiles."talentsCyberAge.txt";
my $fileBiograpCA	= $dirToRSCfiles."biographyCyberAge.txt";
my $fileMetiersCA	= $dirToRSCfiles."metiersEtTalentsCyberAge.txt";
my $fileEquipmeCA	= $dirToRSCfiles."tableEquipementsCyberAge.txt";

## open (INPUT, "<".$fileTalentsCA ) or die "File [".$fileTalentsCA."] not found !";
## while (my $line = <INPUT>) {
## 	$line =~ s/[\r\n]//g;
## 	print "\t {".$line."}\n";
## } ## END "while (my $line = <INPUT>)"
## close INPUT;

my %talents = ();
open (INPUT, "<".$fileTalentsCA ) or die "File [".$fileTalentsCA."] not found !";
while (my $line = <INPUT>) {
	$line =~ s/[\r\n]//g;
	## print "\t {".$line."}\n";
	if ($line =~ /^(.*?)\t(.*?)(\t\[(.*?)\])?$/) {
		my $talent = $1;
		my $baseSi = $2;
		my $listTa = $4;
		if ($baseSi eq "X")		{ $baseSi = 0; }
		elsif ($baseSi eq "-4")	{ $baseSi = 15; }
		elsif ($baseSi eq "-2")	{ $baseSi = 30; }
		elsif ($baseSi eq "0")	{ $baseSi = 50; }
		elsif ($baseSi eq "1")	{ $baseSi = 60; }
		elsif ($baseSi eq "2")	{ $baseSi = 80; }
		if ( ! defined $listTa) { $listTa = ""; }
		## print "\t\t{".$talent."}\t[".$baseSi."]\t{".$listTa."}\n";
		if ($listTa ne "") {
			my @possibles		= split(";", $listTa);
			my @datas			= ($baseSi, \@possibles);
			$talents{$talent}	= \@datas;
		} else { 
			my @empty			= ();
			my @datas			= ($baseSi, \@empty);
			$talents{$talent}	= \@datas; 
		}
	} ## END ...
} ## END "while (my $line = <INPUT>)"
close INPUT;

if ($toShowAllParse) {
	print "\t TALENTS / COMPETENCES\n";
	for my $talent (sort(keys(%talents))) {
		my @couplePair	= @{$talents{$talent}};
		my $value		= $couplePair[0];
		my @possibles	= @{$couplePair[1]};
		print "\t\t [".$talent."] (".$value."%)\n";
		for my $possible (@possibles) 
			{ print "\t\t\t {".$possible."}\n"; }
	} ## END "for my $talent (sort(keys(%talents)))"
	getc();
} ## "if ($toShowAllParse)"

my %metiers = ();
open (INPUT, "<".$fileMetiersCA ) or die "File [".$fileMetiersCA."] not found !";
while (my $line = <INPUT>) {
	$line =~ s/[\r\n]//g;
	## print "\t {".$line."}\n";
	if ($line =~ /^(.*?)\t(.*?)$/) {
		my @competences	= split(";", $2);
		## print "\t\t**[".$1."]**{".@competences."}**\n";
		## for my $elt (@competences)
		## 	{ print "\t\t\t {".$elt."}\n"; }
		$metiers{$1}	= \@competences;
	} ## END ...
} ## END "while (my $line = <INPUT>)"
close INPUT;

print "\t METIERS\n";
for my $metier (sort(keys(%metiers))) {
	print "\t\t [".$metier."]\n";
	my @competences = @{$metiers{$metier}};
	for my $competence (@competences) 
		{ print "\t\t\t {".$competence."}\n"; }
} ## END "for my $metier (sort(keys(%metiers)))"
if ($toShowAllParse) 
	{ getc(); }

my %equipments = ();
## my @currentTable	= ();
## my $currentTabName	= undef;
my $currentEquTable = undef; ## new BiographicTable();
open (INPUT, "<".$fileEquipmeCA ) or die "File [".$fileEquipmeCA."] not found !";
while (my $line = <INPUT>) {
	$line =~ s/[\r\n]//g;
	## print "\t {".$line."}\n";
	if ($line =~ /^Table (.*?)(\t(.*?))?$/) {
		if (defined $currentEquTable) {
			$equipments{$currentEquTable->getNAME()} = $currentEquTable;
			## print "***** ***** ***** ***** ***** \n";
			## print $currentBioTable->toString();
			## print "***** ***** ***** ***** ***** \n";
			$currentEquTable	= undef;
		} ## END "if (defined $currentTabName)"
		$currentEquTable = new BiographicTable();
		$currentEquTable->setNAME( $1 );
		if (defined $2) { $currentEquTable->setCOMMENT( $2 ); }
	} ## END ...
	elsif ($line =~ /^\t(.*?)(\t\[(.*?)\])?$/) {
		$currentEquTable->addCONTENTS($1);
		if (defined $3) { $currentEquTable->addLINKSTO($3); }
		else { $currentEquTable->addLINKSTO( "" ); }
		$currentEquTable->addADDINS( "" );
	} ## END ...
	## else { print "\t{{".$line."}}\n"; }
} ## END "while (my $line = <INPUT>)"
if (defined $currentEquTable) 
	{ $equipments{$currentEquTable->getNAME()} = $currentEquTable; }
close INPUT;

if ($toShowAllParse) {
	print "\t EQUIPEMENTS\n";
	for my $element (sort(keys(%equipments))) {
		## print "\t\t [".$element."]\n";
		print "\t\t\t *****\n".$equipments{$element}->toString()."\t\t\t *****\n";
	} ## END "for my $element (sort(keys(%equipments)))"
	getc();
} ## "if ($toShowAllParse)"

use BiographicTable;
use BiographicElement;

my %biographics = ();
## my @currentTable	= ();
## my $currentTabName	= undef;
my $currentBioTable = undef; ## new BiographicTable();
open (INPUT, "<".$fileBiograpCA ) or die "File [".$fileBiograpCA."] not found !";
while (my $line = <INPUT>) {
	$line =~ s/[\r\n]//g;
	## print "\t {".$line."}\n";
	if ($line =~ /^Table (.*?)(\t(.*?))?$/) {
		if (defined $currentBioTable) {
			$biographics{$currentBioTable->getNAME()} = $currentBioTable;
			## print "***** ***** ***** ***** ***** \n";
			## print $currentBioTable->toString();
			## print "***** ***** ***** ***** ***** \n";
			$currentBioTable	= undef;
		} ## END "if (defined $currentTabName)"
		$currentBioTable = new BiographicTable();
		$currentBioTable->setNAME( $1 );
		if (defined $2) { $currentBioTable->setCOMMENT( $2 ); }
	} ## END ...
	elsif ($line =~ /^\t(.*?)(\t\[(.*?)\])?(\t\{(.*?)\})?$/) {
		## print "\t\t 1: [".$1."]\t "
		## 			."2: [".((defined $2)?$2:"<null>")."]\t 3: [".((defined $3)?$3:"<null>")."]\t "
		## 			."4: [".((defined $4)?$4:"<null>")."]\t 5: [".((defined $5)?$5:"<null>")."]\n";
		$currentBioTable->addCONTENTS($1);
		if (defined $3) { $currentBioTable->addLINKSTO($3); }
		else { $currentBioTable->addLINKSTO( "" ); }
		if (defined $5) { $currentBioTable->addADDINS($5); }
		else { $currentBioTable->addADDINS( "" ); }
		## if (defined $5) { print "*****".$5."\n"; }
	} ## END ...
	## else { print "\t{{".$line."}}\n"; }
} ## END "while (my $line = <INPUT>)"
if (defined $currentBioTable) 
	{ $biographics{$currentBioTable->getNAME()} = $currentBioTable; }
close INPUT;

if ($toShowAllParse) {
	print "\t BIOGRAPHIE\n";
	for my $element (sort(keys(%biographics))) {
		## print "\t\t [".$element."]\n";
		print "\t\t\t *****\n".$biographics{$element}->toString()."\t\t\t *****\n";
	} ## END "for my $element (sort(keys(%biographics)))"
	getc();
} ## "if ($toShowAllParse)"

my $personnaeToOuput = new Personnae();

## Etape 1: Imaginer un concept
my $concept = undef;
do {
	print "\t **** Concept ***** \n";
	$concept = <STDIN>;
	chomp($concept);
	print "\t\t Concept: {".$concept."}\n";
	## print "\t\t{".( ( (defined $concept) )?"true":"false" )."}\n";
	## print "\t\t{".( ( ($concept eq "") )?"true":"false" )."}\n";
	## print "\t\t{".( ( (defined $concept) && ($concept eq "") )?"true":"false" )."}\n";
} while ( (defined $concept) && ($concept eq "") ); 
$personnaeToOuput->setConcept( $concept );
$personnaeToOuput->setTitle( $concept );
## Etape 2: Scores de caractéristiques
## ## Caractéristiques	Score 	Dérivée
## ## Apparence			3D6 	Prestance		= APP x5%
## ## Constitution		3D6 	Endurance		= CON x5%
## ## Dextérité			3D6 	Agilité			= DEX x5%
## ## Force				3D6 	Puissance		= FOR x5%
## ## Taille			2D6+6 	Corpulence		= TAI x5%
## ## Éducation			3D6+6 	Connaissance	= EDU x5%
## ## Intelligence		2D6+6 	Intuition		= INT x5%
## ## Pouvoir			3D6 	Volonté			= POU x5%
sub randomizer {
	my $whatDices	= shift;
	my $multi		= 0;
	my $kind		= 0;
	my $adder		= 0;
	if ($whatDices =~ /^([0-9])D([0-9]+)\+?([0-9]+)?$/) {
		$multi		= $1;
		$kind		= $2;
		$adder		= $3;
		## print "\t\t multi: [".$multi."]\n";
		## print "\t\t kind-: [".$kind."]\n";
		## if (defined $adder) { print "\t\t adder: [".$adder."]\n"; }
		## print "\t ***** ***** ***** \n";
		my $value = 0;
		do {
			$value = 0; 
			for (my $i = 0 ; $i < $multi ; $i++) 
				{ $value += (int(rand($kind))+1); }
			if (defined $adder) { $value += $adder; }
		} while ($value <= 8);
		return $value;
	} else { print "\t ??{".$whatDices."} ?? \n";return 0; }
} ## sub randomizer
my $APP = &randomizer("3D6");
my $CON = &randomizer("3D6");
my $DEX = &randomizer("3D6");
my $FOR = &randomizer("3D6");
my $TAI = &randomizer("2D6+6");
my $EDU = &randomizer("3D6+6");
my $INT = &randomizer("2D6+6");
my $POU = &randomizer("3D6");
print "\t **** Attributs ***** \n";
my $validateAttributes = undef;
do {
	print "\t\t APP: (".$APP.")\n";
	print "\t\t CON: (".$CON.")\n";
	print "\t\t DEX: (".$DEX.")\n";
	print "\t\t FOR: (".$FOR.")\n";
	print "\t\t TAI: (".$TAI.")\n";
	print "\t\t EDU: (".$EDU.")\n";
	print "\t\t INT: (".$INT.")\n";
	print "\t\t POU: (".$POU.")\n";
	print "\t Valider ? [y/N]";
	$validateAttributes = <STDIN>;
	
	chomp($validateAttributes);
	print "\t\t Validation: {".$validateAttributes."}\n";
	
	my $attributesDetection = "(APP|CON|DEX|FOR|TAI|EDU|INT|POU)";
	if ( ($validateAttributes ne "Y") && ($validateAttributes ne "y") ) {
		print "\t Nouveau tirage ? [All|XXX|n]";
		my $newTirage = <STDIN>;
		
		chomp($newTirage);
		print "\t\t newTirage: {".$newTirage."}\n";
		
		if ($newTirage eq "All") {
			$APP = &randomizer("3D6");
			$CON = &randomizer("3D6");
			$DEX = &randomizer("3D6");
			$FOR = &randomizer("3D6");
			$TAI = &randomizer("2D6+6");
			$EDU = &randomizer("3D6+6");
			$INT = &randomizer("2D6+6");
			$POU = &randomizer("3D6");
		} elsif ($newTirage =~ /$attributesDetection/) {
			print "\t => {".$1."}\n";
			if ($1 eq "APP") { $APP = &randomizer("3D6"); }
			elsif ($1 eq "CON") { $CON = &randomizer("3D6"); }
			elsif ($1 eq "DEX") { $DEX = &randomizer("3D6"); }
			elsif ($1 eq "FOR") { $FOR = &randomizer("3D6"); }
			elsif ($1 eq "TAI") { $TAI = &randomizer("2D6+6"); }
			elsif ($1 eq "EDU") { $EDU = &randomizer("3D6+6"); }
			elsif ($1 eq "INT") { $INT = &randomizer("2D6+6"); }
			elsif ($1 eq "POU") { $POU = &randomizer("3D6"); }
		} else {
			my $exchange = undef;
			do {
				print "\t Echange valeurs [XXX:YYY:{0-9}+|n]\n";
				$exchange = <STDIN>;
				
				chomp($exchange);
				print "\t\t exchange: {".$exchange."}\n";
				
			} while($exchange !~ /^($attributesDetection:$attributesDetection:([0-9]+)|N|n)$/);
			if ( ($1 ne "N") && ($1 ne "n") ) { 
				my $first = $1;
				my $secon = $2;
				my $value = $3;
				print "\t\t first: [".$first."]\n";
				print "\t\t secon: [".$secon."]\n";
				print "\t\t value: [".$value."]\n";
				if ($first eq "APP") { $APP -= $value; }
				elsif ($first eq "CON") { $CON -= $value; }
				elsif ($first eq "DEX") { $DEX -= $value; }
				elsif ($first eq "FOR") { $FOR -= $value; }
				elsif ($first eq "TAI") { $TAI -= $value; }
				elsif ($first eq "EDU") { $EDU -= $value; }
				elsif ($first eq "INT") { $INT -= $value; }
				elsif ($first eq "POU") { $POU -= $value; }
				if ($secon eq "APP") { $APP += $value; }
				elsif ($secon eq "CON") { $CON += $value; }
				elsif ($secon eq "DEX") { $DEX += $value; }
				elsif ($secon eq "FOR") { $FOR += $value; }
				elsif ($secon eq "TAI") { $TAI += $value; }
				elsif ($secon eq "EDU") { $EDU += $value; }
				elsif ($secon eq "INT") { $INT += $value; }
				elsif ($secon eq "POU") { $POU += $value; }
			} ## END "if ( ($1 ne "N") && ($1 ne "n") )"
		} ## ...
	} ## if ( ($validateAttributes ne "Y") || ($validateAttributes ne "y") )
} while( ($validateAttributes ne "Y") && ($validateAttributes ne "y") );

$personnaeToOuput->setAPP( $APP );
$personnaeToOuput->setCON( $CON );
$personnaeToOuput->setDEX( $DEX );
$personnaeToOuput->setFOR( $FOR );
$personnaeToOuput->setTAI( $TAI );
$personnaeToOuput->setEDU( $EDU );
$personnaeToOuput->setINT( $INT );
$personnaeToOuput->setPOU( $POU );

## Etape 3: Autres valeurs
## ## Aplomb				= 0
## ## Santé Mentale (SAN)	= POU x5%
## ## Points de Vie		= (CON + TAI) / 2, arrondi à l'entier supérieur
## ## Seuil de Blessure	= Points de Vie / 2, arrondi à l'entier inférieur
## ## Points de Magie		= POU
## ## Impact				= voir la table ci-dessous
## ## ## ## FOR+TAI  	Impact
## ## ## ## 02 à 12  	  -4
## ## ## ## 13 à 16  	  -2
## ## ## ## 17 à 24  	  0
## ## ## ## 25 à 32  	  +2
## ## ## ## 33 à 40  	  +4
my $aplomb	= 0;
my $SAN		= $POU*5;
print "\t\t SAN: {".$SAN."}\n";
my $PV		= int( ($CON + $TAI) / 2 );
## ## print "\t\t PV-: {".$PV."}\n";
if ( ($CON + $TAI) % 2 == 1) { $PV++; }
print "\t\t PV-: {".$PV."}\n";
my $seuilBL	= int( $PV / 2 );
print "\t\t sBL: {".$seuilBL."}\n";
my $impact	= ($FOR + $TAI);
## ## print "\t\t imp: {".$impact."}\n";
if ( ($impact >= 02) && ($impact <= 12) )		{ $impact = -4; }
elsif ( ($impact >= 13) && ($impact <= 16) )	{ $impact = -2; }
elsif ( ($impact >= 17) && ($impact <= 24) )	{ $impact = 0; }
elsif ( ($impact >= 25) && ($impact <= 32) )	{ $impact = +2; }
elsif ( ($impact >= 33) && ($impact <= 40) )	{ $impact = +4; }
print "\t\t imp: {".$impact."}\n";

$personnaeToOuput->setSAN( $SAN );
$personnaeToOuput->setPV( $PV );
$personnaeToOuput->setImpact( $impact );
## TODO ++ aplomb 
## TODO ++ seuil de blessure ?

## ## ## Competences Métier : EDU*20 (%)
my $countJobTalent	= 0;
my $countJobMaxims	= $EDU*20;
## ## ## Compétences intérêt perso : INT*10 (%)
my $countPersoTalent	= 0;
my $countPersoMaxims	= $INT*10;

## préparation étape 4 : générer biographie
## ## ## quelques variables pour retenir des éléments supplémentaires liés à la biographie...
my %allowedJob	= ();
my %godfathers	= ();
my %greatTales	= ();
for my $metier (keys %metiers) {
	$allowedJob{$metier} = 0;
	$godfathers{$metier} = 0;
} ## for my $metier (keys %metiers)
## my %moreEquCom	= (); ## ajout équipement ; ajout talent lié à un métier ; ...
my @debtsFrom	= (); ## dettes redevables
my @debtsToTo	= (); ## dettes que l'on doit
my @equipments	= ();
my @cailloux	= ();
my @programmes	= ();
my $argent		= 0;  ## DONE argent de base ?
my $age			= undef;
my $count4biog	= 6;

print "\t **** Age de base ***** \n";
my $validateAge = undef;
do {
	my $tirageAge = int(rand(6)) + 1;
	if ($tirageAge == 1) {
		$age		= 12 + int(rand(16-12+1));
		$argent		= (int(rand(6))+1)*2000;
		$count4biog	= 3;
	} elsif ( ($tirageAge == 2) || ($tirageAge == 3) ) {
		$age		= 17 + int(rand(30-17+1));
		$argent		= (int(rand(6))+1)*1000 + 10000;
		$count4biog	= 6; 
	} elsif ( ($tirageAge == 4) || ($tirageAge == 5) ) {
		$age		= 30 + int(rand(50-30+1));
		$argent		= (int(rand(6))+1)*2000 + 30000;
		$count4biog	= 6;
	} elsif ($tirageAge == 6) {
		$age		= 50 + int(rand(20));
		$argent		= (int(rand(6))+1)*2000 + 5000;
		$count4biog	= 8;
	}
	print "\t\t Age: ".$age." ans. \n";
	print "\t\t Fortune: ".$argent." euros. \n";
	
	if ($age < ($EDU+6))
		{ print "\t WARN \"Age < (EDU+6)\" ! => [".$age."] < [".($EDU+6)."] WARN !\n"; }
	
	print "\t Valider ? [y/N]";
	$validateAge = <STDIN>;
	chomp($validateAge);
} while( ($validateAge ne "Y") && ($validateAge ne "y") );

## my @moreTalents = ();
sub getARandomElementBIOGRAPHIC {
	my $orientation	= $biographics{"d'Orientation"};
	my $be			= undef;
	do {
		my @content	= $orientation->getCONTENTS();
		my @addins	= $orientation->getADDINS();
		my @links	= $orientation->getLINKSTO();
		my $rand	= int(rand(@content));
		my $content	= $content[$rand];
		my $addin	= $addins[$rand];
		my $link	= $links[$rand];
		
		## print "\t'".$content."'\t'".$link."'\t'".$addin."'\n";
		
		if ( ! defined $be) { 
			$be = new BiographicElement();
			$be->setCONTENT( $content );
			if ($addin ne "") { $be->addADDINS( split(';', $addin) ); }
		} else {
			$be->addCONTENT( $content );
			if ($addin ne "") { $be->addADDINS( split(';', $addin) ); }
		}
		
		if ($link ne "") {
			if ($link eq "Cicatrices") {
				$orientation	= $biographics{ "Cicatrices-localisation" };
				@content		= $orientation->getCONTENTS();
				$rand			= int(rand(@content));
				$content		= "Cicatrice : ".$content[$rand];
				
				$orientation	= $biographics{ "Cicatrices-gravité" };
				@content		= $orientation->getCONTENTS();
				$rand			= int(rand(@content));
				$content		.= $content[$rand];
				
				$be->addCONTENT( $content );
				$orientation = undef;
			} else { $orientation = $biographics{ $link }; }
		} ## END "if ($link ne "")"
		else { $orientation = undef; }
	} while (defined $orientation);
	return $be;
}

sub getARandomElementEQUIPMENT {
	my $orientation	= $equipments{"Equipement"};
	my $be			= undef;
	do {
		my @content	= $orientation->getCONTENTS();
		my @addins	= $orientation->getADDINS();
		my @links	= $orientation->getLINKSTO();
		my $rand	= int(rand(@content));
		my $content	= $content[$rand];
		my $addin	= $addins[$rand];
		my $link	= $links[$rand];
		
		## print "\t'".$content."'\t'".$link."'\t'".$addin."'\n";
		
		if ( ! defined $be) { 
			$be = new BiographicElement();
			$be->setCONTENT( $content );
			if ($addin ne "") { $be->addADDINS( split(';', $addin) ); }
		} else {
			$be->addCONTENT( $content );
			if ($addin ne "") { $be->addADDINS( split(';', $addin) ); }
		}
		
		if ($link ne "") 
			{ $orientation = $equipments{ $link }; }
		else { $orientation = undef; }
	} while (defined $orientation);
	return $be;
}

sub addToGreatTalent {
	my $selection	= shift;
	my $initValue	= shift;
	my $addValues	= shift;
	my $jobOrPerso	= shift;
	
	if ( (defined $talents{$selection}) 
			&& ( ! defined $greatTales{$selection}) ) {
		my @values		= @{$talents{$selection}};
		my $initValDef	= $values[0];
		$greatTales{$selection} = $initValDef;
		print "\t\t Selected {".$selection."} setted at ".$initValDef."% (initial / base)\n";
	} ## END "if (defined $talents{$talent})"
	
	if (defined $greatTales{$selection}) {
		print "\t\t Selected {".$selection."} +".$addValues."%\n";
		$greatTales{$selection} += $addValues;
	} else { 
		print "\t\t Selected {".$selection."} setted at ".$initValue."%\n";
		$greatTales{$selection} = $initValue;
	}
	
	if ( (defined $jobOrPerso) && ($jobOrPerso == 1) )
		{ $countJobTalent += $addValues; }
	else
		{ $countPersoTalent += $addValues; }
}

print "\t **** Biographie ***** \n";
## my $limit = $count4biog; ## 10; ## TODO fct(age) cf. plus haut / bas
## for (my $i = 0 ; $i < $limit ; $i++)
## 	{ print &getARandomElement(); }
my @biographicElements = ();
do {
	my $beToShowKeep = &getARandomElementBIOGRAPHIC();
	print "\t\t ".$beToShowKeep->toString()."\n";
	print "\t Conserver ? [Y/n]";
	my $validateBio = <STDIN>;
	chomp($validateBio);
	if ( ($validateBio ne "N") && ($validateBio ne "n") ) 
		{ push (@biographicElements, $beToShowKeep); }
} while (@biographicElements < $count4biog);
print "\t **** Biographie ++ processing ***** \n";
for my $bioELT (@biographicElements) {
	print "\t\t ".$bioELT->toString()."\n";
	
	$personnaeToOuput->addLightBiography( $bioELT->getCONTENT() );
	
	my @addins = $bioELT->getADDINS();
	for my $addin (@addins) {
		print "\t\t\t [".$addin."]\n";
		# %allowedJob
		# %godfathers
		# %greatTales
		my @splitColon = split(':', $addin);
		if (@splitColon > 1) {
			my $first	= $splitColon[0];
			my $second	= $splitColon[1];
			if ($first eq "talent") {
				my @competences = ();
				if ($second eq "*") 
					{ @competences = sort(keys(%talents)); } 
				else {
					my @parse	= split('=', $second);
					my $metier	= $parse[0];
					my $select	= $parse[1];
					print "\t\t => [".$metier."]\n";
					if (defined $metiers{$metier}) {
						if ($select eq "*") 
							{ @competences = @{$metiers{$metier}}; }
						elsif ($select eq "all") 
							{ for my $comp (@competences) 
								{ $greatTales{$comp} = 50; } }
						## TODO affiner selection ?
						else { @competences = @{$metiers{$metier}}; }
					} else { 
						print "\t\t JOB [".$metier."] has NO talents DEFINED !!!!!\n";
						push  (@competences, "Connaissance du milleu -".$metier."-"); 
					}
				} ## END else of "if ($second eq "*")"
				if (@competences > 0) {
					## Choix de compétence / talent...
					print "\t\t ***** Choix parmi : \n";
					my $i = 0;
					for my $comp (@competences) 
						{ print "\t\t (".($i+1).")-{".$comp."}\n";$i++; }
					my $choice = 0;
					do { 
						print "\t\t [1-".($i)."]?";
						$choice = <STDIN>;
						chomp($choice);
						if ($choice eq '0') { $choice = 0; }
						$choice = int($choice) or $choice = -1;
						## print "\t\t => [".$choice."] => {".$select."}\n";
						print "\t\t => [".$choice."]\n"; 
						
						## print "\t\t '> 0' {".(($choice > 0)?"true":"false")."]\n";
						## print "\t\t '<= ".$i."' {".(($choice <= $i)?"true":"false")."]\n";
						## print "\t\t '&&' {".( ( ($choice > 0) && ($choice <= $i) )?"true":"false" )."}\n";
						## print "\t\t '!&&' {".( ( ! ( ($choice > 0) && ($choice <= $i) ) )?"true":"false" )."}\n";
					} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
					my $selection = $competences[$choice-1];
					
					&addToGreatTalent($selection, 50, 10);
				} ## END "if (@competences > 0)"
			} ## END "if ($first eq "talent")"
			elsif ($first eq "debtTo") {
				print "\t\t Debt TO {".$second."} added. \n";
				push(@debtsToTo, $second);
			} ## END "elsif ($first eq "debtTo")"
			elsif ($first eq "debtFrom") {
				print "\t\t Debt FROM {".$second."} added. \n";
				push(@debtsFrom, $second);
			} ## END "elsif ($first eq "debtFrom")"
			elsif ($first eq "credit") {
				if ($second =~ /^([+-]?)(\d+)$/ ) {
					my $sum = int($2);
					if ($1 eq "") 
						{ $argent = $sum; }
					elsif ($1 eq "-") 
						{ $argent -= $sum; }
					elsif ($1 eq "+") 
						{ $argent += $sum; }
					print "\t\t Money is now [".$argent."]\n";
				} else { print "\n\nUNKNOWN CREDIT FORM={[".$second."]}\n\n"; }
			} ## END "elsif ($first eq "credit")"
			elsif ($first eq "Parrain") {
				print "\t\t Parrain {".$second."} added. \n";
				if (defined $godfathers{$second}) 
					{ $godfathers{$second}++; }
				else { $godfathers{$second} = 1; }
			} ## END "elsif ($first eq "Parrain")"
			elsif ($first eq "logiciel") {
				print "\t\t software {".$second."} added. \n";
				push(@programmes, $second);
			} ## END "elsif ($first eq "Parrain")"
			elsif ($first eq "métier") {
				my @parse	= split('=', $second);
				my $metier	= $parse[0];
				if (defined $allowedJob{$metier}) 
					{ $allowedJob{$metier} += int($parse[1]); }
				else { $allowedJob{$metier} = int($parse[1]); }
				print "\t\t Job {".$metier."} at level [".$allowedJob{$metier}."]. \n";
			} ## END "elsif ($first eq "métier")"
			else { print "\n\nUNKNOWN FIRST={[".$first."]}\n\n"; }
		} ## END "if (@splitColon > 1)"
		else {
			
			if ($addin eq "EquipementCybernetique=*") {
				my $be			= undef;
				my $validateBE	= undef;
				do {
					$be = &getARandomElementEQUIPMENT();
					print "\t Gain équipement: {".$be->toString()."}\n";
					print "\t Conserver ? [Y/n]";
					$validateBE = <STDIN>;
					chomp($validateBE);
				} while( ($validateBE eq "N") || ($validateBE eq "n") );
				push (@equipments, $be->toString());
			} ## END "elsif ($first eq "EquipementCybernetique=*")"
			elsif ($addin eq "EquipementCybernetique=BrocheTypeC") 
				{ push (@equipments, "Broche de Type C"); }
			elsif ($addin eq "cablage=*[except total]") {
				my @cablages = ();
				push (@cablages, @{$equipments{"Cablage-de-combat"}});
				push (@cablages, @{$equipments{"Cablage-auditif"}});
				
				print "\t\t ***** Choix parmi : \n";
				my $i = 0;
				for my $comp (@cablages) 
					{ print "\t\t (".($i+1).")-{".$comp."}\n";$i++; }
				my $choice = 0;
				do { 
					print "\t\t [1-".($i)."]?";
					$choice = <STDIN>;
					chomp($choice);
					if ($choice eq '0') { $choice = 0; }
					$choice = int($choice) or $choice = -1;
					## print "\t\t => [".$choice."] => {".$select."}\n";
					print "\t\t => [".$choice."]\n"; 
				} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
				my $selection = $cablages[$choice-1];
				print "\t\t Selected {".$selection."}\n";
				push (@equipments, $selection);
			} ## END "elsif ($first eq "cablage=*[except total]")"

			elsif ($addin eq "Cailloux=Onirogramme[6]") 
				{ push (@cailloux, "Onirogramme[6]"); }
			elsif ($addin eq "EquilibrePsychique-=1") { 
				$SAN -= (int(rand(10))+1);
				$personnaeToOuput->setSAN( $SAN );
				## TODO changer aplomb ?! => +1
			} ## END "elsif ($addin eq "EquilibrePsychique-=1")"
			elsif ($addin eq "EquilibrePsychique=1") { 
				$SAN = (int(rand(20))+1);
				$personnaeToOuput->setSAN( $SAN );
				## TODO changer aplomb ?! => +2
			} ## END "elsif ($addin eq "EquilibrePsychique=1")"
			elsif ($addin eq "Esprit-=1") { 
				$POU -= (int(rand(10))+1);
				$personnaeToOuput->setPOU( $POU );
				## TODO changer aplomb ?! => +2
			} ## END "elsif ($addin eq "Esprit-=1")"
			elsif ($addin eq "ConnaissanceMedias=+1") { 
				my $compet = "Connaissance des Médias";
				&addToGreatTalent($compet, 30, 30);
			} ## END "elsif ($addin eq "ConnaissanceMedias=+1")"
			elsif ($addin eq "Onirisme=+1") { 
				my $compet = "Onirisme";
				&addToGreatTalent($compet, 30, 30);
			} ## END "elsif ($addin eq "Onirisme=+1")"
			elsif ($addin eq "Onirisme=+2") { 
				my $compet = "Onirisme";
				&addToGreatTalent($compet, 60, 60);
			} ## END "elsif ($addin eq "Onirisme=+2")"
			elsif ($addin eq "Cailloux=Onirogramme[6]") 
				{ push (@cailloux, "6 cailloux d'Onirogramme. "); }
			## ## DONE "EquilibrePsychique-=1"
			## ## TODO "Onirisme=+1"
			else 
				{ print "TODO PARSE {[".$addin."]} !!!!! \n"; }
		}
	} ## END "for my $addin (@addins)"
} ## for my $bioELT (@biographicElements)

$personnaeToOuput->addCyberEquipments( @equipments );
$personnaeToOuput->addCailloux( @cailloux );
$personnaeToOuput->addProgrammes( @programmes );
my $divers = "";
for my $debtTo (@debtsToTo) 
	{ $divers .= "Dette envers ".$debtTo.". "; }
for my $debtFr (@debtsFrom) 
	{ $divers .= "Dette de ".$debtFr.". "; }
if ($divers eq "") { $divers = "---"; }
$personnaeToOuput->setDivers( $divers );
$personnaeToOuput->setAge( $age );
$personnaeToOuput->setArgent( $argent );

print "\t **** Choix Parrain ***** \n";
## %godfathers > 1
my @possibleGDs = ();
for my $keyGD (sort(keys(%godfathers))) {
	## print "\t\t {".$keyGD."}\t(".$godfathers{$keyGD}.")\n";
	my $localCount = $godfathers{$keyGD};
	if ($localCount > 0) 
		{ push(@possibleGDs, $keyGD); }
} ## END "for my $keyGD (sort(keys(%godfathers))"
if (@possibleGDs > 0) {
	push (@possibleGDs, "---");
	my $i = 0;
	for my $parrain (@possibleGDs) 
		{ print "\t\t (".($i+1).")-{".$parrain."}\n";$i++; }
	my $choice = 0;
	do { 
		print "\t\t [1-".($i)."]?";
		$choice = <STDIN>;
		chomp($choice);
		if ($choice eq '0') { $choice = 0; }
		$choice = int($choice) or $choice = -1;
		## print "\t\t => [".$choice."] => {".$select."}\n";
		print "\t\t => [".$choice."]\n"; 
	} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
	my $selection = $possibleGDs[$choice-1];
	print "\t\t Selected {".$selection."}\n";
	$personnaeToOuput->setParrain( $selection );
} else { 
	print "\t Pas de choix possible !\n";
	$personnaeToOuput->setParrain( "---" );
}
	
## Etape 4: Choisir une occupation : choix métier + répartir EDU*20 (et au moins une à 60%)
print "\t **** Choix métier + talents / compétences ***** \n";
my @possibleJOBs = ();
for my $keyJOB (sort(keys(%allowedJob))) {
	## print "\t\t {".$keyGD."}\t(".$godfathers{$keyGD}.")\n";
	my $localCount = $allowedJob{$keyJOB};
	if ($localCount > 0) { 
		print "\t\t {".$keyJOB."} recommended (".$localCount."). \n";
		push(@possibleJOBs, $keyJOB); 
		## for (my $i = 0 ; $i < $localCount ; $i++) 
		## 	{ push(@possibleJOBs, $keyJOB); }
		## ## print "\t\t {".$keyJOB."} => (".$localCount."). \n";
	} elsif ($localCount < 0) 
		{ print "\t\t {".$keyJOB."} not permitted (".$localCount."). \n"; }
	else { ; }
} ## END "for my $keyGD (sort(keys(%godfathers))"
if (@possibleJOBs == 0) {
	for my $keyJOB (sort(keys(%allowedJob))) {
		my $localCount = $allowedJob{$keyJOB};
		if ($localCount >= 0) 
			{ push(@possibleJOBs, $keyJOB); }
	} ## END "for my $keyGD (sort(keys(%godfathers))"
} ## END "if (@possibleJOBs == 0)"
if (@possibleJOBs > 0) {
	my $i = 0;
	for my $job (@possibleJOBs) 
		{ print "\t\t (".($i+1).")-{".$job."}\n";$i++; }
	my $choice = 0;
	do { 
		print "\t\t [1-".($i)."]?";
		$choice = <STDIN>;
		chomp($choice);
		if ($choice eq '0') { $choice = 0; }
		$choice = int($choice) or $choice = -1;
		## print "\t\t => [".$choice."] => {".$select."}\n";
		print "\t\t => [".$choice."]\n"; 
	} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
	my $selection = $possibleJOBs[$choice-1];
	print "\t\t Selected {".$selection."}\n";
	$personnaeToOuput->setMetier( $selection );
	
	## appliquer talents (!! CyberTek : choisir compétences) choix de la compétence à 70% !
	my @CTcomps = ();
	if ($selection eq "CyberTek") {
		my @tmpComps = @{$metiers{$selection}};
		do {
			print "\t **** CyberTek : Choisir quatre compétences ! (".@CTcomps."/4)\n";
			$i = 0;
			for my $comp (@tmpComps) 
				{ print "\t\t (".($i+1).")-{".$comp."}\n";$i++; }
			$choice = 0;
			do { 
				print "\t\t [1-".($i)."]?";
				$choice = <STDIN>;
				chomp($choice);
				if ($choice eq '0') { $choice = 0; }
				$choice = int($choice) or $choice = -1;
				## print "\t\t => [".$choice."] => {".$select."}\n";
				print "\t\t => [".$choice."]\n"; 
			} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
			my $selectedComp = $tmpComps[$choice-1];
			print "\t\t Selected {".$selectedComp."}\n";
			push (@CTcomps, $selectedComp);
		} while (@CTcomps < 4);
	} ## END "if ($selection eq "CyberTek")"
	
	my @competences = ($selection eq "CyberTek")?@CTcomps:@{$metiers{$selection}};
	print "\t **** Compétence majeure ? \n";
	$i = 0;
	for my $comp (@competences) 
		{ print "\t\t (".($i+1).")-{".$comp."}\n";$i++; }
	$choice = 0;
	do { 
		print "\t\t [1-".($i)."]?";
		$choice = <STDIN>;
		chomp($choice);
		if ($choice eq '0') { $choice = 0; }
		$choice = int($choice) or $choice = -1;
		## print "\t\t => [".$choice."] => {".$select."}\n";
		print "\t\t => [".$choice."]\n"; 
	} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
	my $selectedComp = $competences[$choice-1];
	print "\t\t Selected {".$selectedComp."}\n";
	
	&addToGreatTalent($selectedComp, 60, 60, 1); ## +20%
	## 'majeure' à 60% : autres à 50%
	for my $comp (@competences) {
		if ($comp ne $selectedComp) {
			&addToGreatTalent($comp, 50, 50, 1); ## +10%
		} ## END "if ($comp ne $selectedComp)"
		else { print "..."; }
	} ## END "for my $comp (@competences)"
		
} else { 
	print "\t Pas de choix possible !\n";
	$personnaeToOuput->setMetier( "--- ??" );
}
## my %greatTales	= ();
print "\t **** Compilation talents / compétences ***** \n";
my @talentsProjection = ();
for my $talentName (sort(keys(%greatTales))) 
	{ push(@talentsProjection, $talentName."\t".$greatTales{$talentName}); }
$personnaeToOuput->addTalents( @talentsProjection );

print "\t **** Sexe ***** \n";
my @sexes = ( "Indéterminé-e", "Femme", "Homme" );
my $i = 0;
for my $sexe (@sexes) 
	{ print "\t\t (".($i+1).")-{".$sexe."}\n";$i++; }
my $choice = 0;
do { 
	print "\t\t [1-".($i)."]?";
	$choice = <STDIN>;
	chomp($choice);
	if ($choice eq '0') { $choice = 0; }
	$choice = int($choice) or $choice = -1;
	## print "\t\t => [".$choice."] => {".$select."}\n";
	print "\t\t => [".$choice."]\n"; 
} while( ! ( ($choice > 0) && ($choice <= $i) ) );				
my $selection = $sexes[$choice-1];
print "\t\t Selected {".$selection."}\n";
$personnaeToOuput->setSexe( $selection );

my $name = undef;
do {
	print "\t **** Nom ***** \n";
	$name = <STDIN>;
	chomp($name);
	print "\t\t NOM: {".$name."}\n";
} while ( (defined $name) && ($name eq "") ); 
$personnaeToOuput->setName( $name );

## Etape 5: Les Compétences d'intérêts personnels (INT*10% ailleurs) => indiquer valeur
my $remain4job = "For Job, max was [".$countJobMaxims."] (EDU*20), used [".$countJobTalent."], remain [".($countJobMaxims - $countJobTalent)."]";
my $remain4per = "For Perso, max was [".$countPersoMaxims."] (INT*10), used [".$countPersoTalent."], remain [".($countPersoMaxims - $countPersoTalent)."]";

$personnaeToOuput->addLightBiography( $remain4job );
$personnaeToOuput->addLightBiography( $remain4per );

print $remain4job."\n";
print $remain4per."\n";

## Etape 6: Finitions
## ## ## ...

if ( ! -d "generated") 
	{ mkdir("generated"); }

my $outputFile = $concept."-".$name;
$outputFile =~ s/[ ]//g;
$outputFile = "generated/personnae".$outputFile.".txt";
open (OUTPUT, ">".$outputFile);
print OUTPUT $personnaeToOuput->toStringPersonnae();
close OUTPUT;

system( "convertLaTeXChars.pl ".$outputFile);
