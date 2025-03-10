---
title: Добавить и удалить закладку
linktitle: Добавить и удалить закладку
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-and-delete-bookmark/
description: Вы можете добавить закладку в PDF-документ с помощью C#. Возможно удалить все или определенные закладки из PDF-документа.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add and Delete a Bookmark",
    "alternativeHeadline": "Manage PDF Bookmarks: Add and Delete with Ease",
    "abstract": "Новая функция позволяет пользователям эффективно управлять закладками в PDF-документах с помощью C#. Вы можете легко добавлять новые закладки или удалять существующие, независимо от того, хотите ли вы удалить все закладки или нацелиться на конкретные записи. Эта функциональность улучшает навигацию и организацию документов для повышения удобства использования.",
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
    "description": "Вы можете добавить закладку в PDF-документ с помощью C#. Возможно удалить все или определенные закладки из PDF-документа."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавить закладку в PDF-документ

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) объекта Document, которая сама находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Чтобы добавить закладку в PDF:

1. Откройте PDF-документ с помощью объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте закладку и определите ее свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF-документ.

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

## Добавить дочернюю закладку в PDF-документ

Закладки могут быть вложенными, указывая на иерархические отношения между родительскими и дочерними закладками. Эта статья объясняет, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в PDF-файл, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), определив ее свойства.
1. Добавьте OutlineItemCollection в коллекцию [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) объекта Document.

Дочерняя закладка создается так же, как и родительская закладка, описанная выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить дочернюю закладку в PDF-документ.

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

## Удалить все закладки из PDF-документа

Все закладки в PDF хранятся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Эта статья объясняет, как удалить все закладки из PDF-файла.

Чтобы удалить все закладки из PDF-файла:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Сохраните измененный файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Следующие фрагменты кода показывают, как удалить все закладки из PDF-документа.

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

## Удалить конкретную закладку из PDF-документа

Чтобы удалить конкретную закладку из PDF-файла:

1. Передайте заголовок закладки в качестве параметра методу Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Затем сохраните обновленный файл с помощью метода Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Метод [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) удаляет любую закладку с заголовком, переданным в метод.

Следующие фрагменты кода показывают, как удалить конкретную закладку из PDF-документа.

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