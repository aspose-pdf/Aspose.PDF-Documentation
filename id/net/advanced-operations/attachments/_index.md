---
title: Bekerja dengan Lampiran di PDF
linktitle: Bekerja dengan Lampiran
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 190
url: /id/net/attachments/
description: Gunakan C# PDF API untuk mengakses, menambahkan, dan menghapus lampiran dalam file PDF menggunakan C# dari dalam aplikasi Anda. Panduan lengkap dengan contoh kode C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments in PDF",
    "alternativeHeadline": "Effortlessly Manage PDF Attachments with C#",
    "abstract": "Temukan cara untuk mengelola lampiran dalam file PDF secara efisien menggunakan C# PDF API yang kuat. Fitur ini memungkinkan pengembang untuk mengakses, menambahkan, dan menghapus berbagai jenis file yang dilampirkan ke PDF, lengkap dengan contoh kode C# yang mendetail untuk integrasi yang mulus ke dalam aplikasi. Tingkatkan kemampuan manipulasi PDF Anda dengan memanfaatkan panduan komprehensif ini",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF API, attachments in PDF, add attachments, remove attachments, extract attachments, Aspose.PDF for .NET, manipulate PDF documents, save attachment to file, delete attachment from PDF",
    "wordcount": "181",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "Gunakan C# PDF API untuk mengakses, menambahkan, dan menghapus lampiran dalam file PDF menggunakan C# dari dalam aplikasi Anda. Panduan lengkap dengan contoh kode C#."
}
</script>

Dalam bagian ini, kami akan menjelaskan cara bekerja dengan lampiran di PDF menggunakan Aspose.PDF for .NET.
Lampiran adalah file tambahan yang dilampirkan ke dokumen induk, bisa berupa berbagai jenis file, seperti pdf, word, gambar, atau file lainnya.
Anda akan belajar cara menambahkan lampiran ke pdf, mendapatkan informasi tentang lampiran, dan menyimpannya ke file, menghapus lampiran dari PDF secara programatis dengan C#.

- [Menambahkan lampiran ke dokumen PDF](/pdf/id/net/add-attachment-to-pdf-document/)
- [Ekstrak dan simpan lampiran](/pdf/id/net/extract-and-save-an-attachment/)
- [Menghapus lampiran dari PDF yang ada](/pdf/id/net/removing-attachment-from-an-existing-pdf/)
- [Portofolio](/pdf/id/net/portfolio/)

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