[English](Home) · [Dansk](Home-da) · **Bahasa Melayu**

# Miles to Kilometer Converter

Aplikasi Tkinter kecil yang menukar batu (mile) kepada kilometer: taip jarak, tekan Calculate dan baca hasilnya.

![Penukar selepas menukar 10 batu](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-mile2km-converter/raw/branch/main/docs/images/converter-result.png)


## Apakah ini?

Hari ke-27 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Tetingkap ini mempunyai medan input untuk jarak dalam batu, satu label yang memaparkan hasil dalam kilometer dan butang **Calculate**. Peraturan penukaran diasingkan daripada tetingkap, jadi ia boleh diuji tanpa paparan. Faktor 1.609 dan setiap teks tetingkap ialah pemalar dalam `constants.py`. Teks yang bukan nombor memaparkan "Enter a number" dan bukannya hasil.

## Apa yang diajar oleh latihan ini

- Membina tetingkap dengan Tkinter: `Tk`, `Entry`, `Label` dan `Button`
- Meletakkan widget dalam grid dengan `grid`
- Menjalankan fungsi apabila butang ditekan, dengan argumen `command`
- Membaca teks medan input dengan `get` dan memaparkan hasil dengan menukar teks label menggunakan `config`
- Menukar teks kepada nombor dan mengendalikan teks yang bukan nombor
- Memisahkan peraturan penukaran daripada tetingkap, supaya ia boleh diuji tanpa paparan

## Apa yang dilakukannya

- Medan input untuk jarak dalam batu dan butang **Calculate**
- Hasil dalam kilometer, dibundarkan kepada dua tempat perpuluhan, dengan faktor 1.609
- Mesej "Enter a number" apabila teks bukan nombor
- Ujian penukaran yang sentiasa dijalankan, dan ujian tetingkap yang dijalankan apabila Tkinter dan paparan tersedia
- Tiada kebergantungan semasa larian selain pustaka standard Python

## Seterusnya

- [Bermula](Getting-Started-ms)
- [Dokumen Projek](Project-Documents-ms)
