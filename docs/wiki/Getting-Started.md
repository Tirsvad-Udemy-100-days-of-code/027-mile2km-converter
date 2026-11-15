**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

## Requirements

- Python 3.13 or newer with Tkinter (on Debian the package is `python3-tk`)
- No runtime packages; the tests use `pytest`, which is installed by the `dev` extra

## Setup

Create a local virtual environment named `.venv` in the repository root, upgrade `pip` inside it and install the project with the test tools.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Linux Debian

```bash
sudo apt install python3 python3-venv python3-tk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## Run

With the environment active, from the repository root:

```bash
python -m mile2km
```

![The converter at start](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-start.png)

### Convert a distance

1. Type a distance in miles in the entry field.
2. Press **Calculate**.
3. The distance in kilometers is shown next to **is equal to**.

![The converter after calculating 10 miles](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)

### Invalid input

Text that is not a number shows "Enter a number" instead of a result.

## Tests

With the environment active:

```bash
python -m pytest
```

The GUI tests are skipped when Tkinter or a display is not available; the conversion tests always run.

## Licence

The code is licensed under the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See the `LICENSE` file.
