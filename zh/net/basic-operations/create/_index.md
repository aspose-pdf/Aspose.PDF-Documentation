---
title: 以编程方式创建 PDF 文档
linktitle: 创建 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/create-document/
description: 本页面描述了如何使用 Aspose.PDF 库从头开始创建 PDF 文档。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "Aspose.PDF for .NET 中的新功能允许开发人员使用 C# 和 VB.NET 以编程方式创建 PDF 文档，简化了 WinForms 和 ASP.NET 等各种 .NET 应用程序的过程。通过简单的方法添加页面和文本，用户可以轻松地从头生成自定义 PDF 文件，增强其应用程序功能和用户体验。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

Aspose.PDF for .NET API 允许您使用 C# 和 VB.NET 创建和读取 PDF 文件。该 API 可用于多种 .NET 应用程序，包括 WinForms、ASP.NET 等。在本文中，我们将展示如何使用 Aspose.PDF for .NET API 在 .NET 应用程序中轻松生成和读取 PDF 文件。

## 如何使用 C# 创建 PDF 文件

要使用 C# 创建 PDF 文件，可以使用以下步骤。

1. 创建 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 类的对象。
1. 向 Document 对象的 [Pages](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/properties/pages) 集合中添加一个 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象。
1. 向页面的 [Paragraphs](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page/properties/paragraphs) 集合中添加 [TextFragment](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/textfragment)。
1. 保存生成的 PDF 文档。

下一个代码片段也适用于 [Aspose.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

在这种情况下，我们创建一个 A4 页面大小、纵向方向的单页 PDF 文档。我们的页面将在左上角包含“Hello, World”。