# PROBLEM:  Write a func that accepts any number of input args
# SOLUTION: Use * arg

import html

# *rest arg creates a tuple of extra positional args
def avg(first, *rest):
  return(first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))

# ** arg accepts any number of keyword args
#   **attrs is a dict that holds the passed keyword arg(if any)
def make_element(name, value, **attrs):
  keyvals = [' %s="%s"' % item for item in attrs.items()]
  attr_str = ''.join(keyvals)
  element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
  return element
print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))

# can combine positional *args and keword **args
def anyargs(*args, **kwargs):
  print(args)   # tuple
  print(kwargs) # dict
print(anyargs(1,2,3,4, test1=1, test2=2))