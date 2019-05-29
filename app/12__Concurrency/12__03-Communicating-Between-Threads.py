# PROBLEM:  Have multi-threads in program and want to safely communicate or exchange data between them
# SOLUTION: Use Queue in queue library and create a Queue instance that is shared by threads
#           and use put() and get() operations to add or remove item from queue
#           Locking is builtin so can share between as many queues as possible

from queue import Queue
from threading import Thread, Event
import datetime

# Object that signals shutdown
_sentinel = object()

running = True

# A thread that produces data
def producer(out_q, running):
  run_counter = 0
  while running:
    # Produce data
    data = datetime.datetime.now()
    out_q.put(data)
    run_counter += 1
    if run_counter > 100:
      running = False
  # Put the sentinel on the queue to indicate completion
  out_q.put(_sentinel)

# A thread that consumes data
def consumer(in_q):
  while True:
    # Get data 
    data = in_q.get()
    # Check for termination
    if data is _sentinel:
      in_q.put(_sentinel)
      break
    # Process data
    print(f"data: {data}")

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,running))
t1.start()
t2.start()

# Thread needs to know immediately when a consumer thead has processed item of data
# Pair the sent data with an Event object, allows the producer to monitor progress
def producer2(out_q):
  while running:
    data = datetime.datetime.now()
    # Make (data, event) pair and hand it to the consumer
    evt = Event()
    out_q.put(data, evt)
    # Wait for the consumer to process the item
    evt.wait()

def consumer2(in_q):
  while True:
    data, evt = in_q.get()
    print(f"data2: {data}")
    # Indicate completion
    evt.set()

running = True
q2 = Queue()
t2_1 = Thread(target=consumer2, args=(q2,))
t2_2 = Thread(target=producer2, args=(q2,running))
t2_1.start()
t2_2.start()