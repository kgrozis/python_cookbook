# PROBLEM:  Need to read or write text data
# SOLUTION: Use open() with rt for read, wt to write file (overwrite an existing file), and at to append file

# Read entire file as a string
with open('somefile.txt', 'rt') as f:
  data = f.read()
  print(data)

# Iterate over the lines of the file
with open('somefile.txt', 'rt') as f:
  for line in f:
    print(line)

# write chunks of text data
with open('somefile.txt', 'wt') as f:
  f.write('this is')
  f.write('a text')

# redirect print statement
with open('somefile.txt', 'wt') as f:
  print('this is', file=f)
  print('a text', file=f)

# append
with open('somefile.txt', 'at') as f:
  f.write('file')

# default text is found with sys.getdefaultencoding().
#   Most machines support utf-8
#   can use encoding to explicitly define encoding
with open('somefile.txt', 'rt', encoding='latin-1') as f:
  data = f.read()
  print(data)

# with statement establishes context which file will be used.  
#   When control leaves the with block the file automatically closes
#   If you don't use with statment must close file 
f = open('somefile.txt', 'rt')
data = f.read()
print(data)
f.close()

# By default, Python operates in universal newline mode.  
#   Recognizes both windows ('\r\n') and unix ('\n')
#   Stop the translation with newline='' argument in open()
with open('hello.txt', 'rt', newline='') as f:
  data = f.read()
  print(data)

# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
data = f.read()
print(data)
f.close()

# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
data = f.read()
print(data)
f.close()