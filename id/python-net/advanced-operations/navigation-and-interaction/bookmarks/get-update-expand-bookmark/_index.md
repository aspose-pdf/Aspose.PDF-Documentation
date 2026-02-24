---
title: Dapatkan, Perbarui, dan Perluas Bookmark menggunakan Python
linktitle: Dapatkan, Perbarui, dan Perluas Bookmark
type: docs
weight: 20
url: /id/python-net/get-update-and-expand-bookmark/
description: Artikel ini menjelaskan cara menggunakan bookmark dalam file PDF dengan pustaka Aspose.PDF untuk Python kami.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara menggunakan bookmark dalam PDF dengan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengelola bookmark dalam dokumen PDF menggunakan pustaka Aspose.PDF di Python. Artikel ini dimulai dengan menjelaskan cara mengambil bookmark dari file PDF melalui `OutlineCollection`, yang berisi semua bookmark, dan merinci akses ke atribut bookmark melalui `OutlineItemCollection`. Selanjutnya artikel menggambarkan proses menentukan nomor halaman yang terkait dengan sebuah bookmark menggunakan `PdfBookmarkEditor`. Artikel ini juga menjelaskan cara menangani struktur bookmark hierarkis dengan mengambil bookmark anak dalam setiap `OutlineItemCollection`. Selain itu, dibahas cara memperbarui properti bookmark, memperlihatkan cara memodifikasi atribut bookmark dan menyimpan perubahan ke PDF. Akhirnya, artikel ini membahas kebutuhan memperluas bookmark saat melihat dokumen, menunjukkan cara mengatur status terbuka setiap bookmark agar secara default diperluas. Potongan kode menyertai setiap bagian, memberikan contoh praktis implementasi fungsionalitas ini.
---

## Dapatkan Bookmark

Koleksi [OutlineCollection] objek [Dokumen] berisi semua bookmark file PDF. Artikel ini menjelaskan cara mendapatkan bookmark dari file PDF, dan cara mengetahui halaman mana bookmark tertentu berada.

Untuk mendapatkan bookmark, lakukan iterasi melalui koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) dan dapatkan setiap bookmark dalam OutlineItemCollection. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) menyediakan akses ke semua atribut bookmark. Potongan kode berikut menunjukkan cara mendapatkan bookmark dari file PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```

## Mendapatkan Nomor Halaman Bookmark

Setelah Anda menambahkan bookmark, Anda dapat mengetahui halaman tempatnya berada dengan mengambil PageNumber tujuan yang terkait dengan objek Bookmark.

```python

    import aspose.pdf as ap

    # Create PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Open PDF file
    bookmarkEditor.bind_pdf(input_pdf)
    # Extract bookmarks
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Title:", bookmark.title)
        print(str_level_seprator, "Page Number:", bookmark.page_number)
        print(str_level_seprator, "Page Action:", bookmark.action)
```

## Dapatkan Bookmark Anak dari Dokumen PDF

Bookmark dapat diatur dalam struktur hierarkis, dengan induk dan anak. Untuk mendapatkan semua bookmark, lakukan iterasi melalui koleksi Outlines dari objek Document. Namun, untuk juga mendapatkan bookmark anak, lakukan iterasi melalui semua bookmark di setiap objek [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) yang diperoleh pada iterasi pertama. Potongan kode berikut menunjukkan cara mendapatkan bookmark anak dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Loop through all the bookmarks
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
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Memperbarui Bookmark dalam Dokumen PDF

Untuk memperbarui bookmark dalam file PDF, pertama-tama dapatkan bookmark tertentu dari koleksi OutlineColletion objek Document dengan menentukan indeks bookmark. Setelah Anda mengambil bookmark ke dalam objek [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), Anda dapat memperbarui propertinya dan kemudian menyimpan file PDF yang diperbarui menggunakan metode Save. Potongan kode berikut menunjukkan cara memperbarui bookmark dalam dokumen PDF.

```python

    import aspose.pdf as ap

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

## Bookmark Diperluas saat melihat dokumen

Bookmark disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objek Document, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Namun, mungkin ada kebutuhan agar semua bookmark diperluas saat melihat file PDF.

Untuk memenuhi kebutuhan ini, kita dapat mengatur status terbuka untuk setiap item outline/bookmark menjadi Open. Potongan kode berikut menunjukkan cara mengatur status terbuka setiap bookmark menjadi diperluas dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Traverse through each Ouline item in outlines collection of PDF file
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Set open status for outline item
        item.open = True

    # Save output
    document.save(output_pdf)
```


