---
title: Import and Export Bookmarks
type: docs
weight: 20
url: /net/import-and-export-bookmarks/
description: This section explains how to import and export Bookmarks with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Bookmarks",
    "alternativeHeadline": "Seamlessly Import and Export PDF Bookmarks with XML",
    "abstract": "Discover the new Import and Export Bookmarks feature in Aspose.PDF for .NET, which enables users to seamlessly import bookmarks from XML files into existing PDF documents and export bookmarks back to XML. This functionality enhances document management by simplifying bookmark integration, providing a straightforward process for maintaining organizational structure within PDFs. Optimize your workflow and elevate your PDF handling capabilities with this powerful addition",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Import Bookmarks from XML to an Existing PDF File

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) method allows you to import bookmarks into a PDF file from an XML file. In order to import the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) method. Finally, save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to import bookmarks from an XML file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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

## Export Bookmarks to XML from an Existing PDF File

The ExportBookmarksToXml method allows you to export bookmarks from a PDF file to an XML file.

To export bookmarks:

1. Create a PdfBookmarkEditor object and bind the PDF file using the BindPdf method.
1. Call the ExportBookmarksToXml method.
1. Save the updated PDF file using the Save method.

The following code snippet shows you how to export bookmarks to an XML file.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

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
