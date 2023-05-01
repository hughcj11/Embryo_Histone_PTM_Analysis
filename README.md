# Histone_PTM_Analysis
The following code works on csv files downloaded from Skyline. The abundance data from Skyline should contain the following information in this order: Peptide, Protein, Protein Description, Unimode Accession, Peptide Modified Sequence, Begin Pos, End Pos, Average Measured Retention Time, and the Normalized Area of each Replicate. If Skyline is listing replicates one by one in a row instead of columns, check the "Pivot Replicates" button.

The code will generate the following 6 documents using the Skyline csv file: IntermediateSheet, IntermediateSheet2, HistonePTMLibrary, BioRelevantHistonePTMLibrary, UniqueHistoneLibrary, and UniqueUnimodLibrary.

    HistonePTMLibrary: provides a list of unique modifications found in the data, both biologically relevant and not

    BioRelevantHistonePTMLibrary: provides a list of ONLY biologically relevant unique modifications found in the data

    UniqueHistoneLibrary: provides a list of unique histones found in the data