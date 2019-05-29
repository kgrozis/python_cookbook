# PROBLEM:  Want to undo a decortor applied to a function and gain access to orginal 
#           wrapped func
# SOLUTION: Use __wrapped__ attribute to gain access

from functools import wraps

def decorator1(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('Decorator 1')
    return func(*args, **kwargs)
  return wrapper

def decorator2(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('Decorator 2')
    return func(*args, **kwargs)
  return wrapper

@decorator1
@decorator2
def add(x, y):
  return x + y

print(add(2, 3))
print(add.__wrapped__(2, 3))