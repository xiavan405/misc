#!/bin/env python

#this will take the distinct values of a given lobstr-compare db file and get average info.

import sqlite3
import numpy as np
from scipy import stats

#switch to sys arguments later
print("Please enter path to database for experimental values.")
exp_db=input("> ")
print("Please enter path to database for control values.")
ref_db=input("> ")
conn=sqlite3.connect(exp_db)
out_conn=sqlite.connect(ref_db)
exp=conn.cursor()
ref=out_conn.cursor()

c.execute('''show tables;''')
tables=list(c.fetchall())

def ttest(exp, control):
	return(stats.ttest_ind(exp, control))
