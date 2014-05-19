#!/usr/bin/env python

import pysam
import sys

def generate_samples(path):
    samples_list = []
    for  bam in path:
        bam = bam.rstrip()
        samples_list.append(pysam.Samfile(bam,'rb'))
    return samples_list

def reader(chrom,start,end,samples_list):
    for sample in samples_list:
        for read in sample.fetch(chrom,start,end):
            print(read)

def start(chrom,start,end,sample_path):
    #takes chr start end input and has a hardcoded list of bams to check against
    #maybe make that an option if you follow up on this
    samples = generate_samples(sample_path)
    print(samples)
    chrom = str(chrom[3])
    start = int(start)
    end = int(end)
    reader(chrom,start,end,samples)

def main():
    start(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

main()
