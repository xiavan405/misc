#!/usr/bin/env python

#intended to be used in tandem with polymorphism-standard-deviation.py 
#takes the output of psd and plots it in a few ways.

import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument('-i','--input',nargs=1,required=True,help='input text file of polymorphism-standard-deviation.py output or any text file with a similar structure.')
group.add_argument('-b','--basic',action='store_true',help='plots the standard deviations in the output file in the same order as the file.')
group.add_argument('-s','--sort',action='store_true',help='plots the standard deviations from greatest to least.')
group.add_argument('-d','--scatter',action='store_true',help='scatter plot, useful for seeing trends in the larger datasets.')
args = parser.parse_args()

def sort_plot(input_file):
    infile = open(input_file,'r')
    tuple_list = []
    for entry in infile:
        entry = entry.split(',')
        entry[-1]=entry[-1].rstrip()
        tuple_list.append(entry)
        #print(entry)
    sorted_entries = sorted(tuple_list, key=lambda x: float(x[3]),reverse=True)
    #print(sorted_entries)
    y1 = []
    y2 = []
    x = []
    for i, tuple in enumerate(sorted_entries):
        y1.append(float(tuple[3]))
        y2.append(float(tuple[-1]))
        x.append(i)
    #print(x)
    #print(y1)
    
    left = np.arange(len(sorted_entries))
    width = 0.35
    right = []
    
    for entry in left:
        right.append(int(entry)+width)
    
    plt.bar(left,y1,width,color='red')
    plt.bar(right,y2,width,color="green")
    
    #plt.set_ylabel('Std.Dev.')
    #plt.set_title("Standard Deviations of Longest Repetitive Regions")
    #plt.set_xticks(ind+width)
    #plt.set_xticklabels(y1)

    #after all formatting is done
    plt.show()

def simple_plot(input_file):
    infile = open(input_file,'r')
    y1 = []
    y2 = []
    x = []
    for i,entry in enumerate(infile):
        entry = entry.split(',')
        entry[-1] = entry[-1].rstrip()
        current_1 = float(entry[3])
        current_2 = float(entry[-1])
        #print(current_1)
        #print(current_2)
        y1.append(float(current_1))
        y2.append(float(current_2))
        x.append(i)

    left = np.arange(len(x))
    width = 0.35
    right = []
    
    for entry in left:
        right.append(int(entry)+width)
    
    plt.bar(left,y1,width,color='orange')
    plt.bar(right,y2,width,color='blue')
    plt.show()

def scatter_plot(input_file):
    infile = open(input_file,'r')
    y1 = []
    y2 = []
    x = []
    for i,entry in enumerate(infile):
        entry = entry.split(',')
        entry[-1] = entry[-1].rstrip()
        current_1 = float(entry[3])
        current_2 = float(entry[-1])
        #print(current_1)
        #print(current_2)
        y1.append(float(current_1))
        y2.append(float(current_2))
        x.append(i)

    plt.scatter(x,y1)
    plt.scatter(x,y2)
    plt.show()

def main():
    if args.basic:
        #print("printing simple plot")
        simple_plot(args.input[0])
    if args.sort:
        sort_plot(args.input[0])
    if args.scatter:
        scatter_plot(args.input[0])
    else:
        print('No plotting option given. Run \'python plot-poly-stdev.py --help\' for options.')

main()
