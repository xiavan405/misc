#! for each entry in a list, look through another list for matching valuse and print
#maybe i should just use set instead.
import sets

a = range(1,6)
b = range(5,10)
c=(10,12,14,16,18,20)
d=range(10,21)
e=('a','b','a','c','a','d')
f=(0,1,2,1,3,1,4,1,5,1)

print a
print b

def findmatch(first, second):
	first_set=set(first)
	second_set=set(second)
	matches=first_set.intersection(second_set)
	print matches

#findmatch(a,b)
#findmatch(c,d)

def testloops(x,y):
	for letter in x:
		if (letter == 'a'):
			print "Just ", letter
		else:
			for number in y:
				if (number == 1):
					print number
				else:
					print "%s and %s" %(letter, number)

testloops(e, a)
