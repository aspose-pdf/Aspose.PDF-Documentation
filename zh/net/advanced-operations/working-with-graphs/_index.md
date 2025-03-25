---
title: 在 PDF 文件中使用图形
linktitle: 使用图形
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/working-with-graphs/
description: 本文解释了什么是图形，如何创建填充矩形对象，以及其他功能
lastmod: "2022-02-17"
sitemap:
changefreq: "weekly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "发现使用 Aspose.PDF for .NET 在 PDF 文档中生成和操作图形的强大新功能。此功能允许开发人员创建各种图形形状，包括弧、圆、线和矩形，增强其应用程序中数据的视觉呈现。优化您的 PDF 生成过程，轻松提供动态数据可视化",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "108",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2025-03-17",
    "description": "本文解释了什么是图形，如何创建填充矩形对象，以及其他功能"
}
</script>

## 什么是图形

在 PDF 文档中添加图形是开发人员在使用 Adobe Acrobat Writer 或其他 PDF 处理应用程序时非常常见的任务。PDF 应用程序中可以使用多种类型的图形。
[Aspose.PDF for .NET](/pdf/zh/net/) 也支持向 PDF 文档中添加图形。为此，提供了图形类。图形是段落级元素，可以添加到页面实例的段落集合中。图形实例包含一个形状集合。

以下类型的形状由 [Graph](https://reference.aspose.com/pdf/zh/net/aspose.pdf.drawing/graph) 类支持：

- [弧](/pdf/zh/net/add-arc/) - 有时也称为标志，是一对相邻顶点的有序对，但有时也称为有向线。
- [圆](/pdf/zh/net/add-circle/) - 使用分成扇区的圆来显示数据。我们使用圆形图（也称为饼图）来显示数据如何代表一个整体或一个组的部分。
- [曲线](/pdf/zh/net/add-curve/) - 是一组相连的射影线，每条线在普通双点上与三条其他线相交。
- [线](/pdf/zh/net/add-line) - 线图用于显示连续数据，并且在显示随时间变化的趋势时可以对预测未来事件非常有用。
- [矩形](/pdf/zh/net/add-rectangle/) - 是您在图形中看到的许多基本形状之一，它在帮助您解决问题时非常有用。
- [椭圆](/pdf/zh/net/add-ellipse/) - 是平面上的一组点，形成一个椭圆形的曲线。

以下操作支持形状类型：
- [检查边界](/pdf/zh/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - 检查形状集合中的形状边界。

上述细节也在下面的图中描述：

![图形中的图](graphs.png)

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