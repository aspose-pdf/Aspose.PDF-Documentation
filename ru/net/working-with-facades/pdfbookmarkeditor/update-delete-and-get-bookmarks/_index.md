---
title: Обновление, удаление и получение закладок
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/update-delete-and-get-bookmarks/
description: Этот раздел объясняет, как обновлять, удалять и получать закладки с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update, Delete and Get Bookmarks",
    "alternativeHeadline": "Manage Bookmarks: Update, Delete, and Extract Functions",
    "abstract": "Функция управления закладками в PDF-файлах с использованием Aspose.PDF Facades позволяет пользователям легко обновлять, удалять и извлекать закладки. С помощью методов, таких как ModifyBookmarks, DeleteBookmarks и ExtractBookmarks, пользователи могут эффективно манипулировать закладками, улучшая навигацию и организацию PDF для лучшего пользовательского опыта. Эта функциональность упрощает управление закладками через простую реализацию кода, обеспечивая эффективную обработку PDF-документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "761",
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
    "url": "/net/update-delete-and-get-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-delete-and-get-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обновление существующей закладки в PDF-файле

Чтобы обновить существующую закладку в PDF-файле, вам нужно использовать метод [ModifyBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Этот метод принимает два аргумента: исходный заголовок (заголовок закладки для изменения), целевой заголовок (заголовок, который будет заменен). Вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно вызвать метод [ModifyBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), а затем сохранить обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как изменить существующую закладку в PDF-файле.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

        // Modify the existing bookmark, assigning a new title
        bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void UpdateExistingBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "UpdateBookmark.pdf");

    // Modify the existing bookmark, assigning a new title
    bookmarkEditor.ModifyBookmarks("New Bookmark", "New Title");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "UpdateBookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Удаление всех закладок из PDF-файла

Вы можете удалить все закладки из PDF-файла, используя метод [DeleteBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) без каких-либо параметров. Прежде всего, вам нужно создать объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно вызвать метод [DeleteBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks), а затем сохранить обновленный PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как удалить все закладки из PDF-файла.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

        // Delete all bookmarks in the document
        bookmarkEditor.DeleteBookmarks();

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllBookmarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteAllBookmarks.pdf");

    // Delete all bookmarks in the document
    bookmarkEditor.DeleteBookmarks();

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteAllBookmarks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Удаление конкретной закладки из PDF-файла

Чтобы удалить конкретную закладку, вам нужно вызвать метод [DeleteBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) с параметром строки (заголовок). *Заголовок* здесь представляет закладку, которую нужно удалить из PDF. Создайте объект класса [PdfBookmarkEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor) и свяжите входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вызовите метод [DeleteBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks), а затем сохраните обновленный PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save). Следующий фрагмент кода показывает, как удалить конкретную закладку из PDF-файла.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

        // Delete a bookmark with the title "Page2"
        bookmarkEditor.DeleteBookmarks("Page2");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteParticularBookmark()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

   // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "DeleteABookmark.pdf");

    // Delete a bookmark with the title "Page2"
    bookmarkEditor.DeleteBookmarks("Page2");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "DeleteABookmark_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Получение закладок из PDF-документа Facades

Класс [PdfBookmarkEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor) предоставляет возможность манипулировать закладками в существующем PDF-файле. Он предоставляет различные свойства для получения/установки информации о закладках. Следующий фрагмент кода показывает, как получить информацию, связанную с каждой закладкой в PDF-файле.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

        // Extract all bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each bookmark and display information
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

            // Get the information related to associated action with bookmark
            Console.WriteLine("Bookmark Action: " + bookmark.Action);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetBookmarksFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "GetFromPDF.PDF");

    // Extract all bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each bookmark and display information
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);

        // Get the information related to associated action with bookmark
        Console.WriteLine("Bookmark Action: " + bookmark.Action);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Извлечение закладок из существующего PDF-файла

Метод [ExtractBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) позволяет извлекать закладки из PDF-файла. Чтобы извлечь закладки, вам нужно создать объект [PdfBookmarkEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor) и связать PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вам нужно вызвать метод [ExtractBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). Метод [ExtractBookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) возвращает объект [Bookmarks](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/bookmarks/methods/index). Затем вы можете пройтись по этим закладкам и получить отдельные объекты [Bookmark](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/bookmark). Наконец, вы можете экспортировать закладки в XML-файл с помощью метода [ExportBookmarksToXML](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml). Следующий фрагмент кода показывает, как экспортировать закладки в XML-файл.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

        // Extract bookmarks from the document
        Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

        // Iterate through each extracted bookmark
        foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
        {
            // Get the title information of bookmark item
            Console.WriteLine("Title: {0}", bookmark.Title);

            // Get the destination page for bookmark
            Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
        }

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExtractBookmarksFromPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExtractBookmarks.pdf");

    // Extract bookmarks from the document
    Aspose.Pdf.Facades.Bookmarks bookmarks = bookmarkEditor.ExtractBookmarks();

    // Iterate through each extracted bookmark
    foreach (Aspose.Pdf.Facades.Bookmark bookmark in bookmarks)
    {
        // Get the title information of bookmark item
        Console.WriteLine("Title: {0}", bookmark.Title);

        // Get the destination page for bookmark
        Console.WriteLine("Page Number: {0}", bookmark.PageNumber);
    }

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}