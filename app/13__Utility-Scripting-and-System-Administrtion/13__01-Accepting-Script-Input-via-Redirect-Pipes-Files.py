#!/usr/bin/python3

# PROBLEM:  Want script to accept input using:
#   pipe output from a cmd into script,
#   redirect a file into script
#   pass a filenae or list filenames
# SOLUTION: Use builtin fileinput module

import fileinput

with fileinput.input() as f:
  for line in f:
    # fileinput helper methods: filename(), lineno()
    print(f.filename(), f.lineno(), line, end='')
