# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 07:08:40 2019

@author: vismujum
"""

a = 5
print('the value of a is ' , a)
a = 'My name is Vishal'

print('01. the value of a is ' , a)
b=input("Enter the value of B : ")

print('02. The value of B is (' , b , ')')
print("The Value of B is {} and  greater then a ".format(b))

print(a ,b , sep="*")

print(1,2,3,4,5, sep="*")

print(1,2,3,4,5, sep="*",end="&")

print("I love {1} and {0}".format('bread','butter','jam' )) 

x = 12.34567

print('the value of x is %2.3f' %x)

print('the value of x is %3.4f' %x)
print('the value of x is %10.3f' %x)

#if statement
i = 15
if i<10:
    print("I is less than 10")
print("Out of If loop")

i = int(input("enter the number:"))
if i<10:
    print("I is less than 10")
else:
    print("Out of If loop")
    
# Function
temp=input("Assigne temp like 45F , 102C : ")
degree = int(temp[:-1])
print(degree)
conversion = temp[-1]
print(conversion)


if conversion.upper() == "C":
    result = int(round(9*degree)/5+32)
    output = "Farenhite"
    print ( result , output)
else:
    conversion.upper() == "F"
    result = int(round(degree-32)*5/9)
    output = "Clcius"
    print ( result , output)
    
# for loops
    X =1
    for x in range( 0 , 3):
        print ('Loop execution %d' %(x))
        
#while loops
    i = 1
    while i<= 10:
        print(i)
        i = i +1

for i in range (1,5):
    for j in range(1,3):
        print ( i , "*" , j , "=" , i*j)


Count = 0
while Count <= 100:
        print(Count)
        Count += 1
        if Count >= 17:
            break
        
        
print(list(res))

   

#packages
import math
a = 5
print(math.log(a))

import math as mt
a = 5
print(mt.log(a))

import * from math 
a = 5
print(log(a))

import numpy as np
print(np.log(5) )             

        