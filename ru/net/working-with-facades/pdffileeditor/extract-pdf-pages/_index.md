---
title: Извлечение страниц PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/extract-pdf-pages/
description: Этот раздел объясняет, как извлекать страницы PDF с помощью Aspose.PDF Facades, используя класс PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "Функция Извлечение страниц PDF в Aspose.PDF for .NET Facades предоставляет пользователям расширенные возможности для выборочного извлечения страниц из PDF документов. Используя класс PdfFileEditor, пользователи могут эффективно извлекать заданный диапазон или набор страниц через пути к файлам или потоки, что делает манипуляцию документами более упрощенной и гибкой. Эта функциональность особенно полезна для пользователей, стремящихся настроить свое содержимое PDF без изменения оригинальных файлов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Извлечение страниц PDF между двумя номерами с использованием путей к файлам

[Метод Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет извлекать заданный диапазон страниц из PDF файла. Этот перегруженный метод позволяет извлекать страницы, манипулируя PDF файлами с диска. Этот перегруженный метод требует следующие параметры: путь к входному файлу, начальная страница, конечная страница и путь к выходному файлу. Страницы от начальной до конечной будут извлечены, а выходные данные будут сохранены на диске. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами, используя пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Извлечение массива страниц PDF с использованием путей к файлам

Если вы не хотите извлекать диапазон страниц, а набор конкретных страниц, метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) также позволяет это сделать. Сначала вам нужно создать массив целых чисел со всеми номерами страниц, которые необходимо извлечь. Этот перегруженный метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) принимает следующие параметры: входной PDF файл, массив целых чисел страниц для извлечения и выходной PDF файл. Следующий фрагмент кода показывает, как извлечь страницы PDF, используя пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## Извлечение страниц PDF между двумя номерами с использованием потоков

[Метод Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет извлекать диапазон страниц, используя потоки. Вам нужно передать следующие параметры этому перегруженному методу: входной поток, начальная страница, конечная страница и выходной поток. Страницы, указанные в диапазоне между начальной и конечной страницами, будут извлечены из входного потока и сохранены в выходном потоке. Следующий фрагмент кода показывает, как извлечь страницы PDF между двумя номерами, используя потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Извлечение массива страниц PDF с использованием потоков

Массив страниц может быть извлечен из PDF потока и сохранен в выходном потоке с использованием соответствующего перегруженного метода [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Если вы не хотите извлекать диапазон страниц, а набор конкретных страниц, метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) также позволяет это сделать. Сначала вам нужно создать массив целых чисел со всеми номерами страниц, которые необходимо извлечь. Этот перегруженный метод [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) принимает следующие параметры: входной поток, массив целых чисел страниц для извлечения и выходной поток. Следующий фрагмент кода показывает, как извлечь страницы PDF, используя потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```