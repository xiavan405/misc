#!/usr/bin/env python

#for entry in lobstr-output text file, grab the reference location and pull up the reads
#count the lengths of the repeat in the read and append it to a list, print stdev of that list.

import argparse 
import pysam
import numpy
from collections import defaultdict

parser=argparse.ArgumentParser()
mutually_exclusive = parser.add_mutually_exclusive_group() 
parser.add_argument('-i','--input',required=True,help='input text file of reference locations in tab delimited form. usually lobstr-compare output.')
parser.add_argument('-s','--samples',required=True,nargs=2,help='text file of paths to bam files that the lobstr-output file was derived from, the references will be called on the bams to check the reads.')
mutually_exclusive.add_argument('-l','--lengths',required=False,action="store_true",help='print ints of lengths in a list so variability can be quickly assessed.')
mutually_exclusive.add_argument('-d','--debugging',required=False,action="store_true",help="simplified output for debugging or for quick and dirty outputting of data for some purpose.")
mutually_exclusive.add_argument('--sort', required=False,action="store_true",help='prints a sorted list of tuples of [<loci>,<stdev>], sorted from greatest to least by stdev.')
args=parser.parse_args()

#when using --lengths, output defaultdicts with frequencies instead printing every value!

def generate_samples(path):
    samples_list=[]
    path = open(path,'r')
    for bam in path:
        bam = bam.rstrip()
        samples_list.append(pysam.Samfile(bam,'rb'))
    return(samples_list)

def get_stdev(chrom,start,end,samples):
    len_list = []
    for sample in samples:
        for read in sample.fetch(str(chrom),int(start),int(end)):
            main_bam_fields = str(read).split("\t")
            lobstr_bam_fields = main_bam_fields[11]
            lobstr_bam_fields=lobstr_bam_fields.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").split(", ")
            str_sequence=lobstr_bam_fields[11]
            len_list.append(len(str_sequence))
    if args.lengths or args.sort:
        len_dict = defaultdict(int)
        for entry in len_list:
            len_dict[entry] += 1
        #print lens and stdev
        return [(numpy.std(len_list)), len_dict.items()]
    else:
        return(numpy.std(len_list))

def start(a_list,sample_path_1,sample_path_2):
    samples_1 = generate_samples(sample_path_1)
    samples_2 = generate_samples(sample_path_2)
    loci_list = open(a_list,'r')
    #for args.sort
    sorted_output = []
    for i,entry in enumerate(loci_list):
        entry = entry.split("\t")
        chrom = entry[0]
        start = entry[1]
        end = entry[2]
        if args.lengths:
            stdev_1,len_list_1 = get_stdev(chrom,start,end,samples_1)
            stdev_2,len_list_2 = get_stdev(chrom,start,end,samples_2)
            print("LOCI:%s.%s.%s"%(chrom,start,end))
            print("SAMPLE GROUP 1 STDEV:", stdev_1)
            print("SAMPLE GROUP 1 LENGTHS(BP):", len_list_1)
            print("SAMPLE GROUP 2 STDEV:", stdev_2)
            print("SAMPLE GROUP 2 LENGTHS(BP):", len_list_2)
        elif args.debugging:
            stdev_1 = get_stdev(chrom,start,end,samples_1)
            stdev_2 = get_stdev(chrom,start,end,samples_2)
            stdev_tuple = [chrom,start,end,str(stdev_1),str(stdev_2)]
            print(",".join(stdev_tuple))
       #else: statement keeps firing off inappropriately!
        else:
            stdev_1 = get_stdev(chrom,start,end,samples_1)
            stdev_2 = get_stdev(chrom,start,end,samples_2)
            print("LOCI:",chrom,".",start,".",end)
            print("SAMPLE GROUP 1 STDEV:",stdev_1)
            print("SAMPLE GROUP 2 STDEV:",stdev_2)

def sorter(a_list,sample_path_1,sample_path_2):
    #print("HELLO!")
    samples_1 = generate_samples(sample_path_1)
    samples_2 = generate_samples(sample_path_2)
    loci_list = open(a_list,'r')
    sorted_output = []
    for i,entry in enumerate(loci_list):
        entry = entry.split("\t")
        chrom = entry[0]
        start = entry[1]
        end = entry[2]
        stdev_1, len_list_1 = get_stdev(chrom,start,end,samples_1)
        stdev_2, len_list_2 = get_stdev(chrom,start,end,samples_2)
        sorted_output.append([chrom+'.'+start+'.'+end,stdev_1,stdev_2,len_list_1,len_list_2])
    blah = sorted(sorted_output,key=lambda x: x[1], reverse=True)
    for entry in blah:
            loci = entry[0]
            stdevs = entry[1:3]
            lenlists = entry[3:5]
            print(loci)
            print(stdevs)
            print(lenlists)


def main():
    if args.sort:
        sorter(args.input,args.samples[0],args.samples[1])
    else:
        start(args.input,args.samples[0],args.samples[1])

main()
