```
---
title: Получение и поиск изображений в PDF
linktitle: Поиск и получение изображений
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: Этот раздел объясняет, как искать и получать изображения из документа PDF с помощью библиотеки Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Получение и поиск изображений в PDF",
    "alternativeHeadline": "Как получить и найти изображения в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, .net, получить изображение, поиск изображения",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел объясняет, как искать и получать изображения из документа PDF с помощью библиотеки Aspose.PDF."
}
</script>
```
ImagePlacementAbsorber позволяет искать изображения на всех страницах PDF документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Для поиска изображений во всем документе:

1. Вызовите метод Accept коллекции Pages. Метод Accept принимает объект ImagePlacementAbsorber в качестве параметра. Это возвращает коллекцию объектов ImagePlacement.
1. Пройдитесь по объектам ImagePlacements и получите их свойства (изображение, размеры, разрешение и так далее).

Следующий фрагмент кода показывает, как искать все изображения в документе.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Открыть документ
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Создать объект ImagePlacementAbsorber для поиска размещения изображений
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Применить absorber ко всем страницам
doc.Pages.Accept(abs);

// Пройтись по всем ImagePlacements, получить изображение и свойства ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Получить изображение с помощью объекта ImagePlacement
    XImage image = imagePlacement.Image;

    // Отобразить свойства размещения изображений для всех размещений
    Console.Out.WriteLine("ширина изображения:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("высота изображения:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("LLX изображения:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("LLY изображения:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("горизонтальное разрешение изображения:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("вертикальное разрешение изображения:" + imagePlacement.Resolution.Y);
}
```
Для получения изображения со страницы используйте следующий код:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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

