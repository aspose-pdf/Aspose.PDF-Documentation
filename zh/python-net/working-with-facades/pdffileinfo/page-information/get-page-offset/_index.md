---
title: 获取页面偏移
type: docs
weight: 20
url: /zh/python-net/get-page-offset/
description: 此示例演示如何使用 PdfFileInfo 获取特定页面的 X 和 Y 偏移量，并将其转换为英寸，以进行精确的布局和定位分析。
lastmod: "2026-06-08"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 获取 PDF 页面偏移
Abstract: ‘get_page_offsets’ 函数提取 PDF 文件中每页的水平 (X) 和垂直 (Y) 偏移量。这些偏移量表示页面内容相对于 PDF 原点的位置。通过将点转换为英寸，该函数提供精确、可读性强的度量，可用于注释、图像或文本的准确放置。它支持多页 PDF，旨在为从事 PDF 布局、自动化或内容对齐任务的开发者提供帮助。
---

‘get_page_offsets’ 函数为开发者提供 PDF 文件中页面的精确水平 (X) 和垂直 (Y) 偏移量。在 PDF 文档中，每页可能拥有不同于页面左上角的内部原点，这会影响文本、图像、注释或其他内容的定位。

通过使用 Aspose.PDF Facades，此函数提取这些以点为单位的偏移量并将其转换为英寸，以便于解释。它支持多页 PDF，使其适用于需要精确内容放置的自动化工作流。

1. 创建 PDF facade 对象。
1. 获取 PDF 的页数。
1. 循环遍历每一页以获取偏移量。
1. 打印或存储偏移量。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_page_offsets(infile):
    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    page_x_offset = pdf_info.get_page_x_offset(1) / 72.0
    page_y_offset = pdf_info.get_page_y_offset(1) / 72.0
    print(f"Page X Offset: {page_x_offset} inches")
    print(f"Page Y Offset: {page_y_offset} inches")
```
