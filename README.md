# csvtomd: markdown tables made easy

*Version 0.1.0*

Convert your CSV files into Markdown tables.

[Tables Generator](http://www.tablesgenerator.com/markdown_tables) is a fantastic web tool for converting tabular data into all sorts of table layouts. I like how it lets me import CSV files, but I need the ability to convert many CSV files in batch for a docset on which I'm working.

I built `csvtomd` to convert one or more CSV files into nicely-padded Markdown tables. Now you can build your tables in Excel and convert them for use in GitHub, Bitbucket, or [Mou](http://mouapp.com/) Markdown files without having to construct them by hand.

# Usage

## Requirements

Python 3. Tested on Python 3.4.1.

## Input

File: `thrones.csv`

```
First Name,Last Name,Location,Allegiance
Mance,Rayder,North of the Wall,Wildlings
Margaery,Tyrell,The Reach,House Tyrell
Danerys,Targaryen,Meereen,House Targaryen
Tyrion,Lannister,King's Landing,House Lannister
```

## Markdown Table

First Name  |  Last Name  |  Location           |  Allegiance
------------|-------------|---------------------|-----------------
Mance       |  Rayder     |  North of the Wall  |  Wildlings
Margaery    |  Tyrell     |  The Reach          |  House Tyrell
Danerys     |  Targaryen  |  Meereen            |  House Targaryen
Tyrion      |  Lannister  |  King's Landing     |  House Lannister

## Raw Output

Command: `./csvtomd.py thrones.csv`

```
First Name  |  Last Name  |  Location           |  Allegiance
------------|-------------|---------------------|-----------------
Mance       |  Rayder     |  North of the Wall  |  Wildlings
Margaery    |  Tyrell     |  The Reach          |  House Tyrell
Danerys     |  Targaryen  |  Meereen            |  House Targaryen
Tyrion      |  Lannister  |  King's Landing     |  House Lannister
```

Command: `./csvtomd.py --padding 0 thrones.csv`

```
First Name|Last Name|Location         |Allegiance
----------|---------|-----------------|---------------
Mance     |Rayder   |North of the Wall|Wildlings
Margaery  |Tyrell   |The Reach        |House Tyrell
Danerys   |Targaryen|Meereen          |House Targaryen
Tyrion    |Lannister|King's Landing   |House Lannister
```

## Help

Command: `./csvtomd.py --help`

```
usage: csvtomd.py [-h] [-n] [-p PADDING] csv_file [csv_file ...]

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
```

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time. You can also tweet me at [@mplewis](http://twitter.com/mplewis) or email me at [matt@mplewis.com](mailto:matt@mplewis.com).

# License

Copyright (c) 2014 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).