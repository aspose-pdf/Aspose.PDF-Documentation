---
title: Конвертация PDF в документы Microsoft Word в .NET
linktitle: Конвертация PDF в Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Узнайте, как написать код на C# для конвертации PDF в форматы Microsoft Word с Aspose.PDF for .NET и настроить конвертацию PDF в DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET представляет мощную функцию для конвертации PDF файлов в форматы Microsoft Word (DOC и DOCX) с использованием C#. Эта функциональность не только улучшает редактирование документов, но и предоставляет гибкие варианты для распознавания текста и форматирования, обеспечивая высокую точность между исходным PDF и полученным документом Word.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1495",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обзор

Эта статья объясняет, как **конвертировать PDF в документы Microsoft Word с помощью C#**. Она охватывает следующие темы.

_Формат_: **DOC**

- [C# PDF в DOC](#csharp-pdf-to-doc)
- [C# Конвертация PDF в DOC](#csharp-pdf-to-doc)
- [C# Как конвертировать PDF файл в DOC](#csharp-pdf-to-doc)

_Формат_: **DOCX**

- [C# PDF в DOCX](#csharp-pdf-to-docx)
- [C# Конвертация PDF в DOCX](#csharp-pdf-to-docx)
- [C# Как конвертировать PDF файл в DOCX](#csharp-pdf-to-docx)

_Формат_: **Word**

- [C# PDF в Word](#csharp-pdf-to-docx)
- [C# Конвертация PDF в Word](#csharp-pdf-to-doc)
- [C# Как конвертировать PDF файл в Word](#csharp-pdf-to-docx)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Конвертация PDF в DOC и DOCX

Одной из самых популярных функций является конвертация PDF в Microsoft Word DOC, что делает управление контентом более простым. **Aspose.PDF for .NET** позволяет вам быстро и эффективно конвертировать PDF файлы в формат DOC и DOCX.

## Конвертация PDF в файл DOC (Microsoft Word 97-2003)

Конвертируйте PDF файлы в формат DOC с легкостью и полным контролем. Aspose.PDF for .NET гибок и поддерживает широкий спектр конвертаций. Конвертация страниц из PDF документов в изображения, например, является очень популярной функцией.

Многие из наших клиентов запрашивали конвертацию из PDF в DOC: конвертацию PDF файла в документ Microsoft Word. Клиенты хотят этого, потому что PDF файлы не могут быть легко отредактированы, в то время как документы Word могут. Некоторые компании хотят, чтобы их пользователи могли манипулировать текстом, таблицами и изображениями в файлах, которые изначально были PDF.

Сохраняя традицию упрощения и понимания, Aspose.PDF for .NET позволяет вам преобразовать исходный PDF файл в файл DOC всего за две строки кода. Для реализации этой функции мы ввели перечисление под названием SaveFormat, и его значение .Doc позволяет вам сохранить исходный файл в формате Microsoft Word.

Следующий фрагмент кода на C# показывает, как конвертировать PDF файл в формат DOC.

<a name="csharp-pdf-to-doc"><strong>Шаги: Конвертация PDF в DOC на C#</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в формате **SaveFormat.Doc**, вызвав метод **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### Использование класса DocSaveOptions

Класс [`DocSaveOptions`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/docsaveoptions) предоставляет множество свойств, которые улучшают конвертацию PDF файлов в формат DOC. Среди этих свойств, Mode позволяет вам указать режим распознавания для содержимого PDF. Вы можете выбрать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет свои преимущества и ограничения:

- Режим [`Textbox`](https://reference.aspose.com/pdf/ru/net/aspose.pdf.docsaveoptions/recognitionmode) быстрый и хорошо сохраняет оригинальный вид PDF файла, но редактируемость полученного документа может быть ограничена. Каждый визуально сгруппированный текстовый блок в оригинальном PDF преобразуется в текстовое поле в выходном документе. Это достигает максимального сходства с оригиналом, так что выходной документ выглядит хорошо, но состоит исключительно из текстовых полей, которые можно редактировать в Microsoft Word, что довольно сложно.
- Режим [`Flow`](https://reference.aspose.com/pdf/ru/net/aspose.pdf.docsaveoptions/recognitionmode) является полным режимом распознавания, где движок выполняет группировку и многоуровневый анализ, чтобы восстановить оригинальный документ в соответствии с намерением автора, создавая легко редактируемый документ. Ограничение заключается в том, что выходной документ может выглядеть иначе, чем оригинал.

Свойство [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) может использоваться для контроля относительной близости между текстовыми элементами. Это означает, что расстояние нормируется по размеру шрифта. Более крупные шрифты могут иметь большие промежутки между слогами и все еще считаться единым целым. Оно указывается в процентах от размера шрифта; например, 1 = 100%. Это означает, что два символа размером 12pt, расположенные на расстоянии 12 pt друг от друга, являются близкими.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/docsaveoptions/properties/recognizebullets) используется для включения распознавания маркеров во время конвертации.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for .NET предлагает вам онлайн бесплатное приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество работы.

[![Конвертировать PDF в DOC](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертация PDF в файл DOCX (Microsoft Word 2007-2024)

API Aspose.PDF for .NET позволяет вам читать и конвертировать PDF документы в DOCX с использованием C# и любого языка .NET. DOCX — это известный формат для документов Microsoft Word, структура которого была изменена с простого двоичного на комбинацию XML и двоичных файлов. Файлы Docx можно открывать с помощью Word 2007 и более поздних версий, но не с помощью более ранних версий MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на C# показывает, как конвертировать PDF файл в формат DOCX.

<a name="csharp-pdf-to-docx"><strong>Шаги: Конвертация PDF в DOCX на C#</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/) с исходным PDF документом.
2. Сохраните его в формате **SaveFormat.DocX**, вызвав метод **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### Конвертация PDF в DOCX в улучшенном режиме

Чтобы получить лучшие результаты конвертации PDF в DOCX, вы можете использовать режим `EnhancedFlow`.
Основное отличие между Flow и Enhanced Flow заключается в том, что таблицы (как с границами, так и без) распознаются как настоящие таблицы, а не как текст с изображением на заднем плане.
Также происходит распознавание нумерованных списков и многих других мелочей.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for .NET предлагает вам онлайн бесплатное приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в Word Бесплатное приложение](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Коды такие же, как выше.

_Формат_: **Word**

- [C# PDF в Word Код](#csharp-pdf-to-docx)
- [C# PDF в Word API](#csharp-pdf-to-docx)
- [C# PDF в Word Программно](#csharp-pdf-to-docx)
- [C# PDF в Word Библиотека](#csharp-pdf-to-docx)
- [C# Сохранить PDF как Word](#csharp-pdf-to-docx)
- [C# Генерировать Word из PDF](#csharp-pdf-to-docx)
- [C# Создать Word из PDF](#csharp-pdf-to-docx)
- [C# PDF в Word Конвертер](#csharp-pdf-to-docx)

_Формат_: **DOC**

- [C# PDF в DOC Код](#csharp-pdf-to-doc)
- [C# PDF в DOC API](#csharp-pdf-to-doc)
- [C# PDF в DOC Программно](#csharp-pdf-to-doc)
- [C# PDF в DOC Библиотека](#csharp-pdf-to-doc)
- [C# Сохранить PDF как DOC](#csharp-pdf-to-doc)
- [C# Генерировать DOC из PDF](#csharp-pdf-to-doc)
- [C# Создать DOC из PDF](#csharp-pdf-to-doc)
- [C# PDF в DOC Конвертер](#csharp-pdf-to-doc)

_Формат_: **DOCX**

- [C# PDF в DOCX Код](#csharp-pdf-to-docx)
- [C# PDF в DOCX API](#csharp-pdf-to-docx)
- [C# PDF в DOCX Программно](#csharp-pdf-to-docx)
- [C# PDF в DOCX Библиотека](#csharp-pdf-to-docx)
- [C# Сохранить PDF как DOCX](#csharp-pdf-to-docx)
- [C# Генерировать DOCX из PDF](#csharp-pdf-to-docx)
- [C# Создать DOCX из PDF](#csharp-pdf-to-docx)
- [C# PDF в DOCX Конвертер](#csharp-pdf-to-docx)