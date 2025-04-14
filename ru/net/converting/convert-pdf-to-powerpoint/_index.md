---
title: Конвертация PDF в PowerPoint в .NET
linktitle: Конвертация PDF в PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF позволяет конвертировать PDF в формат PPT (PowerPoint) с использованием .NET. Один из способов - это возможность конвертации PDF в PPTX с слайдами в виде изображений.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET представляет мощную функцию, позволяющую бесшовную конвертацию PDF документов в формат PowerPoint (PPTX), позволяя каждой странице PDF превращаться в отдельный слайд. С возможностью отображения текста как выбираемого или в виде изображений, пользователи могут легко настраивать свои презентации, отслеживая процесс конвертации эффективно. Оптимизируйте свой рабочий процесс документов, используя эту инновационную функциональность для повышения продуктивности",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "867",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обзор

В этой статье объясняется, как **конвертировать PDF в PowerPoint с использованием C#**. Она охватывает следующие темы.

- [Конвертация PDF в PowerPoint](#csharp-pdf-to-powerpoint)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Конвертация PDF в PowerPoint и PPTX на C#

<a name="csharp-convert-pdf-to-powerpoint" id="csharp-convert-pdf-to-powerpoint"><strong>Конвертация PDF в PowerPoint</strong></a>

**Aspose.PDF for .NET** позволяет вам отслеживать процесс конвертации PDF в PPTX.

У нас есть API под названием Aspose.Slides, который предлагает возможность создавать и манипулировать презентациями PPT/PPTX. Этот API также предоставляет возможность конвертировать файлы PPT/PPTX в формат PDF. В последнее время мы получили запросы от многих наших клиентов на поддержку возможности преобразования PDF в формат PPTX. Начиная с релиза Aspose.PDF for .NET 10.3.0, мы представили функцию преобразования PDF документов в формат PPTX. В процессе этой конвертации отдельные страницы PDF файла конвертируются в отдельные слайды в файле PPTX.

Во время конвертации PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> текст отображается как текст, который вы можете выбирать/обновлять. Обратите внимание, что для конвертации PDF файлов в формат PPTX Aspose.PDF предоставляет класс [`PptxSaveOptions`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions). Объект класса PptxSaveOptions передается в качестве второго аргумента в метод [`Document.Save(..) method`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save). Следующий фрагмент кода демонстрирует процесс конвертации PDF файлов в формат PPTX.

## Простая конвертация PDF в PowerPoint с использованием C# и Aspose.PDF .NET

Для конвертации PDF в PPTX, Aspose.PDF for .NET рекомендует использовать следующие шаги кода.

<a name="csharp-pdf-to-powerpoint"><strong>Конвертация PDF в PowerPoint</strong></a>

1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
2. Создайте экземпляр класса [PptxSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions).
3. Используйте метод **Save** объекта **Document**, чтобы сохранить PDF как PPTX.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Конвертация PDF в PPTX с слайдами в виде изображений

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF for .NET представляет вам онлайн бесплатное приложение ["PDF в PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

В случае, если вам нужно конвертировать поисковый PDF в PPTX в виде изображений вместо выбираемого текста, Aspose.PDF предоставляет такую возможность через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions). Для этого установите свойство [SlidesAsImages](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) класса [PptxSaveOptios](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions) в 'true', как показано в следующем примере кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## Подробности о процессе конвертации PPTX

Aspose.PDF for .NET позволяет вам отслеживать процесс конвертации PDF в PPTX. Класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions) предоставляет свойство [CustomProgressHandler](https://reference.aspose.com/pdf/ru/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler), которое можно указать для пользовательского метода для отслеживания процесса конвертации, как показано в следующем примере кода.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```