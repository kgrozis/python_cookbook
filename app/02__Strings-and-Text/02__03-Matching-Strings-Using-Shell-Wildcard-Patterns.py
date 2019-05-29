# PROBLEM:  Want to match text using same wildcard patterns common to Unix shells
# SOLUTION: Use fnmatch module and funcs fnmatch() and fnmatchcase()
#           fnmatch uses underlying OS case matching criteria (MacOS is case sensitive)

from fnmatch import fnmatch, fnmatchcase 

# match global wildcard (*)
print(fnmatch('foo.txt', '*.txt'))
# match single char wildcard (?)
print(fnmatch('foo.txt', '?oo.txt'))
# match numeric wildcard ([0-9]) and global wildcard
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

# list comprehension match
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
# match Dat1.csv, Dat2.csv
print([name for name in names if fnmatch(name, 'Dat*.csv')]) 

# match on case
print(fnmatchcase('foo.txt', '*.TXT'))   # False
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
# list comprehension case match
print([addr for addr in addresses if fnmatchcase(addr, "* ST")])