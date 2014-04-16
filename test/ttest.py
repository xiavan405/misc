#!/bin/env python                                                                      

from scipy import stats 
import numpy as np

#open both average databases for both exp and control
#make ndarray of averages for each value

a = stats.norm.rvs(loc=5, scale=10, size=5)

print(a)

b = stats.norm.rvs(loc=5, scale=10, size=5)

print(b)

c = [ 1 , 2 , 3 , 4 , 5 ]
d = [ 1 , 2 , 3 , 4 , 5 ]

val=stats.ttest_ind(a,b)
valb=stats.ttest_ind(c,d)

print(val)
print(valb)
