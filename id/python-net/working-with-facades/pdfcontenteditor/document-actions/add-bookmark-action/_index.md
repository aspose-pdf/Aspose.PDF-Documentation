---
title: Tambahkan Aksi Bookmark
linktitle: Tambahkan Aksi Bookmark
type: docs
weight: 10
url: /id/python-net/add-bookmark-action/
description: Contoh ini mengikat PDF input, membuat sebuah bookmark berlabel "PdfContentEditor Bookmark" yang menavigasi ke halaman 1, dan menyimpan dokumen yang diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Bookmark dengan Aksi Navigasi dalam PDF Menggunakan Python
Abstract: Contoh ini menunjukkan cara menambahkan bookmark dengan aksi navigasi ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara mengatur teks bookmark, tampilannya, dan aksi yang mengarahkan pengguna ke halaman tertentu.
---

Bookmark menyediakan navigasi cepat dalam dokumen PDF. Menggunakan [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), Anda dapat secara programatik membuat bookmark dan menetapkan aksi seperti menavigasi ke sebuah halaman. Anda juga dapat menyesuaikan tampilan bookmark, termasuk opsi warna dan gaya seperti tebal atau mirik.

1. Buat objek PdfContentEditor.
1. Gabungkan PDF input.
1. Definisikan properti Bookmark.
1. Tetapkan tindakan Bookmark.
1. Simpan Document yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark_action(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add a bookmark action to navigate to page 1
    content_editor.create_bookmarks_action(
        "PdfContentEditor Bookmark",
        apd.Color.blue,
        True,
        False,
        "",
        "GoTo",
        "1",
    )
    # Save updated document
    content_editor.save(outfile)
```