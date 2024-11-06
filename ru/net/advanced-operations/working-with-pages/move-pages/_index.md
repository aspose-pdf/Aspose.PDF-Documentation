---
title: Переместить страницы PDF программно на C#
linktitle: Перемещение страниц PDF
type: docs
weight: 20
url: ru/net/move-pages/
description: Попробуйте переместить страницы в желаемое место или в конец файла PDF с помощью Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Переместить страницы PDF программно на C#",
    "alternativeHeadline": "Как переместить страницы PDF с помощью .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, перемещение страницы pdf",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Попробуйте переместить страницы в желаемое место или в конец файла PDF с помощью Aspose.PDF для .NET."
}
</script>

## Перемещение страницы из одного PDF-документа в другой

Эта тема объясняет, как переместить страницу из одного PDF-документа в конец другого документа с использованием C#.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Для перемещения страницы необходимо:

1. Создать объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с исходным PDF-файлом.
1. Создать объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с целевым PDF-файлом.
1. Получить страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Добавить](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) страницу в целевой документ.
1. Сохранить итоговый PDF с использованием метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Удалить](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) страницу в исходном документе.
1.
1.

Следующий фрагмент кода показывает, как переместить одну страницу.

```csharp
var srcFileName = "<введите имя файла>";
var dstFileName = "<введите имя файла>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// Сохраните выходной файл
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## Перемещение группы страниц из одного PDF-документа в другой

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с исходным PDF-файлом.
1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с целевым PDF-файлом.
1. Определите массив с номерами страниц для перемещения.
1. Выполните цикл по массиву:
    1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Сохраните выходной PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Удалите](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) страницу в исходном документе, используя массив.
1. Сохраните исходный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Показанный ниже пример кода демонстрирует, как переместить несколько страниц из одного PDF-документа в другой.

```csharp
var srcFileName = "<введите имя файла>";
var dstFileName = "<введите имя файла>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// Сохраните выходные файлы
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## Перемещение страницы на новую позицию в текущем PDF-документе

1.
1.
1. Получите страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Добавьте](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) страницу на новое место (например, в конец).
1. [Удалите](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) страницу с предыдущего места.
1. Сохраните полученный PDF файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<введите имя файла>";
var dstFileName = "<введите имя файла>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Сохраните выходной файл
srcDocument.Save(dstFileName);
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


