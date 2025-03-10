---
title: 使用 C# 处理 PDF 图层
linktitle: 使用 PDF 图层
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/work-with-pdf-layers/
description: 下一任务解释如何锁定 PDF 图层、提取 PDF 图层元素、扁平化分层 PDF，并将 PDF 中的所有图层合并为一个。
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "体验增强的 PDF 文档管理，使用新的 Aspose.PDF for .NET 功能，允许用户有效地处理 PDF 图层。此功能支持锁定和解锁图层，将元素提取到单独的文件中，扁平化分层内容，并将多个图层合并为一个，从而提供更大的文档可见性和组织控制。释放您的 PDF 文档的潜力，并通过这些强大的工具简化工作流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

PDF 图层允许 PDF 文档包含不同的内容集，可以选择性地查看或隐藏。PDF 中的每个图层可以包括文本、图像或图形，用户可以根据需要切换这些图层的显示状态。图层通常用于需要组织或分隔不同内容的复杂文档。

## 锁定 PDF 图层

使用 Aspose.PDF for .NET，您可以打开 PDF，锁定第一页上的特定图层，并保存带有更改的文档。

自 24.5 版本以来，已实现此功能。

添加了两个新方法和一个属性：

- Layer.Lock(); - 锁定图层。
- Layer.Unlock(); - 解锁图层。
- Layer.Locked; - 属性，指示图层的锁定状态。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## 提取 PDF 图层元素

Aspose.PDF for .NET 库允许从第一页提取每个图层，并将每个图层保存到单独的文件中。

要从图层创建新的 PDF，可以使用以下代码片段：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

24.9 版本对该功能进行了更新。

可以提取 PDF 图层元素并将其保存到新的 PDF 文件流中：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## 扁平化分层 PDF

Aspose.PDF for .NET 库打开 PDF，遍历第一页上的每个图层，并扁平化每个图层，使其在页面上永久存在。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

'Layer.Flatten(bool cleanupContentStream)' 方法接受一个布尔参数，指定是否从内容流中移除可选内容组标记。将 cleanupContentStream 参数设置为 false 可以加快扁平化过程。

## 将 PDF 中的所有图层合并为一个

Aspose.PDF for .NET 库允许将所有 PDF 图层或第一页上的特定图层合并为一个新图层，并保存更新后的文档。

添加了两个方法以合并页面上的所有图层：

- void MergeLayers(string newLayerName)。
- void MergeLayers(string newLayerName, string newOptionalContentGroupId)。

第二个参数允许重命名可选内容组标记。默认值为 "oc1" (/OC /oc1 BDC)。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```