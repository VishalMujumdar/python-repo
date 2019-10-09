# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 07:09:20 2019

@author: vismujum
"""


import pandas as pd
import numpy as np
import matplotlib as mp
import os
os.getcwd()
os.chdir("C:\\dataset\\archive")
os.getcwd()

sales = pd.read_csv("yearly_sales.csv")
sales
sales.shape       # Returns dimension of datasheet
sales.columns     # name of columns

col_array = sales.columns.values
col_array[2]

#imspecting the dataset
sales.head()  # Header + first five rows
sales.tail()  # Header + botton five rows

sales1= sales.head(2000)
sales1
sales.dtypes

sales.num_of_orders.dtypes
sales["num_of_orders"].dtypes

type(sales.num_of_orders[1])

# Statistics of dataset

sales.num_of_orders.mean()   # Returns the mean value
sales.num_of_orders.std()    # Returns standard deviation

sales.describe()
sales.num_of_orders.describe()
sales.gender.value_counts()
sales.num_of_orders.value_counts()

# Identify null value

sales.gender.isnull()
sum(sales.gender.isnull())

sales_missing = pd.read_csv("yearly_sales_missing.csv")
sales_missing
sales_missing.gender.isnull()

sum(sales_missing.gender.isnull())

# Create sample data
sales.head(1000)
sales_sample = sales.sample(1000)
sales_sample.describe()
sales_sample.shape

sales.num_of_orders.mean()
sales.num_of_orders.median()

# partitioning the dataset

sales_part1 = sales[sales["num_of_orders"] == 2 ]
sales_part1.shape

sales_part2 = sales[sales["num_of_orders"]!= 2 ]
sales_part2.shape

# central tendencies
sales.num_of_orders.mean()
sales.num_of_orders.median()

#dispersion
sales.num_of_orders.var()
sales.num_of_orders.std()

#quantile
sales["num_of_orders"].quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9,1])

sales["num_of_orders"].quantile([.25,.5,.75,1])
sales.describe()

#create box plot
mp.pyplot.boxplot(sales.num_of_orders)
mp.pyplot.boxplot(sales["sales_total"])

# Create Scatter Plot
mp.pyplot.scatter(sales.num_of_orders , sales.sales_total)
mp.pyplot.plot(sales.num_of_orders , sales.sales_total)


#Creating a bar chart
num_of_order_freq = sales.num_of_orders.value_counts()
num_of_order_freq
index  = num_of_order_freq.index
index

values = num_of_order_freq.values
values

mp.pyplot.bar(index,values)

#creating a line chart 
mp.pyplot.plot(sales.num_of_orders , sales.sales_total)

import pandas as pd
# Timeseries data
series = {"month":["Jan","Feb","Mar","Apr","May","June","July"] , "sales":[12,14,15,11,16,17,21]}
series

series_df = pd.DataFrame(series)
series_df

mp.pyplot.plot(series_df.month , series_df.sales)




























