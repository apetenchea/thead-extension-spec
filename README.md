# T-Head ISA extensions (Xthead*)

This repository contains the T-Head RISC-V ISA extensions (Xthead*) specifications.

## Build instructions

The specification is written in AsciiDoc.
The following instructions can be used to generate a PDF containing
all specifications:

```
make
```

## Helper scripts

- `scripts/samples.sh` - search through dissasembly files and gather up to two samples for the given instructions
- `scripts/search.sh` - search through dissasembly files and find which files contain the given instructions
- `scripts/adoc-extrac.py` - search recursively through `.adoc` files and extract the instructions
- `scripts/bb.py` - manipulated 32-bit numbers

## Data

- list of instructions is in `data/ins.txt`
- executable names containing instructions are in `data/samples.txt`
- instructions and their corresponding `.adoc` file names are in `data/files.txt`
