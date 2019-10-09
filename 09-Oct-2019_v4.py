# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:21:48 2019

@author: vismujum
"""

import pandas as pd
import os


os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

bills = pd.read_csv('Bill_v1.csv')
bills.shape
bills.head(10)
bills.columns.values

complaints = pd.read_csv('Complaints_v1.csv')
complaints.describe
complaints.shape
complaints.head(10)
complaints.columns.values

bills_uq = bills.drop_duplicates(['cust_id'])
bills_uq.shape

complaints_uq = complaints.drop_duplicates(['cust_id'])
complaints_uq.shape

complains_outer = pd.merge(bills_uq , complaints_uq , how="outer" , on="cust_id" )
complains_outer.shape

complains_inner = pd.merge(bills_uq , complaints_uq , how="inner" , on="cust_id" )
complains_inner.shape

complains_right = pd.merge(bills_uq , complaints_uq , how="right" , on="cust_id" )
complains_right.shape

complains_left = pd.merge(bills_uq , complaints_uq , how="left" , on="cust_id" )
complains_left.shape

# Test Details
import statistics 

dataSet = [27,23,22,38,43,24,25,23,22,54,31,30,29,48,27,25,29,28,26,33,25,21,23,34,20,23]
statistics.mean(dataSet)
statistics.mode(dataSet) 
statistics.median(dataSet) 
statistics.variance(dataSet)


arthemetic =  pd.read_csv('arthemetic.csv')
arthemetic.describe()

