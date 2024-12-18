---
title: Добавление страниц в PDF-документ
linktitle: Добавление страниц
type: docs
weight: 10
url: /ru/net/add-pages/
description: Эта статья научит вас вставлять (добавлять) страницу в нужное место PDF-файла. Узнайте, как перемещать, удалять (удалять) страницы из PDF-файла с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление страниц в PDF с помощью C#",
    "alternativeHeadline": "Как добавить страницы в документ PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, добавить страницу pdf, вставить страницу pdf",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья научит вас вставлять (добавлять) страницу в нужное место PDF-файла. Узнайте, как перемещать, удалять (удалять) страницы из PDF-файла с помощью C#."
}
</script>
```
Aspose.PDF для .NET API предоставляет полную гибкость для работы со страницами в документе PDF с использованием C# или любого другого языка .NET. Он управляет всеми страницами документа PDF в [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), которое можно использовать для работы со страницами PDF.
Aspose.PDF для .NET позволяет вставлять страницу в документ PDF в любом месте файла, а также добавлять страницы в конец файла PDF.
Этот раздел показывает, как добавить страницы в PDF с использованием C#.

## Добавить или вставить страницу в файл PDF

Aspose.PDF для .NET позволяет вставлять страницу в документ PDF в любом месте файла, а также добавлять страницы в конец файла PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

### Вставить пустую страницу в файл PDF в желаемом месте

Чтобы вставить пустую страницу в файл PDF:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с входным файлом PDF.
1.
1.
1. Сохраните выходной PDF-файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода показывает, как вставить страницу в PDF-файл.

```cs
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Открыть документ
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// Вставить пустую страницу в PDF
pdfDocument.Pages.Insert(2);
// Сохранить выходной файл
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

В приведенном выше примере мы добавили пустую страницу со стандартными параметрами. Если вам необходимо сделать размер страницы таким же, как у другой страницы в документе, вам следует добавить
несколько строк кода:

```cs
var page = pdfDocument.Pages.Insert(2);
//копирование параметров страницы с первой страницы
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### Добавление пустой страницы в конец файла PDF

Иногда требуется, чтобы документ завершался на пустой странице. Эта тема объясняет, как вставить пустую страницу в конец документа PDF.

Для вставки пустой страницы в конец файла PDF:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с входным файлом PDF.
1. Вызовите метод [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), без параметров.
1. Сохраните итоговый PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода показывает, как вставить пустую страницу в конец файла PDF.

```cs
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Открыть документ
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Вставка пустой страницы в конец файла PDF
pdfDocument.Pages.Add();

// Сохранить выходной файл
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
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
    "applicationCategory": "Библиотека манипуляции PDF для .NET",
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

