#!/usr/bin/env python

import numpy as np
import statistics as stats
from math import sqrt
from collections import defaultdict
import sys

#takes "tuple_lists" and passes the individual "stdev_tuples" (formatted as [<value>,<amount of times value occurs>]) to get stdev values from a population

def get_list(stdev_tuple):
    len_list = []
    for values in stdev_tuple:
        current_value = int(stdev_tuple[0])
        current_count = int(stdev_tuple[1])
        while current_count > 0:
            len_list.append(current_value)
            current_count -= 1
            if current_count == 0:
                return(len_list)
                break

def stdev(tuple_list):
    total = []
    for entry in tuple_list:
        total = total + get_list(entry)
    return(total)


def manual_stdev(tuple_list):
    total = []
    for entry in tuple_list:
        total = total + get_list(entry)
    #return(total)
    val_dict = defaultdict(int)
    for val in total:
        val_dict[val] += 1
    print("values are ", val_dict.items())
    sum_total = sum(total)
    n = len(total)
    print("n equals ",n)
    mean= sum_total/n
    print("mean equals ",mean)
    sq_diffs = []
    for value in total:
        diff = value - mean
        sq_diff = diff**2
        sq_diffs.append(sq_diff)
    sd_dict = defaultdict(int)
    for sd in sq_diffs:
        sd_dict[sd] += 1
    print("squared differences are ",sd_dict.items())
    sum_sd = sum(sq_diffs)
    n_sd = len(sq_diffs)
    mean_sd = (sum_sd/n_sd)
    print("sum of squared differences equals",sum_sd)
    print("mean of squared differences equals",mean_sd)
    standard_deviation = sqrt(mean_sd)
    print("standard deviation is the sqrt of ",sum_sd," divided by ",n," equaling ",standard_deviation)
    return(standard_deviation)

#print(get_stdev([26,96]))
#print(len(get_stdev([29,96])))

#total_lengths = (stdev([[26,96],[29,15],[15,180]]))
#print(np.std(total_lengths))
#print(stats.stdev(total_lengths))

print(manual_stdev(
    [[31, 1], [29, 290], [71, 29]]
    ))
