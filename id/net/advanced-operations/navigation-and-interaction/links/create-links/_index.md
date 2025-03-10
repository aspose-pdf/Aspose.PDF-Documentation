---
title: Buat Tautan dalam file PDF dengan C#
linktitle: Buat Tautan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/create-links/
description: Bagian ini menjelaskan cara membuat tautan dalam dokumen PDF Anda dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Links in PDF file with C#",
    "alternativeHeadline": "Create Interactive Links in PDFs Using C#",
    "abstract": "Fitur baru ini memungkinkan pengembang untuk dengan mudah membuat tautan interaktif dalam dokumen PDF menggunakan C#. Fungsionalitas ini meningkatkan keterlibatan pengguna dengan menghubungkan ke aplikasi eksternal atau file PDF lainnya, memungkinkan pengalaman dokumen yang lebih dinamis dan kaya fitur. Ideal untuk tutorial dan membimbing pengguna, integrasi ini memberdayakan pengguna untuk menghubungkan konten secara efektif",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create Links, PDF document, C#, LinkAnnotation, LaunchAction, GoToRemoteAction, Aspose.PDF, Document object, PDF manipulation, External link",
    "wordcount": "690",
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
    "url": "/net/create-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-links/"
    },
    "dateModified": "2024-11-25",
    "description": "Bagian ini menjelaskan cara membuat tautan dalam dokumen PDF Anda dengan C#."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Buat Tautan

Dengan menambahkan tautan ke aplikasi ke dalam dokumen, dimungkinkan untuk menghubungkan ke aplikasi dari dokumen. Ini berguna ketika Anda ingin pembaca melakukan tindakan tertentu pada titik tertentu dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur. Untuk membuat tautan aplikasi:

1. [Buat objek Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Dapatkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) yang ingin Anda tambahkan tautan.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Halaman dan [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Juga, atur properti Action objek [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction).
1. Saat membuat objek [LaunchAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction), tentukan aplikasi yang ingin Anda luncurkan.
1. Tambahkan tautan ke properti [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) objek Halaman.
1. Terakhir, simpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) objek Dokumen.

Potongan kode berikut menunjukkan cara membuat tautan ke aplikasi dalam file PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateApplicationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateApplicationLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateApplicationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Buat Tautan Dokumen PDF dalam File PDF

Aspose.PDF for .NET memungkinkan Anda untuk menambahkan tautan ke file PDF eksternal sehingga Anda dapat menghubungkan beberapa dokumen bersama. Untuk membuat tautan dokumen PDF:

1. Pertama, buat objek [Dokumen](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Kemudian, dapatkan [Halaman](https://reference.aspose.com/pdf/net/aspose.pdf/page) tertentu yang ingin Anda tambahkan tautan.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) menggunakan objek Halaman dan [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation).
1. Atur properti Action ke objek [GoToRemoteAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction).
1. Saat membuat objek GoToRemoteAction, tentukan file PDF yang harus diluncurkan, serta nomor halaman yang harus dibuka.
1. Tambahkan tautan ke koleksi Annotations objek Halaman.
1. Simpan PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) objek Dokumen.

Potongan kode berikut menunjukkan cara membuat tautan dokumen PDF dalam file PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf"))
    {
        // Create link
        var page = document.Pages[1];
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
        link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
        page.Annotations.Add(link);

        // Save PDF document
        document.Save(dataDir + "CreateDocumentLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "CreateDocumentLink.pdf");

    // Create link
    var page = document.Pages[1];
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
    link.Action = new Aspose.Pdf.Annotations.GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
    page.Annotations.Add(link);

    // Save PDF document
    document.Save(dataDir + "CreateDocumentLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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