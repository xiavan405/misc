#!/usr/bin/env python

import sys
import argparse

def sorting(infile):
    to_print = []
    for line in infile:
        line = line.split("\t")
        difference = float(line[4]) - float(line[5])
        #aline.append(difference)
        to_print.append(line)
        #print(to_print)
    sorted_list = (sorted(to_print, key=lambda stuff: stuff[5]))
    for line in sorted_list:
        line[5] = line[5].rstrip()
        for i,value in enumerate(line):
            line[i] = str(value)
            print("\t".join(line))

sorting(open(sys.argv[1], 'r'))
