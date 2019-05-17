# PROBLEM:  Want limited history of last few items seen during itertaion or during
#           some other kind of processing
# SOLUTION: Use collections.deque

# simple text match on a seq of lines and yields the matching line along with the 
#   previous N lines of context when found
from collections import deque

def search(lines, pattern, history=5):
  # create a fixed queue 
  # when queue exceeds length, oldest item deleted
  # queue depth equals history or default 5
  # deque handles list add and pop operations and runs faster
  previous_lines = deque(maxlen=history)
  for line in lines:
    if pattern in line:
      # generator func - decouples process of searching from the code that uses results
      yield line, previous_lines
    # add to queue, delete queue item if > 5
    previous_lines.append(line)

# example use on a file
if __name__ == '__main__':
  with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
      for pline in prevlines:
        print(pline, end='')
      print(line, end='')
      print('-'*20)