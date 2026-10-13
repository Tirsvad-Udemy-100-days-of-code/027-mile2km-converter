"""Smoke tests of the Tkinter window; skipped when tkinter or a display is unavailable."""

from collections.abc import Iterator

import pytest

# Skip the whole module before tkinter is imported: it is missing on headless runners,
# where the import raises a plain ImportError (libtk8.6.so), not ModuleNotFoundError.
pytest.importorskip("tkinter", exc_type=ImportError)

import tkinter as tk

from mile2km import constants
from mile2km.gui import ConverterWindow


@pytest.fixture(scope="module")
def root() -> Iterator[tk.Tk]:
    # One Tk root per module: creating several in a row fails intermittently on Windows.
    try:
        tk_root = tk.Tk()
    except tk.TclError:
        pytest.skip("no display available")
    tk_root.withdraw()
    yield tk_root
    tk_root.destroy()


@pytest.fixture
def window(root: tk.Tk) -> Iterator[ConverterWindow]:
    yield ConverterWindow(root)
    for child in root.winfo_children():
        child.destroy()


def test_window_has_the_assignment_title(window: ConverterWindow) -> None:
    assert window.window.title() == constants.WINDOW_TITLE


def test_button_click_shows_kilometers(window: ConverterWindow) -> None:
    window.miles_entry.insert(0, "10")
    window.calculate_button.invoke()
    assert window.result_label.cget("text") == "16.09"


def test_button_click_with_invalid_text_shows_a_message(
    window: ConverterWindow,
) -> None:
    window.miles_entry.insert(0, "ten")
    window.calculate_button.invoke()
    assert window.result_label.cget("text") == constants.MESSAGE_INVALID_INPUT
