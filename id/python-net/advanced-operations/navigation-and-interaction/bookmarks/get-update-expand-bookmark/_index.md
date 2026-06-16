---
title: Dapatkan, Perbarui, dan Perluas Penanda Buku PDF di Python
linktitle: Dapatkan, Perbarui, dan Perluas Penanda
type: docs
weight: 20
url: /id/python-net/get-update-and-expand-bookmark/
description: Pelajari cara mengambil, memperbarui, dan memperluas penanda buku dalam dokumen PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menggunakan penanda buku dalam PDF dengan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengelola bookmark dalam dokumen PDF menggunakan library Aspose.PDF di Python. Artikel ini dimulai dengan menjelaskan cara mengambil bookmark dari file PDF melalui `OutlineCollection`, yang berisi semua bookmark, dan merinci cara mengakses atribut bookmark melalui `OutlineItemCollection`. Selanjutnya artikel menjelaskan proses menentukan nomor halaman yang terkait dengan bookmark menggunakan `PdfBookmarkEditor`. Artikel juga menjelaskan cara menangani struktur bookmark hierarkis dengan mengambil bookmark anak dalam setiap `OutlineItemCollection`. Artikel ini juga membahas pembaruan properti bookmark, menunjukkan cara memodifikasi atribut bookmark dan menyimpan perubahan ke PDF. Terakhir, artikel membahas kebutuhan memperluas bookmark saat melihat dokumen, menunjukkan cara mengatur status terbuka setiap bookmark untuk memastikan mereka diperluas secara default. Potongan kode menyertai setiap bagian, memberikan contoh praktis dalam mengimplementasikan fungsionalitas ini.
---

## Dapatkan Penanda Buku

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi berisi semua penanda buku sebuah file PDF. Artikel ini menjelaskan cara mendapatkan penanda buku dari file PDF, dan cara mengetahui halaman mana sebuah penanda buku berada.

Untuk mendapatkan penanda buku, lakukan perulangan melalui [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi dan dapatkan setiap penanda buku dalam OutlineItemCollection. The [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) menyediakan akses ke semua atribut bookmark. Potongan kode berikut menunjukkan cara mengambil bookmark dari file PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Mendapatkan Nomor Halaman Bookmark

Setelah Anda menambahkan bookmark, Anda dapat mengetahui halaman apa yang berisi bookmark tersebut dengan mendapatkan PageNumber tujuan yang terkait dengan objek Bookmark.

```python
from os import path
import sys
import aspose.pdf as ap

def get_bookmark_page_number(input_pdf):
    # Create PdfBookmarkEditor
    bookmark_editor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmark_editor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmark_editor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_separator = ""
        for i in range(bookmark.level):
            str_level_separator += "----"

        print(str_level_separator, "Title:", bookmark.title)
        print(str_level_separator, "Page Number:", bookmark.page_number)
        print(str_level_separator, "Page Action:", bookmark.action)
```

## Dapatkan Bookmark Anak dari Dokumen PDF

Bookmark dapat diatur dalam struktur hierarki, dengan induk dan anak. Untuk mendapatkan semua bookmark, lakukan perulangan melalui koleksi Outlines dari objek Document. Namun, untuk juga mendapatkan bookmark anak, lakukan perulangan juga melalui semua bookmark di setiap [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objek yang diperoleh pada perulangan pertama. Potongan kode berikut menunjukkan cara mendapatkan bookmark anak dari dokumen PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def get_child_bookmarks(input_pdf):
    document = ap.Document(input_pdf)
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Child Bookmarks")
            # There are child bookmarks then loop through that as well
            for j in range(len(outline_item)):
                child_outline_item = outline_item[j + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Perbarui Penanda dalam Dokumen PDF

Untuk memperbarui bookmark dalam file PDF, pertama, dapatkan bookmark tertentu dari koleksi OutlineColletion objek Document dengan menentukan indeks bookmark tersebut. Setelah Anda mengambil bookmark ke dalam [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objek, Anda dapat memperbarui propertinya dan kemudian menyimpan file PDF yang diperbarui menggunakan metode Save. Potongan kode berikut menunjukkan cara memperbarui bookmark dalam dokumen PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def update_bookmarks(input_pdf, output_pdf):
    # Open document
    document = ap.Document(input_pdf)

    # Get a bookmark object
    outline = document.outlines[1]

    # Get child bookmark object
    child_outline = outline[1]
    child_outline.title = "Updated Outline"
    child_outline.italic = True
    child_outline.bold = True

    # Save output
    document.save(output_pdf)
```

## Bookmark yang Diperluas saat melihat dokumen

Bookmark disimpan dalam objek Document [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) koleksi, itu sendiri di [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) koleksi. Namun, kami mungkin memiliki kebutuhan untuk menampilkan semua bookmark dalam keadaan diperluas saat melihat file PDF.

Untuk memenuhi kebutuhan ini, kita dapat mengatur status terbuka untuk setiap item outline/bookmark menjadi Open. Potongan kode berikut menunjukkan cara mengatur status terbuka setiap bookmark menjadi diperluas dalam dokumen PDF.

```python
from os import path
import sys
import aspose.pdf as ap

def expanded_bookmarks(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.page_mode = ap.PageMode.USE_OUTLINES
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        item.open = True
    document.save(output_pdf)
```

## Topik Bookmark Terkait

- [Bekerja dengan bookmark PDF di Python](/pdf/id/python-net/bookmarks/)
- [Menambahkan dan menghapus bookmark PDF di Python](/pdf/id/python-net/add-and-delete-bookmark/)
- [Navigasi dan interaksi dalam PDF menggunakan Python](/pdf/id/python-net/navigation-and-interaction/)

