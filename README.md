# About
PDF manipulation command line tool written in Python. This serves as a lightweight PDF manipulation program which may be used instead of various online or GUI PDF tools.

# Installtion

## Installation using PIP

1. Clone this repository:

    `git clone https://github.com/dvdvgt/pdfTool.git`
2. Run the following command inside the root directory of repository:

    `pip install -U .`
    
    to install the program using pip.
3. The tool may now be used as described below.

## Dependencies

- [PyPDF2](https://pypi.org/project/PyPDF2/)

# Usage

## Basic Usage

```
usage: pdfTool [-h] <command> ...

PDF command-line tool

optional arguments:
  -h, --help  show this help message and exit

Commands:
  <command>
    join      Join multiple PDF files.
    extract   Extract specific pages of a pdf.
```
## Joining

```
usage: pdfTool join [-h] infile [infile ...] outfile

positional arguments:
  infile      Input files to be joined seperated by spaces.
  outfile     Name of the output file.

optional arguments:
  -h, --help  show this help message and exit
```

This subcommand merges multiple PDF files into one PDF file. Simply specify all files to merge and the path/name of the resulting file.

Example: 
- `pdfTool join /path/to/file1.pdf /path/to/file2.pdf /path/to/result.pdf`

## Extracting

```
usage: pdfTool extract [-h] [--pages PAGES [PAGES ...]] infile outfile

Extract specific pages of a pdf.

positional arguments:
  infile                Name of the input file from which to extract pages.
  outfile               Name of the output file to write the extracted pages to.

optional arguments:
  -h, --help            show this help message and exit
  --pages PAGES [PAGES ...], -p PAGES [PAGES ...]
                        Range of numbers representing the pages to be extracted. Single
                        pages may be specified as well as a range of pages e.g. 1 2 4-8 20
```

This subcommand extracts pages of a given PDF file. Specify the pages to be extracted and the path/name of the resulting file. Note that all extracted pages will be merged into one file.

The pages may be entered as integers or as e.g. "5-12" representing a range of integers.

Example: 
- `pdfTool extract 1 2 4-8 20 file.pdf result.pdf`
