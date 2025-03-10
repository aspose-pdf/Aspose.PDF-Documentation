---
title: Создание PDF-документа программным способом
linktitle: Создать PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/create-document/
description: На этой странице описывается, как создать PDF-документ с нуля с помощью библиотеки Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "Новая функция в Aspose.PDF для .NET позволяет разработчикам программно создавать PDF-документы с помощью C# и VB.NET, оптимизируя процесс для различных приложений .NET, таких как WinForms и ASP.NET. С помощью простых методов добавления страниц и текста пользователи могут легко генерировать пользовательские PDF-файлы с нуля, улучшая функциональность своих приложений и пользовательский опыт",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

API Aspose.PDF for .NET позволяет создавать и читать PDF-файлы с помощью C# и VB.NET. API можно использовать в различных .NET-приложениях, включая WinForms, ASP.NET и другие. В этой статье мы покажем, как использовать API Aspose.PDF for .NET для простого создания и чтения PDF-файлов в .NET-приложениях.

## Как создать PDF-файл с помощью C#

Для создания PDF-файла с помощью C# можно выполнить следующие шаги:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Добавьте объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в коллекцию [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) объекта Document.
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) в коллекцию [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) страницы.
1. Сохраните полученный PDF-документ.

Следующий фрагмент кода также работает с библиотекой [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

В этом случае мы создаём одностраничный PDF-документ с размером страницы A4 и книжной ориентацией. Наша страница будет содержать надпись «Hello, World» в верхней левой части страницы.