---
title: 通过 ID 移动印章
type: docs
weight: 80
url: /zh/python-net/move-stamp-by-id-example/
description: 在本例中，先在第 1 页添加了一个橡胶印章，然后使用其 ID 将其移动到新位置，最后保存更新后的文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中通过 ID 移动 PDF 中的橡胶印章
Abstract: 本例演示了如何使用 Aspose.PDF for Python via the Facades API 在 PDF 中重新定位已有的橡胶印章注释。它展示了如何创建印章，然后通过其 ID 编程移动它。
---

在 PDF 中添加橡胶印章注释后，可能需要调整其位置。'move_stamp_by_id()' 方法允许您基于标识符重新定位印章，而无需重新创建。这在需要动态调整印章放置的自动化工作流中非常有用。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 添加橡胶印章注释。
1. 使用其 ID 移动印章。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_id_example(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(300, 420, 180, 60),
        "Approved",
        "Move this stamp by ID",
        apd.Color.green,
    )

    # Move stamp by ID overload
    content_editor.move_stamp_by_id(1, 1, 240, 360)

    # Save updated document
    content_editor.save(outfile)
```    
