---
title: Как объединить PDF с помощью C#
linktitle: Объединение файлов PDF
type: docs
weight: 50
url: /ru/net/merge-pdf-documents/
description: Эта страница объясняет, как объединить PDF-документы в один PDF-файл с помощью C# или VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Как объединить PDF с помощью C#",
    "alternativeHeadline": "Объединение PDF-документов",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "манипулирование документами PDF",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта страница объясняет, как объединить PDF-документы в один PDF-файл с помощью C# или VB.NET."
}
</script>

## Объединение нескольких PDF в один PDF на C#

Объединение PDF-файлов на C# не является простой задачей без использования сторонней библиотеки.
Эта статья показывает, как объединить несколько PDF-файлов в один PDF-документ с использованием Aspose.PDF для .NET. Пример написан на C#, но API может быть использовано и в других языках программирования .NET, таких как VB.NET. PDF-файлы объединяются таким образом, что первый присоединяется к концу другого документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Объединение PDF-файлов с использованием C# и DOM

Для конкатенации двух PDF-файлов:

1. Создайте два объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), каждый из которых содержит один из входных PDF-файлов.
1. Затем вызовите метод Add коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) для объекта Document, к которому вы хотите добавить другой PDF-файл.
1.
1.
1. Наконец, сохраните выходной файл PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Ниже приведен фрагмент кода, показывающий, как объединить PDF файлы.

```csharp
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Открыть первый документ
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// Открыть второй документ
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// Добавить страницы второго документа к первому
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// Сохранить результат объединения в выходном файле
pdfDocument1.Save(dataDir);
```

## Пример в действии

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) - это бесплатное онлайн-приложение, которое позволяет вам исследовать функциональность объединения презентаций.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Смотрите также

- [Разделение PDF с использованием DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Разделить PDF с использованием DOM](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Объединить PDF документы с использованием Facades](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Разделить PDF с использованием Facades](https://docs.aspose.com/pdf/net/split-pdf-pages/)

