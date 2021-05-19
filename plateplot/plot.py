"""
Plotting functions.
"""


import altair as alt

from . import utils


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


def platemap_std(
    df,
    well="Well",
    val="Result",
    plate="plate",
    rep="replicate",
    tooltips=None,
    cmap=None,
    plate_size=[250, 180],
    text_size=7,
):
    """Plot the standard deviation platemap of multiple plates.

    Plot an interactive platemap showing the aggregated standard deviation
    of replicate plates.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe containing plate data
    well : string
        name of well column in `df`
    val : string
        name of value column in `df`
    plate:  string
        name of plate column in `df`
    rep : string
        name of replicate column in `df`
    tooltips : list of strings
        name of columns to show info on well-hover
    cmap : string
        colourmap
    plate_size: list[int, int[
        [width, height] size of individual plates in pixels
    text_size : int
        size of text in row, column, plate labels

    Returns
    ---------
    altair.Chart
    """
    # aggregregate data to median
    # use `platemap()` function to create plot
    raise NotImplementedError()


def platemap_mad(
    df,
    well="Well",
    val="Result",
    plate="plate",
    rep="replicate",
    tooltips=None,
    cmap=None,
    plate_size=[250, 180],
    text_size=7,
):
    """Plot the median absolute deviation platemap of multiple plates.

    Plot an interactive platemap showing the aggregated median
    absolute deviation (MAD) of replicate plates.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe containing plate data
    well : string
        name of well column in `df`
    val : string
        name of value column in `df`
    plate:  string
        name of plate column in `df`
    rep : string
        name of replicate column in `df`
    tooltips : list of strings
        name of columns to show info on well-hover
    cmap : string
        colourmap
    plate_size: list[int, int[
        [width, height] size of individual plates in pixels
    text_size : int
        size of text in row, column, plate labels

    Returns
    ---------
    altair.Chart
    """
    # aggregregate data to median
    # use `platemap()` function to create plot
    raise NotImplementedError()


def platemap_mean(
    df,
    well="Well",
    val="Result",
    plate="plate",
    rep="replicate",
    tooltips=None,
    cmap=None,
    plate_size=[250, 180],
    text_size=7,
):
    """Plot the mean platemap of multiple plates.

    Plot an interactive platemap showing the aggregated mean
    of replicate plates.

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
    rep : string
        name of replicate column in `df`
    tooltips : list of strings
        name of columns to show info on well-hover
    cmap : string
        colourmap
    plate_size: list[int, int[
        [width, height] size of individual plates in pixels
    text_size : int
        size of text in row, column, plate labels

    Returns
    ---------
    altair.Chart
    """
    # aggregate to mean
    # plot with `platemap()`
    raise NotImplementedError()


def platemap_median(
    df,
    well="Well",
    val="Result",
    plate="plate",
    rep="replicate",
    tooltips=None,
    cmap=None,
    plate_size=[250, 180],
    text_size=7,
):
    """Plot the median platemap of multiple plates.

    Plot an interactive platemap showing the aggregated median
    of replicate plates.

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
    rep : string
        name of replicate column in `df`
    tooltips : list of strings
        name of columns to show info on well-hover
    cmap : string
        colourmap
    plate_size: list[int, int[
        [width, height] size of individual plates in pixels
    text_size : int
        size of text in row, column, plate labels

    Returns
    ---------
    altair.Chart
    """
    # aggregate to median
    # plot with `platemap()`
    raise NotImplementedError()
