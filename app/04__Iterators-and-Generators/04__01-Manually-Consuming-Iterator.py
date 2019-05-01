# PROBLEM:  Want to iterate without using for loop
# SOLUTION: Manually consume an iterable with next()

with open('/etc/passwd') as f:
  try:
    while True:
      line = next(f)
      print(line, end='')
  except StopIteration: # Signals end of iteration
    pass

# Could also signal end of iteration with none:
# if line is None:
#   break

items = [1, 2, 3]
it = iter(items) # Invokes items.__iter__()
print(next(it))  # Invokes it.__next__()
print(next(it))
print(next(it))
print(next(it))  # creates exception: StopIteration
