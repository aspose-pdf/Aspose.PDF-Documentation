---
title: Cara Menggabungkan PDF menggunakan Python
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/python-net/merge-pdf-documents/
keywords: "gabungkan beberapa pdf menjadi satu pdf python, gabungkan beberapa pdf menjadi satu python, gabungkan beberapa pdf menjadi satu python"
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Python.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cara Menggabungkan PDF menggunakan Python",
    "alternativeHeadline": "Gabungkan dokumen PDF melalui Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulasi dokumen pdf",
    "keywords": "pdf, python, gabungkan pdf, menggabungkan, gabungkan pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu file PDF dengan Python melalui .NET."
}
</script>


## Menggabungkan atau mengkombinasikan beberapa PDF menjadi satu PDF di Python

Menggabungkan file PDF adalah permintaan yang sangat populer di antara pengguna. Ini bisa berguna ketika Anda memiliki beberapa file PDF yang ingin Anda bagikan atau simpan bersama sebagai satu dokumen.

Menggabungkan file PDF dapat membantu Anda mengatur dokumen, menyediakan ruang penyimpanan di PC Anda, dan berbagi beberapa file PDF dengan orang lain dengan menggabungkannya menjadi satu dokumen.

Menggabungkan PDF di Python melalui .NET bukanlah tugas yang mudah tanpa menggunakan pustaka pihak ketiga. Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk Python melalui .NET.

## Menggabungkan File PDF menggunakan Python dan DOM

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), masing-masing berisi salah satu dari file PDF input.

1. Kemudian panggil metode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) untuk objek Dokumen yang ingin Anda tambahkan ke file PDF lainnya.
1. Lewatkan koleksi PageCollection dari objek Dokumen kedua ke metode [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) koleksi PageCollection pertama.
1. Terakhir, simpan file PDF keluaran menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan cara menggabungkan file PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen pertama
    document1 = ap.Document(input_pdf_1)
    # Buka dokumen kedua
    document2 = ap.Document(input_pdf_2)

    # Tambahkan halaman dari dokumen kedua ke yang pertama
    document1.pages.add(document2.pages)

    # Simpan file keluaran yang telah digabungkan
    document1.save(output_pdf)
```


## Contoh Langsung

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis online yang memungkinkan Anda menyelidiki bagaimana fungsionalitas penggabungan presentasi bekerja.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>