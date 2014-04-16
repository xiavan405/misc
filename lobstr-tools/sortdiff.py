#!/bin/env python

#! sort record based file by a field and print fields in question
#standard lobstr-compare output is tab delimited (chrom, start, end, g1_mu, g2_mu, pval)

import sys

#the field that the records will be sorted by (int index to record list)
sortby = []
#the fields to be printed if the whole record is not printed
toprint = []

infile = open(sys.argv[1])

blah = []

for line in infile:
    line = line.split("\t")
    difference = float(line[4]) - float(line[5])
    #aline.append(difference)
    blah.append(line)

#print(blah)

sorted_list = (sorted(blah, key=lambda stuff: stuff[5]))

for line in sorted_list:
    line[5] = line[5].rstrip()
    for i,value in enumerate(line):
        line[i] = str(value)
    print("\t".join(line))
