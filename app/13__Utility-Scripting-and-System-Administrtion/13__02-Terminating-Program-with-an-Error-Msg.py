# PROBLEM:  Want program to terminate by printing a msg to stderr and return nonzero status code
# SOLUTION: Raise a SystemExit exception and supply th eerror ms as an arg

import sys

# Send message to StdErr
sys.stderr.write('It failed\n')
# Exit with non-zero
raise SystemExit(1)