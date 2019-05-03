# PROBLEM:  Need to unpack N elements from an iterable, but the iterble may be longer than elements
#           causing a "too many values to unpack"
# SOLUTION: Use "star expressions"

def drop_first_last(grades):
  # middle captures arbitrary number of middle number in list
  first, *middle, last = grades
  return avg(middle)

def avg(middle):
  i = 0
  grade_total = 0
  for grade in middle:
    i += 1
    grade_total += grade
  return grade_total/i

print(drop_first_last([1,10,10,19]))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# phone numbers captures arbitrary number of phone number in list
#   star expressions are returned as a list
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# star expression iterating over series of tuples
records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x, y):
  print('foo', x, y)
def do_bar(s):
  print('bar', s)
for tag, *args in records:
  if tag == 'foo':
    do_foo(*args)
  elif tag == 'bar':
    do_bar(*args)

# unpacking complex strings with split
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)   # nobodry
print(homedir) # /var/empty
print(sh)      # /usr/bin/false

# recursion
items = [1, 10, 7, 4, 5, 9]
def sum(items):
  head, *tail = items
  return head + sum(tail) if tail else head
print(sum(items))

