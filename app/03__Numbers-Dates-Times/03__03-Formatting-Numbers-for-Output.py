# PROBLEM:  Need to format a number for output, controlling digits, alignment,
#           inclusion of a thousands separator, and other details
# SOLUTION: Use builtin format() function or .format() string method 
#           General form is '[<>^]?width[,]?(.digits)?'
#           width and digits are integers and ? is optional parts
#           Can be used for numbers in decimal module too
#           When digits are restricted round() module is used 

x = 1234.56789

# format() function:
#   2 decimals places
print(format(x, '0.2f'))
#   right justify in 10 chars and 1 deciaml place
print(format(x, '>10.1f'))
#   left justify in 10 chars and 1 decimal place
print(format(x, '<10.1f'))
#   Center justify in 10 chars and 1 decimal place
print(format(x, '^10.1f'))
#   Include thousands separator and 1 decimal place
print(format(x, '0,.1f'))
#   exponential notation
print(format(x, 'e'))
#   exponential notation and 2 deciaml places
print(format(x, '0.2E'))
#   negative number
print(format(-x, '0.1f'))
#   swap chars using translate()
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))

# .format() string method:
print('The value is {:0,.2f}'.format(x))

# formatting using modulus operator:
#   2 decimal places
print('%0.2f' % x)
#   right justify in 10 chars and 1 deciaml place
print('%10.1f' % x)
#   left justify in 10 chars and 1 deciaml place
print('%-10.1f' % x)