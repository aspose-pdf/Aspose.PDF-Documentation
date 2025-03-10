---
title: Impor dan Ekspor Bookmark
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/import-and-export-bookmarks/
description: Bagian ini menjelaskan cara mengimpor dan mengekspor Bookmark dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Bookmarks",
    "alternativeHeadline": "Seamlessly Import and Export PDF Bookmarks with XML",
    "abstract": "Temukan fitur baru Impor dan Ekspor Bookmark di Aspose.PDF for .NET, yang memungkinkan pengguna untuk mengimpor bookmark dari file XML ke dokumen PDF yang ada dan mengekspor bookmark kembali ke XML. Fungsionalitas ini meningkatkan manajemen dokumen dengan menyederhanakan integrasi bookmark, menyediakan proses yang sederhana untuk mempertahankan struktur organisasi dalam PDF. Optimalkan alur kerja Anda dan tingkatkan kemampuan penanganan PDF Anda dengan tambahan yang kuat ini.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/import-and-export-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Impor Bookmark dari XML ke File PDF yang Ada

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) metode memungkinkan Anda untuk mengimpor bookmark ke dalam file PDF dari file XML. Untuk mengimpor bookmark, Anda perlu membuat objek [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, Anda perlu memanggil metode [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). Terakhir, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Potongan kode berikut menunjukkan cara mengimpor bookmark dari file XML.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

        // Import bookmarks
        bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

    // Import bookmarks
    bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Ekspor Bookmark ke XML dari File PDF yang Ada

Metode ExportBookmarksToXml memungkinkan Anda untuk mengekspor bookmark dari file PDF ke file XML.

Untuk mengekspor bookmark:

1. Buat objek PdfBookmarkEditor dan ikat file PDF menggunakan metode BindPdf.
1. Panggil metode ExportBookmarksToXml.
1. Simpan file PDF yang diperbarui menggunakan metode Save.

Potongan kode berikut menunjukkan cara mengekspor bookmark ke file XML.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}