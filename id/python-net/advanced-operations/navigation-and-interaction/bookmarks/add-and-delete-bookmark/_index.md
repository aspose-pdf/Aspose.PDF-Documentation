---
title: Menambahkan dan Menghapus Penanda Buku menggunakan Python
linktitle: Menambah dan Menghapus Penanda Buku
type: docs
weight: 10
url: /id/python-net/add-and-delete-bookmark/
description: Anda dapat menambahkan penanda buku ke dokumen PDF dengan Python. Anda dapat menghapus semua atau penanda buku tertentu dari dokumen PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menambahkan, dan menghapus Penanda Buku menggunakan Python
Abstract: Artikel ini memberikan petunjuk komprehensif tentang mengelola penanda buku dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini menjelaskan proses menambahkan, memodifikasi, dan menghapus penanda buku dalam PDF. Artikel dimulai dengan panduan menambahkan penanda buku dengan membuat objek `OutlineItemCollection` dan menambahkannya ke `OutlineCollection` dokumen. Artikel ini menyertakan contoh kode yang menunjukkan pembuatan dan penambahan penanda buku induk dan anak, menyoroti hubungan hierarkis. Selain itu, artikel ini mencakup metode untuk menghapus semua penanda buku atau penanda buku tertentu berdasarkan judul. Setiap bagian menyertakan cuplikan kode Python untuk mengilustrasikan operasi, memastikan pembaca dapat dengan mudah menerapkan fungsionalitas yang dijelaskan dalam tugas manipulasi PDF mereka.
---

## Menambahkan Penanda Buku ke Dokumen PDF

Penanda buku disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) milik objek Document, yang berada di dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Untuk menambahkan penanda buku ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat penanda buku dan tentukan propertinya.
1. Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) ke koleksi Outlines.

Cuplikan kode berikut menunjukkan cara menambahkan penanda buku dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Menambahkan Penanda Buku Anak ke Dokumen PDF

Penanda buku dapat ditumpuk, menunjukkan hubungan hierarkis antara penanda induk dan anak. Artikel ini menjelaskan cara menambahkan penanda buku anak, yaitu penanda buku tingkat kedua, ke PDF.

Untuk menambahkan penanda buku anak ke file PDF, pertama tambahkan penanda buku induk:

1. Buka dokumen.
1. Tambahkan penanda buku ke [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), dengan mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) milik objek Document.

Penanda buku anak dibuat sama seperti penanda buku induk, seperti dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines milik penanda buku induk.

Cuplikan kode berikut menunjukkan cara menambahkan penanda buku anak ke dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Menghapus Semua Penanda Buku dari Dokumen PDF

Semua penanda buku dalam PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Artikel ini menjelaskan cara menghapus semua penanda buku dari file PDF.

Untuk menghapus semua penanda buku dari file PDF:

1. Panggil metode Delete pada koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Simpan file yang telah dimodifikasi menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) pada objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Cuplikan kode berikut menunjukkan cara menghapus semua penanda buku dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Menghapus Penanda Buku Tertentu dari Dokumen PDF

Untuk menghapus penanda buku tertentu dari file PDF:

1. Berikan judul penanda buku sebagai parameter ke metode Delete pada koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Kemudian simpan file yang telah diperbarui dengan metode Save pada objek Document.

Kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Metode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) menghapus semua penanda buku dengan judul yang diberikan ke metode tersebut.

Cuplikan kode berikut menunjukkan cara menghapus penanda buku tertentu dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


