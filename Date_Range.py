# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:42:35 2020

@author: Adewole
"""

import pandas as pd

a = pd.date_range(start='2014-01-01 00:00:00',end='2020-09-30 23:00:00', freq='1H')
print(a)
b = a.format(formatter=lambda x: x.strftime('%Y%m%d'))


#Changing it to dataframe
df = pd.DataFrame(a, columns =['Date_Time'])
print(df)
df.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather3\Date_Time.xlsx',index = False, header=True)
