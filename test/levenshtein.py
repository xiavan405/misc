#!/bin/python2

print "Please enter a reference string."
reference=raw_input("> ")
print "Please enter the string you wish to compare."
string=raw_input("> ")

#reference="kitten"
#string="sitting"

#find string difference and convert string 2 into string one moving letter by letter.

def levenshtein(refpos, stringpos, count):
	ref_index_range=len(reference)-1
	str_index_range=len(string)-1
	if (stringpos > str_index_range) and (refpos > ref_index_range):
		print count
		exit()
	if (stringpos > str_index_range):
		count += 1
		levenshtein(refpos+1, stringpos+1, count)
	if (refpos > ref_index_range):
		count += 1
		levenshtein(refpos+1, stringpos+1, count)
	if (reference[refpos]==string[stringpos]):
		levenshtein(refpos+1, stringpos+1, count)
	else:
		count += 1
		levenshtein(refpos+1, stringpos+1, count)

levenshtein(0,0,0)
