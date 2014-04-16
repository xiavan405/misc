#!/bin/env python

import time
from scipy import stats
import numpy as np
import sqlite3

#scores: stdout:~0.02sec 
#scores: one-step conn.commit():~0.33sec 
#scores: iterative conn.commit():12-20sec
#scores: passing to ndarray (preallocated array):~0.02sec 
#scores: ndarray (iterative appending): ~0.025sec

i=0
zero_out=time.time()
conn=sqlite3.connect("/home/xiavan/Testing/timetest.sqlite")
c=conn.cursor()
c.execute('''create table if not exists test("pval")''')
conn.commit()
print(time.time() - zero_out)

#my_array = np.zeros(50)
my_array = []

while (i != 50):
	a = stats.norm.rvs(loc=5, scale=10, size=100)
	b = stats.norm.rvs(loc=5, scale=10, size=100)
	pval=stats.ttest_ind(a,b)
	my_array = np.append(my_array, pval[1])
	#my_array[i] = pval[1]
	#print("pval:", pval)
	#c.execute('''insert into test("pval") values("%s")''' %str(pval))
	i+=1
	#conn.commit()
	print(time.time() - zero_out)
	if (i%3 == 0):
		print("this only prints every three times!")

print(my_array)
#conn.commit()
print(my_array)
print(time.time() - zero_out)
