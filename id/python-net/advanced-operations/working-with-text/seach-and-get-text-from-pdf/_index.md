---
title: Cari dan Ekstrak Teks PDF dengan Python
linktitle: Cari dan Dapatkan Teks
type: docs
weight: 60
url: /id/python-net/search-and-get-text-from-pdf/
description: Pelajari cara mencari, memeriksa, dan mengekstrak teks dari dokumen PDF dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cari teks PDF dan periksa fragmen yang diekstrak dengan Python
Abstract: Artikel ini menjelaskan cara mencari dan mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup `TextAbsorber` dan `TextFragmentAbsorber`, termasuk ekstraksi berbasis wilayah, pencarian spesifik halaman, pencocokan frasa, serta inspeksi posisi teks dan properti font.
---

## Cari Teks dari PDF

Cari dan ekstrak teks dari area persegi panjang yang ditetapkan dalam dokumen PDF menggunakan `TextAbsorber` kelas. Ini menggunakan mode pemformatan teks murni untuk output bersih, tidak terformat, yang berguna untuk mengekstrak konten dari wilayah terstruktur seperti header, footer, atau area tabel. Dengan menggabungkan `TextExtractionOptions` dan `TextSearchOptions` dengan batasan persegi panjang, Anda dapat mengontrol di mana dan bagaimana teks diekstrak.

Gunakan halaman ini ketika Anda perlu memeriksa konten teks PDF, mengekstrak teks untuk analisis, atau memeriksa posisi dan format fragmen teks yang cocok.

1. Muat file PDF menggunakan 'ap.Document'.
1. Konfigurasikan Opsi Ekstraksi Teks.
1. Definisikan Area Pencarian dengan Batasan Persegi Panjang.
1. Buat dan Konfigurasi TextAbsorber.
1. Proses Semua Halaman dalam Dokumen.
1. Ambil dan Tampilkan Teks yang Diekstrak.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Cari Teks dari Halaman PDF tertentu

Cari dan ekstrak teks dari halaman dan wilayah tertentu dalam PDF menggunakan Aspose.PDF’s TextAbsorber. Ini menargetkan halaman 2 dokumen dan hanya mengekstrak teks yang ditemukan dalam area persegi panjang yang telah ditentukan.
Dengan menggabungkan TextExtractionOptions (untuk kontrol pemformatan) dan TextSearchOptions (untuk pembatasan area), Anda dapat melakukan ekstraksi teks yang tepat, khusus per halaman, secara efisien.

1. Muat Dokumen PDF.
1. Atur Opsi Ekstraksi Teks.
1. Batasi ekstraksi teks ke area persegi panjang tertentu pada halaman.
1. Buat dan Konfigurasi TextAbsorber.
1. Proses Halaman Tertentu.
1. Ambil dan Tampilkan Teks yang Diekstrak.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Menganalisis dan Mengekstrak Properti Fragmen Teks Terperinci dari PDF

Berbeda dengan TextAbsorber, yang mengekstrak teks mentah, TextFragmentAbsorber menyediakan informasi terperinci tingkat rendah tentang setiap fragmen teks—seperti posisinya, atribut font, warna, dan detail penyematan.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Proses Semua Halaman dalam Dokumen.
1. Iterasi Melalui Fragmen Teks yang Diekstrak.
1. Cetak Informasi Teks Dasar.
1. Cetak Detail Font dan Pemformatan.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Cari Frasa Teks Spesifik pada Satu Halaman PDF

Cari frasa teks tertentu dalam satu halaman dokumen PDF menggunakan TextFragmentAbsorber. Tidak seperti mencari di seluruh dokumen, pendekatan ini membatasi pencarian hanya pada satu halaman, membuatnya lebih efisien untuk mengonfirmasi keberadaan dan lokasi teks di area yang ditargetkan seperti header, footer, atau bagian konten spesifik.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Frasa Pencarian.
1. Terapkan Absorber pada Halaman Tertentu.
1. Iterasi Atas Fragmen yang Ditemukan.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pencarian Teks Halaman-per-Halaman Berurutan dengan Hasil Kumulatif

Cari teks secara bertahap di beberapa halaman dokumen PDF menggunakan TextFragmentAbsorber dari Aspose.PDF.
Tidak seperti pencarian satu halaman atau seluruh dokumen, pendekatan ini memungkinkan Anda memproses halaman secara berurutan, mengumpulkan hasil secara progresif, dan menganalisis fragmen teks dengan konteks khusus halaman. Metode ini ideal untuk dokumen besar atau alur kerja pemrosesan progresif.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dan Atur Frasa Pencarian.
1. Proses Halaman Pertama. Cari hanya halaman 1. Cetak teks, nomor halaman, dan posisi. Berikan hasil yang terisolasi per halaman untuk kejelasan.
1. Proses Halaman Berikutnya Secara Berurutan. Pindah ke halaman 2 dan secara opsional lanjutkan melalui sisa dokumen. 'absorber.visit()' memastikan akumulasi hasil dari semua halaman yang dikunjungi. Mencetak hasil pencarian kumulatif, menampilkan teks dan lokasi.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Pencarian Frasa Target dalam Area Persegi Panjang

Cari frasa tertentu dalam PDF sambil membatasi pencarian ke area persegi panjang tertentu pada satu halaman.
Dengan menggabungkan pencarian frasa dengan batasan spasial, Anda dapat menemukan konten secara tepat di wilayah yang ditentukan tanpa harus memindai seluruh halaman atau dokumen. Ini sangat berguna untuk formulir, header, footer, atau laporan terstruktur di mana konten muncul di lokasi yang dapat diprediksi.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Frasa dan Batas Persegi Panjang
1. Gunakan Absorber pada Halaman 2. Membatasi pemrosesan ke halaman 2, mengurangi perhitungan yang tidak perlu. Memastikan pencarian bersifat spesifik halaman.
1. Iterasi Melalui Fragmen yang Ditemukan dan Cetak

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pencarian Pola Teks pada PDF Menggunakan Ekspresi Reguler

Cari pola teks dalam PDF menggunakan ekspresi reguler. Dengan mengaktifkan mode regex di TextFragmentAbsorber, Anda dapat menemukan pola kompleks seperti angka, tanggal, harga, koordinat, atau format teks khusus. Fungsi ini membatasi pencarian ke halaman tertentu, membuatnya efisien untuk ekstraksi terarah data terstruktur.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Pola Regex.
1. Terapkan Absorber ke Halaman 2. Membatasi pencarian ke halaman 2 untuk efisiensi dan presisi. Hanya teks pada halaman ini yang dianalisis.
1. Iterasi Melalui Fragmen yang Ditemukan. Mencetak fragmen teks yang cocok dan koordinatnya. Menyediakan informasi lokasi yang tepat untuk pola yang diekstrak.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Konversi Kecocokan Teks menjadi Tautan Hiper di PDF Menggunakan TextFragmentAbsorber

Cari frasa teks tertentu dalam PDF dan ubah menjadi hyperlink yang dapat diklik. Dengan menggunakan TextFragmentAbsorber bersama pola regex, ia menemukan kata target dan menerapkan gaya visual (warna dan garis bawah) serta tautan interaktif.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber dengan Pola Regex.
1. Terapkan Absorber ke Halaman 1.
1. Gaya dan Tambahkan Hyperlink ke Kecocokan.
1. Simpan PDF yang Dimodifikasi.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Cari dan Identifikasi Teks Bergaya dalam PDF Menggunakan TextFragmentAbsorber

Cari fragmen teks dalam PDF berdasarkan properti pemformatannya, bukan berdasarkan isinya. Dengan menggunakan TextFragmentAbsorber, ia mengidentifikasi teks dengan gaya tertentu, seperti teks tebal.

1. Muat Dokumen PDF.
1. Inisialisasi TextFragmentAbsorber.
1. Terapkan Absorber ke Halaman 1.
1. Periksa Fragmen Teks Berdasarkan Pemformatan. Memeriksa gaya font untuk pemformatan tebal.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Penyorotan Teks Visual di Halaman PDF

Fungsi ini menggabungkan pengenalan teks dan rendering dalam satu alur kerja. Ia tidak hanya mengekstrak teks tetapi juga memvisualisasikannya dengan menyorot fragmen, segmen, dan karakter dalam kotak berwarna pada gambar PNG setiap halaman.

Contoh kami melakukan visualisasi teks lanjutan pada PDF dengan:

- mencari semua fragmen teks yang terlihat menggunakan ekspresi reguler
- men-render setiap halaman PDF ke dalam gambar PNG beresolusi tinggi
- menggambar persegi panjang berwarna di sekitar fragmen teks, segmen teks, dan karakter individu

1. Atur Resolusi Gambar Output. Setiap halaman PDF dikonversi menjadi gambar PNG dengan resolusi 150 DPI.
1. Buka PDF dan Inisialisasi Text Absorber.
1. Proses Setiap Halaman. Terapkan absorber pada setiap halaman. Kumpulkan semua fragmen teks yang terdeteksi serta posisi geometrisnya.
1. Konversi Halaman ke Aliran PNG.
1. Siapkan Objek Grafik untuk Menggambar.
1. Terapkan Transformasi Koordinat. Konversi koordinat PDF ke piksel gambar.
1. Gambar Persegi Panjang untuk Elemen Teks.
1. Simpan Hasil.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## Topik Teks Terkait

- [Bekerja dengan teks dalam PDF menggunakan Python](/pdf/id/python-net/working-with-text/)
- [Ganti teks dalam PDF menggunakan Python](/pdf/id/python-net/replace-text-in-pdf/)
- [Tambahkan tooltip ke teks PDF di Python](/pdf/id/python-net/pdf-tooltip/)
- [Menambahkan teks ke PDF](/pdf/id/python-net/add-text-to-pdf-file/)