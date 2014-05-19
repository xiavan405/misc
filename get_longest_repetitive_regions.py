#!/usr/bin/env python

import sys

def get_length(a_file):
    for line in a_file:
        line = line.split("\t")
        line[-1] = line[-1].rstrip()
        g1avg = float(line[3])
        g2avg = float(line[4])
        avg = (g1avg + g2avg)/2
        line.append(str(avg))
        print("\t".join(line))

def main():
    infile = open(sys.argv[1],'r')
    get_length(infile)

main()
