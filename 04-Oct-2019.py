# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:53:34 2019

@author: vismujum
"""

import numpy as np

income = np.array([9000 , 8500 , 9800 , 12000 , 7900 , 6700 , 10000])
print (income)
expenses = income * 0.70
savings = income - expenses

print ("Expenses : " , expenses)
print ("Savings : " , savings)

# Data Manupulaion and analysis 
import pandas as pd
buyer_profile = pd.read_csv('C:\\dataset\\Intro to Python\\1.Python Introduction\\datasets\\Buyer_Profile_Train_data.csv')
print(buyer_profile)

print(buyer_profile.Age)
print(buyer_profile.Gender)
print(buyer_profile.Bought)
print(buyer_profile.Age[0])
print(buyer_profile.Age[0:10])

# Data Visulization and Scientifical calculations

import matplotlib as mp
import numpy as np

X = np.random.normal(0,1,1000)
Y = np.random.normal(0,1,1000)
mp.pyplot.scatter(X,Y)

# Sklearn examples 

air_passengers = pd.read_csv('C:\\dataset\\Intro to Python\\1.Python Introduction\\datasets\\AirPassengers.csv')

print(air_passengers)
X = air_passengers['Promotion_Budget']

print (X)
X = X.values.reshape(-1 ,1 )
print(X)

Y = air_passengers['Passengers']
Y=Y.values.reshape(-1,1)
print(Y)

from sklearn import linear_model
