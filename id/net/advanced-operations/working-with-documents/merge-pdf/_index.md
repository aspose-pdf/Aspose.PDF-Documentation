---
title: Cara Menggabungkan PDF menggunakan C#
linktitle: Menggabungkan Berkas PDF
type: docs
weight: 50
url: /id/net/merge-pdf-documents/
description: Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu berkas PDF dengan C# atau VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Cara Menggabungkan PDF menggunakan C#",
    "alternativeHeadline": "Menggabungkan Dokumen PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulasi dokumen PDF",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Halaman ini menjelaskan cara menggabungkan dokumen PDF menjadi satu berkas PDF dengan C# atau VB.NET."
}
</script>

## Menggabungkan atau mengkombinasikan beberapa PDF menjadi satu PDF dalam C#

Menggabungkan PDF dalam C# bukanlah tugas yang mudah tanpa menggunakan pustaka pihak ketiga.
Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF untuk .NET. Contoh ditulis dalam C# tetapi API juga dapat digunakan dalam bahasa pemrograman .NET lainnya seperti VB.NET. File PDF digabungkan sedemikian rupa sehingga yang pertama digabungkan di akhir dokumen lain.

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Menggabungkan File PDF menggunakan C# dan DOM

Untuk menggabungkan dua file PDF:

1. Buat dua objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), masing-masing berisi salah satu file PDF masukan.
1. Kemudian panggil metode Add dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) untuk objek Document yang ingin Anda tambahkan file PDF lain ke dalamnya.
1.
1.
1. Akhirnya, simpan file PDF keluaran menggunakan metode [Simpan](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara menggabungkan file PDF.

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Buka dokumen pertama
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Buka dokumen kedua
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Tambahkan halaman dokumen kedua ke dokumen pertama
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Simpan file keluaran yang telah digabungkan
pdfDocument1.Save(dataDir);
```

## Contoh Langsung

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis yang memungkinkan Anda untuk menyelidiki bagaimana fungsionalitas penggabungan presentasi bekerja.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Lihat juga

- [Membagi PDF menggunakan DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Memisahkan PDF menggunakan DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Menggabungkan Dokumen PDF menggunakan Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Memisahkan PDF menggunakan Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

