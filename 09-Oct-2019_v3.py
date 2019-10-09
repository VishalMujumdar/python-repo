# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:58:50 2019

@author: vismujum
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

orders = pd.read_csv('orders.csv')
orders.shape
orders.head(10)

slots = pd.read_csv('slots.csv')
slots.shape
slots.head(10)

sum(orders.Unique_id.duplicated())
sum(slots.Unique_id.duplicated())

orders_uq = orders.drop_duplicates(['Unique_id']) 
slots_uq = orders.drop_duplicates(['Unique_id'])

sum(orders_uq.Unique_id.duplicated())
sum(slots_uq.Unique_id.duplicated())

innerJoin = pd.merge(orders_uq,slots_uq,how='inner') 
innerJoin.shape

outerJoin = pd.merge(orders_uq,slots_uq,on='Unique_id',how='outer') 
outerJoin.shape

leftJoin = pd.merge(orders_uq,slots_uq,on='Unique_id',how='left') 
leftJoin.shape

rightJoin = pd.merge(orders_uq,slots_uq,on='Unique_id',how='right') 
rightJoin.shape










