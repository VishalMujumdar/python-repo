# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 23:17:27 2019

@author: vismujum
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

bankData = pd.read_csv("bank_market.csv")

bankData.shape

bankData.columns.values

bankData_v1 = bankData.head(1000)
bankData_v1.shape

bankData_v2 = bankData[["Cust_num","age","default","balance"]]
bankData_v2.head(5)

bankData_v3 = bankData[["Cust_num","age"]][20000:20100]
bankData_v3.head(10)

bankData_v41 = bankData.drop(['poutcome','y'],axis=1 )[20000:20020]
bankData_v41.head(5)

bankSubset = bankData[(bankData['age'] > 40) &(bankData['loan'] == "no")]

bankSubset.shape
bankData.shape


bankSubset_v1 = bankData[(bankData['age'] > 40) | (bankData['loan'] == "no")]

bankSubset_v1.shape
bankSubset.shape
bankData.shape

bankSubset_v2 = bankData[(bankData['age'] > 40) & (bankData['loan'] == "no") | (bankData['marital']=="single")]

bankSubset_v2.shape













