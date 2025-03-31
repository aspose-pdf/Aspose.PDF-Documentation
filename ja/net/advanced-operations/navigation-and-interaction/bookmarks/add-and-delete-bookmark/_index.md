---
title: ブックマークの追加と削除
linktitle: ブックマークの追加と削除
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-and-delete-bookmark/
description: C#を使用してPDFドキュメントにブックマークを追加できます。PDFドキュメントからすべてまたは特定のブックマークを削除することも可能です。
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
    "abstract": "この新機能により、ユーザーはC#を使用してPDFドキュメント内のブックマークを効率的に管理できます。新しいブックマークを簡単に追加したり、既存のブックマークを削除したりできます。すべてのブックマークを削除するか、特定のエントリをターゲットにすることができます。この機能は、ドキュメントのナビゲーションと整理を向上させ、ユーザーエクスペリエンスを改善します。",
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
    "description": "C#を使用してPDFドキュメントにブックマークを追加できます。PDFドキュメントからすべてまたは特定のブックマークを削除することも可能です。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

## PDFドキュメントにブックマークを追加する

ブックマークは、Documentオブジェクトの[OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)コレクションに保持されており、さらに[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションに含まれています。

PDFにブックマークを追加するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを使用してPDFドキュメントを開きます。
1. ブックマークを作成し、そのプロパティを定義します。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)コレクションをOutlinesコレクションに追加します。

次のコードスニペットは、PDFドキュメントにブックマークを追加する方法を示しています。

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

## PDFドキュメントに子ブックマークを追加する

ブックマークはネスト可能で、親ブックマークと子ブックマークの階層関係を示します。この記事では、PDFに子ブックマーク、つまり第二レベルのブックマークを追加する方法を説明します。

PDFファイルに子ブックマークを追加するには、まず親ブックマークを追加します：

1. ドキュメントを開きます。
1. [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection)にブックマークを追加し、そのプロパティを定義します。
1. OutlineItemCollectionをDocumentオブジェクトの[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションに追加します。

子ブックマークは、上記で説明した親ブックマークと同様に作成されますが、親ブックマークのOutlinesコレクションに追加されます。

次のコードスニペットは、PDFドキュメントに子ブックマークを追加する方法を示しています。

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

## PDFドキュメントからすべてのブックマークを削除する

PDF内のすべてのブックマークは、[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションに保持されています。この記事では、PDFファイルからすべてのブックマークを削除する方法を説明します。

PDFファイルからすべてのブックマークを削除するには：

1. [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションのDeleteメソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)メソッドを使用して、変更されたファイルを保存します。

次のコードスニペットは、PDFドキュメントからすべてのブックマークを削除する方法を示しています。

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

## PDFドキュメントから特定のブックマークを削除する

PDFファイルから特定のブックマークを削除するには：

1. ブックマークのタイトルを[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションのDeleteメソッドにパラメータとして渡します。
1. 次に、DocumentオブジェクトのSaveメソッドで更新されたファイルを保存します。

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)クラスは、[OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection)コレクションを提供します。[Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete)メソッドは、メソッドに渡されたタイトルを持つブックマークを削除します。

次のコードスニペットは、PDFドキュメントから特定のブックマークを削除する方法を示しています。

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