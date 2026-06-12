---
title: Putar Halaman PDF dengan Python
linktitle: Memutar Halaman PDF
type: docs
weight: 110
url: /id/python-net/rotate-pages/
description: Pelajari cara memutar halaman PDF dan mengubah orientasi halaman dengan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara memutar Halaman dalam PDF dengan Python
Abstract: Artikel ini menyediakan panduan tentang cara memperbarui atau mengubah orientasi halaman pada halaman dalam file PDF yang ada secara programatis menggunakan Python. Dengan memanfaatkan Aspose.PDF for Python via .NET, pengguna dapat dengan mudah beralih antara orientasi lanskap dan potret dengan menyesuaikan properti MediaBox halaman. Artikel ini menyertakan cuplikan kode Python yang menunjukkan cara mengiterasi halaman dalam dokumen PDF, memodifikasi dimensi dan posisi MediaBox mereka, serta menyesuaikan CropBox jika diperlukan. Selain itu, dijelaskan cara menetapkan sudut rotasi halaman menggunakan metode ‘rotate’ untuk mencapai orientasi yang diinginkan. Proses berakhir dengan menyimpan file PDF yang telah diperbarui.
---

Topik ini menjelaskan cara memperbarui atau mengubah orientasi halaman pada halaman dalam file PDF yang ada secara programatis dengan Python.

Gunakan halaman ini ketika Anda perlu mengubah halaman antara orientasi potret dan lanskap atau menerapkan sudut rotasi pada konten PDF yang ada.

## Ubah Orientasi Halaman

Fungsi ini memutar setiap halaman PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 derajat searah jarum jam menggunakan Aspose.PDF for Python.
Ini berguna untuk memperbaiki masalah orientasi halaman, seperti dokumen yang dipindai yang berada dalam posisi miring. PDF asli tetap tidak berubah, dan versi yang diputar disimpan sebagai file baru.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Ubah ukuran halaman PDF dalam Python](/pdf/id/python-net/change-page-size/)
- [Memotong halaman PDF di Python](/pdf/id/python-net/crop-pages/)
- [Dapatkan dan atur properti halaman PDF di Python](/pdf/id/python-net/get-and-set-page-properties/)