---
title: Bekerja dengan Grafik dalam file PDF
linktitle: Bekerja dengan Grafik
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /id/net/working-with-graphs/
description: Artikel ini menjelaskan apa itu Grafik, bagaimana cara membuat objek persegi panjang terisi, dan fungsi lainnya
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Temukan fitur baru yang kuat untuk menghasilkan dan memanipulasi grafik dalam dokumen PDF menggunakan Aspose.PDF for .NET. Fungsionalitas ini memungkinkan pengembang untuk membuat berbagai bentuk grafik, termasuk busur, lingkaran, garis, dan persegi panjang, meningkatkan presentasi visual data dalam aplikasi mereka. Optimalkan proses pembuatan PDF Anda dan sampaikan visualisasi data dinamis dengan mudah",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2024-11-25",
    "description": "Artikel ini menjelaskan apa itu Grafik, bagaimana cara membuat objek persegi panjang terisi, dan fungsi lainnya"
}
</script>

## Apa itu Grafik

Menambahkan grafik ke dokumen PDF adalah tugas yang sangat umum bagi pengembang saat bekerja dengan Adobe Acrobat Writer atau aplikasi pemrosesan PDF lainnya. Ada banyak jenis grafik yang dapat digunakan dalam aplikasi PDF.
[Aspose.PDF for .NET](/pdf/net/) juga mendukung penambahan grafik ke dokumen PDF. Untuk tujuan ini, kelas Grafik disediakan. Grafik adalah elemen tingkat paragraf dan dapat ditambahkan ke koleksi Paragraf dalam instance Halaman. Sebuah instance Grafik berisi koleksi Bentuk.

Jenis bentuk berikut didukung oleh kelas [Grafik](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Busur](/pdf/net/add-arc/) - kadang-kadang juga disebut bendera adalah pasangan terurut dari simpul yang berdekatan, tetapi kadang-kadang juga disebut garis terarah.
- [Lingkaran](/pdf/net/add-circle/) - menampilkan data menggunakan lingkaran yang dibagi menjadi sektor. Kami menggunakan grafik lingkaran (juga disebut diagram pai) untuk menunjukkan bagaimana data mewakili bagian dari satu keseluruhan atau satu kelompok.
- [Kurva](/pdf/net/add-curve/) - adalah persatuan terhubung dari garis proyektif, setiap garis bertemu tiga garis lainnya di titik ganda biasa.
- [Garis](/pdf/net/add-line) - grafik garis digunakan untuk menampilkan data kontinu dan dapat berguna dalam memprediksi peristiwa di masa depan ketika menunjukkan tren dari waktu ke waktu.
- [Persegi panjang](/pdf/net/add-rectangle/) - adalah salah satu dari banyak bentuk dasar yang akan Anda lihat dalam grafik, ini bisa sangat berguna dalam membantu Anda menyelesaikan masalah.
- [Elips](/pdf/net/add-ellipse/) - adalah sekumpulan titik pada bidang, menciptakan bentuk oval yang melengkung.

Detail di atas juga digambarkan dalam gambar di bawah ini:

![Gambar dalam Grafik](graphs.png)


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