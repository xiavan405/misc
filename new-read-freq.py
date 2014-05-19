#!/usr/bin/env python

#takes the lobstr-compare-output and pumps out read info for each locus.
#try to use multiprocessing where applicable

import pysam
import argparse
from collections import defaultdict

parser=argparse.ArgumentParser()
parser.add_argument('--locus','-l',nargs=1,required=True,help='text file, probably lobstr-compare output, list of reference location formatted loci. format: <chrX> <start_bp> <end_bp>')
parser.add_argument('--samples','-s',nargs=1,required=True,help='two text files of the locations of all the samples of lobstr output in bam format or any bams with repetitive loci.')
parser.add_argument('-w','--walnut',action='store_true',required=False,help='if you are accessing the original bams from walnut, use this option to format the reference labels appropriately (<1> instead of <chr1>)')
parser.add_argument('-r','--reads',action='store_true',required=False,help='directly print reads instead of dicts.')
args = parser.parse_args()

def generate_samples(path):
    samples_list=[]
    path = open(path,'r')
    for bam in path:
        bam =bam.rstrip()
        samples_list.append(pysam.Samfile(bam,"rb"))
    return(samples_list)

def get_len(a_file,chrom,start,end):
    length=0
    for read in a_file.fetch(chrom,int(start),int(end)):
        length += 1 
    return(length)

def counter(chrom,start,end,sample):
    per_sample_counts=[]
    for samplecount, infile in enumerate(sample):
        per_sample_counts.append(str(get_len(infile,chrom,start,end)))
    return(per_sample_counts)

def start(loci_list, sample_path):
    #print("main function called")
    #pysam takes a few seconds to open all the bams, so there is some
    #startup time before the program starts spitting out read coverage
    samples = generate_samples(sample_path)
    #print("Samples formatted")
    loci_list = open(loci_list[0],'r')
    dict_1 = defaultdict(int)
    #print("Dictionaries initialized")
    for i,entry in enumerate(loci_list):
        entry = entry.split("\t")
        if args.walnut == True:
            chrom = str(entry[0][3])
        else:
            chrom = str(entry[0])
        start = int(entry[1])
        end = int(entry[2])
        #print("Starting count:")
        #print("S,1,%s,%s,%s"%(chrom,start,end))
        #print(",".join(counter(chrom,start,end,samples)))
        if args.reads == True:
            #call the reads!
            for sample in samples:
                for read in sample.fetch(chrom,start,end):
                   # main_bam_fields=str(read).split("\t")
                   # lobstr_bam_fields=str(main_bam_fields[11])
                   # lobstr_bam_fields=lobstr_bam_fields.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").split(", ")
                   # index_loci= start
                   # str_start=lobstr_bam_fields[1]
                   # str_end=lobstr_bam_fields[3]
                   # length_bp=int(str_end) - int(str_start)
                   # length_str= int(length_bp)/len(lobstr_bam_fields[5])
                   # str_unit= lobstr_bam_fields[5]
                   # str_sequence= lobstr_bam_fields[11]
                   # info= [str_start, str_end, length_bp, length_str, str_unit, str_sequence]
                   # print(info)
                   print(read)
        else:
            for entry in counter(chrom,start,end,samples):
                #print(entry)
                dict_1[entry] += 1
           
            print("returning dicts")
            print(dict_1.items())

def main():
    #print("calling main function")
    start(args.locus,args.samples[0])

main()
