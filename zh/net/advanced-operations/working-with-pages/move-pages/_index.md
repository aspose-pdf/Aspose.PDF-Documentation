---
title: 以编程方式移动 PDF 页面 C#
linktitle: 移动 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/move-pages/
description: 尝试使用 Aspose.PDF for .NET 在所需位置或 PDF 文件末尾移动页面。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET 引入了一项强大的新功能，允许用户以编程方式在文档之间移动 PDF 页面或在同一文档内重新排列它们。此功能通过使开发人员能够在指定位置插入页面并轻松管理页面组织，同时保持文档完整性，增强了 PDF 操作能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "尝试使用 Aspose.PDF for .NET 在所需位置或 PDF 文件末尾移动页面。"
}
</script>

## 从一个 PDF 文档移动页面到另一个 PDF 文档

本主题解释了如何使用 C# 将页面从一个 PDF 文档移动到另一个文档的末尾。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

要移动页面，我们应该：

1. 创建一个包含源 PDF 文件的 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 创建一个包含目标 PDF 文件的 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 集合中获取页面。
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 页面到目标文档。
1. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存输出 PDF。
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) 源文档中的页面。
1. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存源 PDF。

以下代码片段演示了如何移动一个页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## 从一个 PDF 文档移动一组页面到另一个 PDF 文档

1. 创建一个包含源 PDF 文件的 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 创建一个包含目标 PDF 文件的 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 定义一个包含要移动的页面编号的数组。
1. 遍历数组：
    1. 从 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 集合中获取页面。
    1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 页面到目标文档。
1. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存输出 PDF。
1. 使用数组在源文档中 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) 页面。
1. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存源 PDF。

以下代码片段演示了如何将一组页面从一个 PDF 文档移动到另一个 PDF 文档。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## 在当前 PDF 文档中将页面移动到新位置

1. 创建一个包含源 PDF 文件的 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 从 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 集合中获取页面。
1. [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) 页面到新位置（例如到末尾）。
1. [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) 先前位置的页面。
1. 使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存输出 PDF。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
    }
}
```

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