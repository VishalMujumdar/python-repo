# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 07:06:25 2019

@author: vismujum
"""

import numpy as np
income = np.array([1000, 2000 , 3000 , 4000 , 5000])
print(income)

expenses = income *.6
print(expenses)

saving = income - expenses
print(saving)

import pandas as pd
data = {"name":["ram","shyam","Mahesh"], "age":[23, 35 , 45]}
df = pd.DataFrame(data)

print(df)

import os 
os.getcwd()

os.chdir("C:\\dataset\\archive")
os.getcwd()

data1= pd.read_csv("yearly_sales.csv")
print(data1)

data1.columns
print(data1.gender)
print(data1.gender[1])

print(data1.gender[0:10])

import matplotlib as mp
x = np.random.normal(0,1,1000)
y = np.random.normal(0,1,1000)

print(x)
print(y)

mp.pyplot.scatter(x,y)

import sklearn as sklearn 

print(data1.columns)

x1  = data1["num_of_orders"]
y1 = data1["sales_total"]

x1 = x1.values.reshape(-1,1)
y1 = y1.values.reshape(-1,1)

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(x1,y1)

print("Cofficient is : " , reg.coef_)
print("Intercept is : " , reg.intercept_)

# Data Handling

data1= pd.read_csv("yearly_sales.csv")
print(data1)

data2 = pd.read_excel("housing.xlsx","housing_train")
print(data2)

data1.shape

data2.shape

data1.columns.values
data1.dtypes
data1.no_of_orders.dtypes
data1.head()
data1.head(10)
data1.tail()

data1.describe()

data1.gender.value_counts()
data1.gender.isnull()
sum(data1.gender.isnull())

data3= pd.read_csv("yearly_sales_missing.csv")
print(data3)
data3.gender.isnull()
sum(data3.gender.isnull())

# Subset

data1.sample(25)
data1.head(25)
data4 = data1.iloc[[2 , 4, 6 ,8, 12]]
data4

data5 = data1[["cust_id" , "gender"]]
data5

data6 = data1[["cust_id" , "gender"]][1:25]
data6

#Data filtering
data7 = data1[(data1["gender"]=="F") & (data1["num_of_orders"]>10)]
data7
data8 = data1[(data1["gender"]=="F") | (data1["num_of_orders"]>10)]
data8

# Creating a New Column
data1["Unit_price"] = (data1["sales_total"])/(data1["num_of_orders"])
data1.columns
data9 = data1.sort_values("sales_total")
print(data9)

#Sorting of Data
data10 = data1.sort_values("sales_total", ascending = False)
print(data10)

#Duplicate Values
data11= pd.read_csv("yearly_sales_dup.csv")
print(data11)

data12 = data11.duplicated()
data12
print(data12)

sum(data12)

data15 = data12.drop_duplicates()
data15.shape

data16 = data11.cust_id.drop_duplicates()
data16.shape

data17 = data11.drop_duplicates(["cust_id"])
data17.shape


#merging data set
data18 = pd.read_csv("age.csv")
print(data18)

data19 = pd.read_csv("income.csv")
print(data19)

sum(data18.duplicated(["cust_id"]))
sum(data19.duplicated(["cust_id"]))

data18.shape
data20 = data18.drop_duplicates(["cust_id"])
data20.shape
data21 = data19.drop_duplicates(["cust_id"])

data22 = pd.merge(data20,data21,on="cust_id" , how="inner" )
data22.shape

data23 = pd.merge(data20,data21,on="cust_id" , how="outer" )
data23.shape

data24 = pd.merge(data20,data21,on="cust_id" , how="left" )
data24.shape

data25 = pd.merge(data20,data21,on="cust_id" , how="right" )
data25.shape

#exporting the output
data25.to_csv("rjoin.csv")

























