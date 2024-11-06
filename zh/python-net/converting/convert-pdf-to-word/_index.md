---
title: 将PDF转换为Microsoft Word文档在Python中
linktitle: 将PDF转换为Word 2003/2019
type: docs
weight: 10
url: zh/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: 学习如何使用Aspose.PDF for Python via .NET编写PDF到Microsoft Word格式转换的Python代码，并调优PDF到DOC(DOCX)的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何**使用Python将PDF转换为Microsoft Word文档**。它涵盖了以下主题。

_格式_: **DOC**
- [Python PDF到DOC](#python-pdf-to-doc)
- [Python 将PDF转换为DOC](#python-pdf-to-doc)
- [Python 如何将PDF文件转换为DOC](#python-pdf-to-doc)

_格式_: **DOCX**
- [Python PDF到DOCX](#python-pdf-to-docx)
- [Python 将PDF转换为DOCX](#python-pdf-to-docx)
- [Python 如何将PDF文件转换为DOCX](#python-pdf-to-docx)

_格式_: **Word**
- [Python PDF到Word](#python-pdf-to-docx)
- [Python 将PDF转换为Word](#python-pdf-to-doc)

- [Python 如何将PDF文件转换为Word](#python-pdf-to-docx)

## Python PDF 到 DOC 和 DOCX 转换

最受欢迎的功能之一是 PDF 到 Microsoft Word DOC 的转换，这使得内容管理更加容易。**Aspose.PDF for Python** 允许您不仅将 PDF 文件转换为 DOC，还可以轻松高效地转换为 DOCX 格式。

## 将 PDF 转换为 DOC（Word 97-2003）文件

轻松且完全控制地将 PDF 文件转换为 DOC 格式。Aspose.PDF for Python 是灵活的，并支持多种转换。例如，将 PDF 文档的页面转换为图像是一个非常受欢迎的功能。

许多客户请求的一种转换是 PDF 到 DOC：将 PDF 文件转换为 Microsoft Word 文档。客户希望这样做是因为 PDF 文件不容易编辑，而 Word 文档可以。一些公司希望他们的用户能够操作那些最初为 PDF 的文件中的文本、表格和图像。

延续简化和易于理解的传统，Aspose.PDF for Python 允许您用两行代码将源 PDF 文件转换为 DOC 文件。
 为了实现此功能，我们引入了一个名为 SaveFormat 的枚举，其值 .Doc 允许将源文件保存为 Microsoft Word 格式。

以下 Python 代码片段展示了将 PDF 文件转换为 DOC 格式的过程。

<a name="csharp-pdf-to-doc"><strong>步骤：在 Python 中将 PDF 转换为 DOC</strong></a>

1. 使用源 PDF 文档创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。
2. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法将其保存为 [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) 格式。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)
    # 将文件保存为 MS Word 文档格式
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### 使用 DocSaveOptions 类

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类提供了许多属性，这些属性改进了将 PDF 文件转换为 DOC 格式的过程。 在这些属性中，Mode 允许您指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任何值。每个值都有特定的优点和限制：

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # 设置识别模式为 Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 设置水平接近度为 2.5
    save_options.relative_horizontal_proximity = 2.5
    # 启用在转换过程中识别项目符号的功能
    save_options.recognize_bullets = True

    # 将文件保存为 MS Word 文档格式
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试研究其功能和工作质量。
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Python API 通过 .NET 允许您读取和转换 PDF 文档为 DOCX。DOCX 是一种众所周知的 Microsoft Word 文档格式，其结构从纯二进制更改为 XML 和二进制文件的组合。Docx 文件可以用 Word 2007 及更高版本打开，但不能用支持 DOC 文件扩展名的早期版本的 MS Word 打开。

以下 Python 代码片段展示了将 PDF 文件转换为 DOCX 格式的过程。

<a name="csharp-pdf-to-docx"><strong>步骤：在 Python 中将 PDF 转换为 DOCX</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的实例。

2. 通过调用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法将其保存为 [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) 格式。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # 设置识别模式为 Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 设置水平接近度为 2.5
    save_options.relative_horizontal_proximity = 2.5
    # 在转换过程中启用识别项目符号的功能
    save_options.recognize_bullets = True

    # 将文件保存为 MS Word 文档格式
    document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类具有一个名为 Format 的属性，该属性提供了指定结果文档格式的功能，即 DOC 或 DOCX。
 为了将PDF文件转换为DOCX格式，请从DocSaveOptions.DocFormat枚举中传递Docx值。

{{% alert color="warning" %}}
**尝试在线将PDF转换为DOCX**

Aspose.PDF for Python为您提供在线免费应用程序["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 免费应用程序 PDF 转 Word](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 另请参阅

本文还涵盖了这些主题。代码与上述相同。

_格式_：**Word**
- [Python PDF 转 Word 代码](#python-pdf-to-docx)
- [Python PDF 转 Word API](#python-pdf-to-docx)
- [Python PDF 转 Word 编程](#python-pdf-to-docx)
- [Python PDF 转 Word 库](#python-pdf-to-docx)
- [Python 将PDF保存为Word](#python-pdf-to-docx)
- [Python 从PDF生成Word](#python-pdf-to-docx)
- [Python 从PDF创建Word](#python-pdf-to-docx)

- [Python PDF 转 Word 转换器](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF 转 DOC 代码](#python-pdf-to-doc)
- [Python PDF 转 DOC API](#python-pdf-to-doc)
- [Python PDF 转 DOC 编程](#python-pdf-to-doc)
- [Python PDF 转 DOC 库](#python-pdf-to-doc)
- [Python 将 PDF 保存为 DOC](#python-pdf-to-doc)
- [Python 从 PDF 生成 DOC](#python-pdf-to-doc)
- [Python 从 PDF 创建 DOC](#python-pdf-to-doc)
- [Python PDF 转 DOC 转换器](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF 转 DOCX 代码](#python-pdf-to-docx)
- [Python PDF 转 DOCX API](#python-pdf-to-docx)
- [Python PDF 转 DOCX 编程](#python-pdf-to-docx)
- [Python PDF 转 DOCX 库](#python-pdf-to-docx)
- [Python 将 PDF 保存为 DOCX](#python-pdf-to-docx)
- [Python 从 PDF 生成 DOCX](#python-pdf-to-docx)
- [Python 从 PDF 创建 DOCX](#python-pdf-to-docx)
- [Python PDF 转 DOCX 转换器](#python-pdf-to-docx)