# PROBLEM:  Want to attach additional info to func args to let others know more about 
#           how a func is supposed to be used
# SOLUTION: Use func arg annotations to give programmers hints about how a func is
#           supposed to be used

# interpreter doesn't attach any semantic meaning to annotations
#   annotations are not type checks
#   make code more readable and appear in documentation
def add(x:int, y:int) -> int:
  return x + y

print(help(add))

# Send floats to add | no type check
print(add(5.1, 2.5))
# Send strings to add | no type check
print(add('hello', ' world'))

# Function annotations stored in func __annotation__ attribute
print(add.__annotations__)