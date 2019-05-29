# PROBLEM:  Want simpler way to format strings
# SOLUTION: Use f-strings
#           f-strings can use f or F to prefix string
#           syntax: f ' <text> { <expression> <optional !s, !r, or !a> <optional : format specifier> } <text> ... '


import datetime

user = "Jane Doe"
action = "buy"

name = "Fred"
age = 50
anniversary = datetime.date(1991, 10, 12)

# format()
log_message = "User {} has logged in and did an action {}.".format(user, action)
print(log_message)

# f-strings
print(f"User {user} has logged in and did an action {action}.")
print(f"My name is {name}, my ae next year is {age+1} my anniversay is {anniversary:%A, %B %d, %Y}")
print(f"He said his name is {name!r}")

# use f-strings to convert a numeric to string
value = 1234
print(f'input={value:#06x}')

# escape sequences, cannot use backslashes ('\')
print(f'{"quoted string"}')
# literal brace ('{}')
print(f'{{ {4*10} }}')
