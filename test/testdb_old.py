#!/bin/env python

#this will take the distinct values of a given lobstr-compare db file and get average info.

import sqlite3
import numpy as np

print("Please input the path to the database of lobstr bam info.")
db=input("> ")
print("please input a name/path for the output database.")
out_db=input("> ")
conn = sqlite3.connect(db)
c = conn.cursor()
out_conn=sqlite3.connect(out_db)
out_c=out_conn.cursor()

c.execute('''show tables;''')
tables=list(c.fetchall())

def getinfo():
	for entry in tables:
		c.execute('''select distinct index_loci from %s''' %entry)
		out_c.execute('''create if not exists table %s("index_loci","mean","stdev")''' %entry)
		for value in c.fetchall():
			c.execute('''select length_bp from %s where index_loci = %s''' %(entry, value))
			current_values = np.ndarray(c.fetchall())
			current_average = current_values.mean()
			current_stdev = current_values.std()
			out_c.execute('''insert into "%s" ("index_loci", "mean", "stdev") values("%s", "%s", "%s")''' %(entry, value, current_average, current_stdev))

