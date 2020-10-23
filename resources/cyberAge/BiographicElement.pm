package BiographicElement;

use strict;

sub new {
	my $class	= shift;
	$class		= ref($class) || $class;

	my $self	= {};

	$self->{CONTENT}	= undef;
	$self->{ADDINS}		= ();

	bless($self, $class);
	return $self;
}

sub addCONTENT {
	my $self			= shift;
	my $toAdd			= shift;
	if ($self->{CONTENT} =~ /^Table (.*?)$/) 
		{ $self->{CONTENT} = "[".$1."] ".$toAdd; } 
	else { $self->{CONTENT} .= " --- ".$toAdd; }
}

sub setCONTENT {
	my $self			= shift;
	$self->{CONTENT}	= shift;
}

sub getCONTENT {
	my $self		= shift;
	return $self->{CONTENT};
}

sub addADDINS {
	my $self			= shift;
	while(@_) { push (@{$self->{ADDINS}},shift); }
}

sub getADDINS {
	my $self = shift;
	return ($self->{ADDINS})?@{$self->{ADDINS}}:();
}

sub toString {
	my $self = shift;
	my $toReturn = "";
	
	$toReturn .= $self->getCONTENT(); ## +"\n";
	my @addins = $self->getADDINS();
	my $i = 0;
	for my $element (@addins) {
		if ($i == 0) { $toReturn .= "\t{"; }
		else { $toReturn.= ";"; }
		$toReturn .= "'".$element."'";
		$i++;
		if ($i == @addins) { $toReturn.= "}"; }
	} ## END "for my $element (@addins)"
	
	$toReturn .= ""; ## "\n";
	
	return $toReturn;
}

1;
