# PROBLEM:  Change output produced by printing or viewing instances
# SOLUTION: Define __str__() and __repr__() methods

# __repr__(): returns the code representation of an instance; returns text
# __str__():  converts the instance to a string
class Pair:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)
  def __str__(self):
    return '({0.x!r}, {0.y!r})'.format(self)

p = Pair(3, 4)
p # __repr__() output
print(p) # __str__() output
print('p is {0!r}'.format(p)) # !r formatting code indicates output __repr__()
print('p is {0}'.format(p))

# best practice define both __repr__() and __str__() simplifies debugging

# alternative with modulus
class Pair:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)
  def __str__(self):
    return '(%s, %s)' % (self.x, self.y)

p = Pair(3, 4)
p # __repr__() output
print(p) # __str__() output
print('p is {0!r}'.format(p)) # !r formatting code indicates output __repr__()
print('p is {0}'.format(p))