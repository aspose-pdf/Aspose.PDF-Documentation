---
title: Ubah Ukuran Halaman PDF dengan Python
linktitle: Ubah Ukuran Halaman PDF
type: docs
weight: 60
url: id/python-net/change-page-size/
description: Ubah Ukuran Halaman dari dokumen PDF Anda menggunakan Aspose.PDF untuk Python melalui pustaka .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ubah Ukuran Halaman PDF dengan Python",
    "alternativeHeadline": "Ubah Ukuran Halaman PDF dengan Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, ubah ukuran pdf, ubah ukuran pdf",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Ubah Ukuran Halaman dari dokumen PDF Anda menggunakan Aspose.PDF untuk Python melalui pustaka .NET."
}
</script>


## Ubah Ukuran Halaman PDF

Aspose.PDF untuk Python via .NET memungkinkan Anda mengubah ukuran halaman PDF dengan baris kode sederhana dalam aplikasi Python Anda. Topik ini menjelaskan cara memperbarui/mengubah dimensi (ukuran) halaman dari file PDF yang ada.

Kelas [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) berisi metode [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) yang memungkinkan Anda mengatur ukuran halaman. Cuplikan kode di bawah ini memperbarui dimensi halaman dalam beberapa langkah mudah:

1. Muat file PDF sumber.
1. Dapatkan halaman ke dalam objek [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Dapatkan halaman tertentu.
1. Panggil metode set_page_size() untuk memperbarui dimensinya.
1. Panggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) untuk menghasilkan file PDF dengan dimensi halaman yang diperbarui.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Dapatkan halaman tertentu
    page = document.pages[1]

    # Atur ukuran halaman sebagai A4 (11.7 x 8.3 in) dan dalam Aspose.Pdf, 1 inci = 72 poin
    # Jadi dimensi A4 dalam poin adalah (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Simpan dokumen yang diperbarui
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF untuk .NET Library",
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