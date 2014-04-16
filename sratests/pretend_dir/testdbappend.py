#this is just the python version and using practice with the sqlite3 module since it seems to be giving trouble.

import sqlite3

conn = sqlite3.connect("automateSRA.sqlite")

c = conn.cursor()

my_array=[ '11', '12', '13', '14', '15']

for arg in my_array:
	print arg
	c.execute('''insert into "current_entries" values ("%s");''' %arg)
	conn.commit()
