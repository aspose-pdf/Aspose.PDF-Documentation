---
title: 在 .NET 中将 PDF 转换为 Microsoft Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: 学习如何编写 C# 代码将 PDF 转换为 Microsoft Word 格式，以及如何调整 PDF 到 DOC(DOCX) 的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概览

本文介绍了如何**使用 C# 将 PDF 转换为 Microsoft Word 文档**。它涵盖了以下主题。

_格式_: **DOC**

- [C# PDF 到 DOC](#csharp-pdf-to-doc)
- [C# 将 PDF 转换为 DOC](#csharp-pdf-to-doc)
- [C# 如何将 PDF 文件转换为 DOC](#csharp-pdf-to-doc)

_格式_: **DOCX**

- [C# PDF 到 DOCX](#csharp-pdf-to-docx)
- [C# 将 PDF 转换为 DOCX](#csharp-pdf-to-docx)
- [C# 如何将 PDF 文件转换为 DOCX](#csharp-pdf-to-docx)

_格式_: **Word**

- [C# PDF 到 Word](#csharp-pdf-to-docx)
- [C# 将 PDF 转换为 Word](#csharp-pdf-to-doc)
- [C# 如何将 PDF 文件转换为 Word](#csharp-pdf-to-docx)

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。
以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## PDF 转 DOC 和 DOCX 转换

最受欢迎的功能之一是 PDF 转 Microsoft Word DOC 转换，这使内容管理更加轻松。**Aspose.PDF for .NET** 允许您快速高效地将 PDF 文件转换为 DOC 和 DOCX 格式。

## 将 PDF 转换为 DOC (Microsoft Word 97-2003) 文件

轻松将 PDF 文件转换为 DOC 格式，并完全控制。Aspose.PDF for .NET 灵活并支持多种转换。例如，将 PDF 文档的页面转换为图像是一个非常受欢迎的功能。

许多客户要求从 PDF 转换为 DOC：将 PDF 文件转换为 Microsoft Word 文档。客户之所以需要这样做，是因为 PDF 文件不易编辑，而 Word 文档可以。一些公司希望其用户能够在最初为 PDF 的文件中操作文本、表格和图像。

保持简单易懂的传统，Aspose.PDF for .NET 允许您仅用两行代码就将源 PDF 文件转换为 DOC 文件。
保持简单易懂的传统，Aspose.PDF for .NET 让您只需两行代码即可将源 PDF 文件转换为 DOC 文件。

以下 C# 代码片段展示了如何将 PDF 文件转换为 DOC 格式。

<a name="csharp-pdf-to-doc"><strong>步骤：在 C# 中将 PDF 转换为 DOC</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 对象的实例。
2. 通过调用 **Document.Save()** 方法将其保存为 **SaveFormat.Doc** 格式。

```csharp
public static void ConvertPDFtoWord()
{
    // 打开源 PDF 文档
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // 将文件保存为 MS 文档格式
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### 使用 DocSaveOptions 类

[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 类提供了许多属性，这些属性有助于改进 PDF 文件到 DOC 格式的转换。
[`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) 类提供了许多属性，这些属性有助于将 PDF 文件转换为 DOC 格式。

- [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 模式速度快，且能够很好地保留 PDF 文件的原始外观，但生成文档的可编辑性可能会受到限制。原始 PDF 中每个视觉上分组的文本块都会在输出文档中转换为文本框。这样可以最大限度地保持与原始文件的相似性，因此输出文档看起来不错，但它完全由文本框组成，在 Microsoft Word 中编辑这些文本框可能相当具有挑战性。
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 是完全识别模式，其中引擎执行分组和多级分析，以便按照作者的意图恢复原始文档，同时生成易于编辑的文档。
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) 是完全识别模式，引擎在此模式下执行分组和多级分析，以恢复原始文件按照作者意图，同时生成易于编辑的文档。

- [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) 属性用于控制文本元素之间的相对接近度。这意味着距离通过字体大小进行规范化。较大的字体可能在音节之间有更大的空间，但仍被视为一个整体。它以字体大小的百分比指定；例如，1 = 100%。这意味着放置在12pt距离的两个12pt字符是接近的。
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) 用于在转换过程中开启项目符号识别。

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // 设置识别模式为 Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // 设置水平接近度为 2.5
        RelativeHorizontalProximity = 2.5f,
        // 在转换过程中启用识别项目符号的值
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试探索其功能和工作质量。

[![转换 PDF 为 DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOCX（Microsoft Word 2007-2021）文件

Aspose.PDF for .NET API 允许您使用 C# 和任何 .NET 语言读取并转换 PDF 文档为 DOCX。DOCX 是 Microsoft Word 文档的著名格式，其结构已从纯二进制更改为 XML 和二进制文件的组合。Docx 文件可以用 Word 2007 及更高版本打开，但无法用更早版本的 MS Word 打开，这些早期版本支持 DOC 文件扩展名。

以下 C# 代码片段显示了如何将 PDF 文件转换为 DOCX 格式。

<a name="csharp-pdf-to-docx"><strong>步骤：在 C# 中将 PDF 转换为 DOCX</strong></a>

1.
1.
2. 将其保存为 **SaveFormat.DocX** 格式，通过调用 **Document.Save()** 方法。

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // 打开源PDF文档
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // 保存结果DOC文件
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### 以增强模式转换PDF为DOCX

要获得更好的PDF到DOCX转换结果，您可以使用 `EnhancedFlow` 模式。
Flow和Enhanced Flow之间的主要区别是表格（有边框和无边框的）被识别为真正的表格，而不是背景中带图片的文本。
还包括对编号列表和许多其他小事项的识别。

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // 打开源PDF文档
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // 实例化DocSaveOptions对象
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // 指定输出格式为DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // 设置其他DocSaveOptions参数
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // 以docx格式保存文档
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for .NET 为您提供在线免费应用程序 ["PDF 到 Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试探索它的功能和工作质量。

[![Aspose.PDF 转换 PDF 到 Word 免费应用](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 另请参阅

本文还涵盖了以下主题。代码与上面相同。

_格式_: **Word**

- [C# PDF 到 Word 代码](#csharp-pdf-to-docx)
- [C# PDF 到 Word API](#csharp-pdf-to-docx)
- [C# PDF 到 Word 编程方式](#csharp-pdf-to-docx)
- [C# PDF 到 Word 库](#csharp-pdf-to-docx)
- [C# 保存 PDF 为 Word](#csharp-pdf-to-docx)
- [C# 从 PDF 生成 Word](#csharp-pdf-to-docx)
- [C# 从 PDF 创建 Word](#csharp-pdf-to-docx)
- [C# PDF 到 Word 转换器](#csharp-pdf-to-docx)

_格式_: **DOC**

- [C# PDF 到 DOC 代码](#csharp-pdf-to-doc)
- [C# PDF 到 DOC API](#csharp-pdf-to-doc)
- [C# PDF 转 DOC API](#csharp-pdf-to-doc)
- [C# PDF 转 DOC 编程方式](#csharp-pdf-to-doc)
- [C# PDF 转 DOC 库](#csharp-pdf-to-doc)
- [C# 将 PDF 保存为 DOC](#csharp-pdf-to-doc)
- [C# 从 PDF 生成 DOC](#csharp-pdf-to-doc)
- [C# 从 PDF 创建 DOC](#csharp-pdf-to-doc)
- [C# PDF 转 DOC 转换器](#csharp-pdf-to-doc)

_格式_: **DOCX**

- [C# PDF 转 DOCX 代码](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX API](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX 编程方式](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX 库](#csharp-pdf-to-docx)
- [C# 将 PDF 保存为 DOCX](#csharp-pdf-to-docx)
- [C# 从 PDF 生成 DOCX](#csharp-pdf-to-docx)
- [C# 从 PDF 创建 DOCX](#csharp-pdf-to-docx)
- [C# PDF 转 DOCX 转换器](#csharp-pdf-to-docx)
