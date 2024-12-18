---
title: Membuat Tautan dalam Berkas PDF dengan C#
linktitle: Membuat Tautan
type: docs
weight: 10
url: /id/net/create-links/
description: Bagian ini menjelaskan bagaimana cara membuat tautan dalam dokumen PDF Anda dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Membuat Tautan dalam Berkas PDF dengan C#",
    "alternativeHeadline": "Cara Membuat Tautan dalam PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, membuat tautan dalam pdf",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Bagian ini menjelaskan bagaimana cara membuat tautan dalam dokumen PDF Anda dengan C#."
}
</script>

Kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Membuat Tautan

Dengan menambahkan tautan ke aplikasi dalam dokumen, adalah mungkin untuk menghubungkan aplikasi dari dokumen. Ini berguna ketika Anda ingin pembaca melakukan tindakan tertentu pada titik tertentu dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur. Untuk membuat tautan aplikasi:

1. [Buat Objek Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda tambahkan tautan.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Halaman dan [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Saat membuat objek [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction), tentukan aplikasi yang ingin Anda jalankan.
1. Tambahkan tautan ke properti [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) dari objek Page.
1. Akhirnya, simpan PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek Document.

Berikut ini adalah potongan kode yang menunjukkan cara membuat tautan ke aplikasi dalam berkas PDF.

```csharp
// Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Buka dokumen
Document document = new Document(dataDir + "CreateApplicationLink.pdf");

// Buat tautan
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// Simpan dokumen yang telah diperbarui
document.Save(dataDir);
```
### Membuat Tautan Dokumen PDF dalam Berkas PDF

Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan tautan ke berkas PDF eksternal sehingga Anda dapat menghubungkan beberapa dokumen bersama-sama. Untuk membuat tautan dokumen PDF:

1. Pertama, buat objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Kemudian, dapatkan [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) tertentu yang ingin Anda tambahkan tautan kepadanya.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Page dan [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Atur properti Action ke objek [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. Tambahkan tautan ke koleksi Anotasi objek Halaman.
1. Simpan PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) dari objek Dokumen.

Berikut adalah potongan kode yang menunjukkan cara membuat tautan dokumen PDF dalam file PDF.

 ```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Buka dokumen
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// Buat tautan
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// Simpan dokumen yang telah diperbarui
document.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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

