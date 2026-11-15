[English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

# Kom godt i gang

## Krav

- Python 3.13 eller nyere med Tkinter (på Debian hedder pakken `python3-tk`)
- Ingen pakker ved kørsel; testene bruger `pytest`, som installeres med `dev`-udvidelsen

## Opsætning

Opret et lokalt virtuelt miljø med navnet `.venv` i repositoriets rod, opgradér `pip` i det og installér projektet med testværktøjerne.

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

Forlad miljøet med `deactivate`.

## Kør

Når miljøet er aktivt, fra repositoriets rod:

```bash
python -m mile2km
```

![Konverteren ved start](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-start.png)

### Omregn en afstand

1. Skriv en afstand i miles i indtastningsfeltet.
2. Tryk på **Calculate**.
3. Afstanden i kilometer vises ved siden af **is equal to**.

![Konverteren efter omregning af 10 miles](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)

### Ugyldigt input

Tekst, der ikke er et tal, viser "Enter a number" i stedet for et resultat.

## Tests

Når miljøet er aktivt:

```bash
python -m pytest
```

GUI-testene springes over, hvis Tkinter eller en skærm ikke er tilgængelig; omregningstestene kører altid.

## Licens

Koden er udgivet under licensen the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). Se filen `LICENSE`.
