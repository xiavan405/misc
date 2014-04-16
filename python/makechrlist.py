#!/bin/python2

file = open('/home/xiavan/Tools/lobSTR/resources/lobstr_v2.0.3_hg19_strinfo.tab','r')
count = 1
#chrom = 1
#list = ['chr1','chr10','chr11','chr11','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chr23']
#this is completely borked, rewrite tomorrow, dont try to make sense of it its dumb

current_chr = " "
chrlist = []
for line in file:
	splitline = line.split("\t")
	if current_chr == splitline[0]:
		pass
	else:
		current_chr = splitline[0]
		if current_chr == "chrom":
			pass
		else:
			curr_list =[current_chr]
			chrlist = chrlist + curr_list
			print "Found %s" %current_chr
			if current_chr == "chrY":
				break

print chrlist

#for entry in chrlist:
#for line in file:
#	print line
#	count += 1
#	print count
#                line_list = line.split("\t")
#                if entry == line_list[0]:
 #                       print "Found first instance of %s" %entry
  #                      print "The current count is %s" %count
   #                     count = 0
#			break
  #              else:
#			pass
 #                       #print "%s versus %s on line %s" %(entry, line_list[0], count)
#	print "Completing run for %s, moving on to the next chromosome." %entry
###
