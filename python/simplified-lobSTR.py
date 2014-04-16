#!/usr/bin/env python 

import argparse
import itertools
import os.path
import sys
import time

from multiprocessing import Pool
from subprocess import call

import numpy
import numpy as np
import pysam
import scipy.stats.mstats

def getideal (unit, length):
    output=""
    scycle=itertools.cycle(unit)
    length=int(length)
    while (length != 0):
        output += scycle.__next__()
        length -= 1
    return output

def getpurity(seq1, seq2):
    oneago= None
    thisrow= list(range(1, len(seq2) + 1)) + [0]
    for x in list(range(len(seq1))):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in range(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    return thisrow[len(seq2) - 1]

def repeat_length(chrom, start, end, samples):
    """
    Return the length of the repeat at this locus as called by lobSTR.
    """
    for sample in samples:
        called_length = []

        for read in sample.fetch(chrom, start, end):
            main_bam_fields=str(read).split("\t")
            lobstr_bam_fields=str(main_bam_fields[11])
            lobstr_bam_fields=lobstr_bam_fields.replace("[","").replace("]","").replace("(","").replace(")","").replace("'","").split(", ")
            #print(main_bam_fields)
            #print(main_bam_fields[4])	
            #print(lobstr_bam_fields)
            #list out all the import vars: then print them into the database as a member of the appropriate reference loci.
            index_loci= start
            str_start= lobstr_bam_fields[1]
            str_end= lobstr_bam_fields[3]
            length_bp= int(str_end) - int(str_start)
            length_str= int(length_bp) - len(lobstr_bam_fields[5])
            str_unit= lobstr_bam_fields[5]
            str_sequence = lobstr_bam_fields[11]
            ideal=(getideal(str_unit,length_bp))
            purity=(getpurity(ideal, str_sequence))
            #add into array all essential info
            #(focusing on minimal data right now
            #can be more verbose l8r
            #chrom_array = np.append(chrom_array, chrom)
            called_length.append(length_str)

            #index_loci_array = np.append(index_loci_array, index_loci) 
            #length_str_array = np.append(length_str_array, length_str)
            #grouped_reads += current_entry
            #if ( i%1000 == 0 ):
            #    reads += 1000
            #    print(reads, "reads completed.")
            #    print(time.time()-zero_out,"seconds passed.")
        if called_length:
            yield sum(called_length) / len(called_length)

def run(group1, group2):
    with open(args.region_file) as h:
        h.__next__()
        for i,line in enumerate(h):
            fields = line.split("\t")
            chrom, start, end = fields[:3]
            start, end = int(start), int(end)
            g1_lens = numpy.array(list(repeat_length(chrom,start,end,group1)))
            g2_lens = numpy.array(list(repeat_length(chrom,start,end,group2)))
            g1_mu = g1_lens.mean()
            g2_mu = g2_lens.mean()

            if g1_lens.shape[0] > 1 and g2_lens.shape[0] > 1:
                if g1_mu != g2_mu:
                    t, p = scipy.stats.mstats.ttest_ind(g1_lens, g2_lens)
                    print(chrom, start, end, g1_mu, g2_mu, p, sep='\t')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--region-file", required=True)
    parser.add_argument("-1", nargs="+", required=True)
    parser.add_argument("-2", nargs="+", required=True)
    args = parser.parse_args()

    group1 = [pysam.Samfile(path, "rb") for path in getattr(args, "1")]
    group2 = [pysam.Samfile(path, "rb") for path in getattr(args, "2")]
    run(group1, group2)
