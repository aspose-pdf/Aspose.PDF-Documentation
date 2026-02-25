---
title: 如何使用 Python 合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 50
url: /zh/python-net/merge-pdf-documents/
description: 本页介绍如何使用 Python 将 PDF 文档合并为单个 PDF 文件。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 合并 PDF 页面
Abstract: 本文阐述了将多个 PDF 文件合并为单个文档的常见需求，这一过程对于组织、优化存储以及共享 PDF 内容非常有价值。文章探讨了通过 .NET 使用 Aspose.PDF for Python 高效合并 PDF 文件，并指出在没有第三方库的情况下，Python 中的 PDF 合并可能具有挑战性。本文提供了合并 PDF 文件的分步指南——创建新文档、合并文件以及保存合并后的文档。代码片段展示了使用 Aspose.PDF 实现的示例，突出该库简化合并过程的能力。此外，还介绍了 Aspose.PDF Merger，这是一款在线合并 PDF 的工具，使用户能够在网络环境中体验其功能。
---

## 在 Python 中合并或组合多个 PDF 为单个 PDF

合并 PDF 文件是用户非常常见的需求。当您有多个 PDF 文件想要共享或一起存储为一个文档时，这将非常有用。

合并 PDF 文件可以帮助您整理文档，释放电脑上的存储空间，并通过将多个 PDF 文件合并为一个文档来与他人共享。

在 Python 中通过 .NET 合并 PDF 若不使用第三方库并非易事。
本文展示了如何使用 Aspose.PDF for Python via .NET 将多个 PDF 文件合并为单个 PDF 文档。

## 使用 Python 和 DOM 合并 PDF 文件

将两个 PDF 文件连接起来：

1. 创建一个新文档。
1. 合并 PDF 文件
1. 保存合并后的文档

将多个 PDF 文档合并为单个文件：

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## 实时示例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) 是一个在线免费网页应用程序，允许您了解演示合并功能的工作原理。

[![Aspose.PDF 合并](merger.png)](https://products.aspose.app/pdf/merger)


