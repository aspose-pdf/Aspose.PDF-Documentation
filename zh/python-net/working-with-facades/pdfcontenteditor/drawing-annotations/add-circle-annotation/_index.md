---
title: 添加圆形注释
type: docs
weight: 10
url: /zh/python-net/add-circle-annotation/
description: 此示例绑定输入 PDF，在首页创建一个圆形注释，并保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加圆形注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加圆形注释。它展示了如何定义注释边界、设置内容文本、配置颜色和外观，并保存更新后的文档。
---

圆形注释对于突出 PDF 文档中感兴趣的区域非常有用。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)，您可以通过指定定义圆形边界的矩形以及注释文本、颜色、填充选项、页码和边框宽度来创建圆形形状。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 定义圆形边界。
1. 添加圆形注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)

    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)

    # Save output PDF file
    content_editor.save(outfile)
```
