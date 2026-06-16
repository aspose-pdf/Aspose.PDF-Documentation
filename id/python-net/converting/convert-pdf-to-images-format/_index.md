---
title: Konversi PDF ke Format Gambar di Python
linktitle: Konversi PDF ke Gambar
type: docs
weight: 70
url: /id/python-net/convert-pdf-to-images-format/
lastmod: "2026-06-12"
description: Pelajari cara merender halaman PDF menjadi file TIFF, BMP, EMF, JPEG, PNG, GIF, dan SVG di Python dengan Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Konversi halaman PDF ke TIFF, PNG, JPEG, GIF, BMP, EMF, dan SVG di Python.
Abstract: Artikel ini menjelaskan cara mengonversi file PDF ke format gambar umum dengan Aspose.PDF for Python via .NET. Ini mencakup ekspor TIFF seluruh dokumen dengan `TiffDevice`, pembuatan gambar raster per halaman dengan subclass `ImageDevice` seperti `BmpDevice`, `JpegDevice`, `PngDevice`, `GifDevice`, dan `EmfDevice`, serta ekspor vektor ke SVG dengan `SvgSaveOptions`. Setiap bagian menyertakan langkah-langkah inti dan contoh Python yang diperlukan untuk menyimpan konten PDF sebagai output gambar.
---

## Python Mengonversi PDF ke Gambar

**Aspose.PDF for Python via .NET** mendukung beberapa cara untuk mengonversi konten PDF ke gambar. Pada praktiknya, kebanyakan alur kerja menggunakan salah satu dari dua opsi:

- pendekatan Device untuk merender halaman PDF ke format gambar raster
- pendekatan SaveOptions untuk mengekspor konten PDF ke SVG

Artikel ini menunjukkan cara mengonversi file PDF ke TIFF, BMP, EMF, JPEG, PNG, GIF, dan SVG.

Perpustakaan mencakup beberapa kelas rendering. `DocumentDevice` dirancang untuk konversi seluruh dokumen, sementara `ImageDevice` menargetkan halaman individu.

## Konversi PDF menggunakan kelas DocumentDevice

Gunakan `DocumentDevice` ketika Anda ingin merender seluruh PDF menjadi satu file TIFF multi‑halaman.

The [Perangkat Tiff](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) kelas didasarkan pada `DocumentDevice` dan menyediakan [proses](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) metode untuk mengonversi semua halaman dalam file PDF menjadi satu output TIFF.

{{% alert color="success" %}}
**Coba konversi PDF ke TIFF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["PDF ke TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF PDF ke TIFF dengan Aplikasi](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Konversi Halaman PDF menjadi Satu Gambar TIFF

Aspose.PDF for Python via .NET dapat merender setiap halaman dalam file PDF menjadi satu gambar TIFF.

Langkah: Konversi PDF ke TIFF di Python

1. Muat PDF sumber dengan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Buat [PengaturanTiff](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) dan [Perangkat Tiff](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) objek.
1. Konfigurasikan opsi TIFF seperti kompresi, kedalaman warna, dan penanganan halaman kosong.
1. Panggil [proses](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) metode untuk menulis file TIFF.

Cuplikan kode berikut menunjukkan cara mengonversi semua halaman PDF menjadi satu gambar TIFF.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## Konversi PDF menggunakan kelas ImageDevice

Gunakan `ImageDevice` ketika Anda membutuhkan output per halaman dalam format gambar raster.

`ImageDevice` adalah kelas dasar untuk `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, dan `EmfDevice`.

- The [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) class memungkinkan Anda mengonversi halaman PDF menjadi gambar BMP.
- The [Perangkat EMF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) kelas memungkinkan Anda mengonversi halaman PDF menjadi gambar EMF.
- The [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) kelas memungkinkan Anda mengonversi halaman PDF menjadi gambar JPEG.
- The [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) kelas memungkinkan Anda untuk mengonversi halaman PDF menjadi gambar PNG.
- The [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) kelas memungkinkan Anda mengonversi halaman PDF menjadi gambar GIF.

Alur kerja sama untuk setiap format: muat dokumen, buat perangkat yang sesuai, kemudian proses halaman yang diperlukan.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) mengekspos [proses](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) metode untuk merender halaman tertentu sebagai BMP. Kelas perangkat gambar lain mengikuti pola yang sama, sehingga Anda dapat mengubah format dengan mengubah kelas perangkat.

Tautan dan contoh kode berikut menunjukkan cara merender halaman PDF ke format gambar umum:

- [Konversi PDF ke BMP di Python](#convert-pdf-to-bmp)
- [Konversi PDF ke EMF di Python](#convert-pdf-to-emf)
- [Konversi PDF ke JPEG dalam Python](#convert-pdf-to-jpeg)
- [Mengonversi PDF ke PNG di Python](#convert-pdf-to-png)
- [Konversi PDF ke GIF dalam Python](#convert-pdf-to-gif)

Langkah: PDF ke Gambar (BMP, EMF, JPG, PNG, GIF) di Python

1. Muat file PDF dengan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Buat sebuah instance dari yang diperlukan [Perangkat Gambar](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) subkelas:
    - [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (untuk mengkonversi PDF ke BMP)
    - [Perangkat EMF](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (untuk mengonversi PDF ke EMF)
    - [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (untuk mengonversi PDF ke JPG)
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (untuk mengonversi PDF ke PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (untuk mengonversi PDF ke GIF)
1. Iterasi halaman yang ingin Anda ekspor.
1. Panggil [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) metode untuk menyimpan setiap halaman sebagai gambar.

### Konversi PDF ke BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Konversi PDF ke JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Konversi PDF ke PNG dengan font default

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Konversi PDF ke GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi PDF ke PNG secara online**

Sebagai contoh bagaimana aplikasi kami bekerja, silakan periksa fitur berikutnya.

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Cara mengonversi PDF ke PNG menggunakan App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Konversi PDF menggunakan kelas SaveOptions

Gunakan `SaveOptions` ketika Anda ingin mengekspor konten PDF ke SVG.

{{% alert color="success" %}}
**Coba konversi PDF ke SVG secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda ["PDF ke SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke SVG dengan Aplikasi](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** adalah format berbasis XML untuk grafik vektor dua dimensi. Karena SVG tetap berbasis vektor, format ini berguna ketika Anda membutuhkan output yang dapat diskalakan untuk web, UI, atau alur kerja desain.

File SVG berbasis teks, dapat dicari, dan mudah diproses lanjutan di alat lain.

Aspose.PDF for Python via .NET dapat mengonversi SVG ke PDF dan mengekspor halaman PDF ke SVG. Untuk konversi PDF-ke-SVG, buat sebuah [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objek dan berikan ke [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

Langkah-langkah berikut menunjukkan cara mengonversi file PDF ke SVG dengan Python.

Langkah: Mengonversi PDF ke SVG di Python

1. Muat PDF sumber menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Buat sebuah [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) objek dan konfigurasikan opsi yang diperlukan.
1. Panggil [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode dengan `SvgSaveOptions` instance untuk menulis output SVG.

### Konversi PDF ke SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## Konversi terkait

- [Konversi format gambar ke PDF](/pdf/id/python-net/convert-images-format-to-pdf/) ketika Anda perlu membangun kembali PDF dari JPG, PNG, TIFF, SVG, atau sumber gambar lainnya.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) untuk output yang ramah peramban alih-alih gambar raster.
- [Konversi PDF ke format lain](/pdf/id/python-net/convert-pdf-to-other-files/) untuk alur kerja ekspor EPUB, Markdown, teks, dan XPS.
