#!/usr/bin/perl -l

my $COMPAT_REPORTS_DIR = "compat_reports";
chomp(my @files = `find $COMPAT_REPORTS_DIR -name compat_report.html`);

my $title = $ENV{BUILD_NUMBER}
  ? "Compatibility Reports for build $ENV{BUILD_NUMBER}"
  : "Compatibility Reports";
print "<html><title>$title</title><style type='text/css'>.compatible{color:green}.incompatible{color:red}</style></head><body><h1>$title</h1><ul>";
for (@files) {
  s/^$COMPAT_REPORTS_DIR\///;
  my $report_subject = m%^([^/]+)% ? $1 : $_;
  my $compatible = system("egrep", "-q", "Verdict.+Incompatible",  "$COMPAT_REPORTS_DIR/$_");
  if (0 > $compatible) {
    die "Unable to execute egrep: $!\n";
  }
  my $textclass= $compatible ? "compatible" : "incompatible";
  print qq{<li class="$textclass"><a href="$_">$report_subject</a> ($textclass) </li>};
}
print "</ul></body></html>";
