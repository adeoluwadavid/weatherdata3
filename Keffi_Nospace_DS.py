# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:59:02 2020

@author: Adewole
"""

import pandas as pd

df = pd.read_excel('Keffi_Weather_Nospace.xlsx')

temp = df['Temperature']
dewP = df['Dew_Point']
hum = df['Humidity']
wind_speed = df['Wind_Speed']
wind_gust = df['Wind_Gust']
pressure = df['Pressure']
precip = df['Precip']
wind = df['Wind']
condition = df['Condition']
time = df['Time']
date_time = df['Date_Time']

temp_extracted = temp.str.extract(r'([\d\.\d]+)').astype('str')
dewP_extracted = dewP.str.extract(r'([\d\.\d]+)').astype('str')
hum_extracted = hum.str.extract(r'([\d\.\d]+)').astype('str')
wind_speed_extracted = wind_speed.str.extract(r'([\d\.\d]+)').astype('str')
wind_gust_extracted = wind_gust.str.extract(r'([\d\.\d]+)').astype('str')
pressure_extracted = pressure.str.extract(r'([\d\.\d]+)').astype('str')
precip_extracted = precip.str.extract(r'([\d\.\d]+)').astype('str')


temp_int = temp_extracted.astype('int')
dewP_int = dewP_extracted.astype('int')
hum_int = hum_extracted.astype('int')
wind_speed_int = wind_speed_extracted.astype('int')
wind_gust_int = wind_gust_extracted.astype('int')
pressure_float = pressure_extracted.astype('float')
precip_float = precip_extracted.astype('float')
wind_str = wind.astype('str')
condition_str = condition.astype('str')
time_str = time
date_time_date = date_time

df['Temperature'] = temp_int
df['Dew_Point'] = dewP_int
df['Humidity'] = hum_int
df['Wind_Speed'] = wind_speed_int
df['Wind_Gust'] = wind_gust_int
df['Pressure'] = pressure_float
df['Precip'] = precip_float
df['Wind'] = wind_str
df['Condition'] = condition_str
df['Time'] = time_str
df['Date_Time'] = date_time_date

#print(type(df['Temperature']))
print(df.head())
#x=pd.DataFrame(temp_int, columns=['Temp'])
#print(x)
df.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather3\Keffi_Nospace_Value.xlsx',index = False, header=True)