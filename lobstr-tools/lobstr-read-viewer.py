#!/bin/env python

import pysam
import sys
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('locus', metavar='N', nargs=3,help='reference location where read coverage will be examined. Format is chr<N> <starting-base-count> <end-base-count>')
parser.add_argument('-s','--samples',nargs=2,required=True,help="Two text files of newline-delimited paths to lobstr-compare output, one for each group to be compared.")
parser.add_argument('-r','--reads',action="store_true",help='prints reads at every sample per group.')
args=parser.parse_args()

samples1_path=open(args.samples[0], 'r')
samples2_path=open(args.samples[1], 'r')

def generate_samples(path):
    samples_list=[]
    for bam in path:
        bam=bam.rstrip()
        samples_list.append(pysam.Samfile(bam, "rb"))
    return(samples_list)

def getlen(a_file, chrom, start, end):
    length=0
    for read in a_file.fetch(chrom, int(start), int(end)):
        length+=1
    return(length)

def reads_overview(chrom, start, end, sample):
    per_sample_counts=[]
    for samplecount,infile in enumerate(sample):
        per_sample_counts.append(getlen(infile, args.locus[0], args.locus[1], args.locus[2]))
    print("Reads at each sample:\n\n",per_sample_counts,"\n")
    print("number of samples: ",len(per_sample_counts))
    average=float(sum(per_sample_counts)/len(per_sample_counts))
    print("average: ",average)
    print("total reads: ",sum(per_sample_counts))

def get_reads(chrom, start, end, sample):
        for i,infile in enumerate(sample):
            print("\nReads for sample", i, ":\n")
            for read in (infile.fetch(args.locus[0], int(args.locus[1]), int(args.locus[2]))):
                main_bam_fields=str(read).split("\t")
                lobstr_bam_fields=str(main_bam_fields[11])
                lobstr_bam_fields=lobstr_bam_fields.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").split(", ")
                index_loci= start
                str_start= lobstr_bam_fields[1]
                str_end= lobstr_bam_fields[3]
                length_bp= int(str_end) - int(str_start)
                length_str = int(length_bp)/len(lobstr_bam_fields[5])
                str_unit= lobstr_bam_fields[5]
                str_sequence = lobstr_bam_fields[11]
                #ideal=(getideal(str_unit,length_bp))
                #purity=(getpurity(ideal, str_sequence))
                #called_length.append(length_str)
                info = [str_start, str_end, length_bp, length_str, str_unit, str_sequence]
                print(info)


samples1=generate_samples(samples1_path)
samples2=generate_samples(samples2_path)

if args.reads:
    print("\nGroup 1 :")
    get_reads(args.locus[0],args.locus[1],args.locus[2], samples1)
    print("\nGroup 2 :")
    get_reads(args.locus[0],args.locus[1],args.locus[2], samples2)
else:
    print("\nGroup 1 :")
    reads_overview(args.locus[0], int(args.locus[1]), int(args.locus[2]), samples1)
    print("\nGroup 2 :")
    reads_overview(args.locus[0], int(args.locus[1]), int(args.locus[2]), samples2)

