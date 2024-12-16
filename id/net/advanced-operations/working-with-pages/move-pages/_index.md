---
title: Memindahkan Halaman PDF secara Programatis C#
linktitle: Memindahkan Halaman PDF
type: docs
weight: 20
url: /id/net/move-pages/
description: Cobalah memindahkan halaman ke lokasi yang diinginkan atau di akhir file PDF menggunakan Aspose.PDF untuk .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memindahkan Halaman PDF secara Programatis C#",
    "alternativeHeadline": "Cara memindahkan Halaman PDF dengan .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen PDF",
    "keywords": "pdf, c#, memindahkan halaman pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumentasi Aspose.PDF",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Cobalah memindahkan halaman ke lokasi yang diinginkan atau di akhir file PDF menggunakan Aspose.PDF untuk .NET."
}
</script>
## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Topik ini menjelaskan cara memindahkan halaman dari satu dokumen PDF ke akhir dokumen lain menggunakan C#.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Untuk memindahkan halaman kita harus:

1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF sumber.
1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF tujuan.
1. Mendapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Menambahkan](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) halaman ke dokumen tujuan.
1. Menyimpan output PDF menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Menghapus](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) halaman di dokumen sumber.
1.
1.

Potongan kode berikut ini menunjukkan cara memindahkan satu halaman.

```csharp
var srcFileName = "<masukkan nama file>";
var dstFileName = "<masukkan nama file>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// Simpan file output
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## Memindahkan Sekumpulan Halaman dari Satu Dokumen PDF ke Dokumen PDF Lain

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF sumber.
2. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF tujuan.
3. Tentukan sebuah array dengan nomor halaman yang akan dipindahkan.
4. Jalankan loop melalui array:
    1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    2.
1. Simpan output PDF menggunakan metode [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Hapus](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) halaman dalam dokumen sumber menggunakan array.
1. Simpan PDF sumber menggunakan metode [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Berikut ini adalah potongan kode yang menunjukkan cara memindahkan sejumlah halaman dari satu dokumen PDF ke dokumen PDF lainnya.

```csharp
var srcFileName = "<masukkan nama file>";
var dstFileName = "<masukkan nama file>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// Simpan file output
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## Memindahkan Halaman ke Lokasi Baru dalam Dokumen PDF Saat Ini

1.
1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Tambahkan](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) halaman ke lokasi baru (misalnya ke akhir).
1. [Hapus](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) halaman di lokasi sebelumnya.
1. Simpan PDF keluaran menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<masukkan nama file>";
var dstFileName = "<masukkan nama file>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Simpan file keluaran
srcDocument.Save(dstFileName);
```

