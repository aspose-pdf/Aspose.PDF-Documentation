---
title: 将 PDF 转换为 PowerPoint 在 .NET 中
linktitle: 将 PDF 转换为 PowerPoint
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF 允许您使用 .NET 将 PDF 转换为 PPT（PowerPoint）格式。 一种方法是将 PDF 转换为 PPTX，并将幻灯片作为图像。
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to PowerPoint in .NET",
    "alternativeHeadline": "Convert PDF Documents to PowerPoint Presentations Efficiently in C#",
    "abstract": "Aspose.PDF for .NET 引入了一项强大的功能，使 PDF 文档无缝转换为 PowerPoint (PPTX) 格式，允许每个 PDF 页面转换为一个独立的幻灯片。 通过将文本呈现为可选择的或图像，用户可以轻松自定义他们的演示文稿，同时有效跟踪转换进度。 通过利用这一创新功能来优化您的文档工作流程，以提高生产力",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1174",
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
    "url": "/net/convert-pdf-to-powerpoint/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-powerpoint/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。 请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述

本文解释了如何 **使用 C# 将 PDF 转换为 PowerPoint**。 它涵盖了以下主题。

_格式_: **PPTX**
- [C# PDF 转 PPTX](#csharp-pdf-to-pptx)
- [C# 将 PDF 转换为 PPTX](#csharp-pdf-to-pptx)
- [C# 如何将 PDF 文件转换为 PPTX](#csharp-pdf-to-pptx)

_格式_: **PowerPoint**
- [C# PDF 转 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 将 PDF 转换为 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 如何将 PDF 文件转换为 PowerPoint](#csharp-pdf-to-powerpoint)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## C# PDF 到 PowerPoint 和 PPTX 转换

**Aspose.PDF for .NET** 让您跟踪 PDF 到 PPTX 转换的进度。

我们有一个名为 Aspose.Slides 的 API，它提供创建和操作 PPT/PPTX 演示文稿的功能。 此 API 还提供将 PPT/PPTX 文件转换为 PDF 格式的功能。 最近，我们收到了许多客户的要求，以支持将 PDF 转换为 PPTX 格式的能力。 从 Aspose.PDF for .NET 版本 10.3.0 开始，我们引入了一项将 PDF 文档转换为 PPTX 格式的功能。 在此转换过程中，PDF 文件的各个页面被转换为 PPTX 文件中的单独幻灯片。

在 PDF 到 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> 转换过程中，文本被呈现为文本，您可以选择/更新它。 请注意，为了将 PDF 文件转换为 PPTX 格式，Aspose.PDF 提供了一个名为 [`PptxSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 的类。 PptxSaveOptions 类的对象作为第二个参数传递给 [`Document.Save(..) 方法`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)。 以下代码片段展示了将 PDF 文件转换为 PPTX 格式的过程。

## 使用 C# 和 Aspose.PDF .NET 简单转换 PDF 到 PowerPoint

为了将 PDF 转换为 PPTX，Aspose.PDF for .NET 建议使用以下代码步骤。

<a name="csharp-pdf-to-powerpoint"><strong>步骤：在 C# 中将 PDF 转换为 PowerPoint</strong></a> | <a name="csharp-pdf-to-pptx"><strong>步骤：在 C# 中将 PDF 转换为 PPTX</strong></a>

1. 创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类的实例。
2. 创建 [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 类的实例。
3. 使用 **Document** 对象的 **Save** 方法将 PDF 保存为 PPTX。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTX()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Save the file in PPTX format
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## 将 PDF 转换为 PPTX 并将幻灯片作为图像

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for .NET 向您展示在线免费应用程序 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 PPTX 的免费应用](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

如果您需要将可搜索的 PDF 转换为 PPTX 作为图像而不是可选择的文本，Aspose.PDF 提供了通过 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 类实现此功能。 为此，将 [PptxSaveOptios](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 类的属性 [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) 设置为 'true'，如下所示的代码示例。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithSlidesAsImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions
        {
            SlidesAsImages = true
        };

        // Save the file in PPTX format with slides as images
        document.Save(dataDir + "PDFToPPT_out.pptx", saveOptions);
    }
}
```

## PPTX 转换的进度详细信息

Aspose.PDF for .NET 让您跟踪 PDF 到 PPTX 转换的进度。 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 类提供了 [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) 属性，可以指定为自定义方法以跟踪转换的进度，如以下代码示例所示。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFToPPTWithCustomProgressHandler()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {

        // Instantiate PptxSaveOptions object
        var saveOptions = new Aspose.Pdf.PptxSaveOptions();

        // Specify custom progress handler
        saveOptions.CustomProgressHandler = ShowProgressOnConsole;

        // Save the file in PPTX format with progress tracking
        document.Save(dataDir + "PDFToPPTWithProgressTracking_out.pptx", saveOptions);
    }
}

 // Define the method to handle progress events and display them on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            // Display overall progress of the conversion
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Conversion progress: {eventInfo.Value}%.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            // Display progress of the page layout creation
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} layout created.");
            break;

        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            // Display progress of the page being exported
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Result page {eventInfo.Value} of {eventInfo.MaxValue} exported.");
            break;

        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            // Display progress of the source page analysis
            Console.WriteLine($"{DateTime.Now.TimeOfDay}  - Source page {eventInfo.Value} of {eventInfo.MaxValue} analyzed.");
            break;

        default:
            break;
    }
}
```

## 另请参阅 

本文还涵盖了以下主题。 代码与上述相同。

_格式_: **PowerPoint**
- [C# PDF 转 PowerPoint 代码](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint API](#csharp-pdf-to-powerpoint)
- [C# 以编程方式将 PDF 转 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint 库](#csharp-pdf-to-powerpoint)
- [C# 将 PDF 保存为 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 从 PDF 生成 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# 从 PDF 创建 PowerPoint](#csharp-pdf-to-powerpoint)
- [C# PDF 转 PowerPoint 转换器](#csharp-pdf-to-powerpoint)

_格式_: **PPTX**
- [C# PDF 转 PPTX 代码](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX API](#csharp-pdf-to-pptx)
- [C# 以编程方式将 PDF 转 PPTX](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX 库](#csharp-pdf-to-pptx)
- [C# 将 PDF 保存为 PPTX](#csharp-pdf-to-pptx)
- [C# 从 PDF 生成 PPTX](#csharp-pdf-to-pptx)
- [C# 从 PDF 创建 PPTX](#csharp-pdf-to-pptx)
- [C# PDF 转 PPTX 转换器](#csharp-pdf-to-pptx)