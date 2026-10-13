"""@file constants.py
@brief All constants of the miles to kilometers converter.

Every other module imports its numbers and texts from here, so a value is defined once.
"""

## Kilometers in one mile, as used in the course assignment.
KM_PER_MILE: float = 1.609

## Digits after the decimal point shown in the result label.
RESULT_DECIMALS: int = 2

## Title of the main window.
WINDOW_TITLE: str = "Miles to Kilometer Converter"

## Text of the label next to the miles entry.
LABEL_MILES: str = "Miles"

## Text of the label between the entry and the result.
LABEL_EQUAL: str = "is equal to"

## Text of the label next to the result.
LABEL_KM: str = "Km"

## Text of the calculate button.
BUTTON_CALCULATE: str = "Calculate"

## Result shown before the first calculation.
DEFAULT_RESULT: str = "0"

## Text shown in the result label when the entry is not a number.
MESSAGE_INVALID_INPUT: str = "Enter a number"

## Width of the entry widget, in characters.
ENTRY_WIDTH: int = 7

## Padding around the window content, in pixels.
WINDOW_PADDING: int = 20

## Padding between widgets, in pixels.
WIDGET_PADDING: int = 5
