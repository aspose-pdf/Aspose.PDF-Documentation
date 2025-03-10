---
title: Изменение размера страницы PDF с помощью C#
linktitle: Изменение размера страницы PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/change-page-size/
description: Измените размер страницы вашего PDF-документа с помощью библиотеки Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change PDF Page Size with C#",
    "alternativeHeadline": "Effortlessly Resize PDF Pages in C#",
    "abstract": "Новая функциональность в Aspose.PDF for .NET позволяет разработчикам легко изменять размер страниц PDF-документов программно. Всего за несколько строк кода пользователи могут изменять существующие размеры PDF, улучшая свои возможности управления документами и обеспечивая совместимость с различными требованиями к макету. Эта функция упрощает процесс изменения размера страниц PDF до предпочитаемых форматов, таких как A4, непосредственно в приложениях .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "300",
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
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2024-11-26",
    "description": "Измените размер страницы вашего PDF-документа с помощью библиотеки Aspose.PDF for .NET."
}
</script>

## Изменение размера страницы PDF

Aspose.PDF for .NET позволяет вам изменять размер страниц PDF с помощью простых строк кода в ваших приложениях .NET. Эта тема объясняет, как обновить/изменить размеры страниц (размер) существующего PDF-файла.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) содержит метод SetPageSize(...), который позволяет установить размер страницы. Ниже приведен фрагмент кода, который обновляет размеры страниц за несколько простых шагов:

1. Загрузите исходный PDF-файл.
1. Получите страницы в объект [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Получите заданную страницу.
1. Вызовите метод SetPageSize(..), чтобы обновить ее размеры.
1. Вызовите метод Save(..) класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), чтобы сгенерировать PDF-файл с обновленными размерами страниц.

{{% alert color="primary" %}}

Обратите внимание, что свойства высоты и ширины используют пункты в качестве основной единицы, где 1 дюйм = 72 пункта и 1 см = 1/2.54 дюйма = 0.3937 дюйма = 28.3 пункта.

{{% /alert %}}

Следующий фрагмент кода показывает, как изменить размеры страниц PDF на размер A4.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Set the page size as A4 (11.7 x 8.3 in) and in Aspose.Pdf, 1 inch = 72 points
        // So A4 dimensions in points will be (842.4, 597.6)
        pdfPage.SetPageSize(597.6, 842.4);
        // Save PDF document
        document.Save(dataDir + "UpdateDimensions_out.pdf"); 
    }
}
```

## Получить размер страницы PDF

Вы можете прочитать размер страницы PDF существующего PDF-файла с помощью Aspose.PDF for .NET. Следующий пример кода показывает, как прочитать размеры страниц PDF с помощью C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateDimensions.pdf"))
    {
        // Adds a blank page to pdf document
        Page page = document.Pages.Count > 0 ? document.Pages[1] : document.Pages.Add();
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
        // Rotate page at 90 degree angle
        page.Rotate = Rotation.on90;
        // Get page height and width information
        Console.WriteLine(page.GetPageRect(true).Width.ToString() + ":" + page.GetPageRect(true).Height);
    }
}
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