"""
![plate-img](https://user-images.githubusercontent.com/10051679/118867629-31ee9500-b8db-11eb-81e0-10ed5328a692.png)

Python functions to plot interative platemaps using [altair](https://altair-viz.github.io/) from pandas DataFrames.

Platemaps should be able to handle anything from 6-384 well plates (1536 potentially incoming).
"""

from plateplot.plot import platemap
from plateplot import transforms
from plateplot import utils
