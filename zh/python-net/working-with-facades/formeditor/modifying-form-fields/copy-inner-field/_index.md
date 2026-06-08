---
title: 复制内部字段
type: docs
weight: 20
url: /zh/python-net/copy-inner-field/
description: 使用 Python（通过 Aspose.PDF for Python）将 PDF 表单字段复制到新位置。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将 PDF 表单字段复制到新位置
Abstract: 本示例演示了如何使用 Aspose.PDF for Python 将 PDF 文档中现有的表单字段复制到新位置。代码打开 PDF，将字段复制到指定的页面和坐标位置，并保存更新后的文档。
---

PDF 表单通常需要在保持原始格式和行为的同时复制字段。使用 Aspose.PDF for Python，开发者可以以编程方式将现有字段复制到同一页或其他页的新的位置。

本文阐述了如何将名为 ‘First Name’ 的字段复制为名为 ‘First Name Copy’ 的新字段，放置在第 2 页的特定坐标 (x=200, y=600)，生成一个包含新位置字段的 PDF。

1. 打开现有的 PDF 表单。
1. 创建一个 FormEditor 对象。
1. 将 PDF 文档绑定到 FormEditor。
1. 将 ‘First Name’ 字段复制到第 2 页坐标为 (200, 600) 的新字段 ‘First Name Copy’。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_inner_field(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_inner_field("First Name", "First Name Copy", 2, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**请注意：**

'copy_inner_field' 方法签名如下：

```python
copy_inner_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' — 您想要复制的字段。
- 'new_field_name' – 新字段的名称。
- 'page_number' – 新字段将出现的页码。
- x, y – 该页上的坐标。

page_number 应为正整数，对应于 PDF 中已存在的页（基于 1 的索引）。

如果传入负数参数，例如：

```python
form_editor.copy_inner_field("First Name", "First Name Copy", -1, 200, 600)
```

程序将恢复到之前的参数。
