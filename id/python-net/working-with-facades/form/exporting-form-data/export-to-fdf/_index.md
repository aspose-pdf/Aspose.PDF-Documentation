---
title: Ekspor ke FDF
linktitle: Ekspor ke FDF
type: docs
weight: 10
url: /id/python-net/export-to-fdf/
description: Contoh ini menjelaskan cara mengekspor data bidang formulir PDF ke file FDF (Forms Data Format) menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengakses data formulir interaktif melalui facade Form, mengikat dokumen PDF sumber, dan menyimpan nilai yang diekstrak ke dalam aliran FDF.
lastmod: "2026-06-12"
---

FDF adalah format ringan yang dirancang khusus untuk menyimpan dan mentransfer data formulir PDF tanpa menyematkan seluruh dokumen. Dalam contoh ini, sebuah [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objek diinisialisasi dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul, memungkinkan pengembang berinteraksi dengan bidang AcroForm dan mengekspor nilainya.

1. Buat instance pdf_facades.Form() untuk bekerja dengan bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan dokumen PDF yang berisi formulir.
1. Gunakan 'open(')' untuk membuat aliran biner yang dapat ditulis untuk file FDF.
1. Ekspor Data Formulir. Panggil 'export_fdf()' untuk mengekstrak dan menyimpan semua nilai bidang formulir.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, "wb") as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)
```
