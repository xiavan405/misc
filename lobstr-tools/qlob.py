#!/usr/bin/env python

import sys
import datetime
import argparse
import logging
from multiprocessing import Pool

parser=argparse.ArgumentParser()
parser.add_argument("-b", "--bams", required=True, help="text file list of bamfile locations")
parser.add_argument("-i", "--index", required=True, help="location of index file to be used with lobSTR (usually lobSTR index in ~/lobSTR/resources/")
parser.add_argument("-o", "--output", required=True, help="output location for lobSTR")
args=parser.parse_args()

def preprocessing(bamlist,index, output):
    to_be_accessed=[]
    for entry in bamlist:
        to_be_accessed.append([entry.rstrip(), index.rstrip(), output.rstrip()])
    return(to_be_accessed)

def remove_redundants(bamlist):
    bamlist = open(bamlist,'r').readlines()
    history = open("qlob_history.txt","a+").readlines()
    if history == []:
        history.append("empty")
    non_redundants=[]
    for bam in bamlist:
        non_redundants.append(bam.rstrip())
        #print("passed the bam check")
        for entry in history:
            #print("passed the history entry check")
            if bam == entry:
                #print("2")
                pass
            else:
                #print("3")
                non_redundants.append(bam.rstrip())
                break
    return(non_redundants)

'''
def old_remove_redundants(bam):
    history=open("qlob_history.txt", "a+")
    not_redundant=[]
    for line in history:
        if bam==line:
            pass
        else:
            not_redundant.append(line)
    #return(not_redundant)
'''

def record_history(bam):
    history=open("qlob_history.txt", "a+")
    history.write(bam)
    history.write("\n")

def logger(bam):
    logging.basicConfig(filename='qlob.log', level=logging.DEBUG)
    logging.debug(datetime.datetime.now())
    logging.debug(bam)

def main(bamtuple):
    print("lobstr --entropy-threshold 0.6 --bam -f ",bamtuple[0],"--index-prefix ",bamtuple[1],"--out ",bamtuple[2]) #%(bamtuple[0], bamtuple[1], bamtuple[2]))
    record_history(bamtuple[0])
    logger(bamtuple[0])

for entry in preprocessing(remove_redundants(args.bams), args.index, args.output):
    main(entry)

#if __name__ == '__main__':
#    pool = Pool(processes=2)
#    pool.map(main, preprocessing(remove_redundants(args.bams),args.index,args.output))
