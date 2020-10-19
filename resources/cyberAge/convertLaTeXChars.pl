#!/usr/bin/perl -w

use strict;

## http://en.wikibooks.org/wiki/LaTeX/Special_Characters

my $file = $ARGV[0];

my @lines = ();
open (FILE,"<".$file);
while (my $line = <FILE>) { push (@lines,$line); }
close (FILE);

open (FILE,">".$file);
foreach my $line (@lines) {
	$line =~ s/ê/\{\\^e\}/g;
	$line =~ s/é/\{\\'e\}/g;
	$line =~ s/è/\{\\`e\}/g;
	$line =~ s/á/\{\\'a\}/g;
	$line =~ s/à/\{\\`a\}/g;
	$line =~ s/â/\{\\^a\}/g;
	$line =~ s/û/\{\\^u\}/g;
	$line =~ s/ù/\{\\`u\}/g;
	$line =~ s/ô/\{\\^o\}/g;
	$line =~ s/ò/\{\\`o\}/g;
	$line =~ s/í/\{\\'i\}/g;
	$line =~ s/î/\{\\^i\}/g;
	$line =~ s/ç/\\c\{c\}/g;
	$line =~ s/ä/{\\"a\}/g;
	$line =~ s/ë/{\\"e\}/g;
	$line =~ s/ï/{\\"i\}/g;
	$line =~ s/ö/{\\"o\}/g;
	$line =~ s/ü/{\\"u\}/g;
	$line =~ s/ţ/\\c{t\}/g;
	$line =~ s/ļ/\\d{l\}/g;
	$line =~ s/š/\\v{s\}/g; ## caron / hacek
	$line =~ s/ň/\\v{n\}/g;
	$line =~ s/ř/\\v{r\}/g;
	$line =~ s/ž/\\v{z\}/g;
	
	$line =~ s/Ê/\{\\^E\}/g;
	$line =~ s/É/\{\\'E\}/g;
	$line =~ s/È/\{\\`E\}/g;
	$line =~ s/Î/\{\\^I\}/g;
	$line =~ s/Ì/\{\\`I\}/g;
	$line =~ s/Ï/\{\\"I\}/g;
	$line =~ s/À/\{\\`A\}/g;
	$line =~ s/Â/\{\\^A\}/g;
	$line =~ s/Û/\{\\^U\}/g;
	$line =~ s/Ù/\{\\`U\}/g;
	$line =~ s/Ô/\{\\^O\}/g;
	$line =~ s/Ò/\{\\`O\}/g;
	$line =~ s/Ç/\\c\{C\}/g;
	print FILE $line;
}
close (FILE);
