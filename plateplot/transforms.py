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


def mean(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns:
    --------
    pandas.DataFrame
    """
    return group(df, well, val, plate).agg(func="mean")


def median(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns
    --------
    pandas.DataFrame
    """
    return group(df, well, val, plate).agg(func="median")


def std(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns
    --------
    pandas.DataFrame
    """
    return group(df, well, val, plate).agg(func="std")


def var(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns
    --------
    pandas.DataFrame
    """
    return group(df, well, val, plate).agg(func="var")


def mad(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Returns
    --------
    pandas.DataFrame
    """
    df_mad = group(df, well, val, plate).agg(func="mad")
    # for some reason mad keeps the multi-index, so we have to drop that
    return df_mad.reset_index(drop=True)



def cv(df, well, val, plate):
    """
    Parameters
    -----------
    df : pandas.DataFrame
    well : str
    val : str
    plate : str

    Notes
    ------
    Coefficient of variation should not be used on z-scored
    values, or any other values which could be negative.

    Returns
    --------
    pandas.DataFrame
    """
    cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100
    return group(df, well, val, plate).agg(func=cv)
