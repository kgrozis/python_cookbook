# PROBLEM:  Want to read or write data encoded as JSON
# SOLUTION: Use json.dumps() and json.loads() module to encode and decode data in JSON 
#           Supports basic types None, bool, int, float, str, list, dict
#           Dict keys are autoconverted into strings

from urllib.request import urlopen
import json
from pprint import pprint
from collections import OrderedDict

# Turn Python data structure into JSON
data = {
  'name' : 'ACME',
  'shares' : 100,
  'price' : 542.23
}

json_str = json.dumps(data)
print('JSON: %s' % json_str)

# Turn JSON string back to Python data
data = json.loads(json_str)
print('Python: %s' % data)

# Writing JSON data
with open('data.json', 'w') as f:
  json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
  data = json.load(f)
  print('File: %s' % data)

# boolean translation into JSON
print(json.dumps(False)) # 'false'
print(json.dumps(True))  # 'true'
print(json.dumps(None))  # 'null'

# standard json module encodes nested values without any structure ('/n')
# u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
# resp = json.loads(u.read().decode('utf-8'))
# pprint(resp)

# decode json and keep it's ordered
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# turn JSON dict into a python object
class JSONObject:
  def __init__(self, d):
    self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)

# Use indent option to format JSON 
data = {
  'price' : 542.23,
  'name' : 'ACME',
  'shares' : 100
}
print(json.dumps(data))                 # Nested JSON output
print(json.dumps(data, indent=4))       # Indented JSON ooutput
print(json.dumps(data, sort_keys=True)) # Sort keys in JSON output

# serialize an instance as JSON
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
# method to serialize
def serialize_instance(obj):
  d = {'__classname__' : type(obj).__name__}
  d.update(vars(obj))
  return d
# create object
p = Point(2, 3)
# object as json
print(json.dumps(serialize_instance(p)))

# unserialize an instance
classes = {
  'Point' : Point
}
'''
def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d
'''
p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)
# a = json.load(s, object_hook=unserialize_object)
# print(a)