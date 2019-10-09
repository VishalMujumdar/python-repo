# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:26:34 2019

@author: vismujum
"""

import pandas as pd
import os 

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

autoData = pd.read_csv("AutoDataset.csv")

autoData.shape
autoData.columns.values

autoData_v1 = autoData[autoData[' make']=='toyota']
autoData_v1

autoData_v2 = autoData[(autoData[' city-mpg'] > 30) & (autoData[' engine-size'] < 120) ]
autoData_v2

autoData_v3 = autoData[(autoData[' body-style'] == 'sedan') ]
autoData_v3

autoData_v4 = autoData[[' make',' body-style',' fuel-type', ' price']]
autoData_v4

autoData[' make'].value_counts()

#sales.gender.value_counts()
autoData_v5 = autoData[(autoData[' make']=='audi') | (autoData[' make']=='bmw')|(autoData[' make']=='porsche')]
autoData_v5

autoData['area'] = (autoData[' length']) * (autoData[' width']) * (autoData[' height']) 

autoData['area']

autoData_sort = autoData.sort_values(' length')
autoData_sort.head(10)

autoData_sort = autoData.sort_values(' length', ascending =False)
autoData_sort.head(10)