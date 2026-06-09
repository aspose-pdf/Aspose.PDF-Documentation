---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /zh/python-net/open-pdf-document/
description: 了解如何使用 Python Aspose.PDF for Python via .NET 库打开 PDF 文件。您可以打开现有的 PDF、来自流的文档以及加密的 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF 库在 Python 中打开 PDF 文档
Abstract: 本文提供了使用 Aspose.PDF 库在 Python 中打开现有 PDF 文档的指南。它概述了三种实现方法——通过指定文件名打开 PDF、从流中打开 PDF，以及通过提供密码打开受密码保护的 PDF。每种方法都包含代码片段，演示如何利用 Aspose.PDF 库访问 PDF 并打印其页数。这些示例展示了 Aspose.PDF 在处理不同 PDF 文件访问场景时的灵活性和功能性。
---

## 打开现有 PDF 文档

打开文档有多种方式。最简单的是指定文件名。

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## 从流打开现有 PDF 文档

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## 打开加密的 PDF 文档

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
