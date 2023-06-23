#Author: Chelsea Hughes
import csv
import re
import numpy as np
from pandas import read_csv
from scipy.stats import f_oneway
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

base_path = "/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/"

#The below code performs statistics on the relative abundance data for each unique hPTM (residue,PTM,and histone)
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/Full_Relative_Abundance.csv",header=0)
datastats= data.iloc[:,0:8]
datastats["Normoxic_Average"]=data.iloc[:,8:14].mean(axis=1)
datastats["Anoxic_Average"]=data.iloc[:,14:20].mean(axis=1)
datastats['log2FC'] = np.log2(datastats['Anoxic_Average'] / (datastats['Normoxic_Average']+.0000001)) #.0000001 added to remove zeroes
# datastats['Fvalue'],datastats['Anova_Pvalue'] = f_oneway(data.iloc[:,8:14],data.iloc[:,14:20],axis=1)
datastats['T-test_t_statistic'], datastats['T-test_p_value'] = ttest_ind(data.iloc[:,8:14], data.iloc[:,14:20],axis=1)
datastats['T-test_p_value'] = datastats['T-test_p_value'].fillna(1)
datastats['corrected_p_values'] = multipletests(datastats['T-test_p_value'], method='fdr_bh')[1]

# Write DataFrame to CSV
datastats.to_csv(base_path+'/Datastats.csv', index=False)

#The below code performs statistics on the relative abundance data global hPTM changes (independent of residue and histone)
data = read_csv("/Users/chelseahughes/Desktop/Histone Analysis/Calculation for Embryo Samples/Embryo Anoxia Total PTM.csv",header=0)
datastats= data.iloc[:,5:6]
datastats["Normoxic_Average"]=data.iloc[:,8:14].mean(axis=1)
datastats["Anoxic_Average"]=data.iloc[:,14:20].mean(axis=1)
datastats['log2FC'] = np.log2(datastats['Anoxic_Average'] / (datastats['Normoxic_Average']+.0000001)) #.0000001 added to remove zeroes
# datastats['Fvalue'],datastats['Anova_Pvalue'] = f_oneway(data.iloc[:,8:14],data.iloc[:,14:20],axis=1)
datastats['T-test_t_statistic'], datastats['T-test_p_value'] = ttest_ind(data.iloc[:,8:14], data.iloc[:,14:20],axis=1)
datastats['T-test_p_value'] = datastats['T-test_p_value'].fillna(1)
datastats['corrected_p_values'] = multipletests(datastats['T-test_p_value'], method='fdr_bh')[1]
datastats.to_csv(base_path+'/DatastatsGlobal.csv', index=False)