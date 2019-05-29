# PROBLEM:  Want a custom iteration patterns that's different than the usual builtin
#           functions (range(), reversed(), etc...
# SOLUTION: Define a generator function

# produce a frange of floating-point numbers
def frange(start, stop, increment):
  x = start
  while x < stop:
# yield statement turns funtion into generator
# will only run in response to iteration
    yield x
    x += increment 
# iterate over funtion using a for loop or use it with some other function that 
#   consumes an iterable (sum(), list(),...)
for n in frange(0, 4, 0.5):
  print(n)
print(list(frange(0,1,0.125)))

def countdown(n):
  print('Starting to count from', n)
  while n > 0:
    yield n 
    n -= 1
  print('Done!')

# Create generator object
c = countdown(3)
print(c)
# iterator func only runs in response to next() function
print(next(c))
print(next(c))
print(next(c))
print(next(c)) # raises StopIteration exception