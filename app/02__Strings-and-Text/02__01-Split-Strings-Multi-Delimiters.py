# PROBLEM:  Need to split a string into fields, but deliminters aren't consistent
# SOLUTION: Use split() for simple patterns or re.split() for complex patterns

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'
# re.split()
#   Can specifiy multiple patterns to match with
#   Output is same as split()
output = re.split(r'[;,\s]\s*', line)
print(output)
fields = re.split(r'(;|,|\s)\s*', line) # capture delimiters with text
print(fields)
values = fields[::2] # parse values from list
print(values)
deliminters = fields[1::2] + [""] # parse deliminaters from list
print(deliminters)