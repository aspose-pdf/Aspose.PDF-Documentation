---
title: Bekerja dengan AcroForms
linktitle: AcroForms
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/acroforms/
description: Dengan Aspose.PDF for .NET Anda dapat membuat formulir dari awal, mengisi kolom formulir dalam dokumen PDF, mengekstrak data dari formulir, dan lain-lain.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET memperkenalkan kemampuan yang ditingkatkan untuk bekerja dengan AcroForms, memungkinkan pengguna untuk secara efisien membuat formulir dari awal, mengisi kolom PDF, dan mengekstrak data dengan mulus. Fitur kuat ini mendukung integrasi beberapa catatan database, memungkinkan manajemen formulir yang dinamis dan pengalaman pengguna yang lebih lancar.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Dasar-Dasar AcroForms

**AcroForms** adalah teknologi formulir PDF yang asli. AcroForms adalah formulir yang berorientasi halaman. Mereka pertama kali diperkenalkan pada tahun 1998. Mereka menerima input dalam Format Data Formulir atau FDF dan Format Data Formulir XML atau xFDF. Vendor pihak ketiga mendukung AcroForms. Ketika Adobe memperkenalkan AcroForms, mereka menyebutnya sebagai "formulir PDF yang dibuat dengan Adobe Acrobat Pro/Standard dan bukan jenis formulir XFA statis atau dinamis yang khusus. Acroforms dapat dipindahkan dan berfungsi di semua platform.

Anda dapat menggunakan AcroForms untuk menambahkan halaman tambahan ke dokumen formulir PDF. Berkat konsep Template, Anda dapat menggunakan AcroForms untuk mendukung pengisian formulir dengan beberapa catatan database.

PDF 1.7 mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF.

*AcroForms (juga dikenal sebagai formulir Acrobat)*, diperkenalkan dan termasuk dalam spesifikasi format PDF 1.2.

*Arsitektur Formulir XML Adobe (XFA)*, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk).

Untuk memahami **Acroforms** vs **XFA** formulir, kita perlu memahami dasar-dasarnya terlebih dahulu. Untuk memulai, keduanya adalah formulir PDF yang dapat Anda gunakan. Acroforms adalah yang lebih tua, dibuat pada tahun 1998, dan masih disebut sebagai formulir PDF klasik. Formulir XFA adalah halaman web yang dapat Anda simpan sebagai PDF, dan muncul pada tahun 2003. Butuh waktu sebelum PDF mulai menerima formulir XFA.

AcroForms memiliki kemampuan yang tidak ditemukan di XFA dan sebaliknya XFA memiliki beberapa kemampuan yang tidak ditemukan di AcroForms. Sebagai contoh:

- AcroForms mendukung konsep "Template", memungkinkan halaman tambahan ditambahkan ke dokumen formulir PDF untuk mendukung pengisian formulir dengan beberapa catatan database.
- XFA mendukung konsep aliran dokumen yang memungkinkan kolom untuk mengubah ukuran jika diperlukan untuk mengakomodasi data.

Untuk pembelajaran yang lebih mendetail tentang kemampuan pustaka Java, lihat artikel berikut:

- [Buat AcroForm](/pdf/net/create-form) - buat formulir dari awal dengan C#.
- [Isi AcroForm](/pdf/net/fill-form) - isi kolom formulir dalam dokumen PDF Anda.
- [Ekstrak AcroForm](/pdf/net/extract-form) - dapatkan nilai dari semua atau kolom individu dokumen PDF.
- [Modifikasi AcroForm](/pdf/net/modifing-form) - dapatkan atau atur FieldLimit, atur font kolom formulir, dan lain-lain.
- [Posting Data AcroForm](/pdf/net/posting-acroform-data/) - impor dan ekspor data formulir ke dan dari file XML.
- [Impor dan Ekspor Data](/pdf/net/import-and-export-data/) - impor dan ekspor data menggunakan Kelas Formulir.
- [Hapus Formulir dari PDF](/pdf/net/remove-form/) - hapus Teks berdasarkan subtype/form, hapus semua formulir.
- [Impor dan Ekspor Data dalam JSON](/pdf/net/import-export-json/) - impor dan ekspor data dengan JSON

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