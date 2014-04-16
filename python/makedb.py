#!/bin/python2

import sqlite3
import fileinput
import sys

entrylist=open(sys.argv[1])
conn = sqlite3.connect("lobSTR.sqlite")
c = conn.cursor()

for line in entrylist:
    c.execute('''create table if not exists walnut_bams(entry_id)''')
    c.execute('''insert into "walnut_bams" ("entry_id") values ("%s")''' %line)

conn.commit()
	
