# PROBLEM:  os.path is clunky and awkward.  a lot of string-in-string-out funcs that creates
#           nested code.  os.path becomes hard to read.  Must read it inside out
#           os module has lots of utilities that aren't related to filesystems
# SOLUTION: object-oriented version of os.path.  Replaces utitlies with Path object

from pathlib import Path
from shutil import copyfile
from os import chdir

# write pwd
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# join leaf dir Test to path
TEST_DIR = BASE_DIR.joinpath('15__Test-Dir')
print(TEST_DIR)

# make directory
Path('/usr/src/app/15__Test-Dir/Original_Dir').mkdir(parents=True, exist_ok=True)
# rename directory
Path('/usr/src/app/15__Test-Dir/Original_Dir').rename('/usr/src/app/15__Test-Dir/Rename_Dir')

# Glob pattern matching
top_level_py_files = Path.cwd().glob('*.py')
for top_level_py_file in top_level_py_files:
  print(top_level_py_file)
all_py_files = Path.cwd().rglob('*.py')
for all_py_file in all_py_files:
  print(all_py_file)

# Read file
file_contents = [
  path.read_text()
  for path in Path.cwd().rglob('*.py')
]
print(file_contents)

# write file
path = Path("/usr/src/app/15__Test-Dir/test.py")
with path.open(mode='wt') as config:
  config.write('# config goes here')

# Pass Path object to builtin open() func
with open(path, mode='wt') as config:
  config.write('# more configs goes here')

# no equvilent of shutil.copyfile
source = Path("/usr/src/app/15__Test-Dir/test.py")
destination = Path("/usr/src/app/15__Test-Dir/copy.py")
copyfile(source, destination)

# no equvilent of os.chdir
parent = Path('..')
chdir(parent)

# Path has __str__
print(Path("/usr/src/app/15__Test-Dir/test.py"))