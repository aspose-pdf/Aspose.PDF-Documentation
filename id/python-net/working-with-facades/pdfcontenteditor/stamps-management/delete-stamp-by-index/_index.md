---
title: Hapus Stempel Berdasarkan Indeks
linktitle: Hapus Stempel Berdasarkan Indeks
type: docs
weight: 50
url: /id/python-net/delete-stamp-by-index/
description: Contoh ini membuat dua stempel karet pada halaman 2. Setelah itu, sebuah stempel dapat dihapus dengan menentukan indeksnya.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Stempel Karet Berdasarkan Indeks dalam PDF Menggunakan PdfContentEditor di Python
Abstract: Contoh ini menunjukkan cara menghapus anotasi stempel karet dalam PDF menggunakan indeksnya dengan Aspose.PDF for Python via the Facades API. Ini memperlihatkan cara menambahkan beberapa stempel dan kemudian menghapus salah satunya berdasarkan urutan mereka pada halaman.
---

Ketika ada beberapa stempel karet pada sebuah halaman, Anda dapat menghapus yang spesifik dengan menggunakan indeksnya. Metode delete_stamp() memungkinkan penghapusan anotasi sesuai urutan mereka, yang berguna ketika Anda tidak melacak ID stempel tetapi mengetahui urutannya.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF input.
1. Hubungkan file PDF input ke instance PdfContentEditor menggunakan bind_pdf(infile).
1. Panggil 'delete_stamp(1, [2, 3])' untuk menghapus stamp dengan indeks 1 dari halaman 2 dan 3.
1. Simpan dokumen PDF yang telah dimodifikasi ke file output menggunakan save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
