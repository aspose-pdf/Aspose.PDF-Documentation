---
title: Bekerja dengan Teks dalam PDF menggunakan C#
linktitle: Bekerja dengan Teks
type: docs
weight: 30
url: /id/net/working-with-text/
description: Bagian ini menjelaskan berbagai teknik penanganan teks. Pelajari cara menambahkan, mengganti, memutar, mencari teks menggunakan Aspose.PDF dan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Teks dalam PDF menggunakan C#",
    "alternativeHeadline": "Tambah, Putar, Cari, dan Hapus Teks dalam Berkas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, tambah teks, cari teks, hapus teks, manipulasi teks dalam pdf",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan berbagai teknik penanganan teks. Pelajari cara menambahkan, mengganti, memutar, mencari teks menggunakan Aspose.PDF dan C#."
}
</script>

Kita semua terkadang perlu menambahkan teks ke dalam file PDF. Misalnya, ketika Anda ingin menambahkan terjemahan di bawah teks utama, menempatkan keterangan di sebelah gambar, atau sekadar mengisi formulir aplikasi. Sangat membantu juga jika semua elemen teks dapat diformat sesuai dengan gaya yang Anda inginkan. Manipulasi teks paling populer dalam file PDF Anda adalah: menambahkan teks ke PDF, memformat teks dalam file PDF, mengganti dan memutar teks dalam dokumen Anda. **Aspose.PDF for .NET** adalah solusi terbaik yang memiliki segala yang Anda butuhkan untuk berinteraksi dengan konten PDF.

Anda dapat melakukan hal berikut:

- [Tambah Teks ke file PDF](/pdf/id/net/add-text-to-pdf-file/) - tambahkan teks ke PDF Anda, gunakan font dari strem dan file, tambahkan string HTML, tambahkan hyperlink, dll.
- [Tooltip PDF](/pdf/id/net/pdf-tooltip/) - Anda dapat menambahkan tooltip ke teks yang dicari dengan menambahkan tombol tak terlihat menggunakan C#.
- [Pemformatan Teks dalam PDF](/pdf/id/net/text-formatting-inside-pdf/) - Banyak fitur yang dapat Anda tambahkan ke dokumen Anda saat memformat teks di dalamnya.
- [Pemformatan Teks dalam PDF](/pdf/id/net/text-formatting-inside-pdf/) - Banyak fitur yang dapat Anda tambahkan ke dokumen Anda saat memformat teks di dalamnya.
- [Mengganti Teks dalam PDF](/pdf/id/net/replace-text-in-pdf/) - untuk mengganti teks di semua halaman dokumen PDF. Anda pertama-tama perlu menggunakan TextFragmentAbsorber.
- [Memutar Teks Dalam PDF](/pdf/id/net/rotate-text-inside-pdf/) - memutar teks dalam PDF menggunakan properti rotasi dari Kelas TextFragment.
- [Mencari dan Mendapatkan Teks dari Halaman Dokumen PDF](/pdf/id/net/search-and-get-text-from-pages-of-pdf/) - Anda dapat menggunakan kelas TextFragmentAbsorber untuk mencari dan mendapatkan teks dari halaman.
- [Menentukan Pemutusan Baris](/pdf/id/net/determine-line-break/) - topik ini menjelaskan cara melacak pemutusan baris dari fragmen teks multi-baris.

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

