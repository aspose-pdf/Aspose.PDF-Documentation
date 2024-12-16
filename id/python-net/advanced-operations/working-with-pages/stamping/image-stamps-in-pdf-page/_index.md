---
title: Tambahkan Cap Gambar di PDF menggunakan Python
linktitle: Cap Gambar di File PDF
type: docs
weight: 10
url: /id/python-net/image-stamps-in-pdf-page/
description: Tambahkan Cap Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan perpustakaan Aspose.PDF untuk Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambahkan Cap Gambar di PDF menggunakan Python",
    "alternativeHeadline": "Tambahkan Cap Gambar di PDF menggunakan Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, pembuatan dokumen",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Tambahkan Cap Gambar dalam dokumen PDF Anda menggunakan kelas ImageStamp dengan perpustakaan Aspose.PDF untuk Python."
}
</script>


## Menambahkan Cap Gambar di File PDF

Anda dapat menggunakan kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) untuk menambahkan cap gambar ke file PDF. Kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) menyediakan properti yang diperlukan untuk membuat cap berbasis gambar, seperti tinggi, lebar, opasitas, dan sebagainya.

Untuk menambahkan cap gambar:

1. Buat objek Dokumen dan objek ImageStamp menggunakan properti yang diperlukan.
2. Panggil metode [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) dari kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) untuk menambahkan cap ke PDF.

Potongan kode berikut menunjukkan cara menambahkan cap gambar di file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat cap gambar
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Tambahkan cap ke halaman tertentu
    document.pages[1].add_stamp(image_stamp)

    # Simpan dokumen keluaran
    document.save(output_pdf)
```


## Mengontrol Kualitas Gambar saat Menambahkan Cap

Saat menambahkan gambar sebagai objek cap, Anda dapat mengontrol kualitas gambar tersebut. Properti [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) dari kelas [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) digunakan untuk tujuan ini. Ini menunjukkan kualitas gambar dalam persentase (nilai valid adalah 0..100).

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat cap gambar
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Tambahkan cap ke halaman tertentu
    document.pages[1].add_stamp(image_stamp)

    # Simpan dokumen keluaran
    document.save(output_pdf)
```

## Cap Gambar sebagai Latar Belakang dalam Kotak Mengambang

Aspose.PDF untuk API Python memungkinkan Anda menambahkan cap gambar sebagai latar belakang dalam kotak mengambang.
 The property [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) dari kelas [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) dapat digunakan untuk mengatur stempel gambar latar belakang untuk kotak mengambang seperti yang ditunjukkan dalam contoh kode berikut.

```python

    import aspose.pdf as ap

    # Membuat objek Dokumen
    document = ap.Document()
    # Tambahkan halaman ke dokumen PDF
    page = document.pages.add()
    # Buat objek FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # Atur posisi kiri untuk FloatingBox
    box.left = 40
    # Atur posisi atas untuk FloatingBox
    box.top = 80
    # Atur perataan horizontal untuk FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Tambahkan fragmen teks ke koleksi paragraf dari FloatingBox
    box.paragraphs.add(ap.text.TextFragment("teks utama"))
    # Atur batas untuk FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Tambahkan gambar latar belakang
    box.background_image = img
    # Atur warna latar belakang untuk FloatingBox
    box.background_color = ap.Color.yellow
    # Tambahkan FloatingBox ke koleksi paragraf dari objek halaman
    page.paragraphs.add(box)
    # Simpan dokumen PDF
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk Python melalui .NET Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>