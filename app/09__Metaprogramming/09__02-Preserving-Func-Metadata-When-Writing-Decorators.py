# PROBLEM:  Loose importatn metadata (name, doc string, annotation, and calling signature) with decorator
# SOLUTION: Apply @wraps decorator from functools library to underlying wrapper func

import time
from functools import wraps
from inspect import signature

def timethis(func):
  '''
  Decorator that reports the execution time.
  '''
  print("In timethis")
  # makes wrapped func available to you in the __wrapped__ attribute
  @wraps(func)
  def wrapper(*args, **kwargs):
    print("In wrapper")
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__, end-start)
    return result
  return wrapper

@timethis
def countdown(n:int):
  '''
  Counts down
  '''
  print("In countdown()")
  while n > 0:
    n -= 1

countdown(100000)
print(countdown.__name__)        # w/o wraps: 'wrapper
print(countdown.__doc__)         # w/o doc: ''
print(countdown.__annotations__) # w/o annotations: {}

# access __wrapped__ attribute directly
print(countdown.__wrapped__(100000))
print(signature(countdown))