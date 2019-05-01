# PROBLEM:  Want to read or write a CSV file
# SOLUTION: Use CSV library

import csv
from collections import namedtuple
import re

# Read CSV:
#   Read data as a seq of tuples
with open('stocks.csv') as f:
  f_csv = csv.reader(f)
  headings = next(f_csv)
  Row = namedtuple('Row', headings)
  for r in f_csv:
    row = Row(*r)
    print(row.Symbol, row.Change)

# read data as seq of dicts
with open('stocks.csv') as f:
  f_csv = csv.DictReader(f)
  for row in f_csv:
    print(row["Symbol"], row["Change"])

# read tab-seperated values
with open("stocks.tsv") as f:
  f_tsv = csv.reader(f, delimiter='\t')
  for row in f_tsv:
    print(row)

# may have an invalid char in csv file.  need to identify chars and scrub
#   use reegex sub for nonvalid chars
with open('stock.csv') as f:
  f_csv = csv.reader(f)
  headers = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ]
  Row = namedtuple('Row', headers)
  for r in f_csv:
    row = Row(*r)
    print(row)

# csv interprets all values as strings
#   must conversions for any type other than string
col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)
  for row in f_csv:
    row = tuple(convert(value) for convert, value in zip(col_types, row))
    print(row)
# alternative typing
print('Reading as dicts with type conversion')
field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]
with open('stocks.csv') as f:
  for row in csv.DictReader(f):
    row.update((key, conversion(row[key])) for key, conversion in field_types)
    print(row)


# Write CSV
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]
with open("stocks.csv", "w") as f:
  f_csv = csv.writer(f)
  f_csv.writerow(headers)
  f_csv.writerows(rows)

# Write a seq of dicts as CSV
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007','Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007','Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007','Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
with open("stocks.csv", "w") as f:
  f_csv = csv.DictWriter(f, headers)
  f_csv.writeheader()
  f_csv.writerows(rows)