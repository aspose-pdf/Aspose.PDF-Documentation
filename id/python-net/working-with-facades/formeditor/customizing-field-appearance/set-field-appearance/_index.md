---
title: Atur Penampilan Bidang
linktitle: Atur Penampilan Bidang
type: docs
weight: 50
url: /id/python-net/set-field-appearance/
description: Contoh ini menunjukkan cara mengubah penampilan visual bidang formulir PDF menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur Penampilan Bidang Formulir PDF Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuka PDF, mengatur penampilan bidang formulir menggunakan kelas FormEditor, dan menyimpan dokumen yang diperbarui. Contoh ini mengatur penampilan bidang bernama "First Name" menjadi tidak terlihat menggunakan flag AnnotationFlags.INVISIBLE.
---

Bidang formulir PDF mendukung flag penampilan yang mengendalikan visibilitas, kemampuan cetak, dan interaktivitas. Menggunakan Aspose.PDF for Python, pengembang dapat memodifikasi flag tersebut secara programatik untuk bidang formulir tertentu.

Menggunakan [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas, pengembang dapat memodifikasi flag ini untuk menyembunyikan, menampilkan, atau menyesuaikan perilaku bidang formulir dalam PDF interaktif.

1. Buka dokumen PDF yang ada.
1. Buat objek FormEditor.
1. Atur tampilan bidang bernama "First Name" menjadi tidak terlihat.
1. Simpan dokumen yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance(
        "First Name", ap.annotations.AnnotationFlags.INVISIBLE
    ):
        raise Exception(
            "Failed to set field appearance. Field may not support appearance flags."
        )

    # Save updated document
    form_editor.save(outfile)
```
