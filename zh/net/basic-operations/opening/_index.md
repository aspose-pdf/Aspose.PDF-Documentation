---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/open-pdf-document/
description: 了解如何在 C# Aspose.PDF for .NET PDF 库中打开 PDF 文件。您可以打开现有 PDF、从流中加载文档以及处理加密的 PDF 文档。
aliases:
    - /net/opening-a-pdf-document/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Open PDF document programmatically",
    "alternativeHeadline": "Programmatically Open and Access Various PDF Documents with C#",
    "abstract": "发现使用 Aspose.PDF for .NET 库打开 PDF 文档。此功能允许开发人员无缝访问现有 PDF，从流中加载文档，并轻松处理加密文件，提高工作流程效率并扩展 C# 中 PDF 操作的能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "238",
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
    "url": "/net/open-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/open-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 打开现有 PDF 文档

打开文档有几种方法。最简单的方法是指定文件名。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## 从流中打开现有 PDF 文档

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentStream()
{
    var fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Create a new WebClient instance
    var webClient = new System.Net.WebClient();
    // Concatenate the domain with the Web resource filename
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## 打开加密的 PDF 文档

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    const string password = "Aspose2020";
    try
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "DocSite.pdf", password))
        {
            Console.WriteLine("Pages " + document.Pages.Count);
        }
    }
    catch (Aspose.Pdf.InvalidPasswordException e)
    {
        Console.WriteLine(e);
    }
}
```