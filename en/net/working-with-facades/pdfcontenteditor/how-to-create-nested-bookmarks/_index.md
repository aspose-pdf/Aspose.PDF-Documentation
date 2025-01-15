---
title: Adding Bookmarks to PDF file
type: docs
weight: 20
url: /net/how-to-create-nested-bookmarks/
description: This section explains how to create Nested Bookmarks with PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Bookmarks to PDF file",
    "alternativeHeadline": "Create Nested Bookmarks in PDF Documents Easily",
    "abstract": "Enhance your PDF documents with the new Nested Bookmarks feature using the PdfContentEditor class from Aspose.Pdf.Facades. This functionality allows you to create hierarchical bookmarks that organize your content effectively, enabling users to navigate easily through chapters and associated pages within the PDF. Streamline document navigation and improve user experience with this sophisticated bookmarking solution",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "211",
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
    "url": "/net/how-to-create-nested-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-create-nested-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Bookmarks give you the option to keep track/link to specific page inside the PDF document. [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) class in [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) provides a feature which allows you to create your own bookmark in a sophisticated yet intuitive way within an existing PDF file, at a given page or all pages.

## Implementation details

Other than the creation of simple bookmarks, sometimes you have a requirement to create a bookmark in the form of chapters where you nest the individual bookmarks inside of the chapter bookmarks so that when you click on the + sign for a chapter you would see the pages inside when the bookmarks expands, as shown in the picture below .

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

        // Saves the result PDF to file
        editor.Save(dataDir + "PdfContentEditorDemo_Bookmark.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBookmarksAction()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Saves the result PDF to file
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}
