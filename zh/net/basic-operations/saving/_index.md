---
title: 以编程方式保存 PDF 文档
linktitle: 保存 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/save-pdf-document/
description: 了解如何在 C# Aspose.PDF for .NET PDF 库中保存 PDF 文件。将 PDF 文档保存到文件系统、流和 Web 应用程序中。
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "发现开发人员如何轻松地以编程方式保存 PDF 文档，使用 Aspose.PDF for .NET。此功能支持将 PDF 保存到文件系统、流以及直接在 Web 应用程序中，适应各种用例，同时确保符合 PDF/A 和 PDF/X 标准，以便进行长期归档和图形交换。通过这种强大的保存机制优化您的 PDF 处理能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

下一个代码片段也适用于 [Aspose.Drawing](/pdf/net/drawing/) 库。

## 将 PDF 文档保存到文件系统

您可以使用 `Document` 类的 `Save` 方法将创建或操作的 PDF 文档保存到文件系统中。
当您不提供格式类型（选项）时，文档将以 Aspose.PDF v.1.7 (*.pdf) 格式保存。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## 将 PDF 文档保存到流

您还可以通过使用 `Save` 方法的重载将创建或操作的 PDF 文档保存到流中。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

有关更详细的说明，请访问 [Showcase](/pdf/net/showcases/) 部分。

## 保存 PDF/A 或 PDF/X 格式

PDF/A 是便携式文档格式（PDF）的 ISO 标准化版本，用于归档和长期保存电子文档。
PDF/A 与 PDF 的不同之处在于它禁止不适合长期归档的特性，例如字体链接（与字体嵌入相对）和加密。PDF/A 查看器的 ISO 要求包括颜色管理指南、嵌入字体支持和用于阅读嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的一个子集。PDF/X 的目的是促进图形交换，因此它有一系列与打印相关的要求，这些要求不适用于标准 PDF 文件。

在这两种情况下，使用 `Save` 方法来存储文档，而文档必须使用 `Convert` 方法进行准备。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```