# PROBLEM:  Need to check the start or end of a string for specific text patterns
# SOLUTION: Use str.startswith() or str.endswith()

import os
from urllib.request import urlopen

# check file
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))

# check url
url = 'http://www.python.org'
print(url.startswith('http'))

# use tuple for multiple choices
#   Must be tuple or will not work.  Will not work with lists
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h', '.py'))])
print(any(name.endswith('.py') for name in filenames))

choices = ['http:', 'ftp:']           # List
print(url.startswith(tuple(choices))) # convert list to tuple

# read url or file with same method
def read_data(names):
  if name.startwith(('http:', 'https:', 'ftp:')):
    return urlopen(name).read()
  else:
    with open(name) as f:
      return f.read()