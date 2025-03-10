---
title: Вставка страниц PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/insert-pdf-pages/
description: Этот раздел объясняет, как вставить страницы PDF с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Оптимизируйте управление PDF с помощью новой функции, позволяющей пользователям вставлять конкретные страницы из одного PDF в другой, используя класс PdfFileEditor. Эта функциональность поддерживает как вставку на основе диапазона, так и вставку на основе массива страниц, повышая эффективность рабочего процесса за счет бесшовного объединения документов через пути к файлам или потоки.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Вставка страниц PDF между двумя номерами с использованием путей к файлам

Определенный диапазон страниц можно вставить из одного PDF в другой, используя метод [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Для этого вам нужен входной PDF-файл, в который вы хотите вставить страницы, порт-файл, из которого необходимо взять страницы для вставки, место, куда страницы должны быть вставлены, и диапазон страниц порт-файла, которые должны быть вставлены во входной PDF-файл. Этот диапазон задается параметрами начальной и конечной страниц. Наконец, выходной PDF-файл сохраняется с указанным диапазоном страниц, вставленных во входной файл. Следующий фрагмент кода показывает, как вставить страницы PDF между двумя номерами, используя потоки файлов.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Вставка массива страниц PDF с использованием путей к файлам

Если вы хотите вставить некоторые конкретные страницы в другой PDF-файл, вы можете использовать перегрузку метода [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index), которая требует целочисленного массива страниц. В этом массиве вы можете указать, какие конкретные страницы вы хотите вставить во входной PDF-файл. Для этого вам нужен входной PDF-файл, в который вы хотите вставить страницы, порт-файл, из которого необходимо взять страницы для вставки, место, куда страницы должны быть вставлены, и целочисленный массив страниц из порт-файла, которые должны быть вставлены во входной PDF-файл. Этот массив содержит список конкретных страниц, которые вас интересуют для вставки во входной PDF-файл. Наконец, выходной PDF-файл сохраняется с указанным массивом страниц, вставленных во входной файл. Следующий фрагмент кода показывает, как вставить массив страниц PDF с использованием путей к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Вставка страниц PDF между двумя номерами с использованием потоков

Если вы хотите вставить диапазон страниц, используя потоки, вам нужно просто использовать соответствующую перегрузку метода [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Для этого вам нужен входной PDF-поток, в который вы хотите вставить страницы, порт-поток, из которого необходимо взять страницы для вставки, место, куда страницы должны быть вставлены, и диапазон страниц порт-потока, которые должны быть вставлены во входной PDF-поток. Этот диапазон задается параметрами начальной и конечной страниц. Наконец, выходной PDF-поток сохраняется с указанным диапазоном страниц, вставленных во входной поток. Следующий фрагмент кода показывает, как вставить страницы PDF между двумя номерами, используя потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## Вставка массива страниц PDF с использованием потоков

Вы также можете вставить массив страниц в другой PDF-файл, используя потоки с помощью соответствующей перегрузки метода Insert, которая требует целочисленного массива страниц. В этом массиве вы можете указать, какие конкретные страницы вы хотите вставить во входной PDF-поток. Для этого вам нужен входной PDF-поток, в который вы хотите вставить страницы, порт-поток, из которого необходимо взять страницы для вставки, место, куда страницы должны быть вставлены, и целочисленный массив страниц из порт-потока, которые должны быть вставлены во входной PDF-файл. Этот массив содержит список конкретных страниц, которые вас интересуют для вставки во входной PDF-поток. Наконец, выходной PDF-поток сохраняется с указанным массивом страниц, вставленных во входной файл. Следующий фрагмент кода показывает, как вставить массив страниц PDF с использованием потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```