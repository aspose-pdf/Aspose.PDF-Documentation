---
title: Menggunakan OneClick PDF Document Generator
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/using-oneclick-pdf-document-generator/
description: Pelajari cara menggunakan Aspose.PDF OneClick PDF Document Generator di Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Buka generasi dokumen yang mulus di Microsoft Dynamics dengan Aspose.PDF OneClick PDF Document Generator. Fitur inovatif ini memungkinkan pengguna untuk membuat template PDF yang dapat disesuaikan langsung di dalam CRM, menghasilkan dokumen secara efisien dengan satu klik, dan dengan mudah mengintegrasikan tombol OneClick ke dalam formulir untuk akses yang lebih mudah. Tingkatkan kemampuan manajemen data Anda dan tingkatkan produktivitas dengan alat yang kuat ini",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Buat Template dan Tambahkan di CRM

- Buka Word dan buat template.
- Masukkan bidang MailMerge untuk data yang berasal dari CRM.

![Insert MailMerg fields](using-oneclick-pdf-document-generator_1.png)

- Pastikan bahwa nama Field cocok persis dengan field CRM.
- Template spesifik untuk digunakan dengan entitas individu.

![Demo Template](using-oneclick-pdf-document-generator_2.png)

- Setelah Template dibuat, buka entitas Konfigurasi OneClick PDF di CRM dan buat catatan baru.
- Beri nama template, pilih entitas yang ditentukan untuk template dan lampirkan dokumen yang dibuat di lampiran.

![Select Template](using-oneclick-pdf-document-generator_3.png)

## Hasilkan Dokumen dari Tombol Ribbon

- Buka Catatan di mana Anda ingin menghasilkan dokumen. (Pastikan template sudah dilampirkan dalam konfigurasi untuk entitas tersebut)
- Klik tombol OneClick PDF dari ribbon.

![Click OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Dari Popup: Pilih template, Nama File dan Aksi dan Klik Hasilkan.
- Periksa file yang diunduh atau Catatan, berdasarkan pilihan.

## Konfigurasi Tombol OneClick dan gunakan

- Untuk menggunakan Tombol OneClick langsung dari Formulir, buka Kustomisasi Formulir.
- Masukkan WebResource di mana Anda ingin menambahkan Tombol OneClick.
- Pilih OpenButtonPage di Webresource dan beri Nama.
- Konfigurasikan Tombol di bidang Data dalam contoh berikut.

![WebResource Properties](using-oneclick-pdf-document-generator_5.png)

- Gunakan baris terpisah untuk setiap tombol dan gunakan sintaks berikut:
  - Sintaks: Nama Template |<Aksi: Unduh/Catatan>|Nama File Output
  - Contoh:Demo|Unduh|File Saya yang Diunduh
- Simpan dan terbitkan kustomisasi.
- Tombol tersedia di formulir.

![The button is available on the form](using-oneclick-pdf-document-generator_6.png)