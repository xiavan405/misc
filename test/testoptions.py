#!/bin/env python

import argparse

#properly utilize optional and positonal arguments, as well as a help statement. 
#nargs is just to allow multiple values to be passed under one argument flag

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)
