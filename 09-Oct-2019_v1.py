# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:59:09 2019

@author: vismujum
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")

onlineRetail = pd.read_csv("Online Retail.csv" ,encoding = "ISO-8859-1")

onlineRetail.head(10)

onlineRetail.columns.values

onlineRetail_sort = onlineRetail.sort_values('UnitPrice',ascending=False)
onlineRetail_sort.head(20)