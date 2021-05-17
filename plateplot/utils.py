"""General utility functions"""


def split_row_col(well):
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
    row = well[0]
    col = int(well[1:])
    return row, col
