---
title: Добавление штампов с изображениями в PDF с использованием C#
linktitle: Штампы с изображениями в файле PDF
type: docs
weight: 10
url: /ru/net/image-stamps-in-pdf-page/
description: Добавьте штамп с изображением в ваш PDF-документ с использованием класса ImageStamp и библиотеки Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление штампов с изображениями в PDF с использованием C#",
    "alternativeHeadline": "Добавление штампов с изображениями в PDF с использованием C#",
    "author": {
        "@type": "Person",
        "name":"Андрий Андруховский",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация PDF-документов",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "Добавьте штамп с изображением в ваш PDF-документ с использованием класса ImageStamp и библиотеки Aspose.PDF."
}
</script>
```
## Добавление штампа с изображением в PDF файл

Вы можете использовать класс ImageStamp, чтобы добавить штамп с изображением в PDF файл. Класс ImageStamp предоставляет необходимые свойства для создания штампа на основе изображения, такие как высота, ширина, прозрачность и так далее.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Для добавления штампа с изображением:

1. Создайте объект Document и объект ImageStamp с необходимыми свойствами.
1. Вызовите метод AddStamp класса Page, чтобы добавить штамп в PDF.

Следующий фрагмент кода показывает, как добавить штамп с изображением в PDF файл.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Создать штамп с изображением
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// Добавить штамп на определенную страницу
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
## Управление качеством изображения при добавлении штампа

При добавлении изображения в качестве объекта штампа, вы можете контролировать качество изображения. Свойство Quality класса ImageStamp используется для этой цели. Оно указывает качество изображения в процентах (допустимые значения от 0 до 100).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Открыть документ
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Создать штамп изображения
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## Штамп изображения как фон в плавающем блоке

API Aspose.PDF позволяет добавлять штамп изображения как фон в плавающем блоке.
API Aspose.PDF позволяет добавить изображение в виде печати на фон в плавающем блоке.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Создание объекта документа
Document doc = new Document();
// Добавление страницы в документ PDF
Page page = doc.Pages.Add();
// Создание объекта FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// Установка левой позиции для FloatingBox
aBox.Left = 40;
// Установка верхней позиции для FloatingBox
aBox.Top = 80;
// Установка горизонтального выравнивания для FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Добавление текстового фрагмента в коллекцию параграфов FloatingBox
aBox.Paragraphs.Add(new TextFragment("основной текст"));
// Установка границы для FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// Добавление фонового изображения
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// Установка фонового цвета для FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// Добавление FloatingBox в коллекцию параграфов объекта страницы
page.Paragraphs.Add(aBox);
// Сохранение документа PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
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
                "areaServed": "US",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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

