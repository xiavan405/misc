#!/bbash basenamein/python env

import sys
import sqlite3
import os

db = "/home/xiavan/Data/lobSTRdata/exomedata/lobSTR.sqlite"
conn = sqlite3.connect(db)
c = conn.cursor()

rfile = open(sys.argv[1])

for line in rfile:
    name = os.path.basename(line)
    c.execute('''insert into walnut_bams values("%s")''' %name)

conn.commit()
print("Done!")
exit()
