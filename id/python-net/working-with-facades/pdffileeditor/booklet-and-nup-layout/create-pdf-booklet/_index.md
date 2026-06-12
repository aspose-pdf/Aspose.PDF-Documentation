---
title: Buat PDF Booklet
linktitle: Buat PDF Booklet
type: docs
weight: 20
url: /id/python-net/create-pdf-booklet/
description: Hasilkan PDF bergaya buklet dari dokumen yang ada menggunakan Aspose.PDF for Python
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat PDF Booklet dari PDF yang Ada Menggunakan Python
Abstract: Pelajari cara menghasilkan PDF bergaya buklet dari dokumen yang ada menggunakan Aspose.PDF for Python. Contoh ini menunjukkan cara menggunakan kelas PdfFileEditor untuk mengatur ulang halaman sehingga dapat dicetak dan dilipat sebagai buklet. Metode ini secara otomatis mengurutkan halaman untuk menghasilkan tata letak buklet yang tepat.
---

Membuat dokumen bergaya buklet adalah kebutuhan umum saat menyiapkan PDF untuk pencetakan. Dalam tata letak buklet, halaman diatur ulang sehingga ketika dicetak dan dilipat, mereka muncul dalam urutan yang benar.

Menggunakan Aspose.PDF for Python, pengembang dapat dengan mudah mengonversi PDF standar menjadi buklet menggunakan the [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas. Metode ‘make_booklet’ secara otomatis menyusun ulang halaman dokumen masukan dan menghasilkan PDF baru yang dioptimalkan untuk pencetakan booklet.

1. Buka dokumen PDF yang ada.
1. Buat instance PdfFileEditor.
1. Gunakan metode make_booklet untuk menyusun ulang halaman.
1. Simpan output sebagai file PDF siap booklet.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Potongan kode ini menunjukkan cara menggunakan metode 'try_make_booklet' dari [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) kelas untuk menyusun ulang halaman untuk pencetakan buku kecil tanpa melemparkan pengecualian jika operasi gagal.

Tata letak buku kecil menyusun ulang halaman sehingga ketika dicetak dan dilipat, dokumen terbaca dalam urutan yang benar. Mengotomatisasi proses ini memastikan hasil yang konsisten dan menghilangkan kebutuhan akan penyusunan ulang halaman secara manual.

Metode 'try_make_booklet' bekerja mirip dengan 'make_booklet', tetapi dengan perbedaan penting:

- 'make_booklet' melempar pengecualian jika operasi gagal.
- 'try_make_booklet' mengembalikan True atau False, memungkinkan pengembang mengelola kesalahan dengan lebih aman.

1. Buka dokumen PDF yang ada.
1. Buat instance PdfFileEditor.
1. Coba Membuat Booklet.
1. Tangani Hasil.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
