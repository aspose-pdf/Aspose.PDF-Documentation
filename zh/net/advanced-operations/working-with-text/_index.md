---
title: 使用 C# 在 PDF 中处理文本
linktitle: 处理文本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/working-with-text/
description: 本节解释了各种文本处理技术。了解如何使用 Aspose.PDF 和 C# 添加、替换、旋转、搜索文本。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Text in PDF using C#",
    "alternativeHeadline": "Enhanced Text Manipulation Features in PDF with C#",
    "abstract": "发现使用 Aspose.PDF for .NET 在 PDF 中强大的文本操作能力。此功能允许用户无缝地在 PDF 文档中添加、替换、旋转和格式化文本，增强文档的互动性和自定义性。为您的应用程序提供高效的搜索功能和灵活的文本处理技术，专为 C# 开发人员量身定制。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF manipulation, add text to PDF, rotate text in PDF, search text in PDF, replace text in PDF, text formatting inside PDF, Aspose.PDF for .NET, text handling techniques, PDF document generation, Floating Box tool",
    "wordcount": "371",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2024-11-26",
    "description": "本节解释了各种文本处理技术。了解如何使用 Aspose.PDF 和 C# 添加、替换、旋转、搜索文本。"
}
</script>

我们有时需要向 PDF 文件添加文本。例如，当您想在主要文本下方添加翻译、在图像旁边放置标题或仅仅填写申请表时。如果所有文本元素都可以按照您自己的期望样式进行格式化，那也是非常有帮助的。在 PDF 文件中最常见的文本操作是：向 PDF 添加文本、在 PDF 文件中格式化文本、替换和旋转文档中的文本。**Aspose.PDF for .NET** 是与 PDF 内容交互所需的一切的最佳解决方案。

您可以执行以下操作：

- [向 PDF 文件添加文本](/pdf/zh/net/add-text-to-pdf-file/) - 向您的 PDF 添加文本，使用流和文件中的字体，添加 HTML 字符串，添加超链接等。
- [PDF 工具提示](/pdf/zh/net/pdf-tooltip/) - 您可以通过使用 C# 添加一个不可见的按钮来为搜索的文本添加工具提示。
- [PDF 内部文本格式化](/pdf/zh/net/text-formatting-inside-pdf/) - 在格式化文本时，您可以向文档添加许多功能。使用 Aspose.PDF 库添加行缩进、添加文本边框、添加下划线文本、添加换行符。
- [使用浮动框](/pdf/zh/net/floating-box/) - 浮动框工具是一个特殊工具，用于在 PDF 页面上放置文本和其他内容。
- [在 PDF 中替换文本](/pdf/zh/net/replace-text-in-pdf/) - 在 PDF 文档的所有页面中替换文本。您首先需要使用 TextFragmentAbsorber。
- [在 PDF 中旋转文本](/pdf/zh/net/rotate-text-inside-pdf/) - 使用 TextFragment 类的旋转属性在 PDF 中旋转文本。
- [搜索并获取 PDF 文档页面中的文本](/pdf/zh/net/search-and-get-text-from-pdf/) - 您可以使用 TextFragmentAbsorber 类搜索并获取页面中的文本。
- [确定换行](/pdf/zh/net/determine-line-break/) - 本主题解释如何跟踪多行文本片段的换行。

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