---
title: Bekerja dengan Portofolio dalam PDF menggunakan Python
linktitle: Portofolio
type: docs
weight: 20
url: id/python-net/portfolio/
description: Cara Membuat Portofolio PDF dengan Python. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Portofolio dalam PDF menggunakan Python",
    "alternativeHeadline": "Buat Portofolio dalam dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf dalam pdf",
    "keywords": "pdf, python, portofolio",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Cara Membuat Portofolio PDF dengan Python. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF."
}
</script>


Membuat portofolio PDF memungkinkan konsolidasi dan pengarsipan berbagai jenis file ke dalam satu dokumen yang konsisten. Dokumen semacam itu dapat mencakup file teks, gambar, spreadsheet, presentasi, dan materi lainnya, serta memastikan bahwa semua materi relevan disimpan dan diatur di satu tempat.

Portofolio PDF akan membantu menampilkan presentasi Anda dengan cara berkualitas tinggi, di mana pun Anda menggunakannya. Secara umum, membuat portofolio PDF adalah tugas yang sangat terkini dan modern.

## Cara Membuat Portofolio PDF

Aspose.PDF untuk Python melalui .NET memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Tambahkan file ke dalam objek document.collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Ketika file-file tersebut telah ditambahkan, gunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas Document untuk menyimpan dokumen portofolio.


Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.

Kode di bawah ini menghasilkan portofolio berikut.

### Sebuah Portofolio PDF dibuat dengan Aspose.PDF untuk Python

![Sebuah Portofolio PDF dibuat dengan Aspose.PDF untuk Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Memulai Objek Dokumen
    document = ap.Document()

    # Memulai objek Koleksi dokumen
    document.collection = ap.Collection()

    # Mendapatkan File untuk ditambahkan ke Portofolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Menyediakan deskripsi dari file
    excel.description = "File Excel"
    word.description = "File Word"
    image.description = "File Gambar"

    # Menambahkan file ke koleksi dokumen
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Menyimpan dokumen Portofolio
    document.save(output_pdf)
```

## Menghapus File dari Portofolio PDF

Untuk menghapus/menghilangkan file dari portofolio PDF, coba gunakan baris kode berikut.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Simpan file yang diperbarui
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python Library",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Library Manipulasi PDF untuk Python",
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