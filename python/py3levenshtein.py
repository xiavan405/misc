#!/bin/python2 

a=input("Reference= ")
b=input("String to compare= ")

def levenshtein(seq1, seq2):
	oneago = None
	thisrow = list(range(1, len(seq2) + 1)) + [0]
	for x in list(range(len(seq1))):
		twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
		for y in range(len(seq2)):
			delcost = oneago[y] + 1
			addcost = thisrow[y - 1] + 1
			subcost = oneago[y - 1] + (seq1[x] != seq2[y])
			thisrow[y] = min(delcost, addcost, subcost)
	return thisrow[len(seq2) - 1]


#a = "AAATAAATAACTAAAT"
#b = "AAATAAATAAATAAAT"
print(levenshtein(a, b))
