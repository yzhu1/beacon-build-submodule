#!/usr/bin/perl
use strict;
my $names_wanted = shift || 300;
my $seed = shift || rand;
srand($seed);

open my $fh, "<surnames.txt";
chomp(my @family_names = <$fh>);
open $fh, "<givennames_male.txt";
chomp (my @male_given_names = <$fh>);
open $fh, "<givennames_female.txt";
chomp (my @female_given_names = <$fh>);
close $fh;

# my @standard_suffixes = qw(Jr. Sr. 3rd 4th Esq. DFA);
my @standard_suffixes = qw(Jr. 3rd 4th);

my $SUFFIX_PROB = 0.10;
my $MIDDLENAME_PROB = 0.75;
my $MIDDLENAME_IS_GIVENNAME_PROB = 0.5;

$, = ",";
$\=$/;

for (1..$names_wanted) {
  my ($lname,$fname,$mname,$suffix) = ("") x 4;
  $lname = pick_from(\@family_names);
  my $givennames_ar = ($_ % 2) ?  \@female_given_names : \@male_given_names;
  $fname = pick_from($givennames_ar);
  my $mn_picker = rand();
  if ($mn_picker < $MIDDLENAME_PROB) {
    if ($mn_picker < $MIDDLENAME_PROB * $MIDDLENAME_IS_GIVENNAME_PROB) {
      $mname = pick_from($givennames_ar);
    } else {
      $mname = pick_from(\@family_names);
    }
  }
  if (rand() < $SUFFIX_PROB) {
    $suffix = pick_from(\@standard_suffixes);
  }
  print $lname,$fname,$mname,$suffix;
}

sub pick_from {
  my $ar = shift;
  return ${$ar}[rand @$ar];
}
