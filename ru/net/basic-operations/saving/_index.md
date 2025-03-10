---
title: Сохранение PDF-документа программным способом
linktitle: Сохранить PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ru/net/save-pdf-document/
description: Узнайте, как сохранить PDF-файл в библиотеке C# Aspose.PDF for .NET. Сохраняйте PDF-документ в файловой системе, в потоке и в веб-приложениях.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "Узнайте, как разработчики с лёгкостью программно сохраняют PDF-документы с помощью Aspose.PDF для .NET. Эта функция поддерживает сохранение PDF-файлов в файловую систему, потоки и непосредственно в веб-приложениях, адаптируясь к различным сценариям использования и обеспечивая соответствие стандартам PDF/A и PDF/X для долгосрочного архивирования и обмена графикой. Оптимизируйте свои возможности работы с PDF-файлами с помощью этого надёжного механизма сохранения",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.Drawing](/pdf/net/drawing/).

## Сохранение PDF-документа в файловую систему

Вы можете сохранить созданный или обработанный PDF-документ в файловой системе с помощью метода `Save` класса `Document`.
Если вы не укажете тип формата (параметры), то документ будет сохранён в формате Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## Сохранение PDF-документа в поток

Также можно сохранить созданный или обработанный PDF-документ в поток с помощью перегрузок методов `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

Для более подробного объяснения перейдите в раздел [Showcase](/pdf/net/showcases/).

## Сохранение в формате PDF/A или PDF/X

PDF/A — это версия Portable Document Format (PDF), стандартизированная ISO, предназначенная для использования при архивировании и долгосрочном хранении электронных документов.
PDF/A отличается от PDF тем, что запрещает функции, не подходящие для долгосрочного хранения, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO к просмотрщикам PDF/A включают рекомендации по управлению цветом, поддержку встроенных шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X является подмножеством стандарта ISO для PDF. Цель PDF/X — облегчить обмен графикой, поэтому он содержит ряд требований, связанных с печатью, которые не применяются к стандартным файлам PDF.

В обоих случаях для хранения документов используется метод `Save`, а документы должны быть подготовлены с помощью метода `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```