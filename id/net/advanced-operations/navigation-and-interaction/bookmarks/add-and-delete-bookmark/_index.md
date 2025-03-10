---
title: Tambahkan dan Hapus Bookmark
linktitle: Tambahkan dan Hapus Bookmark
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-and-delete-bookmark/
description: Anda dapat menambahkan bookmark ke dokumen PDF dengan C#. Anda dapat menghapus semua atau bookmark tertentu dari dokumen PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add and Delete a Bookmark",
    "alternativeHeadline": "Manage PDF Bookmarks: Add and Delete with Ease",
    "abstract": "Fitur baru ini memungkinkan pengguna untuk mengelola bookmark dalam dokumen PDF dengan efisien menggunakan C#. Anda dapat dengan mudah menambahkan bookmark baru atau menghapus yang sudah ada, baik Anda ingin menghapus semua bookmark atau menargetkan entri tertentu. Fungsionalitas ini meningkatkan navigasi dan organisasi dokumen untuk pengalaman pengguna yang lebih baik.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add bookmark, delete bookmark, PDF document, C# programming, OutlineItemCollection, OutlineCollection, child bookmark, parent bookmark",
    "wordcount": "851",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "Anda dapat menambahkan bookmark ke dokumen PDF dengan C#. Anda dapat menghapus semua atau bookmark tertentu dari dokumen PDF."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) library.

## Tambahkan Bookmark ke Dokumen PDF

Bookmark disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) objek Document, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Untuk menambahkan bookmark ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat bookmark dan tentukan propertinya.
1. Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) ke koleksi Outlines.

Potongan kode berikut menunjukkan cara menambahkan bookmark dalam dokumen PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf"))
    {
        // Create a bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Test Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Set the destination page number
        pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

        // Add bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddBookmark.pdf");

    // Create a bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Test Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Set the destination page number
    pdfOutline.Action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[1]);

    // Add bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Tambahkan Bookmark Anak ke Dokumen PDF

Bookmark dapat dinesting, menunjukkan hubungan hierarkis dengan bookmark induk dan anak. Artikel ini menjelaskan cara menambahkan bookmark anak, yaitu, bookmark tingkat kedua, ke PDF.

Untuk menambahkan bookmark anak ke file PDF, pertama tambahkan bookmark induk:

1. Buka dokumen.
1. Tambahkan bookmark ke [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) objek Document.

Bookmark anak dibuat seperti bookmark induk, yang dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines bookmark induk.

Potongan kode berikut menunjukkan cara menambahkan bookmark anak ke dokumen PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf"))
    {
        // Create a parent bookmark object
        var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfOutline.Title = "Parent Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Create a child bookmark object
        var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
        pdfChildOutline.Title = "Child Outline";
        pdfChildOutline.Italic = true;
        pdfChildOutline.Bold = true;

        // Add child bookmark in parent bookmark's collection
        pdfOutline.Add(pdfChildOutline);

        // Add parent bookmark in the document's outline collection.
        document.Outlines.Add(pdfOutline);

        // Save PDF document
        document.Save(dataDir + "AddChildBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddChildBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddChildBookmark.pdf");

    // Create a parent bookmark object
    var pdfOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfOutline.Title = "Parent Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Create a child bookmark object
    var pdfChildOutline = new Aspose.Pdf.OutlineItemCollection(document.Outlines);
    pdfChildOutline.Title = "Child Outline";
    pdfChildOutline.Italic = true;
    pdfChildOutline.Bold = true;

    // Add child bookmark in parent bookmark's collection
    pdfOutline.Add(pdfChildOutline);

    // Add parent bookmark in the document's outline collection.
    document.Outlines.Add(pdfOutline);

    // Save PDF document
    document.Save(dataDir + "AddChildBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Semua Bookmark dari Dokumen PDF

Semua bookmark dalam PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Artikel ini menjelaskan cara menghapus semua bookmark dari file PDF.

Untuk menghapus semua bookmark dari file PDF:

1. Panggil metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Simpan file yang dimodifikasi menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Potongan kode berikut menunjukkan cara menghapus semua bookmark dari dokumen PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf"))
    {
        // Delete all bookmarks
        document.Outlines.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks
    document.Outlines.Delete();

    // Save PDF document
    document.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Hapus Bookmark Tertentu dari Dokumen PDF

Untuk menghapus bookmark tertentu dari file PDF:

1. Berikan judul bookmark sebagai parameter ke metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Kemudian simpan file yang diperbarui dengan metode Save objek Document.

Kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Metode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) menghapus bookmark dengan judul yang diberikan ke metode.

Potongan kode berikut menunjukkan cara menghapus bookmark tertentu dari dokumen PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf"))
    {
        // Delete particular outline by Title
        document.Outlines.Delete("Child Outline");

        // Save PDF document
        document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularBookmark.pdf");

    // Delete particular outline by Title
    document.Outlines.Delete("Child Outline");

    // Save PDF document
    document.Save(dataDir + "DeleteParticularBookmark_out.pdf");
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