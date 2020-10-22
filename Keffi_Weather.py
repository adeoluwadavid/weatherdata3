# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:04:40 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt



def weatherData(startDate,endDate,data):
    start_date = startDate
    end_date = endDate
    dataToPlot = data
    df = pd.read_excel('Keffi_Weather_Combined.xlsx')
    p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
    df.set_index(p,inplace=True)
    
    rng = df[start_date:end_date]
    
    temperature = rng.Temperature
    dewPoint = rng.Dew_Point
    humidity = rng.Humidity
    wind = rng.Wind
    windSpeed = rng.Wind_Speed
    windGust = rng.Wind_Gust
    pressure = rng.Pressure
    precip = rng.Precip
    condition = rng.Condition
    
    df['Temperature'] = temperature
    df['Dew_Point'] = dewPoint
    df['Humidity'] = humidity
    df['Wind'] = wind
    df['Wind_Speed'] = windSpeed
    df['Wind_Gust'] = windGust
    df['Pressure'] = pressure
    df['Precip'] = precip
    df['Condition'] = condition 
    
    temp1 = temperature.dropna(how='any').astype('str')
    dewP1 = dewPoint.dropna(how='any').astype('str')
    humidity1 = humidity.dropna(how='any').astype('str')
    wind1 = wind.dropna(how='any').astype('str')
    windSpeed1 = windSpeed.dropna(how='any').astype('str')
    windGust1 = windGust.dropna(how='any').astype('str')
    pressure1 = pressure.dropna(how='any').astype('str')
    precip1 = precip.dropna(how='any').astype('str')
    condition1 = condition.dropna(how='any').astype('str')
    
    temp2 = temp1.str.extract(r'([0-9]+)')
    dewP2 = dewP1.str.extract(r'([0-9]+)')
    humidity2 = humidity1.str.extract(r'([0-9]+)')
    wind2 = wind1
    windSpeed2 = windSpeed1.str.extract(r'([0-9]+)')
    windGust2 = windGust1.str.extract(r'([0-9]+)')
    pressure2 = pressure1.str.extract(r'([\d\.\d]+)')
    precip2 = precip1.str.extract(r'([\d\.\d]+)')
    condition2 = condition1
    
    df['Temperature'] = temp2
    df['Dew_Point'] = dewP2
    df['Humidity'] = humidity2
    df['Wind'] = wind2
    df['Wind_Speed'] = windSpeed2
    df['Wind_Gust'] = windGust2
    df['Pressure'] = pressure2
    df['Precip'] = precip2
    df['Condition'] = condition2
    
    temp3 = df['Temperature'].dropna(how='any').astype('str')
    dewP3 = df['Dew_Point'].dropna(how='any').astype('str')
    humidity3 = df['Humidity'].dropna(how='any').astype('str')
    wind3 = df['Wind'].dropna(how='any').astype('str')
    windSpeed3 = df['Wind_Speed'].dropna(how='any').astype('str')
    windGust3 = df['Wind_Gust'].dropna(how='any').astype('str')
    pressure3 = df['Pressure'].dropna(how='any').astype('str')
    precip3 = df['Precip'].dropna(how='any').astype('str')
    condition3 = df['Condition'].dropna(how='any').astype('str')
    
    # Temperature and Dew Point in Celsius
    temp = (temp3.astype('float') -32) * (5/9)
    dewP = (dewP3.astype('float') - 32) * (5/9)
    
    hum = humidity3.astype('int')
    w = wind3
    
    #Wind Speed and Wind Gust in kmh
    wS = windSpeed3.astype('float') * 1.60934
    wG = windGust3.astype('float') * 1.60934
    press = pressure3.astype('float')
    preC = precip3.astype('float')
    c = condition3
    
    if(dataToPlot == 'Temperature'):
        plt.plot(temp,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Temperature(C)")
    elif(dataToPlot == 'Dew Point'):
        plt.plot(dewP,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Dew Point(C)")
    elif(dataToPlot == 'Humidity'):
        plt.plot(hum,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Humidity(%)")
    elif(dataToPlot == 'Wind'):
        plt.plot(w,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Wind")
    elif(dataToPlot == 'Wind Speed'):
        plt.plot(wS,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Wind Speed(kmh)")
    elif(dataToPlot == 'Wind Gust'):
        plt.plot(wG,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Wind Gust(kmh)")
    elif(dataToPlot == 'Pressure'):
        plt.plot(press,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Pressure(in)")
    elif(dataToPlot == 'Precip'):
        plt.plot(preC,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Precip(in)")
    elif(dataToPlot == 'Condition'):
        plt.plot(c,"-o")
        plt.xlabel("Time(Hours)")
        plt.ylabel("Condition")
    else:
        print("Enter a correct data to plot")