from csvtomd import md_table

import sure  # noqa
from csv import reader



def test_default():
    with open('test/input/normal.csv') as f:
        to_convert = [row for row in reader(f)]
    with open('test/output/normal.md') as f:
        expected = f.read().strip()
    md_table(to_convert).should.equal(expected)


def test_jagged():
    with open('test/input/jagged.csv') as f:
        to_convert = [row for row in reader(f)]
    with open('test/output/jagged.md') as f:
        expected = f.read().strip()
    md_table(to_convert).should.equal(expected)
