---
title: 使用 Python 将 PDF 转换为 Microsoft Word 文档
linktitle: 将 PDF 转换为 Word 2003/2019
type: docs
weight: 10
url: zh/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: 学习如何使用 Aspose.PDF 通过 .NET 将 PDF 转换为 Microsoft Word 格式的 Python 代码，并优化 PDF 到 DOC(DOCX) 的转换。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概述

本文解释了如何使用 Python **将 PDF 转换为 Microsoft Word 文档**。它涵盖了以下主题。

_格式_: **DOC**
- [Python PDF 转 DOC](#python-pdf-to-doc)
- [Python 转换 PDF 为 DOC](#python-pdf-to-doc)
- [Python 如何将 PDF 文件转换为 DOC](#python-pdf-to-doc)

_格式_: **DOCX**
- [Python PDF 转 DOCX](#python-pdf-to-docx)
- [Python 转换 PDF 为 DOCX](#python-pdf-to-docx)
- [Python 如何将 PDF 文件转换为 DOCX](#python-pdf-to-docx)

_格式_: **Word**
- [Python PDF 转 Word](#python-pdf-to-docx)
- [Python 转换 PDF 为 Word](#python-pdf-to-doc)

- [Python 如何将 PDF 文件转换为 Word](#python-pdf-to-docx)

## Python PDF 到 DOC 和 DOCX 转换

其中一个最受欢迎的功能是 PDF 到 Microsoft Word DOC 转换，这使得内容管理更加容易。**Aspose.PDF for Python** 允许您不仅将 PDF 文件转换为 DOC，还可以轻松高效地转换为 DOCX 格式。

## 将 PDF 转换为 DOC (Word 97-2003) 文件

轻松且完全控制地将 PDF 文件转换为 DOC 格式。Aspose.PDF for Python 灵活且支持多种转换。例如，将 PDF 文档页面转换为图像是一个非常受欢迎的功能。

许多客户要求的一个转换是 PDF 到 DOC：将 PDF 文件转换为 Microsoft Word 文档。客户希望这样做是因为 PDF 文件不易编辑，而 Word 文档可以编辑。有些公司希望他们的用户能够操作最初为 PDF 的文件中的文本、表格和图像。

保持简化和易于理解的传统，Aspose.PDF for Python 让您通过两行代码将源 PDF 文件转换为 DOC 文件。
 要实现此功能，我们引入了一个名为 SaveFormat 的枚举，其值 .Doc 允许您将源文件保存为 Microsoft Word 格式。

以下 Python 代码片段展示了将 PDF 文件转换为 DOC 格式的过程。

<a name="csharp-pdf-to-doc"><strong>步骤：在 Python 中将 PDF 转换为 DOC</strong></a>

1. 使用源 PDF 文档创建一个 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 对象的实例。
2. 调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法，将其保存为 [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) 格式。

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### 使用 DocSaveOptions 类

[DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) 类提供了许多属性，可以改善将 PDF 文件转换为 DOC 格式的过程。 在这些属性中，Mode 允许您指定 PDF 内容的识别模式。您可以为此属性指定 RecognitionMode 枚举中的任何值。每个值都有特定的优点和限制：

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# 打开 PDF 文档
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# 设置识别模式为 Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 设置水平接近度为 2.5
save_options.relative_horizontal_proximity = 2.5
# 启用识别项目符号的值，以便在转换过程中识别项目符号
save_options.recognize_bullets = True

# 将文件保存为 MS Word 文档格式
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Python 为您提供了一个免费的在线应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试调查其功能和工作质量。
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Python API 允许您使用 Python 通过 .NET 读取和转换 PDF 文档为 DOCX。DOCX 是 Microsoft Word 文档的一种众所周知的格式，其结构从简单的二进制文件更改为 XML 和二进制文件的组合。Docx 文件可以用 Word 2007 及更高版本打开，但不能用支持 DOC 文件扩展名的早期 MS Word 版本打开。

以下 Python 代码片段显示了将 PDF 文件转换为 DOCX 格式的过程。

<a name="csharp-pdf-to-docx"><strong>步骤：在 Python 中将 PDF 转换为 DOCX</strong></a>

1. 使用源 PDF 文档创建 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 对象的实例。

2. 通过调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法，将其保存为 [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) 格式。

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# 打开 PDF 文档
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# 设置识别模式为 Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 将水平接近度设置为 2.5
save_options.relative_horizontal_proximity = 2.5
# 启用识别项目符号的功能在转换过程中
save_options.recognize_bullets = True

# 将文件保存为 MS Word 文档格式
document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 类有一个名为 Format 的属性，它提供了指定结果文档格式的功能，即 DOC 或 DOCX。
 为了将 PDF 文件转换为 DOCX 格式，请从 DocSaveOptions.DocFormat 枚举中传递 Docx 值。

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Python 为您提供免费的在线应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 另见

本文还涵盖了这些主题。代码与上面相同。

_格式_: **Word**
- [Python PDF 转换为 Word 代码](#python-pdf-to-docx)
- [Python PDF 转换为 Word API](#python-pdf-to-docx)
- [Python 编程方式转换 PDF 为 Word](#python-pdf-to-docx)
- [Python PDF 转换为 Word 库](#python-pdf-to-docx)
- [Python 将 PDF 保存为 Word](#python-pdf-to-docx)
- [Python 从 PDF 生成 Word](#python-pdf-to-docx)
- [Python 从 PDF 创建 Word](#python-pdf-to-docx)

- [Python PDF 转换为 Word 转换器](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF 到 DOC 代码](#python-pdf-to-doc)
- [Python PDF 到 DOC API](#python-pdf-to-doc)
- [Python PDF 到 DOC 编程](#python-pdf-to-doc)
- [Python PDF 到 DOC 库](#python-pdf-to-doc)
- [Python 将 PDF 保存为 DOC](#python-pdf-to-doc)
- [Python 从 PDF 生成 DOC](#python-pdf-to-doc)
- [Python 从 PDF 创建 DOC](#python-pdf-to-doc)
- [Python PDF 到 DOC 转换器](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF 到 DOCX 代码](#python-pdf-to-docx)
- [Python PDF 到 DOCX API](#python-pdf-to-docx)
- [Python PDF 到 DOCX 编程](#python-pdf-to-docx)
- [Python PDF 到 DOCX 库](#python-pdf-to-docx)
- [Python 将 PDF 保存为 DOCX](#python-pdf-to-docx)
- [Python 从 PDF 生成 DOCX](#python-pdf-to-docx)
- [Python 从 PDF 创建 DOCX](#python-pdf-to-docx)
- [Python PDF 到 DOCX 转换器](#python-pdf-to-docx)