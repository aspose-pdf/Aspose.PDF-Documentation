---
title: Dapatkan, Perbarui, dan Perluas Sebuah Penanda Buku menggunakan Python
linktitle: Dapatkan, Perbarui, dan Perluas Sebuah Penanda Buku
type: docs
weight: 20
url: id/python-net/get-update-and-expand-bookmark/
description: Artikel ini menjelaskan cara menggunakan penanda buku dalam file PDF dengan pustaka Aspose.PDF untuk Python kami.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dapatkan, Perbarui, dan Perluas Sebuah Penanda Buku dengan Python",
    "alternativeHeadline": "Cara mendapatkan Penanda Buku dari file PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, mendapatkan penanda buku",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Artikel ini menjelaskan cara menggunakan penanda buku dalam file PDF dengan pustaka Aspose.PDF untuk Python kami."
}
</script>


## Dapatkan Penanda Buku

Koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) berisi semua penanda buku dari file PDF. Artikel ini menjelaskan cara mendapatkan penanda buku dari file PDF, dan bagaimana mengetahui pada halaman mana penanda buku tertentu berada.

Untuk mendapatkan penanda buku, lakukan iterasi melalui koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) dan dapatkan setiap penanda buku dalam OutlineItemCollection. [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) menyediakan akses ke semua atribut penanda buku. Cuplikan kode berikut menunjukkan cara mendapatkan penanda buku dari file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Iterasi melalui semua penanda buku
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
```


## Mendapatkan Nomor Halaman dari Penanda Buku

Setelah Anda menambahkan penanda buku, Anda dapat mengetahui pada halaman mana penanda tersebut berada dengan mendapatkan PageNumber tujuan yang terkait dengan objek Bookmark.

```python

    import aspose.pdf as ap

    # Buat PdfBookmarkEditor
    bookmarkEditor = ap.facades.PdfBookmarkEditor()
    # Buka file PDF
    bookmarkEditor.bind_pdf(input_pdf)
    # Ekstrak penanda buku
    bookmarks = bookmarkEditor.extract_bookmarks()
    for bookmark in bookmarks:
        str_level_seprator = ""
        for i in range(bookmark.level):
            str_level_seprator += "----"

        print(str_level_seprator, "Judul:", bookmark.title)
        print(str_level_seprator, "Nomor Halaman:", bookmark.page_number)
        print(str_level_seprator, "Aksi Halaman:", bookmark.action)
```

## Mendapatkan Penanda Buku Anak dari Dokumen PDF

Penanda buku dapat diatur dalam struktur hierarki, dengan induk dan anak.
 Untuk mendapatkan semua penanda buku, lakukan perulangan melalui koleksi Outlines dari objek Document. Namun, untuk mendapatkan penanda buku anak juga, lakukan perulangan melalui semua penanda buku dalam setiap objek [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) yang diperoleh dalam perulangan pertama. Cuplikan kode berikut menunjukkan cara mendapatkan penanda buku anak dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Lakukan perulangan melalui semua penanda buku
    for i in range(len(document.outlines)):
        outline_item = document.outlines[i + 1]
        print(outline_item.title)
        print(outline_item.italic)
        print(outline_item.bold)
        print(outline_item.color)
        count = len(outline_item)
        if count > 0:
            print("Penanda Buku Anak")
            # Terdapat penanda buku anak, maka lakukan perulangan melalui itu juga
            for j in range(len(outline_item)):
                child_outline_item = outline_item[i + 1]
                print(child_outline_item.title)
                print(child_outline_item.italic)
                print(child_outline_item.bold)
                print(child_outline_item.color)
```

## Memperbarui Penanda Buku dalam Dokumen PDF

Untuk memperbarui penanda buku dalam file PDF, pertama, dapatkan penanda buku tertentu dari koleksi OutlineColletion objek Document dengan menentukan indeks penanda buku. Setelah Anda mendapatkan penanda buku ke dalam objek [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), Anda dapat memperbarui propertinya dan kemudian menyimpan file PDF yang diperbarui menggunakan metode Save. Cuplikan kode berikut menunjukkan cara memperbarui penanda buku dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Dapatkan objek penanda buku
    outline = document.outlines[1]

    # Dapatkan objek penanda buku anak
    child_outline = outline[1]
    child_outline.title = "Outline yang Diperbarui"
    child_outline.italic = True
    child_outline.bold = True

    # Simpan keluaran
    document.save(output_pdf)
```

## Penanda Buku yang Diperluas saat melihat dokumen

Penanda buku disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) objek Document, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
 Namun, kita mungkin memiliki persyaratan untuk memperluas semua penanda buku saat melihat file PDF.

Untuk memenuhi persyaratan ini, kita dapat mengatur status terbuka untuk setiap item garis besar/penanda buku sebagai Terbuka. Cuplikan kode berikut menunjukkan cara mengatur status terbuka untuk setiap penanda buku agar diperluas dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Atur mode tampilan halaman yaitu tampilkan thumbnail, layar penuh, tampilkan panel lampiran
    document.page_mode = ap.PageMode.USE_OUTLINES
    # Telusuri setiap item Ouline dalam koleksi outlines dari file PDF
    for i in range(len(document.outlines)):
        item = document.outlines[i + 1]
        # Atur status terbuka untuk item outline
        item.open = True

    # Simpan keluaran
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>