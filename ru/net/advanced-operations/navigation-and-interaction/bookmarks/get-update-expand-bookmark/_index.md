---
title: Получение, обновление и расширение закладки
linktitle: Получение, обновление и расширение закладки
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/get-update-and-expand-bookmark/
description: Эта статья описывает, как использовать закладки в PDF-файле с нашей библиотекой Aspose.PDF for .NET.
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
    "abstract": "Новая функция Получение, обновление и расширение закладки улучшает библиотеку Aspose.PDF for .NET, предоставляя пользователям возможность извлекать, изменять и визуально расширять закладки в PDF-документах. Эта функциональность позволяет эффективно навигировать и организовывать содержимое PDF, упрощая управление сложными документами с иерархическими структурами закладок.",
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
    "description": "Эта статья описывает, как использовать закладки в PDF-файле с нашей библиотекой Aspose.PDF for .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Получение закладок

Коллекция [OutlineCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlinecollection) объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) содержит все закладки PDF-файла. Эта статья объясняет, как получить закладки из PDF-файла и как узнать, на какой странице находится конкретная закладка.

Чтобы получить закладки, пройдите по коллекции [OutlineCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlinecollection) и получите каждую закладку в OutlineItemCollection. OutlineItemCollection предоставляет доступ ко всем атрибутам закладки. Следующий фрагмент кода показывает, как получить закладки из PDF-файла.

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

## Получение номера страницы закладки

После того как вы добавили закладку, вы можете узнать, на какой странице она находится, получив номер страницы, связанный с объектом Bookmark.

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

## Получение дочерних закладок из PDF-документа

Закладки могут быть организованы в иерархическую структуру, с родителями и детьми. Чтобы получить все закладки, пройдите по коллекциям Outlines объекта Document. Однако, чтобы получить также дочерние закладки, пройдите по всем закладкам в каждом объекте [OutlineItemCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlineitemcollection), полученном в первом цикле. Следующие фрагменты кода показывают, как получить дочерние закладки из PDF-документа.

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

## Обновление закладок в PDF-документе

Чтобы обновить закладку в PDF-файле, сначала получите конкретную закладку из коллекции OutlineColletion объекта Document, указав индекс закладки. После того как вы извлекли закладку в объект [OutlineItemCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlineitemcollection), вы можете обновить ее свойства и затем сохранить обновленный PDF-файл, используя метод Save. Следующие фрагменты кода показывают, как обновить закладки в PDF-документе.

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

## Обновление дочерних закладок в PDF-документе

Чтобы обновить дочернюю закладку:

1. Извлеките дочернюю закладку, которую хотите обновить, из PDF-файла, сначала получив родительскую закладку, а затем дочернюю закладку, используя соответствующие индексы.
1. Сохраните обновленный PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.document/save/methods/1).

{{% alert color="primary" %}}

Получите закладку из коллекции OutlineCollection объекта Document, указав индекс закладки, а затем получите дочернюю закладку, указав индекс этой родительской закладки.

{{% /alert %}}

Следующий фрагмент кода показывает, как обновить дочерние закладки в PDF-документе.

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

## Расширенные закладки при просмотре документа

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlineitemcollection) объекта Document, который, в свою очередь, находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/ru/net/aspose.pdf/outlinecollection). Однако у нас может быть требование, чтобы все закладки были развернуты при просмотре PDF-файла.

Чтобы выполнить это требование, мы можем установить статус открытия для каждого элемента закладки как Открытый. Следующий фрагмент кода показывает, как установить статус открытия для каждой закладки как развернутой в PDF-документе.

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