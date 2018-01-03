# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:58:41 2017

@author: Lenny
"""

%load_ext line_profiler
from numpy.random import randn

def add_and_sum(x,y):
    added=x+y
    summed=added.sum(axis=1)
    return summed

def call_function():
    x=randn(1000,1000)
    y=randn(1000,1000)
    return add_and_sum(x,y)

x=randn(3000,3000)
y=randn(3000,3000)

%lprun -f add_and_sum add_and_sum(x,y)

%lprun -f add_and_sum -f call_function call_function()