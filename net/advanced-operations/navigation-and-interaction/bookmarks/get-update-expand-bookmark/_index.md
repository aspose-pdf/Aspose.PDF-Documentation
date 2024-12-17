---
title: Get, Update and Expand a Bookmark
linktitle: Get, Update and Expand a Bookmark
type: docs
weight: 20
url: /net/get-update-and-expand-bookmark/
description: This article describes how to use bookmarks in a PDF file with our Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get, Update and Expand a Bookmark",
    "alternativeHeadline": "Effortlessly Manage PDF Bookmarks",
    "abstract": "The new Get, Update and Expand a Bookmark feature enhances the Aspose.PDF for .NET library by providing users with the capability to retrieve, modify, and visually expand bookmarks within PDF documents. This functionality enables efficient navigation and organization of PDF content, making it easier to manage complex documents with hierarchical bookmark structures",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get bookmarks, update bookmarks, expand bookmarks, PDF bookmarks, Aspose.PDF for .NET, OutlineCollection, OutlineItemCollection, child bookmarks",
    "wordcount": "1050",
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
    "url": "/net/get-update-and-expand-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-update-and-expand-bookmark/"
    },
    "dateModified": "2024-11-25",
    "description": "This article describes how to use bookmarks in a PDF file with our Aspose.PDF for .NET library."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Get Bookmarks

The [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object's [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection contains all a PDF file's bookmarks. This article explains how to get bookmarks from a PDF file, and how to get which page a particular bookmark is on.

To get the bookmarks, loop through the [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection and get each bookmark in the OutlineItemCollection. The OutlineItemCollection provides access to all the bookmark's attributes. The following code snippet shows you how to get bookmarks from the PDF file.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (Aspose.Pdf.OutlineItemCollection outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (Aspose.Pdf.OutlineItemCollection outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Getting a Bookmark's Page Number

Once you have added a bookmark you can find out what page it is on by getting the destination PageNumber associated with the Bookmark object.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetBookmarkPageNumber()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Open PDF file
        bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

        // Extract bookmarks
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            string strLevelSeparator = string.Empty;

            for (int i = 1; i < bookmark.Level; i++)
            {
                strLevelSeparator += "----";
            }

            Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
            Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
            Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetBookmarkPageNumber()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Open PDF file
    bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

    // Extract bookmarks
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        string strLevelSeparator = string.Empty;

        for (int i = 1; i < bookmark.Level; i++)
        {
            strLevelSeparator += "----";
        }

        Console.WriteLine("{0}Title: {1}", strLevelSeparator, bookmark.Title);
        Console.WriteLine("{0}Page Number: {1}", strLevelSeparator, bookmark.PageNumber);
        Console.WriteLine("{0}Page Action: {1}", strLevelSeparator, bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Get Child Bookmarks from a PDF Document

Bookmarks can be organized in a hierarchical structure, with parents and children. To get all bookmarks, loop through the Document object's Outlines collections. However, to get child bookmarks as well, also loop through all the bookmarks in each [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) object obtained in the first loop. The following code snippets show how to get child bookmarks from a PDF document.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetChildBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (Aspose.Pdf.OutlineItemCollection outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);

            if (outlineItem.Count > 0)
            {
                Console.WriteLine("Child Bookmarks");

                // There are child bookmarks then loop through that as well
                foreach (Aspose.Pdf.OutlineItemCollection childOutline in outlineItem)
                {
                    Console.WriteLine(childOutline.Title);
                    Console.WriteLine(childOutline.Italic);
                    Console.WriteLine(childOutline.Bold);
                    Console.WriteLine(childOutline.Color);
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetChildBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (Aspose.Pdf.OutlineItemCollection outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);

        if (outlineItem.Count > 0)
        {
            Console.WriteLine("Child Bookmarks");

            // There are child bookmarks then loop through that as well
            foreach (Aspose.Pdf.OutlineItemCollection childOutline in outlineItem)
            {
                Console.WriteLine(childOutline.Title);
                Console.WriteLine(childOutline.Italic);
                Console.WriteLine(childOutline.Bold);
                Console.WriteLine(childOutline.Color);
            }
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Update Bookmarks in a PDF Document

To update a bookmark in a PDF file, first, get the particular bookmark from the Document object's OutlineColletion collection by specifying the bookmark's index. Once you have retrieved the bookmark into [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) object, you can update its properties and then save the updated PDF file using the Save method. The following code snippets show how to update bookmarks in a PDF document.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf"))
    {
        // Get a bookmark object
        Aspose.Pdf.OutlineItemCollection pdfOutline = document.Outlines[1];
        pdfOutline.Title = "Updated Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Save output
        document.Save(dataDir + "UpdateBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf");

    // Get a bookmark object
    Aspose.Pdf.OutlineItemCollection pdfOutline = document.Outlines[1];
    pdfOutline.Title = "Updated Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Save output
    document.Save(dataDir + "UpdateBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Update Child Bookmarks in a PDF Document

To update a child bookmark:

1. Retrieve the child bookmark you want to update from the PDF file by first getting the parent bookmark and then the child bookmark using appropriate index values.
1. Save the updated PDF file using the [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/1) method.

{{% alert color="primary" %}}

Get a bookmark from the Document object's OutlineCollection collection by specifying the bookmark's index, and then get the child bookmark by specifying the index od this parent bookmark.

{{% /alert %}}

The following code snippet shows you how to update child bookmarks in a PDF document.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateChildBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf"))
    {
        // Get a bookmark object
        Aspose.Pdf.OutlineItemCollection pdfOutline = document.Outlines[1];

        // Get child bookmark object
        Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
        childOutline.Title = "Updated Outline";
        childOutline.Italic = true;
        childOutline.Bold = true;

        // Save output document
        document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void UpdateChildBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf");

    // Get a bookmark object
    Aspose.Pdf.OutlineItemCollection pdfOutline = document.Outlines[1];

    // Get child bookmark object
    Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
    childOutline.Title = "Updated Outline";
    childOutline.Italic = true;
    childOutline.Bold = true;

    // Save output document
    document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Expanded Bookmarks when viewing document

Bookmarks are held in the Document object's [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) collection, itself in the [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) collection. However, we may have a requirement to have all the bookmarks expanded when viewing the PDF file.

In order to accomplish this requirement, we can set open status for each outline/bookmark item as Open. The following code snippet shows you how to set the open status for each bookmark as expanded in a PDF document.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExpandBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

        // Traverse through each Outline item in outlines collection of PDF file
        foreach (Aspose.Pdf.OutlineItemCollection item in document.Outlines)
        {
            // Set open status for outline item
            item.Open = true;
        }

        // Save output
        document.Save(dataDir + "ExpandBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ExpandBookmarks()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

    // Traverse through each Outline item in outlines collection of PDF file
    foreach (Aspose.Pdf.OutlineItemCollection item in document.Outlines)
    {
        // Set open status for outline item
        item.Open = true;
    }

    // Save output
    document.Save(dataDir + "ExpandBookmarks_out.pdf");
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
