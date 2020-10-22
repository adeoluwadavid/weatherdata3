# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:58:16 2020

@author: Adewole
"""

import pandas as pd

df = pd.read_excel('Keffi_Weather_Combined2.xlsx')
print(df)
a = df.dropna(how='any')
print(a)
a.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather3\KF.xlsx', index = False, header=True)