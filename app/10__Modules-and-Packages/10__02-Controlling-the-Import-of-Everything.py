# PROBLEM:  Want precise control over symbols that are exported from a module or package 
#           when using 'from module import *' statement
# SOLUTION: define variable __all__ in module that explicitly lists export names
#           if all is an empty string nothing will be imported

from somemodule import *

# imported funcs in __all__ statement
spam()
grok()