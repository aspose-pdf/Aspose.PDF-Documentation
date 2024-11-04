---
title: Mengubah Ukuran Halaman PDF dengan C#
linktitle: Mengubah Ukuran Halaman PDF
type: docs
weight: 40
url: /net/change-page-size/
description: Mengubah ukuran halaman dari dokumen PDF Anda menggunakan perpustakaan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mengubah Ukuran Halaman PDF dengan C#",
    "alternativeHeadline": "Mengubah Ukuran Halaman PDF dengan .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, mengubah ukuran pdf, mengubah ukuran pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Mengubah ukuran halaman dari dokumen PDF Anda menggunakan perpustakaan Aspose.PDF untuk .NET."
}
</script>
## Mengubah Ukuran Halaman PDF

Aspose.PDF untuk .NET memungkinkan Anda mengubah ukuran halaman PDF dengan beberapa baris kode dalam aplikasi .NET Anda. Topik ini menjelaskan cara memperbarui/mengubah dimensi halaman (ukuran) dari file PDF yang sudah ada.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

Kelas [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) mengandung metode SetPageSize(...) yang memungkinkan Anda mengatur ukuran halaman. Potongan kode di bawah ini memperbarui dimensi halaman dalam beberapa langkah mudah:

1. Muat file PDF sumber.
1. Dapatkan halaman ke dalam objek [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Dapatkan halaman tertentu.
1. Panggil metode SetPageSize(..) untuk memperbarui dimensinya.
1. Panggil metode Save(..) kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) untuk menghasilkan file PDF dengan dimensi halaman yang diperbarui.

{{% alert color="primary" %}}

Harap dicatat bahwa properti tinggi dan lebar menggunakan poin sebagai unit dasar, di mana 1 inci = 72 poin dan 1 cm = 1/2.54 inci = 0.3937 inci = 28.3 poin.
Silakan perhatikan bahwa properti tinggi dan lebar menggunakan poin sebagai satuan dasar, dimana 1 inci = 72 poin dan 1 cm = 1/2.54 inci = 0.3937 inci = 28.3 poin.

{{% /alert %}}

Potongan kode berikut menunjukkan cara mengubah dimensi halaman PDF menjadi ukuran A4.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## Dapatkan Ukuran Halaman PDF

Anda dapat membaca ukuran halaman PDF dari file PDF yang ada menggunakan Aspose.PDF untuk .NET. Contoh kode berikut menunjukkan cara membaca dimensi halaman PDF menggunakan C#.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


