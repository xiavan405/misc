#!/usr/bin/env python

#proof of concept for checking redundancy from one list to another to make sure it works before adding it to qlob

import argparse
from os.path import basename
from os.path import exists
from os.path import dirname
from os import stat
from os import getcwd
from subprocess import call
import logging

#argparse stuff, input, ref
parser = argparse.ArgumentParser()
parser.add_argument('-b','--bams',nargs=1,required=True,help="text file of bam locations to be lobstred")
parser.add_argument('-o','--output',nargs=1,required=True,help="location lobstr output will be saved to")
parser.add_argument('-i','--index',nargs=1,required=True,help="lobSTR index location and prefix")
args = parser.parse_args()

##global reference
##reference="./qlob.history"

def create_list_input(a_file):
    to_print = []
    for entry in a_file:
        entry = entry.split("/")
        name = entry[-1]
        name = name.split(".")
        to_print.append(name[0].rstrip())
    return(to_print)

def create_list_reference(a_reference):
    to_print = []
    for entry in a_reference:
        to_print.append(entry.rstrip())
    return(to_print)

def remove_redundants(a_file, reference):
    a_file = open(a_file,'r')
    reference = (open(reference,'r'))
    file_set = set(create_list_input(a_file))
    reference_set = set(create_list_reference(reference))
    non_redundants = file_set.difference(reference_set)
    return(non_redundants)

def record_logger(bam_id):
    #name = basename(bam_location)
    #name = name.split(".")
    #bam_id = name[0]
    a_reference = open(reference, 'a+')
    a_reference.write(bam_id)
    a_reference.write('\n')

def check_output(bam_location, output):
    new_location = output + basename(bam_location)
    if exists(new_location) == True:
        file_info = stat(new_location)
        if int(file_info.st_size) > 500:
            True
        elif int(file_info.st_size) <= 500:
            False
        else:
            error_string = str("Error in check_output() filesize check for:"+new_location)
            logger(error_string)
    else:
        print("file doesn't exist!")
        dne_error_string = str("Error in check_output() file does not exist:"+new_location)
        logger(dne_error_string)

def logger(string):
    logging.error(string)

def start(bam_id,index,output):
    
    #hardcoded value, change this if the threshold needs to be changed, maybe i should add an option
    entropy_threshold = 0.6
    #tons of hardcoded values here bc i wasnt sure how to do this without them
    bam = ("/home/xiavan/walnut/"+bam_id+"/13_final_bam/"+bam_id+".bam")
    call("lobSTR --entropy-threshold %s --bam -f  %s --index-prefix %s --out %s" %(entropy_threshold,bam,index,output+bam_id),shell=True)
    if check_output(bam,output) == True:
        record_logger(bam_id)
    else:
        pass

def main():

    reference = getcwd()+"/qlob.history"
    
    logging.basicConfig(filename="qlob.log",level=logging.ERROR)

    if exists(reference):
        bams = remove_redundants(args.bams[0],reference)
    else:
        f=open(reference,'w')
        f.write("\n")
        f.close()
        bams = remove_redundants(args.bams[0],reference)
    index = args.index[0]
    output = args.output[0]
    for bam in bams:
        bam_id = bam
        start(bam_id,index,output)

main()
