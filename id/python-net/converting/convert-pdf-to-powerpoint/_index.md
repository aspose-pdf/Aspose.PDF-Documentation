---
title: Konversi PDF ke PowerPoint dengan Python
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/python-net/convert-pdf-to-powerpoint/
description: Pelajari cara mengonversi PDF ke PowerPoint dengan Python, termasuk PDF ke PPTX, slide sebagai gambar, dan resolusi gambar khusus dengan Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Konversi PDF ke slide PowerPoint PPTX dengan Python
Abstract: Artikel ini menunjukkan cara mengonversi file PDF menjadi presentasi PowerPoint dengan Aspose.PDF for Python via .NET. Artikel ini mencakup konversi PDF ke PPTX, mengonversi slide menjadi gambar, dan mengatur resolusi gambar untuk output presentasi.
---

## Konversi PDF ke PowerPoint dengan Python

**Aspose.PDF for Python via .NET** memungkinkan Anda mengonversi file PDF menjadi presentasi PowerPoint PPTX dari kode Python.

Gunakan alur kerja ini ketika Anda perlu mengubah kembali laporan PDF, dek slide, brosur, atau handout menjadi file PowerPoint. Selama konversi, halaman PDF individual dikonversi menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke PPTX, teks dapat dirender sebagai teks yang dapat dipilih yang dapat Anda perbarui di PowerPoint. Untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) kelas. Lewati sebuah `PptxSaveOptions` objek sebagai argumen kedua ke [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

## Konversi PDF ke PPTX di Python

Untuk mengonversi PDF ke PPTX, gunakan langkah kode berikut.

Langkah: Konversi PDF ke PowerPoint di Python

1. Buat sebuah instance dari [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Buat sebuah instance dari [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) kelas.
1. Panggil [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Konversi PDF ke PPTX dengan Slide sebagai Gambar

{{% alert color="success" %}}
**Coba konversi PDF ke PowerPoint secara daring**

Aspose.PDF menyediakan layanan daring ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) aplikasi di mana Anda dapat menguji kualitas konversi.


[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Jika Anda perlu mengonversi PDF yang dapat dicari menjadi PPTX sebagai gambar alih-alih teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) kelas. Untuk mencapai ini, atur properti [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) dari [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) kelas menjadi 'true' seperti yang ditunjukkan pada contoh kode berikut.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Konversi PDF ke PPTX dengan Resolusi Gambar Kustom

Metode ini mengonversi dokumen PDF menjadi file PowerPoint (PPTX) sambil mengatur resolusi gambar khusus (300 DPI) untuk kualitas yang lebih baik.

1. Muat PDF ke dalam objek 'ap.Document'.
1. Buat instance 'PptxSaveOptions'.
1. Atur properti 'image_resolution' ke 300 DPI untuk rendering berkualitas tinggi.
1. Simpan PDF sebagai file PPTX menggunakan opsi penyimpanan yang telah ditentukan.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Konversi terkait

- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) untuk output dokumen yang dapat diedit alih-alih slide.
- [Konversi PDF ke Excel](/pdf/id/python-net/convert-pdf-to-excel/) ketika PDF sumber berisi data bisnis yang penuh tabel.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) untuk alur kerja publikasi yang siap untuk browser.
