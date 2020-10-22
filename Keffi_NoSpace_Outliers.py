# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:57:34 2020

@author: Adewole
"""

import pandas as pd
import numpy as np

df = pd.read_excel('Keffi_Weather_Nospace.xlsx')

hum = df['Condition']
hum_extracted = hum.str.extract(r'([\d\.\d]+)').astype('str')

hum_to_int = hum_extracted.astype('float')

hum_to_array = np.array(hum_to_int)

## Using Z-Score to calculated Outliers
outliers= []
#
def detect_outliers(data):
    threshold = 3
    my_mean = np.mean(data)
    std = np.std(data)
    print(my_mean)
    print(std)
    for i in data:
        z_score = (i - my_mean)/std
        z = np.abs(z_score)
        if np.greater(z, threshold):
             outliers.append(i)
    return outliers
    
result = detect_outliers(hum_to_array)
print(len(result))

#for i in result:
#    print(i)