#testing the argparse module, which allows for optional parameters and arguments to be passed to python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo
