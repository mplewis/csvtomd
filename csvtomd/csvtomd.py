#!/usr/bin/env python3

"""
csvtomd 0.3.0

Convert your CSV files into Markdown tables.

More info: http://github.com/mplewis/csvtomd
"""

import argparse

# import csv
# import sys


DEFAULT_PADDING = 2


def check_negative(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError('"%s" must be an integer' % value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError('"%s" must not be a negative value' % value)
    return ivalue


def wrap(outer, count, inner):
    if count <= 0:
        return inner
    return wrap(outer, count - 1, outer + inner + outer)


# if __name__ == "__main__":
#     main()
