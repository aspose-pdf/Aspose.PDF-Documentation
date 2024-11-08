---
title: 以编程方式打开 PDF 文档
linktitle: 打开 PDF
type: docs
weight: 20
url: /zh/python-cpp/open-pdf-document/
description: 学习如何在 Python Aspose.PDF for Python via C++ 库中打开 PDF 文件。您可以打开现有 PDF、来自流的文档和加密的 PDF 文档。
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 打开现有的 PDF 文档

有几种方法可以打开文档。最简单的是指定文件名。

```python

    import AsposePDFPythonWrappers as ap
    # 打开文档
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("页数: " + str(count))
```

## 打开加密的 PDF 文档

```python

    import AsposePDFPythonWrappers as ap
    # 打开文档
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("页数: " + str(count))
```