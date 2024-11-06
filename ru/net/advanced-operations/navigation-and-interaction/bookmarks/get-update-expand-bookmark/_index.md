---
title: Добавление и удаление закладки
linktitle: Добавление и удаление закладки
type: docs
weight: 10
url: ru/net/add-and-delete-bookmark/
description: Вы можете добавить закладку в документ PDF с помощью C#. Возможно удалить все или определенные закладки из документа PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление и удаление закладки",
    "alternativeHeadline": "Как добавить и удалить закладку из PDF",
    "author": {
        "@type": "Person",
        "name":"Андрий Андруховский",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, удаление закладки, добавление закладки",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете добавить закладку в документ PDF с помощью C#. Возможно удалить все или определенные закладки из документа PDF."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление закладки в документ PDF

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) объекта Document, которая находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Чтобы добавить закладку в PDF:

1. Откройте документ PDF с помощью объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте закладку и определите ее свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в документ PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Открыть документ
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Создать объект закладки
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Тестовая закладка";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Установить номер страницы назначения
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Добавить закладку в коллекцию контуров документа.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Сохранить результат
pdfDocument.Save(dataDir);
```
## Добавление дочерней закладки в PDF-документ

Закладки могут быть вложенными, указывая на иерархическую связь с родительскими и дочерними закладками. В этой статье объясняется, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в файл PDF, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), определив её свойства.
1. Добавьте OutlineItemCollection в коллекцию [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) объекта Document.

Дочерняя закладка создается так же, как родительская, описанная выше, но добавляется в коллекцию Outlines родительской закладки

Следующие примеры кода показывают, как добавить дочернюю закладку в документ PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Открыть документ
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Создать объект родительской закладки
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Родительская закладка";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Создать объект дочерней закладки
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Дочерняя закладка";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Добавить дочернюю закладку в коллекцию родительской закладки
pdfOutline.Add(pdfChildOutline);
// Добавить родительскую закладку в коллекцию закладок документа.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Сохранить результат
pdfDocument.Save(dataDir);
```
## Удаление всех закладок из PDF-документа

Все закладки в PDF содержатся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). В этой статье объясняется, как удалить все закладки из файла PDF.

Для удаления всех закладок из файла PDF:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Сохраните измененный файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Ниже приведены примеры кода, показывающие, как удалить все закладки из PDF-документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Открыть документ
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Удалить все закладки
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Сохранить обновленный файл
pdfDocument.Save(dataDir);
```
## Удаление конкретной закладки из документа PDF

Для удаления конкретной закладки из файла PDF:

1. Передайте название закладки в качестве параметра в метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Затем сохраните обновленный файл с помощью метода Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Метод [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) удаляет любую закладку с переданным в метод названием.

Следующие фрагменты кода показывают, как удалить конкретную закладку из документа PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Открыть документ
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Удалить конкретную закладку по названию
pdfDocument.Outlines.Delete("Child Outline");

// Сохранить обновленный файл
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
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

