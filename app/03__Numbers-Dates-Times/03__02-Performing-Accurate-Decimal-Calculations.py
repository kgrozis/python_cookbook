# PROBLEM:  Perform accurate calcs with decimal numbers and don't want inaccuracies of floats
# SOLUTION: Use decimal module
#           Common application is accounting.  For rest float is fine

from decimal import Decimal, localcontext
import math

# inaccurate float arithematic
a = 4.2
b = 2.1

print(a + b)          # 6.300000000000001
print((a + b) == 6.3) # False

# accurate arithematic with decimal mod
#   performance impact
#   must specify decimals as strings
c = Decimal('4.2')
d = Decimal('2.1')

print(c + d)          # 6.3
print((c + d) == 6.3) # True

# localcontect()
e = Decimal('1.3')
f = Decimal('1.7')

with localcontext() as ctx:
  # control precision in with statement
  ctx.prec = 3
  print(e / f)
with localcontext() as ctx:
  # control precision in with statement
  ctx.prec = 50
  print(e / f)
print(e / f)

# subtractive cancelation, errors propagate with large number in floats
#   one disappears
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# more accurate version of sum
print(math.fsum(nums))