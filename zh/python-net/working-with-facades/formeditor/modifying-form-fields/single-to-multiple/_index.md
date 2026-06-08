---
title: 单行字段转换为多行字段
type: docs
weight: 80
url: /zh/python-net/single-to-multiple/
description: 使用 Aspose.PDF for Python 将 PDF 文档中的单行文本字段转换为多行字段。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将 PDF 中的单行文本字段转换为多行字段
Abstract: 本示例演示如何使用 Aspose.PDF for Python 将 PDF 文档中的单行文本字段转换为多行字段。代码加载现有的 PDF 表单，修改指定字段以允许多行文本，并保存更新后的文档。
---

PDF 表单有时包含设计为单行输入的文本字段，这对于某些类型的数据可能不够。使用 Aspose.PDF for Python，开发人员可以轻松地将这些字段转换为多行文本字段，而无需重新创建它们。

使用 [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) 类，开发人员可以修改现有文本字段，而不会影响其位置或其他属性。

1. 加载现有的 PDF 文档。
1. 创建一个 FormEditor 实例。
1. 将 PDF 文档绑定到编辑器。
1. 将选定的字段转换为多行。
1. 保存更新后的文档。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def single2multiple(infile, outfile):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(infile)
    # Change a single-lined text field to a multiple-lined one
    form_editor.single_2_multiple("City")
    # Save updated document
    form_editor.save(outfile)
```

