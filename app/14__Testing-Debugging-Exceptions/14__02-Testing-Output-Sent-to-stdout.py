# PROBLEM:  Writing unit tests and need to apply patches to select objects in order to make 
#           assertions about how they were used in the test
# SOLUTION: Use unitest.mock.patch() func.  Patch can be used as a decorator, context manager
#           or stand-alone

from unittest.mock import patch
import example

@patch('example.func')
def test1(x, mock_func):
  example.func(x) # Uses patched example.func
  mock_func.assert_called_with(x)