"""
Transform and aggregate data before plotting.
"""

import numpy as np


def group(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns
    --------
    pandas.DataFrameGroupBy
    """
    df_sub = df[[well, val, plate]]
    df_grouped = df_sub.groupby([plate, well], as_index=False)
    return df_grouped


def cv(x):
    """
    Parameters
    -----------
    x : array-like

    Notes
    ------
    Coefficient of variation should not be used on z-scored
    values, or any other values which could be negative.

    Returns
    --------
    array-like
        same dimensions as input
    """
    return np.std(x, ddof=1) / np.mean(x) * 100
