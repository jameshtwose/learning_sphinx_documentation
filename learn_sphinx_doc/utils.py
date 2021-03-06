r"""Submodule utils.py includes the following functions and classes: <br>

    - **silence_stdout():** a function intended to be used in a with statetment to suppress printed output. <br>
    - **JmsColors:** a class containing useful colours according to Jms and functions to show these colors in various forms.
        <br>
    - **apply_scaling():** a utility function to be used in conjunction with pandas pipe() to scale columns of a data frame
        seperately. <br>
    - **flatten():** a utility function used to flatten a list of lists to a single list. <br>

"""
import os
import sys
from contextlib import (
    contextmanager,
)  # these three are needed to create the silence output function
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


# Create a function which will silence printing when called
@contextmanager
def silence_stdout():
    r"""Utility function used to suppress print statements from other functions.

    Parameters
    ----------
    None

    Returns
    -------
    None


    Examples
    --------
    >>> message = "Ooo look"
    >>> with silence_stdout():
    ...    print(f"My super cool message: {message}")   
    >>> print(message)

    """

    new_target = open(os.devnull, "w")
    old_target = sys.stdout
    sys.stdout = new_target
    try:
        yield new_target
    finally:
        sys.stdout = old_target


class JmsColors:
    r"""Utility class for James Twose's color codes.

    :param get_names(): returns a list of the color names e.g. [PURPLE, DARKBLUE, etc.]
    :param to_dict(): returns a dictionary of format {color name: hexcode}
    :param to_list(): returns a list of hexcodes
    :param plot_colors(): returns a lineplot of all the available colours (like a color swatch)

    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from jmspack.utils import JmsColors
    >>> x = np.linspace(0, 10, 100)
    >>> fig = plt.figure()
    >>> _ = plt.plot(x, np.sin(x), color=JmsColors.ORANGE)
    >>> _ = plt.plot(x, np.cos(x), color=JmsColors.LIGHTBLUE)
    >>> # plt.show()
    """

    PURPLE = "#8f0fd4"
    DARKBLUE = "#0072e8"
    BLUEGREEN = "#009cdc"
    GREENBLUE = "#00c7b1"
    GREENYELLOW = "#71db5c"
    YELLOW = "#fcdd14"

    DARKGREY = "#282d32"
    MEDIUMGREY = "#808080"
    LIGHTGREY = "#b1b1b1"
    OFFWHITE = "#d5d5d5"

    @staticmethod
    def get_names():
        return [
            k
            for k in JmsColors.__dict__.keys()
            if not k.startswith("__") and not callable(getattr(JmsColors, k))
        ]

    @staticmethod
    def to_dict():
        return {
            k: v
            for k, v in JmsColors.__dict__.items()
            if not k.startswith("__") and not callable(getattr(JmsColors, k))
        }

    @staticmethod
    def to_list():
        return [
            v
            for k, v in JmsColors.__dict__.items()
            if not k.startswith("__") and not callable(getattr(JmsColors, k))
        ]

    @staticmethod
    def plot_colors():
        for i, c in enumerate(JmsColors.to_list()):
            _ = plt.title("Available Jms Colors")
            _ = plt.plot([1, 5], [i, i], color=c, linewidth=5)


def apply_scaling(
    df: pd.DataFrame,
    method: Union[str, Optional[Callable]] = "MinMax",
    kwargs: Dict = {},
):
    r"""Utility function to be used in conjunction with pandas pipe()
    to scale columns of a data frame seperately.

    Parameters
    ----------
    df: pd.DataFrame
        The data frame you want to scale.
    method: Callable, str
        The name of the method you wish to use [method options: "MinMax",
        "Standard"], or an Sklearn transformer,
        see: https://scikit-learn.org/stable/modules/preprocessing.html
    kwargs: Dict
        Dictionary containing additional keywords to be added to the Scaler.

    Returns
    -------
    pd.DataFrame

    Examples
    --------
    >>> import seaborn as sns
    >>> import pandas as pd
    >>> df = sns.load_dataset("iris")
    >>> scaled_df = (df
    ...             .select_dtypes("number")
    ...             .pipe(apply_scaling)
    ...             )
    """

    if method == "MinMax":
        scal_df = pd.DataFrame(
            MinMaxScaler(**kwargs).fit_transform(df),
            index=df.index,
            columns=df.columns,
        )
    elif method == "Standard":
        scal_df = pd.DataFrame(
            StandardScaler(**kwargs).fit_transform(df),
            index=df.index,
            columns=df.columns,
        )
    else:
        scal_df = pd.DataFrame(
            method(**kwargs).fit_transform(df), index=df.index, columns=df.columns  # type: ignore
        )
    return scal_df


def flatten(list_of_lists):
    r"""Utility function used to flatten a list of list into a single list.

    Parameters
    ----------
    l: list
        A list of lists.

    Returns
    -------
    pd.DataFrame


    Examples
    --------
    >>> from jmspack.utils import flatten
    >>> list_of_lists = [[f"p_{x}" for x in range(10)],
    ...                 [f"p_{x}" for x in range(10, 20)],
    ...                 [f"p_{x}" for x in range(20, 30)]]
    >>> flatten(list_of_lists)

    """
    return [item for sublist in list_of_lists for item in sublist]
