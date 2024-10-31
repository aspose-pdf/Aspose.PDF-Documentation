---
title: Bekerja dengan AcroForms menggunakan Python
linktitle: AcroForms
type: docs
weight: 10
url: /python-net/acroforms/
description: Dengan Aspose.PDF untuk Python Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, dan lain-lain.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan AcroForms menggunakan Python",
    "alternativeHeadline": "Opsi untuk bekerja dengan AcroForms dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generasi dokumen pdf",
    "keywords": "pdf, python, acroforms dalam pdf",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "Dengan Aspose.PDF untuk Python Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, dan lain-lain."
}
</script>


## Dasar-dasar AcroForms

**AcroForms** - teknologi formulir PDF unik dari Adobe. AcroForms adalah formulir yang berorientasi halaman. Mereka pertama kali muncul pada tahun 1998. Mereka menerima input dalam bentuk format Data atau FDF dan format Data formulir XML atau xFDF. Penyedia pihak ketiga mendukung AcroForms. Ketika Adobe memperkenalkan AcroForms, mereka menyebutnya "formulir PDF, yang merupakan karya Adobe Acrobat Pro/Standard dan bukan jenis khusus dari formulir XFA statis atau dinamis. AcroForms dapat dipindahkan dan bekerja di semua platform.

Anda dapat menggunakan AcroForms untuk menambahkan halaman tambahan ke dokumen formulir PDF. Berkat konsep Template, Anda dapat menggunakan AcroForms untuk mendukung pengisian formulir dengan beberapa catatan database.

PDF 1.7 mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF.

*AcroForms (juga dikenal sebagai formulir Acrobat)*, diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.

Untuk pembelajaran lebih rinci tentang kemampuan perpustakaan Java, lihat artikel berikut:

- [Buat AcroForm](/pdf/python-net/create-form) - buat formulir dari awal dengan Python.
- [Isi AcroForm](/pdf/python-net/fill-form) - isi bidang formulir dalam dokumen PDF Anda.
- [Ekstrak AcroForm](/pdf/python-net/extract-form) - dapatkan nilai dari semua atau bidang individual dokumen PDF.

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