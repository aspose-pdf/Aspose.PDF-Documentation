---
title: 以编程方式保存 PDF 文档
linktitle: 保存 PDF
type: docs
weight: 30
url: /zh/python-net/save-pdf-document/
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 库保存 PDF 文件。将 PDF 文档保存到文件系统、流以及 Web 应用程序中。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF 库在 Python 中保存 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中保存 PDF 文档的指南。它概述了保存 PDF 的三种主要方法——保存到文件系统、保存到流以及保存为特定格式，如 PDF/A 或 PDF/X。`save()` 方法是 `Document` 类的核心操作。要将 PDF 保存到文件系统，可以创建或操作文档，例如添加新页面，然后直接保存到路径。对于保存到流，`Save` 方法的重载允许将文档写入流对象。此外，本文解释了如何将文档保存为 PDF/A 或 PDF/X 格式，这些分别是长期归档和图形交换的标准。此过程需要在保存之前使用 `convert` 方法准备文档。提供的 Python 代码示例演示了每种方法，展示了这些方法的实际应用。
---

## 保存 PDF 文档到文件系统

您可以使用 将创建或操作的 PDF 文档保存到文件系统 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## 将 PDF 文档保存到流

您还可以通过使用重载，将创建或处理后的 PDF 文档保存到流中 `Save` 方法。

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## 保存 PDF/A 或 PDF/X 格式

您可以轻松地将文档保存为特定的 PDF 版本，例如 PDF/A 或 PDF/X。在这种情况下，我们需要在保存文档之前调用 convert 方法。

PDF/A 是一种经 ISO 标准化的便携文档格式（PDF）版本，用于归档和长期保存电子文档。
PDF/A 与 PDF 的区别在于它禁止不适合长期归档的功能，例如字体链接（相对于字体嵌入）和加密。ISO 对 PDF/A 查看器的要求包括颜色管理指南、嵌入字体支持以及用于读取嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的子集。PDF/X 的目的是促进图形交换，因此它具有一系列不适用于标准 PDF 文件的印刷相关要求。

在这两种情况下， [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 此方法用于存储文档，而文档必须使用 [转换](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
