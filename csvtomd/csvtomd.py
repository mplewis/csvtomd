#!/usr/bin/env python3

"""
csvtomd v0.1.2

Convert your CSV files into Markdown tables.

More info: http://github.com/mplewis/csvtomd
"""

import argparse
from csv import reader
from pprint import pprint


def check_negative(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            '"%s" must be an integer' % value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(
            '"%s" must not be a negative value' % value)
    return ivalue


def pad_to(unpadded, target_len):
    """
    Pad a string to the target length in characters, or return the original
    string if it's longer than the target length.
    """
    under = target_len - len(unpadded)
    if under <= 0:
        return unpadded
    return unpadded + (' ' * under)


def normalize_cols(table):
    """
    Pad short rows to the length of the longest row to help render "jagged"
    CSV files
    """
    longest_row_len = max([len(row) for row in table])
    for row in table:
        while len(row) < longest_row_len:
            row.append('')
    return table


def pad_cells(table):
    """Pad each cell to the size of the largest cell in its column."""
    col_sizes = [max(map(len, col)) for col in zip(*table)]
    for row in table:
        for cell_num, cell in enumerate(row):
            row[cell_num] = pad_to(cell, col_sizes[cell_num])
    return table


def horiz_div(col_widths, horiz, vert, padding):
    """
    Create the column dividers for a table with given column widths.

    col_widths: list of column widths
    horiz: the character to use for a horizontal divider
    vert: the character to use for a vertical divider
    padding: amount of padding to add to each side of a column
    """
    horizs = [horiz * w for w in col_widths]
    div = ''.join([padding * horiz, vert, padding * horiz])
    return div.join(horizs)


def md_table(table, *, padding=1, divider='|', header_div='-'):
    """
    Convert a 2D array of items into a Markdown table.

    padding: the number of padding spaces on either side of each divider
    divider: the vertical divider to place between columns
    header_div: the horizontal divider to place between the header row and
        body cells
    """
    # Output data buffer
    output = ''
    table = normalize_cols(table)
    table = pad_cells(table)

    header = table[0]
    body = table[1:]

    col_widths = [len(cell) for cell in header]
    horiz = horiz_div(col_widths, header_div, divider, padding)


    # Get max length of any cell for each column
    # Set up the horizontal header dividers
    header_divs = [None] * len(col_sizes)
    num_cols = len(col_sizes)
    # Pad header divs to the column size
    for cell_num in range(num_cols):
        header_divs[cell_num] = header_div * (col_sizes[cell_num] +
                                              padding * 2)
    # Trim first and last padding chars, if they exist
    if padding > 0:
        header_div_row = divider.join(header_divs)[padding:-padding]
    else:
        header_div_row = divider.join(header_divs)
    # Split out the header from the body
    # Build the inter-column dividers using the padding settings above
    multipad = ' ' * padding
    divider = multipad + divider + multipad
    output += divider.join(header) + '\n'
    output += header_div_row + '\n'
    for row in body:
        output += divider.join(row) + '\n'
    # Strip the last newline
    if output.endswith('\n'):
        output = output[:-1]
    return output


def main():
    parser = argparse.ArgumentParser(
        description='Read one or more CSV files and output their contents in the '
                    'form of Markdown tables.')
    parser.add_argument('files', metavar='csv_file', type=str,
                        nargs='+', help='One or more CSV files to be converted')
    parser.add_argument('-n', '--no-filenames', action='store_false',
                        dest='show_filenames',
                        help="Don't display filenames when outputting multiple "
                             "Markdown tables.")
    parser.add_argument('-p', '--padding', type=check_negative, default=2,
                        help="The number of spaces to add between table cells "
                             "and column dividers. Default is 2 spaces.")
    parser.add_argument('-d', '--delimiter', default=',',
                        help="CSV delimiter, expected values: ',', ';'. Default is %(default)s")

    args = parser.parse_args()
    first = True
    for file_num, filename in enumerate(args.files):
        # Print space between consecutive tables
        if not first:
            print('')
        else:
            first = False
        # Read the CSV files
        with open(filename, 'rU') as f:
            csv = reader(f, delimiter=args.delimiter)
            table = [row for row in csv]
        # Print filename for each table if --no-filenames wasn't passed and more
        # than one CSV was provided
        file_count = len(args.files)
        if args.show_filenames and file_count > 1:
            print(filename + '\n')
        # Generate and print Markdown table
        print(md_table(table, padding=args.padding))

if __name__ == '__main__':
    main()
