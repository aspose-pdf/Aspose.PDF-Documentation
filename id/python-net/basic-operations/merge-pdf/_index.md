---
title: Gabungkan File PDF di Python
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/python-net/merge-pdf/
description: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan halaman PDF menggunakan Python
Abstract: Artikel ini membahas kebutuhan umum untuk menggabungkan beberapa file PDF menjadi satu dokumen, sebuah proses yang berharga untuk mengatur dan mengoptimalkan penyimpanan serta berbagi konten PDF. Artikel ini mengeksplorasi penggunaan Aspose.PDF for Python via .NET untuk secara efisien menggabungkan file PDF, dengan mengakui bahwa menggabungkan PDF di Python dapat menjadi tantangan tanpa pustaka pihak ketiga. Artikel ini menyediakan panduan langkah demi langkah untuk mengkonkatenasi file PDF — membuat dokumen baru, menggabungkan file, dan menyimpan dokumen yang telah digabungkan. Sebuah cuplikan kode menunjukkan implementasinya menggunakan Aspose.PDF, menyoroti kemampuan perpustakaan untuk menyederhanakan proses penggabungan. Selain itu, artikel ini memperkenalkan Aspose.PDF Merger, alat daring untuk menggabungkan PDF, memungkinkan pengguna menjelajahi fungsionalitasnya dalam lingkungan berbasis web.
---

## Gabungkan File PDF menggunakan Python dan DOM

Untuk menggabungkan dua file PDF:

1. Buat Dokumen Baru.
1. Gabungkan File PDF
1. Simpan Dokumen yang Digabung

Menggabungkan beberapa dokumen PDF menjadi satu file:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Contoh Langsung

[Penggabung Aspose.PDF](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja fungsi penggabungan presentasi.

[![Penggabung Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

