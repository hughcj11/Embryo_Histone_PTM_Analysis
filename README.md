# Histone_PTM_Analysis
https://github.com/hughcj11/Histone_PTM_Analysis

The following code (Histone_PTM_ID) works on a csv file downloaded from Skyline, which should contain the following information in this order: Peptide, Protein, Protein Description, Unimod Accession, Peptide Modified Sequence, Begin Pos, End Pos, Average Measured Retention Time, and the Normalized Area of each Replicate. If Skyline is listing replicates one by one in a row instead of columns, check the "Pivot Replicates" button. It is critical that the csv file is ordered this way so that the code reads the correct columns.
    *Note: For this code to work, the Skyline output for Unimod Accession should contain only the peptide sequence and the unimod in (). Any mass shifts that do not have Unimod IDs are displayed in [] and will be removed at this time. This is necessary so that the code can correctly count the residues. To account for these mass shifts without unimod IDs, additional code will need to be written in this file.
To run your specific file, you must first update the base path so that the code can locate your specific data file. Once the base path is updated, all files generated will appear in the same folder as your Skyline data.

Additionally, this code will require a reference library of Unimod IDs and their biological relevance. This document will be referenced in the code as a biological relevance dictionary. BE SURE TO UPDATE THE FILE PATH IN THE CODE to reference your biological relevance dictionary (Line 5). This document should be updated regularly to ensure the information remains accurate.




The following code will generate the following 8 documents using the Skyline csv file: IntermediateSheet, IntermediateSheet2, HistonePTMLibrary, BioRelevantHistonePTMLibrary, UniqueHistoneLibrary, UniqueUnimodLibrary, Replicate calculations, and Replicate calculations Total PTMs.
    
    IntermediatePTMSheet: pulls out all the modifications on each peptide
    
    IntermediatePTMSheet2: will produce hPTM IDs

    UniqueUnimodLibrary: identifies unique unimods+residue found in the dataset. This document can be used to manually update the reference list of hPTMS and their biological relevance. This is not used in any calculations and is only meant to be an aid.

    HistonePTMLibrary: provides a list of unique modifications found in the data, both biologically relevant and not

    BioRelevantHistonePTMLibrary: provides a list of ONLY biologically relevant/unspecified unique modifications found in the data

    UniqueHistoneLibrary: provides a list of unique histones found in the data

    Replicate calculations: provides a biologically relevant HistonePTMLibrary with the relative abundance calculated for each PTM type and histone location for each replicate. This will calculate the "Sample X Modified" (the sum of the normalized area from all histone peptides containing the given histone PTM) and "Sample X All values" (the sum of the normalized area from all histone peptides that contained the amino acid residue, regardless of its modification status, where the given histone PTM was detected). These will be used to calculate the "Sample X beta value" in the Excel workbook.

    Replicate calculations Total PTMs:provides a biologically relevant HistonePTMLibrary with the relative abundance calculated for each PTM type regardless of histone location/residue for each replicate.

The file downloaded from Skyline should be copied and pasted into the first sheet of the Excel Calculations Workbook. The "Replicate calculations" sheet should be copied onto the second sheet of the Excel Calculations Workbook.

The code Histone_PTM_Statistics performs stastistics on the unique hPTMS and the global hPTM changes.

The code Embryo hPTM R code is used in R to generate abundance maps/PCA plot.
