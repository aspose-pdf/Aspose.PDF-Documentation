---
title: 添加弹出注释
type: docs
weight: 40
url: /zh/python-net/add-popup-annotation/
description: 此示例加载 PDF，将弹出注释添加到首页，并保存修改后的文档。弹出注释默认设置为可见，并显示指定的评论文本。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 向 PDF 添加弹出注释
Abstract: 此示例演示如何使用 Aspose.PDF for Python 通过 Facades API 在 PDF 文档中插入弹出注释。它说明了如何定义弹出区域、设置注释文本、控制可见性以及保存更新后的文档。
---

弹出注释可用于在 PDF 文件中添加评论、解释或交互式注释。使用 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定位置、内容、可见性和页码以编程方式创建弹出注释。

1. 创建 PdfContentEditor 对象。
1. 绑定输入 PDF。
1. 定义弹出注释矩形。
1. 添加弹出注释。
1. 保存已更新的 Document。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_popup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add popup annotation to page 1
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    # Save updated document
    content_editor.save(outfile)
```
