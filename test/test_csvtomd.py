from .csvtomd import md_table

import sure
from csv import reader
from glob import glob
from os.path import basename, splitext


def test_all_csv_files():
    for csv in glob('test/input/*.csv'):
        filename_only = splitext(basename(csv))[0]
        with open(csv) as f:
            to_convert = [row for row in reader(f)]
        with open('test/output/{}.md'.format(filename_only)) as f:
            expected = f.read()
        print(to_convert)
        md_table(to_convert).should.equal(expected)
