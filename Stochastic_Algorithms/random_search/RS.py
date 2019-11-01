#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:56:59 2019

@author: arsalan
"""
import numpy as np 
import matplotlib.pyplot as plt 
from random import random, uniform

#x = [i for i in range(0,50)]
x1  = np.random.uniform(low=0, high=1.5, size=(50,))
x1 = sorted(list(x1))

x2  = np.random.uniform(low=-1.5, high=0, size=(50,))
x2 = sorted(list(x2)) 

#y = [m*(t**4.4) + t +c for t in x]
#plt.plot(x,y,'r')



def objective_function(x_input):
    m = 1.57
    c = 3.34
    return m*(x_input[0]**4.4) + x_input[1] + c

def random_vector(search_space):
    x1 = search_space[0]
    x2 = search_space[1]
    x1_ = uniform(min(x1), max(x1))
    x2_ = uniform(min(x2), max(x2))
    return [x1_,x2_]

def search(search_space,max_iter):
    best = {}
    best['cost'] = None
    for i in range(0,max_iter):
        candidate = {}
        candidate['vector'] = random_vector(search_space)
        candidate['cost'] = objective_function(candidate['vector'])
        if best != None or candidate['cost'] < best['cost']:
            best = candidate
        print(best['cost'])
    return best

search_space = [x1,x2]
max_iter = 100

best = search(search_space,max_iter)
print(best)