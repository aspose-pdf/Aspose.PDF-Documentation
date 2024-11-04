---
title: Конвертация HTML в PDF в .NET
linktitle: Конвертация HTML в PDF файл
type: docs
weight: 40
url: /net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: Эта тема показывает, как конвертировать HTML в PDF и MHTML в PDF с использованием Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## Обзор

Эта статья объясняет, как **конвертировать HTML в PDF с помощью C#**. Она охватывает следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

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

## Конвертация HTML в PDF на C#
## Преобразование HTML в PDF на C#

**Aspose.PDF для .NET** - это API для работы с PDF, которое позволяет без проблем преобразовывать существующие HTML-документы в PDF. Процесс преобразования HTML в PDF может быть гибко настроен.

## Конвертировать HTML в PDF

Следующий пример кода на C# показывает, как преобразовать HTML-документ в PDF.

<a name="csharp-html-to-pdf"><strong>Шаги: Преобразование HTML в PDF на C#</strong></a>

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Сохраните выходной документ PDF, вызвав метод **Document.Save()**.

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["HTML в PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете изучить функциональность и качество его работы.
{{% /alert %}}

[![Преобразование Aspose.PDF HTML в PDF с помощью бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)

## Расширенное преобразование из HTML в PDF

Движок преобразования HTML имеет несколько опций, позволяющих нам контролировать процесс конвертации.

### Поддержка медиа запросов

Медиа запросы - популярная техника для предоставления специализированного стилевого файла различным устройствам. Мы можем установить тип устройства, используя свойство [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype).

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // установите режим Печать или Экран
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### Включение (отключение) встраивания шрифтов

HTML-страницы часто используют шрифты (например, шрифты из локальной папки, Google Fonts и т.д.). Мы также можем контролировать встраивание шрифтов в документ с помощью свойства [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts).

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // Отключение встраивания шрифтов
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### Управление загрузкой внешних ресурсов

Механизм преобразования предоставляет механизм, который позволяет вам контролировать загрузку определенных ресурсов, связанных с HTML-документом.
Класс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) имеет свойство [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources), с помощью которого мы можем определить поведение загрузчика ресурсов.
Класс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) имеет свойство [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources), с помощью которого мы можем определить поведение загрузчика ресурсов.
Предположим, что нам нужно заменить все изображения PNG на одно изображение `test.jpg` и заменить внешний URL на внутренний для других ресурсов.
Для этого мы можем определить пользовательский загрузчик `SamePictureLoader` и указать [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) на это имя.

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument = new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            // Установить MIME тип
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## Конвертация веб-страницы в PDF

Конвертация веб-страницы немного отличается от конвертации локального HTML-документа. Для преобразования содержимого веб-страницы в формат PDF сначала можно получить содержимое HTML-страницы с использованием экземпляра HttpClient, создать объект Stream, передать содержимое в объект Document и отобразить результат в формате PDF.

При конвертации веб-страницы, размещенной на веб-сервере, в PDF:

<a name="csharp-webpage-to-pdf"><strong>Шаги: Конвертация веб-страницы в PDF на C#</strong></a>

1. Прочитайте содержимое страницы с помощью объекта HttpClient.
1. Создайте объект [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) и установите базовый URL.
1. Инициализируйте объект Document, передав объект Stream.
1. При необходимости установите размер страницы и/или ориентацию.

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://en.wikipedia.org/wiki/Aspose_API";
    // Установите размер страницы A3 и ориентацию Landscape;   
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Предоставление учетных данных для конвертации веб-страницы в PDF

Иногда нам нужно выполнить конвертацию HTML-файлов, которые требуют аутентификации и привилегий доступа, чтобы только аутентифицированные пользователи могли получить содержимое страницы. Это также включает сценарий, когда некоторые ресурсы/данные, на которые ссылается HTML, загружаются с некоторого внешнего сервера, который требует аутентификации и для удовлетворения этой потребности, свойство [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) добавлено в класс [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions). Следующий пример кода показывает шаги по передаче учетных данных для запроса HTML и его соответствующих ресурсов при конвертации HTML-файла в PDF.

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### Отрисовка всего HTML-содержимого на одной странице

Aspose.PDF для .NET позволяет отрисовывать все содержимое на одной странице при конвертации HTML-файла в формат PDF. Например, если у вас есть HTML-содержимое, размер которого превышает одну страницу, вы можете использовать опцию для вывода данных в одну страницу PDF. Для использования этой опции класс HtmlLoadOptions был расширен флагом IsRenderToSinglePage. Приведенный ниже фрагмент кода показывает, как использовать эту функциональность.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Инициализация опций HTMLLoadSave
HtmlLoadOptions options = new HtmlLoadOptions();
// Установка свойства отрисовки на одну страницу
options.IsRenderToSinglePage = true;
// Загрузка документа
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// Сохранение
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### Отрисовка HTML с данными SVG
### Отрисовка HTML с данными SVG

Aspose.PDF для .NET предоставляет возможность конвертировать HTML-страницу в документ PDF. Поскольку HTML позволяет добавлять графический элемент SVG в виде тега на странице, Aspose.PDF также поддерживает конвертацию таких данных в результирующий файл PDF. Следующий фрагмент кода показывает, как конвертировать HTML-файлы с графическими тегами SVG в тегированные PDF-документы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Установить путь к входному файлу
string inFile = dataDir + "HTMLSVG.html";
// Установить путь к выходному файлу
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// Инициализировать HtmlLoadOptions
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// Инициализировать объект Document
Document pdfDocument = new Document(inFile, options);
// сохранить
pdfDocument.Save(outFile);
```

## Конвертация MHTML в PDF 

{{% alert color="success" %}}
**Попробуйте конвертировать MHTML в PDF онлайн**
**Попробуйте конвертировать MHTML в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["MHTML в PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), где вы можете изучить функциональность и качество его работы.

[![Конвертация MHTML в PDF с помощью бесплатного приложения Aspose.PDF](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME инкапсуляция агрегированных HTML документов">MHTML</abbr>, сокращенно от MIME HTML, это формат архива веб-страниц, используемый для объединения ресурсов, которые обычно представлены внешними ссылками (такими как изображения, анимации Flash, апплеты Java и аудиофайлы) с HTML-кодом в один файл.
<abbr title="MIME инкапсуляция агрегированных HTML документов">MHTML</abbr>, сокращение от MIME HTML, это формат архивации веб-страниц, используемый для объединения ресурсов, которые обычно представлены внешними ссылками (такими как изображения, анимации Flash, Java апплеты и аудиофайлы) с HTML кодом в один файл.

<a name="csharp-mhtml-to-pdf"><strong>Шаги: Конвертация MHTML в PDF на C#</strong></a>

1. Создайте экземпляр класса [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/).
3. Сохраните выходной PDF документ, вызвав метод **Document.Save()**.

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument = new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## См. также

Эта статья также охватывает эти темы.
Эта статья также охватывает следующие темы.

_Формат_: **HTML**
- [C# HTML в PDF код](#csharp-html-to-pdf)
- [C# HTML в PDF API](#csharp-html-to-pdf)
- [C# HTML в PDF программно](#csharp-html-to-pdf)
- [C# библиотека HTML в PDF](#csharp-html-to-pdf)
- [C# сохранить HTML как PDF](#csharp-html-to-pdf)
- [C# генерация PDF из HTML](#csharp-html-to-pdf)
- [C# создание PDF из HTML](#csharp-html-to-pdf)
- [C# конвертер HTML в PDF](#csharp-html-to-pdf)

_Формат_: **MHTML**
- [C# MHTML в PDF код](#csharp-mhtml-to-pdf)
- [C# MHTML в PDF API](#csharp-mhtml-to-pdf)
- [C# MHTML в PDF программно](#csharp-mhtml-to-pdf)
- [C# библиотека MHTML в PDF](#csharp-mhtml-to-pdf)
- [C# сохранить MHTML как PDF](#csharp-mhtml-to-pdf)
- [C# генерация PDF из MHTML](#csharp-mhtml-to-pdf)
- [C# создание PDF из MHTML](#csharp-mhtml-to-pdf)
- [C# конвертер MHTML в PDF](#csharp-mhtml-to-pdf)

_Формат_: **WebPage**
- [C# WebPage в PDF код](#csharp-webpage-to-pdf)
- [C# WebPage в PDF API](#csharp-webpage-to-pdf)
- [C# WebPage в PDF программно](#csharp-webpage-to-pdf)
- [C# Веб-страница в PDF программно](#csharp-webpage-to-pdf)
- [C# Библиотека для конвертации веб-страницы в PDF](#csharp-webpage-to-pdf)
- [C# Сохранение веб-страницы как PDF](#csharp-webpage-to-pdf)
- [C# Создание PDF из веб-страницы](#csharp-webpage-to-pdf)
- [C# Создание PDF из веб-страницы](#csharp-webpage-to-pdf)
- [C# Конвертер веб-страницы в PDF](#csharp-webpage-to-pdf)
