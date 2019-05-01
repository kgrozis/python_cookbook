# PROBLEM:  Want to organize code into a pkg consisting of a hierarchical collection of modules
# SOLUTION: Define an __init__.py file in each directory

from formats import jpg
from formats import png
from primitive import fill
from primitive import line
from primitive import text

jpg.print_jpg()