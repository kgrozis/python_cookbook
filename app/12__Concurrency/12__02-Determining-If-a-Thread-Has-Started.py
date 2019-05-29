# PROBLEM:  Want to know when thread start running
#           Threads execute independently and nondeterministically.  Presents a problem if other
#           other threads in the program need to know if a thread has reached a certain point in 
#           execution
# SOLUTION: Use Event object from threading library. 
#           Event instances are similar to a sticky flag that allows thread to wait for something
#           to happen.
#           Events initally set to 0.  If event is unset and thread waits on the event , it will 
#           block or go to sleep until a set.  Threads that sets an event will waake up all of 
#           threads waiting 
#           Event objects are best used for one-time events and then discarded.  Reseting an
#           event can lead to unexpected behavior
#           If thead is going to repeatedly signal an event use Condition object

from threading import Thread, Event, Condition, Semaphore
import time 

# Execute in an independent thread
def countdown(n, started_evt):
  print('Countdown starting')
  started_evt.set()
  while n > 0:
    print('T-minus', n)
    n -= 1
    time.sleep(1)

# Create event object to signal startup
started_evt = Event()

# Launch thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for thread to start
started_evt.wait()
# appears after 'Launching countdown'
print('Countdown is running')

# Condition Object
class PeriodicTimer:
  def __init__(self, interval):
    self._interval = interval
    self._flag = 0
    self._cv = Condition()
  def start(self):
    t = Thread(target=self.run)
    t.daemon = True
    t.start()
  def run(self):
    ''' Run timer and notify wawiting threads after each interval
    '''
    while True:
      time.sleep(self._interval)
      with self._cv:
        self._flag ^= 1
        self._cv.notify_all()
  def wait_for_tick(self):
    ''' Wait for the next tick of the timer
    '''
    with self._cv:
      last_flag = self._flag
      while last_flag == self._flag:
        self._cv.wait()

# Condition() example
print('/nStart Conditional Example')
ptimer = PeriodicTimer(1)
ptimer.start()

# two threads that synchronize on the timer
def pcountdown(nticks):
  while nticks > 0:
    ptimer.wait_for_tick()
    print('pT-minus', nticks)
    nticks -= 1

def pcountup(last):
  n = 0
  while n < last:
    ptimer.wait_for_tick()
    print('Counting', n)
    n += 1

Thread(target=pcountdown, args=(10,)).start()
Thread(target=pcountup, args=(20,)).start()

# Event objects wake all waiting threads
# Want to wake a single thread use Semaphore or Condition object

# worker thread
def worker(n, sema):
  # wait to be signaled
  sema.acquire()
  # do work
  print('working', n)

# create threads
sema = Semaphore(0)
nworkers = 10
for n in range(nworkers):
  t = Thread(target=worker, args=(n, sema,))
  t.start()

# pool of threads started.  Threads are all blocked waiting to acquire semaphore
# When semaphore is released, one worker will wake up and run
sema.release()
sema.release()