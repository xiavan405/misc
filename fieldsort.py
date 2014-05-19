#!/usr/bin/env python

import sys

def sorter(a_file):
    output_list = []
    for line in a_file:
        line = line.split("\t")
        line[-1] = line[-1].rstrip()
        output_list.append(line)
    sorted_out = sorted(output_list, key=lambda x: float(x[-1]),reverse=True)
    #print(sorted_out)
    for line in sorted_out:
        print("\t".join(line))

def main():
    infile = open(sys.argv[1],'r')
    sorter(infile)

main()
