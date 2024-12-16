---
title: Menambahkan Lampiran ke Dokumen PDF menggunakan Python
linktitle: Menambahkan Lampiran ke Dokumen PDF
type: docs
weight: 10
url: /id/python-net/add-attachment-to-pdf-document/
description: Halaman ini menjelaskan bagaimana menambahkan lampiran ke file PDF dengan Aspose.PDF untuk Python via .NET library.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Lampiran ke Dokumen PDF melalui Python",
    "alternativeHeadline": "Cara menambahkan lampiran ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, lampiran dalam pdf",
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
    "url": "/python-net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Halaman ini menjelaskan bagaimana menambahkan lampiran ke file PDF dengan Aspose.PDF untuk Python via .NET library"
}
</script>


Attachments dapat berisi berbagai macam informasi dan dapat berupa berbagai jenis file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

1. Buat proyek Python baru.
1. Impor paket Aspose.PDF
1. Buat objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Buat objek [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) dengan file yang Anda tambahkan, dan deskripsi file.
1. Tambahkan objek [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) ke koleksi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/), dengan metode [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods).

Koleksi [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) berisi semua lampiran dalam file PDF.
 Berikut adalah potongan kode yang menunjukkan cara menambahkan lampiran dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Siapkan file baru yang akan ditambahkan sebagai lampiran
    fileSpecification = ap.FileSpecification(attachment_file, "Contoh file teks")

    # Tambahkan lampiran ke koleksi lampiran dokumen
    document.embedded_files.append(fileSpecification)

    # Simpan keluaran baru
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