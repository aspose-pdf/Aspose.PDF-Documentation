---
title: Расширяемая платформа метаданных - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/working-with-extensible-metadata-platform-xmp/
description: В этом разделе объясняется, как работать с Расширяемой платформой метаданных - XMP с использованием класса PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "Функциональность Расширяемой платформы метаданных (XMP) в Aspose.PDF for .NET позволяет пользователям эффективно встраивать и манипулировать стандартизированными и собственными метаданными в PDF-файлах. Используя класс PdfXmpMetadata, эта функция упрощает процесс отслеживания изменений и улучшения семантических возможностей PDF-документов, что делает ее ценным инструментом для разработчиков, стремящихся интегрировать продвинутое управление метаданными.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Расширяемая платформа метаданных (XMP) — это стандарт, созданный компанией Adobe Systems Inc. Этот стандарт был разработан для обработки и хранения стандартизированных и собственных метаданных. Эти метаданные могут быть встроены в различные форматы файлов, но в этой статье мы сосредоточимся только на формате PDF. Мы увидим, как мы можем встроить метаданные в PDF-файл, используя пространство имен Aspose.Pdf.Facades в Aspose.PDF for .NET. Мы будем использовать класс [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) для манипуляции XMP в PDF-документе.

{{% /alert %}}

## Фон

PDF-файл проходит через множество этапов в течение своего жизненного цикла. Мы создаем PDF-документ, а затем передаем его другим людям или отделам для дальнейшей обработки. Однако в процессе нам необходимо отслеживать различные аспекты внесенных изменений. XMP служит этой цели, позволяя отслеживать изменения или другую информацию о данных в файле.

## Объяснение

Для манипуляции XMP с использованием Aspose.Pdf.Facades мы будем использовать класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). Мы будем использовать этот класс для манипуляции предопределенными свойствами метаданных. Класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) добавляет эти свойства в PDF-файл. Он также помогает открывать и сохранять PDF-файлы, в которые мы добавляем метаданные. Таким образом, используя класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), мы можем легко манипулировать XMP в PDF-файле.
Следующий фрагмент кода поможет вам понять, как использовать класс [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) для работы с XMP:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## Заключение

{{% alert color="primary" %}}
В этой статье мы увидели, как мы можем работать с XMP, используя Aspose.Pdf.Facades. Класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class), использованный в этой статье, делает очень простым для пользователя манипулирование метаданными в PDF-документе. Если класс [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) используется правильно, будет очень легко внедрить интеллект в PDF-файлы и приблизить семантическую сеть к реализации.
{{% /alert %}}