---
title: Добавление вложения в PDF-документ
linktitle: Добавление вложения в PDF-документ
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-attachment-to-pdf-document/
description: На этой странице описывается, как добавить вложение в PDF-файл с помощью библиотеки Aspose.PDF для .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Attachment to a PDF document",
    "alternativeHeadline": "Easily Attach Files to Your PDF Documents",
    "abstract": "Aspose.PDF для .NET теперь предлагает эффективный способ улучшить ваши PDF-документы, позволяя пользователям легко добавлять различные вложения, включая текстовые файлы и изображения. Эта функция упрощает процесс встраивания дополнительной информации в PDF, обеспечивая быстрый доступ к важным данным в ваших документах. Оптимизируйте управление документами с помощью этой мощной функции и улучшите взаимодействие с пользователем, храня все необходимые ресурсы вместе.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Adding attachments to PDF, PDF file types, Aspose.PDF for .NET, FileSpecification object, Document object, EmbeddedFiles collection, PDF document manipulation, C# PDF library, PDF attachment functionality, Aspose.Drawing integration",
    "wordcount": "309",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Эта страница описывает, как добавить вложение к PDF-файлу с помощью библиотеки Aspose.PDF для .NET."
}
</script>

Вложения могут содержать широкий спектр информации и быть различных типов файлов. В этой статье объясняется, как добавить вложение в PDF-файл.

Следующий фрагмент кода также работает с библиотекой [Aspose.Drawing](/pdf/net/drawing/).

1. Создайте новый проект на C#.
1. Добавьте ссылку на DLL Aspose.PDF.
1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) с добавляемым файлом и описанием файла.
1. Добавьте объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) в коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с помощью метода Add коллекции.

Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) содержит все вложения в файле PDF. Следующий фрагмент кода показывает, как добавить вложение в документ PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddEmbeddedFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"))
    {
        // Setup new file to be added as attachment
        Aspose.Pdf.FileSpecification fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "test.txt", "Sample text file");

        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);

        // Save PDF document
        document.Save(dataDir + "AddAnnotations_out.pdf");
    }
}
```

<!-- 8048395784 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "издательство": {
        "@type": "Организация",
        "название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternativeName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "контактные точки": [
            {
                "@type": "Контактная точка",
                "телефон": "+1 903 306 1676",
                "тип контакта": "sales",
                "обслуживаемая территория": "США",
                "availableLanguage": "en"
            },
            {
                "@type": "Контактная точка",
                "телефон": "+44 141 628 8900",
                "тип контакта": "sales",
                "обслуживаемая территория": "Великобритания",
                "availableLanguage": "en"
            },
            {
                "@type": "Контактная точка",
                "телефон": "+61 2 8006 6987",
                "тип контакта": "sales",
                "обслуживаемая территория": "Австралия",
                "availableLanguage": "en"
            }
        ]
    },
    "предложения": {
        "@type": "Предложение",
        "цена": "1199",
        "валюта цены": "USD"
    },
    "категория приложения": "Библиотека управления PDF-файлами для .NET",
    "URL загрузки": "https://www.nuget.org/packages/Aspose.PDF/",
    "операционная система": "Windows, MacOS, Linux",
    "снимок экрана": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "версия программного обеспечения": "2022.1",
    "совокупный рейтинг": {
        "@type
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