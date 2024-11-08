---
title: 将 PDF 转换为 Microsoft Word
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: 使用 Aspose.PDF for PHP 轻松将 PDF 文件转换为 DOC 和 DOCX 格式，并完全控制转换过程。了解更多关于如何调整 PDF 到 Microsoft Word 文档的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何使用 PHP 将 PDF 转换为 Word。代码非常简单，只需将 PDF 加载到 Document 类中并将其保存为输出的 Microsoft Word DOC 或 DOCX 格式。它涵盖了以下主题

- [PHP PDF 转 Word](#convert-pdf-to-doc)
- [PHP PDF 转 DOC](#convert-pdf-to-doc)
- [PHP PDF 转 DOCX](#convert-pdf-to-docx)
- [PHP 转换 PDF 为 Word](#convert-pdf-to-docx)
- [PHP 转换 PDF 为 DOC](#convert-pdf-to-doc)
- [PHP 转换 PDF 为 DOCX](#convert-pdf-to-docx)
- [PHP 如何将 PDF 文件转换为 Word DOC](#convert-pdf-to-doc) 或 [Word DOCX](#convert-pdf-to-docx)

- [PHP PDF 转 Word 库、API 或代码以从 PDF 程序化地保存、生成或创建 Word 文档](#convert-pdf-to-docx)

## 将 PDF 转换为 DOC

最受欢迎的功能之一是 PDF 到 Microsoft Word DOC 的转换，这使得内容易于操作。Aspose.PDF for PHP 允许您将 PDF 文件转换为 DOC。

**Aspose.PDF for PHP** 可以从头开始创建 PDF 文档，是一个用于更新、编辑和操作现有 PDF 文档的优秀工具包。一个重要的功能是能够将页面和整个 PDF 文档转换为图像。另一个受欢迎的功能是 PDF 到 Microsoft Word DOC 的转换，这使得内容易于操作。（大多数用户无法编辑 PDF 文档，但可以轻松在 Microsoft Word 中处理表格、文本和图像。）

为了简化和便于理解，Aspose.PDF for PHP 提供了一个两行代码，将源 PDF 文件转换为 DOC 文件。

以下 Java 代码片段展示了将 PDF 文件转换为 DOC 格式的过程。

1. 使用源 PDF 文档创建一个 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 对象的实例。

2. 通过调用 **Document.save()** 方法将其保存为 **SaveFormat.Doc** 格式。

```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个新的 DocSaveOptions 对象
$saveOption = new DocSaveOptions();

// 设置输出格式为 DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// 将文档保存为 DOC
$document->save($outputFile, $saveOption);
```

## 使用 DocSaveOptions 类

[DocSaveOptions 类](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) 提供了许多属性，可以改善将 PDF 文件转换为 DOC 格式的过程。在这些属性中，Mode 允许您指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任何值。每一个值都有特定的优点和限制：

- [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 模式速度快，并且有助于保留 PDF 文件的原始外观，但生成文档的可编辑性可能受到限制。
 每个在原始 PDF 中视觉上分组的文本块都会在输出文档中转换为文本框。这实现了与原始文档的最大相似性，因此输出文档看起来不错，但它完全由文本框组成，这可能会使在 Microsoft Word 中的编辑变得困难。

- Flow 是一种完整的识别模式，其中引擎执行分组和多级分析，以根据作者的意图恢复原始文档，同时生成一个易于编辑的文档。其限制是输出文档可能看起来与原始文档不同。

- RelativeHorizontalProximity 属性可用于控制文本元素之间的相对接近度，这意味着距离是由字体大小规范的。较大的字体可能在音节之间有更大的距离，仍然被视为一个整体。它被指定为字体大小的百分比，例如，1 = 100%。这意味着两个 12pt 的字符相距 12pt 时是接近的。

- RecognitionBullets 用于在转换过程中打开项目符号识别。
```php
// 加载 PDF 文档
$document = new Document($inputFile);

// 创建一个新的 DocSaveOptions 对象
$saveOption = new DocSaveOptions();

// 将识别模式设置为 EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 将输出格式设置为 DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// 将识别模式设置为 Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// 将水平接近度设置为 2.5
saveOptions->setRelativeHorizontalProximity(2.5f);

// 启用在转换过程中识别项目符号的功能
saveOptions->setRecognizeBullets(true);

// 将文档保存为 DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for PHP 提供了一个免费的在线应用程序["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，在这里您可以尝试研究其功能和质量。

[![将 PDF 转换为 DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOCX

DocFormat 枚举还提供了选择 DOCX 作为 Word 文档输出格式的选项。要将源 PDF 文件渲染为 DOCX 格式，请使用下面指定的代码片段。

## 如何将 PDF 转换为 DOCX

以下 Java 代码片段显示了将 PDF 文件转换为 DOCX 格式的过程。

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 对象的实例。
2. 通过调用 **Document.save()** 方法将其保存为 **SaveFormat.DocX** 格式。

```php
    // 加载 PDF 文档
    $document = new Document($inputFile);
    
    // 将文档保存为 DOCX 格式
    $document->save($outputFile, SaveFormat::$DocX);
```

[DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) 类有一个名为 Format 的属性，该属性提供了指定结果文档格式的功能，即 DOC 或 DOCX。
 为了将 PDF 文件转换为 DOCX 格式，请从 DocSaveOptions.DocFormat 枚举中传递 Docx 值。

请查看以下代码片段，该代码段提供了使用 Java 将 PDF 文件转换为 DOCX 格式的功能。

```php
// 载入 PDF 文档
$document = new Document($inputFile);

// 创建一个新的 DocSaveOptions 对象
$saveOption = new DocSaveOptions();

// 将识别模式设置为 EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// 将输出格式设置为 DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// 将文档保存为 DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**在线尝试将 PDF 转换为 DOCX**

Aspose.PDF for PHP 为您提供在线免费应用程序 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试研究其功能和工作质量。

{{% /alert %}}
