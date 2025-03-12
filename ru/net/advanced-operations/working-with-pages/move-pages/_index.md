---
title: Перемещение страниц PDF программным способом на C#
linktitle: Переместить страницы PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/move-pages/
description: Попробуйте переместить страницы в нужное место или в конец PDF-файла с помощью Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF для .NET представляет новую мощную функцию, которая позволяет пользователям программно перемещать страницы PDF между документами или изменять их расположение в одном и том же документе. Эта функциональность расширяет возможности работы с PDF-файлами, позволяя разработчикам вставлять страницы в определённые места и легко управлять организацией страниц, сохраняя целостность документа.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Попробуйте переместить страницы в нужное место или в конец PDF-файла с помощью Aspose.PDF для .NET"
}
</script>

## Перемещение страницы из одного PDF-документа в другой

Этот раздел объясняет, как переместить страницу из одного PDF-документа в конец другого документа с помощью C#.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Чтобы переместить страницу, нам необходимо:

1. Создать объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с исходным PDF-файлом.
1. Создать объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с целевым PDF-файлом.
1. Получить страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Добавить](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) страницу в целевой документ.
1. Сохранить выходной PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Удалить](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) страницу в исходном документе.
1. Сохранить исходный PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода показывает, как переместить одну страницу.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## Перемещение нескольких страниц из одного PDF-документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) для исходного PDF-файла.
1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) для целевого PDF-файла.
1. Определите массив с номерами страниц для перемещения.
1. Пройдитесь по массиву:
    1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1. [Добавьте](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) страницу в целевой документ.
1. Сохраните выходной PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. Используйте массив для [удаления](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) страницы в исходном документе.
1. Сохраните исходный PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода демонстрирует, как перенести несколько страниц из одного PDF-документа в другой.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## Перемещение страницы в новое место в текущем PDF-документе

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) для исходного PDF-файла.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Добавьте](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) страницу в новое место (например, в конец).
1. [Удалите](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) страницу из предыдущего места.
1. Сохраните выходной PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
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