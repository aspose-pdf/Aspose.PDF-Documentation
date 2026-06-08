---
title: 按 ID 管理印章
type: docs
weight: 95
url: /zh/python-net/manage-stamp-by-id/
description: 如何使用 Aspose.PDF for Python 按唯一 ID 操作 PDF 中的橡胶印章注释
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 中的 PdfContentEditor 按 ID 管理 PDF 中的橡胶印章
Abstract: 本示例演示如何通过 Aspose.PDF for Python 的 Facades API 按唯一 ID 操作 PDF 中的橡胶印章注释。您可以在特定页面隐藏或显示特定印章，而不影响其他印章。
---

在包含多个橡胶印章的 PDF 中，基于 ID 控制各个印章可能很有用。'hide_stamp_by_id()' 和 'show_stamp_by_id()' 方法允许有选择地控制可见性。本示例展示了如何：

- 添加具有唯一 ID 的多个印章
- 隐藏特定页面上的印章
- 在另一页显示印章

通过使用基于 ID 的操作，您可以避免按页面位置或其他属性跟踪印章。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 添加具有特定 ID 的橡皮图章。
1. 根据其 ID 和页码隐藏和显示印章。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def manage_stamp_by_id(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(200, 380, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    content_editor.create_rubber_stamp(
        2,
        apd.Rectangle(200, 480, 180, 60),
        "Draft",
        "Draft stamp for ID-based operations",
        apd.Color.orange,
    )

    # Apply ID-based stamp operations
    content_editor.hide_stamp_by_id(1, 1)
    content_editor.show_stamp_by_id(1, 2)

    # Save updated document
    content_editor.save(outfile)
```
