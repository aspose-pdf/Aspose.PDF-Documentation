---
title: Bekerja dengan Teks di PDF menggunakan C#
linktitle: Bekerja dengan Teks
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/working-with-text/
description: Bagian ini menjelaskan berbagai teknik penanganan teks. Pelajari cara menambahkan, mengganti, memutar, dan mencari teks menggunakan Aspose.PDF dan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "Temukan kemampuan manipulasi teks yang kuat dalam PDF menggunakan Aspose.PDF for .NET. Fitur ini memungkinkan pengguna untuk dengan mudah menambahkan, mengganti, memutar, dan memformat teks dalam dokumen PDF, meningkatkan interaktivitas dan kustomisasi dokumen. Memberdayakan aplikasi Anda dengan fungsionalitas pencarian yang efisien dan teknik penanganan teks yang fleksibel yang dirancang untuk pengembang C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Bagian ini menjelaskan berbagai teknik penanganan teks. Pelajari cara menambahkan, mengganti, memutar, dan mencari teks menggunakan Aspose.PDF dan C#."
}
</script>

Kita semua kadang-kadang perlu menambahkan teks ke file PDF. Misalnya, ketika Anda ingin menambahkan terjemahan di bawah teks utama, menempatkan keterangan di samping gambar, atau hanya mengisi formulir aplikasi. Ini juga berguna jika semua elemen teks dapat diformat sesuai gaya yang Anda inginkan. Manipulasi teks yang paling populer di file PDF Anda adalah: menambahkan teks ke PDF, memformat teks di dalam file PDF, mengganti dan memutar teks di dokumen Anda. **Aspose.PDF for .NET** adalah solusi terbaik yang memiliki semua yang Anda butuhkan untuk berinteraksi dengan konten PDF.

 Anda dapat melakukan hal-hal berikut:

- [Menambahkan Teks ke file PDF](/pdf/net/add-text-to-pdf-file/) - menambahkan teks ke PDF Anda, menggunakan font dari stream dan file, menambahkan string HTML, menambahkan hyperlink, dll.
- [Tooltip PDF](/pdf/net/pdf-tooltip/) - Anda dapat menambahkan tooltip ke teks yang dicari dengan menambahkan tombol tak terlihat menggunakan C#.
- [Pemformatan Teks di dalam PDF](/pdf/net/text-formatting-inside-pdf/) - Banyak fitur yang dapat Anda tambahkan ke dokumen Anda saat memformat teks di dalamnya. Tambahkan indentasi baris, tambahkan batas teks, tambahkan teks garis bawah, tambahkan umpan baris baru dengan pustaka Aspose.PDF.
- [Menggunakan FloatingBox](/pdf/net/floating-box/) - alat Floating Box adalah alat khusus untuk menempatkan teks dan konten lainnya di halaman PDF.
- [Mengganti Teks di PDF](/pdf/net/replace-text-in-pdf/) - untuk mengganti teks di semua halaman dokumen PDF. Anda pertama-tama perlu menggunakan TextFragmentAbsorber.
- [Memutar Teks di Dalam PDF](/pdf/net/rotate-text-inside-pdf/) - memutar teks di dalam PDF menggunakan properti rotasi dari Kelas TextFragment.
- [Mencari dan Mendapatkan Teks dari Halaman Dokumen PDF](/pdf/net/search-and-get-text-from-pdf/) - Anda dapat menggunakan kelas TextFragmentAbsorber untuk mencari dan mendapatkan teks dari halaman.
- [Menentukan Pemutusan Baris](/pdf/net/determine-line-break/) - topik ini menjelaskan cara melacak pemutusan baris dari fragmen teks multi-baris.

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