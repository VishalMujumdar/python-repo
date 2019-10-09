# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:26:57 2019

@author: vismujum
"""

import  math
import random 
x = 24

v01 = math.sqrt(x)
v02 = (math.ceil(v01))*(-1)
v03 = math.floor(v01)

print ("Original number is : <" + str(x) + "> Square Root is <" + str(v01)+">. Ceiling value is : <"+ str(v02) +"> Floor value is <"+ str(v03)+">" )
print (" Absolute values are v01 : <"+ str(math.fabs(v01)) + "> v02 : <"+str(math.fabs(v02)) +" > v03: < "+ str(math.fabs(v03)) +">")


x01 = 4 
v04 = math.exp(x01)

print("Exponential value is : < "+ str(v04) + ">")

x02 = 100
v05 = math.log(x02)
v06 = math.log10(x02)

print("Log value is <" + str(v05) + "> and log base 10 value is :<"+ str(v06) +">")

v06 = math.pow(10 , 2)
print("Value of power is : <"+str(v06)+">")


x03 = 30


v07 = math.sin(x03)
v08 = math.cos(x03)
v09 = math.tan(x03)

print(" Sin value is :<"+str(v07)+">"+ "COS value is :<"+str(v08)+"> TAN value is :<"+str(v09)+">")

print(math.degrees(3))
print(math.radians(180))

# Random functions
print(random.random)
print(random.randint(3,6))
print(random.uniform(4,7))
print(random.randrange(10,100,4))

#Built in function
y = 25
print("Absolute valuee is :<"+str(abs(25))+">")

print(max(10,11,12,16,17))
print(min(10,11,12,16,17))
print(divmod(100,80))
print(len("vishal"))

range(10)
print(range(1,10))

print(range(10))

print(round(80.34567889,2))

print(math.sin(90/360*2*(math.pi)))

def sayHello():
    print("Hello World !!")
    

sayHello()

# Function to identify area

def area(radius):
    a = radius ** 2
    return a

area(4)

def check(num):
    if (num %2 ==0):
        print("true")
    else:
        print("false")
        
571+95
19*17  
print(57+39)
print(18*17)
print("data vedi")
print(34/56)
print(600+900)
#576-'96'
22/7
#Print(800+9)




















