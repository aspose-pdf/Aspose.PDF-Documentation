---
title: Memisahkan PDF secara pemrograman
linktitle: Memisahkan file PDF
type: docs
weight: 60
url: /id/net/split-pdf-document/
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi .NET Anda dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memisahkan PDF secara pemrograman",
    "alternativeHeadline": "Cara memisahkan PDF dengan .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, memisahkan pdf",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF individu dalam aplikasi .NET Anda dengan C#."
}
</script>
## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis yang memungkinkan Anda untuk mengeksplorasi bagaimana fungsionalitas pemisahan presentasi bekerja.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara membagi halaman PDF menjadi file PDF individual dalam aplikasi .NET Anda. Untuk membagi halaman PDF menjadi file PDF satu halaman menggunakan C#, langkah-langkah berikut dapat diikuti:

1. Lakukan perulangan melalui halaman dokumen PDF melalui koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) individu ke dalam dokumen kosong
1. Simpan PDF baru menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Kode berikut ini juga dapat bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Memecah PDF menjadi beberapa file atau pdf terpisah dalam C#

Potongan kode C# berikut menunjukkan kepada Anda cara memecah halaman PDF menjadi file PDF individu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// Lakukan perulangan melalui semua halaman
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```

