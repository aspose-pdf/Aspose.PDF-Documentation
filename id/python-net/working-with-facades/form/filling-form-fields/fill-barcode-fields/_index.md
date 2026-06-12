---
title: Isi Bidang Kode Batang
linktitle: Isi Bidang Kode Batang
type: docs
weight: 50
url: /id/python-net/fill-barcode-fields/
description: Contoh ini menunjukkan cara mengisi bidang kode batang secara programatik dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara mengaitkan dokumen PDF, menetapkan nilai ke bidang kode batang, dan menyimpan file yang diperbarui.
lastmod: "2026-06-12"
---

Bidang kode batang dalam formulir PDF memungkinkan informasi yang terkode disimpan dan ditampilkan secara visual sebagai kode batang. Dalam contoh ini, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengakses bidang formulir dan menetapkan nilai kode batang. Setelah data diisi, PDF disimpan dengan konten kode batang yang diperbarui.

1. Inisialisasi 'pdf_facades.Form()' untuk mengelola interaksi formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan PDF yang berisi bidang kode batang.
1. Gunakan 'fill_field()' untuk menetapkan nilai kode batang.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Barcode Fields
def fill_barcode_fields(infile, outfile):
    """Fill barcode fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill barcode fields by name
    pdf_form.fill_field("product_barcode", "123456789012")

    # Save updated PDF
    pdf_form.save(outfile)
```
