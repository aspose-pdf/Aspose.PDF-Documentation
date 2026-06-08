---
title: 按索引移动印章
type: docs
weight: 90
url: /zh/python-net/move-stamp-by-index/
description: 如何使用 Aspose.PDF for Python 通过页面上的索引重新定位 PDF 中的橡胶印章注释
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用基于索引的定位在 PDF 中移动橡胶印章
Abstract: 此示例演示如何使用 Aspose.PDF for Python 通过 Facades API，利用页面上印章的索引重新定位 PDF 中的橡胶印章注释。它重点展示了创建多个印章并为移动操作做好准备。
---

在 PDF 编辑中，可能需要调整现有橡胶印章的位置。此代码片段展示了如何：

- 在同一页面上添加多个印章
- 使用它们的索引准备重新定位。
- 可选地通过指定其页面、索引和新坐标来移动印章。

‘move_stamp(page_number, stamp_index, new_x, new_y)’ 方法可以精确地重新定位印章。

1. 创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 对象。
1. 将 PDF 绑定到编辑器。
1. 向页面添加多个橡胶印章。
1. 在执行移动操作之前保存文档。
1. 根据索引移动特定的印章。
1. 保存更新后的 PDF。

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    content_editor.create_rubber_stamp(
        2,
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
    content_editor.save(outfile)

    # Move first stamp on page 1 by index
    # content_editor.move_stamp(1, 1, 10, 10)
    # Save updated document
    content_editor.save(outfile)
```    
