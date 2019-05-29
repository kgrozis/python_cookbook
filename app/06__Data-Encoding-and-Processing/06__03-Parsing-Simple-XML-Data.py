# PROBLEM:  Want to extract data from a XML doc
# SOLUTION: Use xml.etree.ElementTree module to extract data

from urllib.request import urlopen
from xml.etree.ElementTree import parse 

# Download RSS feed and parse
u = urlopen('http://planet.python.org/rss20.xml')
# parse() parses entire XML doc into a doc obj
doc = parse(u)

# extract & output tags of interest
for item in doc.iterfind('channel/item'):
  title = item.findtext('title')
  date = item.findtext('pubDate')
  link = item.findtext('link')
  print('TITLE: %s \n DATE: %s \n LINK: %s\n-------------------' % (title, date, link))

u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
# find operation takes place relative to a starting elemtn
e = doc.find('channel/title')
print(e)
# return name of xml tag
print(e.tag)
# return leaf's text
print(e.text)
# extract attributes
print(e.get('some_attribute'))