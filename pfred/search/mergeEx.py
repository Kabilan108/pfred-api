"""Python implementation of mergeEx.pl"""

import re
import sys
import click
from typing import List, Dict, TextIO
import io


# from mergeEx.pl
def cleanup(_id: str) -> str:
    """Clean up an ID based on a set of regular expressions.

    Parameters
    ----------
    _id : str
        The ID to clean up.

    Returns
    -------
    str
        The cleaned up ID.
    """

    id_patterns = [
        (r"(^\d{7})\d{4}", r"\1"),  # Ann Arbor compounds
        (r"(^\d{7})-\d{4}", r"\1"),  # .
        (r"(^PF-\d{8})", r"\1"),  # Pfizer new PF compounds
        (r"(^\w{2}-\d{6})-\d{2}", r"\1"),  # Other legacy Pfizer compounds
        (r"^PHA-00(\d{6})", r"PHA-00\1"),  # PHA cmpds
        (r"^PNU-0(\d{6})", r"PNU-0\1"),  # PNU cmpds
        (r"^PNUL(\d{6})", r"PNUL\1"),  # PNUL cmpds
    ]

    for pattern, replacement in id_patterns:
        if re.match(pattern, _id, flags=re.IGNORECASE):
            return re.sub(pattern, replacement, _id, flags=re.IGNORECASE)

    return _id


# from mergeEx.pl
def read_file(file: str) -> List[str]:
    """Read lines from a file

    Parameters
    ----------
    file : str
        The file to read.

    Returns
    -------
    List[str]
        The lines read from the file.
    """

    with open(file, "r", encoding="utf-8") as handle:
        return [line.strip() for line in handle.readlines()]


# from mergeEx.pl
def process_lines(
    lines: List[str], idx: int, ref: Dict[str, str], num_fields: int, keep_file: bool
) -> None:
    """Process lines from standard input.

    Parameters
    ----------
    lines : List[str]
        The lines to process.
    idx : int
        The index to use for matching the reference.
    ref : Dict[str, str]
        The reference dictionary.
    num_fields : int
        The number of fields in the reference.
    keep_file : bool
        Whether to keep all lines from the input.
    """

    for line in lines:
        fields = line.split("\t")
        _id = cleanup(fields[idx - 1])
        if _id in ref:
            print(f"{line}\t{ref[_id]}")
        elif keep_file:
            print(f"{line}", end="")
            for j in range(num_fields):
                print("\t ", end="")
                if j == idx - 1:
                    print(f"{_id}", end="")
            print()


def merge_ex(idx1: int, idx2: int, file1: str | TextIO, file2: str, keep_all_in_file1: bool) -> None:
    """A python implementation of mergeEx.pl.

    Parameters
    ----------
    idx1 : int
        The first index
    idx2 : int
        The second index
    file1 : str
        The first file to read.
    file2 : str
        The second file to read.
    keep_all_in_file1 : bool
        Whether to keep all lines from the input.
    """

    lines2 = read_file(file2)
    ref = {}
    num_fields = 0
    for line in lines2:
        fields = line.split('\t')
        if num_fields == 0:
            num_fields = len(fields)
        _id = cleanup(fields[idx2 - 1])
        ref[_id] = line

    if isinstance(file1, str):
        lines1 = read_file(file1)
    elif isinstance(file1, io.TextIOWrapper):
        lines1 = [line.rstrip() for line in file1.readlines()]
    else:
        print(type(file1))
        raise TypeError("file1 must be a string or a file-like object.")
    
    print(lines1)
    print(idx1)
    print(ref)
    print(num_fields)

    process_lines(lines1, idx1, ref, num_fields, keep_all_in_file1)


# from mergeEx.pl
@click.command()
@click.argument('idx1', type=int)
@click.argument('idx2', type=int)
@click.argument('file2', type=click.Path(exists=True))
@click.option('--keep-all', is_flag=True, help='Keep all lines from the input file.')
def main(idx1: int, idx2: int, file2: str, keep_all: bool) -> None:
    """Command line interface for mergeEx.pl.

    Expects file1 as standard input.
    """

    merge_ex(idx1, idx2, sys.stdin, file2, keep_all)


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
