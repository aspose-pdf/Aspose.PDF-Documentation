---
title: 如何使用 C# 合并 PDF
linktitle: 合并 PDF 文件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/merge-pdf-documents/
description: 本页面解释如何使用 C# 或 VB.NET 将 PDF 文档合并为一个单一的 PDF 文件。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Merge PDF using C#",
    "alternativeHeadline": "Combine PDF Effortlessly Using C#",
    "abstract": "发现使用 C# 和 Aspose.PDF 库轻松合并多个 PDF 文档为一个文件的强大功能。此功能使开发人员能够通过高效地合并 PDF 来简化工作流程，在整个过程中保持质量和结构。非常适合软件集成，此功能通过简化文档管理任务来提高生产力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "411",
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
    "url": "/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/merge-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "本页面解释如何使用 C# 或 VB.NET 将 PDF 文档合并为一个单一的 PDF 文件。"
}
</script>

## 在 C# 中合并或组合多个 PDF 为单个 PDF

在 C# 中合并 PDF 不是一项简单的任务，除非使用第三方库。
本文展示了如何使用 Aspose.PDF for .NET 将多个 PDF 文件合并为一个单一的 PDF 文档。示例使用 C# 编写，但该 API 也可以在其他 .NET 编程语言中使用，例如 VB.NET。PDF 文件的合并方式是将第一个文件连接到其他文档的末尾。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 合并 PDF 文件

要连接两个 PDF 文件：

1. 创建两个 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象，每个对象包含一个输入 PDF 文件。
1. 然后调用要添加其他 PDF 文件的 Document 对象的 [PageCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pagecollection) 集合的 Add 方法。
1. 将第二个 Document 对象的 PageCollection 集合传递给第一个 PageCollection 集合的 Add 方法。
1. 最后，使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf.document/save/methods/4) 方法保存输出 PDF 文件。

以下代码片段展示了如何连接 PDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "Concat1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "Concat2.pdf"))
        {
            // Add pages of second document to the first
            document1.Pages.Add(document2.Pages);

            // Save PDF document
            document1.Save(dataDir + "MergeDocuments_out.pdf");
        }
    }
}
```

## 实时示例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) 是一个在线免费网络应用程序，允许您调查演示合并功能的工作原理。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## 另请参见

- [使用 DOM 拆分 PDF](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [使用 Facades 连接 PDF 文档](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [使用 Facades 拆分 PDF](https://docs.aspose.com/pdf/net/split-pdf-pages/)

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