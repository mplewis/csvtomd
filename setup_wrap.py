import sys
import os
import subprocess
import pypandoc

with open('README.rst', 'w') as dest:
    long_description = pypandoc.convert('README.md', 'rst')
    dest.write(long_description)

args = ['python3', 'setup.py'] + sys.argv[1:]
subprocess.call(args)

os.remove('README.rst')
