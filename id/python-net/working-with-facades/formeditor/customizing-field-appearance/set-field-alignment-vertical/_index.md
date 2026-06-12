---
title: Atur Penjajaran Field Secara Vertikal
linktitle: Atur Penjajaran Field Secara Vertikal
type: docs
weight: 40
url: /id/python-net/set-field-alignment-vertical/
description: Contoh ini menunjukkan cara mengatur penjajaran vertikal dari sebuah form field dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Penjajaran Vertikal untuk Form Field PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka PDF, mengatur penjajaran vertikal untuk sebuah field menggunakan kelas FormEditor, dan menyimpan PDF yang diperbarui. Contoh ini mengatur penjajaran vertikal dari field bernama "First Name" ke bagian bawah area field.
---

Form field PDF dapat berisi teks yang memerlukan penjajaran vertikal yang tepat untuk tampilan yang konsisten dan profesional. Dengan menggunakan Aspose.PDF for Python, pengembang dapat memodifikasi secara programatis penjajaran vertikal dari form field.
Penjajaran vertikal memungkinkan pengembang mengontrol apakah teks field muncul di bagian atas, tengah, atau bawah kotak pembatas field, meningkatkan tata letak dan keterbacaan data form.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas dan the [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) konstanta, pengembang dapat menyesuaikan perataan vertikal secara programatis untuk mencapai tata letak formulir yang konsisten:

1. Buka dokumen PDF yang ada.
1. Buat objek FormEditor.
1. Atur perataan vertikal dari bidang bernama "First Name" ke bawah.
1. Simpan dokumen yang telah dimodifikasi.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Attempt to set vertical alignment of the "First Name" field to bottom
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field vertical alignment. Field may not support vertical alignment."
        )
```
