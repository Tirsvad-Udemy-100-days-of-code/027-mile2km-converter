"""@file converter.py
@brief The conversion rule, free of any user interface.
"""

import math

from mile2km.constants import KM_PER_MILE, RESULT_DECIMALS


def miles_to_km(miles: float) -> float:
    """@brief Convert a distance from miles to kilometers.

    @param miles Distance in miles.
    @return Distance in kilometers.
    """
    return miles * KM_PER_MILE


def parse_miles(text: str) -> float:
    """@brief Read a distance in miles from text typed by the user.

    @param text Text of the entry widget.
    @return The distance as a number.
    @throws ValueError if the text is not a finite number.
    """
    try:
        miles = float(text.strip())
    except ValueError as error:
        raise ValueError(f"not a number: {text!r}") from error
    if not math.isfinite(miles):
        raise ValueError(f"not a finite number: {text!r}")
    return miles


def format_km(kilometers: float) -> str:
    """@brief Format a distance in kilometers for display.

    @param kilometers Distance in kilometers.
    @return The distance rounded to the configured number of decimals.
    """
    return f"{kilometers:.{RESULT_DECIMALS}f}"


def convert_text(text: str) -> str:
    """@brief Convert the text of the miles entry to the text of the result.

    @param text Text typed by the user, in miles.
    @return The distance in kilometers, formatted for display.
    @throws ValueError if the text is not a finite number.
    """
    return format_km(miles_to_km(parse_miles(text)))
