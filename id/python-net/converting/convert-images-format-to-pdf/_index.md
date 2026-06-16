---
title: Konversi Format Gambar ke PDF dalam Python
linktitle: Konversi Gambar ke PDF
type: docs
weight: 60
url: /id/python-net/convert-images-format-to-pdf/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, dan format gambar lainnya ke PDF dalam Python dengan Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Cara Mengonversi Gambar ke PDF dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi berbagai format gambar ke PDF menggunakan Python, khususnya memanfaatkan pustaka Aspose.PDF untuk Python via .NET. Artikel ini mencakup berbagai format gambar termasuk BMP, CGM, DICOM, EMF, GIF, PNG, SVG, dan TIFF. Setiap bagian merinci langkah‑langkah yang diperlukan untuk melakukan konversi, menyediakan cuplikan kode untuk menggambarkan prosesnya. Misalnya, mengonversi BMP ke PDF melibatkan pembuatan dokumen PDF baru, mendefinisikan penempatan gambar, menyisipkan gambar, dan menyimpan dokumen. Demikian pula, untuk format seperti CGM, DICOM, dan lainnya, opsi pemuatan khusus serta langkah‑langkah pemrosesan dijelaskan. Artikel ini juga menyoroti keuntungan menggunakan Aspose.PDF untuk tugas semacam itu, seperti dukungannya untuk berbagai metode enkoding dan kemampuan memproses gambar satu bingkai maupun multi‑bingkai.
---

## Konversi terkait

- [Konversi PDF ke format gambar](/pdf/id/python-net/convert-pdf-to-images-format/) ketika Anda membutuhkan alur kerja terbalik.
- [Konversi HTML ke PDF](/pdf/id/python-net/convert-html-to-pdf/) untuk konten web dan sumber MHTML.
- [Konversi format file lain ke PDF](/pdf/id/python-net/convert-other-files-to-pdf/) untuk EPUB, XPS, teks, dan input non-gambar lainnya.

## Konversi Gambar Python ke PDF

**Aspose.PDF for Python via .NET**  memungkinkan Anda untuk mengonversi berbagai format gambar menjadi file PDF. Perpustakaan kami menunjukkan contoh kode untuk mengonversi format gambar paling populer, seperti - BMP, CGM, DICOM, EMF, JPG, PNG, SVG dan format TIFF.

## Konversi BMP ke PDF

Konversi file BMP ke dokumen PDF menggunakan pustaka **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> gambar adalah file dengan ekstensi. BMP mewakili file Gambar Bitmap yang digunakan untuk menyimpan gambar digital bitmap. Gambar ini tidak bergantung pada adapter grafis dan juga disebut format file bitmap independen perangkat (DIB).

Anda dapat mengonversi BMP ke file PDF dengan Aspose.PDF for Python via .NET API. Oleh karena itu, Anda dapat mengikuti langkah-langkah berikut untuk mengonversi gambar BMP:

Langkah-langkah Mengonversi BMP ke PDF dengan Python:

1. Buat dokumen PDF kosong.
1. Buat halaman yang Anda butuhkan, misalnya, kami membuat A4, tetapi Anda dapat menentukan format Anda sendiri.
1. Menempatkan gambar (dari infile) di dalam halaman menggunakan persegi panjang yang ditentukan.
1. Simpan dokumen sebagai PDF.

Jadi cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi BMP ke PDF secara online**

Aspose mempersembahkan aplikasi daring untuk Anda ["BMP ke PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi BMP ke PDF menggunakan Aplikasi](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Konversi CGM ke PDF

Konversi CGM (Computer Graphics Metafile) menjadi PDF (atau format lain yang didukung) menggunakan Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> adalah ekstensi file untuk format Computer Graphics Metafile yang umum digunakan dalam aplikasi CAD (computer-aided design) dan grafik presentasi. CGM adalah format grafik vektor yang mendukung tiga metode enkoding berbeda: biner (terbaik untuk kecepatan baca program), berbasis karakter (menghasilkan ukuran file paling kecil dan memungkinkan transfer data yang lebih cepat) atau enkoding teks jelas (memungkinkan pengguna membaca dan memodifikasi file dengan editor teks).

Periksa cuplikan kode berikut untuk mengonversi file CGM ke format PDF.

Langkah-langkah untuk Mengonversi CGM ke PDF dalam Python:

1. Tentukan Jalur File
1. Atur Opsi Muat untuk CGM.
1. Konversi CGM ke PDF
1. Pesan Konversi Cetak

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi DICOM ke PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format adalah standar industri medis untuk pembuatan, penyimpanan, transmisi, dan visualisasi gambar medis digital serta dokumen pasien yang diperiksa.

**Aspose.PDF for Python** memungkinkan Anda mengonversi gambar DICOM dan SVG, tetapi karena alasan teknis untuk menambahkan gambar Anda perlu menentukan jenis file yang akan ditambahkan ke PDF.

Potongan kode berikut menunjukkan cara mengonversi file DICOM ke format PDF dengan Aspose.PDF. Anda harus memuat gambar DICOM, menempatkan gambar pada halaman dalam file PDF dan menyimpan output sebagai PDF. Kami menggunakan pustaka pydicom tambahan untuk mengatur dimensi gambar ini. Jika Anda ingin memposisikan gambar pada halaman, Anda dapat melewati potongan kode ini.

1. Muat file DICOM.
1. Ekstrak dimensi gambar.
1. Cetak ukuran gambar.
1. Buat dokumen PDF baru.
1. Siapkan gambar DICOM untuk PDF.
1. Atur ukuran halaman PDF dan margin.
1. Tambahkan gambar ke halaman.
1. Simpan PDF.
1. Cetak Pesan Konversi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi DICOM ke PDF secara daring**

Aspose mempersembahkan aplikasi daring untuk Anda ["DICOM ke PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF DICOM ke PDF menggunakan Aplikasi](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Konversi EMF ke PDF

<abbr title="Enhanced metafile format">EMF</abbr> menyimpan gambar grafis secara independen perangkat. Metafile EMF terdiri dari catatan berukuran variabel dalam urutan kronologis yang dapat merender gambar yang disimpan setelah parsing pada perangkat keluaran apa pun.

Potongan kode berikut menunjukkan cara mengonversi EMF ke PDF dengan Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi EMF ke PDF secara online**

Aspose mempersembahkan aplikasi daring untuk Anda ["EMF ke PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi EMF ke PDF menggunakan Aplikasi](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Ubah GIF menjadi PDF

Konversi file GIF ke dokumen PDF menggunakan perpustakaan **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> dapat menyimpan data terkompresi tanpa kehilangan kualitas dalam format tidak lebih dari 256 warna. Format GIF yang independen dari perangkat keras dikembangkan pada tahun 1987 (GIF87a) oleh CompuServe untuk mentransmisikan gambar bitmap melalui jaringan.

Jadi cuplikan kode berikut mengikuti langkah-langkah ini dan menunjukkan cara mengonversi BMP ke PDF menggunakan Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi GIF ke PDF secara online**

Aspose mempersembahkan aplikasi daring untuk Anda ["GIF ke PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF GIF ke PDF menggunakan Aplikasi](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Konversi PNG ke PDF

**Aspose.PDF for Python via .NET** mendukung fitur untuk mengonversi gambar PNG ke format PDF. Periksa potongan kode berikut untuk melaksanakan tugas Anda.

<abbr title="Portable Network Graphics">PNG</abbr> merujuk pada jenis format file gambar raster yang menggunakan kompresi lossless, yang membuatnya populer di antara penggunanya.

Anda dapat mengonversi gambar PNG ke PDF menggunakan langkah-langkah berikut:

1. Buat Dokumen PDF Baru.
1. Definisikan Penempatan Gambar.
1. Simpan PDF.
1. Cetak Pesan Konversi.

Selain itu, cuplikan kode di bawah ini menunjukkan cara mengonversi PNG ke PDF dengan Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi PNG ke PDF secara daring**

Aspose mempersembahkan aplikasi daring untuk Anda ["PNG ke PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi Aspose.PDF PNG ke PDF menggunakan App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Konversi SVG ke PDF

**Aspose.PDF for Python via .NET** menjelaskan cara mengonversi gambar SVG ke format PDF dan cara mendapatkan dimensi file SVG sumber.

Scalable Vector Graphics (SVG) adalah sekumpulan spesifikasi dari format file berbasis XML untuk grafik vektor dua dimensi, baik statis maupun dinamis (interaktif atau animasi). Spesifikasi SVG adalah standar terbuka yang telah dikembangkan oleh World Wide Web Consortium (W3C) sejak tahun 1999.

<abbr title="Scalable Vector Graphics">SVG</abbr> Gambar dan perilakunya didefinisikan dalam berkas teks XML. Ini berarti bahwa mereka dapat dicari, diindeks, di‑skrip, dan bila diperlukan, dikompresi. Sebagai berkas XML, gambar SVG dapat dibuat dan diedit dengan editor teks apa pun, tetapi seringkali lebih mudah membuatnya dengan program menggambar seperti Inkscape.

{{% alert color="success" %}}
**Coba konversi format SVG ke PDF secara online**

Aspose.PDF for Python via .NET mempersembahkan aplikasi online Anda [“SV ke PDF”](https://products.aspose.app/pdf/conversion/svg-to-pdf), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi SVG ke PDF dengan Aspose.PDF](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Potongan kode berikut menunjukkan proses mengonversi file SVG ke format PDF dengan Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi TIFF ke PDF

**Aspose.PDF** format file didukung, baik itu gambar TIFF satu frame maupun multi-frame. Artinya Anda dapat mengonversi gambar TIFF ke PDF.

TIFF atau TIF, Tagged Image File Format, mewakili citra raster yang dimaksudkan untuk penggunaan pada berbagai perangkat yang mematuhi standar format file ini. Gambar TIFF dapat berisi beberapa frame dengan gambar yang berbeda. Format file Aspose.PDF juga didukung, baik itu gambar TIFF satu frame maupun multi-frame.

Anda dapat mengonversi TIFF ke PDF dengan cara yang sama seperti format file raster grafis lainnya:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Konversi CDR ke PDF

Potongan kode berikut menunjukkan cara memuat file CorelDRAW (CDR) dan menyimpannya sebagai PDF menggunakan 'CdrLoadOptions' di Aspose.PDF for Python via .NET.

1. Buat 'CdrLoadOptions()' untuk mengkonfigurasi bagaimana file CDR harus dimuat.
1. Inisialisasi objek Document dengan file CDR dan opsi pemuatan.
1. Simpan dokumen sebagai PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Ubah JPEG ke PDF

Contoh ini menunjukkan cara mengonversi JPEG ke file PDF menggunakan Aspose.PDF for Python via .NET.

1. Buat dokumen PDF baru.
1. Tambahkan halaman baru.
1. Tentukan persegi penempatan (ukuran A4: 595x842 poin).
1. Masukkan gambar ke halaman.
1. Simpan PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
