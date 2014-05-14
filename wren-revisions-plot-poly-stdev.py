#!/usr/bin/env python

#use repeat length as the x value
#combine results from both sample sets
#i could quickly make a combined set, and have argparse reflect that actually

import argparse
import matplotlib.pyplot as plt
import numpy as np

parser=argparse.ArgumentParser()
parser.add_argument('-i','--input',nargs=1,required=True,help='input text file with loci,2 sample set stdevs, and repeat length fields per line.')
parser.add_argument('-p','--plot',nargs=1,required=False,help='basic scatter plot of repeat length v. stdev')
args = parser.parse_args()

def plotter(input_file):
    infile = open(input_file,'r')
    y=[]
    x=[]
    for entry in infile:
        entry = entry.split(',')
        entry[-1]=entry[-1].rstrip()
        current_stdev=float(entry[3])
        current_repeat_length=float(entry[-1])
        y.append(current_stdev)
        x.append(current_repeat_length)
    ax = plt.scatter(x,y)
    plt.ylabel("Standard Deviation", fontsize=20)
    plt.xlabel("Repeat Length(bp)", fontsize=20)
    plt.title("Title",fontsize=20)
    plt.show()
    #print(x)
    #print(y)
    #print('howdy')
    #heatmap,xedges,yedges=np.histogram2d(x,y,bins=(584,312))
    #extent = [xedges[0],xedges[-1],yedges[0],yedges[-1]]

    #plt.clf()
    #plt.imshow(heatmap)
    #plt.show()

def main():
    plotter(args.input[0])

main()
