import argparse
from . import pdfUtils

def main():
    # Top level parser
    PARSER = argparse.ArgumentParser(description="PDF command-line tool")
    SUBPARSER = PARSER.add_subparsers(
        title="Commands",
        dest="command",
        metavar="<command>"
    )
    #
    # Join
    #
    JOIN_PARSER = SUBPARSER.add_parser(
        "join",
        help="Join multiple PDF files."
    )
    JOIN_PARSER.add_argument("infile", type=argparse.FileType("rb"), nargs="+", help="Input files to be joined seperated by spaces.")
    JOIN_PARSER.add_argument("outfile", type=argparse.FileType("wb"), help="Name of the output file.")
    #
    # Extract
    #
    ADD_PARSER = SUBPARSER.add_parser(
        "extract",
        help="Extract specific pages of a pdf.",
        description="Extract specific pages of a pdf."
    )
    ADD_PARSER.add_argument(
        "--pages", "-p",
        dest="pages",
        type=str,
        nargs="+",
        help="Range of numbers representing the pages to be extracted. Single pages may be specified as well as a range of pages e.g. 1 2 4-8 20"        
    )
    ADD_PARSER.add_argument("infile", type=argparse.FileType("rb"), help="Name of the input file from which to extract pages.")
    ADD_PARSER.add_argument("outfile", type=argparse.FileType("wb"), help="Name of the output file to write the extracted pages to.")

    ARGS = PARSER.parse_args()
    #
    # Call appropriate functions depending on the parsed parameters.
    #
    if ARGS.command == "join":
        pdfUtils.join(ARGS.infile, ARGS.outfile)
    elif ARGS.command == "extract":
        pages: list = arg_range(ARGS.pages)
        # Subtract one from every number since pyPDF starts counting pages at 0
        pages = list(map(lambda x: x-1, pages))
        pdfUtils.extract(
            ARGS.infile,
            ARGS.outfile,
            arg_range(ARGS.pages)
        )


def arg_range(nums : list) -> list:
    """
    Parameters
    ----------
    nums: list
        List of strings to convert to a list of integers.
        Elements may have the format "1-10" (representing a range of integer) 
        or "5" (representing a single integer).
    
    Returns
    -------
    list
        List of interges.
    """
    # Convert list of strings to list of integers.
    out = []
    for num in nums:
        if "-" in num:
            start, end = map(int, num.split("-"))
            for i in range(start, end + 1):
                out.append(i)
        else:
            out.append(int(num))
    return out

if __name__ == "__main__":
    main()