"""@file __main__.py
@brief Entry point: `python -m mile2km` starts the converter window.
"""

from mile2km.gui import ConverterWindow


def main() -> None:
    """@brief Create the converter window and run it until it is closed."""
    ConverterWindow().run()


if __name__ == "__main__":
    main()
