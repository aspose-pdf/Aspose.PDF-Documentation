---
title: 将 XML 转换为 FDF 格式
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/converting-an-xml-to-fdf-format/
description: 本节解释了如何使用 FormDataConverter 将 XML 转换为 FDF 格式。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "该功能允许开发人员使用 Aspose.PDF for .NET 中的 FormDataConverter 类无缝地将 XML 文件转换为 FDF 格式。此功能增强了文档格式之间的数据交换，促进了应用程序中表单数据的高效管理。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades) 命名空间在 [Aspose.PDF for .NET](/pdf/zh/net/) 中对 AcroForms 的支持非常好。它还支持将表单数据导入和导出到不同的文件格式，如 FDF、XFDF 和 XML。然而，有时开发人员需要将一种格式转换为另一种格式。在本文中，我们将探讨允许我们将 FDF 格式转换为 XML 的功能。

{{% /alert %}}

## 实现细节

FDF 代表表单数据格式，FDF 文件包含以键/值对形式的表单值。我们还知道 XML 文件以标签的形式包含值。在这里，通常键表示为标签名称，值表示为该标签内的值。现在，[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades) 提供了将 XML 文件格式转换为 FDF 格式的灵活性。

为此，请使用 [FormDataConverter](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/FormDataConverter) 类。该类提供了将一种数据格式转换为另一种格式的不同方法。本文展示了如何使用一个方法 ConvertXmlToFdf(..)，该方法将 FDF 文件作为输入或源流，并将其保存为 XML 格式。以下代码片段展示了如何将 FDF 文件转换为 XML 文件。

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