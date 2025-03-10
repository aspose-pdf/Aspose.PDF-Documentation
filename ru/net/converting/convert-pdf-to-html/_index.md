---
title: Конвертация PDF в HTML в .NET
linktitle: Конвертация PDF в формат HTML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Эта тема показывает, как конвертировать PDF файл в формат HTML с помощью библиотеки Aspose.PDF на C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to HTML in .NET",
    "alternativeHeadline": "Convert PDF Files to HTML with Simplified Options in C#",
    "abstract": "Представляем мощную новую функцию в Aspose.PDF for .NET, которая позволяет бесшовную конвертацию PDF документов в формат HTML. Эта функциональность поддерживает многопользовательский вывод, управление изображениями SVG и опции для прозрачного рендеринга текста, позволяя разработчикам легко преобразовывать PDF в контент, готовый к вебу, всего лишь с несколькими строками кода на C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1368",
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
    "url": "/net/convert-pdf-to-html/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-html/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обзор

Эта статья объясняет, как **конвертировать PDF в HTML с использованием C#**. Она охватывает следующие темы.

_Формат_: **HTML**
- [C# PDF в HTML](#csharp-pdf-to-html)
- [C# Конвертация PDF в HTML](#csharp-pdf-to-html)
- [C# Как конвертировать PDF файл в HTML](#csharp-pdf-to-html)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Конвертация PDF в HTML

**Aspose.PDF for .NET** предоставляет множество функций для конвертации различных форматов файлов в PDF документы и конвертации PDF файлов в различные форматы вывода. В этой статье обсуждается, как конвертировать PDF файл в <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for .NET предоставляет возможность конвертировать HTML файлы в PDF формат с использованием подхода InLineHtml. Мы получили много запросов на функциональность, которая конвертирует PDF файл в HTML формат и предоставили эту функцию. Обратите внимание, что эта функция также поддерживает XHTML 1.0.

**Aspose.PDF for .NET** поддерживает функции для конвертации PDF файла в HTML. Основные задачи, которые вы можете выполнить с помощью библиотеки Aspose.PDF, перечислены:

- Конвертация PDF в HTML.
- Разделение вывода на многопользовательский HTML.
- Указание папки для хранения SVG файлов.
- Сжатие SVG изображений во время конвертации.
- Сохранение изображений в качестве фона PNG.
- Указание папки для изображений.
- Создание последующих файлов только с содержимым тела.
- Прозрачный рендеринг текста.
- Рендеринг слоев PDF документа.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF for .NET представляет вам онлайн бесплатное приложение ["PDF в HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET предоставляет двухстрочный код для преобразования исходного PDF файла в HTML. Перечисление [`SaveFormat`](https://reference.aspose.com/pdf/net/aspose.pdf/saveformat) содержит значение Html, которое позволяет вам сохранить исходный файл в HTML. Следующий фрагмент кода показывает процесс конвертации PDF файла в HTML.

<a name="csharp-pdf-to-html"><strong>Шаги: Конвертация PDF в HTML на C#</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в формате **SaveFormat.Html**, вызвав метод **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Save the output HTML
        document.Save(dataDir + "output_out.html", Aspose.Pdf.SaveFormat.Html);
    }
}
```

### Разделение вывода на многопользовательский HTML

При конвертации большого PDF файла с несколькими страницами в формат HTML, вывод появляется как одна HTML страница. Это может оказаться очень длинным. Чтобы контролировать размер страницы, возможно разделить вывод на несколько страниц во время конвертации PDF в HTML. Пожалуйста, попробуйте использовать следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoMultiPageHTML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "MultiPageHTML_out.html", htmlOptions);
    }
}
```

### Указание папки для хранения SVG файлов

Во время конвертации PDF в HTML возможно указать папку, в которую должны сохраняться SVG изображения. Используйте класс [`HtmlSaveOption`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlsaveoptions/fields/specialfolderforsvgimages) для указания специального каталога для SVG изображений. Это свойство получает или устанавливает путь к каталогу, в который SVG изображения должны быть сохранены при встрече во время конвертации. Если параметр пустой или равен null, то любые SVG файлы сохраняются вместе с другими изображениями.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML save options object
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the folder where SVG images are saved during PDF to HTML conversion
            SpecialFolderForSvgImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
    }
}
```

### Сжатие SVG изображений во время конвертации

Чтобы сжать SVG изображения во время конвертации PDF в HTML, пожалуйста, попробуйте использовать следующий код:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoCompressedHTMLWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Compress the SVG images if there are any
            CompressSvgGraphicsIfAny = true
        };

        // Save the output HTML
        document.Save(dataDir + "CompressedSVGHTML_out.html", newOptions);
    }
}
```

### Сохранение изображений в качестве фона PNG

Формат вывода по умолчанию для сохранения изображений - SVG. Во время конвертации некоторые изображения из PDF преобразуются в векторные изображения SVG. Это может быть медленно. Вместо этого изображения могут быть преобразованы в один файл фона PNG для каждой страницы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToHtmlSaveImagesAsPngBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion_PDFToHTMLFormat();
           
    // Create HtmlSaveOption with tested feature
    var htmlSaveOptions = new HtmlSaveOptions();
           
    // Option to save images in PNG format as background for each page.
    htmlSaveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;

    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       document.Save(dataDir + "imagesAsPngBackground_out.html", htmlSaveOptions);         
    }
}
```

### Указание папки для изображений

Мы также можем указать папку, в которую изображения будут сохранены во время конвертации PDF в HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SavePDFtoHTMLWithSeparateImageFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Create HtmlSaveOptions with tested feature
        var newOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Specify the separate folder to save images
            SpecialFolderForAllImages = dataDir
        };

        // Save the output HTML
        document.Save(dataDir + "HTMLWithSeparateImageFolder_out.html", newOptions);
    }
}
```

### Создание последующих файлов только с содержимым тела

Недавно нам было предложено ввести функцию, при которой PDF файлы конвертируются в HTML, и пользователь может получить только содержимое тега `<body>` для каждой страницы. Это приведет к созданию одного файла с CSS, `<html>`, `<head>` деталями и всех страниц в других файлах только с содержимым `<body>`.

Чтобы удовлетворить это требование, в класс HtmlSaveOptions было введено новое свойство HtmlMarkupGenerationMode.

С помощью следующего простого фрагмента кода вы можете разделить выходной HTML на страницы. В выходных страницах все HTML объекты должны находиться точно там, где они находятся сейчас (обработка шрифтов и вывод, создание и вывод CSS, создание и вывод изображений), за исключением того, что выходной HTML будет содержать содержимое, в настоящее время размещенное внутри тегов (теперь теги “body” будут опущены). Однако при использовании этого подхода ссылка на CSS является ответственностью вашего кода, поскольку такие вещи, как будут удалены. Для этой цели вы можете прочитать CSS через File.ReadAllText() и отправить его через AJAX на веб-страницу, где он будет применен с помощью jQuery.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithBodyContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // Set HtmlMarkupGenerationMode to generate only body content
            HtmlMarkupGenerationMode =
                Aspose.Pdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent,

            // Specify to split the output into multiple pages
            SplitIntoPages = true
        };

        // Save the output HTML
        document.Save(dataDir + "CreateSubsequentFiles_out.html", options);
    }
}
```

### Прозрачный рендеринг текста

В случае, если исходный/входной PDF файл содержит прозрачные тексты, затененные передними изображениями, могут возникнуть проблемы с рендерингом текста. Поэтому, чтобы учесть такие сценарии, можно использовать свойства SaveShadowedTextsAsTransparentTexts и SaveTransparentTexts.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithTransparentTextRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Initialize HtmlSaveOptions
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable transparent text rendering
            SaveShadowedTextsAsTransparentTexts = true,
            SaveTransparentTexts = true
        };

        // Save the output HTML
        document.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
    }
}
```

### Рендеринг слоев PDF документа

Мы можем рендерить слои PDF документа в отдельном элементе типа слоя во время конвертации PDF в HTML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToHTMLWithLayersRendering()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var htmlOptions = new Aspose.Pdf.HtmlSaveOptions
        {
            // Enable rendering of PDF document layers separately in the output HTML
            ConvertMarkedContentToLayers = true
        };

        // Save the output HTML
        document.Save(dataDir + "LayersRendering_out.html", htmlOptions);
    }
}
```

## См. также 

Эта статья также охватывает следующие темы. Коды такие же, как выше.

_Формат_: **HTML**
- [C# PDF в HTML Код](#csharp-pdf-to-html)
- [C# PDF в HTML API](#csharp-pdf-to-html)
- [C# PDF в HTML Программно](#csharp-pdf-to-html)
- [C# PDF в HTML Библиотека](#csharp-pdf-to-html)
- [C# Сохранить PDF как HTML](#csharp-pdf-to-html)
- [C# Генерировать HTML из PDF](#csharp-pdf-to-html)
- [C# Создать HTML из PDF](#csharp-pdf-to-html)
- [C# PDF в HTML Конвертер](#csharp-pdf-to-html)