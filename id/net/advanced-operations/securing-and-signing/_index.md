---
title: Mengamankan dan menandatangani PDF di C#
linktitle: Mengamankan dan menandatangani di PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /id/net/securing-and-signing/
description: Bagian ini menjelaskan fitur-fitur menggunakan tanda tangan dan mengamankan dokumen PDF Anda menggunakan C#
lastmod: "2024-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "Temukan kemampuan canggih untuk mengamankan dan menandatangani dokumen PDF secara digital menggunakan C#. Fitur ini memungkinkan pengguna untuk menerapkan tanda tangan digital yang kuat dengan berbagai algoritma dan opsi digest, memastikan integritas dan keaslian dokumen. Tingkatkan keamanan PDF Anda dengan fungsionalitas penandatanganan komprehensif Aspose.PDF yang dirancang untuk integrasi yang mulus dalam aplikasi .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "302",
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
    "url": "/net/securing-and-signing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/securing-and-signing/"
    },
    "dateModified": "2024-02-07",
    "description": "Bagian ini menjelaskan fitur-fitur menggunakan tanda tangan dan mengamankan dokumen PDF Anda menggunakan C#"
}
</script>

Bagian ini menjelaskan bagaimana cara menandatangani dokumen PDF secara digital dengan aman menggunakan C#. Istilah tanda tangan elektronik dan tanda tangan digital digunakan secara bergantian, tetapi pada dasarnya keduanya berbeda. Secara umum, tanda tangan digital dilengkapi dengan segel yang disetujui oleh [otoritas sertifikasi](https://en.wikipedia.org/wiki/Certificate_authority) dan digunakan untuk melindungi dokumen yang ditandatangani dari pemalsuan. Sebaliknya, tanda tangan elektronik sering digunakan untuk menunjukkan niat untuk menandatangani dokumen.

Aspose.PDF mendukung tanda tangan digital:
- PKCS1 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 dengan algoritma tanda tangan RSA dan digest SHA-1.
- PKCS7 terpisah dengan algoritma tanda tangan DSA, RSA, dan ECDSA. Algoritma digest yang didukung tergantung pada algoritma tanda tangan.
- Tanda tangan timestamp.

Algoritma digest untuk PKCS7 terpisah:
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Disarankan untuk menghindari tanda tangan digital dengan algoritma digest SHA-1 karena ketidakamanannya.

- [Menandatangani file PDF secara digital](/pdf/net/digitally-sign-pdf-file/)
- [Atur Hak Istimewa, Enkripsi dan Dekripsi File PDF](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Ekstrak Informasi Gambar dan Tanda Tangan](/pdf/net/extract-image-and-signature-information/)
- [Tandatangani Dokumen PDF Dari Kartu Pintar](/pdf/net/sign-pdf-document-from-smart-card/)

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