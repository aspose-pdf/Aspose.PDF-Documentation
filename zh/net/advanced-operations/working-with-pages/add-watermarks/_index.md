---
title: 使用 C# 向 PDF 添加水印
linktitle: 添加水印
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /zh/net/add-watermarks/
description: 本文解释了使用 C# 程序化处理文档和获取 PDF 中水印的功能。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-existing-watermarks/
    - /net/adding-multi-line-watermark-to-existing-pdf/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add watermark to PDF using C#",
    "alternativeHeadline": "Add Custom Watermarks to PDF with C#",
    "abstract": "Aspose.PDF for .NET 中的新功能允许开发人员使用 Artifact 功能以编程方式向 PDF 文档添加可自定义的水印。此功能通过支持各种文档属性（包括类型、不透明度、旋转和文本自定义）来增强文档管理，使用户能够轻松创建专业且可识别的 PDF 文件。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "462",
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
    "url": "/net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-watermarks/"
    },
    "dateModified": "2024-11-26",
    "description": "本文解释了使用 C# 程序化处理文档和获取 PDF 中水印的功能。"
}
</script>

**Aspose.PDF for .NET** 允许使用 Artifacts 向您的 PDF 文档添加水印。请查看本文以解决您的任务。

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库一起使用。

使用 Adobe Acrobat 创建的水印称为工件（如 PDF 规范中的 14.8.2.2 真实内容和工件所述）。为了处理工件，Aspose.PDF 有两个类：[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 和 [ArtifactCollection](https://reference.aspose.com/pdf/net/aspose.pdf/artifactcollection)。

为了获取特定页面上的所有工件，[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 类具有 Artifacts 属性。此主题解释了如何在 PDF 文件中处理工件。

## 处理工件

[Artifact](https://reference.aspose.com/pdf/net/aspose.pdf/artifact) 类包含以下属性：

- **Artifact.Type**：获取工件类型（支持 Artifact.ArtifactType 枚举的值，其中包括背景、布局、页面、分页和未定义）。
- **Artifact.Subtype**：获取工件子类型（支持 Artifact.ArtifactSubtype 枚举的值，其中包括背景、页脚、页眉、未定义、水印）。

{{% alert color="primary" %}}

请注意，使用 Adobe Acrobat 创建的水印的类型为分页，子类型为水印。

{{% /alert %}}

- **Artifact.Contents**：获取工件内部操作符的集合。其支持类型为 System.Collections.ICollection。
- **Artifact.Form**：获取工件的 XForm（如果使用了 XForm）。水印、页眉和页脚工件包含显示所有工件内容的 XForm。
- **Artifact.Image**：获取工件的图像（如果存在图像，否则为 null）。
- **Artifact.Text**：获取工件的文本。
- **Artifact.Rectangle**：获取工件在页面上的位置。
- **Artifact.Rotation**：获取工件的旋转（以度为单位，正值表示逆时针旋转）。
- **Artifact.Opacity**：获取工件的不透明度。可能的值范围为 0…1，其中 1 表示完全不透明。

## 如何在 PDF 文件上添加水印

以下代码片段演示了如何使用 C# 获取 PDF 文件第一页上的每个水印。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddWatermarks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddWatermarksInput.pdf"))
    {
        // Create a new watermark artifact
        var artifact = new Aspose.Pdf.WatermarkArtifact();
        artifact.SetTextAndState(
            "WATERMARK",
            new Aspose.Pdf.Text.TextState()
            {
                FontSize = 72,
                ForegroundColor = Aspose.Pdf.Color.Blue,
                Font = Aspose.Pdf.Text.FontRepository.FindFont("Courier")
            });
        // Set watermark properties
        artifact.ArtifactHorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        artifact.ArtifactVerticalAlignment = Aspose.Pdf.VerticalAlignment.Center;
        artifact.Rotation = 45;
        artifact.Opacity = 0.5;
        artifact.IsBackground = true;
        // Add watermark artifact to the first page
        document.Pages[1].Artifacts.Add(artifact);
        // Save PDF document
        document.Save(dataDir + "AddWatermarks_out.pdf");
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