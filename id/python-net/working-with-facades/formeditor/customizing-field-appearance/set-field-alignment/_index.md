---
title: Atur Penyelarasan Bidang
linktitle: Atur Penyelarasan Bidang
type: docs
weight: 30
url: /id/python-net/set-field-alignment/
description: Contoh ini menunjukkan cara mengatur penyelarasan teks FormField dalam dokumen PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Penyelarasan Teks untuk FormField PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka dokumen PDF, mengatur penyelarasan field tertentu menggunakan kelas FormEditor, dan menyimpan PDF yang telah diperbarui. Contoh ini mengatur penyelarasan teks field bernama "First Name" ke tengah.
---

FormField PDF sering memerlukan penyelarasan teks yang disesuaikan untuk menjaga tata letak yang konsisten dan profesional. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatik mengatur penyelarasan konten teks FormField.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas, dalam kombinasi dengan [FormFieldFacade](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formfieldfacade/) constants, memungkinkan pengembang untuk memodifikasi penyelarasan field formulir yang ada secara programatis.

1. Buka dokumen PDF yang ada.
1. Buat objek FormEditor.
1. Atur penyelarasan field bernama "First Name" ke tengah.
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


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception(
            "Failed to set field alignment. Field may not support alignment."
        )
```
