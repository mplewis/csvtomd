#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# Ensure stdin input to csvtomd works properly

# no args: read from stdin
echo 'stdin from normal'
cat test/input/normal.csv | python3 csvtomd/csvtomd.py | cmp test/output/normal.md
echo 'stdin from jagged'
cat test/input/jagged.csv | python3 csvtomd/csvtomd.py | cmp test/output/jagged.md

# - arg: read from file
echo 'stdin via - from normal'
cat test/input/normal.csv | python3 csvtomd/csvtomd.py - | cmp test/output/normal.md

# ensure other args work too
echo 'stdin with --padding 1 from normal'
cat test/input/normal.csv | python3 csvtomd/csvtomd.py --padding 1 | cmp test/output/normal_pad1.md
