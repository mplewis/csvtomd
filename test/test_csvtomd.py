from csvtomd.csvtomd import (
    pad_to, normalize_cols, pad_cells, horiz_div, add_dividers, md_table
)

import pytest
import sure  # noqa

import csv
from glob import glob


def read_csv(path):
    with open(path) as f:
        return list(csv.reader(f))


def read_file(path):
    with open(path) as f:
        return f.read()


def test_pad_to():
    pad_to('word', 8).should.equal('word    ')
    pad_to('word', 2).should.equal('word')


def test_normalize_cols():
    initial = [
        ['a', 'b', 'c'],
        ['d'],
        ['e', 'f'],
    ]
    expected = [
        ['a', 'b', 'c'],
        ['d',  '',  ''],
        ['e', 'f',  ''],
    ]
    normalize_cols(initial).should.equal(expected)


def test_pad_cells():
    initial = [
        ['12345', '123',  '1'],
        [    '1', '123', '12'],
    ]
    expected = [
        ['12345', '123', '1 '],
        ['1    ', '123', '12'],
    ]
    pad_cells(initial).should.equal(expected)


def test_horiz_div():
    """
    notice that first and last cols aren't fully padded:
    ['abc', 'd', 'ef'] =>
    abc | d | ef
    ----|---|---
    """
    output = horiz_div([3, 1, 2], '-', '|', 1)
    expected = '----|---|---'
    output.should.equal(expected)
    output = horiz_div([5, 3, 1], '.', '#', 2)
    expected = '.......#.......#...'
    output.should.equal(expected)


def test_add_dividers():
    output = add_dividers(['a', 'b', 'c'], '|', 1)
    expected = 'a | b | c'
    output = add_dividers(['a', 'b', 'c', 'd', 'e'], '#', 0)
    expected = 'a#b#c#d#e'
    output = add_dividers(['a', 'b', 'c', 'd'], '.', 3)
    expected = 'a   .   b   .   c   .   d   .   e'


csvs = glob('test/input/*.csv')
mds = glob('test/output/*.md')
@pytest.mark.parametrize('csv,md', zip(csvs, mds))
def test_md_table(csv, md):
    table = read_csv(csv)
    output = md_table(table)
    expected = read_file(md).rstrip('\n')
    print(output)
    print(expected)
    output.should.equal(expected)
