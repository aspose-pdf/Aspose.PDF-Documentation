---
title: 添加方形注释
type: docs
weight: 60
url: /zh/python-net/add-square-annotation/
description: 本示例绑定一个输入 PDF，在首页添加一个填充的蓝色方形批注，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加方形批注
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加方形批注。它展示了如何定义批注矩形、文本内容、颜色、填充选项，并保存更新后的文档。
---

方形批注通常用于突出显示感兴趣的区域、标记重要章节或在 PDF 文档中提供视觉提示。Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定边界矩形、内容文本、边框颜色、填充选项、页码和边框宽度来创建方形（或圆形）批注。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 定义方形批注。
1. 添加方形批注。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
