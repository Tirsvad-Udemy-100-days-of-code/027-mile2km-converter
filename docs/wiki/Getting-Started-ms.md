[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

## Keperluan

- Python 3.13 atau lebih baharu dengan Tkinter (pada Debian pakejnya ialah `python3-tk`)
- Tiada pakej masa larian; ujian menggunakan `pytest`, yang dipasang oleh tambahan `dev`

## Persediaan

Cipta persekitaran maya setempat bernama `.venv` dalam akar repositori, naik taraf `pip` di dalamnya dan pasang projek dengan alat ujian.

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

Keluar daripada persekitaran dengan `deactivate`.

## Jalankan

Dengan persekitaran aktif, dari akar repositori:

```bash
python -m mile2km
```

![Penukar pada permulaan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-start.png)

### Tukar jarak

1. Taip jarak dalam batu pada medan input.
2. Tekan **Calculate**.
3. Jarak dalam kilometer dipaparkan di sebelah **is equal to**.

![Penukar selepas menukar 10 batu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)

### Input tidak sah

Teks yang bukan nombor memaparkan "Enter a number" dan bukannya hasil.

## Ujian

Dengan persekitaran aktif:

```bash
python -m pytest
```

Ujian GUI dilangkau apabila Tkinter atau paparan tidak tersedia; ujian penukaran sentiasa dijalankan.

## Lesen

Kod ini dilesenkan di bawah the GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). Lihat fail `LICENSE`.
