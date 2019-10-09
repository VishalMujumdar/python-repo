# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:07:08 2019

@author: vismujum
"""

def fn1(x):
    return x+1

def fn2(x):
    return x+1.0

def fn3(x,y):
    return x+y

def fn4(x,y,z):
    return (x>=y) and (x<=z)

def f5(x,y):
    return x>y


print(fn1(1))

fn1(6)
fn1(-5.3)
fn1(fn1(fn1(6)))
fn3(fn1(4),fn2(6.2))


f5('apple', 'ant')
fn2 (2.5)

fn2(2)
fn3( 3 , 4.6)
fn4( 7 , 4 ,9)
f5 ( 2 ,3 )

x = 8
y = 9
print (x , y)

#del x 
#print(x)

#1x = 20

x1 = 20
x1

#x.1 = 35

l = 30
a = 3
la = 30

#x.1 = 56



