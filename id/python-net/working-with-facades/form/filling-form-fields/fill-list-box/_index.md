---
title: Isi Kotak Daftar
linktitle: Isi Kotak Daftar
type: docs
weight: 40
url: /id/python-net/fill-list-box/
description: Contoh ini menunjukkan cara mengisi kotak daftar dan bidang multi‑pilih secara programatis dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengikat dokumen PDF, memilih nilai dalam bidang formulir berbasis daftar, dan menyimpan file yang telah diperbarui.
lastmod: "2026-06-12"
---

Kotak daftar dan bidang multi‑pilih memungkinkan pengguna memilih satu atau beberapa nilai dari sekumpulan opsi yang telah ditentukan. Dalam contoh ini, the [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) digunakan untuk mengakses formulir PDF dan menetapkan nilai yang dipilih ke bidang favorite_colors. Setelah opsi yang diinginkan dipilih, dokumen yang diperbarui disimpan.

1. Inisialisasi 'pdf_facades.Form()' untuk mengelola dan memperbarui bidang formulir.
1. Panggil 'bind_pdf()' untuk melampirkan PDF sumber yang berisi kotak daftar atau bidang multi‑pilih.
1. Gunakan 'fill_field()' untuk memilih nilai dari opsi yang tersedia.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Fill List Box / Multi-Select Fields
def fill_list_box_fields(infile, outfile):
    """Fill list box and multi-select fields in PDF form."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Fill list box / multi-select fields by name
    pdf_form.fill_field("favorite_colors", "Red")

    # Save updated PDF
    pdf_form.save(outfile)
```
