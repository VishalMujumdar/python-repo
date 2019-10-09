# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:23:55 2019

@author: vismujum
"""

x = 8.9
x
y=2.98
y
print(x)
del x 
#print(x)

age = 30
print(age)

weight = 102.88
print(weight)

x=17
print(x **2)

name = "sheldon"
msg="Hello sheldon where come sie bitte"

print(name)
print(msg)
print (name[0])
print (name[1])
print (msg[0:5])

len(msg)

print(msg[10:len(msg)])

msg = "Under construction"
msg*10
print(msg*10)

msg1 = "site under construction "
msg2 = "Go to home page"
msg2 += msg1
msg1 += msg2
print(msg1)

#Examples of List

myList = ["sherry" , "male", 35 , "Consultant"]
myLen = len(myList)

for count in range(myLen):
    print(str(count) + " : "+ str(myList[count]))


myList2 = ["New Port" , "CA" , "USA" , 3003]
finalList = myList + myList2

print (finalList)
print(len(finalList))

del finalList[5]
print (finalList)

# Define tuples
myTuple = ("Mark", "Tulley" , 55)

print(myTuple)
print(len(myTuple))
print(myTuple[1])
print(myTuple[0])
print(myTuple[2])
print(myTuple[1]*10)
print(finalList)

finalList[2] = 55
print(finalList)

myTuple[2] = 55
print(myTuple)

# Dictionary
city = {0:"LA" , 1: "NY" , "two":"BOS"}
print(city)
print(city[0])
print(city[1])
print(city[2])
print(city['three'])

del city[1]

print(city)
print(city.keys())
print(city.values())

#if else
age = 49

if age < 50:
    print ( "Age is in Group 1 ")
else:
    print("Age is in Group 2")

#if-elif Statement
marks = 55

if (marks <35):
    print("Failed")
elif (marks < 60):
    print("Second Division")
elif (marks < 80):
    print("First Division")
elif (marks < 100):
    print("Distinction")
else:
    print("Error in calculation")

# Nested if
x = 55

if (x < 50):
    print("Number is less then 50")
    if (x <40):
        print("Number is less then 40")
        if (x < 30):
            print("Number is less then 30")
        else:
            print("Number is greater then 30")
    else:
        print("Number is greater then 40")
else:
    print("Number is greater then 50")
        

# For Loop
my_num = 1
for i in range (1,20):
    my_num = my_num + 1
    print("The number has value : " , my_num)


sumx = 0

for x in range (1,20):
    sumx = sumx + x
    print("Vaue of X is :<", x , "> , value of sumx is :<",sumx , ">")


# Break statement
sumx = 0
for x in range(1,200):
    print("Value of X :<",x,">. Value of sumx : <",sumx,">")
    sumx = sumx + x
    if (sumx > 500):
        break
    print(sumx)

# Functions 

def square(a):
    c = a ** a
    return c

def divide ( var1 , var2):
    a = var1 % var2
    return a

square ( 5)
divide ( 4 , 9)

import math
print(math.log(10))
print(math.exp(5))
print(math.sqrt(25))

import math as mt
print(mt.log(10))
print(mt.exp(5))
print(mt.sqrt(25))























