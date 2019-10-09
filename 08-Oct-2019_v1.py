# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:52:22 2019

@author: vismujum
"""
import pandas as pd

import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

# Read the GDP file

gdp = pd.read_csv("GDP.csv", encoding="ISO-8859-1")

gdp.shape
gdp.columns.values

gdp_v1 = gdp.head(10)
print(gdp_v1)

gdp_v2 = gdp[["Country","Rank"]]
gdp_v2

gdp_v3 = gdp.iloc[[2,9,15,25]]
gdp_v3

gdp_v4 = gdp[["Country","GDP"]][0:10]
gdp_v4

gdp_v5 = gdp.drop(["Country_code"],axis=1)[0:12]
gdp_v5