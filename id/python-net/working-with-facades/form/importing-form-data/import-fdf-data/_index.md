---
title: Impor Data FDF
linktitle: Impor Data FDF
type: docs
weight: 10
url: /id/python-net/import-fdf-data/
description: Contoh ini menunjukkan cara mengimpor data formulir dari file FDF ke dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengikat dokumen PDF, membaca nilai bidang formulir dari aliran FDF, dan secara otomatis mengisi bidang yang sesuai.
lastmod: "2026-06-12"
---

FDF (Forms Data Format) adalah format ringan yang digunakan untuk menyimpan dan mentransfer nilai bidang formulir PDF tanpa menyertakan seluruh dokumen. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk memuat formulir PDF dan mengimpor data bidang dari file FDF eksternal. Setelah proses impor, PDF yang diperbarui disimpan sebagai file baru.

1. Inisialisasi pdf_facades.Form() untuk bekerja dengan bidang formulir PDF interaktif.
1. Panggil \u0027bind_pdf()\u0027 untuk melampirkan templat formulir PDF.
1. Gunakan 'open()' untuk membaca file FDF dalam mode biner.
1. Panggil 'import_fdf()' untuk mengisi bidang PDF dengan data dari file FDF.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, "rb") as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
