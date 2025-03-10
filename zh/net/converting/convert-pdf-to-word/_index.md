---
title: 在 .NET 中将 PDF 转换为 Microsoft Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: 了解如何编写 C# 代码以将 PDF 转换为 Microsoft Word 格式，并调整 PDF 转换为 DOC(DOCX)。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET 引入了一项强大的功能，可以使用 C# 将 PDF 文件转换为 Microsoft Word 格式 (DOC 和 DOCX)。此功能不仅增强了文档编辑，还提供了灵活的文本识别和格式选项，确保源 PDF 与生成的 Word 文档之间的高保真度。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1495",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 概述

本文解释了如何 **使用 C# 将 PDF 转换为 Microsoft Word 文档**。它涵盖了以下主题。

_格式_: **DOC**

- [C# PDF 转 DOC](#csharp-pdf-to-doc)
- [C# 将 PDF 转换为 DOC](#csharp-pdf-to-doc)
- [C# 如何将 PDF 文件转换为 DOC](#csharp-pdf-to-doc)

_格式_: **DOCX**

- [C# PDF 转 DOCX](#csharp-pdf-to-docx)
- [C# 将 PDF 转换为 DOCX](#csharp-pdf-to-docx)
- [C# 如何将 PDF 文件转换为 DOCX](#csharp-pdf-to-docx)

_格式_: **Word**

- [C# PDF 转 Word](#csharp-pdf-to-docx)
- [C# 将 PDF 转换为 Word](#csharp-pdf-to-doc)
- [C# 如何将 PDF 文件转换为 Word](#csharp-pdf-to-docx)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## PDF 转 DOC 和 DOCX 转换

最受欢迎的功能之一是 PDF 转 Microsoft Word DOC 转换，这使内容管理变得更加轻松。**Aspose.PDF for .NET** 允许您快速高效地将 PDF 文件转换为 DOC 和 DOCX 格式。

## 将 PDF 转换为 DOC (Microsoft Word 97-2003) 文件

轻松且完全控制地将 PDF 文件转换为 DOC 格式。Aspose.PDF for .NET 灵活且支持多种转换。例如，将 PDF 文档的页面转换为图像是一个非常受欢迎的功能。

我们的许多客户请求将 PDF 转换为 DOC：将 PDF 文件转换为 Microsoft Word 文档。客户希望这样做是因为 PDF 文件不易于编辑，而 Word 文档则可以。一些公司希望其用户能够在以 PDF 开始的文件中操作文本、表格和图像。

延续简化和易于理解的传统，Aspose.PDF for .NET 让您只需两行代码即可将源 PDF 文件转换为 DOC 文件。为了实现此功能，我们引入了一个名为 SaveFormat 的枚举，其值 .Doc 允许您将源文件保存为 Microsoft Word 格式。

以下 C# 代码片段展示了如何将 PDF 文件转换为 DOC 格式。

<a name="csharp-pdf-to-doc"><strong>步骤：在 C# 中将 PDF 转换为 DOC</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象的实例，使用源 PDF 文档。
2. 通过调用 **Document.Save()** 方法将其保存为 **SaveFormat.Doc** 格式。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### 使用 DocSaveOptions 类

[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 类提供了许多属性，可以改善将 PDF 文件转换为 DOC 格式的效果。在这些属性中，Mode 使您能够指定 PDF 内容的识别模式。您可以为此属性选择 RecognitionMode 枚举中的任何值。每个值都有特定的优点和限制：

- [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 模式速度快，适合保留 PDF 文件的原始外观，但生成文档的可编辑性可能有限。原始 PDF 中的每个视觉分组文本块都转换为输出文档中的文本框。这实现了与原始文档的最大相似性，因此输出文档看起来不错，但完全由文本框组成，这在 Microsoft Word 中编辑起来相当困难。
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 是完全识别模式，引擎执行分组和多级分析，以根据作者的意图恢复原始文档，同时生成易于编辑的文档。限制是输出文档可能与原始文档看起来不同。

[`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) 属性可用于控制文本元素之间的相对接近度。这意味着距离是以字体大小为标准的。较大的字体可能在音节之间有更大的间距，但仍被视为一个整体。它以字体大小的百分比表示；例如，1 = 100%。这意味着两个 12pt 的字符相距 12 pt 是接近的。
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) 用于在转换过程中开启项目符号识别。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试探索其功能和工作质量。

[![将 PDF 转换为 DOC](/pdf/zh/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOCX (Microsoft Word 2007-2024) 文件

Aspose.PDF for .NET API 允许您使用 C# 和任何 .NET 语言读取和转换 PDF 文档为 DOCX。DOCX 是 Microsoft Word 文档的知名格式，其结构从简单的二进制文件更改为 XML 和二进制文件的组合。Docx 文件可以在 Word 2007 及更高版本中打开，但不能在早期版本的 MS Word 中打开，后者支持 DOC 文件扩展名。

以下 C# 代码片段展示了如何将 PDF 文件转换为 DOCX 格式。

<a name="csharp-pdf-to-docx"><strong>步骤：在 C# 中将 PDF 转换为 DOCX</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象的实例，使用源 PDF 文档。
2. 通过调用 **Document.Save()** 方法将其保存为 **SaveFormat.DocX** 格式。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### 在增强模式下将 PDF 转换为 DOCX

为了获得更好的 PDF 转 DOCX 转换结果，您可以使用 `EnhancedFlow` 模式。
Flow 和 Enhanced Flow 之间的主要区别在于表格（无论是否带边框）被识别为真实表格，而不是带有背景图片的文本。
还可以识别编号列表和许多其他小细节。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试探索其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 Word 免费应用](/pdf/zh/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 另请参阅

本文还涵盖了以下主题。代码与上述相同。

_格式_: **Word**

- [C# PDF 转 Word 代码](#csharp-pdf-to-docx)
- [C# PDF 转 Word API](#csharp-pdf-to-docx)
- [C# 程序化 PDF 转 Word](#csharp-pdf-to-docx)
- [C# PDF 转 Word 库](#csharp-pdf-to-docx)
- [C# 将 PDF 保存为 Word](#csharp-pdf-to-docx)
- [C# 从 PDF 生成 Word](#csharp-pdf-to-docx)
- [C# 从 PDF 创建 Word](#csharp-pdf-to-docx)
- [C# PDF 转 Word 转换器](#csharp-pdf-to-docx)

_格式_: **DOC**

- [C# PDF 转 DOC 代码](#csharp-pdf-to-doc)
- [C# PDF 转 DOC API](#csharp-pdf-to-doc)
- [C# 程序化 PDF 转 DOC](#csharp-pdf-to-doc)
- [C# PDF 转 DOC 库](#csharp-pdf-to-doc)
- [C# 将 PDF 保存为 DOC](#csharp-pdf-to-doc)
- [C# 从 PDF 生成 DOC](#csharp-pdf-to-doc)
- [C# 从 PDF 创建 DOC](#csharp-pdf-to-doc)
- [C# PDF 转 DOC 转换器](#csharp-pdf-to-doc)

_格式_: **DOCX**

- [C# PDF 转 DOCX 代码](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX API](#csharp-pdf-to-docx)
- [C# 程序化 PDF 转 DOCX](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX 库](#csharp-pdf-to-docx)
- [C# 将 PDF 保存为 DOCX](#csharp-pdf-to-docx)
- [C# 从 PDF 生成 DOCX](#csharp-pdf-to-docx)
- [C# 从 PDF 创建 DOCX](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX 转换器](#csharp-pdf-to-docx)