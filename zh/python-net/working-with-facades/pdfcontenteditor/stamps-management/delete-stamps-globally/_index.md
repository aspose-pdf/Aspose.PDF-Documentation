---
title: 全局删除印章
type: docs
weight: 60
url: /zh/python-net/delete-stamps-globally/
description: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 在 PDF 的所有页面上全局删除橡胶印章注释。它展示了如何通过 ID 删除印章，而无需指定单独的页面。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 PdfContentEditor 在 Python 中全局删除 PDF 的橡胶印章
Abstract: 本示例演示如何使用 Aspose.PDF for Python via the Facades API 在 PDF 的所有页面上全局删除橡胶印章注释。它展示了如何通过 ID 删除印章，而无需指定单独的页面。
---

在处理多页文档时，您可能需要在整个文档中删除某些印章。'delete_stamp_by_id()' 和 'delete_stamp_by_ids()' 方法允许您通过标识符全局删除印章，无需手动遍历每一页。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 实例。
1. 绑定输入的 PDF 文档。
1. 在多个页面上添加橡胶印章。
1. 使用其 ID 全局删除印章。
1. 保存更新后的 PDF 文档。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamps_globally(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Add stamps across multiple pages so global deletion is meaningful
    for page in range(1, 5):
        content_editor.create_rubber_stamp(
            page,
            apd.Rectangle(120, 500, 180, 60),
            "Draft",
            "Stamp for global deletion",
            apd.Color.gray,
        )

    # delete_stamp_by_id without page number removes stamp ID from all pages
    content_editor.delete_stamp_by_id(1)
    # delete_stamp_by_ids without page number removes a list of IDs from all pages
    content_editor.delete_stamp_by_ids([2, 3])

    # Save updated document
    content_editor.save(outfile)
```
