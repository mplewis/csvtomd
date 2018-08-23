# csvtomd: markdown tables made easy

# This project is discontinued

Thanks for all your contributions! At this time I'm not continuing development on the Python version of this tool.

I'm moving work to the following JS projects:

* [csvtomd lib](https://github.com/mplewis/csvtomd-lib)
* [csvtomd CLI](https://github.com/mplewis/csvtomd-cli)
* [csvtomd web](https://github.com/mplewis/csvtomd-web)

I'm happy to point to your projects if you decide to take over development on the Python version! Just let me know.

-----

![Excel —> Markdown](http://mplewis.com/files/csvtomd.png?)

[![CircleCI](https://circleci.com/gh/mplewis/csvtomd.svg?style=svg)](https://circleci.com/gh/mplewis/csvtomd)

Convert your CSV files into Markdown tables.

[Tables Generator](http://www.tablesgenerator.com/markdown_tables) is a fantastic web tool for converting tabular data into all sorts of table layouts. I like how it lets me import CSV files, but I need the ability to convert many CSV files in batch for a docset on which I'm working.

I built `csvtomd` to convert one or more CSV files into nicely-padded Markdown tables. Now you can build your tables in Excel and convert them for use in GitHub Markdown files without having to construct them by hand.

# Installation

This is a Python 3 script, so use `pip3` to install:

```
pip3 install csvtomd
```

After this, run `csvtomd --help` from your terminal to verify it's installed properly.

# Usage

`csvtomd MY_SPREADSHEET.csv` generates a Markdown table from `MY_SPREADSHEET.csv`.

`csvtomd SHEET1.csv SHEET2.csv SHEET3.csv` generates three Markdown tables from the input files and displays them alongside the input filename.

`csvtomd` or `csvtomd -` generates a Markdown table from standard input. You can type CSV data or pipe a file in.

## Example Input

File: `thrones.csv`

```
First Name,Last Name,Location,Allegiance
Mance,Rayder,North of the Wall,Wildlings
Margaery,Tyrell,The Reach,House Tyrell
Danerys,Targaryen,Meereen,House Targaryen
Tyrion,Lannister,King's Landing,House Lannister
```

## Example Markdown Table

Command: `csvtomd thrones.csv`

First Name  |  Last Name  |  Location           |  Allegiance
------------|-------------|---------------------|-----------------
Mance       |  Rayder     |  North of the Wall  |  Wildlings
Margaery    |  Tyrell     |  The Reach          |  House Tyrell
Danerys     |  Targaryen  |  Meereen            |  House Targaryen
Tyrion      |  Lannister  |  King's Landing     |  House Lannister

## Example Raw Output

Command: `csvtomd thrones.csv`

```
First Name  |  Last Name  |  Location           |  Allegiance
------------|-------------|---------------------|-----------------
Mance       |  Rayder     |  North of the Wall  |  Wildlings
Margaery    |  Tyrell     |  The Reach          |  House Tyrell
Danerys     |  Targaryen  |  Meereen            |  House Targaryen
Tyrion      |  Lannister  |  King's Landing     |  House Lannister
```

Command: `csvtomd --padding 0 thrones.csv`

```
First Name|Last Name|Location         |Allegiance
----------|---------|-----------------|---------------
Mance     |Rayder   |North of the Wall|Wildlings
Margaery  |Tyrell   |The Reach        |House Tyrell
Danerys   |Targaryen|Meereen          |House Targaryen
Tyrion    |Lannister|King's Landing   |House Lannister
```

## Requirements

Python 3.

Tested with Python 3.4.1 on Mac OS X 10.9.3.

Doesn't require any external packages, so it should be platform-agnostic.

## Help

Command: `csvtomd --help`

```
usage: csvtomd.py [-h] [-n] [-p PADDING] [-d DELIMITER] csv_file [csv_file ...]

Read one or more CSV files and output their contents in the form of Markdown
tables.

positional arguments:
  csv_file              One or more CSV files to be converted

optional arguments:
  -h, --help            show this help message and exit
  -n, --no-filenames    Don't display filenames when outputting multiple
                        Markdown tables.
  -p PADDING, --padding PADDING
                        The number of spaces to add between table cells and
                        column dividers. Default is 2 spaces.
  -d DELIMITER, --delimiter DELIMITER
                        CSV delimiter, expected values: ',', ';'. Default is ,
```

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time.

## Testing

I only accept pull requests for features with tests.

```sh
# Run tests in the project root
$ py.test
============================= test session starts ==============================
platform darwin -- Python 3.5.0, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
rootdir: /your/path/to/csvtomd, inifile:
collected 3 items

test/test_csvtomd.py ...

=========================== 3 passed in 0.04 seconds ===========================
```

## Releasing

```sh
# Bump version number in setup.py and csvtomd.py
# Delete old builds
rm -rf dist
# Build source and binary wheel distribution
python setup_wrap.py sdist bdist_wheel
# Upload to PyPI
pip install twine
twine upload dist/*
```

[Here's an actual guide to PyPI.](https://packaging.python.org/distributing/) [And another really good one.](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

# License

Copyright (c) 2017 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).
