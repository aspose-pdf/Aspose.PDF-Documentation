---
title: 移动字段
type: docs
weight: 50
url: /zh/python-net/move-field/
description: 将现有表单字段移动到 PDF 文档中的其他位置。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将 PDF 表单字段移动到新位置
Abstract: 此示例演示如何使用 Aspose.PDF for Python 将现有表单字段移动到 PDF 文档中的其他位置。代码打开现有的 PDF，将指定的表单字段重新定位到新的坐标，并保存更新后的文档。
---

PDF 表单在创建后常常需要进行布局调整。使用 Aspose.PDF for Python，开发人员可以在不重新创建表单字段的情况下将其移动到新位置。

此示例展示了如何通过指定其在页面中的新坐标来重新定位 “Country” 字段。The [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供 move_field 方法以在 PDF 页面内重新定位字段。

1. 打开现有的 PDF 表单。
1. 创建一个 FormEditor 对象。
1. 将 PDF 文档绑定到 FormEditor。
1. 使用坐标将 'Country' 字段移动到新位置。
1. 保存修改后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def move_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Move field to new page
    form_editor.move_field("Country", 200, 600, 280, 620)
    # Save updated document
    form_editor.save(outfile)
```
