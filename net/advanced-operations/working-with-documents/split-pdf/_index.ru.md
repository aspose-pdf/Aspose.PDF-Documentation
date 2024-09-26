---
title: Разделение PDF программно
linktitle: Разделение файлов PDF
type: docs
weight: 60
url: /net/split-pdf-document/
keywords: разделение pdf на несколько файлов, разделение pdf на отдельные pdf, разделение pdf c#
description: Эта тема показывает, как разделить страницы PDF на отдельные файлы PDF в ваших .NET приложениях на C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Разделение PDF программно",
    "alternativeHeadline": "Как разделить PDF с помощью .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, разделение pdf",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта тема показывает, как разделить страницы PDF на отдельные файлы PDF в ваших .NET приложениях на C#."
}
</script>
## Пример в реальном времени

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) - это бесплатное веб-приложение, которое позволяет вам исследовать, как работает функциональность разделения презентаций.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Эта тема показывает, как разделить страницы PDF на отдельные файлы PDF в ваших .NET приложениях. Чтобы разделить страницы PDF на отдельные файлы PDF с использованием C#, можно следовать следующим шагам:

1. Перебирать страницы документа PDF через коллекцию [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Для каждой итерации создать новый объект Document и добавить в него отдельный объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Сохранить новый PDF с использованием метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Разделение PDF на несколько файлов или отдельные pdf в C#

Следующий фрагмент кода на C# показывает, как разделить страницы PDF на отдельные файлы PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// Цикл по всем страницам
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```

