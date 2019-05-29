# PROBLEM:  Want to make objects support context-management protocol ('with' statement)
# SOLUTION: Need to implement __enter__() and __exit__() methods
#           Used commonly with managing files, net connections, and locks
#           Used when must explicitly release resources

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

# represents a network connection (doen't do anything)
class LazyConnection:
  def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
    self.address = address
    self.family = family
    self.type = type
    self.sock = None
  # establish connection
  def __enter__(self):
    print('>>> opening connection....')
    if self.sock is not None:
      raise RuntimeError('Already connected')
    self.sock = socket(self.family, self.type)
    self.sock.connect(self.address)
    return self.sock
  # closs connection
  def __exit__(self, exc_ty, exc_val, tb):
    print('>>> closing connection...')
    self.sock.close()
    self.sock = None

conn = LazyConnection(('www.python.org', 80))
# connection closed
with conn as s:
  # conn.__enter__() executes: connection open
  s.send(b'GET /index.html HTTP/1.0\r\n')
  s.send(b'Host: www.python.org\r\n')
  s.send(b'\r\n')
  resp = b''.join(iter(partial(s.recv, 8192), b''))
  # conn.__exit__() executes: connection closed