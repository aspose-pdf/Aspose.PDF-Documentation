---
title: Salin Field Luar
linktitle: Salin Field Luar
type: docs
weight: 30
url: /id/python-net/copy-outer-field/
description: Contoh ini menunjukkan cara menyalin field formulir dari satu dokumen PDF ke dokumen lain menggunakan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salin Field Form PDF dari Dokumen Lain Menggunakan Python
Abstract: Artikel ini menjelaskan cara membuat dokumen PDF baru, menyalin field "First Name" dari PDF sumber ke halaman 1 pada koordinat (200, 600), dan menyimpan dokumen target yang diperbarui.
---

Kadang-kadang, formulir PDF memerlukan penggunaan kembali bidang dari satu dokumen ke dokumen lain. Dengan menggunakan Aspose.PDF for Python, pengembang dapat secara programatis menyalin bidang formulir dari PDF sumber ke PDF target.

The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) kelas menyediakan metode 'copy_outer_field', yang menyalin sebuah bidang dari dokumen sumber ke dokumen target pada halaman dan koordinat yang ditentukan.

Kode tersebut membuat PDF baru (target), menambahkan sebuah halaman, dan kemudian menyalin sebuah bidang dari PDF yang ada (sumber) ke dokumen target pada koordinat yang ditentukan.

1. Buat dokumen PDF target baru.
1. Tambahkan setidaknya satu halaman ke PDF target.
1. Simpan dokumen target yang kosong.
1. Buat objek FormEditor dan kaitkan ke PDF target.
1. Salin bidang 'First Name' dari PDF sumber ke halaman 1 pada (200, 600).
1. Simpan PDF target yang diperbarui.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Harap dicatat:**

Tanda tangan metode 'copy_outer_field' terlihat seperti ini:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – bidang yang ingin Anda duplikat.
- 'new_field_name' – nama bidang baru.
- 'page_number' – halaman tempat bidang baru akan muncul.
- x, y – koordinat pada halaman tersebut.

page_number diharapkan menjadi bilangan bulat positif yang sesuai dengan halaman yang ada dalam PDF (indeks dimulai dari 1).

Jika Anda memberikan parameter negatif, misalnya:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

Program kemudian akan kembali ke parameter sebelumnya.
