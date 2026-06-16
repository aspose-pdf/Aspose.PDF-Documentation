---
title: Impor Data XFDF
linktitle: Impor Data XFDF
type: docs
weight: 20
url: /id/python-net/import-xfdf-data/
description: Contoh ini menunjukkan cara mengimpor data formulir dari file XFDF ke dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengikat dokumen PDF, membaca data XFDF berbasis XML melalui aliran file, dan secara otomatis mengisi bidang formulir yang cocok. Mengimpor data XFDF memungkinkan pertukaran data formulir yang efisien dan mendukung alur kerja dokumen otomatis yang bergantung pada format XML terstruktur.
lastmod: "2026-06-12"
---

XFDF (XML Forms Data Format) adalah representasi XML dari data formulir PDF yang dirancang untuk interoperabilitas dan pertukaran data. Dalam contoh ini, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengikat formulir PDF dan mengimpor nilai bidang dari file XFDF eksternal. Setelah mengimpor data, PDF yang diperbarui disimpan sebagai dokumen baru.

1. Inisialisasi pdf_facades.Form() untuk berinteraksi dengan bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan templat formulir PDF.
1. Gunakan 'open()' untuk membaca file XFDF.
1. Panggil 'import_xfdf()' untuk mengisi bidang PDF dengan nilai dari file XFDF.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
