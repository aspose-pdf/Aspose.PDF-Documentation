---
title: Конвертация PDF в HTML в .NET
linktitle: Конвертация PDF в формат HTML
type: docs
weight: 50
url: ru/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Эта тема показывает, как конвертировать PDF файл в формат HTML с помощью библиотеки Aspose.PDF для C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Обзор

Эта статья объясняет, как **конвертировать PDF в HTML с использованием C#**. Она охватывает следующие темы.

_Формат_: **HTML**
- [C# PDF в HTML](#csharp-pdf-to-html)
- [C# Конвертация PDF в HTML](#csharp-pdf-to-html)
- [C# Как конвертировать PDF файл в HTML](#csharp-pdf-to-html)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Конвертация PDF в HTML

**Aspose.PDF для .NET** предоставляет множество функций для конвертации различных форматов файлов в документы PDF и конвертации PDF файлов в различные выходные форматы.
**Aspose.PDF для .NET** предоставляет множество функций для конвертации различных форматов файлов в документы PDF и конвертации файлов PDF в различные выходные форматы.

**Aspose.PDF для .NET** поддерживает функции для конвертации PDF-файла в HTML. Основные задачи, которые вы можете выполнить с помощью библиотеки Aspose.PDF, перечислены:

- конвертировать PDF в HTML;
- разделение вывода на многостраничный HTML;
- указание папки для сохранения файлов SVG;
- сжатие изображений SVG во время конвертации;
- указание папки для изображений;
- создание последующих файлов только с содержимым тела;
- прозрачное отображение текста;
- рендеринг слоев документа PDF.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF для .NET предоставляет двухстрочный код для трансформации исходного PDF-файла в HTML.
Aspose.PDF для .NET предоставляет две строки кода для преобразования исходного PDF файла в HTML.

<a name="csharp-pdf-to-html"><strong>Шаги: Конвертация PDF в HTML в C#</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в формат **SaveFormat.Html** вызвав метод **Document.Save()**.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Откройте исходный PDF документ
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Сохраните файл в формате документа MS
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### Разделение выходных данных на многостраничный HTML

При конвертации большого PDF файла с несколькими страницами в формат HTML, результатом является одна HTML страница.
При конвертации большого PDF-файла с несколькими страницами в формат HTML, результат появляется в виде одной HTML-страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Открыть исходный PDF-документ
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Создать объект настроек сохранения HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Указать разделение выходного файла на несколько страниц
htmlOptions.SplitIntoPages = true;

// Сохранить документ
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### Указать папку для сохранения SVG-файлов

Во время конвертации PDF в HTML можно указать папку, в которую должны быть сохранены SVG-изображения.
Во время конвертации PDF в HTML возможно указать папку для сохранения изображений SVG.

```csharp
// Загрузка файла PDF
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// Создание объекта опций сохранения HTML
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Указание папки, куда сохранять изображения SVG во время конвертации PDF в HTML
newOptions.SpecialFolderForSvgImages = dataDir;

// Сохранение результирующего файла
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### Сжатие изображений SVG во время конвертации

Для сжатия изображений SVG во время конвертации PDF в HTML, пожалуйста, используйте следующий код:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Создание HtmlSaveOption с проверенной функцией
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Сжатие изображений SVG, если таковые имеются
newOptions.CompressSvgGraphicsIfAny = true;
```

### Указание папки для изображений

Мы также можем указать папку, в которую будут сохраняться изображения во время конвертации PDF в HTML:
Мы также можем указать папку, в которую будут сохраняться изображения при конвертации PDF в HTML:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Создайте HtmlSaveOption с проверенной функцией
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Укажите отдельную папку для сохранения изображений
newOptions.SpecialFolderForAllImages = dataDir;
```

### Создание последующих файлов только с содержимым тега Body

Недавно нам поступил запрос на внедрение функции, при которой файлы PDF конвертируются в HTML, и пользователь может получать содержимое тега `<body>` для каждой страницы. Это приведет к созданию одного файла с CSS, деталями `<html>`, `<head>` и всех страниц в других файлах только с содержимым `<body>`.

Для удовлетворения этого требования было введено новое свойство, HtmlMarkupGenerationMode, в класс HtmlSaveOptions.

С помощью следующего простого фрагмента кода вы можете разделить выходной HTML на страницы.
С помощью следующего простого фрагмента кода вы можете разделить выходной HTML на страницы.

```csharp
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// Это проверенная настройка
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### Отображение прозрачного текста

В случае, если исходный/входной файл PDF содержит прозрачные тексты, затененные передними изображениями, могут возникнуть проблемы с рендерингом текста. Поэтому для решения таких сценариев можно использовать свойства SaveShadowedTextsAsTransparentTexts и SaveTransparentTexts.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### Отрисовка слоёв PDF-документа

Мы можем отрисовывать слои PDF-документа в отдельных элементах типа слоя во время конвертации PDF в HTML:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// Создаем объект настроек сохранения HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Указываем отрисовку слоёв PDF-документа отдельно в выходном HTML
htmlOptions.ConvertMarkedContentToLayers = true;

// Сохраняем документ
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## Смотрите также

Эта статья также охватывает следующие темы. Коды такие же, как выше.

_Формат_: **HTML**
- [Код C# PDF в HTML](#csharp-pdf-to-html)
- [API C# PDF в HTML](#csharp-pdf-to-html)
- [Программное C# PDF в HTML](#csharp-pdf-to-html)
- [Библиотека C# PDF в HTML](#csharp-pdf-to-html)
- [C# Сохранить PDF как HTML](#csharp-pdf-to-html)
- [C# Сохранить PDF как HTML](#csharp-pdf-to-html)
- [C# Генерировать HTML из PDF](#csharp-pdf-to-html)
- [C# Создать HTML из PDF](#csharp-pdf-to-html)
- [C# Конвертер PDF в HTML](#csharp-pdf-to-html)
