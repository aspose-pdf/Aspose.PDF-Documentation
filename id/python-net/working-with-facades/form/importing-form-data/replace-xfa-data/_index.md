---
title: Ganti Data XFA
linktitle: Ganti Data XFA
type: docs
weight: 50
url: /id/python-net/replace-xfa-data/
description: Contoh ini menunjukkan cara mengganti data formulir XFA yang ada dalam PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengaitkan dokumen PDF berbasis XFA, memuat data baru dari file XFA eksternal, dan memperbarui konten formulir secara programatis.
lastmod: "2026-06-12"
---

Formulir XFA (XML Forms Architecture) menyimpan datanya dalam format XML di dalam struktur PDF. Dalam contoh ini, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengaitkan sebuah PDF dan mengganti dataset XFA yang ada menggunakan aliran XML eksternal. Setelah menerapkan data baru, PDF yang diperbarui disimpan sebagai file terpisah.

1. Inisialisasi pdf_facades.Form() untuk mengelola data formulir XFA.
1. Panggil ‘bind_pdf()’ untuk melampirkan PDF yang berisi formulir XFA.
1. Gunakan 'FileIO()' untuk membaca file XML XFA.
1. Panggil 'set_xfa_data()' untuk memperbarui PDF dengan konten XFA baru.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, "r") as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)
```
