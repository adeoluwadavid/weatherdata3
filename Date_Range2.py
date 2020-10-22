# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:32:23 2020

@author: Adewole
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Keffi_Weather_Combined.xlsx')
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)
print(df)
