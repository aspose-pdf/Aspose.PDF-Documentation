---
title: 从PDF中提取上标和下标文本
linktitle: 提取上标和下标
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/extract-superscripts-subscripts-from-pdf/
description: 本文描述了使用Aspose.PDF在C#中从PDF中提取上标和下标文本的各种方法。
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "使用Aspose.PDF for .NET库从PDF文档中提取上标和下标文本的新功能使用户能够准确检索技术文档中发现的专业文本格式。此增强功能通过为开发人员提供轻松操作这些文本元素的工具，简化了处理数学表达式和化学规格的过程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 提取上标和下标文本

从PDF文档中提取文本是一件常见的事情。然而，在提取的文本中，**上标和下标**可能不会显示，这在技术文档和文章中是典型的。下标或上标是放置在常规文本行下方或上方的字符、数字或字母。它通常比其余文本小。

**下标和上标**最常用于公式、数学表达式和化合物的规格。当同一段文本中可能有许多下标和上标时，编辑它们是非常困难的。
在最新的一个版本中，**Aspose.PDF for .NET**库增加了从PDF中提取上标和下标文本的支持。

使用**TextFragmentAbsorber**类，您可以对找到的文本进行任何操作，即您可以简单地使用整个文本。尝试下一个代码片段：

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

或者单独使用**TextFragments**，对它们进行各种操作，例如按坐标或大小排序。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```