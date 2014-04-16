#!/bin/python2
import random as r

count=0
countb=0

list=('blah.')

while (count != 20):
	count += 1
	coin=r.randint(1,2)
	if (r == 1):
		list = list + ('blah.')
	else:
		list = list + ('bleh.')
	

print list

