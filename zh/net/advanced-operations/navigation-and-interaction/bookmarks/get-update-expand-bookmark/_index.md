---
title: 获取、更新和扩展书签
linktitle: 获取、更新和扩展书签
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/get-update-and-expand-bookmark/
description: 本文描述了如何使用我们的 Aspose.PDF for .NET 库在 PDF 文件中使用书签。
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
    "abstract": "新的获取、更新和扩展书签功能通过提供用户检索、修改和可视化扩展 PDF 文档中的书签的能力，增强了 Aspose.PDF for .NET 库。此功能使 PDF 内容的高效导航和组织成为可能，使管理具有层次书签结构的复杂文档变得更加容易。",
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
    "description": "本文描述了如何使用我们的 Aspose.PDF for .NET 库在 PDF 文件中使用书签。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 获取书签

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 集合包含 PDF 文件的所有书签。本文解释了如何从 PDF 文件中获取书签，以及如何获取特定书签所在的页面。

要获取书签，请循环遍历 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 集合，并获取 OutlineItemCollection 中的每个书签。OutlineItemCollection 提供对所有书签属性的访问。以下代码片段演示了如何从 PDF 文件中获取书签。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
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

## 获取书签的页码

一旦您添加了书签，您可以通过获取与书签对象关联的目标 PageNumber 来找出它所在的页面。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetBookmarkPageNumber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

        // Extract bookmarks
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        foreach (var bookmark in bookmarks)
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Create PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetBookmarks.pdf");

    // Extract bookmarks
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    foreach (var bookmark in bookmarks)
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

## 从 PDF 文档中获取子书签

书签可以以层次结构组织，具有父书签和子书签。要获取所有书签，请循环遍历 Document 对象的 Outlines 集合。然而，要获取子书签，还需要循环遍历在第一次循环中获得的每个 [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) 对象中的所有书签。以下代码片段演示了如何从 PDF 文档中获取子书签。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf"))
    {
        // Loop through all the bookmarks
        foreach (var outlineItem in document.Outlines)
        {
            Console.WriteLine(outlineItem.Title);
            Console.WriteLine(outlineItem.Italic);
            Console.WriteLine(outlineItem.Bold);
            Console.WriteLine(outlineItem.Color);

            if (outlineItem.Count > 0)
            {
                Console.WriteLine("Child Bookmarks");

                // There are child bookmarks then loop through that as well
                foreach (var childOutline in outlineItem)
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetChildBookmarks.pdf");

    // Loop through all the bookmarks
    foreach (var outlineItem in document.Outlines)
    {
        Console.WriteLine(outlineItem.Title);
        Console.WriteLine(outlineItem.Italic);
        Console.WriteLine(outlineItem.Bold);
        Console.WriteLine(outlineItem.Color);

        if (outlineItem.Count > 0)
        {
            Console.WriteLine("Child Bookmarks");

            // There are child bookmarks then loop through that as well
            foreach (var childOutline in outlineItem)
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

## 更新 PDF 文档中的书签

要更新 PDF 文件中的书签，首先，通过指定书签的索引从 Document 对象的 OutlineColletion 集合中获取特定书签。一旦您将书签检索到 [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) 对象中，您可以更新其属性，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段演示了如何在 PDF 文档中更新书签。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];
        pdfOutline.Title = "Updated Outline";
        pdfOutline.Italic = true;
        pdfOutline.Bold = true;

        // Save PDF document
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];
    pdfOutline.Title = "Updated Outline";
    pdfOutline.Italic = true;
    pdfOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 更新 PDF 文档中的子书签

要更新子书签：

1. 通过首先获取父书签，然后使用适当的索引值获取子书签，从 PDF 文件中检索您要更新的子书签。
2. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/1) 方法保存更新后的 PDF 文件。

{{% alert color="primary" %}}

通过指定书签的索引，从 Document 对象的 OutlineCollection 集合中获取书签，然后通过指定该父书签的索引获取子书签。

{{% /alert %}}

以下代码片段演示了如何在 PDF 文档中更新子书签。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateChildBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf"))
    {
        // Get a bookmark object
        var pdfOutline = document.Outlines[1];

        // Get child bookmark object
        Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
        childOutline.Title = "Updated Outline";
        childOutline.Italic = true;
        childOutline.Bold = true;

        // Save PDF document
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateChildBookmarks.pdf");

    // Get a bookmark object
    var pdfOutline = document.Outlines[1];

    // Get child bookmark object
    Aspose.Pdf.OutlineItemCollection childOutline = pdfOutline[1];
    childOutline.Title = "Updated Outline";
    childOutline.Italic = true;
    childOutline.Bold = true;

    // Save PDF document
    document.Save(dataDir + "UpdateChildBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 查看文档时展开书签

书签保存在 Document 对象的 [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) 集合中，该集合本身在 [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) 集合中。然而，我们可能需要在查看 PDF 文件时将所有书签展开。

为了实现这一要求，我们可以将每个大纲/书签项的打开状态设置为打开。以下代码片段演示了如何在 PDF 文档中将每个书签的打开状态设置为展开。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExpandBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

        // Traverse through each Outline item in outlines collection of PDF file
        foreach (var item in document.Outlines)
        {
            // Set open status for outline item
            item.Open = true;
        }

        // Save PDF document
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
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Set page view mode i.e. show thumbnails, full-screen, show attachment panel
    document.PageMode = Aspose.Pdf.PageMode.UseOutlines;

    // Traverse through each Outline item in outlines collection of PDF file
    foreach (var item in document.Outlines)
    {
        // Set open status for outline item
        item.Open = true;
    }

    // Save PDF document
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