---
title: Преобразование FDF в формат XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/converting-an-fdf-to-xml-format/
description: В этом разделе объясняется, как можно преобразовать FDF в формат XML с помощью класса FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Узнайте, как эффективно конвертировать файлы FDF в формат XML с помощью класса FormDataConverter в Aspose.PDF для .NET. Эта функция упрощает обработку данных, преобразуя пары «ключ-значение» из FDF в легко читаемую структуру XML, улучшая взаимодействие и управление данными в ваших приложениях",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}

Пространство имён Aspose.Pdf.Facades (https://reference.aspose.com/pdf/net/aspose.pdf.facades) в [Aspose.PDF for .NET](/pdf/net/) очень хорошо поддерживает AcroForms. Оно также поддерживает импорт и экспорт данных форм в различные форматы файлов, такие как FDF, XFDF и XML. Однако иногда разработчикам может потребоваться преобразовать один формат в другой. В этой статье рассматривается функция преобразования FDF в XML.

{{% /alert %}}

## Детали реализации

FDF означает формат данных форм, а файл FDF содержит значения формы в виде пары «ключ/значение». Мы также знаем, что файл XML содержит значения в виде тегов. Где в основном ключ представлен как имя тега, а значение представлено как значение внутри этого тега. Теперь Aspose.Pdf.Facades предоставляет нам возможность преобразовывать формат файла FDF в формат XML.

Мы можем использовать класс FormDataConverter (https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) для этой цели. Этот класс предоставляет нам различные методы для преобразования одного формата данных в другой формат. В этой статье мы будем использовать только один метод под названием ConvertFdfToXml (https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Этот метод принимает файл FDF в качестве входных данных или исходного потока и сохраняет его в формате XML.

Следующий фрагмент кода показывает, как преобразовать файл FDF в файл XML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```