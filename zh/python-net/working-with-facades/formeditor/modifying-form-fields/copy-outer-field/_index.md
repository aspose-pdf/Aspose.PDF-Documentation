---
title: 复制外部字段
type: docs
weight: 30
url: /zh/python-net/copy-outer-field/
description: 此示例演示如何使用 Aspose.PDF for Python 将表单字段从一个 PDF 文档复制到另一个 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 从另一个文档复制 PDF 表单字段
Abstract: 本文解释了如何创建一个新的 PDF 文档，将源 PDF 中的 "First Name" 字段复制到第 1 页的坐标 (200, 600) 处，并保存更新后的目标文档。
---

有时，PDF 表单需要在文档之间复用字段。使用 Aspose.PDF for Python，开发者可以通过编程方式将表单字段从源 PDF 复制到目标 PDF。

这 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类提供了 \u0027copy_outer_field\u0027 方法，该方法将在指定页面和坐标处将字段从源文档复制到目标文档。

代码创建一个新的 PDF（目标），添加一个页面，然后将现有 PDF（源）中的字段复制到目标文档的指定坐标处。

1. 创建一个新的目标 PDF 文档。
1. 至少向目标 PDF 添加一页。
1. 保存空的目标文档。
1. 创建一个 FormEditor 对象并将其绑定到目标 PDF。
1. 将源 PDF 中的 'First Name' 字段复制到第 1 页的坐标 (200, 600)。
1. 保存更新后的目标 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**请注意：**

‘copy_outer_field’ 方法签名如下：

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' — 您想要复制的字段。
- 'new_field_name' – 新字段的名称。
- 'page_number' – 新字段将出现的页码。
- x, y – 该页上的坐标。

page_number 应为正整数，对应于 PDF 中已存在的页（基于 1 的索引）。

如果传入负数参数，例如：

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

程序将恢复到之前的参数。
