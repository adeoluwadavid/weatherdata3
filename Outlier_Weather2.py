# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:22:36 2020

@author: Adewole
"""

import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_excel('Keffi_Weather_Combined.xlsx')

z=np.abs(stats.zscore(df.Temperature))
print(z)

#hum = df['Dew_Point'].dropna(how='any')
#hum_extracted = hum.str.extract(r'([\d\.\d]+)').astype('str')
#hum_to_int = hum_extracted.astype('float')
#
#hum_to_array = np.array(hum_to_int)

print(df.shape)