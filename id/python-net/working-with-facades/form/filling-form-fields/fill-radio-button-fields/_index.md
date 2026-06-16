---
title: Isi Bidang Tombol Pilihan
linktitle: Isi Bidang Tombol Pilihan
type: docs
weight: 30
url: /id/python-net/fill-radio-button-fields/
description: Contoh ini menunjukkan cara mengisi bidang tombol pilihan secara programatis dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengikat dokumen PDF, memilih opsi tombol pilihan berdasarkan indeks, dan menyimpan file yang diperbarui.
lastmod: "2026-06-12"
---

Tombol pilihan memungkinkan pengguna memilih satu opsi dari grup yang telah ditentukan, seperti bidang jenis kelamin atau preferensi. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengikat PDF sumber dan menetapkan opsi yang dipilih berdasarkan nilai indeksnya. Setelah opsi yang diinginkan dipilih, dokumen yang dimodifikasi disimpan.

1. Inisialisasi pdf_facades.Form() untuk mengelola bidang formulir PDF.
1. Panggil 'bind_pdf()' untuk melampirkan PDF yang berisi bidang tombol pilihan.
1. Gunakan 'fill_field()' untuk memilih opsi pertama (indeks 0).
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill Radio Button Fields
def fill_radio_button_fields(infile, outfile):
    """Fill radio button fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill radio button fields by name
    pdf_form.fill_field("gender", 0)  # Select male option (index 0)
    # pdf_form.fill_field("gender", 1) # Select female option (index 1)

    # Save updated PDF
    pdf_form.save(outfile)
```
