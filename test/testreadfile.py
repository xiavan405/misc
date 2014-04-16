#!/bin/python2

f = open('/home/xiavan/Tools/lobSTR/resources/lobstr_v2.0.3_hg19_strinfo.tab', 'r')

for line in f:
	entry = line.split("\t")
	print entry[0]
