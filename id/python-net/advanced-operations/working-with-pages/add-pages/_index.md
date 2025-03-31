---
title: Tambahkan Halaman dalam PDF dengan Python
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /id/python-net/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghilangkan) halaman dari file PDF menggunakan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Halaman dalam PDF dengan Python",
    "alternativeHeadline": "Cara menambahkan Halaman dalam dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, tambahkan halaman pdf, sisipkan halaman pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghilangkan) halaman dari file PDF menggunakan Python."
}
</script>


Aspose.PDF untuk Python melalui .NET API menyediakan fleksibilitas penuh untuk bekerja dengan halaman dalam dokumen PDF menggunakan Python. Ini memelihara semua halaman dari dokumen PDF dalam [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) yang dapat digunakan untuk bekerja dengan halaman PDF. Aspose.PDF untuk Python melalui .NET memungkinkan Anda menyisipkan halaman ke dalam dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF. Bagian ini menunjukkan cara menambahkan halaman ke PDF menggunakan Python.

## Menambah atau Menyisipkan Halaman dalam File PDF

Aspose.PDF untuk Python melalui .NET memungkinkan Anda menyisipkan halaman ke dalam dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

### Menyisipkan Halaman Kosong dalam File PDF di Lokasi yang Diinginkan

Untuk menyisipkan halaman kosong dalam file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF masukan.

1. Panggil metode [insert](https://reference.aspose.com/pdf/id/net/aspose.pdf/pagecollection/methods/insert) dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dengan indeks yang ditentukan.
1. Simpan PDF keluaran menggunakan metode [save](https://reference.aspose.com/pdf/id/net/aspose.pdf.document/save/methods/4).

Cuplikan kode berikut menunjukkan cara menyisipkan halaman dalam file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    # Sisipkan halaman kosong dalam PDF
    document.pages.insert(2)
    # Simpan file keluaran
    document.save(output_pdf)
```

### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir pada halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF masukan.

1. Panggil metode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) tanpa parameter apapun.
1. Simpan PDF keluaran menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara memasukkan halaman kosong di akhir file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Masukkan halaman kosong di akhir file PDF
    document.pages.add()

    # Simpan file keluaran
    document.save(output_pdf)