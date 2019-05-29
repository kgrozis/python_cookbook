# PROBLEM: Want to write a program that parses options supplied on th command line
# SOLUTION: Use argparse module

import argparse

# create instance of ArgumentParser for parsing CLI
parser = argparse.ArgumentParser(description='Search Files')

# add declarations for options you want to support
# dest arg: specifies the name of an attribute where the result of parsing will be placed
# metvar arg: generates help messages
# action arg: specifies processing associated with arg
#
# collects all the extra CLI args into a list
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
# required flag means arg must be supplied at least once
# can use either -p, --pat
parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                  dest='patterns', action='append',
                  help='text pattern to search for')
# sets boolean flag depending on whether or not arg was provided
parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')
# akes a single value and stores it as a string
parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')
# arg takes a value that must match the set of choices
parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='search speed')

# process sys.argv value 
# results are placed into an attribute with name given in dest arg
args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)