---
title: Ekstrak Teks dari PDF menggunakan Python
linktitle: Ekstrak Teks dari PDF
type: docs
weight: 10
url: /python-cpp/extract-text/
description: Bagian ini menjelaskan cara mengekstrak teks dari dokumen PDF menggunakan pustaka Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari PDF tidaklah mudah. Tidak banyak pembaca PDF yang dapat mengekstrak teks dari gambar PDF atau PDF yang dipindai. Namun, alat **Aspose.PDF for Python via C++** memungkinkan Anda untuk dengan mudah mengekstrak teks dari semua file PDF.

Periksa cuplikan kode dan ikuti langkah-langkah untuk mengekstrak teks dari PDF Anda:

1. Impor pustaka Aspose.PDF untuk Python
1. Buat objek ekstraktor baru, yang digunakan untuk mengekstrak teks dan gambar dari dokumen PDF.
1. Hubungkan objek ekstraktor ke file PDF, yang merupakan sumber ekstraksi.
1. Ekstrak semua teks dari dokumen PDF dan masukkan ke dalam beberapa variabel.

1. Lakukan apapun, cetak teks yang diekstraksi ke konsol, cari beberapa fragmen, dll.

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```