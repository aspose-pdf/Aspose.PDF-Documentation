---
title: 通过 Python 提取 PDF 中的字体
linktitle: 提取 PDF 中的字体
type: docs
weight: 30
url: /zh/python-net/extract-fonts-from-pdf/
description: 使用 Aspose.PDF for Python 库从您的 PDF 文档中提取所有嵌入的字体。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 从 PDF 中提取字体
Abstract: 本文说明了如何使用 Aspose.PDF for Python 检查 PDF 文档中使用的字体。它展示了如何使用 Document 类打开 PDF，调用 `font_utilities.get_all_fonts()` 来检索可用的字体对象，并遍历结果以读取字体名称，用于分析、审计或文档处理工作流。
---

使用 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 打开 PDF 并调用 `font_utilities.get_all_fonts()` 检索所有可用的 [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) 文档引用的对象。这在审计嵌入字体、在转换前检查字体可用性或分析文档资源时非常有用。

1. 打开源 PDF 作为 `Document`.
1. 调用 `document.font_utilities.get_all_fonts()` 获取字体集合。
1. 遍历返回的 `Font` 对象。
1. 读取并打印每个 `font.font_name` 值。

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
