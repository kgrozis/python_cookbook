# PROBLEM:  Want to implement a server that communicates with clients using the UDP/IP 
# SOLUTION: Use socketserver library

from socketserver import BaseRequestHandler, UDPServer
import time 

class TimeHandler(BaseRequestHandler):
  def handle(self):
    print(f'Got connection from {self.client_address}')
    # Get message and client socket
    msg, sock = self.request
    resp = time.ctime()
    sock.sendto(resp.encoe('ascii'), self.client_address)

if __name__ == '__main__':
  serv = UDPServer(('', 20000), TimeHandler)
  serv.serve_forever