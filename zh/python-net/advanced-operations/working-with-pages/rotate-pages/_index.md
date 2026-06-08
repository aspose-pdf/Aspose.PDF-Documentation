---
title: 在 Python 中旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 110
url: /zh/python-net/rotate-pages/
description: 学习如何在 Python 中旋转 PDF 页面并更改页面方向。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 旋转 PDF 页面
Abstract: 这篇文章提供了一个指南，介绍如何使用 Python 以编程方式更新或更改现有 PDF 文件中页面的页面方向。利用 Aspose.PDF for Python via .NET，用户可以通过调整页面的 MediaBox 属性轻松在横向和纵向之间切换。文章包含一个 Python 代码片段，演示如何遍历 PDF 文档中的页面，修改它们的 MediaBox 尺寸和位置，并在必要时调整 CropBox。此外，还解释了如何使用 “rotate” 方法设置页面的旋转角度以实现所需的方向。该过程以保存更新后的 PDF 文件结束。
---

本主题描述了如何使用 Python 以编程方式更新或更改现有 PDF 文件中页面的页面方向。

当您需要在纵向和横向之间切换页面方向或对现有 PDF 内容应用旋转角度时，请使用此页面。

## 更改页面方向

此函数会旋转 PDF 的每一页 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用 Aspose.PDF for Python 顺时针旋转 90 度。
它对于纠正页面方向问题非常有用，例如扫描的文档被横向放置。原始 PDF 保持不变，旋转后的版本保存为新文件。

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中更改 PDF 页面大小](/pdf/zh/python-net/change-page-size/)
- [在 Python 中裁剪 PDF 页面](/pdf/zh/python-net/crop-pages/)
- [在 Python 中获取和设置 PDF 页面属性](/pdf/zh/python-net/get-and-set-page-properties/)