---
title: 添加自定义操作链接
type: docs
weight: 20
url: /zh/python-net/add-custom-action-link/
description: 此示例绑定一个输入 PDF，在首页添加自定义操作链接，并保存修改后的文档。为简化起见，使用了空的操作列表，但实际实现可以包含实际的操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中向 PDF 添加自定义操作链接
Abstract: 此示例演示如何使用 Aspose.PDF for Python via the Facades API 向 PDF 文档添加自定义操作链接。它展示了如何在页面上创建可点击区域，分配自定义操作，并保存更新后的文档。
---

自定义操作链接允许您在 PDF 中定义交互区域，点击时可触发特定操作，例如执行脚本、导航页面或运行特定应用程序的命令。Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), 您可以通过指定页面、矩形、颜色和操作来创建自定义操作链接。

1. 创建一个 PdfContentEditor 实例。
1. 绑定输入的 PDF 文档。
1. 为可点击链接定义一个矩形。
1. 指定页码和链接颜色。
1. 分配自定义操作（本示例为空）。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_custom_action_link(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add custom action link. Empty action list keeps the sample runnable
    # without requiring additional enum lookups.
    content_editor.create_custom_action_link(
        apd.Rectangle(200, 500, 260, 20),
        1,
        apd.Color.dark_red,
        [],
    )
    # Save updated document
    content_editor.save(outfile)
```
