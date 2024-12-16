---
title: Работа с размещением изображений
linktitle: Работа с размещением изображений
type: docs
weight: 50
url: /ru/net/working-with-image-placement/
description: Этот раздел описывает особенности работы с размещением изображений в PDF файле с использованием библиотеки C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с размещением изображений",
    "alternativeHeadline": "Как получить позицию изображения в PDF файле",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, размещение изображений в pdf",
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
    "url": "/net/working-with-image-placement/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-image-placement/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает особенности работы с размещением изображений в PDF файле с использованием библиотеки C#."
}
</script>
С выпуском Aspose.PDF для .NET 7.0.0, мы представили классы [ImagePlacement](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) и [ImagePlacementCollection](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection), которые предоставляют возможности, аналогичные описанным выше классам для получения разрешения и позиции изображения в документе PDF.

- ImagePlacementAbsorber выполняет поиск использования изображения как коллекцию объектов ImagePlacement.
- ImagePlacement предоставляет элементы Resolution и Rectangle, которые возвращают фактические значения размещения изображения.

Следующий фрагмент кода также работает с новым графическим интерфейсом [Aspose.Drawing](/pdf/ru/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Загрузите исходный PDF документ
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Загрузите содержимое первой страницы
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Получите свойства изображения
    Console.Out.WriteLine("ширина изображения:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("высота изображения:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("изображение LLX:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("изображение LLY:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("горизонтальное разрешение изображения:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("вертикальное разрешение изображения:" + imagePlacement.Resolution.Y);

    // Извлеките изображение с видимыми размерами
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // Извлеките изображение из ресурсов
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // Создайте битмап с фактическими размерами
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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

