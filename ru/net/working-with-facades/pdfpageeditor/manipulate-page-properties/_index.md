---
title: Манипуляция свойствами страниц
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/manipulate-page-properties/
description: Этот раздел объясняет, как манипулировать свойствами страниц с помощью Aspose.PDF Facades, используя класс PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "Представляем класс PdfPageEditor, мощный инструмент для управления свойствами страниц PDF с помощью Aspose.PDF for .NET Facades. Эта функция позволяет разработчикам извлекать и изменять основные атрибуты страниц, такие как поворот, уровни масштабирования и размеры страниц, обеспечивая точный контроль над представлением содержимого PDF. С простыми методами для получения и установки свойств, включая возможность изменения размера конкретного содержимого страниц, улучшение PDF-документов стало проще простого.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Получение свойств страниц PDF из существующего PDF файла

[PdfPageEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor) позволяет работать с отдельными страницами PDF файла. Он помогает вам получить свойства отдельной страницы, такие как размеры различных областей страницы, поворот страницы, масштаб страницы и т.д. Чтобы получить эти свойства, вам нужно создать объект [PdfPageEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor) и связать входной PDF файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вы можете использовать различные методы для получения свойств страницы, такие как [GetPageRotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) и т.д.

Следующий фрагмент кода показывает, как получить свойства страниц PDF из существующего PDF файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## Установка свойств страниц PDF в существующем PDF файле

Чтобы установить свойства страниц, такие как поворот страницы, масштаб или начальная точка, вам нужно использовать класс [PdfPageEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor). Этот класс предоставляет различные методы и свойства для установки этих свойств страниц. Прежде всего, вам нужно создать объект класса [PdfPageEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor) и связать входной PDF файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3). После этого вы можете использовать эти методы и свойства для установки свойств страницы. Наконец, сохраните обновленный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save).

Следующий фрагмент кода показывает, как установить свойства страниц PDF в существующем PDF файле.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## Изменение размера содержимого страниц в конкретных страницах PDF файла

Метод ResizeContents класса [PdfPageEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfpageeditor) позволяет изменять размер содержимого страниц в PDF файле. Класс [ContentsResizeParameters](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) используется для указания параметров, которые будут использоваться для изменения размера страницы(ц), например, поля в процентах или единицах и т.д. Вы можете изменить размер всех страниц или указать массив страниц, которые нужно изменить с помощью метода ResizeContents.

Следующий фрагмент кода показывает, как изменить размер содержимого некоторых конкретных страниц PDF файла.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```