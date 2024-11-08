---
title: Memisahkan PDF secara program di Python
linktitle: Memisahkan file PDF
type: docs
weight: 60
url: /id/python-net/split-pdf-document/
keywords: membagi pdf menjadi beberapa file, membagi pdf menjadi pdf terpisah, membagi pdf python
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individual dalam aplikasi Python Anda.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memisahkan PDF secara program",
    "alternativeHeadline": "Cara memisahkan PDF dengan Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, membagi pdf",
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
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individual dalam aplikasi Python Anda."
}
</script>


Memisahkan halaman PDF bisa menjadi fitur yang berguna bagi mereka yang ingin membagi file besar menjadi halaman atau kelompok halaman terpisah.

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis yang memungkinkan Anda menyelidiki bagaimana fungsi pemisahan presentasi bekerja.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi Python Anda. Untuk memisahkan halaman PDF menjadi file PDF satu halaman menggunakan Python, langkah-langkah berikut dapat diikuti:

1. Loop melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individu ke dalam dokumen kosong

1. Simpan PDF baru menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Pisahkan PDF menjadi beberapa file atau pdf terpisah di Python

Cuplikan kode Python berikut menunjukkan cara membagi halaman PDF menjadi file PDF individual.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    page_count = 1

    # Lakukan loop melalui semua halaman
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1