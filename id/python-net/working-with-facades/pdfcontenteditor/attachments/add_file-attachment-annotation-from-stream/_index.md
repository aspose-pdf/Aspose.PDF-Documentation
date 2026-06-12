---
title: Tambahkan Anotasi Lampiran File Dari Stream
linktitle: Tambahkan Anotasi Lampiran File Dari Stream
type: docs
weight: 40
url: /id/python-net/add-file-attachment-annotation-from-stream/
description: Contoh ini memuat PDF, membaca file eksternal ke dalam memori stream, menambahkan anotasi lampiran file ke halaman pertama, dan menyimpan dokumen yang telah dimodifikasi.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Anotasi Lampiran File ke PDF dari Stream dalam Python
Abstract: Contoh ini menunjukkan cara membuat anotasi lampiran file dalam PDF menggunakan stream file dengan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menentukan posisi anotasi, mengatur deskripsi, menyertakan nilai opacity, dan menyimpan dokumen yang telah dimodifikasi.
---

Anotasi lampiran file memungkinkan penyematan file sebagai ikon interaktif dalam halaman PDF. Dengan menggunakan pendekatan berbasis stream, Anda dapat melampirkan file secara dinamis tanpa bergantung pada jalur file fisik. Metode ini juga mendukung penyesuaian tampilan anotasi, termasuk opacity.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Baca File Lampiran sebagai Stream.
1. Tambahkan Anotasi Lampiran File.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
