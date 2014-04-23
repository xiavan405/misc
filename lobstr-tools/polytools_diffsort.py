#!/usr/bin/env python

import sys

infile=list(open(sys.argv[1]).readlines())

def sorting(infile):
        to_print = []
        for line in infile:
            line = line.split("\t")
            difference = float(line[4]) - float(line[5])
            to_print.append(line)
        sorted_list = (sorted(to_print, key=lambda stuff: stuff[6], reverse=True))
        for line in sorted_list:
                line[6] = line[6].rstrip()
                for i,value in enumerate(line):
                    line[i] = str(value)
                print("\t".join(line))

sorting(infile)
