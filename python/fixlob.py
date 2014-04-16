#!/bin/python env

#! take list of stats and bams and print only bam files. 

import sys

test = ['\n']
rfile = open(sys.argv[1], "r")

def getbams(infile):
    for i,line in enumerate(infile):
        splitline = line.split(" ")
        #print(splitline)
        if splitline == test:
            pass
        else:
            if (len(splitline) == 11):
                name = splitline[10].rstrip('\n')
            else:
                name = splitline[9].rstrip('\n')
            namesplit = name.split(".")
            stats = "stats"
            if stats in namesplit:
                pass
            else:
                print("/home/xiavan/Data/lobSTRdata/genomedata/unsorted_old_data/"+name)

getbams(rfile)
