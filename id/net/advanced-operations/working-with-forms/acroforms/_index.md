---
title: Bekerja dengan AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /id/net/acroforms/
description: Dengan Aspose.PDF untuk .NET Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, dan lain-lain.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan AcroForms",
    "alternativeHeadline": "Opsi untuk bekerja dengan AcroForms dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, acroforms dalam pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "Dengan Aspose.PDF untuk .NET Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, dan lain-lain."
}
</script>

## Dasar-dasar AcroForms

**AcroForms** adalah teknologi formulir PDF yang asli. AcroForms adalah formulir berorientasi halaman. Mereka pertama kali diperkenalkan pada tahun 1998. Mereka menerima input dalam Format Data Formulir atau FDF dan Format Data Formulir XML atau xFDF. Vendor pihak ketiga mendukung AcroForms. Ketika Adobe memperkenalkan AcroForms, mereka menyebutnya sebagai "formulir PDF yang dibuat dengan Adobe Acrobat Pro/Standard dan bukan jenis formulir XFA statis atau dinamis yang khusus. Acroforms portabel dan mereka bekerja di semua platform.

Anda dapat menggunakan AcroForms untuk menambahkan halaman tambahan ke dokumen formulir PDF. Berkat konsep Template, Anda dapat menggunakan AcroForms untuk mendukung pengisian formulir dengan beberapa catatan database.

PDF 1.7 mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF.

*AcroForms (juga dikenal sebagai formulir Acrobat)*, diperkenalkan dan termasuk dalam spesifikasi format PDF 1.2.

*Formulir Adobe XML Forms Architecture (XFA)*, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.)
*Formulir Adobe XML Forms Architecture (XFA)*, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.

Untuk memahami **Acroforms** vs **XFA** forms, kita perlu memahami dasar-dasarnya terlebih dahulu. Sebagai permulaan, keduanya adalah formulir PDF yang dapat Anda gunakan. Acroforms adalah yang lebih tua, dibuat kembali pada tahun 1998, dan masih disebut sebagai formulir PDF klasik. Formulir XFA adalah halaman web yang dapat Anda simpan sebagai PDF, dan muncul kembali pada tahun 2003. Butuh waktu sebelum PDF mulai menerima formulir XFA.

AcroForms memiliki kemampuan yang tidak ditemukan di XFA dan sebaliknya XFA memiliki beberapa kemampuan yang tidak ditemukan di AcroForms. Misalnya:

- AcroForms mendukung konsep "Templates", memungkinkan halaman tambahan untuk ditambahkan ke dokumen formulir PDF untuk mendukung pengisian formulir dengan beberapa catatan database.
- XFA mendukung konsep aliran dokumen ulang yang memungkinkan suatu bidang untuk diubah ukurannya jika diperlukan untuk mengakomodasi data.

Untuk pembelajaran lebih rinci tentang kemampuan dari perpustakaan Java, lihat artikel-artikel berikut:
Untuk mempelajari lebih lanjut kemampuan dari perpustakaan Java, lihat artikel berikut:

- [Buat AcroForm](/pdf/id/net/create-form) - buat formulir dari awal dengan C#.
- [Isi AcroForm](/pdf/id/net/fill-form) - isi bidang formulir dalam dokumen PDF Anda.
- [Ekstrak AcroForm](/pdf/id/net/extract-form) - dapatkan nilai dari semua atau satu bidang dokumen PDF.
- [Memodifikasi AcroForm](/pdf/id/net/modifing-form) - dapatkan atau atur FieldLimit, atur font bidang formulir, dan lainnya.
- [Mengirimkan Data AcroForm](/pdf/id/net/posting-acroform-data/) - impor dan ekspor data formulir ke dan dari file XML.
- [Impor dan Ekspor Data](/pdf/id/net/import-and-export-data/) - impor dan ekspor data menggunakan Form Class.

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

