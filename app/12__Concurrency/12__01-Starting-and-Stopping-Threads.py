# PROBLEM:  Want to create and destroy threads for concurrent execution of code
# SOLUTION: Threading library can be used to execute any Python callable in its thread

import time
import multiprocessing
# Create and launch a thread
from threading import Thread

# no operations to terminate a thread, signal, adjust scheduling, or perform any high-level operations
#   need to build operations for yourself
class CountdownTask:
  def __init__(self):
    self._running = True
  def terminate(self):
    self._running = False
  def run(self, n):
    while self._running and n > 0:
      print('CountdownTask: T-minus', n)
      n -= 1
      time.sleep(2)

# Polling for thread termination if tricky with bokcing operations like I/O
#   If thread is blocked it may never check to see if it's been killed
#   Use timeout loops
class IOTask:
  def terminate(self):
    self._running = False
  def run(self, sock):
    #sock is a socket
    sock.settimeout(5) # set timeout period
    while self._running:
      # Perform a blocking I/O opertaion w/timeout
      try:
        data = sock.resv(8192)
        break
      except sock.timeout:
        continue
      # continued processing
    # terminatd
    return

# Threads are limited to 1 thread execution at a time in interpretor
#   don't use threads for parallelism
#   use threads for I/O (files, dbs), concurrentism
# Thread defined via inheritance from Thread class
class CountdownThread(Thread):
  def __init__(self, n):
    super().__init__()
    self.n = n
  def run(self):
    while self.n > 0:
      print('CountdownThread: T-minus', self.n)
      self.n -= 1
      time.sleep(2)

def countdown(n):
  while n > 0:
    print('T-minus', n)
    n -= 1
    time.sleep(2)

# Create thread
t = Thread(target=countdown, args=(10,), daemon=True)
# Make thread a daemon, but they can't be joined
#t = Thread(target=countdown, args=(10,), daemon=True)
# Start thread
t.start()

# threads execute in their own system-level thread and managed by host OS
# query to verify thread is alive
if t.is_alive():
  print('still running')
else:
  print('completed')

# request to join a thread and wait for it to finish
t.join()

c =  CountdownTask()
t2 = Thread(target=c.run, args=(10,))
t2.start()
time.sleep(2)
c.terminate() # signal termination
#t2.join()     # wait for actual termination

c2 = CountdownThread(5)
c2.start()

c3 = CountdownTask()
p = multiprocessing.Process(target=c3.run, args=(5,))
