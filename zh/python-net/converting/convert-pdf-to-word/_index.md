---
title: 在 Python 中将 PDF 转换为 Word
linktitle: 转换 PDF 为 Word
type: docs
weight: 10
url: /zh/python-net/convert-pdf-to-word/
lastmod: "2026-06-08"
description: 了解如何在 Python 中将 PDF 转换为 Word，包括 PDF 转 DOC、PDF 转 DOCX，以及使用 Aspose.PDF 的高级布局识别。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中将 PDF 转换为 DOC 和 DOCX
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为 Microsoft Word 格式。内容包括 PDF 转 DOC、PDF 转 DOCX，以及用于将 PDF 内容创建可编辑 Word 文档的高级布局识别选项。
---

此页面展示了如何在 Python 中**将 PDF 转换为 Word**。当您需要从 PDF 文件获取可编辑的 DOC 或 DOCX 输出以进行修订、重用或办公文档工作流时，请使用这些示例。

## 在 Python 中将 PDF 转换为 DOC

最受欢迎的功能之一是 PDF 转换为 Microsoft Word DOC，这简化了内容管理。**Aspose.PDF for Python via .NET** 使您能够轻松高效地将 PDF 文件转换为 DOC 以及 DOCX 格式。

当您需要修改文本、在办公工作流中重用内容或将 PDF 内容转移到可编辑的 DOC 或 DOCX 文档时，请使用 Word 转换。

这 [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类提供了众多属性，可提升将 PDF 文件转换为 DOC 格式的过程。在这些属性中，Mode 允许您指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任意值。每个值都有其特定的优势和限制：

步骤：在 Python 中将 PDF 转换为 DOC

1. 将 PDF 加载到 'ap.Document' 对象中。
1. 创建一个 'DocSaveOptions' 实例。
1. 将 format 属性设置为 'DocFormat.DOC'，以确保输出为 .doc 格式（旧版 Word 格式）。
1. 使用指定的保存选项将 PDF 保存为 Word 文档。
1. 打印确认消息。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转换为 DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，在此您可以尝试调查其功能以及其工作质量。

[![将 PDF 转换为 DOC](/pdf/zh/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 在 Python 中将 PDF 转换为 DOCX

Aspose.PDF for Python API 可让您使用基于 .NET 的 Python 读取并将 PDF 文档转换为 DOCX。DOCX 是一种广为人知的 Microsoft Word 文档格式，其结构已从纯二进制更改为 XML 与二进制文件的组合。Docx 文件可以在 Word 2007 及其后续版本中打开，但不能在早期支持 DOC 文件扩展名的 MS Word 版本中打开。

下面的 Python 代码片段展示了将 PDF 文件转换为 DOCX 格式的过程。

步骤：在 Python 中将 PDF 转换为 DOCX

1. 使用 'ap.Document' 加载源 PDF。
1. 创建一个 'DocSaveOptions' 的实例。
1. 将 format 属性设置为 'DocFormat.DOC_X' 以生成 .docx 文件（现代 Word 格式）。
1. 使用已配置的保存选项将 PDF 保存为 DOCX 文件。
1. 在转换后打印确认消息。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## 使用高级布局识别将 PDF 转换为 DOCX

使用 Python 和 Aspose.PDF 将 PDF 文档转换为 DOCX（Word）文件，并使用高级识别设置。它采用增强的流模式来保留文档结构，使输出更易编辑且更接近原始布局。

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

这 [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类具有名为 Format 的属性，可提供指定生成文档格式的功能，即 DOC 或 DOCX。为了将 PDF 文件转换为 DOCX 格式，请从 DocSaveOptions.DocFormat 枚举中传入 Docx 值。

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转 Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 转换 PDF 到 Word 应用](/pdf/zh/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 相关转换

- [将 PDF 转换为 Excel](/pdf/zh/python-net/convert-pdf-to-excel/) 用于面向电子表格的导出。
- [将 PDF 转换为 PowerPoint](/pdf/zh/python-net/convert-pdf-to-powerpoint/) 当您需要演示幻灯片而不是文字处理输出时。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 用于网络出版和基于浏览器的内容工作流。
