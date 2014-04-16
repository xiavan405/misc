#!/bin/python2

import random as r
count=250
#raditz=r.randint(1000,9999)

while count != 0:
	rint=r.randint(1000000,9999999)
	cnum=r.randint(1,23)
	chr = "chr%s" %cnum
	print "%s\t%s" %(chr, rint)
	count-=1
