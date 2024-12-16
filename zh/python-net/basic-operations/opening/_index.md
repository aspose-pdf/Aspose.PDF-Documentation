---
title: 以编程方式打开PDF文档
linktitle: 打开PDF
type: docs
weight: 20
url: /zh/python-net/open-pdf-document/
description: 了解如何在Python Aspose.PDF for Python via .NET库中打开PDF文件。您可以打开现有的PDF、从流中打开文档以及加密的PDF文档。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 打开现有的PDF文档

有几种方法可以打开文档。最简单的是指定文件名。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## 从流中打开现有的PDF文档

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # 打开文档
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## 打开加密的PDF文档

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```