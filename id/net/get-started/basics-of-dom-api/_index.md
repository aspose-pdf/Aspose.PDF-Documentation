---
title: Dasar-Dasar Aspose.PDF DOM API
linktitle: Dasar-Dasar DOM API
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /id/net/basics-of-dom-api/
description: Aspose.PDF for .NET juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam istilah objek.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "API DOM Aspose.PDF for .NET yang baru menyediakan pendekatan berorientasi objek yang kuat untuk memanipulasi dokumen PDF dengan merepresentasikan strukturnya sebagai pohon hierarkis. Fitur ini memungkinkan pengembang untuk dengan mudah mengakses, memperbarui, dan mengekspor elemen PDF sambil meningkatkan fleksibilitas dan kontrol atas manipulasi dokumen melalui antarmuka pemrograman yang intuitif.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Pengenalan ke API DOM

Model Objek Dokumen (DOM) adalah bentuk representasi dokumen terstruktur sebagai model berorientasi objek. DOM adalah standar resmi World Wide Web Consortium (W3C) untuk merepresentasikan dokumen terstruktur dengan cara yang netral terhadap platform dan bahasa.

Dengan kata sederhana, DOM adalah pohon objek yang merepresentasikan struktur dari beberapa dokumen. Aspose.PDF for .NET juga menggunakan ide DOM untuk merepresentasikan struktur dokumen PDF dalam istilah objek. Namun, aspek-aspek dari DOM (seperti Elemen-nya) dimanipulasi dalam sintaks bahasa pemrograman yang digunakan. Antarmuka publik dari sebuah DOM ditentukan dalam antarmuka pemrograman aplikasinya (API).

### Pengenalan ke Dokumen PDF

Format Dokumen Portabel (PDF) adalah standar terbuka untuk pertukaran dokumen. Dokumen PDF adalah kombinasi dari teks dan data biner. Jika Anda membukanya di editor teks, Anda akan melihat objek mentah yang mendefinisikan struktur dan isi dokumen.

Struktur logis dari file PDF bersifat hierarkis dan menentukan urutan di mana aplikasi tampilan menggambar halaman dokumen dan isinya. Sebuah PDF terdiri dari empat komponen: objek, struktur file, struktur dokumen, dan aliran konten.

### Struktur Dokumen PDF

Karena struktur file PDF bersifat hierarkis, Aspose.PDF for .NET juga mengakses elemen dengan cara yang sama. Hierarki berikut menunjukkan kepada Anda bagaimana dokumen PDF secara logis terstruktur dan bagaimana API DOM Aspose.PDF for .NET menyusunnya.

![Struktur Dokumen PDF](../images/structure.png)

### Mengakses Elemen Dokumen PDF

Objek Dokumen berada di tingkat akar dari model objek. API DOM Aspose.PDF for .NET memungkinkan Anda untuk membuat objek Dokumen dan kemudian mengakses semua objek lain dalam hierarki. Anda dapat mengakses koleksi seperti Halaman atau elemen individu seperti Halaman, dll. API DOM menyediakan titik masuk dan keluar tunggal untuk memanipulasi dokumen PDF seperti yang ditunjukkan di bawah ini:

- Buka dokumen PDF.
- Akses struktur dokumen PDF dengan gaya DOM.
- Perbarui data dalam dokumen PDF.
- Validasi dokumen PDF.
- Ekspor dokumen PDF ke berbagai format.
- Akhirnya, simpan dokumen PDF yang diperbarui.

## Cara Menggunakan API Aspose.PDF for .NET yang Baru

Topik ini akan menjelaskan API Aspose.PDF for .NET yang baru dan membimbing Anda untuk memulai dengan cepat dan mudah. Harap dicatat bahwa rincian mengenai penggunaan fitur tertentu bukanlah bagian dari artikel ini.

API Aspose.PDF for .NET terdiri dari dua bagian:

- API DOM Aspose.PDF for .NET.
- Aspose.Pdf.Facades (Aspose.PDF.Kit lama untuk .NET).

Anda akan menemukan rincian dari masing-masing area ini di bawah ini.

### API DOM Aspose.PDF for .NET

API DOM Aspose.PDF for .NET sesuai dengan struktur dokumen PDF, yang membantu Anda bekerja dengan dokumen PDF tidak hanya di tingkat file dan dokumen, tetapi juga di tingkat objek. Kami telah memberikan lebih banyak fleksibilitas kepada pengembang untuk mengakses semua elemen dan objek dari dokumen PDF. Menggunakan kelas-kelas dari API DOM Aspose.PDF, Anda dapat mendapatkan akses programatik ke elemen dan format dokumen. API DOM baru ini terdiri dari berbagai namespace seperti yang diberikan di bawah ini:

### Aspose.PDF

Namespace ini menyediakan kelas Dokumen yang memungkinkan Anda untuk membuka dan menyimpan dokumen PDF. Kelas Lisensi juga merupakan bagian dari namespace ini. Ini juga menyediakan kelas terkait halaman PDF, lampiran, dan bookmark seperti Halaman, KoleksiHalaman, SpesifikasiFile, KoleksiFileTertanam, KoleksiItemGaris, dan KoleksiGaris, dll.

#### Aspose.Text

Namespace ini menyediakan kelas yang membantu Anda bekerja dengan teks dan berbagai aspeknya, misalnya Font, KoleksiFont, RepositoriFont, GayaFont, TextAbsorber, FragmenTeks, TextFragmentAbsorber, KoleksiFragmenTeks, StatusFragmenTeks, SegmenTeks dan KoleksiSegmenTeks, dll.

#### Aspose.Text.TextOptions

Namespace ini menyediakan kelas yang memungkinkan Anda untuk mengatur berbagai opsi untuk mencari, mengedit, atau mengganti teks, misalnya OpsiEditTeks, OpsiGantiTeks dan OpsiCariTeks.

#### Aspose.InteractiveFeatures

Namespace ini berisi kelas yang membantu Anda bekerja dengan fitur interaktif dari dokumen PDF, misalnya bekerja dengan dokumen dan tindakan lainnya. Namespace ini berisi kelas seperti GoToAction, GoToRemoteAction dan GoToURIAction, dll.

#### Aspose.InteractiveFeatures.Annotations

Anotasi adalah bagian dari fitur interaktif dokumen PDF. Kami telah mendedikasikan namespace untuk anotasi. Namespace ini berisi kelas yang membantu Anda bekerja dengan anotasi, misalnya, Anotasi, KoleksiAnotasi, AnotasiLingkaran dan AnotasiTautan, dll.

#### Aspose.InteractiveFeatures.Forms

Namespace ini berisi kelas yang membantu Anda bekerja dengan formulir PDF dan bidang formulir, misalnya Formulir, Bidang, BidangKotakTeks dan KoleksiOpsi, dll.

#### Aspose.Pdf.Devices

Kami dapat melakukan berbagai operasi pada dokumen PDF seperti mengonversi dokumen PDF ke berbagai format gambar. Namun, operasi semacam itu tidak termasuk dalam objek Dokumen dan kami tidak dapat memperluas kelas Dokumen untuk operasi semacam itu. Itulah sebabnya kami telah memperkenalkan konsep Perangkat dalam API DOM baru.

#### Aspose.Pdf.Facades

Sebelum Aspose.PDF for .NET, Anda memerlukan Aspose.PDF.Kit untuk .NET untuk memanipulasi file PDF yang ada. Untuk menjalankan kode Aspose.PDF.Kit lama, Anda dapat menggunakan namespace Aspose.PDF.Facades.