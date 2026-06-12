---
title: Ganti Nama Field Form
linktitle: Ganti Nama Field Form
type: docs
weight: 30
url: /id/python-net/rename-form-fields/
description: Contoh ini menunjukkan cara mengganti nama field form dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Ini memperlihatkan cara mengikat formulir PDF, memperbarui nama field yang ada secara programatis, dan menyimpan file yang telah dimodifikasi. Mengganti nama field membantu menstandarisasi struktur form, meningkatkan pemetaan data, dan menyederhanakan integrasi dengan alur kerja otomatis atau sistem eksternal.
lastmod: "2026-06-12"
---

Mengganti nama field form berguna saat menyelaraskan formulir PDF dengan konvensi penamaan internal atau menyiapkan dokumen untuk pemrosesan data terstruktur. Pada contoh ini, [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fasad dari [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) modul digunakan untuk mengikat PDF sumber dan menerapkan pemetaan yang menggantikan nama field lama dengan yang baru. Setelah memperbarui identifier field, dokumen disimpan dengan perubahan yang diterapkan.

1. Inisialisasi pdf_facades.Form() untuk berinteraksi dengan bidang formulir PDF.
1. Panggil \u0027bind_pdf()\u0027 untuk melampirkan dokumen PDF.
1. Buat daftar tuple yang berisi nama field lama dan nama baru yang bersesuaian.
1. Iterasi melalui pemetaan dan panggil 'rename_field()' untuk setiap entri.
1. Simpan Document yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
