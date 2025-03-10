---
title: Создание NUp из PDF файлов
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ru/net/make-nup-of-pdf-files/
description: Эта статья показывает, как создать NUp из PDF файлов с использованием классов Aspose.PDF Facades и PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "Функция NUp в Aspose.PDF for .NET позволяет пользователям эффективно объединять несколько PDF файлов в один выходной документ, настраивая размер страницы и конфигурации макета. Эта функциональность поддерживает как пути к файлам, так и потоки, что позволяет гибко интегрироваться в различные рабочие процессы, улучшая представление документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Создание NUp из PDF с использованием путей к файлам

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF файла и сохранить его в выходной PDF файл. Этот перегруз позволяет вам создать NUp, используя пути к файлам. Следующий фрагмент кода показывает, как создать NUP, используя пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Создание NUp с использованием размера страницы и путей к файлам

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF файла и сохранить его в выходной PDF файл. Этот перегруз позволяет вам создать NUp, используя пути к файлам. Вы также можете установить размер страницы выходного PDF файла, используя этот перегруз. Следующий фрагмент кода показывает, как создать NUp, используя размер страницы и пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Создание NUp из PDF с использованием размера страницы, горизонтальных и вертикальных значений и путей к файлам

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF файла и сохранить его в выходной PDF файл. Этот перегруз позволяет вам создать NUp, используя пути к файлам. Вы также можете установить размер страницы выходного PDF файла и горизонтальное и вертикальное количество страниц на каждой выходной странице, используя этот перегруз. Следующий фрагмент кода показывает, как создать NUp, используя размер страницы, горизонтальные и вертикальные значения и пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Создание NUp из PDF с использованием массива PDF файлов и путей к файлам

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из массива входных PDF файлов и сохранить их в один выходной PDF файл. Этот перегруз позволяет вам создать NUp, используя пути к файлам. Следующий фрагмент кода показывает, как создать NUp, используя массив PDF файлов и пути к файлам.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Создание NUp из PDF с использованием потоков

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF потока и сохранить его в выходной PDF поток. Этот перегруз позволяет вам создать NUp, используя потоки вместо путей к файлам. Следующий фрагмент кода показывает, как создать NUp, используя потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Создание NUp из PDF с использованием размера страницы и потоков

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF потока и сохранить его в выходной PDF поток. Этот перегруз позволяет вам создать NUp, используя потоки вместо путей к файлам. Вы также можете установить размер страницы выходного PDF потока, используя этот перегруз. Следующий фрагмент кода показывает, как создать NUp, используя размер страницы и потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Создание NUp из PDF с использованием размера страницы, горизонтальных и вертикальных значений и потоков

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из входного PDF потока и сохранить его в выходной PDF поток. Этот перегруз позволяет вам создать NUp, используя потоки вместо путей к файлам. Вы также можете установить размер страницы выходного PDF потока и горизонтальное и вертикальное количество страниц на каждой выходной странице, используя этот перегруз. Следующий фрагмент кода показывает, как создать NUp, используя размер страницы, горизонтальные и вертикальные значения и потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## Создание NUp из PDF с использованием массива PDF файлов и потоков

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) метод класса [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) позволяет вам создать NUp из массива входных PDF потоков и сохранить их в один выходной PDF поток. Этот перегруз позволяет вам создать NUp, используя потоки вместо путей к файлам. Следующий фрагмент кода показывает, как создать NUp, используя массив PDF файлов с использованием потоков.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```