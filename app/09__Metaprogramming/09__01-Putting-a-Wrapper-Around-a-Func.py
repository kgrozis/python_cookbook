# PROBLEM:  Want wrapper layer around a func that adds extra processing
# SOLUTION: Define a decorator func

import time
from functools import wraps

def timethis(func):
  '''
  Decorator that reports the execution time. 
  '''
  print('>>> In timethis...')
  @wraps(func)
  # typical for wrapper func to accept (*args, **kwargs)
  #   makes sure args will be accepted
  # place 'extra' code to exe in wrapper func()
  def wrapper(*args, **kwargs):
    print('>>> In wrapper...')
    start = time.time()
    # return value is always func(*args, **kwargs)
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__, end-start)
    return result

  return wrapper

@timethis
def countdown(n):
  '''
  Counts down
  '''
  print('>>> In countdown...')
  while n > 0:
    n -= 1

countdown(100000)
countdown(1000000)