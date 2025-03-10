---
title: Конвертация XML в формат FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/converting-an-xml-to-fdf-format/
description: Этот раздел объясняет, как вы можете конвертировать XML в формат FDF с помощью FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "Эта функция позволяет разработчикам без проблем конвертировать XML файлы в формат FDF с использованием класса FormDataConverter в Aspose.PDF for .NET. Эта функциональность улучшает обмен данными между форматами документов, облегчая эффективное управление данными форм в приложениях.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но также справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Пространство имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF for .NET](/pdf/ru/net/) очень хорошо поддерживает AcroForms. Оно также поддерживает импорт и экспорт данных форм в различные форматы файлов, такие как FDF, XFDF и XML. Однако иногда разработчику необходимо конвертировать один формат в другой. В этой статье мы рассмотрим функцию, которая позволяет нам конвертировать формат FDF в XML.

{{% /alert %}}

## Подробности реализации

FDF означает формат данных форм, и файл FDF содержит значения форм в паре ключ/значение. Мы также знаем, что файл XML содержит значения в виде тегов. При этом ключ в основном представлен как имя тега, а значение — как значение внутри этого тега. Теперь [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) предоставляет гибкость для конвертации формата файла XML в формат FDF.

Используйте класс [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) для этой цели. Этот класс предоставляет различные методы для конвертации одного формата данных в другой. Эта статья показывает, как использовать один метод, ConvertXmlToFdf(..), который принимает файл FDF в качестве входного или исходного потока и сохраняет его в формате XML. Следующий фрагмент кода показывает, как конвертировать файл FDF в файл XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```