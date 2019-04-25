# PROBLEM:  Round float to fixed number of decimal places
# SOLUTION: Simple rounding use builtin round(value, ndigit)
#           negative rounding will round to left of decimal point

print(round(1.23, 1)) # round down, 1.2
print(round(1.27, 1)) # round up, 1.3

a = 1627731
print(round(a, -1)) # 1627730
print(round(a, -2)) # 1627700
print(round(a, -3)) # 1628000

# Outputting use format()
x = 1.23456
print(format(x, '0.2f'))            # 1.23
print(format(x, '0.3f'))            # 1.235
print("value is {:0.3f}".format(x)) # value is 1.235

# Don't round numbers to fix float accuracy problems
a = 2.1
b = 4.2
c = a + b
print("c = %s" % c) # c = 6.300000000000001