---
title: Bekerja dengan Grafik dalam Berkas PDF
linktitle: Bekerja dengan Grafik
type: docs
weight: 70
url: /id/net/graphs/
description: Artikel ini menjelaskan apa itu Grafik, cara membuat objek persegi panjang yang terisi, dan fungsi lainnya
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Bekerja dengan Grafik dalam Berkas PDF",
    "alternativeHeadline": "Cara membuat grafik dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, grafik dalam pdf",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "dateModified": "2022-02-04",
    "description": "Artikel ini menjelaskan apa itu Grafik, cara membuat objek persegi panjang yang terisi, dan fungsi lainnya"
}
</script>
## Apa itu Grafik

Menambahkan grafik ke dalam dokumen PDF adalah tugas yang sangat umum bagi pengembang saat bekerja dengan Adobe Acrobat Writer atau aplikasi pengolah PDF lainnya. Terdapat banyak jenis grafik yang dapat digunakan dalam aplikasi PDF.
[Aspose.PDF for .NET](/pdf/id/net/) juga mendukung penambahan grafik ke dalam dokumen PDF. Untuk tujuan ini, kelas Graph disediakan. Graph adalah elemen tingkat paragraf dan dapat ditambahkan ke koleksi Paragraphs dalam instance Page. Sebuah instance Graph berisi koleksi Shapes.

Berikut adalah jenis-jenis bentuk yang didukung oleh kelas [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/id/net/add-arc/) - terkadang juga disebut bendera adalah pasangan berurutan dari verteks yang berdekatan, tetapi terkadang juga disebut garis berarah.
- [Circle](/pdf/id/net/add-circle/) - menampilkan data menggunakan lingkaran yang dibagi menjadi sektor. Kami menggunakan grafik lingkaran (juga disebut diagram lingkaran) untuk menunjukkan bagaimana data mewakili bagian dari satu keseluruhan atau satu kelompok.
- [Curve](/pdf/id/net/add-curve/) - adalah gabungan terhubung dari garis proyektif, setiap garis bertemu tiga lainnya di titik ganda biasa.
- [Curve](/pdf/id/net/add-curve/) - adalah gabungan terhubung dari garis proyektif, setiap garis bertemu tiga garis lainnya di titik ganda biasa.
- [Line](/pdf/id/net/add-line) - grafik garis digunakan untuk menampilkan data berkelanjutan dan dapat berguna dalam memprediksi peristiwa masa depan ketika mereka menunjukkan tren dari waktu ke waktu.
- [Rectangle](/pdf/id/net/add-rectangle/) - adalah salah satu dari banyak bentuk dasar yang akan Anda lihat dalam grafik, ini dapat sangat berguna dalam membantu Anda memecahkan masalah.
- [Ellipse](/pdf/id/net/add-ellipse/) - adalah kumpulan titik di bidang, menciptakan bentuk melengkung, oval.

Detail di atas juga digambarkan dalam gambar di bawah ini:

![Figures in Graphs](graphs.png)

