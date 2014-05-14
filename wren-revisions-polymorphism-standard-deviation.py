#!/usr/bin/env python

import argparse
import pysam
import numpy
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input',nargs=1,required=True,help='input text file of reference locations in tab delimited forms. usually lobstr-compare-output.')
parser.add_argument('-s','--samples',nargs=1,required=True,help='list of bam file locations that the reads from the input file will be pulled from.')
parser.add_argument('-l','--lengths',action="store_true",required=False,help='option to print the lengths of the reads for the particular loci in defaultdict form')
args=parser.parse_args()

def generate_samples(path):
    samples_list = []
    path = open(path,'r')
    for bam in path:
        bam = bam.rstrip()
        samples_list.append(pysam.Samfile(bam,'rb'))
    return(samples_list)

def get_stdev(chrom,start,end,samples_file):
    len_list = []
    for sample in samples_file:
        for read in sample.fetch(str(chrom),int(start),int(end)):
            main_bam_fields = str(read).split("\t")
            lobstr_bam_fields = main_bam_fields[11]
            lobstr_bam_fields = lobstr_bam_fields.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").split(",")
            str_sequence = lobstr_bam_fields[11]
            len_list.append(len(str_sequence))
    len_dict = defaultdict(int)
    for entry in len_list:
        len_dict[entry] += 1
    return([(numpy.std(len_list)),len_dict])

def start(a_list,sample_path):
    samples = generate_samples(sample_path)
    loci_list = open(a_list,'r')
    sorted_output = []
    for i,entry in enumerate(loci_list):
        entry = entry.split("\t")
        chrom,start,end = entry[0:3]
        stdev, len_list = get_stdev(chrom,start,end,samples)
        repeat_length = int(end) - int(start)
        stdev_tuple = [chrom,start,end,str(stdev),str(repeat_length)]
        print(','.join(stdev_tuple))
        if args.lengths:
            current_dict = str(len_list.items())
            #just some formatting to get rid of the "dict.items(...)" when printing to stdout
            print(str(len_list.items())[11:-1].replace("(","[").replace(")","]"))
def main():
    start(args.input[0],args.samples[0])

main()
