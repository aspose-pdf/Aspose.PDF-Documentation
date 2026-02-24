---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /zh/python-net/open-pdf-document/
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 库打开 PDF 文件。您可以打开现有 PDF、从流中打开文档以及加密的 PDF 文档。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF 库在 Python 中打开 PDF 文档
Abstract: 本文提供了在 Python 中使用 Aspose.PDF 库打开现有 PDF 文档的指南。它概述了实现此目标的三种方法——通过指定文件名打开 PDF、从流中打开 PDF，以及通过提供密码打开加密的 PDF。每种方法都包括一个代码片段，演示如何利用 Aspose.PDF 库访问 PDF 并打印其页数。这些示例展示了 Aspose.PDF 在处理各种 PDF 文件访问场景时的灵活性和功能。
---

## 打开现有 PDF 文档

打开文档有几种方法。最简单的是指定文件名。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## 从流中打开现有 PDF 文档

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## 打开加密的 PDF 文档

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```

