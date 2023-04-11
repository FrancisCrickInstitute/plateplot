"""General utility functions"""
from typing import Tuple


def split_row_col(well: str) -> Tuple[str, int]:
    """Split a well label into row and column labels.

    e.g "A01" becomes ["A", 1]

    Parameters
    -----------
    well : string
        well label

    Returns
    ---------
    string
        row
    int
        column
    """
    row = well[:-2]
    col = int(well[-2:])
    return row, col
