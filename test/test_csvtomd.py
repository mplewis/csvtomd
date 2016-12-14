from csvtomd.csvtomd import (
    pad_to, normalize_cols, pad_cells, horiz_div, add_dividers
)

import sure  # noqa


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
