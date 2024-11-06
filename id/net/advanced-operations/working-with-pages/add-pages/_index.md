---
title: Menambahkan Halaman ke Dokumen PDF
linktitle: Tambah Halaman
type: docs
weight: 10
url: id/net/add-pages/
description: Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambah Halaman di PDF dengan C#",
    "alternativeHeadline": "Cara menambah Halaman dalam dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, tambah halaman pdf, sisipkan halaman pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman pada lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan C#."
}
</script>
Aspose.PDF untuk .NET API memberikan fleksibilitas penuh untuk bekerja dengan halaman dalam dokumen PDF menggunakan C# atau bahasa .NET lainnya. Ini mempertahankan semua halaman dokumen PDF dalam [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) yang dapat digunakan untuk bekerja dengan halaman PDF.
Aspose.PDF untuk .NET memungkinkan Anda memasukkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.
Bagian ini menunjukkan cara menambahkan halaman ke PDF menggunakan C#.

## Tambah atau Sisipkan Halaman dalam File PDF

Aspose.PDF untuk .NET memungkinkan Anda memasukkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Sisipkan Halaman Kosong di File PDF di Lokasi yang Diinginkan

Untuk memasukkan halaman kosong dalam file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF masukan.
1. 
1. Simpan output PDF menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara Anda memasukkan halaman dalam file PDF.

```cs
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// Masukkan halaman kosong dalam PDF
pdfDocument.Pages.Insert(2);
// Simpan file output
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

Dalam contoh di atas, kami menambahkan halaman kosong dengan parameter default. Jika Anda perlu membuat ukuran halaman sama dengan halaman lain dalam dokumen, Anda harus menambahkan beberapa baris kode:

```cs
var page = pdfDocument.Pages.Insert(2);
//salin parameter halaman dari halaman 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen berakhir di halaman kosong. Topik ini menjelaskan cara memasukkan halaman kosong di akhir dokumen PDF.

Untuk memasukkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF masukan.
1. Panggil metode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), tanpa parameter apa pun.
1. Simpan PDF keluaran menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara memasukkan halaman kosong di akhir file PDF.

```cs
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Sisipkan halaman kosong di akhir file PDF
pdfDocument.Pages.Add();

// Simpan file keluaran
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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
```

