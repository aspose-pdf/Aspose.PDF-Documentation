---
title: Buat Dokumen PDF N-Up
linktitle: Buat Dokumen PDF N-Up
type: docs
weight: 10
url: /id/python-net/create-n-up-pdf-document/
description: Pelajari cara membuat dokumen PDF N-Up sambil menangani potensi error dengan aman menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Tata Letak PDF N-Up di Python
Abstract: Pelajari cara menghasilkan tata letak PDF N-Up menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menggabungkan beberapa halaman dokumen PDF ke satu halaman menggunakan metode 'make_n_up' atau 'try_make_n_up' dari kelas PdfFileEditor.
---

Tata letak N-Up menempatkan beberapa halaman dokumen PDF ke dalam satu halaman dalam format grid. Tata letak ini sering digunakan untuk mencetak presentasi, handout, atau laporan di mana beberapa halaman dapat dilihat sekaligus.

Dengan menggunakan Aspose.PDF for Python, pengembang dapat dengan cepat membuat dokumen N-Up dengan menentukan jumlah baris dan kolom yang menentukan berapa banyak halaman asli yang muncul pada setiap halaman output.

Dalam cuplikan kode ini, metode 'make_n_up' dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas mengatur halaman PDF input ke dalam kisi 2 × 2, yang berarti empat halaman asli muncul pada satu halaman dalam dokumen output.

Dalam contoh yang ditunjukkan, tata letaknya menggunakan 2 baris dan 2 kolom, menghasilkan empat halaman per lembar:

1. Buka file PDF sumber.
1. Buat instance PdfFileEditor.
1. Tentukan jumlah baris dan kolom untuk tata letak N-Up.
1. Hasilkan PDF baru dengan halaman yang digabungkan.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    nup_maker.make_n_up(
        FileIO(infile), FileIO(outfile, "w"), 2, 2
    )  # 2 rows and 2 columns for N-Up layout
```

Aspose.PDF for Python via .NET memungkinkan Anda menghasilkan tata letak N-Up dengan kelas PdfFileEditor. Metode 'try_make_n_up' berfungsi serupa dengan make_n_up, tetapi alih-alih melemparkan pengecualian ketika suatu operasi gagal, ia mengembalikan nilai boolean yang menunjukkan apakah proses berhasil.

Tata letak N-Up mengatur beberapa halaman PDF pada satu halaman menggunakan grid yang ditentukan oleh baris dan kolom.

Metode 'try_make_n_up' menyediakan cara yang lebih aman untuk melakukan operasi ini karena:

- Mengembalikan True jika tata letak berhasil dibuat
- Mengembalikan False jika operasi gagal
- Tidak menginterupsi eksekusi program dengan pengecualian

Dalam contoh di bawah, dokumen diatur menggunakan grid 2 × 2, yang menempatkan empat halaman asli pada setiap halaman output.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create N-Up PDF Document
def try_create_nup_pdf_document(infile, outfile):
    # Create NUpMaker object
    nup_maker = pdf_facades.PdfFileEditor()
    # Make N-Up layout from input PDF file and save to output PDF file
    if not nup_maker.try_make_n_up(FileIO(infile), FileIO(outfile, "w"), 2, 2):
        print("Failed to create N-Up PDF document.")
```
