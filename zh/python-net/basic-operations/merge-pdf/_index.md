---
title: 在 Python 中合并 PDF 文件
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /zh/python-net/merge-pdf/
description: 了解如何在 Python 中将多个 PDF 文件合并为单个文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 合并 PDF 页面
Abstract: 本文讨论了将多个 PDF 文件合并为单个文档的常见需求，这一过程对于组织、优化存储和共享 PDF 内容非常有价值。文章探讨了使用 Aspose.PDF for Python via .NET 高效合并 PDF 文件，并指出在没有第三方库的情况下，Python 中合并 PDF 可能具有挑战性。本文提供了逐步指南来串联 PDF 文件——创建新文档、合并文件以及保存合并后的文档。代码片段演示了使用 Aspose.PDF 实现的方式，突出该库简化合并过程的能力。此外，文章还介绍了 Aspose.PDF Merger，这是一款用于合并 PDF 的在线工具，使用户能够在基于 Web 的环境中体验其功能。
---

## 使用 Python 和 DOM 合并 PDF 文件

合并两个 PDF 文件：

1. 创建一个新文档。
1. 合并 PDF 文件
1. 保存合并文档

将多个 PDF 文档合并为单个文件：

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## 实时示例

[Aspose.PDF 合并器](https://products.aspose.app/pdf/merger) 是一个免费在线网络应用程序，允许您调查演示合并功能的工作原理。

[![Aspose.PDF 合并器](merger.png)](https://products.aspose.app/pdf/merger)

