# Histone_PTM_Analysis
https://github.com/hughcj11/Histone_PTM_Analysis

The following code works on a csv file downloaded from Skyline, which should contain the following information in this order: Peptide, Protein, Protein Description, Unimod Accession, Peptide Modified Sequence, Begin Pos, End Pos, Average Measured Retention Time, and the Normalized Area of each Replicate. If Skyline is listing replicates one by one in a row instead of columns, check the "Pivot Replicates" button.
    *Note: For this code to work, the Skyline output for Unimod Accession should contain only the peptide sequence and the unimod in (). Any mass shifts that do not have Unimod IDs are displayed in [] and will be removed at this time. To account for these mass shifts, additional code will need to be written in this file.
Additionally, this code will require a reference library of Unimod IDs and their biological relevance. This document will be referenced in the code as a biological relevance dictionary. This document should be updated regularly to ensure the information remains accurate.

The following code will generate the following 6 documents using the Skyline csv file: IntermediateSheet, IntermediateSheet2, HistonePTMLibrary, BioRelevantHistonePTMLibrary, UniqueHistoneLibrary, and UniqueUnimodLibrary.
    
    IntermediatePTMSheet: pulls out all the modifications on each peptide
    
    IntermediatePTMSheet2: will  produce hPTM IDs

    HistonePTMLibrary: provides a list of unique modifications found in the data, both biologically relevant and not

    BioRelevantHistonePTMLibrary: provides a list of ONLY biologically relevant unique modifications found in the data

    UniqueHistoneLibrary: provides a list of unique histones found in the data

To calculate the abundance data for each hPTM, you will need to create an Excel calculations workbook. The first sheet of this workbook should contain the downloaded Skyline data. The second sheet should contain the BioRelevantHistonePTMLibrary.