---
title: 按 ID 删除印章
type: docs
weight: 85
url: /zh/python-net/delete-stamp-by-ids-examples/
description:
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 PDF 中按单个或多个 ID 删除橡胶印章
Abstract: 本示例演示了如何使用 Aspose.PDF for Python 通过 Facades API，基于唯一 ID 从 PDF 中删除橡胶印章注释。它涵盖了单 ID 删除和多 ID 删除两种情况。
---

在处理包含多个印章的 PDF 时，通常需要在不影响其他印章的情况下删除特定印章。使用基于 ID 的删除，您可以精准控制要删除的印章：

- 'delete_stamp_by_id(stamp_id, page_number)' – 删除特定页面上按其 ID 的单个印章
- 'delete_stamp_by_ids(page_number, stamp_ids)' – 删除给定页面上按其 ID 的多个印章

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 添加两个具有不同 ID 的橡皮图章。
1. 使用单 ID 和多 ID 删除方法删除图章。
1. 保存更新后的 PDF。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_ids_examples(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Create two stamps on page 1 so they can be deleted by ID
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 320, 180, 60),
        "Draft",
        "Delete by single ID",
        apd.Color.orange,
    )
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(120, 250, 180, 60),
        "Draft",
        "Delete by multiple IDs",
        apd.Color.orange,
    )

    # Delete by single ID overload and by IDs overload
    content_editor.delete_stamp_by_id(1, 1)
    content_editor.delete_stamp_by_ids(1, [2])

    # Save updated document
    content_editor.save(outfile)
```

