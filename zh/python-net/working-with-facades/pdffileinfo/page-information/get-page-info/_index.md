---
title: 获取页面信息
type: docs
weight: 10
url: /zh/python-net/get-page-info/
description: 了解如何使用 Aspose.PDF for Python 以编程方式访问 PDF 的页面级信息。本指南展示了如何检索 PDF 文档中特定页面的宽度、高度、旋转角度和偏移量。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python 获取 PDF 页面信息
Abstract: 该函数提取 PDF 页面 的宽度、高度、旋转角度以及水平方向 (X) 和垂直方向 (Y) 的偏移量。这些属性以点为单位返回，反映页面的实际尺寸和 PDF 中内容的位置。函数会打印检索到的数值，使开发者能够了解页面布局和方向，以便进行进一步的 PDF 操作。
---

‘get_page_information’ 实用函数帮助开发者了解 PDF 页面 的结构和布局。每个 PDF 页面可能拥有不同的尺寸、旋转角度和内部偏移，这可能会影响内容放置或自动化任务。

它能够检索 PDF 文件中特定页面的关键元数据和布局信息。Aspose.PDF Facades API 提供诸如页面宽度、高度、旋转角度以及 X/Y 偏移等细节。这些信息对于页面布局分析、注释放置或自动化 PDF 处理等任务至关重要。

1. 创建一个 PDF facade 对象。
1. 检索页面尺寸和布局。
1. 打印或存储检索到的值。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_information(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_width = pdf_info.get_page_width(1)
    page_height = pdf_info.get_page_height(1)
    page_rotation = pdf_info.get_page_rotation(1)
    page_x_offset = pdf_info.get_page_x_offset(1)
    page_y_offset = pdf_info.get_page_y_offset(1)

    print(f"Page Width: {page_width}")
    print(f"Page Height: {page_height}")
    print(f"Page Rotation: {page_rotation}")
```
