# PROBLEM:  Code organized in package and want to import a submodule from one o the other pkg
#           submodules without hardcoding the package name into the import statement
# SOLUTION: Use pkg-relative import

# Absolete path
from mypackage.A import grok

print(dir(grok))
grok.testA()