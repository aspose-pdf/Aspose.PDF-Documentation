---
title: 添加自由文本批注
type: docs
weight: 20
url: /zh/python-net/add-free-text-annotation/
description: 此示例加载现有的 PDF 文件，在指定位置向第一页添加自由文本批注，然后保存修改后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加自由文本批注
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 在 PDF 文档中插入自由文本批注。它展示了如何绑定 PDF、定义批注位置、添加自定义文本以及保存更新后的文档。
---

自由文本批注允许您直接在 PDF 页面上放置可见文本，而无需弹出评论。使用 PdfContentEditor，您可以指定批注矩形、显示的文本以及目标页面。

1. 创建 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 绑定输入 PDF。
1. 定义批注位置。
1. 添加自由文本注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1
    )
    # Save updated document
    content_editor.save(outfile)
```
