---
title: Программное кадрирование страниц PDF на C#
linktitle: Кадрирование страниц
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/crop-pages/
description: Можно получить свойства страницы, такие как ширина, высота, область для обрезки, а также область для полей и область обрезки, используя Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF для .NET представляет новую мощную функцию, которая позволяет разработчикам программно получать доступ к различным свойствам страницы PDF-файла и управлять ими, включая область содержимого, область обрезки, область под обрез, область иллюстраций и область обрезки. Эта функция упрощает процесс настройки макетов PDF-файлов, обеспечивая точность представления документов и улучшая качество печати при минимальном количестве белых полей. С помощью простых в использовании фрагментов кода пользователи могут легко интегрировать эти возможности в свои приложения, улучшая управление PDF-файлами и их обработку.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Вы можете получить свойства страницы, такие как ширина, высота, поля обрезки и область обрезки, используя Aspose.PDF для .NET"
}
</script>

## Получение свойств страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, область для обрезки и область для полей. Aspose.PDF позволяет получить доступ к этим свойствам.

- **Область для печати**: Область для печати является самой большой областью страницы. Она соответствует размеру страницы (например, A4, A5, US Letter и т. д.), выбранному при печати документа на PostScript или PDF. Другими словами, область для печати определяет физический размер носителя, на котором отображается или печатается PDF-документ.
- **Область для полей**: Если в документе есть поля, то в PDF также будет область для полей. Поля — это количество цвета (или изображения), которое выходит за край страницы. Они используются для того, чтобы при печати и обрезке документа («обрезке») чернила доходили до самого края страницы. Даже если страница обрезана неправильно — обрезана немного не по меткам — на странице не появятся белые поля.
- **Область обрезки**: Область обрезки указывает окончательный размер документа после печати и обрезки.
- **Область изображения**: Область изображения — это область, обведённая вокруг фактического содержимого страниц в ваших документах. Эта область страницы используется при импорте PDF-документов в другие приложения.
- **Область кадрирования**: Область кадрирования — это размер «страницы», который отображается в Adobe Acrobat. В обычном режиме в Adobe Acrobat отображается только содержимое области кадрирования. Для получения подробных описаний этих свойств ознакомьтесь со спецификацией Adobe.Pdf, особенно с разделом 10.10.1 Границы страницы.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) области для печати и области для полей. На рисунке ниже проиллюстрированы эти свойства.
Для получения более подробной информации посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Приведённый ниже фрагмент показывает, как обрезать страницу:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

В этом примере мы использовали образец файла [здесь](crop_page.pdf). Изначально наша страница выглядит так, как показано на рисунке 1.

После изменения страница будет выглядеть как на рисунке 2.

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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