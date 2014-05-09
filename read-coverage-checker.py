#!/usr/bin/env python

import pysam
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c","--cutoff",help="cutoff point (in number of reads)")
parser.add_argument("-s","--samples",nargs=2,help="pair of text files of paths to the bam files containing the reads on the loci of interest")
parser.add_argument("-i","--input",help="lobstr compare output file that will be culled for loci with less than the cutoff amount of reads in the samples")
args = parser.parse_args()

def generate_samples(path):
    path = open(path,'r')
    samples_list=[]
    for bam in path:
        bam = bam.rstrip()
        samples_list.append(pysam.Samfile(bam,"rb"))
    return(samples_list)

def filtered_reads(infile,cutoff,sample1,sample2):
    infile = open(infile,'r')
    sample1 = generate_samples(sample1)
    sample2 = generate_samples(sample2)
    samples = sample1 + sample2
    acceptable_reads = []
    for i,locus in enumerate(infile):
        locus = locus.split("\t")
        chrom = locus[0]
        start = int(locus[1])
        end = int(locus[2])
        total = 0
        for sample in samples:
            for read in sample.fetch(chrom,start,end):
                total += 1
        if total >= int(cutoff):
            acceptable_reads.append("\t".join(locus))
    for entry in acceptable_reads:
        print(entry)

filtered_reads(args.input, args.cutoff,args.samples[0],args.samples[1])
