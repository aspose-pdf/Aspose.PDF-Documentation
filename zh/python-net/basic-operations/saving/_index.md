---
title: 以编程方式保存 PDF 文档
linktitle: 保存 PDF
type: docs
weight: 30
url: /zh/python-net/save-pdf-document/
description: 了解如何使用 Aspose.PDF for Python via .NET 库在 Python 中保存 PDF 文件。将 PDF 文档保存到文件系统、流以及 Web 应用程序中。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF 库在 Python 中保存 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中保存 PDF 文档的指导。它概述了保存 PDF 的三种主要方法——保存到文件系统、保存到流以及保存为 PDF/A 或 PDF/X 等特定格式。`Document` 类的 `save()` 方法是这些操作的核心。要将 PDF 保存到文件系统，可以创建或操作文档，例如添加新页面，然后直接保存到路径。对于保存到流，`Save` 方法的重载允许将文档写入流对象。此外，本文还解释了如何将文档保存为 PDF/A 或 PDF/X 格式，这些分别是长期存档和图形交换的标准。此过程需要在保存之前使用 `convert` 方法准备文档。提供的 Python 代码片段演示了每种方法，展示了这些方法的实际应用。
---

## 将 PDF 文档保存到文件系统

您可以使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法，将创建或修改的 PDF 文档保存到文件系统。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## 将 PDF 文档保存到流

您也可以通过使用 `Save` 方法的重载，将创建或修改的 PDF 文档保存到流中。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## 保存 PDF/A 或 PDF/X 格式

PDF/A 是一种符合 ISO 标准的可移植文档格式（PDF）版本，用于电子文档的归档和长期保存。
PDF/A 与 PDF 的区别在于它禁止不适合长期归档的功能，例如字体链接（而非字体嵌入）和加密。ISO 对 PDF/A 查看器的要求包括颜色管理指南、嵌入式字体支持以及用于读取嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的一个子集。PDF/X 的目的在于促进图形交换，因此它包含一系列不适用于标准 PDF 文件的印刷相关要求。

在这两种情况下，都使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存文档，而文档必须使用 [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法进行准备。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

