---
title: 程序化地保存 PDF 文档
linktitle: 保存 PDF
type: docs
weight: 30
url: zh/python-net/save-pdf-document/
description: 学习如何在 Python Aspose.PDF for Python via .NET 库中保存 PDF 文件。将 PDF 文档保存到文件系统、流和 Web 应用程序中。
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 将 PDF 文档保存到文件系统

您可以使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法将创建或操作的 PDF 文档保存到文件系统。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # 进行一些操作，例如添加新空白页
    document.pages.add()
    document.save(output_pdf)
```

## 将 PDF 文档保存到流

您也可以通过使用 `Save` 方法的重载将创建或操作的 PDF 文档保存到流。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # 进行一些操作，例如添加新空白页
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## 保存为 PDF/A 或 PDF/X 格式

PDF/A 是一种 ISO 标准化的便携文档格式 (PDF) 版本，用于电子文档的归档和长期保存。 PDF/A 与 PDF 的不同之处在于，它禁止不适合长期归档的功能，例如字体链接（与字体嵌入相对）和加密。 ISO 对 PDF/A 查看器的要求包括颜色管理指南、嵌入字体支持以及用于读取嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的一个子集。 PDF/X 的目的是促进图形交换，因此它具有一系列不适用于标准 PDF 文件的打印相关要求。

在这两种情况下，使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法来存储文档，而文档必须使用 [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法进行准备。

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```