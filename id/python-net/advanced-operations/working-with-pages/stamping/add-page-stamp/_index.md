---
title: Tambahkan Stempel Halaman ke PDF dengan Python
linktitle: Menambahkan Stempel Halaman
type: docs
weight: 30
url: /id/python-net/page-stamps-in-the-pdf-file/
description: Pelajari cara menambahkan stempel halaman PDF sebagai overlay atau latar belakang dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Stempel Halaman ke PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara menambahkan stempel halaman ke dokumen PDF menggunakan Aspose.PDF for Python. Stempel halaman memungkinkan Anda menambahkan overlay atau underlay konten—seperti logo, watermark, atau anotasi—ke halaman tertentu dalam PDF. Contoh ini menunjukkan cara membuka PDF yang sudah ada, membuat objek PdfPageStamp dari halaman PDF lain, mengkonfigurasinya sebagai stempel latar belakang, dan menerapkannya ke halaman tertentu. PDF yang telah distempel kemudian disimpan sebagai dokumen baru. Teknik ini berguna untuk branding, watermarking, atau menekankan konten tingkat halaman dalam alur kerja PDF otomatis.
---

Aspose.PDF for Python via .NET menunjukkan cara menerapkan stempel halaman (watermark atau overlay) ke halaman tertentu dalam PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Stempel halaman dapat berupa halaman PDF yang ada yang digunakan sebagai lapisan latar belakang atau latar depan (lihat [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Ini berguna untuk menambahkan logo, watermark, atau konten halaman berulang lainnya.

1. Buka dokumen PDF menggunakan `ap.Document()` (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Buat sebuah `PdfPageStamp` objek menggunakan halaman PDF atau file untuk digunakan sebagai stempel (lihat [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Atur properti stempel, misalnya, `background = True` menempatkannya di belakang konten.
1. Tambahkan stempel ke halaman tertentu menggunakan `document.pages[page_number].add_stamp(page_stamp)` (lihat [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Simpan PDF yang telah dimodifikasi ke file output yang ditentukan menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## Topik Stamping Terkait

- [Cap halaman PDF dengan Python](/pdf/id/python-net/stamping/)
- [Tambahkan nomor halaman ke PDF dengan Python](/pdf/id/python-net/add-page-number/)
- [Tambahkan cap gambar ke PDF di Python](/pdf/id/python-net/image-stamps-in-pdf-page/)
- [Tambahkan cap teks ke PDF di Python](/pdf/id/python-net/text-stamps-in-the-pdf-file/)