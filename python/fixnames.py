#!/bin/python env

import sys
import os

rfile = open(sys.argv[1], "r")

for line in rfile:
    line = line.rstrip("\n")
    name = os.path.basename(line)
    #print(name[0:9], line)
    print("/home/xiavan/walnut/"+name[0:9]+"/13_final_bam/by_chr/"+name)
