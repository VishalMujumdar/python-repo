# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:08:13 2019

@author: vismujum
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\dataset\\python-ex")
os.getcwd()

# Read Sales Sample csv file
Sales = pd.read_csv("Sales_sample.csv")

Sales
Sales.shape
Sales.columns.values
Sales.head(10)
Sales.tail(10)
Sales.dtypes
Sales.custId.dtype
type(Sales.custId[1])
Sales.describe()

#Sales.column.values
Sales.columns.values
Sales.custName.values
Sales['unitsSold'].describe()
Sales.salesChannel.value_counts()

sum(Sales.custId.isnull())
Sales.sample(n=10)


# Read Sales by Country csv file
salesCountry = pd.read_csv("Sales_by_country_v1.csv")
salesCountry.shape
salesCountry.columns.values
salesCountry.head(10)
salesCountry.tail(5)
salesCountry.describe()
salesCountry.apply(lambda x:[x.unique()])

salesCountry.unitsSold.describe()
salesCountry.custCountry.describe()
salesCountry.custCountry.value_counts()

sales_v1 = salesCountry.head(30)

sales_v1

del(sales_v1)

#sales_v1












