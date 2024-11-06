---
title: Поворот текста внутри PDF с использованием Python
linktitle: Поворот текста внутри PDF
type: docs
weight: 50
url: ru/python-net/rotate-text-inside-pdf/
description: Узнайте различные способы поворота текста в PDF. Aspose.PDF позволяет поворачивать текст на любой угол, поворачивать фрагмент текста или целый абзац.
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Поворот текста внутри PDF с использованием Python",
    "alternativeHeadline": "Как повернуть текст в PDF файле",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание pdf документов",
    "keywords": "pdf, python, создание документов",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Узнайте различные способы поворота текста в PDF. Aspose.PDF позволяет поворачивать текст на любой угол, поворачивать фрагмент текста или целый абзац."
}
</script>


## Поворот текста внутри PDF с использованием свойства вращения

Используя свойство Rotation класса [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment), вы можете поворачивать текст под различными углами. Поворот текста может быть использован в различных сценариях генерации документа. Вы можете указать угол поворота в градусах, чтобы повернуть текст по вашему требованию. Пожалуйста, ознакомьтесь со следующими различными сценариями, в которых вы можете реализовать поворот текста.

## Реализация поворота с использованием TextFragment и TextBuilder

```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализировать объект документа
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создать текстовый фрагмент
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// Установить свойства текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создать повернутый текстовый фрагмент
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// Установить свойства текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// Создать повернутый текстовый фрагмент
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// Установить свойства текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// создать объект TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавить текстовый фрагмент на страницу PDF
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// Сохранить документ
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## Реализация вращения с использованием TextParagraph и TextBuilder (Вращаемые фрагменты)

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// Создать текстовый фрагмент
TextFragment textFragment1 = new TextFragment("повернутый текст");
// Установить свойства текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установить вращение
textFragment1.TextState.Rotation = 45;
// Создать текстовый фрагмент
TextFragment textFragment2 = new TextFragment("основной текст");
// Установить свойства текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создать текстовый фрагмент
TextFragment textFragment3 = new TextFragment("другой повернутый текст");
// Установить свойства текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установить вращение
textFragment3.TextState.Rotation = -45;
// Добавить текстовые фрагменты в параграф
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// Создать объект TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавить текстовый параграф на страницу PDF
textBuilder.AppendParagraph(paragraph);
// Сохранить документ
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## Реализация вращения с использованием TextFragment и Page.Paragraphs

```csharp
// Для полного примера и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализировать объект документа
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создать текстовый фрагмент
TextFragment textFragment1 = new TextFragment("основной текст");
// Установить свойства текста
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Создать текстовый фрагмент
TextFragment textFragment2 = new TextFragment("повернутый текст");
// Установить свойства текста
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установить вращение
textFragment2.TextState.Rotation = 315;
// Создать текстовый фрагмент
TextFragment textFragment3 = new TextFragment("повернутый текст");
// Установить свойства текста
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// Установить вращение
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// Сохранить документ
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## Реализация Вращения с использованием TextParagraph и TextBuilder (Вращение всего абзаца)

```csharp
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Инициализация объекта документа
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // Указать вращение
    paragraph.Rotation = i * 90 + 45;
    // Создать текстовый фрагмент
    TextFragment textFragment1 = new TextFragment("Текст абзаца");
    // Создать текстовый фрагмент
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Создать текстовый фрагмент
    TextFragment textFragment2 = new TextFragment("Вторая строка текста");
    // Установить свойства текста
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // Создать текстовый фрагмент
    TextFragment textFragment3 = new TextFragment("И еще немного текста...");
    // Установить свойства текста
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // Создать объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Добавить текстовый фрагмент на страницу PDF
    textBuilder.AppendParagraph(paragraph);
}
// Сохранить документ
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>