#!/usr/bin/env python

import sys
import datetime
import argparse
import logging
from multiprocessing import Pool
from os.path import basename
from os.path import exists
from os import stat

parser=argparse.ArgumentParser()
parser.add_argument("-b", "--bams", required=True, help="text file list of bamfile locations")
parser.add_argument("-i", "--index", required=True, help="location of index file to be used with lobSTR (usually lobSTR index in ~/lobSTR/resources/")
parser.add_argument("-o", "--output", required=True, help="output location for lobSTR")
parser.add_argument("-n", "--norun", action="store_true", help="only prints list of files to be accessed after referencing history. For debugging purposes.")
args=parser.parse_args()

def preprocessing(bamlist,index, output):
    to_be_accessed=[]
    for entry in bamlist:
        to_be_accessed.append([entry.rstrip(), index.rstrip(), output.rstrip()])
    return(to_be_accessed)

def rrv2(bamlist):
    bamlist = open(bamlist,'r').readlines()
    history=open("qlob_history.txt","a+").readlines()
    bamlist = set(bamlist)
    history = set(history)
    non_redundants = bamlist.difference(history)
    return non_redundants

def remove_redundants(bamlist):
    bamlist = open(bamlist,'r').readlines()
    history = open("qlob_history.txt","a+").readlines()
    if history == []:
        history.append("empty")
    non_redundants=[]
    for bam in bamlist:
        #non_redundants.append(bam.rstrip())
        for entry in history:
            if bam == entry:
                #print("2")
                pass
            else:
                #print("3")
                non_redundants.append(bam.rstrip())
                break
    return(non_redundants)

def record_history(bam):
    history=open("qlob_history.txt", "a+")
    history.write(bam)
    history.write("\n")

def logger(bam, boolean):
    if boolean == True:
        logging.info(datetime.datetime.now())
        logging.info(bam)
    elif boolean == False:
        error_string=str("Filesize indicates bamfile is empty: "+bam)
        logging.error(error_string)

def check_output(bam_location, output):
    new_location=output+basename(bam_location)
    if exists(new_location) == True:
        file_info = stat(new_location)
    #usually am empty bam, which would generated when the sshfs
    #becomes unmounted, will be about 450 bytes, so I chose 500 as the cutoff.
        if int(file_info.st_size) > 500:
            True
        elif int(file_info.st_size) <= 500:
            False
        else:
            error_string=str("Error in check_output() filesize check for "+new_location)
            logging.error(error_string)
    else:
        print("file doesn't exist!")
        dne_error_string=str("Error in check_output() file does not exist: "+new_location)
        logging.error(dne_error_string)

def main(bamtuple):
    print("lobstr --entropy-threshold 0.6 --bam -f ",bamtuple[0],"--index-prefix ",bamtuple[1],"--out ",bamtuple[2]) #%(bamtuple[0], bamtuple[1], bamtuple[2]))
    
    '''
    check_output will check the filesize of the lobstr output file and as long as it is 
    greater than 500kb it will be considered valid. Then it can be added to the log and
    the history file stating it has been completed.
    '''
    
    if check_output(bamtuple[0], args.output) == True:
        record_history(bamtuple[0])
        logger(bamtuple[0], True)
    else:
        logger(bamtuple[0], False)
        
    '''
    If the check_output finds a file too small, it will log that the file did not get
    completely processed by lobSTR, usually this will result from the sshfs file
    system becoming unmounted after a period of time. logger() will need to deal with
    both positive and negative check_output() results which is why i added the boolean
    parameter.
    '''

#initialize logging file
logging.basicConfig(filename='qlob.log', level=logging.DEBUG)
#unparallelized start of qlob

if args.norun == True:
    stuff_to_print=(preprocessing(rrv2(args.bams),args.index,args.output))
    for entry in stuff_to_print:
        print(entry[0])
else:    
    for entry in preprocessing(rrv2(args.bams), args.index, args.output):
        main(entry)

#if __name__ == '__main__':
#    pool = Pool(processes=2)
#    pool.map(main, preprocessing(remove_redundants(args.bams),args.index,args.output))
