# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:07:15 2020

@author: Adewole
"""

import pandas as pd
import numpy as np


dataset= [10,12,12,13,12,11,14,13,15,10,10,10,
          100,12,14,13, 12,10, 10,11,12,15,12,13,
          12,11,14,13,15,10,15,12,10,14,13,15,10]
outliers = []

def detect_outlier(data_1):
    threshold = 3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    print(mean_1)
    print(std_1)
    for y in data_1:
        z_score = (y - mean_1)/std_1
        z = np.abs(z_score)
        if z > threshold:
            outliers.append(y)
    return outliers
outlier_datapoints = detect_outlier(dataset)
print(outlier_datapoints)

