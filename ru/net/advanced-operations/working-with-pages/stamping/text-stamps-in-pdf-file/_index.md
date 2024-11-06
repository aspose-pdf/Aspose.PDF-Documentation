---
title: Добавление текстовых штампов в PDF C#
linktitle: Текстовые штампы в PDF файле
type: docs
weight: 20
url: ru/net/text-stamps-in-the-pdf-file/
description: Добавьте текстовый штамп в документ PDF, используя класс TextStamp с библиотекой Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление текстовых штампов в PDF C#",
    "alternativeHeadline": "Добавление текстовых штампов в PDF C#",
    "author": {
        "@type": "Person",
        "name":"Андрий Андруховский",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация документов PDF",
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
    "url": "/net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Добавьте текстовый штамп в документ PDF, используя класс TextStamp с библиотекой Aspose.PDF для .NET."
}
</script>

## Добавление текстовой печати с помощью C#

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/TextStamp) для добавления текстовой печати в файл PDF. Класс TextStamp предоставляет свойства, необходимые для создания текстовой печати, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текстовую печать, вам нужно создать объект Document и объект TextStamp с необходимыми свойствами. После этого вы можете вызвать метод AddStamp страницы для добавления печати в PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Следующий фрагмент кода показывает, как добавить текстовую печать в файл PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "AddTextStamp.pdf");

// Создать текстовую печать
TextStamp textStamp = new TextStamp("Sample Stamp");
// Установить, является ли печать фоном
textStamp.Background = true;
// Установить начало
textStamp.XIndent = 100;
textStamp.YIndent = 100;
// Повернуть печать
textStamp.Rotate = Rotation.on90;
// Установить свойства текста
textStamp.TextState.Font = FontRepository.FindFont("Arial");
textStamp.TextState.FontSize = 14.0F;
textStamp.TextState.FontStyle = FontStyles.Bold;
textStamp.TextState.FontStyle = FontStyles.Italic;
textStamp.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Aqua);
// Добавить печать на конкретную страницу
pdfDocument.Pages[1].AddStamp(textStamp);

dataDir = dataDir + "AddTextStamp_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
## Определение выравнивания для объекта TextStamp

Добавление водяных знаков в документы PDF является одной из часто требуемых функций, и Aspose.PDF для .NET полностью способен добавлять как изображения, так и текстовые водяные знаки. У нас есть класс с названием [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp), который предоставляет возможность добавлять текстовые печати на файл PDF. Недавно появилась потребность в поддержке функции указания выравнивания текста при использовании объекта TextStamp. Чтобы удовлетворить эту потребность, мы ввели свойство TextAlignment в класс TextStamp. Используя это свойство, мы можем указать горизонтальное выравнивание текста.

Следующий фрагмент кода показывает пример того, как загрузить существующий документ PDF и добавить TextStamp на него.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Создание объекта Document с входным файлом
Document doc = new Document(dataDir+ "DefineAlignment.pdf");
// Создание объекта FormattedText с образцом строки
FormattedText text = new FormattedText("This");
// Добавление новой текстовой строки в FormattedText
text.AddNewLineText("is sample");
text.AddNewLineText("Center Aligned");
text.AddNewLineText("TextStamp");
text.AddNewLineText("Object");
// Создание объекта TextStamp с использованием FormattedText
TextStamp stamp = new TextStamp(text);
// Указание горизонтального выравнивания текстовой печати как центрированное
stamp.HorizontalAlignment = HorizontalAlignment.Center;
// Указание вертикального выравнивания текстовой печати как центрированное
stamp.VerticalAlignment = VerticalAlignment.Center;
// Указание горизонтального выравнивания текста TextStamp как центрированное
stamp.TextAlignment = HorizontalAlignment.Center;
// Установка верхнего поля для объекта печати
stamp.TopMargin = 20;
// Добавление объекта печати на первую страницу документа
doc.Pages[1].AddStamp(stamp);

dataDir = dataDir + "StampedPDF_out.pdf";
// Сохранение обновленного документа
doc.Save(dataDir);
```
## Вставка текста с обводкой как штамп в PDF файл

Мы реализовали настройку режима рендеринга для сценариев добавления и редактирования текста. Чтобы отобразить текст с обводкой, пожалуйста, создайте объект TextState и установите RenderingMode в TextRenderingMode.StrokeText, а также выберите цвет для свойства StrokingColor. Затем привяжите TextState к штампу, используя метод BindTextState().

Следующий фрагмент кода демонстрирует добавление текста с обводкой:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
// Создайте объект TextState для передачи продвинутых свойств
TextState ts = new TextState();
// Установите цвет для обводки
ts.StrokingColor = Color.Gray;
// Установите режим рендеринга текста
ts.RenderingMode = TextRenderingMode.StrokeText;
// Загрузите входной документ PDF
Facades.PdfFileStamp fileStamp = new Facades.PdfFileStamp(new Aspose.Pdf.Document(dataDir + "input.pdf"));

Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
stamp.BindLogo(new Facades.FormattedText("PAID IN FULL", System.Drawing.Color.Gray, "Arial", Facades.EncodingType.Winansi, true, 78));

// Привяжите TextState
stamp.BindTextState(ts);
// Установите начало координат X, Y
stamp.SetOrigin(100, 100);
stamp.Opacity = 5;
stamp.BlendingSpace = Facades.BlendingColorSpace.DeviceRGB;
stamp.Rotation = 45.0F;
stamp.IsBackground = false;
// Добавьте штамп
fileStamp.AddStamp(stamp);
fileStamp.Save(dataDir + "ouput_out.pdf");
fileStamp.Close();
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET библиотеки",
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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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

