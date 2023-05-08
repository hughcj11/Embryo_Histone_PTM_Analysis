# Histone_PTM_Analysis
https://github.com/hughcj11/Histone_PTM_Analysis

The following code works on a csv file downloaded from Skyline, which should contain the following information in this order: Peptide, Protein, Protein Description, Unimod Accession, Peptide Modified Sequence, Begin Pos, End Pos, Average Measured Retention Time, and the Normalized Area of each Replicate. If Skyline is listing replicates one by one in a row instead of columns, check the "Pivot Replicates" button.
    *Note: For this code to work, the Skyline output for Unimod Accession should contain only the peptide sequence and the unimod in (). Any mass shifts that do not have Unimod IDs are displayed in [] and will be removed at this time. To account for these mass shifts, additional code will need to be written in this file.

Additionally, this code will require a reference library of Unimod IDs and their biological relevance. This document will be referenced in the code as a biological relevance dictionary. This document should be updated regularly to ensure the information remains accurate.

The following code will generate the following 7 documents using the Skyline csv file: IntermediateSheet, IntermediateSheet2, HistonePTMLibrary, BioRelevantHistonePTMLibrary, UniqueHistoneLibrary, UniqueUnimodLibrary, and Replicate calculations.
    
    IntermediatePTMSheet: pulls out all the modifications on each peptide
    
    IntermediatePTMSheet2: will  produce hPTM IDs

    UniqueUnimodLibrary: identifies unique unimods+residue found in the dataset. This document can be used to manually update the reference list of hPTMS and their biological relevance. This is not used in any calculations and is only meant to be a aid.

    HistonePTMLibrary: provides a list of unique modifications found in the data, both biologically relevant and not

    BioRelevantHistonePTMLibrary: provides a list of ONLY biologically relevant unique modifications found in the data

    UniqueHistoneLibrary: provides a list of unique histones found in the data

    Replicate calculations: biologically relevant HistonePTMLibrary with the relative abundance calculated for each replicate for each PTM type and histone location
