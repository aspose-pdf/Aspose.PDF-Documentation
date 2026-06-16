---
title: Konversi PDF/A dan PDF/UA ke PDF dalam Python
linktitle: Konversi PDF/A dan PDF/UA ke PDF
type: docs
weight: 120
url: /id/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-06-12"
description: Pelajari cara menghapus kepatuhan PDF/A dan PDF/UA dari file PDF dalam Python dengan Aspose.PDF for Python via .NET dan menyimpannya sebagai dokumen PDF standar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengonversi PDF/A dan PDF/UA ke PDF standar dalam Python
Abstract: Artikel ini menjelaskan cara menghapus kepatuhan PDF/A dan PDF/UA dari dokumen PDF berbasis standar menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup skenario di mana Anda mungkin membutuhkan PDF standar alih-alih file arsip atau yang dibatasi aksesibilitas, dan menunjukkan cara menyimpan hasil setelah menghapus metadata dan pembatasan kepatuhan.
---

Gunakan halaman ini ketika Anda perlu mengonversi PDF berbasis standar, seperti PDF/A atau PDF/UA, kembali menjadi dokumen PDF biasa untuk penyuntingan, pemrosesan, atau distribusi lebih lanjut.

PDF yang mematuhi standar berguna untuk alur kerja pengarsipan, pencetakan, dan aksesibilitas, tetapi dalam beberapa kasus Anda mungkin perlu menghapus kepatuhan tersebut sebelum mengintegrasikan file ke sistem atau jalur proses lain. Aspose.PDF for Python via .NET memungkinkan Anda melakukan hal itu secara programatik dan kemudian menyimpan hasilnya sebagai file PDF standar.

## Ubah PDF/A menjadi PDF

Contoh ini menghapus metadata dan pembatasan kepatuhan PDF/A dari sebuah PDF sehingga dokumen dapat disimpan kembali sebagai file PDF biasa.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Panggil 'remove_pdfa_compliance()' untuk menghapus semua pengaturan kepatuhan dan metadata yang terkait dengan PDF/A.
1. Simpan PDF hasil ke jalur output.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## Menghapus kepatuhan PDF/UA

Contoh ini menunjukkan cara menghapus kepatuhan terkait PDF/UA sehingga dokumen dapat disimpan sebagai PDF standar untuk alur kerja yang tidak spesifik aksesibilitas.

1. Muat dokumen PDF menggunakan 'ap.Document()'.
1. Panggil 'document.remove_pdfa_compliance()' untuk menghapus semua pembatasan atau pengaturan kepatuhan PDF/A.
1. Simpan PDF yang telah dimodifikasi ke 'path_outfile'.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## Kapan menggunakan alur kerja ini

- Hapus pengaturan kepatuhan sebelum mengirim dokumen ke alur alat yang tidak memerlukan pembatasan PDF/A atau PDF/UA.
- Permudah pemrosesan dokumen hilir ketika metadata arsip atau aksesibilitas tidak lagi diperlukan.
- Normalisasi PDF masukan sebelum mengekspornya ke format lain.

## Konversi terkait

- [Ubah PDF menjadi PDF/A, PDF/E, dan PDF/X](/pdf/id/python-net/convert-pdf-to-pdf_x/) jika Anda memerlukan alur kerja sebaliknya dan ingin membuat PDF yang mematuhi standar.
- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) untuk output dokumen yang dapat disunting setelah menghapus batasan kepatuhan.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) untuk output yang ramah browser dari file PDF standar.
