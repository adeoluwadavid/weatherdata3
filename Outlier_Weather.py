# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:26:00 2020
humidity2 = humidity1.str.extract(r'([0-9]+)')
@author: Adewole
"""

import pandas as pd
import numpy as np

df = pd.read_excel('Keffi_Weather_Combined.xlsx')

hum = df['Wind_Speed'].dropna(how='any')
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
print(result)

for i in result:
    print(i)
        