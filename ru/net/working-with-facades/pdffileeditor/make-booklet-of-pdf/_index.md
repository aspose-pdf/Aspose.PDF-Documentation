---
title: Создание буклета из PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/make-booklet-of-pdf/
description: Этот раздел объясняет, как создать буклет из PDF с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "Функция создания буклета из PDF в Aspose.PDF позволяет пользователям без усилий создавать буклеты из PDF-файлов с использованием класса PdfFileEditor. Эта функциональность поддерживает как пути к файлам, так и потоки, позволяя настраивать размеры страниц и указывать левые и правые страницы для улучшенного контроля вывода. Этот мощный инструмент упрощает процесс создания буклетов, делая его незаменимым ресурсом для манипуляции PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Создание буклета из PDF с использованием путей к файлам

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-файла и сохранить его в выходной PDF-файл. Этот перегруз позволяет создавать буклет с использованием путей к файлам. Следующий фрагмент кода показывает, как создать буклет с использованием путей к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## Создание буклета из PDF с использованием размера страницы и путей к файлам

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-файла и сохранить его в выходной PDF-файл. Этот перегруз позволяет создавать буклет с использованием путей к файлам. Вы также можете установить размер страницы выходного PDF-файла с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием размера страницы и путей к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## Создание буклета из PDF с использованием размера страницы, указанных левых и правых страниц и путей к файлам

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-файла и сохранить его в выходной PDF-файл. Этот перегруз позволяет создавать буклет с использованием путей к файлам. Вы также можете установить размер страницы выходного PDF-файла и указать конкретные страницы для левой и правой сторон выходного PDF-файла с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием размера страницы, указанных левых и правых страниц и путей к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## Создание буклета из PDF с использованием указанных левых и правых страниц и путей к файлам

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-файла и сохранить его в выходной PDF-файл. Этот перегруз позволяет создавать буклет с использованием путей к файлам. Вы также можете указать конкретные страницы для левой и правой сторон выходного PDF-файла с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием указанных левых и правых страниц и путей к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## Создание буклета из PDF с использованием потоков

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-потока и сохранить его в выходные PDF-потоки. Этот перегруз позволяет создавать буклет с использованием потоков вместо путей к файлам. Следующий фрагмент кода показывает, как создать буклет с использованием потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## Создание буклета из PDF с использованием размера страницы и потоков

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-потока и сохранить его в выходной PDF-поток. Этот перегруз позволяет создавать буклет с использованием потоков вместо путей к файлам. Вы также можете установить размер страницы выходного PDF-потока с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием размера страницы и потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## Создание буклета из PDF с использованием размера страницы, указанных левых и правых страниц и потоков

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-потока и сохранить его в выходной PDF-поток. Этот перегруз позволяет создавать буклет с использованием потоков вместо путей к файлам. Вы также можете установить размер страницы выходного PDF-файла и указать конкретные страницы для левой и правой сторон выходного PDF-потока с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием размера страницы, указанных левых и правых страниц и потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## Создание буклета из PDF с использованием указанных левых и правых страниц и потоков

Метод [MakeBooklet](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать буклет из входного PDF-потока и сохранить его в выходной PDF-поток. Этот перегруз позволяет создавать буклет с использованием потоков вместо путей к файлам. Вы также можете указать конкретные страницы для левой и правой сторон выходного PDF-потока с помощью этого перегруза. Следующий фрагмент кода показывает, как создать буклет с использованием указанных левых и правых страниц и потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```