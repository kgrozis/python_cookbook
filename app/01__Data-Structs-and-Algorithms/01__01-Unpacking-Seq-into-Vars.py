# PROBLEM:  Have a tuple or seq and would like to unpack into a collection vars
# SOLUTION: Use a simple assignment operator
#           Cannot have a mismatch of number o elements or you'll get an error
#           Can upack any iterable also including: strings: files, iterators, generators, strings
p = (4, 5)  # tuple data structure
x, y = p  # unpacking using assignment operator
print("X = %s" % x)
print("y = %s" % y)

data = ["ACME", 50, 91.1, (2012, 12, 21)]  # List data structure
name, shares, price, date = data  # unpacking using assignment operator
print("name = %s" % name)
print("date =", date)
name, shares, price, (year, mon, day) = data  # unpacking list and nested tuple
print("name = %s" % name)
print("year = %s | mon = %s | day = %s" % (year, mon, day))
_, shares, price, _ = data  # no way to discard values; use throwaway var ('_')
print("Shares = %s, Price = %s" % (shares, price))

s = "hello"
a, b, c, d, e = s
print(a, b, e)  # h e o
