---
title: 使用 Python 旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 110
url: /zh/python-net/rotate-pages/
description: 本主题描述了如何使用 Python 对现有 PDF 文件的页面方向进行编程旋转。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 旋转 PDF 页面
Abstract: 本文提供了使用 Python 对现有 PDF 文件中的页面方向进行编程更新或更改的指南。通过 Aspose.PDF for Python via .NET，用户可以通过调整页面的 MediaBox 属性轻松在横向和纵向之间切换。文章包含一个 Python 代码片段，演示如何遍历 PDF 文档中的页面，修改其 MediaBox 的尺寸和位置，并在必要时调整 CropBox。此外，还解释了如何使用 'rotate' 方法设置页面的旋转角度以实现所需的方向。该过程以保存更新后的 PDF 文件结束。
---

本主题描述了如何使用 Python 对现有 PDF 文件的页面方向进行编程更新或更改。

## 更改页面方向

此函数使用 Aspose.PDF for Python 将 PDF [`文档`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 的每一页顺时针旋转 90 度。
它对于纠正页面方向问题非常有用，例如扫描的文档横向显示。原始 PDF 保持不变，旋转后的版本保存为新文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_page(infile, outfile):
    """
    Rotate all pages in a PDF document by 90 degrees clockwise.

    Demonstrates how to rotate PDF pages using the Aspose.PDF library.
    This function applies a 90-degree clockwise rotation to every page
    in the input document and saves the result to a new file.

    Args:
        infile (str): Path to the input PDF file to rotate.
        outfile (str): Path where the rotated PDF will be saved.

    Returns:
        None: The function modifies the PDF pages and saves to the output path.

    Note:
        - Applies 90-degree clockwise rotation (ap.Rotation.ON90) to all pages
        - Rotates every page in the document uniformly
        - The original document is not modified; a new file is created
        - Rotation options include: ON90 (90°), ON180 (180°), ON270 (270°)
        - Useful for correcting page orientation or adjusting layout

    Example:
        >>> rotate_page("input.pdf", "rotated_output.pdf")
        # Rotates all pages 90 degrees clockwise and saves to rotated_output.pdf
    """
    document = ap.Document(infile)
    for page in document.pages:
        # `page` is a `Page` object; `rotate` uses the `Rotation` enum
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```


