---
title: Конвертация HTML в PDF в .NET
linktitle: Конвертация HTML в PDF файл
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Эта тема показывает, как конвертировать HTML в PDF и MHTML в PDF с использованием Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert HTML to PDF in .NET",
    "alternativeHeadline": "Convert HTML and MHTML to PDF with C#",
    "abstract": "Функция конвертации в Aspose.PDF for .NET позволяет бесшовно преобразовывать документы HTML и MHTML в высококачественные PDF файлы. С помощью расширенных параметров настройки пользователи могут контролировать встраивание шрифтов, медиа-запросы и управление внешними ресурсами, обеспечивая при этом точное отображение веб-страниц или локальных HTML файлов в формате PDF с гибкостью, адаптированной к их конкретным потребностям.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1889",
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
    "url": "/net/convert-html-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-html-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

## Обзор 

Эта статья объясняет, как **конвертировать HTML в PDF с помощью C#**. Она охватывает следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

_Формат_: **HTML**
- [C# HTML в PDF](#csharp-html-to-pdf)
- [C# Конвертация HTML в PDF](#csharp-html-to-pdf)
- [C# Как конвертировать HTML в PDF](#csharp-html-to-pdf)

_Формат_: **MHTML**
- [C# MHTML в PDF](#csharp-mhtml-to-pdf)
- [C# Конвертация MHTML в PDF](#csharp-mhtml-to-pdf)
- [C# Как конвертировать MHTML в PDF](#csharp-mhtml-to-pdf)

_Формат_: **WebPage**
- [C# WebPage в PDF](#csharp-webpage-to-pdf)
- [C# Конвертация WebPage в PDF](#csharp-webpage-to-pdf)
- [C# Как конвертировать WebPage в PDF](#csharp-webpage-to-pdf)

## Конвертация C# HTML в PDF

**Aspose.PDF for .NET** — это API для манипуляции PDF, который позволяет бесшовно конвертировать любые существующие HTML документы в PDF. Процесс конвертации HTML в PDF можно гибко настроить.

## Конвертация HTML в PDF

Следующий пример кода на C# показывает, как конвертировать HTML документ в PDF.

<a name="csharp-html-to-pdf"><strong>Шаги: Конвертация HTML в PDF на C#</strong></a>

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Сохраните выходной PDF документ, вызвав метод **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["HTML в PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация HTML в PDF с помощью бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Расширенная конвертация из HTML в PDF

Движок конвертации HTML имеет несколько опций, которые позволяют контролировать процесс конвертации.

### Поддержка медиа-запросов

Медиа-запросы — это популярная техника для предоставления адаптированной таблицы стилей для различных устройств. Мы можем установить тип устройства, используя свойство [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvancedMediaType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document using HtmlLoadOptions with Print media type
    var options = new HtmlLoadOptions
    {
        // Set Print or Screen mode
        HtmlMediaType = Aspose.Pdf.HtmlMediaType.Print
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertHTMLtoPDFAdvancedMediaType_out.pdf");
    }
}
```

### Включение (отключение) встраивания шрифтов

HTML страницы часто используют шрифты (например, шрифты из локальной папки, Google Fonts и т.д.). Мы также можем контролировать встраивание шрифтов в документ, используя свойство [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedEmbedFonts()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Load the HTML file into a document using HtmlLoadOptions with the font embedding option set
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Disable font embedding
         IsEmbedFonts = false
     };

     // Open HTML document
     using (var document = new Aspose.Pdf.Document(dataDir + "test_fonts.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "ConvertHTMLtoPDFAdvanced_EmbedFonts_out.pdf");
     }
 }
```

### Управление загрузкой внешних ресурсов

Движок конвертации предоставляет механизм, который позволяет контролировать загрузку определенных ресурсов, связанных с HTML документом. Класс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) имеет свойство [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources), с помощью которого мы можем определить поведение загрузчика ресурсов. Предположим, нам нужно заменить все изображения PNG на одно изображение `test.jpg` и заменить внешние URL на внутренние для других ресурсов. Для этого мы можем определить пользовательский загрузчик `SamePictureLoader` и указать [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) на это имя.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Load the HTML file into a document with a custom resource loader for external images
    var options = new Aspose.Pdf.HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };

    // Open HTML document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Aspose.Pdf.LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    Aspose.Pdf.LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(dataDir + "test.jpg");
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Set MIME Type
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new Aspose.Pdf.LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new System.Net.Http.HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```

## Конвертация веб-страницы в PDF

Конвертация веб-страницы немного отличается от конвертации локального HTML документа. Чтобы конвертировать содержимое веб-страницы в формат PDF, мы можем сначала получить содержимое HTML страницы, используя экземпляр HttpClient, создать объект Stream, передать содержимое объекту Document и отобразить выходные данные в формате PDF.

При конвертации веб-страницы, размещенной на веб-сервере, в PDF:

<a name="csharp-webpage-to-pdf"><strong>Шаги: Конвертация WebPage в PDF на C#</strong></a>

1. Прочитайте содержимое страницы, используя объект HttpClient.
1. Создайте экземпляр объекта [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) и установите базовый URL.
1. Инициализируйте объект Document, передавая объект потока.
1. При необходимости установите размер страницы и/или ориентацию.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    const string url = "https://en.wikipedia.org/wiki/Aspose_API";

    // Set page size A3 and Landscape orientation;   
    var options = new Aspose.Pdf.HtmlLoadOptions(url)
    {
        PageInfo =
        {
            Width = 842,
            Height = 1191,
            IsLandscape = true
        }
    };

    // Load the web page content as a stream and create a PDF document
    using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url), options))
    {
        // Save PDF document
        document.Save(dataDir + "html_test.pdf");
    }
}

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Предоставление учетных данных для конвертации веб-страницы в PDF

Иногда нам нужно выполнить конвертацию HTML файлов, которые требуют аутентификации и прав доступа, чтобы только авторизованные пользователи могли получать содержимое страницы. Это также включает сценарий, когда некоторые ресурсы/данные, на которые ссылаются внутри HTML, загружаются с внешнего сервера, который требует аутентификации, и для удовлетворения этого требования в класс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) добавлено свойство [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials). Следующий фрагмент кода показывает шаги для передачи учетных данных для запроса HTML и его соответствующих ресурсов при конвертации HTML файла в PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedAuthorized()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     const string url = "http://httpbin.org/basic-auth/user1/password1";
     var credentials = new System.Net.NetworkCredential("user1", "password1");

     var options = new Aspose.Pdf.HtmlLoadOptions(url)
     {
         ExternalResourcesCredentials = credentials
     };

     using (var document = new Aspose.Pdf.Document(GetContentFromUrlAsStream(url, credentials), options))
     {
         // Save PDF document
         document.Save(dataDir + "HtmlTest_out.pdf");
     }
 }

private static Stream GetContentFromUrlAsStream(string url, System.Net.ICredentials credentials = null)
{
    using (var handler = new System.Net.Http.HttpClientHandler { Credentials = credentials })
    using (var httpClient = new System.Net.Http.HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```

### Отображение всего содержимого HTML на одной странице

Aspose.PDF for .NET предоставляет возможность отображать все содержимое на одной странице при конвертации HTML файла в формат PDF. Например, если у вас есть некоторый HTML контент, размер выходных данных которого превышает одну страницу, вы можете использовать опцию для отображения выходных данных на одной PDF странице. Для использования этой опции класс HtmlLoadOptions был расширен флагом IsRenderToSinglePage. Ниже приведен фрагмент кода, показывающий, как использовать эту функциональность.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ConvertHTMLtoPDFAdvancedSinglePageRendering()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Initialize HtmlLoadOptions
     var options = new Aspose.Pdf.HtmlLoadOptions
     {
         // Set Render to single page property
         IsRenderToSinglePage = true
     };

     // Open PDF document
     using (var document = new Aspose.Pdf.Document(dataDir + "HTMLToPDF.html", options))
     {
         // Save PDF document
         document.Save(dataDir + "RenderContentToSamePage_out.pdf");
     }
 }
```

### Отображение HTML с данными SVG

Aspose.PDF for .NET предоставляет возможность конвертировать HTML страницу в PDF документ. Поскольку HTML позволяет добавлять графический элемент SVG в качестве тега на странице, Aspose.PDF также поддерживает конвертацию таких данных в результирующий PDF файл. Следующий фрагмент кода показывает, как конвертировать HTML файлы с тегами графики SVG в помеченные PDF документы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHTMLtoPDFWithSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize HtmlLoadOptions
    var options = new Aspose.Pdf.HtmlLoadOptions(Path.GetDirectoryName(dataDir + "HTMLSVG.html"));

    // Initialize Document object
    using (var document = new Aspose.Pdf.Document(dataDir + "HTMLSVG.html", options))
    {
        // Save PDF document
        document.Save(dataDir + "RenderHTMLwithSVGData_out.pdf");
    }
}
```

## Конвертация MHTML в PDF 

{{% alert color="success" %}}
**Попробуйте конвертировать MHTML в PDF онлайн**

Aspose.PDF for .NET предлагает вам онлайн бесплатное приложение ["MHTML в PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация MHTML в PDF с помощью бесплатного приложения](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME инкапсуляция агрегированных HTML документов">MHTML</abbr>, сокращение от MIME HTML, является форматом архива веб-страниц, используемым для объединения ресурсов, которые обычно представлены внешними ссылками (такими как изображения, Flash анимации, Java апплеты и аудиофайлы) с HTML кодом в один файл. Содержимое MHTML файла кодируется так, как если бы это было HTML электронное письмо, с использованием типа MIME multipart/related. Aspose.PDF for .NET может конвертировать HTML файлы в формат PDF, и с выпуском Aspose.PDF for .NET 9.0.0 мы представили новую функцию, которая позволяет вам конвертировать MHTML файлы в формат PDF. Следующий фрагмент кода показывает, как конвертировать MHTML файлы в формат PDF с помощью C#:

<a name="csharp-mhtml-to-pdf"><strong>Шаги: Конвертация MHTML в PDF на C#</strong></a>

1. Создайте экземпляр класса [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Сохраните выходной PDF документ, вызвав метод **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertMHTtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Initialize MhtLoadOptions with page setup
    var options = new Aspose.Pdf.MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true }
    };

    // Initialize Document object using the MHT file and options
    using (var document = new Aspose.Pdf.Document(dataDir + "fileformatinfo.mht", options))
    {
        // Save PDF document
        document.Save(dataDir + "MhtmlTest_out.pdf");
    }
}
```

## См. также 

Эта статья также охватывает эти темы. Коды такие же, как выше.

_Формат_: **HTML**
- [C# Код HTML в PDF](#csharp-html-to-pdf)
- [C# HTML в PDF API](#csharp-html-to-pdf)
- [C# HTML в PDF Программно](#csharp-html-to-pdf)
- [C# HTML в PDF Библиотека](#csharp-html-to-pdf)
- [C# Сохранить HTML как PDF](#csharp-html-to-pdf)
- [C# Генерировать PDF из HTML](#csharp-html-to-pdf)
- [C# Создать PDF из HTML](#csharp-html-to-pdf)
- [C# Конвертер HTML в PDF](#csharp-html-to-pdf)

_Формат_: **MHTML**
- [C# Код MHTML в PDF](#csharp-mhtml-to-pdf)
- [C# MHTML в PDF API](#csharp-mhtml-to-pdf)
- [C# MHTML в PDF Программно](#csharp-mhtml-to-pdf)
- [C# MHTML в PDF Библиотека](#csharp-mhtml-to-pdf)
- [C# Сохранить MHTML как PDF](#csharp-mhtml-to-pdf)
- [C# Генерировать PDF из MHTML](#csharp-mhtml-to-pdf)
- [C# Создать PDF из MHTML](#csharp-mhtml-to-pdf)
- [C# Конвертер MHTML в PDF](#csharp-mhtml-to-pdf)

_Формат_: **WebPage**
- [C# Код WebPage в PDF](#csharp-webpage-to-pdf)
- [C# WebPage в PDF API](#csharp-webpage-to-pdf)
- [C# WebPage в PDF Программно](#csharp-webpage-to-pdf)
- [C# WebPage в PDF Библиотека](#csharp-webpage-to-pdf)
- [C# Сохранить WebPage как PDF](#csharp-webpage-to-pdf)
- [C# Генерировать PDF из WebPage](#csharp-webpage-to-pdf)
- [C# Создать PDF из WebPage](#csharp-webpage-to-pdf)
- [C# Конвертер WebPage в PDF](#csharp-webpage-to-pdf)