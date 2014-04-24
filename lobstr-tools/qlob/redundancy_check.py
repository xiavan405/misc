#!/usr/bin/env python

import sys
#remember sets are inbuilt now

bamfile = open(sys.argv[1]).readlines()
historyfile=open(sys.argv[2]).readlines()

bamset = set(bamfile)
historyset=set(historyfile)

non_redundants=bamset.intersection(historyset)

print("bams")
print(bamset)
print("history")
print(historyset)
print("difference")
print(non_redundants)
