#Author: Chelsea Hughes
import csv
import numpy as np
from pandas import read_csv
import pandas as pd
from scipy.stats import f_oneway
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests
from numpy import inf
base_path = "/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/"

#####Generating values for analysis
##Unique hPTMs
#The below code generates the relative abundance value in a csv file
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= data.iloc[:,0:8]
sample=[f"Sample {i+1}" for i in range(0,12)]
datastats[sample]= (data.iloc[:,9:21].to_numpy() /(data.iloc[:,22:34])*100).to_numpy()
datastats=datastats.replace(np.nan, 0)
datastats.to_csv(base_path+'/Full_Relative_Abundance.csv', index=False)
#The below code generates the beta value in a csv file
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= data.iloc[:,0:8]
sample=[f"Sample {i+1}" for i in range(0,12)]
datastats[sample]= data.iloc[:,9:21].to_numpy() /(data.iloc[:,22:34]+100).to_numpy()
datastats=datastats.replace(-np.inf, 0)
datastats.to_csv(base_path+'/Full_beta_values.csv', index=False)


#The below code generates the m value in a csv file
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= data.iloc[:,0:8]
sample=[f"Sample {i+1}" for i in range(0,12)]
datastats[sample]=np.log2((data.iloc[:,9:21].to_numpy()/((data.iloc[:,22:34]+100).to_numpy()))/(1-(data.iloc[:,9:21].to_numpy()/((data.iloc[:,22:34]+100).to_numpy()))))
datastats=datastats.replace(-np.inf, 0)
datastats.to_csv(base_path+'/Full_M_Values.csv', index=False)

##Global calculations
#The below code generates the global relative abundance value in a csv file
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate_calculations_Total_PTMs.csv",header=0)
datastats= data.iloc[:,0:1]
sample=[f"Sample {i+1}" for i in range(0,12)]
datastats[sample]= (data.iloc[:,1:13].to_numpy()/(data.iloc[:,14:26])*100).to_numpy()
datastats=datastats.replace(-np.inf, 0)
datastats.to_csv(base_path+'/Embryo Anoxia Total PTM.csv', index=False)


####Statistical analysis
##Unique hPTMs
#The below code performs statistics on the relative abundance data for each unique hPTM (residue,PTM,and histone)
data2 = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/Full_Relative_Abundance.csv",header=0)
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= data.iloc[:,0:8]
datastats["Normoxic_Average"]=(data.iloc[:,9:15].sum(axis=1)/data.iloc[:,22:28].sum(axis=1))*100
datastats["Anoxic_Average"]=(data.iloc[:,15:21].sum(axis=1)/data.iloc[:,28:34].sum(axis=1))*100
datastats=datastats.replace(np.inf, 0)
datastats['log2FC'] = np.log2(datastats['Anoxic_Average'] / (datastats['Normoxic_Average']+.0000001)) #.0000001 added to remove zeroes
datastats=datastats.replace(-np.inf, 0)
# datastats['Fvalue'],datastats['Anova_Pvalue'] = f_oneway(data.iloc[:,8:14],data.iloc[:,14:20],axis=1)
datastats['T-test_t_statistic'], datastats['T-test_p_value'] = ttest_ind(data2.iloc[:,8:14], data2.iloc[:,14:20],axis=1)
datastats['T-test_p_value'] = datastats['T-test_p_value'].fillna(1)
datastats['corrected_p_values'] = multipletests(datastats['T-test_p_value'], method='fdr_bh')[1]

# Write DataFrame to CSV
datastats.to_csv(base_path+'/Datastats.csv', index=False)

##Global statistics
#The below code performs statistics on the relative abundance data global hPTM changes (independent of residue and histone)
data2 = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/Embryo Anoxia Total PTM.csv",header=0)
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate_calculations_Total_PTMs.csv",header=0)
datastats= data.iloc[:,0:1]
datastats["Normoxic_Average"]=(data.iloc[:,1:7].sum(axis=1)/data.iloc[:,14:20].sum(axis=1))*100
datastats["Anoxic_Average"]=(data.iloc[:,7:13].sum(axis=1)/data.iloc[:,20:27].sum(axis=1))*100
datastats['log2FC'] = np.log2(datastats['Anoxic_Average'] / (datastats['Normoxic_Average']+.0000001)) #.0000001 added to remove zeroes
# datastats['Fvalue'],datastats['Anova_Pvalue'] = f_oneway(data.iloc[:,8:14],data.iloc[:,14:20],axis=1)
datastats['T-test_t_statistic'], datastats['T-test_p_value'] = ttest_ind(data2.iloc[:,1:7], data2.iloc[:,7:13],axis=1)
datastats['T-test_p_value'] = datastats['T-test_p_value'].fillna(1)
datastats['corrected_p_values'] = multipletests(datastats['T-test_p_value'], method='fdr_bh')[1]
datastats.to_csv(base_path+'/DatastatsGlobal.csv', index=False)

#The below document shows the relative coverage of each modifiable residue (a residue shown as capable of having a PTM). For example, how often K covered by PTMs?
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= pd.DataFrame()
Normoxic_Average=[]
Anoxic_Average=[]
GroupedAATotal=data.drop_duplicates('Amino Acid + Position')
GroupedAA=data.groupby(['Amino Acid']).sum().reset_index()
datastats['Amino Acid']=GroupedAA['Amino Acid']
GroupedAATotal_dict={}
for aminoacid, values in zip(GroupedAATotal['Amino Acid'], zip(GroupedAATotal.iloc[:,22:34].values.tolist())):
    values=values[0]
    if aminoacid in GroupedAATotal_dict.keys():
        GroupedAATotal_dict[aminoacid].append(values)
    else:
        GroupedAATotal_dict[aminoacid]=[]
        GroupedAATotal_dict[aminoacid].append(values)
       
for index, row in GroupedAA.iterrows():
    NormoxicNumerator=row.iloc[9:15].sum()
    amino_acid_dict_rows = GroupedAATotal_dict[row['Amino Acid']]
    if len(amino_acid_dict_rows) ==1:
         dict_rows_sum_for_denom = amino_acid_dict_rows[0]
    else:
        dict_rows_sum_for_denom = [sum(i) for i in zip(*amino_acid_dict_rows)]
    NormoxicDenom=sum(dict_rows_sum_for_denom[0:6])
    Normoxic_Average.append((NormoxicNumerator/NormoxicDenom)*100)
    AnoxicNumerator=row.iloc[15:21].sum()
    AnoxicDenom=sum(dict_rows_sum_for_denom[6:12])
    Anoxic_Average.append((AnoxicNumerator/AnoxicDenom)*100)
datastats["Normoxic_Average"]=Normoxic_Average 
datastats["Anoxic_Average"]=Anoxic_Average 
datastats.to_csv(base_path+'/ResidueCoverage.csv', index=False)

#The below document shows the relative coverage by a specific PTM for each modifiable residue (a residue shown as capable of having a PTM). For example, how often K covered by Ub?
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/code/Embryo Library/Replicate calculations.csv",header=0)
datastats= pd.DataFrame()
Normoxic_Average=[]
Anoxic_Average=[]
GroupedAATotal=data.drop_duplicates('Amino Acid + Position')
GroupedAA=data.groupby(['Amino Acid',"PTM Description"]).sum().reset_index()
datastats['Amino Acid']=GroupedAA['Amino Acid']
datastats["PTM Description"]=GroupedAA["PTM Description"]
GroupedAATotal_dict={}
for aminoacid, values in zip(GroupedAATotal['Amino Acid'], zip(GroupedAATotal.iloc[:,22:34].values.tolist())):
    values=values[0]
    if aminoacid in GroupedAATotal_dict.keys():
        GroupedAATotal_dict[aminoacid].append(values)
    else:
        GroupedAATotal_dict[aminoacid]=[]
        GroupedAATotal_dict[aminoacid].append(values)
       
for index, row in GroupedAA.iterrows():
    NormoxicNumerator=row.iloc[9:15].sum()
    amino_acid_dict_rows = GroupedAATotal_dict[row['Amino Acid']]
    if len(amino_acid_dict_rows) ==1:
         dict_rows_sum_for_denom = amino_acid_dict_rows[0]
    else:
        dict_rows_sum_for_denom = [sum(i) for i in zip(*amino_acid_dict_rows)]
    NormoxicDenom=sum(dict_rows_sum_for_denom[0:6])
    Normoxic_Average.append((NormoxicNumerator/NormoxicDenom)*100)
    AnoxicNumerator=row.iloc[15:21].sum()
    AnoxicDenom=sum(dict_rows_sum_for_denom[6:12])
    Anoxic_Average.append((AnoxicNumerator/AnoxicDenom)*100)
datastats["Normoxic_Average"]=Normoxic_Average 
datastats["Anoxic_Average"]=Anoxic_Average 
datastats.to_csv(base_path+'/ResidueCoverageByPTM.csv', index=False)

#Normalizing protein abundance by obtaining log2
  
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Embryo Protein Abundance/Protein Abundance for Embryos (calculations).csv",header=0)
datastats= data.iloc[:,0:2]
datastats=pd.concat([datastats, data.iloc[:,5:51].apply(np.log2) ], axis=1, join="inner")
datastats=datastats.replace(-np.inf, 0)
datastats.to_csv('/Users/chelseahughes/Desktop/Histone Analysis/Embryo Protein Abundance/Proteinlog2.csv', index=False) 

#Statistics on log2 Protein Abundance
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Embryo Protein Abundance/Proteinlog2.csv",header=0)
datastats= data.iloc[:,0:1]
datastats=datastats.replace(-np.inf, 0)
datastats['T-test_t_statistic'], datastats['T-test_p_value'] = ttest_ind(data.iloc[:,8:14], data.iloc[:,2:8],axis=1)
datastats['T-test_p_value'] = datastats['T-test_p_value'].fillna(1)
datastats['corrected_p_values'] = multipletests(datastats['T-test_p_value'], method='fdr_bh')[1]
datastats.to_csv("/Users/chelseahughes/Desktop/Histone Analysis/Embryo Protein Abundance/Proteinlog2stats.csv", index=False)