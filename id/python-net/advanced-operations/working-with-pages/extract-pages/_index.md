---
title: Ekstrak Halaman PDF dengan Python
linktitle: Mengekstrak Halaman PDF
type: docs
weight: 80
url: /id/python-net/extract-pages/
description: Pelajari cara mengekstrak satu atau beberapa halaman PDF ke dalam file baru menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengekstrak halaman PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara mengekstrak halaman dari file PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menyalin satu halaman atau beberapa halaman ke dalam dokumen baru dengan menggunakan indeks halaman berbasis 1 dan PageCollection API.
---

## Ekstrak Halaman Tunggal dari PDF

Ekstrak halaman tertentu dari dokumen PDF dan simpan sebagai file baru. Menggunakan pustaka Aspose.PDF, skrip menyalin halaman yang diinginkan ke PDF baru, meninggalkan dokumen asli tidak berubah. Ini berguna untuk membagi PDF atau mengisolasi halaman penting untuk didistribusikan.

1. Muat PDF sumber menggunakan the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) untuk menampung halaman yang diekstrak.
1. Tambahkan yang diinginkan [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari dokumen sumber ke PDF baru menggunakan dokumen tujuan’s [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - Dalam contoh ini, halaman 2 diekstrak (pengindeksan berbasis 1).
1. Simpan yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan halaman yang diekstrak ke file output yang ditentukan.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Ekstrak Beberapa Halaman dari PDF

Ekstrak beberapa halaman spesifik dari dokumen PDF dan simpan ke dalam file baru. Dengan menggunakan pustaka Aspose.PDF, halaman yang dipilih disalin ke PDF baru sementara dokumen asli tetap tidak berubah. Ini berguna untuk membuat PDF yang lebih kecil yang hanya berisi bagian relevan dari dokumen yang lebih besar.

1. Muat PDF sumber menggunakan the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Buat yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) untuk menampung halaman yang diekstrak.
1. Pilih halaman yang akan diekstrak (dalam contoh ini, halaman 2 dan 3 menggunakan indeks berbasis 1).
1. Tambahkan setiap yang dipilih [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dari dokumen sumber ke PDF baru menggunakan [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Simpan yang baru [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan halaman yang diekstrak ke file output yang ditentukan.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Topik Halaman Terkait

- [Bekerja dengan halaman PDF di Python](/pdf/id/python-net/working-with-pages/)
- [Hapus halaman PDF di Python](/pdf/id/python-net/delete-pages/)
- [Pindahkan halaman PDF di Python](/pdf/id/python-net/move-pages/)
- [Membagi file PDF di Python](/pdf/id/python-net/split-document/)
