# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 07:15:06 2019

@author: vismujum
"""

# define a new function
def my_function():
    print("Good morning")


my_function()

# function with input argument

def my_function1(fname):
    print("Good Morning " + fname)
    
    
    
my_function1("Vishal")

def my_function2(country = "india"):
    print("I am from  " + country)
    

my_function2()
my_function2("USA")

def my_function3(fruits):
    for x in fruits:
        print(x)


fruits=("apple", "mango" , "banana" , "guava" , "straberry")

my_function3(fruits)

def my_function5(state1 , state2 , state3 , state4 , state5 ):
    print("The sate in north is " + state3)

my_function5("Bihar" , "MP", "UP","Haryana" , "Punjab")

def my_function6(*state ):
    print("The sate in north is " + state[3])
    
my_function6("Bihar" , "MP", "UP","Haryana" , "Punjab" , "Goa")

my_function6("Bihar" , "MP", "UP")

# Function to check weather a number is even or odd
ecounter = 0
ocounter = 0
def evenodd(x):

    if (x%2 ==0):
        print("even : <" + str(x) +">")
        ecounter += 1
    else:
        print("odd : <" + str(x) + ">")
        ocounter += 1

        
evenodd(3)
evenodd(6)

for x in range (100):
    evenodd(x)
    
    

def counter(x):
    ecounter = 0
    ocounter = 0
    for i in range(x):
        if (i%2 ==0):
            print("even : <" + str(i) +">")
            ecounter += 1
        else:
            print("odd : <" + str(i) + ">")
            ocounter += 1
    print("Total events are :<"+str(ocounter) +">" + "even counters are : < "+ str(ecounter) +">")

counter(100)

# Swap two values of variable
def swap(x , y):
    print("Values X before swapping <"+str(x)+">")
    print("Values Y before swapping <"+str(y)+">")
    temp = x 
    x =y
    y = temp
    print("Values X after swapping <"+str(x)+">")
    print("Values Y after swapping <"+str(y)+">")
    
swap(45 , 12)


# File Handling
import os
os.getcwd()

f = open("C:\\dataset\\python\\test1.txt","r")
if f.mode == "r":
    contents = f.read()
    print(contents)
f.close()

y=open("test2" , "w+")
for i in range(10):
    y.write("This is line number %d\n " %i)
y.close()

y=open("test2" , "a")
for i in range(10):
    y.write("This is line number %d\n " %i)
y.close()
    