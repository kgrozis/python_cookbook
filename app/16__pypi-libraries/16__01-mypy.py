# PROBLEM:  Python is dynamically typed langaue.  Want to know what types are expected
# SOLUTION: mypy - python linter for typing

from typing import Dict, List, Mapping,Sequence

def add_one(input: int) -> int:
  return input + 1

def print_seven() -> None:
  # Incorrect string.  Should be an integer.  
  # mypy will uncover error
  # fix is 'five = 5'
  five = "5"
  seven = add_one(add_one(five))
  print(seven)

print(add_one(2))
print_seven()