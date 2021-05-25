"""
Plotting functions.
"""


import altair as alt

from . import utils
from . import transforms


altair_encoding_dict = {
    "continuous": "quantitative",
    "ordered": "ordinal",
    "categorical": "nominal",
}


def platemap(
    df,
    well="Well",
    val="Result",
    plate="plate",
    tooltips=None,
    diverging=False,
    cmap=None,
    val_type="continuous",
    ncols=3,
    plate_size=[250, 180],
    text_size=7,
):
    """Plot a platemap.

    Plot an interactive platemap of one of more plates.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe containing plate data
    well : string
        name of well column in `df`
    val : string
        name of value column in `df`
    plate :  string
        name of plate column in `df`
    tooltips : list of strings
        name of columns to show info on well-hover
    divering : bool
        whether or not data is divering
    cmap : string
        colourmap
    val_type : string
        whether values are: "continuous", "ordered" or "categorical",
        this will influence the colourmap and legend format
    ncols : int
        number of columns to display multiple plates
    plate_size: list[int, int[
        [width, height] size of individual plates in pixels
    text_size : int
        size of text in row, column, plate labels

    Returns
    ---------
    altair.Chart
    """
    val_type_altair = altair_encoding_dict[val_type]
    if tooltips is None:
        tooltips = [well, val, plate]
    rows, cols = zip(*[utils.split_row_col(i) for i in df[well]])
    df["row"] = rows
    df["col"] = cols
    if val_type == "continuous":
        if cmap is None:
            cmap = "purpleorange" if diverging else "viridis"
        if diverging:
            sigma = df[val].abs().max()
            domain = [-sigma, sigma]
        else:
            domain = [df[val].min(), df[val].max()]
        color = alt.Color(
            val, type=val_type_altair, scale=alt.Scale(scheme=cmap, domain=domain)
        )

    else:
        # TODO handle cmaps with ordered and categorical data
        color = alt.Color(val, type=val_type_altair)
    chart = (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x=alt.X("col:N", title=None),
            y=alt.Y("row:N", title=None),
            color=color,
            tooltip=tooltips,
            facet=alt.Facet(
                f"{plate}:N",
                columns=ncols,
                title=None,
                header=alt.Header(orient="bottom"),
            ),
        )
        .configure_axis(labelFontSize=text_size)
        .configure_axisX(orient="top", labelAngle=0, labelPadding=10)
        .configure_scale(bandPaddingInner=0.06)
        .configure_legend(
            labelFontSize=text_size,
            titleFontSize=text_size,
            gradientLength=100,
            gradientThickness=10,
        )
        .resolve_axis(x="independent", y="independent")
        .properties(width=plate_size[0], height=plate_size[1])
    )
    return chart


def platemap_agg(
    df, well="Well", val="Result", plate="plate", agg_func="mean", **kwargs
):
    """
    Plot an interactive platemap of multiple plates after performing
    and aggregation on the replicates.

    Parameters
    -----------
    df : pandas.DataFrame
        dataframe containing plate data
    well : string
        name of well column in `df`
    val : string
        name of value column in `df`
    plate :  string
        name of plate column in `df`
    agg_func : str, function, list or dict
        Function to use for aggregating the data. If a function, must either
        work when passed a pandas.DataFrame, or when passed to DataFrame.apply.
        Accepted combinations are:
        - function
        - string of function name
        This does not handle multiple aggregation functions like
        pandas.DataFrame.agg as we only plot a single feature on the platemap.
    **kwargs : key-word arguments
        additional arguments passed to `platemap`

    Returns
    -------
    altair.Chart
    """
    # handle edge cases for agg_func
    if isinstance(agg_func, str):
        if agg_func.lower() == "cv":
            agg_func = transforms.cv
    df_grouped = transforms.group(df, well, val, plate)
    df_agg = df_grouped.agg(func=agg_func)
    # deal with bug where MAD aggregation still retains multi-index
    # which we need to remove for altair
    if isinstance(agg_func, str):
        if agg_func.lower() == "mad":
            df_agg = df_agg.reset_index(drop=True)
    chart = platemap(df_agg, well, val, plate, **kwargs)
    return chart
