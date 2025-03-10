---
title: 在 C# 中处理 PDF 页面
linktitle: 处理页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/working-with-pages/
description: 如何添加页面、添加页眉和页脚、添加水印，您可以在本节中了解。Aspose.PDF for .NET 为您解释此主题的所有细节。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "发现 Aspose.PDF for .NET 在管理 PDF 页面方面的高级功能，包括精确添加、移动和删除页面。此功能使用户能够通过直观的 C# 代码增强其 PDF 文档，加入页眉、页脚、水印和自定义页面大小。通过无缝的 PDF 操作和自定义功能优化您的文档工作流程",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "如何添加页面、添加页眉和页脚、添加水印，您可以在本节中了解。Aspose.PDF for .NET 为您解释此主题的所有细节。"
}
</script>

**Aspose.PDF for .NET** 允许您在文件的任何位置向 PDF 文档插入页面，以及将页面添加到 PDF 文件的末尾。本节展示了如何在没有 Acrobat Reader 的情况下向 PDF 添加页面。
您可以在 PDF 文件的页眉和页脚中添加文本或图像，并通过 Aspose 的 C# 库选择文档中的不同页眉。
此外，尝试使用 C# 程序化裁剪 PDF 文档中的页面。

本节教您如何使用 Artifact 类在 PDF 文件中添加水印。您将检查此任务的编程示例。
使用 PageNumberStamp 类添加页码。要在文档中添加印章，请使用 ImageStamp 和 TextStamp 类。使用添加水印功能在 PDF 文件中创建背景图像，使用 **Aspose.PDF for .NET**。

您可以执行以下操作：

- [添加页面](/pdf/net/add-pages/) - 在所需位置或 PDF 文件末尾添加页面，并从文档中删除页面。
- [移动页面](/pdf/net/move-pages/) - 将页面从一个文档移动到另一个文档。
- [删除页面](/pdf/net/delete-pages/) - 使用 PageCollection 集合从 PDF 文件中删除页面。
- [更改页面大小](/pdf/net/change-page-size/) - 您可以使用 Aspose.PDF 库的代码片段更改 PDF 页面大小。
- [旋转页面](/pdf/net/rotate-pages/) - 您可以更改现有 PDF 文件中页面的方向。
- [拆分页面](/pdf/net/split-document/) - 您可以将 PDF 文件拆分为一个或多个 PDF。
- [添加页眉和/或页脚](/pdf/net/add-headers-and-footers-of-pdf-file/) - 在 PDF 文件的页眉和页脚中添加文本或图像。
- [裁剪页面](/pdf/net/crop-pages/) - 您可以使用不同的页面属性以编程方式裁剪 PDF 文档中的页面。
- [添加水印](/pdf/net/add-watermarks/) - 使用 Artifact 类在 PDF 文件中添加水印。
- [在 PDF 文件中添加页码](/pdf/net/add-page-number/) - PageNumberStamp 类将帮助您在 PDF 文件中添加页码。
- [添加背景](/pdf/net/add-backgrounds/) - 背景图像可用于添加水印。
- [印章](/pdf/net/stamping/) - 您可以使用 ImageStamp 类向 PDF 文件添加图像印章，使用 TextStamp 类添加文本。

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