#testing the argparse module, which allows for optional parameters and arguments to be passed to python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="increase output verbosity",
		                    action="store_true")
args = parser.parse_args()
if args.v:
	   print "verbosity turned on"
