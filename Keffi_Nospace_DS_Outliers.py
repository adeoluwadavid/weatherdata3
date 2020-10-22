# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:36:12 2020

@author: Adewole
"""

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel('Keffi_O_Dew_Point_Nospace.xlsx')
#df = pd.read_excel('Keffi_Nospace_Value.xlsx')

#z_scores = stats.zscore(df)
#abs_z_scores = np.abs(z_scores)
#filter_entries = (abs_z_scores < 3).all(axis = 1)
#new_df = df[filter_entries]
#print(new_df)
outliers= []
#
def detect_outliers(data):
    threshold = 3
    my_mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score = (i - my_mean)/std
        z = np.abs(z_score)
        if np.greater(z, threshold):
             outliers.append(i)
    return outliers
    
result = detect_outliers(df.Dew_Point)
print(len(result))

#df = df[~df['Dew_Point'].isin(outliers)]
#print(df)
#
#df.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather3\Keffi_O_Dew_Point_Nospace.xlsx', index = False, header=True)