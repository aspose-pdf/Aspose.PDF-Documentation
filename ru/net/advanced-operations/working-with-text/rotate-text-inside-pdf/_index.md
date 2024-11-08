---
title: Вращение текста внутри PDF с использованием C#
linktitle: Вращение текста внутри PDF
type: docs
weight: 50
url: /ru/net/rotate-text-inside-pdf/
description: Узнайте различные способы вращения текста в PDF. Aspose.PDF позволяет вращать текст под любым углом, вращать фрагмент текста или целый абзац.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Вращение текста внутри PDF с использованием C#",
    "alternativeHeadline": "Как вращать текст в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, c#, генерация документов",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
    "url": "/net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotate-text-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Узнайте различные способы вращения текста в PDF. Aspose.PDF позволяет вращать текст под любым углом, вращать фрагмент текста или целый абзац."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Поворот текста внутри PDF с использованием свойства Rotation

Используя свойство Rotation класса [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment), вы можете поворачивать текст под различными углами. Поворот текста может использоваться в различных сценариях генерации документов. Вы можете указать угол поворота в градусах, чтобы повернуть текст в соответствии с вашими требованиями. Пожалуйста, ознакомьтесь с различными сценариями, в которых вы можете реализовать поворот текста.

## Реализация поворота с использованием TextFragment и TextBuilder

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получение конкретной страницы
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создание фрагмента текста
TextFragment textFragment1 = new TextFragment("основной текст");
textFragment1.Position = new Position(100, 600);
// Установка свойств текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создание повернутого фрагмента текста
TextFragment textFragment2 = new TextFragment("повернутый текст");
textFragment2.Position = new Position(200, 600);
// Установка свойств текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Создание повернутого фрагмента текста
TextFragment textFragment3 = new TextFragment("повернутый текст");
textFragment3.Position = new Position(300, 600);
// Установка свойств текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// Создание объекта TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавление фрагмента текста на страницу PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Сохранение документа
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```
## Реализация вращения с использованием TextParagraph и TextBuilder (Вращенные фрагменты)

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получение конкретной страницы
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Создание текстового фрагмента
TextFragment textFragment1 = new TextFragment("вращенный текст");
// Настройка свойств текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установка вращения
textFragment1.TextState.Rotation = 45;
// Создание текстового фрагмента
TextFragment textFragment2 = new TextFragment("основной текст");
// Настройка свойств текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создание текстового фрагмента
TextFragment textFragment3 = new TextFragment("еще один вращенный текст");
// Настройка свойств текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установка вращения
textFragment3.TextState.Rotation = -45;
// Добавление текстовых фрагментов в параграф
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Создание объекта TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавление текстового параграфа на PDF страницу
textBuilder.AppendParagraph(paragraph);
// Сохранение документа
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```
## Реализация вращения с использованием TextFragment и Page.Paragraphs

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получение конкретной страницы
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создание текстового фрагмента
TextFragment textFragment1 = new TextFragment("основной текст");
// Установка свойств текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создание текстового фрагмента
TextFragment textFragment2 = new TextFragment("повернутый текст");
// Установка свойств текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установка вращения
textFragment2.TextState.Rotation = 315;
// Создание текстового фрагмента
TextFragment textFragment3 = new TextFragment("повернутый текст");
// Установка свойств текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установка вращения
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Сохранение документа
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```
## Реализация вращения с использованием TextParagraph и TextBuilder (Весь параграф повернут)

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получение конкретной страницы
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Указание вращения
    paragraph.Rotation = i * 90 + 45;
    // Создание текстового фрагмента
    TextFragment textFragment1 = new TextFragment("Текст параграфа");
    // Создание текстового фрагмента
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Создание текстового фрагмента
    TextFragment textFragment2 = new TextFragment("Вторая строка текста");
    // Установка свойств текста
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Создание текстового фрагмента
    TextFragment textFragment3 = new TextFragment("И немного больше текста...");
    // Установка свойств текста
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Создание объекта TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Добавление текстового фрагмента на страницу PDF
    textBuilder.AppendParagraph(paragraph);
}
// Сохранение документа
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF в .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

