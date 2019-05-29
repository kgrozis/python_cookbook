# PROBLEM:  Want to implement a server that communicates with clients uing TCP/IP
# SOLUTION: Use socketserver library

# socketserver is single threaded and can only handle one request at a time
#  ForkingTCPServer or ThreadingTCPServer allow for multi-threading
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
  def handle(self):
    print('Got connection from', self.client_address)
    while True:
      msg = self.request.recv(8192)
      if not msg:
        break
      self.request.send(msg)

if __name__ == '__main__':
  serv = TCPServer(('', 20000), EchoHandler)
  serv.serve_forever()