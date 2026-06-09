---
title: 添加标记注释
type: docs
weight: 30
url: /zh/python-net/add-markup-annotation/
description: 此示例绑定一个输入 PDF，在首页添加四种不同的标记注释，并保存更新后的文档。每个注释展示了不同的标记样式和颜色。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 在 PDF 中添加高亮、下划线、删除线和波浪线标记注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加多个标记注释—高亮、下划线、删除线和波浪线。示例展示了如何定义注释区域、指定标记类型、应用颜色并保存修改后的文档。
---

标记注释用于在 PDF 中强调或审阅文本。使用 PdfContentEditor，您可以通过指定矩形区域、注释文本、标记类型、页码和颜色，以编程方式应用不同的标记样式。

1. 创建 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 绑定输入 PDF。
1. 定义注释矩形。
1. 添加标记注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(120, 568, 200, 20),
        "This is a strikeout annotation",
        2,
        1,
        apd.Color.orange_red,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 598, 200, 20),
        "This is a squiggly annotation",
        3,
        1,
        apd.Color.dark_blue,
    )
    # Save updated document
    content_editor.save(outfile)
```
