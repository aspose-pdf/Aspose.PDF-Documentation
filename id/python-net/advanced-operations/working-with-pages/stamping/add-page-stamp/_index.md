---
title: Menambahkan Cap Halaman ke PDF dengan Python
linktitle: Menambahkan Cap Halaman
type: docs
weight: 30
url: /id/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET memungkinkan Anda menambahkan Cap Halaman ke file PDF Anda.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan Cap Halaman ke PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara menambahkan cap halaman ke dokumen PDF menggunakan Aspose.PDF for Python. Cap halaman memungkinkan Anda menimpa atau menempatkan konten—seperti logo, watermark, atau anotasi—pada halaman tertentu dalam PDF. Contoh ini menunjukkan cara membuka PDF yang ada, membuat objek PdfPageStamp dari halaman PDF lain, mengonfigurasinya sebagai cap latar belakang, dan menerapkannya ke halaman tertentu. PDF yang telah dicap kemudian disimpan sebagai dokumen baru. Teknik ini berguna untuk branding, watermarking, atau menekankan konten tingkat halaman dalam alur kerja PDF otomatis.
---

Aspose.PDF for Python via .NET menunjukkan cara menerapkan cap halaman (watermark atau overlay) ke halaman tertentu dalam PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Cap halaman dapat berupa halaman PDF yang ada yang digunakan sebagai lapisan latar belakang atau latar depan (lihat [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)). Ini berguna untuk menambahkan logo, watermark, atau konten halaman yang berulang lainnya.

1. Buka dokumen PDF menggunakan `ap.Document()` (lihat [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Buat objek `PdfPageStamp` menggunakan halaman PDF atau file yang akan digunakan sebagai cap (lihat [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. Atur properti cap, misalnya `background = True` untuk menempatkannya di belakang konten.
1. Tambahkan cap ke halaman tertentu menggunakan `document.pages[page_number].add_stamp(page_stamp)` (lihat [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. Simpan PDF yang telah dimodifikasi ke file output yang ditentukan menggunakan [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

