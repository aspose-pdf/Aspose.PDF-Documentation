---
title: Impor dan Ekspor Anotasi menggunakan Python
linktitle: Impor dan Ekspor Anotasi
type: docs
weight: 80
url: /id/python-net/import-export-annotations/
description: Pelajari cara mengimpor anotasi dari satu PDF dan mengekspornya ke dalam dokumen PDF baru menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfer anotasi PDF antar dokumen dalam Python.
Abstract: Artikel ini menjelaskan cara menyalin anotasi dari PDF sumber dan mengekspornya ke dalam dokumen PDF baru menggunakan Aspose.PDF for Python via .NET. Panduan ini membagi proses menjadi langkah‑langkah kecil, termasuk memuat file sumber, membuat dokumen tujuan, menambahkan halaman, menyalin anotasi dari halaman pertama, dan menyimpan hasilnya.
---

Artikel ini menunjukkan cara mengimpor anotasi dari PDF yang ada dan mengekspornya ke dokumen PDF baru menggunakan Aspose.PDF for Python via .NET.

Contoh ini membaca anotasi dari halaman pertama file sumber, membuat PDF baru, menambahkan halaman kosong, dan menyalin setiap anotasi ke halaman baru tersebut. Pendekatan ini berguna ketika Anda perlu memindahkan komentar, penandaan, atau catatan tinjauan ke dalam dokumen output terpisah.

## Muat PDF sumber

Buat sebuah `Document` objek untuk file input yang sudah berisi anotasi. Objek ini memberikan akses ke koleksi halaman dan anotasi yang disimpan pada setiap halaman.

```python
source_document = ap.Document(infile)
```

## Buat PDF tujuan

Selanjutnya, buat dokumen PDF kosong yang akan menerima anotasi yang diimpor. Pada tahap ini, dokumen tujuan tidak berisi halaman apa pun.

```python
destination_document = ap.Document()
```

## Tambahkan halaman untuk anotasi yang diekspor

Karena anotasi harus menjadi milik sebuah halaman, tambahkan halaman baru ke dokumen tujuan sebelum menyalin apa pun.

```python
page = destination_document.pages.add()
```

## Salin anotasi dari halaman sumber

Iterasi melalui koleksi anotasi pada halaman pertama PDF sumber dan tambahkan setiap anotasi ke halaman baru dalam dokumen tujuan.

Argumen kedua dalam `page.annotations.add(annot, True)` memberitahu Aspose.PDF untuk menyalin anotasi ke halaman tujuan alih-alih hanya menggunakan kembali referensi objek yang ada.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Simpan dokumen output

Setelah semua anotasi disalin, simpan dokumen tujuan untuk membuat file PDF akhir.

```python
destination_document.save(outfile)
```

## Contoh lengkap

Kode berikut menggabungkan semua langkah menjadi satu fungsi yang dapat digunakan kembali:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Topik Terkait

- [Anotasi Interaktif](/python-net/interactive-annotations/)
- [Anotasi Penandaan](/python-net/markup-annotations/)
- [Anotasi Media](/python-net/media-annotations/)
- [Anotasi Keamanan](/python-net/security-annotations/)
- [Anotasi Bentuk](/python-net/shape-annotations/)
- [Anotasi Berbasis Teks](/python-net/text-based-annotations/)
- [Anotasi Watermark](/python-net/watermark-annotations/)
