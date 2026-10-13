"""@file gui.py
@brief The Tkinter window of the miles to kilometers converter.
"""

import tkinter as tk

from mile2km import constants
from mile2km.converter import convert_text


class ConverterWindow:
    """@brief Main window: an entry for miles, a result label and a calculate button."""

    def __init__(self, master: tk.Tk | None = None) -> None:
        """@brief Build the window and lay out its widgets in a grid.

        @param master Existing root window, or None to create one.
        """
        self.window: tk.Tk = master if master is not None else tk.Tk()
        self.window.title(constants.WINDOW_TITLE)
        self.window.config(padx=constants.WINDOW_PADDING, pady=constants.WINDOW_PADDING)

        self.miles_entry = tk.Entry(self.window, width=constants.ENTRY_WIDTH)
        self.miles_label = tk.Label(self.window, text=constants.LABEL_MILES)
        self.equal_label = tk.Label(self.window, text=constants.LABEL_EQUAL)
        self.result_label = tk.Label(self.window, text=constants.DEFAULT_RESULT)
        self.km_label = tk.Label(self.window, text=constants.LABEL_KM)
        self.calculate_button = tk.Button(
            self.window, text=constants.BUTTON_CALCULATE, command=self.button_clicked
        )

        pad = constants.WIDGET_PADDING
        self.miles_entry.grid(column=1, row=0, padx=pad, pady=pad)
        self.miles_label.grid(column=2, row=0, padx=pad, pady=pad)
        self.equal_label.grid(column=0, row=1, padx=pad, pady=pad)
        self.result_label.grid(column=1, row=1, padx=pad, pady=pad)
        self.km_label.grid(column=2, row=1, padx=pad, pady=pad)
        self.calculate_button.grid(column=1, row=2, padx=pad, pady=pad)
        self.miles_entry.focus()

    def button_clicked(self) -> None:
        """@brief Read the entry, convert it and show the kilometers in the result label."""
        try:
            result = convert_text(self.miles_entry.get())
        except ValueError:
            result = constants.MESSAGE_INVALID_INPUT
        self.result_label.config(text=result)

    def run(self) -> None:
        """@brief Show the window and handle events until it is closed."""
        self.window.mainloop()
