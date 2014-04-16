#!/bin/python env

# get a grip on pysam sytax and functionality
#pysam is a wrapper of the samtools c api

import pysam

samfile = pysam.Samfile("/home/xiavan/Data/lobSTRdata/genomedata/lgs100840/lgs1000840.bam", "rb")

for alignedread in samfile.fetch('chr1', 10000, 400000):
    print(alignedread)

samfile.close()
