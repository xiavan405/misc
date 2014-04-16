#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(description="Perform various filtering on lobstr-compare output text files. Only one filtering option can be selected at a time.")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-i", "--input", nargs=1, help="Requires lobstr-compare output or similar tab-delimited data as the input text file.", required=True)
group.add_argument("-f", "--findp", action="store_true", help="Finds all loci with p-values less than 0.05")
group.add_argument("-s", "--sorting", action="store_true", help="Sorts all loci entries by p-value.")
group.add_argument("-b", "--bonferroni", action="store_true", help="Performs Bonferroni multiple test correction.")
group.add_argument("-z", "--notzeroes", action="store_true", help="Finds all loci with nonzero p-values less than 0.05.")
args = parser.parse_args()

opened_file=open(args.input[0])
infile = opened_file.readlines()
inlen = len(infile)

to_print=infile

def find_sigp(infile):
    to_output = []
    for line in infile:
        line = line.split("\t")
        if (float(line[5]) < 0.05):
            line[5] = line[5].rstrip()
            line = "\t".join(line)
            print(line)

def find_notzeroes(infile):
    for line in infile:
        line = line.split("\t")
        if (float(line[5]) != 0.0) and (float(line[5]) < 0.05):
            line[5] = line[5].rstrip()
            line = "\t".join(line)
            print(line)

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

def bonferroni(infile, inlen):
    for line in infile:
        outputlist = []
        #print(line)
        line = line.split("\t")
        #line[5] = line[5]*inlen
        #line[5] = line[5].rstrip("\n")
        #line = "\t".join(line)
        outputlist.append(line[0])
        outputlist.append(line[1])
        outputlist.append(line[2])
        outputlist.append(line[3])
        outputlist.append(line[4])
        bf = line[5].rstrip()
        fixed = float(bf)*int(inlen)
        outputlist.append(fixed)
        to_print = "\t".join([outputlist[0],outputlist[1],outputlist[2],outputlist[3],outputlist[4],str(outputlist[5])])
        print(to_print)

#not seeing the arguments for some reason
def main(an_input):
    if args.bonferroni == True:
        an_input = bonferroni(an_input, inlen)
    if args.findp == True:
        an_input = find_sigp(an_input)
    if args.notzeroes == True:
        an_input = find_notzeroes(an_input)        
    if args.sorting == True:
        an_input = sorting(an_input)
    if (args.findp == False) and (args.notzeroes == False) and (args.bonferroni == False) and (args.sorting ==False):
        print("No options specified.")
        exit()
    print(an_input)

main(to_print)
exit()
