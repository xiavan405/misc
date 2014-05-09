#!/usr/bin/env python

import sys

infile=open(sys.argv[1]).readlines()

for line in infile:
    line=line.split("\t")
    line[5]=line[5].rstrip()
    diff=int(line[2])-int(line[1])
    line.append(str(diff))
    print("\t".join(line))
