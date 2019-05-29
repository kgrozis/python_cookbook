# module mypackage.A.spam wants to import the module grok located in the same dir
# using relative import for same dir
from ..B import bar
from . import grok

testA()