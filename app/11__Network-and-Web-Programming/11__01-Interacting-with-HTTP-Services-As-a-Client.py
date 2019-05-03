# PROBLEM:  Need to access various services via HTTP as a client.  Interacting with a REST-based API
# SOLUTION: Use urllib.request module

# builtin modules
from urllib import request, parse
from http.client import HTTPConnection
# pypi module
import requests

# Base URL being accessed
get_url = 'http://httpbin.org/get'
post_url = "http://httpbin.org/post"

# Dictionary of query parameters
parms = {
  'name1' : 'value1',
  'name2' : 'value2'
}
# Extra headers
headers = {
  'user-agent' : 'none/ofyourbusiness',
  'Spam' : 'Eggs'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(get_url + '?' + querystring)
resp = u.read()
print('GET:\n', resp)

# Make a POST request and read the response
u = request.urlopen(post_url, querystring.encode('ascii'))
resp = u.read()
print('\nPOST:\n', resp)

# Make a request an read the response with extra headers
req = request.Request(post_url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()
print('\nHEADER:\n', resp)

# Decoded text returned by the request 
resp = requests.post(post_url, data=parms, headers=headers)
text = resp.text
print('\nPOST REQUEST:\n', text)

# login to pypi using basic auth
resp = requests.get('http://pypi.python.org/pypi?:action=login', auth=('user', 'password'))
text = resp.text
print('\nGET SIMPLE AUTH:\n', text)

# pass http cookies from rquest to the next
resp1 = requests.get(get_url)
text = resp1.text
print('\nGET COOKIE:\n', text)
resp2 = requests.get(get_url, cookies=resp1.cookies)
text = resp2.text
print('\GET AND PASS COOKIE:\n', text)

# Use request to upload content
files = { 'file': ('data.csv', open('data.csv', 'rb')) }
r = requests.post(post_url, files=files)
text = r.text
print('\POST FILE:\n', text)

# http.client module
c = HTTPConnection('www.python.org', 80)
c.request('HEAD', '/index.html')
resp = c.getresponse()
print('\nStatus:', resp.status)
for name, value in resp.getheaders():
  print(name, value)

# urllib authentication
auth = request.HTTPBasicAuthHandler()
auth.add_password('pypi','http://pypi.python.org','username','password')
opener = request.build_opener(auth)
r = request.Request('http://pypi.python.org/pypi?:action=login')
u = opener.open(r)
resp = u.read()

# JSON results
r = requests.get('http://httpbin.org/get?name=Dave&n=37', headers = { 'User-agent': 'goaway/1.0' })
resp = r.json
print(resp)
#print('\nJSON HEADERS:\n', resp['headers'])
#print('\nJSON ARGS:\n', resp['args'])