# PROBLEM:  Want to output data using print(), but want to change the separator
#           char or line ending
# SOLUTion; Use sep and end keyword arguments to print()

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

# suppress newline char
for i in range(5):
  print(i)
for i in range(5):
  print(i, end=' ')

# use join to accomplish same thing
print(','.join('ACME','50','91.5'))