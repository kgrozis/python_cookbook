# PROBLEM:  Want a function to only accept certain args by keywords
# SOLUTION: Put keyword args after a * arg or a single unnamed *
#           keyword specify greater clarity for optional args

# keyword args enforce code clarity
def recv(maxsize, *, block=False):
  'Receives a message'
  pass
# builtin help func
print(help(recv))

# recv(1024, True)       # type error
recv(1024, block=True) # OK

def mininum(*values, clip=None):
  m = min(values)
  if clip is not None:
    m = clip if clip > m else m
  return m 
print(mininum(1, 5, 2, -5, 10))         # -5
print(mininum(1, 5, 2, -5, 10, clip=0)) # 0