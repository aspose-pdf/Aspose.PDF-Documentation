---
title: Isi Kolom Teks
linktitle: Isi Kolom Teks
type: docs
weight: 10
url: /id/python-net/fill-text-fields/
description: Contoh ini menunjukkan cara mengisi otomatis kolom teks dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini menunjukkan cara memuat dokumen PDF, mengisi kolom formulir tertentu berdasarkan nama, dan menyimpan berkas yang diperbarui.
lastmod: "2026-06-12"
---

Mengisi kolom teks secara programatik memungkinkan aplikasi menggunakan kembali templat PDF dan menyisipkan konten dinamis tanpa pengeditan manual. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasade dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengikat formulir PDF dan memperbarui beberapa bidang seperti nama, alamat, dan email. Setelah menetapkan nilai, PDF yang dimodifikasi disimpan sebagai dokumen baru.

1. Inisialisasi 'pdf_facades.Form()' untuk mengelola operasi bidang formulir.
1. Gunakan 'bind_pdf()' untuk melampirkan PDF masukan yang berisi kolom teks.
1. Panggil 'fill_field()' untuk memasukkan data ke bidang seperti nama, alamat, dan email.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Text Fields
def fill_text_fields(infile, outfile):
    """Fill text fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill text fields by name
    pdf_form.fill_field("name", "John Doe")
    pdf_form.fill_field("address", "123 Main St, Anytown, USA")
    pdf_form.fill_field("email", "john.doe@example.com")

    # Save updated PDF
    pdf_form.save(outfile)
```
