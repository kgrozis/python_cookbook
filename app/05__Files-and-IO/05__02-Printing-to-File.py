# PROBLEM:  Want to redirect the output of print() to a file
# SOLUTION: Use the file keyword argument to print()

with open('print2file.txt', 'wt') as f:
  print('hello world', file=f)
