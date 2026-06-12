---
title: Salin Field Dalam
linktitle: Salin Field Dalam
type: docs
weight: 20
url: /id/python-net/copy-inner-field/
description: Salin Form Field PDF ke Posisi Baru Menggunakan Python dengan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salin Form Field PDF ke Posisi Baru Menggunakan Python
Abstract: Contoh ini menunjukkan cara menyalin form field yang ada ke posisi baru dalam dokumen PDF menggunakan Aspose.PDF for Python. Kode membuka PDF, menduplikasi sebuah field ke halaman dan koordinat yang ditentukan, dan menyimpan dokumen yang diperbarui.
---

Formulir PDF sering memerlukan duplikasi bidang sambil mempertahankan format dan perilaku asli. Dengan menggunakan Aspose.PDF for Python, pengembang dapat menyalin bidang yang ada ke posisi baru pada halaman yang sama atau halaman lain secara programatis.

Artikel ini menjelaskan cara menyalin bidang bernama 'First Name' ke bidang baru yang disebut 'First Name Copy' pada halaman 2 dengan koordinat tertentu (x=200, y=600), menghasilkan PDF dengan bidang yang diposisikan baru.

1. Buka formulir PDF yang ada.
1. Buat objek FormEditor.
1. Hubungkan dokumen PDF ke FormEditor.
1. Salin bidang 'First Name' ke bidang baru 'First Name Copy' pada halaman 2 dengan koordinat (200, 600).
1. Simpan dokumen yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Harap dicatat:**

Signature metode 'copy_inner_field' terlihat seperti ini:

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – bidang yang ingin Anda duplikat.
- 'new_field_name' – nama field baru.
- 'page_number' – halaman tempat field baru akan muncul.
- x, y – koordinat pada halaman tersebut.

page_number diharapkan berupa bilangan bulat positif yang sesuai dengan halaman yang ada dalam PDF (indeks berbasis 1).

Jika Anda memberikan parameter negatif, misalnya:

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

Program kemudian akan mengatur ulang ke parameter sebelumnya.
