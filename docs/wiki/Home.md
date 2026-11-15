**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Miles to Kilometer Converter

A small Tkinter application that converts miles to kilometers: type a distance, press Calculate and read the result.

![The converter after calculating 10 miles](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)


## What is it?

Day 27 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*. The window has an entry for the distance in miles, a label that shows the result in kilometers and a **Calculate** button. The conversion rule is kept apart from the window, so it can be tested without a display. The factor 1.609 and every text of the window are constants in `constants.py`. Text that is not a number shows "Enter a number" instead of a result.

## What the exercise teaches

- Building a window with Tkinter: `Tk`, `Entry`, `Label` and `Button`
- Placing the widgets in a grid with `grid`
- Running a function when a button is pressed, with the `command` argument
- Reading the text of an entry with `get` and showing a result by changing the text of a label with `config`
- Turning text into a number and handling text that is not a number
- Keeping the conversion rule free of the window, so that it can be tested without a display

## What it does

- An entry for the distance in miles and a **Calculate** button
- The result in kilometers, rounded to two decimals, using the factor 1.609
- The message "Enter a number" when the text is not a number
- Tests of the conversion that always run, and tests of the window that run when Tkinter and a display are available
- No runtime dependencies beyond the Python standard library

## Next

- [Getting Started](Getting-Started)
- [Project Documents](Project-Documents)
