#!/bin/env python2

import sqlite3

conn = sqlite3.connect("/home/xiavan/Testing/test.sqlite")
c = conn.cursor()

c.execute('''select v from x''')
car = c.fetchall()
print car 

c.execute('''select distinct v from x''')
blah = c.fetchall()

print list(blah)

for val in list(blah):
	#find all matching values
	#get avg and std dev
	#print into new table or db
	#then run t test on that 
