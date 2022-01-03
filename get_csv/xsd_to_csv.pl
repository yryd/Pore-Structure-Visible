
use strict;
use Getopt::Long;
use MaterialsScript qw(:all);


my $doc_name = "PA-H2O"; #Only review doc name
my $doc = $Documents{"$doc_name.xsd"};
my $beads = $doc->DisplayRange->Beads;
my $xyz_point = attach_mol_Z($beads);
my $count_table = Documents->New("$doc_name"."_xyz.std");
table_title();
write_table($xyz_point);
Documents->SaveAll;




sub attach_mol_Z {
  my $beads = shift;
  my @xyz_list;
  foreach my $bead (@$beads) {
      my $bead_name = $bead ->BeadTypeName;
      my @XYZ;
      my $X = $bead->XYZ->X;
      my $Y = $bead->XYZ->Y;
      my $Z = $bead->XYZ->Z;
      my @xyz = ($bead_name,$X, $Y, $Z);
      push(@xyz_list, [@xyz]);
  }
  return \@xyz_list;
}
sub table_title {
    $count_table->Sheets(0)->ColumnHeading(0) = "Name";
    $count_table->Sheets(0)->ColumnHeading(1) = "X";
    $count_table->Sheets(0)->ColumnHeading(2) = "Y";
    $count_table->Sheets(0)->ColumnHeading(3) = "Z";
}
sub write_table {
    my ($xyz) = @_;
    my @site = @$xyz;
    # print("@site\n");
    my $Sheet_total = $count_table->Sheets(0);
    for (my $cow = 0;$cow <= $#site;$cow++) {
        $Sheet_total->Cell($cow,0) = $site[$cow][0];
        $Sheet_total->Cell($cow,1) = $site[$cow][1];
        $Sheet_total->Cell($cow,2) = $site[$cow][2];
        $Sheet_total->Cell($cow,3) = $site[$cow][3];
    }
}
