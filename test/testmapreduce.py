#!/bin/python2

from multiprocessing import Pool

ref = open('/home/xiavan/Testing/test/test.txt','r')
list = ["t.e.s.t.","c.a.r.","d.o.g."]

def printstuff(x):
	blah= x.split(".")
	print blah

if __name__ == '__main__':
	pool = Pool(processes=2)
	pool.map(printstuff, ref)
