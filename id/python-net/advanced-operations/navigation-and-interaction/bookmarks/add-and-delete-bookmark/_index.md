---
title: Menambahkan dan Menghapus Penanda PDF dalam Python
linktitle: Menambahkan dan Menghapus Penanda
type: docs
weight: 10
url: /id/python-net/add-and-delete-bookmark/
description: Pelajari cara menambahkan dan menghapus penanda dalam dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan, dan menghapus Penanda menggunakan Python
Abstract: Artikel ini menyediakan instruksi komprehensif tentang mengelola bookmark dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python. Ini menjelaskan proses menambahkan, memodifikasi, dan menghapus bookmark dalam PDF. Artikel ini dimulai dengan panduan menambahkan bookmark dengan membuat objek `OutlineItemCollection` dan menambahkannya ke `OutlineCollection` dokumen. Ini menyertakan contoh kode yang menunjukkan pembuatan dan penambahan bookmark induk maupun anak, menyoroti hubungan hierarki. Selain itu, artikel ini mencakup metode untuk menghapus semua bookmark atau bookmark tertentu berdasarkan judul. Setiap bagian menyertakan potongan kode Python untuk mengilustrasikan operasi, memastikan pembaca dapat dengan mudah menerapkan fungsi yang dijelaskan dalam tugas manipulasi PDF mereka.
---

## Tambahkan Penanda ke Dokumen PDF

Penanda disimpan dalam objek Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) koleksi, itu sendiri di dalam [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi.

Untuk menambahkan bookmark ke PDF:

1. Buka dokumen PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek.
1. Buat bookmark dan tentukan propertinya.
1. Tambahkan [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) koleksi ke koleksi Outlines.

Potongan kode berikut menunjukkan cara menambahkan penanda buku dalam dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Tambahkan Bookmark Anak ke Dokumen PDF

Bookmark dapat ditumpuk, menunjukkan hubungan hierarkis dengan bookmark induk dan anak. Artikel ini menjelaskan cara menambahkan bookmark anak, yaitu bookmark tingkat kedua, ke PDF.

Untuk menambahkan bookmark anak ke file PDF, pertama tambahkan bookmark induk:

1. Buka dokumen.
1. Tambahkan bookmark ke [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke objek Document. [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi.

Bookmark anak dibuat persis seperti bookmark induk, yang dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines bookmark induk.

Potongan kode berikut menunjukkan cara menambahkan bookmark anak ke dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Hapus semua Bookmark dari Dokumen PDF

Semua bookmark dalam PDF disimpan di [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) collection. Artikel ini menjelaskan cara menghapus semua bookmark dari file PDF.

Untuk menghapus semua bookmark dari file PDF:

1. Panggil [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) metode Delete milik collection.
1. Simpan file yang dimodifikasi menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

Potongan kode berikut menunjukkan cara menghapus semua bookmark dari dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Hapus Penanda Tertentu dari Dokumen PDF

Untuk menghapus penanda tertentu dari file PDF:

1. Berikan judul penanda sebagai parameter ke [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) metode Delete milik collection.
1. Kemudian simpan file yang diperbarui dengan metode Save objek Document.

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas menyediakan [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi. The [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) metode menghapus semua penanda dengan judul yang diberikan ke metode.

Cuplikan kode berikut menunjukkan cara menghapus bookmark tertentu dari dokumen PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Topik Bookmark Terkait

- [Bekerja dengan bookmark PDF di Python](/pdf/id/python-net/bookmarks/)
- [Dapatkan, perbarui, dan perluas bookmark PDF di Python](/pdf/id/python-net/get-update-and-expand-bookmark/)
- [Navigasi dan interaksi dalam PDF menggunakan Python](/pdf/id/python-net/navigation-and-interaction/)

