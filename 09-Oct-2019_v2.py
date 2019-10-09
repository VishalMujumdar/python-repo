# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:43:19 2019

@author: vismujum
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

billData = pd.read_csv("Bill.csv")
billData.shape
billData.columns.values
billData.describe
billData.dtypes
billData.head(10)

dups = billData.duplicated()
sum(dups)

billData.shape

billData_unique = billData.drop_duplicates()
billData_unique.shape

dups_id = billData.cust_id.duplicated()

billData.shape

billData_unique = billData.drop_duplicates(['cust_id'])
billData_unique.shape