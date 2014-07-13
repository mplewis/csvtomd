import pandoc
import os

pandoc.core.PANDOC_PATH = '/usr/bin/env pandoc'

doc = pandoc.Document()
with open('README.md') as f:
    doc.markdown = f.read()

f = open('README.txt', 'w+')
f.write(doc.rst)
f.close()

os.system('setup.py register')
os.remove('README.txt')
