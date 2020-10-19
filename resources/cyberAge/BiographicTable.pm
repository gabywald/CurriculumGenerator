package BiographicTable;

use strict;

sub new {
	my $class	= shift;
	$class		= ref($class) || $class;

	my $self	= {};

	$self->{NAME}		= undef;
	$self->{COMMENT}	= undef;
	$self->{CONTENTS}	= ();
	$self->{LINKSTO}	= ();
	$self->{ADDINS}		= (); ## array of arrays ?

	bless($self, $class);
	return $self;
}

sub setNAME {
	my $self		= shift;
	$self->{NAME}	= shift;
}

sub getNAME {
	my $self		= shift;
	return $self->{NAME};
}

sub setCOMMENT {
	my $self		= shift;
	$self->{COMMENT}	= shift;
}

sub getCOMMENT {
	my $self		= shift;
	return $self->{COMMENT};
}

sub addCONTENTS {
	my $self			= shift;
	while(@_) { push (@{$self->{CONTENTS}},shift); }
}

sub getCONTENTS {
	my $self = shift;
	return ($self->{CONTENTS})?@{$self->{CONTENTS}}:();
}

sub addLINKSTO {
	my $self			= shift;
	while(@_) { push (@{$self->{LINKSTO}},shift); }
}

sub getLINKSTO {
	my $self = shift;
	return ($self->{LINKSTO})?@{$self->{LINKSTO}}:();
}

sub addADDINS {
	my $self			= shift;
	while(@_) { push (@{$self->{ADDINS}},shift); }
}

sub getADDINS {
	my $self = shift;
	return ($self->{ADDINS})?@{$self->{ADDINS}}:();
}

sub toString() {
	my $self = shift;
	my $toReturn = "";
	
	$toReturn .= "Table ".$self->getNAME()."\t".((defined $self->getCOMMENT())?$self->getCOMMENT():"")."\n";
	
	my @contents	= $self->getCONTENTS();
	my @linksto		= $self->getLINKSTO();
	my @addins		= $self->getADDINS();
	## for my $content (@contents) 
	## 	{ $toReturn .= "\t C: ".$content."\n"; }
	## for my $link (@linksto) 
	## 	{ $toReturn .= "\t L:".$link."\n"; }
	## for my $addin (@addins) 
	## 	{ $toReturn .= "\t A:".$addin."\n"; }
	for (my $i = 0 ; $i < @contents ; $i++) 
		{ $toReturn .= "\t".$contents[$i]."\t".$linksto[$i]."\t".$addins[$i]."\n"; }
	
	return $toReturn;
}

1;
