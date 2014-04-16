#/bin/python2

import itertools as i

print "Enter an STR unit and the length of the ideal sequence in bp."

a = raw_input("STR Unit: ")
b = raw_input("Length(BP): ")

def genideal(STR, length, output):
	scycle = i.cycle(STR)
	sanitized_length=int(length)
	while (int(sanitized_length) != 0):
		output += scycle.next()
		sanitized_length -=1
	print output

genideal(a,b,"")
